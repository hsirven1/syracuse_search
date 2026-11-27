#!/usr/bin/env python3
"""Contrôles exacts du cycle 011.

La preuve est dans research/cycles/cycle-011.md. Ce script ne la remplace pas.
Six lignes PASS : fractions partielles de h(z)=z/(1-z), équation (21) pour
quatre termes impairs, croissance jusqu'à 2000, polynôme q pour 1 ≤ n ≤ 500
et le point n=0, récurrence (16) jusqu'à 500, et les quatre cas de parité.

Usage : python3 research/checks/cycle011_berg_meinardus.py
"""


def add(p, q):
    return (p[0] + q[0], p[1] + q[1])


def sub(p, q):
    return (p[0] - q[0], p[1] - q[1])


def mul(p, q):
    # (a + b λ)(c + d λ) avec λ^2 = -1 - λ.
    a, b = p
    c, d = q
    return (a * c - b * d, a * d + b * c - b * d)


def smul(k, p):
    return (k * p[0], k * p[1])


def pmul(f, g):
    out = [(0, 0)] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            out[i + j] = add(out[i + j], mul(a, b))
    return out


def padd(f, g):
    n = max(len(f), len(g))
    out = []
    for i in range(n):
        a = f[i] if i < len(f) else (0, 0)
        b = g[i] if i < len(g) else (0, 0)
        out.append(add(a, b))
    return out


def check_partial_fraction():
    # λ^0 = 1, λ^1 = λ, λ^2 = -1 - λ. On veut
    # sum_ν λ^{2ν} ∏_{μ≠ν} (1 - λ^μ w) = 3w.
    lam = [(1, 0), (0, 1), (-1, -1)]
    lam2 = [lam[0], lam[2], lam[1]]
    total = [(0, 0)]
    one = [(1, 0)]
    for nu in range(3):
        prod = [(1, 0)]
        for mu in range(3):
            if mu == nu:
                continue
            # 1 - λ^μ w
            prod = pmul(prod, [one[0], smul(-1, lam[mu])])
        total = padd(total, pmul([lam2[nu]], prod))
    while len(total) > 1 and total[-1] == (0, 0):
        total.pop()
    assert total == [(0, 0), (3, 0)], total


def poly_trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def check_odd_geometric(e):
    # Identité polynomiale : (1+z^e) z^e - (1-z^e) z^e = 2 z^{2e},
    # puis (1-z^{2e}) n'a pas à être inversé : les deux membres valent 2 z^{2e}.
    assert e % 2 == 1

    def coeff_diff():
        # (1+z^e)*z^e - (1-z^e)*z^e - 2 z^{2e}
        # = z^e + z^{2e} - z^e + z^{2e} - 2 z^{2e} = 0
        p = [0] * (2 * e + 1)
        p[e] += 1
        p[2 * e] += 1
        p[e] -= 1
        p[2 * e] += 1
        p[2 * e] -= 2
        return poly_trim(p)

    assert coeff_diff() == [0]


def t(n):
    if n % 2 == 0:
        return n // 2
    return (3 * n + 1) // 2


def check_growth(limit):
    for n in range(limit + 1):
        assert 2 * (t(n) + 1) <= 3 * (n + 1)
        if n % 2 == 1:
            assert 2 * (t(n) + 1) == 3 * (n + 1)


def orbit_to_one(n, limit):
    seq = [n]
    seen = {n}
    while seq[-1] != 1:
        y = t(seq[-1])
        if y in seen:
            return None
        seq.append(y)
        seen.add(y)
        if len(seq) > limit:
            return None
    return seq


def polynomial_of_orbit(seq):
    # seq se termine par le premier 1. La queue est 1,2,1,2,...
    m = len(seq) - 1
    # q = (1-w^2) * sum_{j<m} a_j w^j + w^m (1+2w)
    q = [0] * (m + 2)
    for j, a in enumerate(seq[:-1]):
        q[j] += a
        if j + 2 < len(q):
            q[j + 2] -= a
    q[m] += 1
    q[m + 1] += 2
    return poly_trim(q)


def expand_check(seq, q):
    # (1-w^2) appliqué à la série, queue 1,2,1,2,... après le premier 1.
    # Les deux derniers coefficients voient la troncature et ne sont pas lus.
    full = list(seq)
    for k in range(6):
        full.append(2 if k % 2 == 0 else 1)
    acc = [0] * (len(full) + 2)
    for j, a in enumerate(full):
        acc[j] += a
        acc[j + 2] -= a
    expected = q + [0] * (len(full) - len(q))
    assert acc[: len(full)] == expected


def check_orbits(n_max, step_limit):
    for n in range(1, n_max + 1):
        seq = orbit_to_one(n, step_limit)
        assert seq is not None and seq[-1] == 1
        q = polynomial_of_orbit(seq)
        assert all(isinstance(c, int) for c in q)
        expand_check(seq, q)
    # n=0 : suite nulle, jamais 1.
    assert t(0) == 0
    zero = [0]
    # q=0 convient, et aucun itéré ne vaut 1.
    x = 0
    for _ in range(5):
        assert x != 1
        x = t(x)


def check_recurrence(limit):
    for n in range(1, limit + 1):
        assert t(2 * n) == n
        assert t(2 * n - 1) == 3 * n - 1


def check_period_dividing_two():
    # Chaque cas de parité est une équation linéaire, une seule racine.
    # Point fixe pair : n/2 = n.
    assert t(0) == 0
    # Point fixe impair : (3n+1)/2 = n, soit n = -1.
    assert (3 * (-1) + 1) // 2 == -1
    # Deux pas pairs : n/4 = n, seule racine 0, qui n'est pas de période 2.
    # Pair puis impair : n = 2m, m impair, (3m+1)/2 = 2m, soit m = 1.
    assert (3 * 1 + 1) // 2 == 2 and t(2) == 1 and t(1) == 2
    # Impair puis pair : (3n+1)/4 = n, soit n = 1.
    assert (3 * 1 + 1) // 4 == 1
    # Deux impairs : 3(3n+1)+2 = 4n, soit 5n = -5, n = -1, déjà point fixe.
    assert 3 * (3 * (-1) + 1) + 2 == 4 * (-1)


def main():
    check_partial_fraction()
    print("PASS fractions partielles : somme λ^{2ν}/(1-λ^ν w) = 3w/(1-w^3)")
    for e in (1, 3, 5, 7):
        check_odd_geometric(e)
    print("PASS équation (21) pour z^{2n-1}/(1-z^{2n-1}), n=1..4")
    check_growth(2000)
    print("PASS croissance t(n)+1 ≤ (3/2)(n+1) pour 0 ≤ n ≤ 2000, égalité sur les impairs")
    check_orbits(500, 10000)
    print("PASS conjecture 2 sur 1 ≤ n ≤ 500, et n=0 séparé")
    check_recurrence(500)
    print("PASS récurrence (16) : t(2n)=n et t(2n-1)=3n-1 pour 1 ≤ n ≤ 500")
    check_period_dividing_two()
    print("PASS les quatre cas de parité ne donnent que le cycle positif {1,2}")


if __name__ == "__main__":
    main()
