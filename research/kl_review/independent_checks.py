"""Exact checks of the candidate model, NOT a transcription certified from KL 2003.

No import of kl_strict_monotonicity_audit.py or upstream KL implementation.
Fibers are solved as congruences 3v = 4m-2 / 2m-1, without quotient indices.
Run from any directory; stdlib only. JSON records finite scope explicitly.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from random import Random
import json
import unittest

OUT = Path(__file__).resolve().parent
COUNTS = {}
WITNESSES = {}


def residues(k):
    return tuple(m for m in range(3**k) if m % 3 == 2)


def rows(k):
    p, ids = 3**k, residues(k)
    result = {}
    for m in ids:
        target, branch = ((4*m-2, 1) if m % 9 == 2 else
                          (2*m-1, 2) if m % 9 == 8 else (0, 0))
        fiber = tuple(v for v in ids if (3*v-target) % p == 0) if branch else ()
        if branch:
            assert len(fiber) == 3
        result[m] = (4*m % p, branch, fiber)
    return result


def evaluate(schema, x, coeff):
    return {m: coeff[0]*x[p] + (coeff[b]*min(x[u] for u in f) if b else 0)
            for m, (p, b, f) in schema.items()}


class ExactCandidateAudit(unittest.TestCase):
    def test_index_maps_and_cycles(self):
        count = 0
        for k in range(2, 8):
            ids, p, x, seen = residues(k), 3**k, 2, set()
            while x not in seen:
                seen.add(x); x = 4*x % p
            self.assertEqual(seen, set(ids)); self.assertEqual(x, 2)
            schema = rows(k)
            for m, (_, branch, fiber) in schema.items():
                if branch:
                    u = ((4*m-2) if branch == 1 else (2*m-1))//3 % (p//3)
                    self.assertEqual(set(fiber), {u+j*(p//3) for j in range(3)})
                    count += 1
            # Each branch visits each lower fiber exactly once.
            for b in (1, 2):
                keys = [f for _, branch, f in schema.values() if branch == b]
                self.assertEqual(len(keys), len(set(keys)))
                self.assertEqual(len(keys), 3**(k-2))
        COUNTS['branch_index_checks_k2_to_k7'] = count

    def test_projection_lift_and_endpoint_sum(self):
        rng = Random(0x4B4C2026)
        coefficients = ((Q(1), Q(1), Q(1)), (Q(1,4), Q(3,4), Q(3,2)),
                        (Q(2,7), Q(5,11), Q(13,17)))
        counts = 0
        for k in range(2, 6):
            low, high, ids, P = rows(k), rows(k+1), residues(k), 3**k
            vectors = product(range(3), repeat=len(ids)) if k <= 3 else (
                [Q(rng.randrange(0, 31), rng.randrange(1, 8)) for _ in ids]
                for _ in range(40))
            # Level 3 exhaustive search 3^9=19683, including boundary zeros.
            for values in vectors:
                c = dict(zip(ids, map(Q, values)))
                lc = {m: c[m % P] for m in high}
                varying = any(len({c[v] for v in ids if v % (P//3) == u}) > 1
                              for u in residues(k-1))
                for coeff in coefficients:
                    f, g = evaluate(low, c, coeff), evaluate(high, lc, coeff)
                    self.assertTrue(all(f[m % P] <= g[m] for m in high))
                    self.assertEqual(any(f[m % P] < g[m] for m in high), varying)
                    for m in ids:
                        self.assertEqual(min(g[v] for v in high if v % P == m), f[m])
                    counts += 1
                f2 = evaluate(low, c, coefficients[1])
                minimum_sum = sum(min(c[v] for v in ids if v % (P//3) == u)
                                  for u in residues(k-1))
                self.assertEqual(sum(f2.values()), sum(c.values())/4+Q(9,4)*minimum_sum)
                self.assertLessEqual(sum(f2.values()), sum(c.values()))
                if sum(f2.values()) == sum(c.values()):
                    self.assertFalse(varying)
                if any(c.values()):
                    self.assertTrue(any(f2[m] < c[m] for m in ids),
                                    'nonzero certificate found at lambda=2')
        COUNTS['lift_projection_coefficient_cases'] = counts

    def test_auxiliary_elimination_and_normalization(self):
        count = 0
        for k in (2, 3):
            ids, schema, stride = residues(k), rows(k), 3**(k-1)
            for vals in product((1, 2), repeat=len(ids)):
                c = dict(zip(ids, map(Q, vals)))
                us = residues(k-1)
                mins = {u: min(c[v] for v in ids if v % stride == u) for u in us}
                for coeff in ((Q(1), Q(1), Q(1)), (Q(1,4), Q(3,4), Q(3,2))):
                    possible = False
                    # Exhaust all normalized auxiliary integer values 1..min(c fiber).
                    for choices in product(*(range(1, int(mins[u])+1) for u in us)):
                        aux = dict(zip(us, map(Q, choices)))
                        if all(c[m] <= coeff[0]*c[p] +
                               (coeff[b]*aux[f[0] % stride] if b else 0)
                               for m, (p, b, f) in schema.items()):
                            possible = True; break
                    fc = evaluate(schema, c, coeff)
                    self.assertEqual(possible, all(c[m] <= fc[m] for m in ids))
                    # Arbitrary positive rescaling followed by minimum normalization.
                    scaled = {m: c[m]*Q(7, 13) for m in ids}
                    norm = {m: scaled[m]/min(scaled.values()) for m in ids}
                    self.assertEqual(min(norm.values()), 1)
                    fn = evaluate(schema, norm, coeff)
                    self.assertEqual(all(c[m] <= fc[m] for m in ids),
                                     all(norm[m] <= fn[m] for m in ids))
                    count += 1
        COUNTS['auxiliary_and_normalization_cases'] = count

    def test_eigenvector_boundary_supports(self):
        count = 0
        for k in (2, 3):
            ids, schema = residues(k), rows(k)
            for bits in product((0, 1), repeat=len(ids)):
                if not any(bits) or all(bits):
                    continue
                v = dict(zip(ids, bits))
                # A zero coordinate receives a strictly positive permutation term.
                self.assertTrue(any(v[m] == 0 and v[p] == 1 for m, (p, _, _) in schema.items()))
                count += 1
        COUNTS['nonempty_proper_eigen_supports_excluded'] = count

    def test_propagation_and_strictification(self):
        count, localized = 0, None
        for k in (2, 3):
            ids, schema = residues(k), rows(k)
            for vals in product((1, 2), repeat=len(ids)):
                v = dict(zip(ids, map(Q, vals)))
                coeff = (Q(1), Q(1), Q(1))
                z = evaluate(schema, v, coeff)
                if not (all(z[m] >= v[m] for m in ids) and any(z[m] > v[m] for m in ids)):
                    continue
                iters, z = [v], v
                for t in range(len(ids)):
                    nxt = evaluate(schema, z, coeff)
                    self.assertTrue(all(nxt[m] >= z[m] for m in ids))
                    if t:
                        previous = iters[-2]
                        self.assertTrue(all(nxt[m]-z[m] >= coeff[0]*(z[p]-previous[p])
                                            for m, (p, _, _) in schema.items()))
                    iters.append(nxt); z = nxt
                self.assertTrue(all(z[m] > v[m] for m in ids))
                w = {m: sum(it[m] for it in iters[:-1]) for m in ids}
                fw = evaluate(schema, w, coeff)
                self.assertTrue(all(fw[m] > w[m] for m in ids))
                if localized is None and any(iters[1][m] == v[m] for m in ids):
                    localized = {'k': k, 'v': list(vals),
                                 'first_slack': [str(iters[1][m]-v[m]) for m in ids]}
                count += 1
        WITNESSES['one_step_not_strict_everywhere'] = localized
        COUNTS['feasible_strict_seeds_propagated'] = count

    def test_essential_hypotheses_and_literal_quantifier(self):
        # B must existentially quantify c on the left. It is not true for every c.
        schema = rows(2)
        c = dict(zip(residues(2), map(Q, (1, 2, 1))))
        fc = evaluate(schema, c, (Q(1), Q(1), Q(1)))
        self.assertLess(fc[5], c[5])
        bad = next(v for v in product((1, 2), repeat=3)
                   if any(evaluate(schema, dict(zip(residues(2), map(Q, v))), (Q(1),)*3)[m] < v[i]
                          for i, m in enumerate(residues(2))))
        self.assertEqual(bad, (1, 2, 1))
        base = dict(zip(residues(2), map(Q, (3, 2, 3))))
        fb = evaluate(schema, base, (Q(1), Q(1), Q(1)))
        self.assertTrue(all(fb[m] > base[m] for m in base))
        WITNESSES['B_literal_free_c_false'] = {'k': 2, 'lambda': 1,
                                               'c': [1, 2, 1], 'F_c': [str(fc[m]) for m in c]}
        # The projection formula cannot simply be extended down to level 1.
        self.assertEqual(min(evaluate(schema, {m: Q(1) for m in schema}, (Q(1),)*3).values()), 1)
        self.assertNotEqual(1, Q(1)+Q(1))  # artificial F_1 row of type 2 would equal 2
        WITNESSES['P_requires_upper_level_at_least_3'] = {'upper_level': 2, 'coefficients': [1,1,1],
                                                        'minimum_high': 1, 'naive_level1': 2}
        # Counterexample to propagation without a positive cyclic coupling.
        z = (Q(1), Q(1))
        for _ in range(10):
            z = (2*z[0], z[1])
            self.assertGreater(z[0], 1)
            self.assertEqual(z[1], 1)
        WITNESSES['E_without_cyclic_coupling_false'] = {'map': '(2*x0,x1)', 'v': [1,1],
                                                       'iterates': '(2^t,1)'}


if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(ExactCandidateAudit))
    (OUT/'logs/independent.json').write_text(json.dumps({
        'tests_run': result.testsRun, 'failures': len(result.failures), 'errors': len(result.errors),
        'counts': COUNTS, 'witnesses': WITNESSES,
        'scope': 'finite exact checks of candidate operator; no primary-source equivalence certified'
    }, indent=2)+'\n')
    raise SystemExit(not result.wasSuccessful())
