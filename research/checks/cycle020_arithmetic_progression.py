#!/usr/bin/env python3
"""Contrôles du cycle 020.

Ils vérifient, sur un rayon de raison positive, que le préfixe commun de
parités a la longueur v_2(d), que la somme d'un mot commun d'exposants
vaut au plus v_2(d)-1, qu'une chute locale ne force pas la première
descente, et que les représentants d'A3 satisfont τ_U(n)=m ≤ log2(n+1).
Ils ne prouvent pas Syracuse et ne cherchent pas de formule de τ pour
les Mersenne ni pour 5·2^k-1.

Usage : python3 research/checks/cycle020_arithmetic_progression.py
"""

from __future__ import annotations


def v2(n: int) -> int:
    if n == 0:
        raise RuntimeError("valuation de 0")
    n = abs(n)
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def T(n: int) -> int:
    if n % 2:
        return (3 * n + 1) // 2
    return n // 2


def U(n: int) -> tuple[int, int]:
    if n <= 0 or n % 2 == 0:
        raise RuntimeError(f"U attend un impair positif, reçu {n}")
    x = 3 * n + 1
    s = v2(x)
    return x >> s, s


def tau(n: int, limit: int = 64) -> int:
    start = n
    cur = n
    for t in range(1, limit + 1):
        cur, _ = U(cur)
        if cur < start:
            return t
    raise RuntimeError(f"τ({n}) > {limit}")


def parity_prefix(n: int, length: int) -> tuple[int, ...]:
    cur = n
    bits = []
    for _ in range(length):
        bits.append(cur % 2)
        cur = T(cur)
    return tuple(bits)


def common_parity_length(a: int, d: int, terms: int, limit: int) -> int:
    seqs = []
    for k in range(terms):
        n = a + k * d
        if n > 1 and n % 2 == 1:
            seqs.append(parity_prefix(n, limit))
    if len(seqs) < 2:
        raise RuntimeError("pas assez de termes")
    count = 0
    for i in range(limit):
        if len({s[i] for s in seqs}) == 1:
            count += 1
        else:
            break
    return count


def constant_chain(a: int, d: int) -> tuple[list[int], str]:
    """Valuations constantes tant que v_2(3a+1) < v_2(d)."""
    vals: list[int] = []
    for _ in range(64):
        if d % 2:
            return vals, "différence impaire"
        r = v2(d)
        s = v2(3 * a + 1)
        if s < r:
            vals.append(s)
            if s >= 2:
                return vals, "chute locale"
            a = (3 * a + 1) // 2
            d = (3 * d) // 2
        else:
            return vals, "scission"
    raise RuntimeError("chaîne trop longue")


def common_accel(a: int, d: int, limit: int = 32) -> tuple[int, ...]:
    """Exposants exacts communs à a et a+d, jusqu'à la première divergence."""
    n, m = a, a + d
    word: list[int] = []
    for _ in range(limit):
        n, sn = U(n)
        m, sm = U(m)
        if sn != sm:
            break
        word.append(sn)
    return tuple(word)


def accel_prefix(n: int, steps: int) -> tuple[int, ...]:
    cur = n
    out = []
    for _ in range(steps):
        cur, s = U(cur)
        out.append(s)
    return tuple(out)


def q_residue(m: int) -> int:
    mod = 1 << (m + 1)
    target = 1 + (1 << m)
    q = (target * pow(pow(3, m, mod), -1, mod)) % mod
    if q % 2 == 0:
        raise RuntimeError(f"résidu pair pour m={m}")
    while (4**m - 3**m) * q <= (1 << m) - 1:
        q += mod
    return q


def main() -> None:
    # Progression 3+4k : r=2, un pas commun de valuation 1, puis scission.
    assert v2(4) == 2
    assert common_parity_length(3, 4, 24, 8) == 2
    prefixes = []
    for k in range(12):
        n = 3 + 4 * k
        prefixes.append(accel_prefix(n, 3))
    assert len({p[0] for p in prefixes}) == 1 and prefixes[0][0] == 1
    assert len({p[1] for p in prefixes}) > 1
    assert tau(3) == 2 and tau(7) == 4
    chain, kind = constant_chain(3, 4)
    assert chain == [1] and kind == "scission"
    print("PASS 3+4k shares two parities, one climb, then the valuation splits")

    # Raison 16, valuation constante 2 : descente au premier pas.
    assert v2(3 * 9 + 1) == 2 and v2(16) == 4
    chain, kind = constant_chain(9, 16)
    assert chain == [2] and kind == "chute locale"
    for k in range(10):
        n = 9 + 16 * k
        cur, s = U(n)
        assert s == 2 and cur < n and tau(n) == 1
        nxt, s2 = U(cur)
        assert s2 == 1 and nxt > cur
    assert common_accel(9, 16)[:2] == (2, 1)
    assert common_parity_length(9, 16, 16, 8) == 4
    print("PASS 9+16k has τ=1 and a common prefix longer than the descent")

    # n≡1 mod 4 : τ=1, même si l'exposant n'est pas constant.
    for n in (5, 9, 13, 17, 25, 41):
        assert n % 4 == 1 and n > 1 and tau(n) == 1
    assert common_parity_length(1, 4, 16, 8) == 2
    varied = {U(1 + 4 * k)[1] for k in range(1, 12)}
    assert len(varied) > 1
    print("PASS n≡1 mod 4 has τ=1 on the sampled progression")

    # Le préfixe commun de parités ne dépasse pas v_2(d).
    samples = ((3, 4), (7, 8), (9, 16), (11, 8), (15, 32), (5, 8), (1, 4))
    for a, d in samples:
        r = v2(d)
        length = common_parity_length(a, d, 20, r + 4)
        assert length == r
        vals, kind = constant_chain(a, d)
        assert sum(vals) <= r - 1
        if kind == "chute locale" and len(vals) == 1:
            assert vals[0] >= 2
            for k in range(8):
                n = a + k * d
                if n > 1 and n % 2 == 1:
                    assert tau(n) == 1
        if kind == "scission":
            observed = []
            for k in range(16):
                n = a + k * d
                if n > 1 and n % 2 == 1:
                    observed.append(accel_prefix(n, len(vals) + 1))
            for i in range(len(vals)):
                assert len({p[i] for p in observed}) == 1
                assert observed[0][i] == vals[i]
            assert len({p[len(vals)] for p in observed}) > 1
    print("PASS common parity prefixes and constant valuation chains stay within v_2(d)")

    # Diagonale d'A3 : corollaire du certificat déjà écrit, contrôle fini.
    examples = {1: 9, 2: 19, 3: 87, 4: 15, 5: 863}
    for m in range(1, 41):
        q = q_residue(m)
        n = (1 << m) * q - 1
        assert (4**m - 3**m) * q > (1 << m) - 1
        assert n + 1 >= (1 << m)
        cur = n
        for t in range(m - 1):
            assert cur == (3**t) * (1 << (m - t)) * q - 1
            assert cur > n or t == 0
            cur, s = U(cur)
            assert s == 1 and cur > n
        assert cur == (3 ** (m - 1)) * 2 * q - 1
        x = 3 * cur + 1
        assert v2(x) == m + 1
        final = x >> (m + 1)
        assert final == ((3**m) * q - 1) >> m
        assert final < n
        if m in examples:
            assert n == examples[m]
        if m >= 2:
            assert n % 4 == 3
    second = 87 + (1 << 7)
    assert tau(87) == 3 and tau(second) == 3
    assert second == (1 << 3) * (11 + (1 << 4)) - 1
    print("PASS A3 representatives 1≤m≤40 have τ=m and n+1≥2^m")

    # Le préfixe de Mersenne n'est pas la descente. Identité A2, un seul h.
    h = 5
    n = (1 << h) - 1
    cur = n
    for t in range(h - 1):
        assert cur == (3**t) * (1 << (h - t)) - 1
        cur, s = U(cur)
        assert s == 1 and cur > n
    assert tau(n) == 35
    print("PASS the Mersenne prefix of 31 stays above the start and τ=35")

    # X53 : la chute locale ne borne pas τ. Identités pour tout k≥0.
    for k in range(12):
        n = 11 + 16 * k
        u1, s1 = U(n)
        u2, s2 = U(u1)
        assert (s1, s2) == (1, 2)
        assert u1 == 17 + 24 * k and u2 == 13 + 18 * k
        assert 3 * n + 1 == 34 + 48 * k
        assert 3 * u1 + 1 == 52 + 72 * k
        assert u2 - n == 2 + 2 * k > 0
        assert u1 > u2
    assert common_accel(11, 16) == (1, 2)
    n = 27
    cur = n
    seen = []
    for _ in range(4):
        cur, _ = U(cur)
        seen.append(cur)
    assert seen == [41, 31, 47, 71]
    assert all(x > 27 for x in seen)
    assert tau(3) == 2 and tau(7) == 4 and tau(27) == 37 and tau(31) == 35

    for k in range(12):
        n = 27 + 32 * k
        u1, s1 = U(n)
        u2, s2 = U(u1)
        u3, s3 = U(u2)
        assert (s1, s2, s3) == (1, 2, 1)
        assert (u1, u2, u3) == (41 + 48 * k, 31 + 36 * k, 47 + 54 * k)
        assert u1 - n == 14 + 16 * k > 0
        assert u2 - n == 4 + 4 * k > 0
        assert u3 - n == 20 + 22 * k > 0
        assert u2 < u1
    assert common_accel(27, 32) == (1, 2, 1)
    _, s4_even = U(47)
    _, s4_odd = U(47 + 54)
    assert s4_even == 1 and s4_odd >= 2
    assert tau(59) == 4
    print("PASS a later common drop stays above the start on 11+16k and 27+32k")

    # Somme des exposants et longueur exacte des parités, sur un rayon.
    for a in range(3, 64, 2):
        for d in range(2, 66, 2):
            word = common_accel(a, d)
            assert sum(word) <= v2(d) - 1
            assert common_parity_length(a, d, 2, v2(d) + 3) == v2(d)
            if word:
                images_a = a
                images_b = a + d
                for _ in word:
                    images_a, _ = U(images_a)
                    images_b, _ = U(images_b)
                assert images_b - images_a == (3 ** len(word)) * d // 2 ** sum(word)
                assert v2(images_b - images_a) == v2(d) - sum(word)
    print("PASS common accelerated sums stay ≤ v_2(d)-1 and parity prefixes equal v_2(d)")

    # X54 : deux rayons de raison 4 couvrent les impairs de l'échantillon.
    odds = set(range(1, 401, 2))
    cover = {1 + 4 * k for k in range(200)} | {3 + 4 * k for k in range(200)}
    assert odds <= cover
    assert tau(5) == 1 and tau(3) == 2 and tau(7) == 4
    print("PASS 1+4k and 3+4k cover the sampled positive odds")

    # X55 : k≥0 et d<0 peut laisser un singleton.
    assert [3 - 4 * k for k in range(8) if 3 - 4 * k > 1] == [3]
    bits = []
    cur = 3
    for _ in range(3):
        bits.append(cur % 2)
        cur = T(cur)
    assert bits == [1, 1, 0] and v2(4) == 2 and v2(10) == 1
    assert [5 - 4 * k for k in range(8) if 5 - 4 * k > 1] == [5]
    assert v2(16) == 4 and v2(4) == 2
    print("PASS k≥0 with a negative step can leave the singletons {3} and {5}")


if __name__ == "__main__":
    main()
