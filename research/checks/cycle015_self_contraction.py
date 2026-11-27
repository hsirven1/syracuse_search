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
        # Le rang 0 est dans la classe. Les rangs 1 .. j+s-2 n'y sont pas.
        x = n
        assert x % m == 1
        for step_i in range(1, j + s - 1):
            x = U(x)
            assert x % m != 1
        return n, j, s
    raise AssertionError("no bridge")


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def solve_linear(a: int, b: int, mod: int) -> int:
    """Plus petite solution ≥ 0 de a t ≡ b (mod mod), gcd déjà réduit à 1."""
    return (b * pow(a, -1, mod)) % mod


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def odd_run_length(n: int) -> int:
    assert n % 2 == 1
    c = 0
    while n % 2 == 1:
        c += 1
        n = T(n)
    return c


def parities(n: int, k: int) -> tuple[int, ...]:
    out = []
    for _ in range(k):
        out.append(n % 2)
        n = T(n)
    return tuple(out)


def check_formulations() -> None:
    # X38 : l'orbite de 1 ne descend pas sous 1, et ses runs impairs valent 1.
    x = 1
    orbit = [1]
    for _ in range(4):
        x = T(x)
        orbit.append(x)
    assert orbit == [1, 2, 1, 2, 1]
    assert odd_run_length(1) == 1 == v2(1 + 1)

    # Pour n>1, un premier run de longueur au plus 1 descend en au plus deux pas.
    for n in range(2, 4001):
        if n % 2 == 0:
            assert T(n) == n // 2 < n
        elif odd_run_length(n) == 1:
            assert n % 4 == 1
            assert T(T(n)) == (3 * n + 1) // 4 < n

    # La formule close vaut jusqu'au premier pair inclus, pas au-delà.
    # Pour n=1, T^2(1)=1 est impair alors que v_2(2)=1.
    assert T(T(1)) == 1 and v2(1 + 1) == 1
    for n in range(1, 20000, 2):
        r = v2(n + 1)
        x = n
        for i in range(r + 1):
            assert x + 1 == 3**i * (n + 1) // 2**i
            if i < r:
                assert x % 2 == 1
            else:
                assert x % 2 == 0
            x = T(x)
        assert odd_run_length(n) == r

    # Pour m=2, U renvoie un impair : le retour dans la classe n'est pas une descente.
    assert U(3) == 5 > 3 and U(3) % 2 == 1
    for n in range(1, 4001):
        assert U(n) % 2 == 1

    # Montée stricte de 2911 pour 1 ≤ t < 5. Le rang 0 est égal au départ.
    y = 2911
    assert y == 2**5 * 91 - 1
    climb = [y]
    x = y
    for _ in range(5):
        x = U(x)
        climb.append(x)
    assert climb == [2911, 4367, 6551, 9827, 14741, 691]
    assert all(climb[t] > y for t in range(1, 5))
    assert climb[5] < y

    # Si tous les runs impairs valent au plus 1, les impairs décroissent jusqu'à 1.
    for n in range(1, 4001, 2):
        if n % 4 == 1 and n > 1:
            nxt = U(n)
            assert nxt % 2 == 1 and nxt < n
    n = 5
    while n != 1:
        assert n % 4 == 1
        n = U(n)
    assert n == 1

    # X39 : le mot des longueurs de runs de 5 est constant, et 5 n'est pas périodique.
    seen = []
    x = 5
    runs = []
    for _ in range(8):
        seen.append(x)
        if x % 2 == 1:
            runs.append(odd_run_length(x))
        x = T(x)
    assert seen == [5, 8, 4, 2, 1, 2, 1, 2]
    assert runs == [1, 1, 1]
    y = 5
    for _ in range(1, 8):
        y = T(y)
        assert y != 5

    # Même vecteur de parités de longueur k : une seule classe modulo 2^k.
    for k in range(1, 11):
        seen_vec = {}
        for r in range(1 << k):
            p = parities(r, k)
            assert p not in seen_vec
            seen_vec[p] = r
        assert len(seen_vec) == 1 << k


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

    for m, s in ((4, 2), (8, 2), (16, 2), (32, 2)):
        n, j, ss = bridge(m, s)
        assert ss == 2 and j >= 1 and n % m == 1
    print("PASS rank 0 in the class, and s=2 bridge on four moduli")
    check_formulations()
    print("PASS orbit of 1, run word of 5, and the R=1 descent")


if __name__ == "__main__":
    main()
