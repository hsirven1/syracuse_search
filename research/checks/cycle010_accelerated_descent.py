#!/usr/bin/env python3
"""Contrôles exacts du cycle 010 : préfixe de 5·2^k-1 et second bloc.

La preuve est dans research/cycles/cycle-010.md. Ce script ne la remplace pas.
Il vérifie la forme U^t = 5·3^t·2^{k-t}-1 pour t < k, la valuation
v_2(5·3^k-1) ∈ {1, 2}, la sortie U^k, la jonction des indices impair et
suivant, l'inégalité τ(n_k) ≥ τ(n_{k+1}) pour k impair ≥ 3, le second
bloc U^{k+s} = 3^s(5·3^k+1)/2^{s+1}-1 pour 0 ≤ s < L et τ ≥ k+L, les
exposants extraits au pas k+2 (4 et 1 pour k = 3 et 5, distincts des
valuations 6 et 3 du numérateur 5·3^{k+2}+1), et le
relevé fini 2 ≤ k ≤ 1000 des temps τ ≤ 2k. Ce relevé n'est pas une preuve
pour k > 1000, ni de l'infinité de τ > 2k.

Usage : python3 research/checks/cycle010_accelerated_descent.py
"""


def v2(n):
    return (n & -n).bit_length() - 1


def U(n):
    x = 3 * n + 1
    return x >> v2(x)


def n_of(k):
    return 5 * (1 << k) - 1


_TAU = {}


def tau(k):
    if k in _TAU:
        return _TAU[k]
    n0 = n_of(k)
    n = n0
    t = 0
    while n >= n0:
        n = U(n)
        t += 1
        if t > 100000:
            raise AssertionError(("tau unbounded in the cap", k))
    _TAU[k] = t
    return t


def prefix_and_exit():
    for k in range(2, 61):
        n0 = n_of(k)
        x = n0
        for s in range(1, k):
            x = U(x)
            expect = 5 * pow(3, s) * (1 << (k - s)) - 1
            if x != expect or x <= n0:
                raise AssertionError(("prefix", k, s, x, expect))
        eps = 1 if k % 2 else 2
        if v2(5 * pow(3, k) - 1) != eps:
            raise AssertionError(("valuation", k, eps))
        xk = U(x)
        expect = (5 * pow(3, k) - 1) >> eps
        if xk != expect:
            raise AssertionError(("exit", k, xk, expect))
        if k >= 3 and xk <= n0:
            raise AssertionError(("still above", k, xk, n0))
        if k == 2 and xk != 11:
            raise AssertionError(("k=2", xk))
        if k == 3 and xk != 67:
            raise AssertionError(("k=3", xk))


def merge_and_order():
    # k = 1 is the identity only: U(9) = 7 < 9, so the order on τ fails.
    n1 = n_of(1)
    if U(n1) != 7 or U(U(n1)) != 11 or U(U(n_of(2))) != 11:
        raise AssertionError("junction at k=1")
    if tau(1) != 1 or tau(2) != 2:
        raise AssertionError("tau at k=1,2")
    for k in range(3, 60, 2):
        x = n_of(k)
        for _ in range(k + 1):
            x = U(x)
        y = n_of(k + 1)
        for _ in range(k + 1):
            y = U(y)
        expect = (5 * pow(3, k + 1) - 1) >> 2
        if x != y or x != expect or x <= n_of(k + 1):
            raise AssertionError(("merge", k, x, y, expect))
        if tau(k) < tau(k + 1):
            raise AssertionError(("order", k, tau(k), tau(k + 1)))
    # Three odd exponents, three valuations: the next block is not uniform.
    vals = [v2(5 * pow(3, k) + 1) for k in (1, 3, 5)]
    if vals != [4, 3, 6]:
        raise AssertionError(("second block", vals))


# Relevé exact 2 ≤ k ≤ 1000. Toute autre valeur de cet intervalle vérifie τ > 2k.
LEQ_2K = (
    (2, 2), (3, 5), (4, 5), (7, 14), (8, 14), (11, 21), (12, 21),
    (17, 32), (18, 32), (19, 31), (20, 31), (27, 54), (28, 51),
    (52, 104), (73, 145), (74, 142), (83, 152), (84, 152),
    (206, 388), (207, 388), (208, 388), (232, 463), (235, 463),
    (236, 462), (324, 648),
)


def second_block():
    # Orbit of n_5 through the first descent. Not a proof for other k.
    n = n_of(5)
    seq = [n]
    for _ in range(13):
        n = U(n)
        seq.append(n)
    if seq != [
        159, 239, 359, 539, 809, 607, 911, 1367, 2051, 3077, 577, 433, 325, 61
    ]:
        raise AssertionError(("orbit5", seq))
    if v2(5 * pow(3, 757) + 1) != 16:
        raise AssertionError("valuation 757")
    for k in range(1, 1000, 2):
        base = 5 * pow(3, k) + 1
        L = v2(base) - 1
        if L < 2:
            raise AssertionError(("L", k, L))
        x = n_of(k)
        for _ in range(k):
            x = U(x)
        for s in range(L):
            if base % 2 ** (s + 1) != 0:
                raise AssertionError(("div", k, s))
            expect = pow(3, s) * base // 2 ** (s + 1) - 1
            if s:
                x = U(x)
            if x != expect:
                raise AssertionError(("block", k, s, x, expect))
            if k >= 3 and x <= n_of(k):
                raise AssertionError(("above", k, s, x))
        m = base >> (L + 1)
        if m % 2 == 0:
            raise AssertionError(("m", k, m))
        exit_num = pow(3, L) * m - 1
        if U(x) != exit_num >> v2(exit_num):
            raise AssertionError(("exit block", k, U(x)))
        y = n_of(k)
        for _ in range(k + 2):
            y = U(y)
        num = 5 * pow(3, k + 2) + 1
        if y != num >> v2(num):
            raise AssertionError(("k+2", k, y, v2(num)))
        if L >= 3 and v2(num) != 3:
            raise AssertionError(("val3", k, L, v2(num)))
        if L == 2 and v2(num) < 4:
            raise AssertionError(("val4", k, v2(num)))
        if k >= 3:
            if tau(k) < k + L or tau(k + 1) < k + L or tau(k) < tau(k + 1):
                raise AssertionError(("bound", k, L, tau(k), tau(k + 1)))
            z = n_of(k + 1)
            floor = z
            for _t in range(1, k + L):
                z = U(z)
                if z <= floor:
                    raise AssertionError(("partner", k, _t, z, floor))
    # 6 et 3 sont v_2(5*3**(k+2)+1). Le pas de U extrait v_2(3y+1).
    for k, numerator_val, extracted in ((3, 6, 4), (5, 3, 1)):
        y = n_of(k)
        for _ in range(k + 1):
            y = U(y)
        num = 5 * pow(3, k + 2) + 1
        if v2(num) != numerator_val or 3 * y + 1 != num // 4:
            raise AssertionError(("numerator", k, v2(num), 3 * y + 1, num))
        if v2(3 * y + 1) != extracted:
            raise AssertionError(("extracted", k, v2(3 * y + 1)))
    if tau(3) != 5:
        raise AssertionError(tau(3))
    x = n_of(3)
    for _ in range(5):
        x = U(x)
    if x != 19:
        raise AssertionError(("k3", x))
    x = n_of(5)
    for _ in range(7):
        x = U(x)
    if x != 1367:
        raise AssertionError(("k5", x))
    if tau(757) != 1840 or tau(758) != 1840:
        raise AssertionError((tau(757), tau(758)))


def survey():
    found = []
    best = (2, 2)
    for k in range(2, 1001):
        t = tau(k)
        if t <= 2 * k:
            found.append((k, t))
        if t * best[0] > best[1] * k:
            best = (k, t)
    if tuple(found) != LEQ_2K:
        raise AssertionError(("survey", found))
    if best != (21, 110):
        raise AssertionError(("max ratio", best))
    if tau(5) != 13:
        raise AssertionError(tau(5))


def main():
    prefix_and_exit()
    print("PASS prefix, exit valuation and U^k > n_k for 3 <= k <= 60")
    merge_and_order()
    print("PASS junction at step k+1 and tau(n_k) >= tau(n_{k+1}) for odd k = 3..59")
    second_block()
    print("PASS second block 0 <= s < L, tau >= k+L for odd k = 3..999, tau(757)=1840")
    survey()
    print("PASS finite survey 2 <= k <= 1000: 25 values with tau <= 2k, max tau/k at k=21")
    print("PASS k=5 has tau=13 > 10")


if __name__ == "__main__":
    main()
