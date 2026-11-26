"""Exact checks for the height-sensitive run bound.

The proofs are in research/cycles/cycle-002.md. These checks do not replace them.
"""

from __future__ import annotations

import math


def v2(n: int) -> int:
    return (n & -n).bit_length() - 1


def min_r_mod(a: int, s: int) -> int:
    """Least positive r with v2(a * 3^r + 1) >= s, via 2-adic lifting."""
    if s < 3:
        raise ValueError(s)
    mod = 1 << s
    target = (-pow(a, -1, mod)) % mod
    if target % 8 not in (1, 3):
        raise AssertionError((a, s, target % 8))
    r = 1 if target % 8 == 3 else 2
    for k in range(3, s):
        mod_next = 1 << (k + 1)
        tgt = target % mod_next
        if pow(3, r, mod_next) == tgt:
            continue
        step = 1 << (k - 2)
        if pow(3, r + step, mod_next) == tgt:
            r += step
        else:
            raise AssertionError((a, s, k, r))
    return r


def v2_at_least(a: int, r: int, s: int) -> int:
    """Return v2(a*3^r+1), computed modulo a sufficient power of two."""
    for k in range(s, s + 64):
        if (pow(3, r, 1 << k) * (a % (1 << k)) + 1) % (1 << k) != 0:
            return k - 1
    return s + 64


def check_order_of_three(max_m: int = 18) -> None:
    for m in range(3, max_m + 1):
        order = 1 << (m - 2)
        assert pow(3, order, 1 << m) == 1
        assert pow(3, order // 2, 1 << m) != 1


def check_negative_slope_family(max_s: int = 32) -> None:
    """For B=1, the excess r_1 - log2(5) is unbounded along M=5*2^r-1."""
    previous = -1
    for s in range(4, max_s + 1):
        r = min_r_mod(5, s)
        valuation = v2_at_least(5, r, s)
        assert valuation >= s
        r1 = valuation - 1
        # log2(5) < 3, so sum - log2(M+1) > r1 - 3, and this tends to infinity.
        excess_lower = r1 - 3
        assert excess_lower >= previous
        previous = excess_lower
        # Symbolic (H) comparison for A = (s - 5) / 2, B = 1:
        # LHS >= r + s - 1, RHS < 2A + r + 3, and s - 1 > 2A + 3 when s > 2A + 4.
        A = (s - 5) / 2
        assert r + (s - 1) > 2 * A + r + 3


def check_explicit_witness() -> None:
    r = min_r_mod(5, 16)
    assert r == 757
    valuation = v2(5 * pow(3, r) + 1)
    assert valuation == 16
    # Window of two runs at M = 5*2^757 - 1: sum = 757 + 15 = 772.
    # log2(5) < 7/3 because 5^3 = 125 < 128 = 2^7, so
    # log2(M+1) < 757 + 7/3 and 2*6 + log2(M+1) < 772.
    assert 5**3 < 2**7
    assert 772 * 3 > (2 * 6 + 757) * 3 + 7


def check_mersenne_forces_B_at_least_one() -> None:
    for h in range(1, 40):
        M = (1 << h) - 1
        assert v2(M + 1) == h
        assert math.log2(M + 1) == h


def check_twenty_seven_kills_one_point_eight() -> None:
    n = 27
    runs = []
    while len(runs) < 13:
        r = v2(n + 1)
        a = (n + 1) >> r
        runs.append(r)
        n = (pow(3, r) * a - 1) // 2
    assert runs == [2, 5, 1, 2, 3, 4, 1, 0, 3, 2, 6, 0, 4]
    assert sum(runs) == 33
    # log2(28) < 16/3 because 28^3 < 2^16, and (9/5)*(13 + 16/3) = 33 exactly,
    # so (9/5)*(13 + log2(28)) < 33.
    assert 28**3 < 2**16
    assert 9 * 55 == 33 * 5 * 3


def forward_rho(limit: int) -> tuple[float, tuple]:
    best = (0.0, None)
    for seed in range(1, limit, 2):
        n = seed
        x0 = math.log2(seed + 1)
        total = 0
        k = 0
        while n != 1 and k < 100000:
            if n & 1 == 0:
                n >>= 1
                total += 0
            else:
                r = v2(n + 1)
                a = (n + 1) >> r
                total += r
                n = (pow(3, r) * a - 1) // 2
            k += 1
            rho = total / (k + x0)
            if rho > best[0]:
                best = (rho, (seed, k, total))
    return best


def main() -> None:
    check_order_of_three()
    check_negative_slope_family()
    check_explicit_witness()
    check_mersenne_forces_B_at_least_one()
    check_twenty_seven_kills_one_point_eight()
    rho, witness = forward_rho(100_000)
    assert rho < 2
    assert witness is not None and witness[0] == 27
    print(
        "PASS order-of-3, a=5 excess through s=32, witness r=757, "
        "Mersenne slope, 27 versus 9/5, and rho<2 on odd seeds < 100000 "
        f"(max rho={rho:.4f} at {witness})."
    )


if __name__ == "__main__":
    main()
