#!/usr/bin/env python3
"""Contrôles du cycle 016.

Ils vérifient l'équivalence entre P(2) et l'évitement du résidu 7
modulo 8, le cycle négatif qui évite ce résidu, et la caractérisation
de tau = 1. Ils vérifient aussi que l'orbite de 5 évite 7 en
rencontrant 5, et que r-i est la valuation de T^i(m)+1. Ils ne
prouvent pas la conjecture 4.13.

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

    orbit5 = [5]
    x = 5
    for _ in range(6):
        x = T(x)
        orbit5.append(x)
    assert orbit5 == [5, 8, 4, 2, 1, 2, 1]
    assert [y % 8 for y in orbit5] == [5, 0, 4, 2, 1, 2, 1]
    assert any(y % 8 == 5 for y in orbit5)
    assert all(y % 8 != 7 for y in orbit5)

    for m in range(1, 4001, 2):
        r = v2(m + 1)
        x = m
        for i in range(r + 1):
            assert v2(x + 1) == r - i
            if i < r:
                assert x % 2 == 1 and v2(x) == 0
                if x % 8 == 7:
                    assert r - i >= 3
                x = T(x)
            else:
                assert x % 2 == 0
    assert [7, 11, 17, 26] == [7, T(7), T(T(7)), T(T(T(7)))]
    chain15 = [15]
    y = 15
    for _ in range(4):
        y = T(y)
        chain15.append(y)
    assert chain15 == [15, 23, 35, 53, 80]
    assert 23 % 8 == 7 and v2(23) == 0 and v2(24) == 3

    print("PASS residue 3n+1")
    print("PASS cycle -5")
    print("PASS montee 11")
    print("PASS C et T jusqu'a 4000")
    print("PASS tau=1 hors de 3 et 7 mod 8")
    print("PASS orbite 5 separe 7 et {5,7}")
    print("PASS valuation de T^i(m)+1")


if __name__ == "__main__":
    main()
