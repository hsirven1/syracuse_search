#!/usr/bin/env python3
"""Exact, bounded-resource verifier of supplied finite descent certificates."""
import argparse
import json
from pathlib import Path

MAX_BYTES = 1_000_000
MAX_BITS = 256
MAX_DEPTH = 128
MAX_NODES = 4096


def word_data(word):
    """Compose 2^j T^j(n)=A*n+D, bits in chronological order."""
    if not isinstance(word, str) or any(b not in '01' for b in word):
        raise ValueError('word must be a string of 0/1 bits')
    if len(word) > MAX_DEPTH:
        raise ValueError('word exceeds depth limit')
    modulus, a, d, q = 1, 1, 0, 0
    for b in word:
        if b == '1':
            a, d, q = 3*a, 3*d+modulus, q+1
        modulus *= 2
    residue = (-d*pow(a, -1, modulus)) % modulus
    return dict(q=q, A=a, D=d, modulus=modulus, residue=residue)


def intersection(lower, upper, modulus, residue):
    first = lower+(residue-lower) % modulus
    if first > upper:
        return None
    last = upper-(upper-residue) % modulus
    return first, last, (last-first)//modulus+1


def verify(certificate):
    issues = []
    stats = dict(nodes=0, empty_classes=0, certified_integers=0,
                 uncertified_integers=0)

    def issue(code, path, message, witness=None, partial=False):
        item = dict(code=code, path=path, message=message,
                    severity='partial' if partial else 'invalid')
        if witness is not None:
            item['witness'] = witness
        issues.append(item)

    def finish():
        status = ('INVALID' if any(i['severity'] == 'invalid' for i in issues)
                  else 'PARTIAL' if issues else 'VALID')
        return dict(status=status, issues=issues, statistics=stats,
                    scope='Only the supplied finite interval; no global Collatz claim.')

    if not isinstance(certificate, dict) or set(certificate) != {'version', 'interval', 'tree'}:
        issue('SCHEMA', '', 'Expected exactly version, interval, tree')
        return finish()
    if type(certificate['version']) is not int or certificate['version'] != 1:
        issue('SCHEMA', '', 'version must be integer 1')
        return finish()
    bounds = certificate['interval']
    if (not isinstance(bounds, list) or len(bounds) != 2 or
            any(type(n) is not int for n in bounds)):
        issue('INTERVAL', '', 'interval must be two integers (booleans forbidden)')
        return finish()
    lower, upper = bounds
    if not 3 <= lower <= upper:
        issue('INTERVAL', '', 'Require 3 <= lower <= upper')
        return finish()
    if upper.bit_length() > MAX_BITS:
        issue('LIMIT', '', f'Endpoints must have at most {MAX_BITS} bits')
        return finish()

    def visit(node, path):
        stats['nodes'] += 1
        if stats['nodes'] > MAX_NODES:
            issue('LIMIT', path, 'Node limit exceeded')
            return
        if len(path) > MAX_DEPTH:
            issue('LIMIT', path, 'Depth limit exceeded')
            return
        if not isinstance(node, dict):
            issue('SCHEMA', path, 'Node must be an object')
            return
        kind = node.get('kind')
        if not isinstance(kind, str) or kind not in {'split', 'descent', 'empty', 'unproved'}:
            issue('SCHEMA', path, 'Unknown or missing node kind')
            return
        allowed = {'kind', 'word', 'claims'} | ({'children'} if kind == 'split' else set())
        if set(node)-allowed:
            issue('SCHEMA', path, 'Unexpected node fields')
            return
        if 'word' in node and (not isinstance(node['word'], str) or node['word'] != path):
            issue('WORD', path, 'Claimed word differs from the tree path')
            return
        data = word_data(path)
        if 'claims' in node:
            claims = node['claims']
            if (not isinstance(claims, dict) or set(claims)-set(data) or
                    any(type(v) is not int for v in claims.values())):
                issue('CLAIMS', path, 'Claims must be known integer fields')
                return
            for key, value in claims.items():
                if value != data[key]:
                    issue('CLAIM_MISMATCH', path,
                          f'{key}: claimed {value}, recomputed {data[key]}')
                    return
        members = intersection(lower, upper, data['modulus'], data['residue'])
        if kind == 'split':
            children = node.get('children')
            if not isinstance(children, dict) or set(children)-{'0', '1'}:
                issue('SCHEMA', path, 'split requires children keyed by 0 and/or 1')
                return
            if len(path) == MAX_DEPTH:
                issue('LIMIT', path, 'Cannot split at maximum depth')
                return
            for bit in '01':
                if stats['nodes'] >= MAX_NODES and bit in children:
                    issue('LIMIT', path+bit, 'Node limit exceeded')
                    return
                if bit in children:
                    visit(children[bit], path+bit)
                else:
                    child = word_data(path+bit)
                    remaining = intersection(lower, upper, child['modulus'], child['residue'])
                    if remaining is None:
                        stats['empty_classes'] += 1
                    else:
                        stats['uncertified_integers'] += remaining[2]
                        issue('MISSING_BRANCH', path+bit, 'Omitted branch is nonempty',
                              remaining[0], partial=True)
            return
        if kind == 'empty' and members is not None:
            issue('FALSE_EMPTY', path, 'Claimed empty class has a member', members[0])
            return
        if members is None:
            stats['empty_classes'] += 1
            return
        first, last, count = members
        if kind == 'unproved':
            stats['uncertified_integers'] += count
            issue('UNPROVED', path, 'Nonempty class lacks a descent proof', first, partial=True)
            return
        gap = data['modulus']-data['A']
        worst = first if gap >= 0 else last
        margin = gap*worst-data['D']
        if margin <= 0:
            issue('NON_STRICT_DESCENT', path,
                  f'Worst affine margin is {margin}, must be > 0', worst)
            return
        stats['certified_integers'] += count

    visit(certificate['tree'], '')
    if not issues and stats['certified_integers'] != upper-lower+1:
        issue('INTERNAL_COVERAGE', '', 'Certified count differs from interval size')
    return finish()


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'Duplicate JSON key: {key}')
        result[key] = value
    return result


def load_certificate(path):
    with Path(path).open('rb') as source:
        raw = source.read(MAX_BYTES+1)
    if len(raw) > MAX_BYTES:
        raise ValueError('JSON file exceeds byte limit')

    def reject_constant(value):
        raise ValueError(f'Non-finite JSON constant: {value}')

    return json.loads(raw.decode('utf-8'), object_pairs_hook=_unique_object,
                      parse_constant=reject_constant)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    args = parser.parse_args(argv)
    try:
        result = verify(load_certificate(args.certificate))
    except (OSError, ValueError, RecursionError) as exc:
        result = dict(status='INVALID', issues=[dict(code='INPUT', message=str(exc))])
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return {'VALID': 0, 'PARTIAL': 2, 'INVALID': 1}[result['status']]


if __name__ == '__main__':
    raise SystemExit(main())
