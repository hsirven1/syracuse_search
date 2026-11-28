#!/usr/bin/env python3
"""Contrôles exacts du cycle 003 : critère de Liouville pour les réalisations rationnelles.

Application raccourcie T(x)=x/2 (pair), (3x+1)/2 (impair). La preuve est dans
research/cycles/cycle-003.md. Ces contrôles ne la remplacent pas : ils vérifient
l'identité de valuation sur les cycles rationnels, la borne archimédienne, et les
comparaisons entières utilisées pour le mot à runs 2^k.

Usage : python3 research/checks/cycle003_liouville.py
"""
from fractions import Fraction
from math import gcd


def v2(n):
    n = abs(n)
    if n == 0:
        raise ValueError("v2(0)")
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def T(x):
    a, b = x.numerator, x.denominator
    if a % 2 == 0:
        return Fraction(a, 2 * b)
    return Fraction(3 * a + b, 2 * b)


def sigma_of(xi):
    sigma = -2 * (xi + 1)
    a, b = sigma.numerator, sigma.denominator
    if b < 0:
        a, b = -a, -b
    g = gcd(a, b)
    return a // g, b // g


def cycle_point(word):
    """Point fixe de la branche périodique : xi = B / (2^s - 3^q)."""
    A, B, s = 1, 0, 0
    for bit in word:
        if bit:
            B = 3 * B + (1 << s)
            A *= 3
        s += 1
    return Fraction(B, (1 << s) - A)


def affine(prefix):
    """(A, B, s) tels que la branche du préfixe soit (A x + B) / 2^s, A=3^{nombre de 1}."""
    A, B, s = 1, 0, 0
    for bit in prefix:
        if bit:
            B = 3 * B + (1 << s)
            A *= 3
        s += 1
    return A, B, s


def runs_of(bits, max_m, max_o):
    """Pour chaque m avec o_m <= max_o, retourne (m, o_m, r_m, o_{m+1}, P_m).

    o_j = nombre de 1 strictement avant le j-ième 0.
    P_m = sum_{j=1}^m 2^{j+o_j} 3^{o_m-o_j}.
    """
    zeros = []
    o = 0
    for bit in bits:
        if bit == 0:
            zeros.append(o)
            if len(zeros) > max_m:
                break
        else:
            o += 1
            if zeros and o > max_o:
                break
    out = []
    P = 0
    for m in range(1, len(zeros)):
        o_m = zeros[m - 1]
        o_next = zeros[m]
        if o_m > max_o:
            break
        if m == 1:
            P = 1 << (1 + o_m)
        else:
            P = P * 3 ** (o_m - zeros[m - 2]) + (1 << (m + o_m))
        out.append((m, o_m, o_next - o_m, o_next, P))
    return out


def check_pair(a, b, run_rows):
    """Identité v_2(A_m)=m+1+o_{m+1} et borne |A_m| <= |a| 3^{o_m} + b P_m."""
    if b % 2 == 0 or b <= 0:
        raise AssertionError((a, b))
    n = 0
    for m, o_m, _r, o_next, P in run_rows:
        A = a * 3 ** o_m - b * P
        if A == 0 or v2(A) != m + 1 + o_next:
            raise AssertionError((a, b, m, A, m + 1 + o_next, v2(A) if A else None))
        if abs(A) > abs(a) * 3 ** o_m + b * P:
            raise AssertionError((a, b, m, "triangle"))
        n += 1
    return n


def periodic_bits(word, nbits):
    L = len(word)
    return [word[i % L] for i in range(nbits)]


def eventual_bits(prefix, word, nbits):
    bits = list(prefix)
    L = len(word)
    while len(bits) < nbits:
        bits.append(word[(len(bits) - len(prefix)) % L])
    return bits


counts = {}

# 1. Identité sur tout mot purement périodique de longueur <= 12 contenant au moins un 0.
#    Chaque tel mot est l'itinéraire d'un rationnel de Z_(2) (direction facile de Lagarias).
n_words = n_rows = 0
seen_xi = {}
for L in range(1, 13):
    for mask in range(1 << L):
        word = [(mask >> i) & 1 for i in range(L)]
        if 0 not in word:
            continue
        xi = cycle_point(word)
        a, b = sigma_of(xi)
        assert b % 2 == 1
        # L'orbite réelle du rationnel reproduit le mot.
        x = xi
        for bit in word * 2:
            assert (x.numerator & 1) == bit
            x = T(x)
        assert x == xi
        rows = runs_of(periodic_bits(word, 400), max_m=24, max_o=48)
        n_rows += check_pair(a, b, rows)
        n_words += 1
        seen_xi[word.__repr__()] = str(xi)
assert n_words == sum((1 << L) - 1 for L in range(1, 13))
counts["cycles_purs_longueur_1_a_12"] = {"mots": n_words, "fenetres": n_rows}

# Témoins nommés.
assert cycle_point([0]) == 0
assert cycle_point([1, 0]) == 1
assert cycle_point([1, 1, 0]) == -5
# Itinéraire de 1 : A_m = -2^{2m+2}, valuation exactement 2m+2.
a1, b1 = sigma_of(Fraction(1))
assert (a1, b1) == (-4, 1)
for m, o_m, r, o_next, P in runs_of(periodic_bits([1, 0], 80), 20, 40):
    assert (o_m, r, o_next) == (m, 1, m + 1)
    assert a1 * 3 ** o_m - b1 * P == -(1 << (2 * m + 2))
counts["temoins_0_1_moins5_et_A_m_de_1"] = "ok"

# 2. Mots ultimement périodiques : préfixe quelconque de longueur <= 4, cycle de longueur <= 6.
n_ev = n_rows = n_skip = 0
for L in range(1, 7):
    for mask in range(1 << L):
        word = [(mask >> i) & 1 for i in range(L)]
        if 0 not in word:
            continue
        eta = cycle_point(word)
        for plen in range(0, 5):
            for pmask in range(1 << plen):
                prefix = [(pmask >> i) & 1 for i in range(plen)]
                A, B, s = affine(prefix)
                xi = Fraction(eta * (1 << s) - B, A)
                if xi.denominator % 2 == 0:
                    n_skip += 1
                    continue
                a, b = sigma_of(xi)
                bits = eventual_bits(prefix, word, 300)
                x = xi
                for bit in bits[:80]:
                    assert (x.numerator & 1) == bit and x.denominator % 2 == 1
                    x = T(x)
                n_rows += check_pair(a, b, runs_of(bits, 16, 36))
                n_ev += 1
counts["ultimement_periodiques"] = {"testes": n_ev, "hors_Z2": n_skip, "fenetres": n_rows}

# 3. Orbites de a/b, b impair <= 63, |a| <= 120.
#    Seules les fenêtres atteintes depuis ces départs sont testées (250 pas ou 18 zéros).
#    Ce n'est pas un recensement des cycles de 3x+b. Le cycle de paramètre 13
#    227 → 347 → 527 → 797 → 1202 → 601 → 908 → 454 → 227 est absent de ce balayage ;
#    son mot, de longueur 8, est déjà dans le contrôle périodique ci-dessus.
def accelerated(n, bparam):
    return n // 2 if n % 2 == 0 else (3 * n + bparam) // 2

cyc13 = [227]
while True:
    nxt = accelerated(cyc13[-1], 13)
    if nxt == cyc13[0]:
        break
    cyc13.append(nxt)
assert cyc13 == [227, 347, 527, 797, 1202, 601, 908, 454]
pts13 = {Fraction(n, 13) for n in cyc13}
assert all(p.denominator == 13 for p in pts13)
word13 = [n & 1 for n in cyc13]
assert word13 == [1, 1, 1, 1, 0, 1, 0, 0]
assert cycle_point(word13) == Fraction(227, 13)
x13 = Fraction(227, 13)
for n in cyc13:
    assert x13 == Fraction(n, 13)
    x13 = T(x13)
assert x13 == Fraction(227, 13)

n_orb = n_rows = hits13 = 0
for bden in range(1, 64, 2):
    for anum in range(-120, 121):
        xi = Fraction(anum, bden)
        a, b = sigma_of(xi)
        bits = []
        x = xi
        nzeros = 0
        for _ in range(250):
            if x in pts13:
                hits13 += 1
            if x.denominator % 2 == 0:
                raise AssertionError(xi)
            bit = x.numerator & 1
            bits.append(bit)
            nzeros += bit == 0
            x = T(x)
            if nzeros >= 18:
                break
        n_rows += check_pair(a, b, runs_of(bits, 16, 40))
        n_orb += 1
assert hits13 == 0
counts["orbites_a_sur_b"] = {"orbites": n_orb, "fenetres": n_rows, "cycle13_visite": hits13}

# 4. Le mot triangulaire (1^j 0)_{j>=1} ne déclenche pas le critère. Dans la plage
#    testée, 2^{m+1+o_{m+1}} < 3^{o_m}+P_m à partir de m=6 (l'inégalité stricte échoue
#    pour m=1..5). Irrationnel par B2, invisible pour B7.
tri = []
for j in range(1, 16):
    tri += [1] * j + [0]
rows = runs_of(tri, 14, 200)
flips = []
for m, o_m, r, o_next, P in rows:
    lhs = 1 << (m + 1 + o_next)
    rhs = 3 ** o_m + P
    flips.append(lhs < rhs)
assert flips[:5] == [False] * 5 and all(flips[5:])
# Pour m >= 8 le seul premier terme de P dépasse déjà le membre de gauche,
# et le rapport croît : 3^{m+1} > 2^{m+3}.
assert 3 ** 35 > 1 << 52          # m = 8, 3^{o-1} > 2^{o+2m}
assert 3 ** 9 > 9 * (1 << 11)     # E(m+1)/E(m) > 9 dès m = 8
for m in range(8, 30):
    assert 3 ** (m + 1) > 1 << (m + 3)
counts["triangulaire_critere_silencieux_des_m_6"] = len(rows)

# 5. Famille R_k = 2^k. Comparaisons entières de la preuve, puis Q_k > k pour k = 1..8.
assert 2 * 32 < 81
assert 2 * 729 + 16 * 81 + 1024 == 3778
assert 3778 + 729 == 4507
assert 4507 < 7 * 729
assert 128 * 729 > 9 * 4507

def exp_bits(kmax):
    bits = []
    for k in range(1, kmax + 1):
        bits.append(0)
        bits += [1] * (1 << k)
    return bits

term = []
o_k = 0
for k in range(1, 7):
    term.append(Fraction(1 << (k + o_k), 3 ** o_k))
    o_k += 1 << k
G6 = sum(term)
assert G6 < Fraction(3778, 729)
# k = 1, comparaison directe
assert (1 << 3) > 3
# k >= 2, forme fermée 8*(4/3)^{2^k-2} > 4507/729 > 1+G
for k in range(2, 9):
    ratio = Fraction(8) * Fraction(4, 3) ** ((1 << k) - 2)
    assert ratio > Fraction(4507, 729)
# et, sans passer par la majoration, l'inégalité entière sur P_k
rows = runs_of(exp_bits(9), max_m=8, max_o=600)
assert [r for _, _, r, _, _ in rows] == [1 << k for k in range(1, 9)]
assert [o for _, o, _, _, _ in rows] == [(1 << k) - 2 for k in range(1, 9)]
for m, o_m, r, o_next, P in rows:
    assert (1 << (o_m + r + 1)) > 3 ** o_m + P
counts["famille_runs_2_puissance_k"] = {"k": 8, "G6": str(G6)}

for key, val in counts.items():
    print(f"PASS {key}: {val}")
