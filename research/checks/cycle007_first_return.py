#!/usr/bin/env python3
"""Contrôles exacts du cycle 007 : premier retour modulo 18.

La preuve est dans research/cycles/cycle-007.md. Ce script ne la remplace pas.
Il revérifie les huit produits du partage en classes, les antécédents
2^k r, l'identité P(n)=3n+1 sur un segment de N1, l'absence de collision
de P sur N2 jusqu'à 20 000, le saut vers N1 pour les impairs ≡3 mod 6
jusqu'à 30 000, et l'inégalité P(m) ≥ x pour chaque point de Σ sur la
chaîne de divisions issue d'un m de N2 jusqu'à 20 000. Ces bornes ne
sont pas la preuve. Le témoin P(16)=4 > 1 montre que l'égalité P(m)=n
n'est pas générale le long de la chaîne.

Usage : python3 research/checks/cycle007_first_return.py
"""

SIGMA = {1, 4, 5, 7, 11, 13, 16, 17}
N2 = {4, 16}
# k minimal tel que 2^k r ≡ 4 ou 16 (mod 18), puis le résidu obtenu.
EXPECTED = {
    1: (2, 4),
    4: (2, 16),
    5: (3, 4),
    7: (4, 4),
    11: (1, 4),
    13: (2, 16),
    16: (4, 4),
    17: (1, 16),
}


def f(n):
    if n % 2 == 0:
        return n // 2
    return 3 * n + 1


def in_sigma(n):
    return n % 18 in SIGMA


def first_return(n):
    x = f(n)
    for _ in range(10000):
        if in_sigma(x):
            return x
        x = f(x)
    raise AssertionError(n)


def residues():
    for r, (k, hit) in EXPECTED.items():
        if pow(2, k, 18) * r % 18 != hit or hit not in N2:
            raise AssertionError((r, k, hit))
        for j in range(1, k):
            if pow(2, j, 18) * r % 18 in N2:
                raise AssertionError((r, j))
    # Le texte imprimé groupe 7 et 16 sous les résidus 16 et 4.
    # Les deux produits valent 4.
    if (16 * 7) % 18 != 4 or (16 * 16) % 18 != 4:
        raise AssertionError("residue slip")
    if 4 % 3 != 1 or 16 % 3 != 1:
        raise AssertionError("mod 3")
    print("PASS residues")


def witnesses():
    for r, (k, _hit) in EXPECTED.items():
        m = (1 << k) * r
        if m % 18 not in N2 or first_return(m) != r:
            raise AssertionError((r, m, first_return(m)))
    # Chaînes écrites dans le cycle : 112 et 16 et 4.
    if (f(112), f(f(112)), f(f(f(112))), f(f(f(f(112))))) != (56, 28, 14, 7):
        raise AssertionError("chain 112")
    if (f(16), f(8)) != (8, 4):
        raise AssertionError("chain 16")
    if (f(4), f(2)) != (2, 1):
        raise AssertionError("chain 4")
    print("PASS witnesses")


def map_on_n1():
    for n in range(1, 3001):
        if n % 6 not in (1, 5):
            continue
        image = 3 * n + 1
        if image % 18 not in N2 or first_return(n) != image:
            raise AssertionError((n, image, first_return(n)))
    print("PASS N1")


def no_collision():
    seen = {}
    for n in range(1, 20001):
        if n % 18 not in N2:
            continue
        image = first_return(n)
        if image in seen:
            raise AssertionError((seen[image], n, image))
        seen[image] = n
    if len(seen) != 2222:
        raise AssertionError(len(seen))
    print("PASS injectivity-bound")


def return_not_below_later_sigma():
    # 16 → 8 → 4 → 2 → 1, et 1 ∈ Σ, mais P(16)=4 > 1.
    if first_return(16) != 4 or not in_sigma(1):
        raise AssertionError("witness 16")
    pairs = 0
    for m in range(2, 20001):
        if m % 18 not in N2:
            continue
        image = first_return(m)
        x = m
        while x % 2 == 0:
            x //= 2
            if in_sigma(x):
                pairs += 1
                if image < x:
                    raise AssertionError((m, x, image))
    if pairs < 2222:
        raise AssertionError(pairs)
    print("PASS return-bound")


def next_odd_in_n1():
    checked = 0
    q = 3
    while q <= 30000:
        x = 3 * q + 1
        while x % 2 == 0:
            x //= 2
        if x % 2 == 0 or x % 6 not in (1, 5):
            raise AssertionError((q, x))
        checked += 1
        q += 6
    if checked != 5000:
        raise AssertionError(checked)
    print("PASS next-odd")


if __name__ == "__main__":
    residues()
    witnesses()
    map_on_n1()
    no_collision()
    next_odd_in_n1()
    return_not_below_later_sigma()
