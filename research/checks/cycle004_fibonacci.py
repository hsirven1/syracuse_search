#!/usr/bin/env python3
"""Contrôles exacts du cycle 004 : runs de Fibonacci et critère de Liouville.

La preuve est dans research/cycles/cycle-004.md. Elle ne calcule aucune
puissance 3^{F_n} au-delà de 3^5. Ce script ne la remplace pas : il vérifie
les bases, le pas entier du lemme, la récurrence de P, l'inégalité D_k > 3^{o_k}+P_k
sur un segment fini, et l'absence de contre-exemple entier pour les préfixes k≤8.

Usage : python3 research/checks/cycle004_fibonacci.py
"""


def fib(n):
    if n <= 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def prefix_sums():
    for k in range(1, 41):
        partial = sum(fib(j + 2) for j in range(1, k))
        if fib(k + 3) - 3 != partial:
            raise AssertionError((k, fib(k + 3) - 3, partial))


def cassini():
    # F_0 = 0, then F_1 = F_2 = 1. Cassini for n≥2 uses F_{n-1}.
    values = [0, 1]
    while len(values) < 42:
        values.append(values[-1] + values[-2])
    for n in range(2, 41):
        if values[n + 1] * values[n - 1] - values[n] ** 2 != (-1) ** n:
            raise AssertionError(n)


def power_lemma(limit=20):
    if 2 ** fib(5) < 3 ** fib(4) + 2 ** (4 - 2):
        raise AssertionError("base n=4")
    if 2 ** fib(6) < 3 ** fib(5) + 2 ** (5 - 2):
        raise AssertionError("base n=5")
    for n in range(4, limit + 1):
        if 2 ** fib(n + 1) < 3 ** fib(n) + 2 ** (n - 2):
            raise AssertionError(("lemma", n))
    for n in range(6, limit + 1):
        product = (3 ** fib(n - 1) + 2 ** (n - 3)) * (3 ** fib(n - 2) + 2 ** (n - 4))
        if product < 3 ** fib(n) + 2 ** (n - 2):
            raise AssertionError(("pas", n))


def partial_P(k):
    """P_k par la somme de la définition, et par la récurrence."""
    o = [0]
    for j in range(1, k):
        o.append(o[-1] + fib(j + 2))
    direct = 0
    for j in range(1, k + 1):
        direct += 2 ** (j + o[j - 1]) * 3 ** (o[k - 1] - o[j - 1])
    recur = 2
    oo = 0
    for m in range(1, k):
        r = fib(m + 2)
        oo += r
        recur = 3 ** r * recur + 2 ** ((m + 1) + oo)
    if direct != recur:
        raise AssertionError((k, direct, recur))
    return o[k - 1], fib(k + 2), direct


def liouville_segment(limit=14):
    for k in range(1, limit + 1):
        o, r, p = partial_P(k)
        if o != fib(k + 3) - 3 or r != fib(k + 2):
            raise AssertionError((k, o, r))
        if 2 ** (o + r + 1) <= 3 ** o + p:
            raise AssertionError(("Q", k))
    # Le pas k=1 échoue, comme l'écrit le cycle ; le pas k≥2 tient.
    if 2 ** fib(4) >= 3 ** fib(3) + 2 ** 1:
        raise AssertionError("le pas k=1 ne doit pas être invoqué")
    for k in range(2, limit + 1):
        if 2 ** fib(k + 3) < 3 ** fib(k + 2) + 2 ** k:
            raise AssertionError(("marge", k))


def ratio_above_beta():
    if not (125 > 121 and 256 > 243):
        raise AssertionError("phi > 8/5 > log2(3)")
    for k in range(2, 16):
        # r_k > beta o_k ⇔ 2^{F_{k+4}-3} > 3^{F_{k+3}-3}
        if 2 ** (fib(k + 4) - 3) <= 3 ** (fib(k + 3) - 3):
            raise AssertionError(k)


def smallest_exact_prefix(runs):
    word = []
    for r in runs:
        word.append(0)
        word.extend([1] * r)
    word.append(0)
    n = 0
    for t, bit_wanted in enumerate(word):
        found = None
        for b in (0, 1):
            x = n + (b << t)
            ok = True
            for s in range(t + 1):
                if (x & 1) != word[s]:
                    ok = False
                    break
                x = (3 * x + 1) >> 1 if (x & 1) else x >> 1
            if ok:
                found = b
                break
        if found is None:
            raise AssertionError(("relevement", t, runs))
        n += found << t
    return n, word


def replay_runs(n, count):
    runs = []
    for _ in range(count):
        if n & 1:
            return runs
        n >>= 1
        c = 0
        while n & 1:
            n = (3 * n + 1) >> 1
            c += 1
        runs.append(c)
    return runs


def integer_prefixes(limit=8):
    for k in range(1, limit + 1):
        runs = [fib(j + 2) for j in range(1, k + 1)]
        n, word = smallest_exact_prefix(runs)
        if replay_runs(n, k) != runs:
            raise AssertionError((k, n, replay_runs(n, k)))
        if n < 2 ** (k - 1):
            raise AssertionError(("borne", k, n))
        # Le résidu relevé réalise le mot, zéro final compris.
        x = n
        for bit in word:
            if (x & 1) != bit:
                raise AssertionError((k, bit))
            x = (3 * x + 1) >> 1 if (x & 1) else x >> 1


def main():
    prefix_sums()
    print("PASS sommes o_k = F_{k+3}-3, k<=40")
    cassini()
    print("PASS Cassini, n<=40")
    power_lemma()
    print("PASS lemme 2^{F_{n+1}} >= 3^{F_n}+2^{n-2}, n<=20, pas inclus")
    liouville_segment()
    print("PASS D_k > 3^{o_k}+P_k pour k<=14, et marge du pas pour k>=2")
    ratio_above_beta()
    print("PASS 125>121, 256>243, et r_k>beta o_k pour 2<=k<=15")
    # G bornée : en r=2 le rapport vaut 8/9 ; en r=3 il vaut 16/27 < 8/9.
    if 2 ** (1 + 2) * 9 != 8 * 3 ** 2:
        raise AssertionError("ratio r=2")
    if 2 ** (1 + 3) * 9 >= 8 * 3 ** 3:
        raise AssertionError("le second rapport n'est pas strictement sous 8/9")
    print("PASS rapport des termes <=8/9, strict des que r_j>2")
    integer_prefixes()
    print("PASS prefixes entiers k<=8 : runs exacts et N >= 2^{k-1}")
    # Bases écrites dans le cycle, reprises ici telles quelles.
    if (32, 31, 256, 251, 8, 3, 64, 43) != (
        2 ** 5,
        3 ** 3 + 4,
        2 ** 8,
        3 ** 5 + 8,
        2 ** 3,
        1 + 2,
        2 ** 6,
        9 + 34,
    ):
        raise AssertionError("bases du texte")
    print("PASS bases du texte : 32>=31, 256>=251, 8>3, 64>43")


if __name__ == "__main__":
    main()
