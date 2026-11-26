#!/usr/bin/env python3
"""Contrôles exacts du cycle 001 : mots de parités à runs en progression arithmétique.

Application raccourcie T(x) = x/2 (x pair), (3x+1)/2 (x impair), sur Z_2.
Ces contrôles finis ne prouvent rien : le résultat repose sur la preuve de
research/cycles/cycle-001.md et sur le théorème de Väänänen–Wallisser (1989).

Usage : python3 research/checks/cycle001_linear_runs.py
"""
from fractions import Fraction
from math import gcd, log, sqrt
import random

random.seed(20261126)


def parity_word(n, length):
    """Premières parités de l'orbite de l'entier n (n peut être négatif)."""
    out = []
    for _ in range(length):
        b = n & 1
        out.append(b)
        n = (3 * n + 1) // 2 if b else n // 2
    return out


def realization_mod(word, K):
    """xi mod 2^K, par la formule xi + 1 = -sum_{w_e=0} 2^e / 3^{o(e)}."""
    M = 1 << K
    inv3 = pow(3, -1, M)
    y, o = 0, 0
    for e, b in enumerate(word[:K]):
        if b:
            o += 1
        else:
            y = (y + (1 << e) * pow(inv3, o, M)) % M
    return (-1 - y) % M


def frac_mod(x, K):
    """Réduction mod 2^K d'un rationnel à dénominateur impair."""
    M = 1 << K
    assert x.denominator % 2 == 1
    return (x.numerator * pow(x.denominator, -1, M)) % M


def linear_run_word(c, d, nblocks):
    w = []
    for j in range(1, nblocks + 1):
        w += [1] * (c * j + d) + [0]
    return w


def f_trunc(q, alpha, nmax):
    """Troncature de f_q(alpha) = sum_{n>=0} q^{-n(n+1)/2} alpha^n (normalisation VW 1989)."""
    return sum(q ** (-(n * (n + 1) // 2)) * alpha ** n for n in range(nmax + 1))


def T_rational(x):
    """T sur Z_(2) : x = a/b, b impair ; x pair au sens 2-adique ssi a pair."""
    a, b = x.numerator, x.denominator
    return Fraction(a, 2 * b) if a % 2 == 0 else Fraction(3 * a + b, 2 * b)


counts = {}

# 1. Formule générale de réalisation, sur des mots aléatoires.
K = 64
n_ok = 0
for trial in range(3000):
    p = random.choice([0.2, 0.5, 0.7, 0.9])
    w = [1 if random.random() < p else 0 for _ in range(K)]
    n = realization_mod(w, K)
    assert parity_word(n, K) == w, (trial, w)
    n_ok += 1
counts["formule_generale_mots_aleatoires"] = n_ok

# 2. c = 0 (runs constants) : mots périodiques réalisés par des RATIONNELS.
#    Contre-exemple attendu à toute version du lemme sans l'hypothèse c >= 1.
c0 = []
for d in range(0, 8):
    alpha = Fraction(2 ** (d + 1), 3 ** d)
    f = 1 / (1 - alpha)                      # f_1(alpha), série géométrique
    xi = -(1 + f) / 2
    assert xi.denominator % 2 == 1
    x, word = xi, []
    for _ in range(10 * (d + 1)):
        word.append(x.numerator & 1)
        x = T_rational(x)
    assert word == ([1] * d + [0]) * 10, (d, xi, word)
    c0.append((d, str(xi)))
counts["c_egal_0_cycles_rationnels"] = c0

# 3. c >= 1 : identité xi = -(1 + f_q(alpha))/2, q = (3/2)^c, alpha = 2^{d+1}/3^d.
K = 160
n_ok = 0
for c in range(1, 5):
    for d in range(-c, 5):
        nb = 1
        while sum(c * j + d + 1 for j in range(1, nb + 1)) < K + 5:
            nb += 1
        w = linear_run_word(c, d, nb)
        xi = realization_mod(w, K)
        assert parity_word(xi, K) == w[:K]
        # (a) somme 2^{n+o_n-1}/3^{o_n} calculée en entiers mod 2^K
        M = 1 << K
        inv3 = pow(3, -1, M)
        S, n = 0, 1
        while True:
            o_n = c * n * (n + 1) // 2 + d * n
            if n + o_n - 1 >= K:
                break
            S = (S + (1 << (n + o_n - 1)) * pow(inv3, o_n, M)) % M
            n += 1
        assert (-1 - S) % M == xi
        # (b) normalisation exacte de Väänänen–Wallisser avec Fraction
        q = Fraction(3 ** c, 2 ** c)
        alpha = Fraction(2) ** (d + 1) / Fraction(3) ** d
        F = f_trunc(q, alpha, n + 2)
        assert frac_mod(-(1 + F) / 2, K) == xi
        # (c) préfixe arbitraire u : T^{|u|} ramène à la réalisation de v
        for _ in range(5):
            u = [random.randint(0, 1) for _ in range(random.randint(0, 6))]
            xu = realization_mod(u + w, K)
            y = xu
            for _ in range(len(u)):
                y = (3 * y + 1) // 2 if y & 1 else y // 2
            assert (y - xi) % (1 << (K - len(u))) == 0
        n_ok += 1
counts["c_ge_1_identite_VW_et_prefixes"] = n_ok

# 4. Mot triangulaire (c=1, d=0) : représentants canoniques de la PR #23.
w = linear_run_word(1, 0, 40)
reps = []
for m in range(1, 7):
    tau = m * (m + 1) // 2 + m
    reps.append(realization_mod(w, tau + 1))
assert reps[:4] == [1, 57, 121, 121], reps
counts["triangulaire_representants"] = reps

# 5. Hypothèses du Satz de VW (l=1, sigma=0, p=2) pour q=(3/2)^c, en entiers exacts.
for c in range(1, 200):
    r, s = 3 ** c, 2 ** c
    assert gcd(r, s) == 1 and r > 1 and s >= 1 and max(r, s) == r
# gamma = 1 + log|s|_2/log h = 1 - log2/log3 (indépendant de c)
assert 2 ** 8 > 3 ** 5          # => log2/log3 > 5/8 => gamma < 3/8
assert 81 > 80                  # 3/8 < (3 - sqrt5)/2  <=>  9/4 > sqrt5  <=>  81 > 80
gamma = 1 - log(2) / log(3)
Gamma = (3 - sqrt(5)) / 2
theta = (1 + sqrt(5)) / (2 - gamma * (3 + sqrt(5)))
counts["VW_gamma_Gamma_theta_flottants_informatifs"] = (round(gamma, 6), round(Gamma, 6), round(theta, 2))

# 6. Recherche bornée de contre-exemple : orbites de rationnels a/b (b impair <= 63,
#    |a| <= 300) sur 4000 pas ; queue de runs en progression arithmétique de raison >= 1 ?
#    Observation finie, pas une preuve.
suspects, undecided, total = [], 0, 0
for b in range(1, 64, 2):
    for a in range(-300, 301):
        total += 1
        x, runs, cur = a, [], 0
        big = False
        for _ in range(4000):
            if x & 1:
                cur += 1
                x = (3 * x + b) // 2
            else:
                runs.append(cur)
                cur = 0
                x //= 2
            if abs(x) > 10 ** 60:
                big = True
                break
        if big:
            undecided += 1
            continue
        tail = runs[-12:]
        if len(tail) == 12:
            diffs = {tail[i + 1] - tail[i] for i in range(11)}
            if len(diffs) == 1 and min(diffs) >= 1:
                suspects.append((a, b))
assert not suspects, suspects
counts["recherche_bornee_rationnels"] = {"orbites": total, "suspects": len(suspects), "non_decidees": undecided}

for k, v in counts.items():
    print(f"PASS {k}: {v}")
