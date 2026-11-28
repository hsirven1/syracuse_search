#!/usr/bin/env python3
"""Contrôles du cycle 014.

Le sandwich harmonique et la somme flottante du témoin X34 comparent
des flottants avec une tolérance : ce sont des contrôles numériques.
Les identités de fibres, la somme des densités, la différence de
sommes harmoniques et les blocs de factorielles sont des égalités
exactes, en fractions ou en entiers. Le témoin f(N)=N+1 ne calcule
pas une orbite.

La discussion est dans research/cycles/cycle-014.md. Ce script ne
remplace pas la preuve.

Usage : python3 research/checks/cycle014_log_density.py
"""

from fractions import Fraction
from math import factorial, log


def harmonic_class(x, r, m):
    total = 0.0
    n = r
    while n <= x:
        total += 1.0 / n
        n += m
    return total


def harmonic(x):
    return sum(1.0 / n for n in range(1, x + 1))


def check_sandwich(x, m):
    full = harmonic(x)
    if not (log(x) <= full <= 1.0 + log(x)):
        raise AssertionError((x, full, log(x)))
    for r in range(1, m + 1):
        s = harmonic_class(x, r, m)
        lower = (1.0 / m) * log(x / r)
        upper = 1.0 / r + (1.0 / m) * log(x / r)
        # Marge flottante : les inégalités du cycle sont exactes.
        if s + 1e-9 < lower or s > upper + 1e-9:
            raise AssertionError((x, m, r, s, lower, upper))
        # La limite est le sandwich du cycle, pas un seuil numérique sur le rapport.


def x34_hits(q, repeats):
    seen = {b: 0 for b in range(q)}
    for m in range(1, 40):
        base = factorial(m)
        for r in range(1, m + 1):
            seen[(base + r) % q] += 1
        if all(seen[b] >= repeats for b in range(q)):
            return True
    return False


def odd_reciprocal_sum(y):
    total = Fraction(0)
    m = 1
    while m <= y:
        total += Fraction(1, m)
        m += 2
    return total


def fiber_reciprocal_sum(x, a):
    """Somme des inverses de la fibre v_2(N)=a, N≤x.

    Ces N sont exactement les N ≡ 2^a (mod 2^{a+1}).
    """
    total = Fraction(0)
    step = 1 << a
    modulus = step << 1
    n = step
    while n <= x:
        if n % modulus != step:
            raise AssertionError((n, a))
        total += Fraction(1, n)
        n += modulus
    return total


def check_fibers():
    xs = (1, 2, 31, 256, 1024, 4096)
    count = 0
    for x in xs:
        for a in range(13):
            left = fiber_reciprocal_sum(x, a)
            right = odd_reciprocal_sum(x >> a) / (1 << a)
            if left != right:
                raise AssertionError((x, a, left, right))
            count += 1
    if count != 78:
        raise AssertionError(count)
    for upper in range(13):
        printed = sum((Fraction(1, 1 << a) for a in range(upper + 1)), Fraction(0))
        correct = sum(
            (Fraction(1, 1 << (a + 1)) for a in range(upper + 1)),
            Fraction(0),
        )
        if printed != 2 - Fraction(1, 1 << upper):
            raise AssertionError((upper, printed))
        if correct != 1 - Fraction(1, 1 << (upper + 1)):
            raise AssertionError((upper, correct))
        # A=0 gives the printed mass 1; A≥1 exceeds 1.
        if (printed > 1) != (upper >= 1):
            raise AssertionError((upper, printed))
    return count


def check_x34_exact():
    previous_end = 0
    recip = Fraction(0)
    bound = Fraction(0)
    for m in range(1, 41):
        base = factorial(m)
        if base < (1 << (m - 1)):
            raise AssertionError(m)
        if base + 1 <= previous_end:
            raise AssertionError(m)
        previous_end = base + m
        for r in range(1, m + 1):
            recip += Fraction(1, base + r)
            bound += Fraction(1, base)
    if not recip < bound:
        raise AssertionError((recip, bound))
    partial = sum((Fraction(m, factorial(m)) for m in range(1, 41)), Fraction(0))
    series = sum((Fraction(1, factorial(j)) for j in range(41)), Fraction(0))
    if partial != series - Fraction(1, factorial(40)):
        raise AssertionError((partial, series))
    for q in range(1, 31):
        for m in (q, q + 1, q + 2):
            base = factorial(m)
            residues = {(base + r) % q for r in range(1, q + 1)}
            if residues != set(range(q)):
                raise AssertionError((q, m))
    for x in (1, 2, 10, 100, 1000, factorial(10)):
        count = 0
        m = 1
        while factorial(m) + 1 <= x:
            count += min(m, x - factorial(m))
            m += 1
        cap = x.bit_length() * (x.bit_length() + 1) // 2
        if count > cap:
            raise AssertionError((x, count, cap))


def check_harmonic_fiber_weights():
    """Poids exact de la revue 6093505644, et représentants de X36.

    La différence de sommes harmoniques est l'identité du cycle 014 §10.
    N < N+1 ne remplace pas la définition de Col_min.
    """
    xs = (1, 3, 17, 100, 511, 2048)
    fiber_count = 0
    cumulative_count = 0
    for x in xs:
        running = Fraction(0)
        full = harmonic_fraction(x)
        for a in range(13):
            left = fiber_reciprocal_sum(x, a)
            y = x >> a
            right = harmonic_fraction(y) / (1 << a) - harmonic_fraction(y >> 1) / (
                1 << (a + 1)
            )
            if left != right:
                raise AssertionError((x, a, left, right))
            fiber_count += 1
            running += left
            cumulative = full - harmonic_fraction(x >> (a + 1)) / (1 << (a + 1))
            if running != cumulative:
                raise AssertionError((x, a, running, cumulative))
            cumulative_count += 1
    if fiber_count != 78 or cumulative_count != 78:
        raise AssertionError((fiber_count, cumulative_count))
    for upper in range(41):
        printed = sum((Fraction(1, 1 << a) for a in range(upper + 1)), Fraction(0))
        correct = sum(
            (Fraction(1, 1 << (a + 1)) for a in range(upper + 1)),
            Fraction(0),
        )
        if printed != 2 - Fraction(1, 1 << upper):
            raise AssertionError((upper, printed))
        if correct != 1 - Fraction(1, 1 << (upper + 1)):
            raise AssertionError((upper, correct))
    for q in range(1, 41):
        for m in (q, q + 1, q + 7):
            base = factorial(m)
            if base < (1 << (m - 1)):
                raise AssertionError(m)
            residues = {(base + r) % q for r in range(1, q + 1)}
            if residues != set(range(q)):
                raise AssertionError((q, m))
    for a in range(16):
        n = 1 << a
        if n % (1 << (a + 1)) != n or not n < n + 1:
            raise AssertionError(a)
    return fiber_count, cumulative_count


def harmonic_fraction(y):
    if y <= 0:
        return Fraction(0)
    return sum((Fraction(1, n) for n in range(1, y + 1)), Fraction(0))


def main():
    x = 20000
    for m in (1, 2, 3, 8, 24):
        check_sandwich(x, m)
    print("PASS sandwich numérique x=20000 modules 1,2,3,8,24")

    # Somme des inverses du témoin, tronquée là où m/m! est encore visible.
    recip = 0.0
    bound = 0.0
    previous_end = 0
    for m in range(1, 20):
        base = factorial(m)
        block_end = base + m
        if base + 1 <= previous_end:
            raise AssertionError("blocks overlap")
        previous_end = block_end
        for r in range(1, m + 1):
            recip += 1.0 / (base + r)
            bound += 1.0 / base
    # ∑_{m≥1} m/m! = e, et la queue m≥20 est < 10^{-15}.
    e_partial = sum(1.0 / factorial(j) for j in range(20))
    if not (recip < bound <= e_partial + 1e-12):
        raise AssertionError((recip, bound, e_partial))
    print("PASS somme numérique des inverses du témoin < e")

    for q in range(1, 9):
        if not x34_hits(q, 2):
            raise AssertionError(q)
    print("PASS chaque résidu modulo q≤8 est atteint au moins deux fois")

    count = check_fibers()
    print(
        "PASS fibres exactes :",
        count,
        "identités, sommes 2-2^{-A} et 1-2^{-(A+1)}",
    )
    check_x34_exact()
    print("PASS blocs exacts, résidus q≤30, et borne de comptage")
    weights, cumulative = check_harmonic_fiber_weights()
    print(
        "PASS poids harmoniques :",
        weights,
        "fibres,",
        cumulative,
        "cumulés, sommes jusqu'à A=40, blocs q≤40",
    )


if __name__ == "__main__":
    main()
