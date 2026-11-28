#!/usr/bin/env python3
"""Contrôles exacts du cycle 008 : horizon global d'un certificat pondéré.

La preuve est dans research/cycles/cycle-008.md. Ce script ne la remplace pas.
Il vérifie le corollaire non pondéré, l'identité de montée sur un sommet partiel,
l'absence de contraction pendant la montée restante pour le poids de X21, les
constantes entières (m_*, t_*, J) du cas ρ=5/6, K=5/3, la descente
K·2^t > 3^R lorsque le premier retour sous K n a lieu après le sommet,
l'identité 3^R-2^R, et la convention t_*=0 pour K≤1/2.

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
                # K · 2^t > 3^R
                if knum * (1 << hit) <= (3**R) * kden:
                    raise AssertionError((knum, kden, L, j, hit, R))
    if seen < 100:
        raise AssertionError(("too few late returns", seen))
    print("PASS late descent K*2^t > 3^R")


def sharp_gap():
    for L in range(1, 41):
        for j in range(0, L):
            R = L - j
            n = climb(L, j)
            left = (1 << R) * (3**L - 1) - (3**R) * n
            right = (3**R) - (1 << R)
            if left != right or right <= 0:
                raise AssertionError((L, j, left, right))
    print("PASS sharp gap 3^R - 2^R")


def t_star(knum, kden):
    """Maximum de {0} et des t≥1 tels que (3/2)^t < 2K."""
    t = 0
    num, den = 1, 1
    while True:
        nxt_num, nxt_den = num * 3, den * 2
        if nxt_num * kden >= nxt_den * 2 * knum:
            return t
        t += 1
        num, den = nxt_num, nxt_den
        if t > 64:
            raise AssertionError("t_star")


def m_star(knum, kden, rnum, rden):
    """Plus petit m≥1 tel que (3/(2ρ))^m ≥ 2K/ρ."""
    m = 1
    while True:
        left = (3**m) * kden * (rden ** (m - 1))
        right = 2 * knum * (2**m) * (rnum ** (m - 1))
        if left >= right:
            return m
        m += 1
        if m > 40:
            raise AssertionError("m_star")


def convention_and_threshold():
    # K≤1/2 : l'ensemble {t≥0 : (3/2)^t < 2K} est vide, y compris à K=1/2.
    for knum, kden in ((1, 2), (1, 4), (1, 5), (2, 5)):
        if kden < 2 * knum:
            raise AssertionError(("legacy set nonempty", knum, kden))
        if t_star(knum, kden) != 0:
            raise AssertionError(("t_star", knum, kden))
    if t_star(3, 4) != 0 or t_star(5, 3) != 2 or t_star(1, 1) != 1:
        raise AssertionError("known t_star")
    # m_*=1 exactement pour K≤3/4, et le couple de X21 reste m_*=3.
    if m_star(1, 4, 1, 4) != 1 or m_star(3, 4, 1, 2) != 1:
        raise AssertionError("m_star below 3/4")
    if m_star(5, 3, 5, 6) != 3:
        raise AssertionError("m_star 5/6")
    for knum, kden, rnum, rden in (
        (4, 5, 1, 2),
        (1, 1, 1, 2),
        (5, 4, 5, 6),
        (3, 2, 9, 10),
    ):
        if t_star(knum, kden) < 1 or m_star(knum, kden, rnum, rden) < 2:
            raise AssertionError(("above 3/4", knum, kden, rnum, rden))
    # log2(3/2) > -1 et log2(3/2) > -2, et (log2 3)^2 > 1.
    if not (3 > 1 and 6 > 1 and 3 > 2):
        raise AssertionError("constant comparison")
    # Pour L≥2, 2^L-1 > 2^{L-1} : l'écart de l'exemple ρ=1/4 est strict.
    for L in range(2, 41):
        if (1 << L) - 1 <= (1 << (L - 1)):
            raise AssertionError((L,))
    print("PASS t_*=0 for K<=1/2 and the 3/4 threshold")


def main():
    unweighted()
    partial_ascent()
    x21_successor()
    constants_five_sixths()
    late_descent()
    sharp_gap()
    convention_and_threshold()


if __name__ == "__main__":
    main()
