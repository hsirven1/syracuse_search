#!/usr/bin/env python3
"""Contrôles du cycle 015.

Les témoins sont des entiers exacts. Ils illustrent B21 ; ils ne
remplacent pas la preuve, qui vaut pour tout module et toute borne.

Usage : python3 research/checks/cycle015_self_contraction.py
"""


def v2(n: int) -> int:
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def U(n: int) -> int:
    y = 3 * n + 1
    return y >> v2(y)


def q_residue(s: int) -> tuple[int, int]:
    mod = 1 << (s + 1)
    q = ((1 << s) + 1) * pow(3**s, -1, mod) % mod
    return q, mod


def a3_value(s: int, q: int) -> int:
    return (1 << s) * q - 1


def check_a3(s: int, q: int) -> None:
    y = a3_value(s, q)
    assert y % 2 == 1
    z = y
    for r in range(1, s):
        z = U(z)
        assert z == 3**r * (1 << (s - r)) * q - 1
        assert z > y
    z = U(z)
    assert z == (3**s * q - 1) >> s
    assert z < y


def minimal_has_no_smaller(m: int, r: int) -> int:
    assert 0 <= r < m and r != 1
    n0 = r if r > 1 else m
    assert n0 > 1 and n0 % m == r
    smaller = [k for k in range(1, n0) if k % m == r]
    assert smaller == []
    return n0


def direct_climb(m: int, s: int) -> int:
    """Classe 1 mod m, avec 4 ne divisant pas m : un cylindre de A3."""
    assert m >= 2 and m % 4 != 0 and m % 2 == 1 or m % 4 == 2
    q0, qmod = q_residue(s)
    y0 = a3_value(s, q0)
    ymod = 1 << (2 * s + 1)
    # y ≡ y0 (mod 2^{2s+1}), y ≡ 1 (mod m). Les deux sont impairs.
    g = 2 if m % 2 == 0 else 1
    assert (y0 - 1) % g == 0
    # Recherche du plus petit t ≥ 0 assez grand.
    # y = y0 + ymod * t ≡ 1 (mod m).
    target = (1 - y0) % m
    # ymod * t ≡ target (mod m).
    step = ymod % m
    gg = gcd(step, m)
    assert target % gg == 0
    t = solve_linear(step // gg, target // gg, m // gg)
    mod_t = m // gg
    for extra in range(0, 6):
        tt = t + mod_t * extra
        y = y0 + ymod * tt
        q = (y + 1) >> s
        if (4**s - 3**s) * q <= (1 << s) - 1:
            continue
        assert y % m == 1
        check_a3(s, q)
        x = y
        for step_i in range(1, s):
            x = U(x)
            assert x >= y
        return y
    raise AssertionError("no direct witness")


def bridge(m: int, s: int) -> tuple[int, int, int]:
    """Classe 1 mod m, 4 | m. Retourne (n, j, s)."""
    assert m % 4 == 0 and s >= 2
    L = v2(m)
    M = m >> L
    assert M % 2 == 1 and L >= 2
    if L % 2 == 1:
        j = (L - 1) // 2
        start = L
    else:
        j = L // 2
        start = L + 1
    assert start == 2 * j + 1
    q0, qmod = q_residue(s)
    odd = (3**j) * M
    # 2^{s-1} q ≡ 1 (mod 3^j M), q ≡ q0 (mod 2^{s+1}).
    A = (pow(2, s - 1, odd) * (qmod % odd)) % odd
    B = (1 - pow(2, s - 1, odd) * (q0 % odd)) % odd
    t0 = (B * pow(A, -1, odd)) % odd
    for extra in range(0, 8):
        q = q0 + qmod * (t0 + odd * extra)
        if (4**s - 3**s) * q <= (1 << s) - 1:
            continue
        raw = (1 << (s - 1)) * q - 1
        assert raw % odd == 0
        t = raw // (3**j)
        assert t % 2 == 1 and t % M == 0
        n = 1 + (1 << start) * t
        assert n % m == 1 and n > 1
        assert U(n) > 0
        # Préfixe : j pas, valuation exacte.
        x = n
        for i in range(1, j + 1):
            assert v2(x - 1) == start - 2 * (i - 1)
            assert v2(x - 1) >= 3
            x = U(x)
            assert v2(x - 1) == start - 2 * i
            assert x % m != 1
        y = x
        q_y = (y + 1) >> s
        assert q_y == q
        check_a3(s, q)
        # Montée : pas r = 1 .. s-2, temps global j+r ≤ j+s-2.
        z = y
        for r in range(1, s - 1):
            z = U(z)
            assert z % 4 == 3
            assert z % m != 1
        # Aucun retour strict avant le temps j+s-1.
        x = n
        for step_i in range(1, j + s - 1):
            x = U(x)
            assert not (x < n and x % m == 1)
        return n, j, s
    raise AssertionError("no bridge")


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def solve_linear(a: int, b: int, mod: int) -> int:
    """Plus petite solution ≥ 0 de a t ≡ b (mod mod), gcd déjà réduit à 1."""
    return (b * pow(a, -1, mod)) % mod


def main() -> None:
    for m in range(2, 41):
        for r in range(m):
            if r == 1:
                continue
            minimal_has_no_smaller(m, r)
    print("PASS minimal element, m=2..40, residue other than 1")

    for m, s in ((3, 5), (5, 6), (6, 5), (10, 7), (14, 4)):
        y = direct_climb(m, s)
        assert y % m == 1
    print("PASS direct A3 climb inside 1 mod m, five moduli not divisible by 4")

    examples = []
    for m, s in ((4, 6), (8, 5), (12, 6), (16, 6), (20, 8), (24, 7), (32, 8), (48, 6)):
        n, j, ss = bridge(m, s)
        examples.append((m, n, j, ss))
    print("PASS bridge, eight moduli divisible by 4")
    print("EXAMPLES", " ".join(f"{m}:{n}" for m, n, _j, _s in examples))


if __name__ == "__main__":
    main()
