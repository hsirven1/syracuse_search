"""Independent exact checks; input scripts are replayed separately in a copy.
Run: python3 audit_collatz/test_experience36.py [--zip PATH]
No inferred assertion about an infinite orbit or scientific priority.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse
import csv
import hashlib
import json
from math import isqrt
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent
COUNTS = {}
WITNESSES = {}


def data(word):
    s, c = 0, 0
    for a in word:
        c = 3*c + 2**s
        s += a
    modulus = 2**(s+1)
    return ((2**s-c)*pow(3**len(word), -1, modulus)) % modulus, modulus


def trajectory(n, word):
    out = [n]
    for a in word:
        z = 3*n+1
        assert (z & -z).bit_length()-1 == a
        n = z//2**a
        assert n > 0 and n % 2 == 1
        out.append(n)
    return out


def shadow(word):
    # Forward affine accumulation, unlike the supplied reverse-inverse sum.
    c, s = 0, 0
    for a in word:
        c, s = 3*c + 2**s, s+a
    return c*pow(2**s, -1, 3**len(word)) % 3**len(word)


def direct_sum(word):
    m, total, exponent = 3**len(word), 0, 0
    for j, a in enumerate(reversed(word)):
        exponent += a
        total += 3**j*pow(2, -exponent, m)
    return total % m


def oscillating_control(N):
    floors, power = [0], 1
    for _ in range(N):
        power *= 3
        floors.append(power.bit_length()-1)
    d = [0]+[floors[i]-floors[i-1] for i in range(1, N+1)]
    jumps, previous, j = [], 0, 1
    while True:
        t = max(previous+1, isqrt(2**j))
        while t <= N and d[t] != 2:
            t += 1
        if t > N:
            break
        jumps.append(t); previous = t; j += 1
    state, baseline, a, b = 0x2545F4914F6CDD1D, 0, [], [0]
    jump_set = set(jumps)
    for t in range(1, N+1):
        state ^= (state << 13) & (2**64-1)
        state ^= state >> 7
        state ^= (state << 17) & (2**64-1)
        baseline += int(t in jump_set)
        bt = baseline+((state & 1) if d[t] == 2 and t not in jump_set else 0)
        a.append(d[t]-(bt-b[-1])); b.append(bt)
    return a, b, jumps


class Experience36Audit(unittest.TestCase):
    def test_all_suffixes_and_exact_indices(self):
        cases = 0
        for length in range(1, 7):
            for word in product(range(1, 5), repeat=length):
                r, modulus = data(word)
                self.assertEqual(r % 2, 1)
                for q in (0, 1):  # also test the canonical seed, omitted in random replay
                    ns = trajectory(r+q*modulus, word)
                    for t in range(1, length+1):
                        for k in range(1, t+1):
                            w = word[t-k:t]
                            A = sum(w)
                            # Exact rational unrolling includes the nonzero discarded tail.
                            rhs = sum((Fraction(3**j, 2**sum(w[-j-1:]))
                                       for j in range(k)), Fraction())
                            self.assertEqual(Fraction(ns[t]),
                                             Fraction(3**k*ns[t-k], 2**A)+rhs)
                            self.assertEqual(ns[t] % 3**k, shadow(w))
                            self.assertEqual(shadow(w), direct_sum(w))
                            cases += 1
        COUNTS['suffix_checks_two_realizers'] = cases

    def test_terminal_bit_is_essential(self):
        # Dropping +1 in 2^(S+1) loses the parity of the final state.
        self.assertEqual((3*1+1) % 2, 0)
        self.assertNotEqual((3*1+1) % 4, 2)
        self.assertEqual((3*1+1 & -(3*1+1)).bit_length()-1, 2)
        WITNESSES['missing_terminal_bit'] = dict(n0=1, prescribed_a=[1], actual_a=[2])

    def test_critical_word_translation_to_shortcut_parities(self):
        checks = 0
        for N in (1, 2, 10, 100):
            clocks = [(3**i).bit_length()-1 for i in range(N+1)]
            a = tuple(clocks[i]-clocks[i-1] for i in range(1, N+1))
            r, _ = data(a)
            n = r
            def floor_beta(t):
                # floor(t log_3(2)), using powers only.
                m = 0
                while 3**(m+1) <= 2**t:
                    m += 1
                return m
            for t in range(clocks[-1]+1):
                if t == 0:
                    self.assertEqual(n % 2, 1)
                    self.assertEqual(floor_beta(1)-floor_beta(0), 0)
                else:
                    self.assertEqual(n % 2, floor_beta(t+1)-floor_beta(t))
                    checks += 1
                n = (3*n+1)//2 if n % 2 else n//2
        COUNTS['critical_shortcut_translation_checks'] = checks

    def test_mutations_are_detected(self):
        w = (1, 4)
        ns = trajectory(3, w)
        self.assertEqual(ns, [3, 5, 1])
        self.assertEqual(shadow(w), 1)
        self.assertEqual(direct_sum(tuple(reversed(w))), 2)
        self.assertEqual(3*shadow(w) % 9, 3)
        self.assertNotEqual(ns[-1], Fraction(1, 16)+Fraction(3, 32))
        WITNESSES['reversed_suffix'] = dict(n0=3, a=[1, 4], t=2, k=2,
                                            correct=1, reversed=2, shifted_power=3)
        self.assertNotEqual(shadow((1, 1)), shadow((1, 3)))
        WITNESSES['valuation_parities_insufficient_mod9'] = {
            'words': [[1, 1], [1, 3]], 'residues': [shadow((1, 1)), shadow((1, 3))]}
        self.assertEqual(trajectory(3, (1,))[-1] % 9, 5)
        self.assertEqual(trajectory(7, (1,))[-1] % 9, 2)
        WITNESSES['k_greater_than_t'] = dict(t=1, k=2, same_valuations=[1],
                                           seeds=[3, 7], endpoints_mod9=[5, 2])

    def test_height_and_global_redundancy(self):
        count = 0
        for length in range(1, 10):
            for word in product((1, 2), repeat=length):
                sums, s = [0], 0
                for a in word:
                    s += a
                    sums.append(s)
                b = [(3**i).bit_length()-1-sums[i] for i in range(length+1)]
                if min(b) < 0:
                    continue
                r, modulus = data(word)
                for q in (0, 1):
                    ns = trajectory(r+q*modulus, word)
                    for t in range(1, length+1):
                        upper = 2**(b[t]+1)*(r+q*modulus+Fraction(t, 3))
                        self.assertLess(ns[t], upper)
                        for k in range(1, t+1):
                            rho = shadow(word[t-k:t])
                            bound = Fraction(rho, 2**(b[t]+1))-Fraction(t, 3)
                            lower = max(1, bound.numerator//bound.denominator+1)
                            self.assertLess(bound, r+q*modulus)
                            # Universal redundancy versus the full-prefix canonical seed.
                            self.assertLessEqual(lower, r)
                            count += 1
        COUNTS['height_checks_two_realizers'] = count

    def test_replay_is_identical_to_supplied_results(self):
        original = ROOT/'experience36_source'
        with tempfile.TemporaryDirectory(prefix='exp36-replay-') as directory:
            replay = Path(directory)
            for src in original.glob('*.py'):
                shutil.copyfile(src, replay/src.name)
            for name in ('verify_dual_residues.py', 'shadow_height.py'):
                subprocess.run([sys.executable, str(replay/name)], cwd=replay,
                               check=True, capture_output=True, text=True)
            self.assertEqual(json.loads((original/'results.json').read_text()),
                             json.loads((replay/'results.json').read_text()))
            for name in ('critical_prefixes.csv', 'shadow_height.csv'):
                with (original/name).open() as f, (replay/name).open() as g:
                    self.assertEqual(list(csv.DictReader(f)), list(csv.DictReader(g)))
        COUNTS['reproduced_artifacts'] = 3

    def test_distinct_control_generators(self):
        # Execute definitions only: the supplied source is already reviewed.
        import importlib.util
        def module(name):
            p = ROOT/'experience36_source'/name
            spec = importlib.util.spec_from_file_location('audit_'+p.stem, p)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            return m
        osc = module('test_oscillations.py')
        _, direct, bd, jumps = osc.build(1000)
        # Reconstruct the explicitly documented second generator independently.
        alt, b, independent_jumps = oscillating_control(1000)
        self.assertEqual(sorted(jumps), independent_jumps)
        first = next(i+1 for i, (x, y) in enumerate(zip(direct, alt)) if x != y)
        self.assertNotEqual(direct, alt)
        COUNTS['generator_first_difference'] = first
        WITNESSES['distinct_generators'] = dict(first_difference=first,
                                                direct_a=direct[first-1], replay_a=alt[first-1],
                                                direct_seed_bits=data(direct)[0].bit_length(),
                                                replay_seed_bits=data(alt)[0].bit_length())

    def test_narrow_candidate_at_first_24_jump_times(self):
        a, b, jumps = oscillating_control(5000)
        rows = []
        for j, t in enumerate(jumps, 1):
            r, _ = data(a[:t])
            rows.append(dict(j=j, J_j=t, canonical_bits=r.bit_length(),
                             conjectured_lower_bound_holds=r >= 2**j))
        self.assertEqual(len(rows), 24)
        self.assertTrue(all(row['conjectured_lower_bound_holds'] for row in rows))
        COUNTS['candidate_jump_times_checked'] = len(rows)
        WITNESSES['candidate_finite_search'] = rows


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--zip', type=Path)
    args = parser.parse_args()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Experience36Audit)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    report = {'tests_run': result.testsRun, 'failures': len(result.failures),
              'errors': len(result.errors), 'counts': COUNTS, 'witnesses': WITNESSES,
              'zip_sha256': hashlib.sha256(args.zip.read_bytes()).hexdigest() if args.zip else None}
    (ROOT/'logs/exp36_independent.json').write_text(json.dumps(report, indent=2)+'\n')
    raise SystemExit(not result.wasSuccessful())
