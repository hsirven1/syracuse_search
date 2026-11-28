#!/usr/bin/env python3
"""Contrôles du cycle 019.

Ils vérifient les formules (1.5) et (1.6) de Bernstein–Lagarias 1996
sur des représentants 2-adiques, le lien avec l'orbite de 1, le calcul
de B1 sur cette même orbite, et la récurrence des restes du lemme sur
les développements binaires. Ils ne démontrent pas la conjecture de
périodicité.

Usage : python3 research/checks/cycle019_bernstein_lagarias.py
"""

from __future__ import annotations


N = 64
MOD = 1 << N


def T(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    q, r = divmod(3 * n + 1, 2)
    if r != 0:
        raise RuntimeError(f"3n+1 impair pour n={n}")
    return q


def S(y: int) -> int:
    if y % 2 == 0:
        return y // 2
    return (y - 1) // 2


def phi_inv(x: int, bits: int = N) -> int:
    """Somme partielle de (1.5), dans 0 .. 2^bits - 1."""
    total = 0
    n = x
    for i in range(bits):
        total += (n & 1) << i
        n = T(n)
    return total


def phi_from_positive(x: int, mod: int = MOD) -> int:
    """(1.6) pour un entier x ≥ 0, dont l'écriture binaire est finie.

    Les positions vérifient 0 ≤ d_1 < d_2 < … et l'indice l commence à 1.
    """
    if x < 0:
        raise ValueError(x)
    positions = [i for i in range(x.bit_length()) if (x >> i) & 1]
    inv3 = pow(3, -1, mod)
    inv_l = inv3
    total = 0
    for d in positions:
        total = (total + (pow(2, d, mod) * inv_l)) % mod
        inv_l = (inv_l * inv3) % mod
    return (-total) % mod


def series_phi_of_neg_one_third(mod: int = MOD) -> int:
    """(1.6) sur les bits de -1/3 = Σ_{k≥0} 4^k."""
    inv3 = pow(3, -1, mod)
    inv_l = inv3
    total = 0
    power = 1  # 4^0 at l=1, position d_1=0
    # l runs until 2^{d_l} ≡ 0, i.e. d_l = 2(l-1) ≥ valuation of the modulus.
    for _ in range(mod.bit_length()):
        total = (total + power * inv_l) % mod
        if power % mod == 0:
            break
        power = (power * 4) % mod
        inv_l = (inv_l * inv3) % mod
    return (-total) % mod


def b1_on_orbit_of_one(mod: int = MOD) -> int:
    """Série de B1 pour l'itinéraire 1,0,1,0,... : ξ+1 = -1/2 Σ_{j≥1} (4/3)^j."""
    inv3 = pow(3, -1, mod * 2)
    total = 0
    term = 1
    wide = mod * 2
    for _j in range(1, mod.bit_length()):
        term = (term * 4 * inv3) % wide
        total = (total + term) % wide
        if term == 0:
            break
    if total % 2 != 0:
        raise RuntimeError("la somme de B1 n'est pas paire")
    xi_plus = (-(total // 2)) % mod
    return (xi_plus - 1) % mod


def main() -> None:
    inv3 = pow(3, -1, MOD)
    minus_one_third = (-inv3) % MOD

    got = phi_inv(1)
    if got != minus_one_third:
        raise SystemExit(f"FAIL (1.5) sur 1: {got} != {-inv3}")
    print("PASS (1.5) : Φ^{-1}(1) ≡ -1/3 (mod 2^64)")

    if phi_from_positive(1) != minus_one_third:
        raise SystemExit("FAIL (1.6) sur 1")
    print("PASS (1.6) : Φ(1) ≡ -1/3 (mod 2^64)")

    if phi_from_positive(2) != (-2 * inv3) % MOD:
        raise SystemExit("FAIL (1.6) sur 2")
    if phi_inv(2) != (-2 * inv3) % MOD:
        raise SystemExit("FAIL (1.5) sur 2")
    print("PASS (1.5) et (1.6) : Φ(2) ≡ Φ^{-1}(2) ≡ -2/3 (mod 2^64)")

    # 5 = 2^0+2^2, donc (1.6) donne -(1/3 + 4/9) = -7/9.
    inv9 = pow(9, -1, MOD)
    phi5 = (-(inv3 + 4 * inv9)) % MOD
    if phi_from_positive(5) != phi5:
        raise SystemExit("FAIL (1.6) sur 5")
    # Itinéraire 5,8,4,2,1,2,1,... : bits 1,0,0,0 puis 1,0,1,0,...
    # Φ^{-1}(5) = 1 + 16 Σ_{k≥0} 4^k = 1 + 16(-1/3) = -13/3.
    phi_inv5 = (1 + 16 * minus_one_third) % MOD
    if phi_inv(5) != phi_inv5:
        raise SystemExit(f"FAIL (1.5) sur 5: {phi_inv(5)} != {phi_inv5}")
    if phi5 == phi_inv5:
        raise SystemExit("FAIL : Φ(5) et Φ^{-1}(5) ne doivent pas coïncider")
    print("PASS : Φ(5) ≡ -7/9 et Φ^{-1}(5) ≡ -13/3 sont distincts")

    if series_phi_of_neg_one_third() != 1:
        raise SystemExit("FAIL (1.6) sur -1/3")
    print("PASS (1.6) : Φ(-1/3) ≡ 1 (mod 2^64)")

    # T(-1/3) = 0 dans Z_2, donc Φ^{-1}(Φ(1)) = 1.
    image = (3 * minus_one_third + 1) % MOD
    if image % 2 != 0 or (image // 2) % (MOD // 2) != 0:
        raise SystemExit("FAIL T(-1/3) = 0")
    print("PASS : T(-1/3) ≡ 0, et l'itinéraire vaut 1,0,0,...")

    # (1.5) implique Φ^{-1} ∘ T = S ∘ Φ^{-1}, et le bit bas est la parité.
    samples = [1, 2, 3, 4, 5, 7, 27, -1, -5, minus_one_third]
    for x in samples:
        left = phi_inv(T(x), bits=N - 1)
        right = S(phi_inv(x)) % (1 << (N - 1))
        if left != right:
            raise SystemExit(f"FAIL conjugaison sur {x}: {left} != {right}")
        if phi_inv(x) % 2 != x % 2:
            raise SystemExit(f"FAIL parité (1.5) sur {x}")
        if x >= 0 and phi_from_positive(x) % 2 != x % 2:
            raise SystemExit(f"FAIL parité (1.6) sur {x}")
    print("PASS : Φ^{-1}∘T = S∘Φ^{-1} (mod 2^63) sur 10 valeurs")
    print("PASS : bit bas de (1.5) sur les 10 valeurs, et de (1.6) sur les x ≥ 0")

    # B1 sur l'orbite de 1 redonne 1. La division par 2 est exacte.
    recovered = b1_on_orbit_of_one()
    if recovered != 1:
        raise SystemExit(f"FAIL B1 sur 1: {recovered}")
    print("PASS B1 : la série de l'itinéraire de 1 redonne ξ ≡ 1")

    # Un développement ultimement périodique est rationnel : période 2, bits 1,0.
    # Σ_{k≥0} 4^k = -1/3. Déjà utilisé ci-dessus.
    if minus_one_third != sum(pow(4, k, MOD) for k in range(N)) % MOD:
        raise SystemExit("FAIL série géométrique")
    print("PASS : Σ_{k≥0} 4^k ≡ -1/3 (mod 2^64)")

    def digits_from_fraction(c: int, d: int, count: int) -> list[int]:
        """Récurrence du lemme : t_{n+1} = (t_n + d b_n)/2, b_n ≡ t_n (mod 2)."""
        if d % 2 == 0:
            raise ValueError(d)
        bits = []
        # s_0 = 0, t_0 = -c. Ensuite la borne place t_n dans un ensemble fini.
        t = -c
        for _ in range(count):
            b = t & 1
            bits.append(b)
            nxt = t + d * b
            if nxt % 2 != 0:
                raise RuntimeError((c, d, t))
            t = nxt // 2
        return bits

    if digits_from_fraction(-1, 3, 8) != [1, 0, 1, 0, 1, 0, 1, 0]:
        raise SystemExit("FAIL chiffres de -1/3")
    if digits_from_fraction(1, 1, 8) != [1, 0, 0, 0, 0, 0, 0, 0]:
        raise SystemExit("FAIL chiffres de 1")
    print("PASS : la récurrence des restes redonne les chiffres de -1/3 et de 1")

    print("11 contrôles PASS")


if __name__ == "__main__":
    main()
