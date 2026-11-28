#!/usr/bin/env python3
"""Contrôles du cycle 021.

Ils vérifient que le cas classique entre dans l'hypothèse de Garcia–Tal,
que leur branche impaire est T, que l'identité de hauteur de B6 est exacte
sur un préfixe, et que la borne de B6 reste approchable si la hauteur est
linéaire. Ils ne démontrent pas R(t)=O(1) et ne relisent pas Heppner.

Usage : python3 research/checks/cycle021_garcia_tal_gate.py
"""

from __future__ import annotations

from fractions import Fraction


def T(n: int) -> int:
    if n % 2:
        return (3 * n + 1) // 2
    return n // 2


def paper_branch(n: int) -> int:
    """H de Garcia–Tal pour d=2, m=3, résidu impair -1."""
    if n % 2 == 0:
        return n // 2
    return (3 * n - (-1)) // 2


def passes() -> list[str]:
    out: list[str] = []

    # m < d^{d/(d-1)} : 3 < 2^2.
    if 3 < 4:
        out.append("PASS hypothese d=2 m=3 : 3<4")
    else:
        raise RuntimeError("3<4")

    for n in range(1, 65):
        if paper_branch(n) != T(n):
            raise RuntimeError(n)
    out.append("PASS branche de H identique a T sur 1..64")

    n = 27
    pred = Fraction(28)
    for _ in range(80):
        if n % 2 == 0:
            pred *= Fraction(n + 2, 2 * (n + 1))
            n //= 2
        else:
            pred *= Fraction(3, 2)
            n = (3 * n + 1) // 2
        if pred != n + 1:
            raise RuntimeError((n, pred))
    out.append("PASS identite de hauteur sur 80 pas depuis 27")

    # Base t=24, a=49. Pour a>=49, (a+2)/a <= 51/49 et (51/49)^4 < 2,
    # donc (a+2)^4 < 2 a^4 et l'inégalité se propage à tout t>=24.
    if 49**4 >= 2**24:
        raise RuntimeError("base")
    if 51**4 >= 2 * 49**4:
        raise RuntimeError("pas")
    out.append("PASS (2t+1)^4 < 2^t pour tout t>=24")

    # (1/4)/log2(3) < 1/6 car 4 log2(3) > 6, soit 3^4 > 2^6.
    if 81 <= 64:
        raise RuntimeError("81>64")
    out.append("PASS ecart relatif < 1/6 si log2(n_t+1) <= log2(2t+1)")

    # t valeurs distinctes dans 1..2t : densite inferieure 1/2.
    for t in (1, 5, 40):
        count = t
        length = 2 * t
        if count * 2 != length:
            raise RuntimeError(t)
    out.append("PASS t valeurs dans 1..2t donnent la proportion 1/2")

    # Suite synthetique, pas une orbite : valeurs 2^j a l'instant 2^{2j}.
    # Le rapport tend vers 0, et les valeurs jusqu'a 2^j sont j+1.
    for j in range(1, 21):
        value = 2**j
        time = 2 ** (2 * j)
        if value * j >= time:
            raise RuntimeError(j)
    for j in range(2, 21):
        if j + 1 >= 2**j:
            raise RuntimeError(("densite", j))
    out.append("PASS suite synthetique : densite nulle et n_t/t -> 0")

    return out


def main() -> None:
    lines = passes()
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
