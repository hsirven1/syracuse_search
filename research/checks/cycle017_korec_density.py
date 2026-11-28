#!/usr/bin/env python3
"""Contrôles du cycle 017.

Ils vérifient les constantes affichées, l'orbite de 1, l'égalité des
minima de T et de l'application classique, la classe y ≡ -1 (mod 2^m),
la formule de cette classe jusqu'au rang m, le comptage de X34,
l'identité de la formule imprimée de d, l'échec de l'implication (4)
pour cette formule, et la première descente de 27.
Ils ne redémontrent pas le théorème 1 de Korec.

Usage : python3 research/checks/cycle017_korec_density.py
"""

from decimal import Decimal, getcontext
from fractions import Fraction
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
        for t in (1, 2, 5, 17):
            y = t * mod - 1
            z = y
            for i in range(m + 1):
                expect = (3**i) * (1 << (m - i)) * t - 1
                if z != expect:
                    raise AssertionError((m, t, i, z, expect))
                if i < m and z % 2 == 0:
                    raise AssertionError((m, t, i, z))
                if i < m:
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


def check_printed_d() -> None:
    # 4 = 2^2, donc log4(3) = log2(3)/2. Pour tout rationnel positif L
    # tenu à la place de log2(3), la formule imprimée devient c/L + 1/4.
    for L in (Fraction(3, 2), Fraction(8, 5), Fraction(53, 32)):
        for c in (Fraction(4, 5), Fraction(5, 6), Fraction(9, 10)):
            printed = Fraction(1, 2) * (c / (L / 2) + Fraction(1, 2))
            if printed != c / L + Fraction(1, 4):
                raise AssertionError((c, L, printed))
    if 4 != 2**2:
        raise AssertionError(4)
    # c = 4/5 > log4(3), car 4^{4/5} > 3 équivaut à 4^4 > 3^5.
    if not (4**4 > 3**5):
        raise AssertionError((4**4, 3**5))
    getcontext().prec = 50
    log2_3 = Decimal(3).ln() / Decimal(2).ln()
    log4_3 = Decimal(3).ln() / Decimal(4).ln()
    if abs(log4_3 - log2_3 / 2) > Decimal("1e-40"):
        raise AssertionError(log4_3 - log2_3 / 2)
    c = Decimal(4) / Decimal(5)
    printed_dec = (c / log4_3 + Decimal("0.5")) / 2
    gap = printed_dec - c / log2_3
    if abs(gap - Decimal("0.25")) > Decimal("1e-40"):
        raise AssertionError(gap)
    if not format(printed_dec, "f").startswith("0.75474380"):
        raise AssertionError(printed_dec)
    if not format(c / log2_3, "f").startswith("0.50474380"):
        raise AssertionError(c / log2_3)
    print("PASS identité de d")


def check_implication_failure() -> None:
    # Pour c = 4/5 et m = 16, log2(m) = 4. Le membre de droite de (4)
    # vaut c/log2(3) - 13/80. Avec k = 8, k/m = 1/2 est sous le d imprimé
    # et au-dessus de ce membre : 3^5 < 2^16 et 2^64 < 3^53.
    if 3**5 >= 2**16:
        raise AssertionError((3**5, 2**16))
    if 2**64 >= 3**53:
        raise AssertionError((2**64, 3**53))
    c = Fraction(4, 5)
    subtracted = (1 + 2 * (1 - c) * 4) / 16
    if subtracted != Fraction(13, 80):
        raise AssertionError(subtracted)
    print("PASS implication (4)")


def check_twenty_seven() -> None:
    if not (2**4 < 27 < 2**5):
        raise AssertionError(27)
    z = 27
    seen = [z]
    for n in range(1, 80):
        z = T(z)
        seen.append(z)
        if z < 27:
            if n != 59 or z != 23:
                raise AssertionError((n, z))
            if min(seen[:-1]) < 27:
                raise AssertionError(min(seen[:-1]))
            if seen[-5:] != [122, 61, 92, 46, 23]:
                raise AssertionError(seen[-5:])
            print("PASS descente de 27")
            return
    raise AssertionError("pas de descente")


def check_zero() -> None:
    if T(0) != 0:
        raise AssertionError(T(0))
    print("PASS point 0")


if __name__ == "__main__":
    check_constants()
    check_one()
    check_minima(2000)
    check_mersenne_class(32)
    check_x34(8, 2)
    check_x34(24, 1)
    check_printed_d()
    check_implication_failure()
    check_twenty_seven()
    check_zero()
