#!/usr/bin/env python3
"""Contrôles exacts du cycle 014.

La discussion est dans research/cycles/cycle-014.md. Ce script ne remplace
pas la preuve. Il vérifie le sandwich harmonique d'une classe de congruence
et le témoin X34 : blocs de factorielles, somme des inverses < e, et
rencontre de chaque résidu.

Usage : python3 research/checks/cycle014_log_density.py
"""

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


def main():
    x = 20000
    for m in (1, 2, 3, 8, 24):
        check_sandwich(x, m)
    print("PASS sandwich harmonique x=20000 modules 1,2,3,8,24")

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
    print("PASS somme des inverses du témoin < e")

    for q in range(1, 9):
        if not x34_hits(q, 2):
            raise AssertionError(q)
    print("PASS chaque résidu modulo q≤8 est atteint au moins deux fois")


if __name__ == "__main__":
    main()
