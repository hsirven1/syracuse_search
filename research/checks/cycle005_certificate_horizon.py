#!/usr/bin/env python3
"""Contrôles exacts du cycle 005 : horizon d'un certificat à poids borné.

La preuve est dans research/cycles/cycle-005.md. Ce script ne la remplace pas.
Il vérifie l'identité de montée, le rapport strict (3/2)^t, le contre-exemple
X21, et le premier retour sous (3/2)(2^L-1) pour 2≤L≤30. Le cas L=6 atteint
le premier entier autorisé par 5·2^t > 2·3^L.

Usage : python3 research/checks/cycle005_certificate_horizon.py
"""


def collatz(y):
    if y % 2 == 0:
        return y // 2
    return (3 * y + 1) // 2


def first_return(L):
    """Premier t≥1 avec 2 T^t(2^L-1) ≤ 3(2^L-1)."""
    n0 = (1 << L) - 1
    y = n0
    limit = 30 * L
    for t in range(1, limit + 1):
        y = collatz(y)
        if 2 * y <= 3 * n0:
            return t
    raise AssertionError(("pas de retour", L, limit))


def ascent_identity():
    for L in range(1, 41):
        x = (1 << L) - 1
        for t in range(0, L + 1):
            expected = (3**t) * (1 << (L - t)) - 1
            if x != expected:
                raise AssertionError((L, t, x, expected))
            if t < L:
                x = collatz(x)
        peak = (3**L) - 1
        if 2 * peak <= 3 * ((1 << L) - 1):
            raise AssertionError(("pic sous le seuil", L))


def ratio_gap():
    for L in range(1, 41):
        n0 = (1 << L) - 1
        for t in range(1, L + 1):
            x = (3**t) * (1 << (L - t)) - 1
            diff = x * (1 << t) - (3**t) * n0
            if diff != (3**t) - (1 << t) or diff <= 0:
                raise AssertionError((L, t, diff))


def counterexample():
    for L in range(2, 81):
        n0 = (1 << L) - 1
        image = 3 * (1 << (L - 1)) - 1
        if collatz(n0) != image:
            raise AssertionError((L, collatz(n0), image))
        # 3·2^{L-1} est divisible par 3 et > 2, donc pas une puissance de 2.
        if image + 1 != 3 * (1 << (L - 1)):
            raise AssertionError(L)
        gap = 5 * n0 - 3 * image
        if gap != (1 << (L - 1)) - 2 or gap < 0:
            raise AssertionError((L, gap))


def return_bound():
    sharp = {}
    for L in range(2, 31):
        t = first_return(L)
        if t <= L or 5 * (1 << t) <= 2 * (3**L):
            raise AssertionError((L, t))
        sharp[L] = t
    # L=4 : 5·2^5 = 160 < 162 = 2·3^4, et le retour est à t=6.
    if sharp[4] != 6 or 5 * (1 << 5) >= 2 * (3**4):
        raise AssertionError(sharp[4])
    # L=6 : 5·2^8 = 1280 < 1458 = 2·3^6, et le retour est à t=9.
    if sharp[6] != 9 or 5 * (1 << 8) >= 2 * (3**6):
        raise AssertionError(sharp[6])


def main():
    ascent_identity()
    print("PASS ascension 1<=L<=40")
    ratio_gap()
    print("PASS rapport strict (3/2)^t")
    counterexample()
    print("PASS contre-exemple X21, 2<=L<=80")
    return_bound()
    print("PASS retour sous 3/2, 2<=L<=30, dont L=4 et L=6")


if __name__ == "__main__":
    main()
