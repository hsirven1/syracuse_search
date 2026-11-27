#!/usr/bin/env python3
"""Contrôles exacts du cycle 012.

La preuve est dans research/cycles/cycle-012.md. Ce script ne la remplace pas.
Il vérifie les trois pas U(3)=5, U(7)=11, U(9)=7, les identités
U(n)+1=3(n+1)/2 pour n=3 et n=7, les comparaisons 9>7, 9>5 et 385>189,
le pas pair 6→3, l'égalité au seuil β sur 3→5, un potentiel rapide
h(t)=1000 t qui croît en 9→7, et la famille x=64A-5, y=96A-7, z=72A-5.

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


def affine_branch():
    samples = ((1, 1), (3, 4), (2, 3), (5, 8), (100, 1))
    for p, q in samples:
        if (1 << (p + q)) <= 3**q:
            raise AssertionError(("not above beta", p, q))
    for A in range(1, 501):
        check_one(A)
        for p, q in samples:
            z = 72 * A - 5
            if (z + 1) ** q * (1 << (2 * p)) <= (2 * z + 1) ** q:
                raise AssertionError(("even step", p, q, A))
    for M in range(1, 101):
        for q in range(1, 101):
            check_one(M * q, M)
    # A=2 changes ω: 123=3*41 and 139 is prime. One path does not fix counters.
    if 3 * 41 != 123:
        raise AssertionError("123")
    if not is_prime(139):
        raise AssertionError("139")


def check_one(A, modulus=None):
    x = 64 * A - 5
    y = 96 * A - 7
    z = 72 * A - 5
    if 3 * x + 1 != 2 * y or 3 * y + 1 != 4 * z:
        raise AssertionError(("identity", A))
    if x % 2 == 0 or y % 2 == 0 or z % 2 == 0:
        raise AssertionError(("parity", A))
    if U(x) != y or U(y) != z:
        raise AssertionError(("U", A))
    if T(x) != y or T(y) != 2 * z or T(2 * z) != z:
        raise AssertionError(("T", A))
    if z <= x or y <= x or 2 * z <= y:
        raise AssertionError(("growth", A))
    if (v2(x + 1), v2(y + 1), v2(z + 1), v2(2 * z + 1)) != (2, 1, 2, 0):
        raise AssertionError(("valuation", A))
    if (y + 1) * 2 != (x + 1) * 3 or (2 * z + 1) * 2 != (y + 1) * 3:
        raise AssertionError(("odd ratios", A))
    if z + 1 != 4 * (18 * A - 1) or 2 * z + 1 != 9 * (16 * A - 1):
        raise AssertionError(("even ratio", A))
    if 18 * A - 1 <= 16 * A - 1 or 9 * (z + 1) <= 4 * (2 * z + 1):
        raise AssertionError(("beta gap", A))
    if modulus is not None and z % modulus != x % modulus:
        raise AssertionError(("residue", A, modulus))


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1 if d == 2 else 2
    return True


def main():
    odd_identities()
    print("PASS odd identities and gaps")
    linear_T()
    print("PASS linear steps 6 and 3")
    affine_branch()
    print("PASS affine branch without prime counters")


if __name__ == "__main__":
    main()
