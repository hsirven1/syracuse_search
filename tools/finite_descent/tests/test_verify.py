import copy
import importlib.util
import itertools
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('finite_verify', ROOT/'verify.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def direct(n, steps):
    bits = ''
    for _ in range(steps):
        b = n % 2
        bits += str(b)
        n = (3*n+1)//2 if b else n//2
    return n, bits


def load_example(name='valid_3_4.json'):
    return v.load_certificate(ROOT/'examples'/name)


class VerifierTests(unittest.TestCase):
    def test_reference(self):
        result = v.verify(load_example())
        self.assertEqual(result['status'], 'VALID')
        self.assertEqual(result['statistics']['certified_integers'], 2)
        self.assertEqual(result['statistics']['empty_classes'], 3)
        self.assertEqual(direct(3, 4), (2, '1100'))
        self.assertEqual(direct(4, 1), (2, '0'))

    def test_missing_nonempty_is_partial(self):
        r = v.verify(load_example('partial_missing_branch.json'))
        self.assertEqual(r['status'], 'PARTIAL')
        self.assertEqual(r['issues'][0]['code'], 'MISSING_BRANCH')
        self.assertEqual(r['issues'][0]['witness'], 3)
        self.assertEqual(r['statistics']['uncertified_integers'], 1)

    def test_false_empty(self):
        r = v.verify(load_example('invalid_false_empty.json'))
        self.assertEqual(r['status'], 'INVALID')
        self.assertEqual(r['issues'][0]['code'], 'FALSE_EMPTY')

    def test_claims_recomputed(self):
        for key in ('A', 'D', 'q', 'modulus', 'residue'):
            with self.subTest(key=key):
                c = load_example()
                c['tree']['children']['0']['claims'][key] += 1
                r = v.verify(c)
                self.assertEqual(r['status'], 'INVALID')
                self.assertEqual(r['issues'][0]['code'], 'CLAIM_MISMATCH')

    def test_bad_word(self):
        for word in ('1', 'x', 0):
            c = load_example()
            c['tree']['children']['0']['word'] = word
            self.assertEqual(v.verify(c)['status'], 'INVALID')

    def test_nonstrict_equality(self):
        r = v.verify(load_example('invalid_nonstrict.json'))
        self.assertEqual(r['status'], 'INVALID')
        self.assertEqual(r['issues'][0]['witness'], 3)
        self.assertIn('margin is 0', r['issues'][0]['message'])

    def test_expanding_word_worst_endpoint(self):
        c = dict(version=1, interval=[3, 7], tree=dict(kind='split', children={
            '0':dict(kind='unproved'), '1':dict(kind='descent')}))
        r = v.verify(c)
        self.assertEqual(r['status'], 'INVALID')
        self.assertEqual(r['issues'][-1]['witness'], 7)

    def test_unproved_root(self):
        r = v.verify(dict(version=1,interval=[3,4],tree=dict(kind='unproved')))
        self.assertEqual(r['status'],'PARTIAL')
        self.assertEqual(r['statistics']['uncertified_integers'],2)

    def test_empty_explicit_and_unproved(self):
        c = load_example()
        c['tree']['children']['1']['children']['0'] = dict(kind='empty',word='10')
        self.assertEqual(v.verify(c)['status'], 'VALID')
        c['tree']['children']['0'] = dict(kind='unproved')
        self.assertEqual(v.verify(c)['status'], 'PARTIAL')

    def test_empty_claim_is_not_ignored(self):
        c = load_example()
        c['tree']['children']['1']['children']['0'] = dict(kind='empty',claims={'D':999})
        self.assertEqual(v.verify(c)['status'], 'INVALID')

    def test_intervals(self):
        for bounds in ([4,3], [0,4], [True,4], [3,4.0], [], [3], [3,2**256]):
            c = load_example()
            c['interval'] = bounds
            self.assertEqual(v.verify(c)['status'], 'INVALID')

    def test_schema(self):
        for c in (None, [], {}, {'version':1}, dict(version=True, interval=[3,4],tree={})):
            self.assertEqual(v.verify(c)['status'], 'INVALID')
        for node in (None, {}, {'kind':[]}, {'kind':'bogus'},
                     {'kind':'descent','children':{}}, {'kind':'split'},
                     {'kind':'split','children':[]},
                     {'kind':'split','children':{'2':{}}}):
            c = dict(version=1,interval=[3,4],tree=node)
            self.assertEqual(v.verify(c)['status'], 'INVALID')

    def test_claim_schema(self):
        for claims in ([], {'A':True}, {'D':0.0}, {'unknown':1}):
            c = load_example()
            c['tree']['children']['0']['claims'] = claims
            self.assertEqual(v.verify(c)['status'], 'INVALID')

    def test_depth_limit(self):
        node = dict(kind='unproved')
        for _ in range(v.MAX_DEPTH+1):
            node = dict(kind='split',children={'0':node})
        r = v.verify(dict(version=1, interval=[3,4],tree=node))
        self.assertEqual(r['status'], 'INVALID')
        self.assertTrue(any(i['code']=='LIMIT' for i in r['issues']))

    def test_node_limit(self):
        # Parser/verifier resource control on an empty subtree, not a search.
        node = dict(kind='empty')
        for _ in range(12):
            node = dict(kind='split', children={'0':copy.deepcopy(node),'1':copy.deepcopy(node)})
        r = v.verify(dict(version=1,interval=[3,4],tree=node))
        self.assertEqual(r['status'], 'INVALID')
        self.assertTrue(any(i['code']=='LIMIT' for i in r['issues']))
        self.assertLessEqual(r['statistics']['nodes'], v.MAX_NODES)

    def test_intersections_against_small_lists(self):
        for low, high in ((3,3),(3,4),(4,19),(31,65)):
            for j in range(7):
                for residue in range(2**j):
                    actual = [n for n in range(low,high+1) if n % 2**j == residue]
                    expected = None if not actual else (actual[0],actual[-1],len(actual))
                    self.assertEqual(v.intersection(low,high,2**j,residue),expected)

    def test_words_against_independent_iteration(self):
        controls = 0
        for j in range(7):
            for bits in itertools.product('01',repeat=j):
                word = ''.join(bits)
                data = v.word_data(word)
                self.assertEqual(data['A'],3**word.count('1'))
                for n in range(3,81):
                    endpoint, actual = direct(n,j)
                    realizes = n % data['modulus'] == data['residue']
                    self.assertEqual(realizes,actual==word)
                    if realizes:
                        self.assertEqual(data['modulus']*endpoint,data['A']*n+data['D'])
                    controls += 1
        self.assertEqual(controls,9906)

    def test_reference_tree_against_direct_small_intervals(self):
        # Reuse the supplied tree, do not seek or synthesize certificates.
        for low in range(3,13):
            for high in range(low,13):
                c = load_example()
                c['interval'] = [low,high]
                r = v.verify(c)
                for n in range(low,high+1):
                    if n % 2 == 0:
                        self.assertLess(direct(n,1)[0],n)
                    elif n % 16 == 3:
                        self.assertLess(direct(n,4)[0],n)
                fully_covered = all(n%2==0 or n%16==3 for n in range(low,high+1))
                self.assertEqual(r['status'],'VALID' if fully_covered else 'PARTIAL')

    def test_invalid_dominates_partial(self):
        c = load_example('partial_missing_branch.json')
        c['tree']['children']['0']['claims']['D'] = 123
        self.assertEqual(v.verify(c)['status'],'INVALID')

    def test_duplicate_json_key(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/'x.json'
            p.write_text('{"version":1,"version":1}')
            with self.assertRaisesRegex(ValueError,'Duplicate'):
                v.load_certificate(p)

    def test_duplicate_branch_key(self):
        raw = '{"version":1,"interval":[3,4],"tree":{"kind":"split",' \
              '"children":{"0":{"kind":"descent"},"0":{"kind":"empty"}}}}'
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/'x.json'
            p.write_text(raw)
            with self.assertRaisesRegex(ValueError,'Duplicate JSON key: 0'):
                v.load_certificate(p)

    def test_file_size_and_json_constants(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/'x.json'
            p.write_bytes(b' '*(v.MAX_BYTES+1))
            with self.assertRaisesRegex(ValueError,'byte limit'):
                v.load_certificate(p)
            for raw in ('NaN','Infinity','{','\udcff'):
                p.write_bytes(raw.encode('utf-8',errors='surrogatepass'))
                with self.assertRaises(ValueError):
                    v.load_certificate(p)

    def test_cli_statuses_and_input_errors(self):
        for name, status, code in (
            ('valid_3_4.json','VALID',0),
            ('partial_missing_branch.json','PARTIAL',2),
            ('invalid_correction.json','INVALID',1),
            ('invalid_nonstrict.json','INVALID',1),
            ('invalid_false_empty.json','INVALID',1)):
            r = subprocess.run([sys.executable,str(ROOT/'verify.py'),str(ROOT/'examples'/name)],
                               capture_output=True,text=True)
            self.assertEqual(r.returncode,code,r.stderr)
            self.assertEqual(json.loads(r.stdout)['status'],status)
        r = subprocess.run([sys.executable,str(ROOT/'verify.py'),str(ROOT/'absent.json')],
                           capture_output=True,text=True)
        self.assertEqual(r.returncode,1)
        self.assertEqual(json.loads(r.stdout)['status'],'INVALID')


if __name__ == '__main__':
    unittest.main()
