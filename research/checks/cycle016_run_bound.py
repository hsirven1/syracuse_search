#!/usr/bin/env python3
"""Contrôles du cycle 016.

Ils vérifient l'équivalence entre P(2) et l'évitement du résidu 7
modulo 8, le cycle négatif qui évite ce résidu, et la caractérisation
de tau = 1. Ils ne prouvent pas la conjecture 4.13.

Usage : python3 research/checks/cycle016_run_bound.py
"""


def v2(n: int) -> int:
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def T(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    return (3 * n + 1) // 2


def C(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


def U(n: int) -> int:
    y = 3 * n + 1
    return y >> v2(y)


def hits_7(step, n: int, limit: int = 200) -> bool:
    seen = set()
    x = n
    for _ in range(limit):
        if x % 8 == 7:
            return True
        if x == 1 or x in seen:
            return False
        seen.add(x)
        x = step(x)
    raise AssertionError(n)


def main() -> None:
    for m in range(1, 9, 2):
        assert (3 * m + 1) % 8 != 7
    for residue in (1, 3, 5, 7):
        image = (3 * residue + 1) % 8
        assert image in (0, 2, 4, 6)

    orbit = []
    x = -5
    for _ in range(3):
        orbit.append(x)
        x = T(x)
    assert orbit == [-5, -7, -10]
    assert T(-10) == -5
    assert all(y % 8 != 7 for y in orbit)

    climb = [11]
    y = 11
    for _ in range(3):
        y = T(y)
        climb.append(y)
    assert climb == [11, 17, 26, 13]
    assert all(z % 8 != 7 for z in climb)
    assert 13 > 11

    for n in range(1, 4001):
        assert hits_7(C, n) == hits_7(T, n)
        if n % 2 == 1:
            assert (v2(n + 1) >= 3) == (n % 8 == 7)

    for n in range(3, 8001, 2):
        if n % 8 in (1, 5):
            assert U(n) < n
        else:
            assert n % 8 in (3, 7)
            assert U(n) > n
    assert U(1) == 1

    print("PASS residue 3n+1")
    print("PASS cycle -5")
    print("PASS montee 11")
    print("PASS C et T jusqu'a 4000")
    print("PASS tau=1 hors de 3 et 7 mod 8")


if __name__ == "__main__":
    main()
