#!/usr/bin/env python3
"""Contrôles exacts du cycle 012.

La preuve est dans research/cycles/cycle-012.md. Ce script ne la remplace pas.
Il vérifie les trois pas U(3)=5, U(7)=11, U(9)=7, les identités
U(n)+1=3(n+1)/2 pour n=3 et n=7, les comparaisons 9>7, 9>5 et 385>189,
le pas pair 6→3, l'égalité au seuil β sur 3→5, et un potentiel rapide
h(t)=1000 t qui croît en 9→7.

Usage : python3 research/checks/cycle012_lyapunov.py
"""


def v2(n):
    return (n & -n).bit_length() - 1


def T(n):
    if n % 2 == 0:
        return n // 2
    return (3 * n + 1) // 2


def U(n):
    x = 3 * n + 1
    return x >> v2(x)


def odd_identities():
    if (U(3), U(7), U(9)) != (5, 11, 7):
        raise AssertionError("accelerated images")
    if (v2(3 + 1), v2(5 + 1)) != (2, 1):
        raise AssertionError("valuations 3,5")
    if (v2(7 + 1), v2(11 + 1)) != (3, 2):
        raise AssertionError("valuations 7,11")
    if (v2(9 + 1), v2(7 + 1)) != (1, 3):
        raise AssertionError("valuations 9,7")
    if (5 + 1) * 2 != 3 * (3 + 1) or (11 + 1) * 2 != 3 * (7 + 1):
        raise AssertionError("exact height identity")
    if not (9 > 7 and 9 > 5 and 385 > 189):
        raise AssertionError("integer gaps")
    # 7*2^2000 > 9 : h(t)=1000 t increases from 9 to 7.
    if 7 * (1 << 2000) <= 9:
        raise AssertionError("fast height")


def linear_T():
    if T(6) != 3 or v2(6 + 1) != 0 or v2(3 + 1) != 2:
        raise AssertionError("step 6")
    if T(3) != 5:
        raise AssertionError("step 3")
    # At c=β, V(5)-V(3)=0 because (5+1)/(3+1)=3/2.
    if (5 + 1) * 2 != (3 + 1) * 3:
        raise AssertionError("threshold equality")
    # c<β fails at 3: β>1/2 because 9>8.
    if 9 <= 8:
        raise AssertionError("half beta")
    # Every rational c=p/q>β has V(3)>V(6), i.e. 2^{2q+2p}>7^q.
    samples = ((1, 1), (3, 4), (2, 3), (5, 8), (100, 1))
    for p, q in samples:
        if (1 << (p + q)) <= 3**q:
            raise AssertionError(("not above beta", p, q))
        if (1 << (2 * q + 2 * p)) <= 7**q:
            raise AssertionError(("six does not increase", p, q))


def main():
    odd_identities()
    print("PASS odd identities and gaps")
    linear_T()
    print("PASS linear steps 6 and 3")


if __name__ == "__main__":
    main()
