#!/usr/bin/env python3
"""Finite *exact-integer* regression checks for PARITY_LOGARITHMIC_GAIN.md.

Not a proof of the conditional unbounded-orbit complexity result.
No search for divergent orbits or new parity words.
"""


def step(n: int) -> int:
    assert n > 0
    return (3 * n + 1) // 2 if n & 1 else n // 2


def check_small_orbits() -> tuple[int, int, int]:
    height_checks = odd_run_checks = coarse_even_checks = 0
    for seed in range(1, 257):
        k = seed.bit_length()  # 2**k >= seed+1
        n = seed
        power_2, power_3 = 1, 1
        even_count = 0
        run_start = seed
        run_length = 0
        for t in range(257):
            # Exact integer version of T^t(N)+1 <= (3/2)^t (N+1).
            assert power_2 * (n + 1) <= power_3 * (seed + 1)
            height_checks += 1

            if t:
                # Weaker fully rational form from delta=log2(3)<8/5,
                # beta=delta-1<3/5. This is only a regression check.
                assert 3 * (5 ** even_count) * t <= (8 ** (even_count + 1)) * (k + 1)
                coarse_even_checks += 1

            if n & 1:
                if run_length == 0:
                    run_start = n
                run_length += 1
                # r odds -> 2**r | starting_state+1.
                assert (run_start + 1) % (1 << run_length) == 0
                odd_run_checks += 1
            else:
                even_count += 1
                run_length = 0

            n = step(n)
            power_2 *= 2
            power_3 *= 3

    return height_checks, odd_run_checks, coarse_even_checks


def check_all_odd_mersenne() -> int:
    tested = 0
    for r in range(1, 41):
        n = (1 << r) - 1
        seed_plus_one = 1 << r
        for t in range(r + 1):
            assert (1 << t) * (n + 1) == (3 ** t) * seed_plus_one
            tested += 1
            if t < r:
                assert n & 1  # all first r input parities are odd
                n = step(n)
    return tested


def check_comparison_constant() -> None:
    assert 3 ** 17 == 129140163
    assert 2 ** 27 == 134217728
    assert 3 ** 17 < 2 ** 27
    assert 3 ** 5 == 243 < 256 == 2 ** 8


if __name__ == "__main__":
    heights, runs, evens = check_small_orbits()
    mersenne = check_all_odd_mersenne()
    check_comparison_constant()
    print(
        "PASS: exact integer height inequalities =", heights,
        "; odd run congruences =", runs,
        "; rational even-count control =", evens,
        "; Mersenne identities =", mersenne,
        "; no Lean or asymptotic claim."
    )
