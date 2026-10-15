#!/usr/bin/env python3
"""Exact adversarial checks for a provisional KL strict-monotonicity argument.

Not a proof of strict monotonicity. Standard library only; Fraction throughout.
Run: python3 research/kl_strict_monotonicity_audit.py
"""
from fractions import Fraction as Q
from itertools import product


def classes(k):
    assert k >= 2
    return tuple(range(2, 3 ** k, 3))


def operator(k, c, a, b, d):
    """Unrolled KL max-auxiliary-variable (min-fiber) operator."""
    modulus = 3 ** k
    fiber_stride = 3 ** (k - 1)
    out = {}
    for m in classes(k):
        y = a * c[(4 * m) % modulus]
        if m % 9 == 2:
            u = ((4 * m - 2) // 3) % fiber_stride
            y += b * min(c[u + j * fiber_stride] for j in range(3))
        elif m % 9 == 8:
            u = ((2 * m - 1) // 3) % fiber_stride
            y += d * min(c[u + j * fiber_stride] for j in range(3))
        out[m] = y
    return out


def lift(k, c):
    return {m: c[m % (3 ** k)] for m in classes(k + 1)}


def nonconstant_fiber(k, c):
    stride = 3 ** (k - 1)
    return any(
        len({c[u + j * stride] for j in range(3)}) > 1
        for u in classes(k - 1) if k - 1 >= 2
    ) if k > 2 else len(set(c.values())) > 1


def four_transitive(k):
    modulus, x, seen = 3 ** k, 2, set()
    while x not in seen:
        seen.add(x)
        x = (4 * x) % modulus
    return x == 2 and seen == set(classes(k))


def check_lift_and_projection(k, c, coeff):
    a, b, d = coeff
    high = operator(k + 1, lift(k, c), a, b, d)
    low = operator(k, c, a, b, d)
    assert all(high[m] >= low[m % (3 ** k)] for m in high)
    strict = any(high[m] > low[m % (3 ** k)] for m in high)

    stride = 3 ** (k - 1)
    fibers_nonconstant = any(
        len({c[u + j * stride] for j in range(3)}) > 1
        for u in (range(2, 3 ** (k - 1), 3) if k >= 2 else ())
    )
    assert strict == fibers_nonconstant

    projected = {
        m: min(high[m + j * (3 ** k)] for j in range(3))
        for m in classes(k)
    }
    assert projected == low
    return strict


def check():
    # The three positive coefficient sets include exact lambda=2:
    coefficients = (
        (Q(1, 4), Q(3, 4), Q(3, 2)),
        (Q(1, 2), Q(43, 50), Q(61, 50)),
        (Q(2, 3), Q(3, 5), Q(4, 3)),
    )
    random_vectors, strict_lifts, projections = 0, 0, 0
    sum_checks, superadditivity = 0, 0
    for k in range(2, 6):
        assert four_transitive(k)
        for group, (a, b, d) in enumerate(coefficients):
            for seed in range(1, 40):
                c = {
                    m: Q(1 + (m * m + 13 * seed * m + seed ** 3)
                         % (7 + seed % 9))
                    for m in classes(k)
                }
                strict_lifts += bool(check_lift_and_projection(
                    k, c, (a, b, d)))
                random_vectors += 1
                projections += 1
                if group == 0:
                    stride = 3 ** (k - 1)
                    lhs = sum(operator(k, c, a, b, d).values())
                    rhs = Q(1, 4) * sum(c.values()) + Q(9, 4) * sum(
                        min(c[u + j * stride] for j in range(3))
                        for u in range(2, 3 ** (k - 1), 3)
                    )
                    assert lhs == rhs
                    sum_checks += 1

            x = {m: Q(1 + ((m + 7) ** 2) % 31) for m in classes(k)}
            y = {m: Q(1 + ((5 * m + 2) ** 2) % 23) for m in classes(k)}
            z = {m: x[m] + y[m] for m in classes(k)}
            fx, fy, fz = (operator(k, c, a, b, d) for c in (x, y, z))
            assert all(fz[m] >= fx[m] + fy[m] for m in classes(k))
            superadditivity += 1

    exhaustive = {}
    for k, values in ((2, 5), (3, 3)):
        count = 0
        a, b, d = coefficients[0]
        for entries in product(range(1, values + 1),
                               repeat=len(classes(k))):
            c = dict(zip(classes(k), map(Q, entries)))
            check_lift_and_projection(k, c, (a, b, d))
            stride = 3 ** (k - 1)
            expected = Q(1, 4) * sum(c.values()) + Q(9, 4) * sum(
                min(c[u + j * stride] for j in range(3))
                for u in range(2, 3 ** (k - 1), 3)
            )
            assert sum(operator(k, c, a, b, d).values()) == expected
            count += 1
        exhaustive[f"k={k}"] = count

    # Rational certificate at k=3 for gamma=1/2 (lambda=sqrt(2)).
    # These are LOWER bounds on exact coefficients:
    # a=1/2, b=sqrt(3)/2 > 43/50, d=sqrt(3/2) > 61/50.
    weights = (248408, 114266, 173913, 234301,
               123122, 296972, 243297, 100000, 236440)
    c = dict(zip(classes(3), map(Q, weights)))
    assert Q(43, 50) ** 2 < Q(3, 4)
    assert Q(61, 50) ** 2 < Q(3, 2)
    fc = operator(3, c, Q(1, 2), Q(43, 50), Q(61, 50))
    slacks = [fc[m] - c[m] for m in classes(3)]
    assert min(slacks) > 0

    # Lambda=1 base feasible vector at k=2, all strict.
    base = dict(zip(classes(2), map(Q, (3, 2, 3))))
    fbase = operator(2, base, Q(1), Q(1), Q(1))
    assert all(fbase[m] > base[m] for m in classes(2))

    print("PASS", {
        "random_exact_lift_checks": random_vectors,
        "nonconstant_cases_with_strict_lift": strict_lifts,
        "exact_fiber_projection_checks": projections,
        "sum_identity_checks": sum_checks,
        "superadditivity_checks": superadditivity,
        "exhaustive_vectors": exhaustive,
        "k3_rational_certificate": "PASS",
        "minimum_exact_slack": str(min(slacks)),
        "base_k2_lambda1": "PASS",
        "proof_of_universal_strict_monotonicity": "NOT FROM FINITE TESTS",
    })


if __name__ == "__main__":
    check()
