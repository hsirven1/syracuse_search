#!/usr/bin/env python3
"""Small exact arithmetic checks of the 2-adic Tschakaloff normalization.

No computation of long parity prefixes, no p-adic theorem proved here.
"""
from fractions import Fraction
from math import gcd


Q = lambda n: n * (n + 1) // 2
q = Fraction(3, 2)
alpha = Fraction(2)


def term(n):
    return alpha**n * q**(-Q(n))


def v2_integer(a):
    assert a
    return (abs(a) & -abs(a)).bit_length() - 1


def v2_rational(r):
    return v2_integer(r.numerator) - v2_integer(r.denominator)


def check_parameter_cutoff():
    assert gcd(3, 2) == 1
    assert q == Fraction(3, 2) and alpha == 2
    assert v2_rational(q) == -1 and v2_rational(alpha) == 1
    # gamma = 1-log(2)/log(3) < 3/8 < (3-sqrt(5))/2
    assert 2**8 == 256 > 243 == 3**5
    assert 9**2 == 81 > 80 == 16*5


def check_normalization_and_shift():
    for n in range(0, 9):
        assert term(n) == Fraction(2**(n + Q(n)), 3**Q(n))
        assert v2_rational(term(n)) == n + Q(n)
    for m in range(1, 8):
        lhs = sum((q**n * term(n) for n in range(m + 1)), Fraction())
        rhs = 1 + alpha * sum((term(n) for n in range(m)), Fraction())
        assert lhs == rhs
        assert v2_rational(term(m + 1)) == Q(m + 1) + m + 1


def check_exact_affine_word_identity():
    for m in range(1, 6):
        Qm = Q(m)
        taum = Qm + m
        Cm = sum(
            2 ** (Q(j) + j - 1) * 3 ** (Qm - Q(j))
            for j in range(1, m + 1)
        )
        # 3^Qm * (sum_{j>=1}^{m} 2^{j+Qj-1}/3^Qj) == Cm
        sm = sum(
            (Fraction(2 ** (j + Q(j) - 1), 3 ** Q(j))
             for j in range(1, m + 1)), Fraction()
        )
        assert 3**Qm * sm == Cm
        assert Qm + m == taum


if __name__ == '__main__':
    check_parameter_cutoff()
    check_normalization_and_shift()
    check_exact_affine_word_identity()
    print('PASS: 1989-criterion parameter inequalities, exact Tschakaloff normalization,')
    print('      q-functional truncation identity, valuations, and finite affine sums')
    print('NOTE: theorem hypotheses are *not* proven by these tests.')
