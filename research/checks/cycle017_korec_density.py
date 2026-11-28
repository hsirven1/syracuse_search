#!/usr/bin/env python3
"""Contrôles du cycle 017.

Ils vérifient les constantes affichées, l'orbite de 1, l'égalité des
minima de T et de l'application classique, la classe y ≡ -1 (mod 2^m)
dont les m premiers termes sont impairs, et le comptage de X34.
Ils ne redémontrent pas le théorème 1 de Korec.

Usage : python3 research/checks/cycle017_korec_density.py
"""

from decimal import Decimal, getcontext
from math import factorial


getcontext().prec = 50


def T(y: int) -> int:
    if y % 2:
        return (3 * y + 1) // 2
    return y // 2


def C(y: int) -> int:
    if y % 2:
        return 3 * y + 1
    return y // 2


def odds(step, y: int, limit: int) -> list[int]:
    out = []
    seen = set()
    z = y
    while z not in seen and len(out) < limit:
        seen.add(z)
        if z % 2:
            out.append(z)
        z = step(z)
    return out


def minimum(step, y: int, limit: int) -> int:
    seen = set()
    z = y
    best = y
    steps = 0
    while z not in seen and steps < limit:
        seen.add(z)
        best = min(best, z)
        z = step(z)
        steps += 1
    if z not in seen:
        raise AssertionError(("pas de cycle", y))
    return best


def check_constants() -> None:
    log4_3 = Decimal(3).ln() / Decimal(4).ln()
    text = format(log4_3, "f")
    if not text.startswith("0.7924812503"):
        raise AssertionError(text)
    if not (Decimal("0.79248125") < log4_3 < Decimal("0.79248126")):
        raise AssertionError(log4_3)
    if not (Decimal("0.7925") > log4_3):
        raise AssertionError(log4_3)
    allouche = Decimal("1.5") - Decimal(2).ln() / Decimal(3).ln()
    if not str(allouche).startswith("0.8690702464"):
        raise AssertionError(allouche)
    print("PASS constantes")


def check_one() -> None:
    orbit = [1]
    z = 1
    for _ in range(4):
        z = T(z)
        orbit.append(z)
    if orbit != [1, 2, 1, 2, 1]:
        raise AssertionError(orbit)
    if any(v < 1 for v in orbit):
        raise AssertionError(orbit)
    print("PASS orbite de 1")


def check_minima(bound: int) -> None:
    for y in range(1, bound + 1):
        if odds(T, y, 30) != odds(C, y, 30):
            raise AssertionError(("impairs", y))
        if minimum(T, y, 20000) != minimum(C, y, 20000):
            raise AssertionError(("minimum", y))
    print("PASS minima", bound)


def check_mersenne_class(max_m: int) -> None:
    for m in range(1, max_m + 1):
        mod = 1 << m
        for t in (1, 2, 5):
            y = t * mod - 1
            z = y
            for i in range(m):
                step = 1 << (m - i)
                if z % 2 == 0 or (z + 1) % step != 0:
                    raise AssertionError((m, t, i, z))
                z = T(z)
            if T(y) != 3 * (1 << (m - 1)) * t - 1:
                raise AssertionError((m, t, T(y)))
    print("PASS classe -1", max_m)


def check_x34(q: int, repeats: int) -> None:
    seen = {b: 0 for b in range(q)}
    counted = 0
    for m in range(1, 30):
        base = factorial(m)
        for r in range(1, m + 1):
            seen[(base + r) % q] += 1
            counted += 1
        if all(seen[b] >= repeats for b in range(q)):
            # m!+m < (m+1)!+1, donc les blocs sont disjoints.
            if factorial(m) + m >= factorial(m + 1) + 1:
                raise AssertionError(m)
            print("PASS X34", q, counted)
            return
    raise AssertionError((q, seen))


if __name__ == "__main__":
    check_constants()
    check_one()
    check_minima(2000)
    check_mersenne_class(16)
    check_x34(8, 2)
    check_x34(24, 1)
