#!/usr/bin/env python3
"""Contrôles exacts du cycle 005 : horizon d'un certificat à poids borné.

La preuve est dans research/cycles/cycle-005.md. Ce script ne la remplace pas.
Il vérifie l'identité de montée, le rapport strict (3/2)^t, le contre-exemple
X21, et le premier retour sous (3/2)(2^L-1) pour 2≤L≤30. La comparaison
servie est 3·2^t > 2·3^L. Le cas L=2, K=1/2 contrôle que 2^L+K-1 est
positif et strictement inférieur à 2^L. L'orbite 8→4→2→1 prend trois pas.

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
        if t <= L or 3 * (1 << t) <= 2 * (3**L):
            raise AssertionError((L, t))
        if 3**L <= 1 << L:
            raise AssertionError(("écart nul", L))
        sharp[L] = t
    images = {}
    for L, t in ((2, 3), (4, 6), (6, 9)):
        y = (1 << L) - 1
        for _ in range(t):
            y = collatz(y)
        images[L] = y
    # L=2 : 3·2^2 = 12 < 18 = 2·3^2, retour à t=3, image 4.
    if sharp[2] != 3 or images[2] != 4 or 3 * (1 << 2) >= 2 * (3**2):
        raise AssertionError((sharp[2], images[2]))
    # L=4 : 3·2^5 = 96 < 162 = 2·3^4, retour à t=6, image 20.
    if sharp[4] != 6 or images[4] != 20 or 3 * (1 << 5) >= 2 * (3**4):
        raise AssertionError((sharp[4], images[4]))
    # L=6 : 3·2^8 = 768 < 1458 = 2·3^6, retour à t=9, image 91.
    if sharp[6] != 9 or images[6] != 91 or 3 * (1 << 8) >= 2 * (3**6):
        raise AssertionError((sharp[6], images[6]))
    # La forme 5·2^t > 2·3^L suit de 3·2^t > 2·3^L. On la contrôle sur les mêmes retours.
    for L, t in sharp.items():
        if 5 * (1 << t) <= 2 * (3**L):
            raise AssertionError((L, t))


def small_ratio_and_peak():
    # L=2, K=1/2. Doubler élimine le dénominateur :
    # 2(2^L+K-1)=2^{L+1}-1=7 < 8=2·2^L, et 7>0.
    # 2(K(2^L-1)+1)=5 < 12=2(K+1)2^L.
    L = 2
    twice_diff = (1 << (L + 1)) - 1
    if twice_diff <= 0 or twice_diff >= (1 << (L + 1)):
        raise AssertionError(twice_diff)
    if (1 << L) + 1 >= 3 * (1 << L):
        raise AssertionError("hauteur")
    y = (3**L) - 1
    for _ in range(3):
        y = collatz(y)
    if y != 1:
        raise AssertionError(y)


def main():
    ascent_identity()
    print("PASS ascension 1<=L<=40")
    ratio_gap()
    print("PASS rapport strict (3/2)^t")
    counterexample()
    print("PASS contre-exemple X21, 2<=L<=80")
    return_bound()
    print("PASS retour sous 3/2, 2<=L<=30, comparaison 3*2^t > 2*3^L")
    small_ratio_and_peak()
    print("PASS K=1/2 et descente 8->1 en trois pas")


if __name__ == "__main__":
    main()
