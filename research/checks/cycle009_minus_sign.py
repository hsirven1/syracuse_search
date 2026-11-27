#!/usr/bin/env python3
"""Contrôles exacts du cycle 009 : signe moins au seuil log2(3).

La preuve est dans research/cycles/cycle-009.md. Ce script ne la remplace pas.
Il vérifie 3^64, le run r_2=29, la chaîne entière r_9≥80, le déséquilibre
des facteurs de longueur 66, les neuf premiers runs, 4 r_k > o_k jusqu'à
k=18, l'écart du candidat σ=2 (valuation 66, distincte de 96), les témoins
2+2^67 et 2+2^66, la constante (2^66+2)/3, et U(1)=1.

Usage : python3 research/checks/cycle009_minus_sign.py
"""


def isqrt(n):
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid * mid <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo


def floor_beta_times(o):
    m = (3 ** o).bit_length() - 1
    if 2 ** m > 3 ** o or 3 ** o >= 2 ** (m + 1):
        raise AssertionError(("log2", o))
    return m - o


def v2(n):
    n = abs(n)
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def runs(limit):
    o = 0
    out = []
    for k in range(1, limit + 1):
        if k == 1:
            r = 64
        else:
            r = floor_beta_times(o) - isqrt(o)
        out.append((k, o, r))
        o += r
    return out


def powers_of_three():
    p16 = 43046721
    if p16 != 3 ** 16:
        raise AssertionError("3^16")
    p32 = p16 * p16
    if p32 != 1853020188851841 or p32 != 3 ** 32:
        raise AssertionError("3^32")
    p64 = p32 * p32
    if p64 != 3433683820292512484657849089281 or p64 != 3 ** 64:
        raise AssertionError("3^64")
    if not (2 ** 101 <= p64 < 2 ** 102):
        raise AssertionError("bits")
    if (p64.bit_length() - 1) - 64 != 37:
        raise AssertionError("floor beta 64")


def chain_and_imbalance():
    seq = runs(12)
    if seq[1][2] != 29 or seq[1][1] != 64:
        raise AssertionError(("r2", seq[1]))
    # Chaîne du cycle, à partir de r_k > o_k/4.
    o = 64
    lower_r = []
    for _ in range(8):
        # plus petit entier strictement supérieur à o/4
        bound = o // 4 + 1
        lower_r.append(bound)
        o = o + bound
    actual = [r for _, _, r in seq[1:9]]
    if any(r < b for r, b in zip(actual, lower_r)):
        raise AssertionError((actual, lower_r))
    if lower_r[-1] < 66 or actual[3] < 66:
        raise AssertionError(("run long", lower_r[-1], actual[3]))
    # Préfixe 0 1^64 0 : 64 uns sur 66 symboles.
    # Un run ultérieur ≥ 66 fournit 1^66.
    if sum(1 for bit in [0] + [1] * 64 + [0] if bit == 1) != 64:
        raise AssertionError("prefix ones")
    if len([0] + [1] * 64 + [0]) != 66:
        raise AssertionError("prefix length")
    # actual[0] = r_2, donc actual[2] = r_4.
    if actual[2] < 66:
        raise AssertionError(("r4", actual[2]))
    if seq[3][0] != 4 or seq[3][2] < 66:
        raise AssertionError(("k4", seq[3]))


def sigma_two_valuation():
    """Le candidat σ=2 donne v_2(A_2)=66. Le reste de la série vaut 96."""
    seq = runs(4)
    o = [0]
    rs = []
    for _, oi, r in seq:
        rs.append(r)
        o.append(oi + r)
    # o[0]=o_1=0, o[1]=o_2, o[2]=o_3, o[3]=o_4 ; rs[1]=r_2.
    if o[1] != 64 or rs[1] != 29 or o[2] != 93:
        raise AssertionError((o, rs))
    if rs[2] * 4 <= o[2] or o[3] < o[2] + 1 or 4 + o[3] <= 96:
        raise AssertionError(("reste", o, rs))
    # P_2 = 2^{1+0} 3^{64} + 2^{2+64}, candidat (a, b) = (2, 1).
    p2 = 2 * 3 ** 64 + 2 ** 66
    a2 = 2 * 3 ** 64 - p2
    if a2 != -(2 ** 66) or v2(a2) != 66 or v2(a2) == 96:
        raise AssertionError(("A2", a2, v2(a2)))
    if v2(2 ** (3 + o[2])) != 96:
        raise AssertionError("terme 3")
    if v2(2 ** (4 + o[3])) <= 96:
        raise AssertionError("terme 4")


def review_witnesses():
    seq = runs(18)
    expected = [64, 29, 45, 69, 107, 166, 259, 405, 636]
    got = [r for _, _, r in seq[:9]]
    if got != expected:
        raise AssertionError(got)
    for k, o, r in seq[1:]:
        if 4 * r <= o:
            raise AssertionError((k, o, r))
    threshold = (2 ** 66 + 2) // 3
    high = 2 + 2 ** 67
    boundary = 2 + 2 ** 66
    if v2(high - 2) != 67 or high <= threshold:
        raise AssertionError("2+2^67")
    if v2(boundary - 2) != 66 or boundary <= threshold:
        raise AssertionError("2+2^66")
    one = 3 * 1 + 1
    if v2(one) != 2 or one // 4 != 1:
        raise AssertionError("U(1)")
    for n in (5, 9, 13):
        step = 3 * n + 1
        u = step
        while u % 2 == 0:
            u //= 2
        if n % 4 != 1 or u >= n:
            raise AssertionError((n, u))


def height_constant():
    mod = 2 ** 66
    if mod % 3 != 1:
        raise AssertionError("2^66 mod 3")
    floor_third = (mod - 1) // 3
    if 3 * floor_third != mod - 1:
        raise AssertionError("division")
    minimum = floor_third + 1
    if 3 * minimum != mod + 2:
        raise AssertionError("constante")
    if minimum <= 2 ** 64:
        raise AssertionError("au-dessus de 2^64")
    # |a|+2b ≤ 3M ≤ 2^66-1 ne peut pas atteindre 2^66.
    if 3 * floor_third >= mod:
        raise AssertionError("contradiction non stricte")


def main():
    powers_of_three()
    print("PASS 3^64 : 2^101 <= 3^64 < 2^102, floor(64 log2(3/2))=37")
    chain_and_imbalance()
    print("PASS chaine r_k > o_k/4 : r_9>=80, et r_4>=66 ; facteurs 64 uns contre 66")
    sigma_two_valuation()
    print("PASS candidat sigma=2 : v_2(A_2)=66, reste de la serie de valuation 96")
    review_witnesses()
    print("PASS neuf runs, 4 r_k > o_k jusqu'a k=18, temoins 2+2^67 et 2+2^66")
    height_constant()
    print("PASS max(|a|,b) >= (2^66+2)/3 > 2^64")
    print("PASS U(1)=1, et U(n)<n pour n=5, 9, 13")


if __name__ == "__main__":
    main()
