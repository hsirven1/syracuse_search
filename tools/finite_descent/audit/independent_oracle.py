"""Small-domain oracle. No imports from the implementation under review."""
from collections import Counter
from functools import lru_cache
import json


class OutsideScope(ValueError):
    pass


def iterate(seed, length):
    current, bits = seed, ''
    for _ in range(length):
        bits += '1' if current % 2 else '0'
        current = (3*current+1)//2 if current % 2 else current//2
    return current, bits


@lru_cache(None)
def metadata(word):
    # Directly construct the residue table from actual dynamics (<=256 seeds).
    residues = [n for n in range(2**len(word))
                if iterate(n, len(word))[1] == word]
    if len(residues) != 1:
        raise AssertionError('Parity coding failed in independent enumeration')
    positions = [i for i, bit in enumerate(word) if bit == '1']
    q = len(positions)
    correction = sum(2**i*3**(q-1-rank) for rank, i in enumerate(positions))
    return dict(q=q, A=3**q, D=correction,
                modulus=2**len(word), residue=residues[0])


def read_json(raw):
    def object_from_pairs(pairs):
        if any(n > 1 for n in Counter(k for k, _ in pairs).values()):
            raise ValueError('duplicate key')
        return dict(pairs)

    def reject(value):
        raise ValueError(value)

    return json.loads(raw, object_pairs_hook=object_from_pairs, parse_constant=reject)


def classify(document):
    """Classify small JSON-compatible objects by visiting actual trajectories."""
    bad, missing = [], []
    witnessed = []
    if not isinstance(document, dict) or set(document) != {'version','interval','tree'}:
        return 'INVALID', witnessed
    if type(document['version']) is not int or document['version'] != 1:
        return 'INVALID', witnessed
    bounds = document['interval']
    if (not isinstance(bounds,list) or len(bounds) != 2 or
            not all(type(n) is int for n in bounds) or not 3 <= bounds[0] <= bounds[1]):
        return 'INVALID', witnessed
    lo, hi = bounds
    if hi > 40:
        raise OutsideScope('Oracle enumerates only intervals inside [3,40]')

    def inspect(node, path, seeds):
        if len(path) > 8:
            raise OutsideScope('Oracle supports depth <=8')
        if not isinstance(node, dict):
            bad.append('node')
            return
        kind = node.get('kind')
        if not isinstance(kind,str) or kind not in ('split','empty','descent','unproved'):
            bad.append('kind')
            return
        permitted = {'kind','word','claims'}
        if kind == 'split':
            permitted.add('children')
        if any(key not in permitted for key in node):
            bad.append('fields')
            return
        if 'word' in node and (type(node['word']) is not str or node['word'] != path):
            bad.append('word')
            return
        if 'claims' in node:
            claims = node['claims']
            actual = metadata(path)
            if (not isinstance(claims,dict) or
                    any(k not in actual or type(v) is not int or v != actual[k]
                        for k,v in claims.items())):
                bad.append('claims')
                return
        if kind == 'split':
            kids = node.get('children')
            if not isinstance(kids,dict) or any(k not in ('0','1') for k in kids):
                bad.append('children')
                return
            for b in ('0','1'):
                # Actual current state at this depth; no congruence formula.
                child_seeds = [n for n in seeds
                               if str(iterate(n,len(path))[0] % 2) == b]
                if b in kids:
                    inspect(kids[b],path+b,child_seeds)
                elif child_seeds:
                    missing.extend(child_seeds)
            return
        if kind == 'empty' and seeds:
            bad.append('false empty')
        elif kind == 'unproved':
            missing.extend(seeds)
        elif kind == 'descent':
            for n in seeds:
                endpoint, bits = iterate(n,len(path))
                if bits != path or endpoint >= n:
                    bad.append('failed descent')
                else:
                    witnessed.append(n)

    inspect(document['tree'],'',list(range(lo,hi+1)))
    if bad:
        return 'INVALID', witnessed
    if missing:
        return 'PARTIAL', witnessed
    if sorted(witnessed) != list(range(lo,hi+1)):
        raise AssertionError('Oracle coverage accounting failed')
    return 'VALID', witnessed
