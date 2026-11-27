#!/usr/bin/env python3
"""Contrôles exacts du cycle 010 : préfixe de 5·2^k-1 et comparaison à 2k.

La preuve est dans research/cycles/cycle-010.md. Ce script ne la remplace pas.
Il vérifie la forme U^t = 5·3^t·2^{k-t}-1 pour t < k, la valuation
v_2(5·3^k-1) ∈ {1, 2}, la sortie U^k, la jonction des indices impair et
suivant, l'inégalité τ(n_k) ≥ τ(n_{k+1}) pour k impair ≥ 3, et le relevé
fini 2 ≤ k ≤ 1000 des temps τ ≤ 2k. Ce relevé n'est pas une preuve pour
k > 1000.

Usage : python3 research/checks/cycle010_accelerated_descent.py
"""


def v2(n):
    return (n & -n).bit_length() - 1


def U(n):
    x = 3 * n + 1
    return x >> v2(x)


def n_of(k):
    return 5 * (1 << k) - 1


def tau(k):
    n0 = n_of(k)
    n = n0
    t = 0
    while n >= n0:
        n = U(n)
        t += 1
        if t > 100000:
            raise AssertionError(("tau unbounded in the cap", k))
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
    survey()
    print("PASS finite survey 2 <= k <= 1000: 25 values with tau <= 2k, max tau/k at k=21")
    print("PASS k=5 has tau=13 > 10")


if __name__ == "__main__":
    main()
