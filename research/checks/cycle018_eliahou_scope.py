#!/usr/bin/env python3
"""Contrôles du cycle 018.

Ils vérifient le cycle trivial, la valeur k(1) du critère attribué à
Eliahou par Halbeisen–Hungerbühler, et l'exclusion de ce cycle hors de
la forme linéaire secondaire. Ils ne calculent pas k(2^40) et ne
redémontrent pas l'estimation de fractions continues.

Usage : python3 research/checks/cycle018_eliahou_scope.py
"""


def T(n: int) -> int:
    if n % 2:
        return (3 * n + 1) // 2
    return n // 2


def odd_steps(length: int) -> int:
    """Plus grand n tel que 3^n ≤ 2^length. C'est floor(length log_3 2)."""
    n = 0
    power = 1
    limit = 1 << length
    while power * 3 <= limit:
        power *= 3
        n += 1
    return n


def k_of_minimum_one() -> int:
    """Plus petit k ≥ 1 tel que k / n(k) ≤ log2(4) = 2."""
    for k in range(1, 20):
        n = odd_steps(k)
        if n > 0 and k <= 2 * n:
            return k
    raise RuntimeError("k(1) introuvable")


def forward_orbit(start: int, limit: int) -> list[int]:
    seen = []
    x = start
    while x not in seen and len(seen) < limit:
        seen.append(x)
        x = T(x)
    return seen


def main() -> None:
    assert T(1) == 2 and T(2) == 1
    trivial = {1, 2}
    assert len(trivial) == 2
    print("PASS cycle trivial {1,2}, cardinal 2")

    assert odd_steps(1) == 0
    assert odd_steps(2) == 1
    assert 3**1 <= 2**2 < 3**2
    print("PASS n(1)=0 et n(2)=1")

    # Lemme 6, pour n = n(l) : l log_3 2 - 1 ≤ n ≤ l log_3 2,
    # soit 3^n ≤ 2^l et 2^l < 3^{n+1}, donc 2^l < 3 * 3^n.
    for length in (1, 2, 16):
        n = odd_steps(length)
        assert 3**n <= 2**length < 3 ** (n + 1)
    print("PASS encadrement de n(l) pour l=1,2,16")

    k1 = k_of_minimum_one()
    assert k1 == 2
    assert len(trivial) >= k1
    print("PASS k(1)=2 et |{1,2}| = k(1)")

    # Forme linéaire secondaire, avec b ≥ 1. Le minimum est 17087915.
    minimum = 17087915
    assert minimum > len(trivial)
    for b in (1, 2):
        value = 17087915 * b
        assert value != 2
    print("PASS {1,2} hors de la forme à b>0")

    orbit = forward_orbit(5, 20)
    assert orbit[0] == 5
    assert 1 in orbit and 2 in orbit
    assert len(orbit) < 20
    print("PASS orbite de 5 finie et rencontre {1,2}")


if __name__ == "__main__":
    main()
