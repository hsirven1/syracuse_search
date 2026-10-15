#!/usr/bin/env python3
"""Verify a known parity-cylinder construction, not a new Collatz theorem."""

def U(n: int) -> int:
    assert n > 0 and n & 1
    y = 3*n + 1
    return y >> ((y & -y).bit_length() - 1)

def witness(m: int) -> tuple[int, int]:
    assert m >= 1
    mod = 1 << (m + 1)
    q = ((1 << m) + 1) * pow(3**m, -1, mod) % mod
    assert q & 1
    while (4**m - 3**m)*q <= (1 << m)-1:
        q += mod
    return (1 << m)*q - 1, q

def test(m: int) -> None:
    n, q = witness(m)
    z = n
    for i in range(1, m):
        z = U(z)
        assert z == 3**i * 2**(m-i)*q - 1
        assert z > n
    z = U(z)
    assert z == (3**m * q - 1) >> m
    assert z < n
    assert ((3**m*q - 1) // (1 << m)) & 1

if __name__ == "__main__":
    for m in range(1, 151):
        test(m)
    print("PASS exact first-descent cylinder test for m=1..150")
