"""One deterministic adversarial campaign; no search for a new theorem."""
import copy
import importlib.util
import itertools
import json
from pathlib import Path
import random
import subprocess
import sys
import tempfile
import unittest

from independent_oracle import classify, iterate, metadata, read_json

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('reviewed_verifier',ROOT/'verify.py')
sut = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sut)


def leaf(kind):
    return {'kind':kind}


def small_shapes(depth):
    base = [leaf(k) for k in ('descent','empty','unproved')]
    if not depth:
        return base
    children = [None]+small_shapes(depth-1)
    for left, right in itertools.product(children,repeat=2):
        base.append(dict(kind='split',children={b:copy.deepcopy(v)
                    for b,v in zip('01',(left,right)) if v is not None}))
    return base


def random_tree(rng, depth=0):
    if depth == 8 or rng.random() < 0.45:
        return leaf(rng.choice(('descent','empty','unproved')))
    return dict(kind='split',children={b:random_tree(rng,depth+1)
                                     for b in '01' if rng.random() < 0.85})


def nodes(tree, path=''):
    yield path, tree
    if tree.get('kind') == 'split':
        for b, child in tree['children'].items():
            yield from nodes(child,path+b)


def at(tree, path):
    for b in path:
        tree = tree['children'][b]
    return tree


class AdversarialAudit(unittest.TestCase):
    def test_deterministic_campaign(self):
        counts, statuses = {}, {'VALID':0,'PARTIAL':0,'INVALID':0}

        def compare(doc, phase):
            expected, witnesses = classify(doc)
            actual = sut.verify(doc)
            counts[phase] = counts.get(phase,0)+1
            statuses[actual['status']] += 1
            self.assertEqual(actual['status'],expected,
                             json.dumps(doc,sort_keys=True))
            if actual['status'] == 'VALID':
                self.assertEqual(sorted(witnesses),list(range(doc['interval'][0],doc['interval'][1]+1)))
                self.assertEqual(actual['statistics']['certified_integers'],len(witnesses))

        reference = read_json((ROOT/'examples/valid_3_4.json').read_text())
        for path in sorted((ROOT/'examples').glob('*.json')):
            compare(read_json(path.read_text()),'provided_examples')
        intervals = [(n,n) for n in range(3,13)]+[(3,4),(3,8),(4,9),(9,12)]
        shapes = small_shapes(2)
        self.assertEqual(len(shapes),403)
        for shape in shapes:
            for interval in intervals:
                compare(dict(version=1,interval=list(interval),tree=shape),'exhaustive_depth2')
        rng = random.Random(190018)
        for _ in range(1000):
            low = rng.randrange(3,41)
            high = rng.randrange(low,41)
            compare(dict(version=1,interval=[low,high],tree=random_tree(rng)),
                    'seeded_depth8')
        # Exercise every location of the supplied tree, including empty branches.
        rich = copy.deepcopy(reference)
        for path, node in list(nodes(rich['tree'])):
            node['word'] = path
            node['claims'] = metadata(path).copy()
        compare(rich,'annotated_reference')
        for path, node in list(nodes(rich['tree'])):
            for field in ('q','A','D','modulus','residue'):
                doc = copy.deepcopy(rich)
                at(doc['tree'],path)['claims'][field] += 1
                compare(doc,'mutated_claims')
            for value in ('x',path+'0',True,None):
                doc = copy.deepcopy(rich)
                at(doc['tree'],path)['word'] = value
                compare(doc,'mutated_words')
            for replacement in (None,{},dict(kind=[]),dict(kind='empty'),
                                dict(kind='unproved'),dict(kind='split',children={}),
                                dict(kind='descent',children={})):
                doc = copy.deepcopy(rich)
                if path:
                    at(doc['tree'],path[:-1])['children'][path[-1]] = replacement
                else:
                    doc['tree'] = replacement
                compare(doc,'mutated_nodes')
        for path in ('10','111','1101'):
            for claims in (metadata(path),dict(D=999),dict(D=True),dict(D=0.0)):
                doc = copy.deepcopy(reference)
                at(doc['tree'],path[:-1])['children'][path[-1]] = dict(kind='empty',claims=claims)
                compare(doc,'empty_branch_claims')
        # Independent direct residue and closed-sum data, then false residues.
        for length in range(7):
            for bits in itertools.product('01',repeat=length):
                word = ''.join(bits)
                tree = dict(kind='descent',word=word,claims=metadata(word))
                for b in reversed(word):
                    tree = dict(kind='split',children={b:tree})
                for n in (3,4,5,7,8,15,16,40):
                    doc = dict(version=1,interval=[n,n],tree=tree)
                    compare(doc,'word_frontiers')
                doc = copy.deepcopy(doc)
                at(doc['tree'],word)['claims']['residue'] += 1
                compare(doc,'false_residues')
        malformed = [None, [], {}, dict(reference,extra=1),dict(reference,version=True)]
        for bounds in ([],[4,3],[2,4],[True,4],[3,4.0]):
            malformed.append(dict(reference,interval=bounds))
        for child in ([],None,{'2':leaf('descent')},{'0':None}):
            malformed.append(dict(version=1,interval=[3,4],tree=dict(kind='split',children=child)))
        for doc in malformed:
            compare(doc,'schema_cases')

        # File/API limits and parse behavior outside the enumerating oracle's scope.
        limits = [dict(reference,interval=[3,2**256])]
        node = leaf('unproved')
        for _ in range(129):
            node = dict(kind='split',children={'0':node})
        limits.append(dict(version=1,interval=[3,4],tree=node))
        node = leaf('empty')
        for _ in range(12):
            node = dict(kind='split',children={'0':copy.deepcopy(node),'1':copy.deepcopy(node)})
        limits.append(dict(version=1,interval=[3,4],tree=node))
        for doc in limits:
            self.assertEqual(sut.verify(doc)['status'],'INVALID')
        counts['resource_API_cases'] = len(limits)
        with tempfile.TemporaryDirectory() as tmp:
            raw_cases = [
                '{"version":1,"version":1}',
                '{"version":1,"interval":[3,4],"tree":{"kind":"split","children":{"0":{},"0":{}}}}',
                '{"version":1,"interval":[3,4],"tree":{"kind":"descent","claims":{"D":0,"D":1}}}',
                'NaN','Infinity','{', '1'*5000,
                '{"x":'+'['*1100+'0'+']'*1100+'}',
                ' '*(1_000_001)]
            for i, raw in enumerate(raw_cases):
                file = Path(tmp)/f'{i}.json'
                file.write_text(raw)
                run = subprocess.run([sys.executable,str(ROOT/'verify.py'),str(file)],
                                     capture_output=True,text=True,timeout=5)
                self.assertEqual(run.returncode,1,run.stderr)
                self.assertEqual(json.loads(run.stdout)['status'],'INVALID')
                self.assertNotIn('Traceback',run.stderr)
            # The five delivered CLI examples are checked against the oracle.
            for file in sorted((ROOT/'examples').glob('*.json')):
                expected, _ = classify(read_json(file.read_text()))
                run = subprocess.run([sys.executable,str(ROOT/'verify.py'),str(file)],
                                     capture_output=True,text=True,timeout=5)
                self.assertEqual(run.returncode,{'VALID':0,'INVALID':1,'PARTIAL':2}[expected])
                self.assertEqual(json.loads(run.stdout)['status'],expected)
            counts['CLI_cases'] = len(raw_cases)+5
        report = dict(status='PASS', seed=190018, cases=counts,
                      oracle_comparison_statuses=statuses,
                      oracle_comparisons=sum(statuses.values()),
                      false_VALID_found=0, status_disagreements=0,
                      mathematical_search=False)
        print('\nAUDIT_RESULT='+json.dumps(report,sort_keys=True))


if __name__ == '__main__':
    unittest.main()
