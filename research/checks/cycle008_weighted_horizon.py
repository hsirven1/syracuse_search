#!/usr/bin/env python3
"""Contrôles exacts du cycle 008 : horizon global d'un certificat pondéré.

La preuve est dans research/cycles/cycle-008.md. Ce script ne la remplace pas.
Il vérifie le corollaire non pondéré, l'identité de montée sur un sommet partiel,
l'absence de contraction pendant la montée restante pour le poids de X21, les
constantes entières (m_*, t_*, J) du cas ρ=5/6, K=5/3, et la descente
2^{t+1} K > 3^R lorsque le premier retour sous K n a lieu après le sommet.

Usage : python3 research/checks/cycle008_weighted_horizon.py
"""


def collatz(y):
    if y % 2 == 0:
        return y // 2
    return (3 * y + 1) // 2


def climb(L, j):
    return (3**j) * (1 << (L - j)) - 1


def unweighted():
    rhos = [(1, 2), (2, 3), (5, 6), (9, 10)]
    for num, den in rhos:
        for L in range(2, 41):
            n0 = (1 << L) - 1
            y = n0
            hit = None
            for t in range(1, 20000):
                y = collatz(y)
                if y * den <= num * n0:
                    hit = t
                    break
            if hit is None or hit <= L:
                raise AssertionError(("unweighted", num, den, L, hit))
            # ρ · 2^t > 3^L
            if num * (1 << hit) <= den * (3**L):
                raise AssertionError(("rho-power", num, den, L, hit))
    print("PASS unweighted rho*2^t > 3^L")


def partial_ascent():
    for L in range(1, 31):
        for j in range(0, L + 1):
            x = climb(L, j)
            for t in range(0, L - j + 1):
                expected = (3 ** (j + t)) * (1 << (L - j - t)) - 1
                if x != expected:
                    raise AssertionError((L, j, t, x, expected))
                if t < L - j:
                    x = collatz(x)
            n = climb(L, j)
            for t in range(1, L - j + 1):
                image = (3 ** (j + t)) * (1 << (L - j - t)) - 1
                if (image << t) - (3**t) * n != (3**t) - (1 << t):
                    raise AssertionError(("gap", L, j, t))
                if (image << t) <= (3**t) * n:
                    raise AssertionError(("ratio", L, j, t))
    print("PASS partial ascent")


def x21_successor():
    """W=2 sur les Mersenne, W=1 ailleurs, ρ=5/6. Le successeur ne contracte pas avant la fin de la montée."""
    for L in range(2, 31):
        n1 = 3 * (1 << (L - 1)) - 1
        if (n1 + 1) & n1 == 0:
            raise AssertionError(("successor mersenne", L))
        for t in range(1, L):
            image = (3 ** (1 + t)) * (1 << (L - 1 - t)) - 1
            if (image + 1) & image == 0:
                raise AssertionError(("image mersenne", L, t))
            # image > (5/6) n1, et W=1 des deux côtés
            if 6 * image <= 5 * n1:
                raise AssertionError(("contracts", L, t, image, n1))
    print("PASS x21 successor stays above 5/6 through the climb")


def constants_five_sixths():
    # (9/5)^m ≥ 4, smallest m. (3/2)^t < 10/3, largest t.
    m = 1
    num, den = 9, 5
    while num < 4 * den:
        m += 1
        num *= 9
        den *= 5
        if m > 20:
            raise AssertionError("m")
    if m != 3:
        raise AssertionError(m)
    t = 0
    num, den = 1, 1  # (3/2)^t = num/den
    # (3/2)^{t+1} < 10/3 iff 9 num < 20 den
    while 9 * num < 20 * den:
        t += 1
        num *= 3
        den *= 2
    if t != 2:
        raise AssertionError(t)
    if (m - 1) * t != 4:
        raise AssertionError("J")
    print("PASS constants m*=3 t*=2 J=4")


def late_descent():
    ks = [(1, 2), (1, 1), (3, 2), (5, 3), (2, 1), (3, 1), (10, 1)]
    seen = 0
    for knum, kden in ks:
        for L in range(2, 18):
            for j in range(0, L):
                n = climb(L, j)
                R = L - j
                y = n
                hit = None
                for t in range(1, 30 * L):
                    y = collatz(y)
                    if y * kden <= knum * n:
                        hit = t
                        break
                if hit is None:
                    raise AssertionError(("no return", knum, kden, L, j))
                if hit <= R:
                    continue
                seen += 1
                # 2^{t+1} K > 3^R
                if (1 << (hit + 1)) * knum <= (3**R) * kden:
                    raise AssertionError((knum, kden, L, j, hit, R))
    if seen < 100:
        raise AssertionError(("too few late returns", seen))
    print("PASS late descent 2^(t+1) K > 3^R")


def main():
    unweighted()
    partial_ascent()
    x21_successor()
    constants_five_sixths()
    late_descent()


if __name__ == "__main__":
    main()
