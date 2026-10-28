#!/usr/bin/env python3
"""Small independent exact controls; not a proof of 2-adic non-stabilization."""


def shortcut(n):
    return (3 * n + 1) // 2 if n & 1 else n // 2


def triangular_word(m):
    return ''.join('1' * j + '0' for j in range(1, m + 1))


def check_complexity():
    # 100 blocks suffice to expose all distinct factors for L <= 80.
    word = triangular_word(100)
    controls = 0
    for L in range(3, 81):
        observed = len({word[i:i + L] for i in range(len(word) - L + 1)})
        predicted = (L + 1) ** 2 // 4
        assert observed == predicted, (L, observed, predicted)
        controls += 1
    return controls


def canonical(m):
    Q = m * (m + 1) // 2
    tau = Q + m
    C = sum(2 ** (j * (j + 3) // 2 - 1) * 3 ** (Q - j * (j + 1) // 2)
            for j in range(1, m + 1))
    modulus = 2 ** (tau + 1)
    N = (-C * pow(3 ** Q, -1, modulus) - 1) % modulus
    assert (3 ** Q * (N + 1) + C) % modulus == 0
    return N


def check_congruences():
    values = []
    for m in range(1, 8):
        n = canonical(m)
        expected_bits = triangular_word(m) + '1'
        actual_bits = ''
        current = n
        for _ in range(len(expected_bits)):
            actual_bits += str(current & 1)
            current = shortcut(current)
        assert actual_bits == expected_bits, (m, n)
        values.append(n)
    assert values[:4] == [1, 57, 121, 121]
    return len(values)


if __name__ == '__main__':
    a = check_complexity()
    b = check_congruences()
    print(f'PASS: {a} factor complexities, {b} canonical congruences and parity paths')
