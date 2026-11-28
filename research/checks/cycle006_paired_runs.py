#!/usr/bin/env python3
"""Contrôles exacts du cycle 006 : runs appariés et deux valeurs de Tschakaloff.

La preuve est dans research/cycles/cycle-006.md. Ce script ne la remplace pas.
Il vérifie, en entiers : les sommes de runs, l'identité terme à terme avec
q = 81/16, l'absence des rapports q^n, les comparaisons qui séparent γ de
Γ(2,0) et le seuil de Bundschuh, le signe de Q_m et le supremum Q_2.

Usage : python3 research/checks/cycle006_paired_runs.py
"""


def run_length(j):
    return j + (j & 1)


def odd_count(j):
    total = 0
    for i in range(1, j + 1):
        total += run_length(i)
    return total


def prefix_sums():
    for m in range(1, 41):
        if odd_count(2 * m - 1) != 2 * m * m:
            raise AssertionError((2 * m - 1, odd_count(2 * m - 1)))
        if odd_count(2 * m) != 2 * m * (m + 1):
            raise AssertionError((2 * m, odd_count(2 * m)))
        if run_length(2 * m - 1) != 2 * m or run_length(2 * m) != 2 * m:
            raise AssertionError(m)


def term_identity():
    # a_m = 2^{2m^2+2m-1}/3^{2m^2} et u_m(9) = (16/81)^{m(m+1)/2} 9^m.
    # b_m = 2^{2m^2+4m}/3^{2m^2+2m} et u_m(4) = (16/81)^{m(m+1)/2} 4^m.
    for m in range(1, 13):
        tri = m * (m + 1) // 2
        left_odd = 2 * 2 ** (2 * m * m + 2 * m - 1) * 81**tri
        right_odd = 3 ** (2 * m * m) * 16**tri * 9**m
        if left_odd != right_odd:
            raise AssertionError(("odd", m))
        left_even = 2 ** (2 * m * m + 4 * m) * 81**tri
        right_even = 3 ** (2 * m * m + 2 * m) * 16**tri * 4**m
        if left_even != right_even:
            raise AssertionError(("even", m))


def not_a_power():
    # 4/9 et 9/4 ne sont pas des puissances entières de 81/16.
    for n in range(1, 9):
        if 4 * 16**n == 9 * 81**n or 9 * 16**n == 4 * 81**n:
            raise AssertionError(n)
        if 4 * 81**n == 9 * 16**n or 9 * 81**n == 4 * 16**n:
            raise AssertionError(-n)


def thresholds():
    # log2/log3 < 2/3 < (√17-1)/4, donc γ_VW > Γ(2,0).
    if not (8 < 9 and 121 < 153):
        raise AssertionError("gamma")
    # log2/log3 > 5/8 > (3-√5)/2, donc le seuil de Bundschuh échoue.
    if not (256 > 243 and 80 > 49):
        raise AssertionError("bundschuh")
    # 2/(3+√5) = (3-√5)/2, forme utilisée pour lire Satz 2.
    # (3-√5)/2 = 2/(3+√5) ssi  (3-√5)(3+√5) = 4 ssi 9-5 = 4.
    if (3 * 3 - 5) != 4:
        raise AssertionError("conjugate")


def partial_numerator(m):
    height = odd_count(m)
    numerator = 0
    for j in range(1, m + 1):
        numerator += 2 ** (j + odd_count(j)) * 3 ** (height - odd_count(j))
    return numerator


def liouville_sign():
    # Q_m = log2(2^{o_m+r_{m+1}+m+1} / (3^{o_m}+P_m)).
    # Le run de B7 est r_{m+1}. P_m = 3^{r_m} P_{m-1} + 2^{m+o_m}.
    previous = 0
    for m in range(1, 41):
        height = odd_count(m)
        direct = partial_numerator(m)
        if m == 1:
            recurrent = 2 ** (1 + height)
        else:
            recurrent = 3 ** run_length(m) * previous + 2 ** (m + height)
        if direct != recurrent:
            raise AssertionError(("recurrence", m))
        previous = direct
        if run_length(m + 1) > m + 2 or height < m * (m + 1) // 2:
            raise AssertionError(("shape", m))
        lhs = 2 ** (height + run_length(m + 1) + m + 1)
        rhs = 3**height + direct
        if m <= 4:
            if lhs <= rhs:
                raise AssertionError(("positive", m))
        elif lhs >= rhs:
            raise AssertionError(("negative", m))
    witnessed = {
        2: (2048, 217),
        4: (8388608, 1655161),
        5: (2**30, 1215000977),
        6: (2**39, 886809454057),
        7: (2**48, 5818906583881865),
        8: (2**59, 38178127571825626921),
    }
    for m, pair in witnessed.items():
        lhs = 2 ** (odd_count(m) + run_length(m + 1) + m + 1)
        rhs = 3 ** odd_count(m) + partial_numerator(m)
        if (lhs, rhs) != pair:
            raise AssertionError((m, lhs, rhs))
    left2, right2 = witnessed[2]
    for m in (1, 3, 4):
        left = 2 ** (odd_count(m) + run_length(m + 1) + m + 1)
        right = 3 ** odd_count(m) + partial_numerator(m)
        if left2 * right <= left * right2:
            raise AssertionError(("sup", m))
    if not (9 * 217 < 2048 < 10 * 217):
        raise AssertionError("height")
    for m in range(9, 21):
        if 12 + 7 * m - m * m >= 0:
            raise AssertionError(("bound", m))


def main():
    prefix_sums()
    print("PASS prefix sums o_{2m-1}=2m^2, o_{2m}=2m(m+1)")
    term_identity()
    print("PASS term identity with q=81/16 for 1<=m<=12")
    not_a_power()
    print("PASS 4/9 and 9/4 are not powers (81/16)^n for |n|<=8")
    thresholds()
    print("PASS 8<9, 121<153, 256>243, 80>49")
    liouville_sign()
    print("PASS Q_4>0, sup Q_m = Q_2, Q_m<0 for 5<=m<=40")


if __name__ == "__main__":
    main()
