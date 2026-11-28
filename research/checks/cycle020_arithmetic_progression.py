#!/usr/bin/env python3
"""Contrôles du cycle 020.

Ils vérifient, sur des progressions de raison fixe, que le préfixe commun
de parités ne dépasse pas v_2(d), que la chaîne de valuations constantes
s'arrête par une descente uniforme ou par une scission, et que les
représentants d'A3 satisfont τ_U(n)=m ≤ log2(n+1). Ils ne prouvent pas
Syracuse et ne cherchent pas de formule de τ pour les Mersenne ni pour
5·2^k-1.

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
                return vals, "descente"
            a = (3 * a + 1) // 2
            d = (3 * d) // 2
        else:
            return vals, "scission"
    raise RuntimeError("chaîne trop longue")


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
    assert chain == [2] and kind == "descente"
    for k in range(10):
        n = 9 + 16 * k
        cur, s = U(n)
        assert s == 2 and cur < n and tau(n) == 1
    assert common_parity_length(9, 16, 16, 8) == 4
    print("PASS 9+16k has constant valuation 2 and τ=1")

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
        assert vals.count(1) <= r - 1
        if kind == "descente":
            assert len(vals) <= r
            for k in range(8):
                n = a + k * d
                if n > 1 and n % 2 == 1:
                    assert tau(n) == len(vals)
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


if __name__ == "__main__":
    main()
