#!/usr/bin/env python3
"""Contrôles du cycle 022.

L'identité β + 1 = δ est la relation 2·(3/2) = 3. Pour un entier x ≥ 64,
la chaîne log2(x+1) ≤ k+1 ≤ 2^{k/2} ≤ sqrt(x), avec k = floor(log2 x),
repose sur x ≤ 2^{k+1}-1 et sur (k+1)^2 ≤ 2^k. Elle échoue pour le réel
x = 255/2 : k = 6 mais x+1 = 257/2 > 2^7. Une borne réelle se ramène à
sa partie entière. La suite a_t = 2^t - 1 vérifie log2(a_t+1)/t = 1.
La suite a_t = t + ceil((5/4)^t) est strictement croissante, de taux
log2(5/4) < log2(3/2), et n'est pas une orbite. Sur l'orbite de 27, la
forme multiplicative de l'identité de B6 est exacte, et N*(k) compte
les impairs parmi les k+1 premiers états.

Usage : python3 research/checks/cycle022_liminf_height.py
"""

from __future__ import annotations

from fractions import Fraction


def T(n: int) -> int:
    if n % 2:
        return (3 * n + 1) // 2
    return n // 2


def passes() -> list[str]:
    out: list[str] = []

    if (3 * 2) == (2 * 3):
        out.append("PASS relation 2*(3/2)=3")
    else:
        out.append("FAIL relation 2*(3/2)=3")

    for k in range(6, 81):
        if (k + 1) ** 2 > 2**k:
            out.append(f"FAIL (k+1)^2<=2^k a k={k}")
            break
    else:
        out.append("PASS (k+1)^2<=2^k pour 6<=k<=80")

    bad = 0
    for x in range(64, 4001):
        k = x.bit_length() - 1
        if not (2**k <= x < 2 ** (k + 1)):
            bad += 1
        if x + 1 > 2 ** (k + 1):
            bad += 1
        if (k + 1) ** 2 > 2**k:
            bad += 1
    if bad == 0:
        out.append("PASS chaine entiere log2(x+1)<=sqrt(x) pour 64<=x<=4000")
    else:
        out.append(f"FAIL chaine sqrt, cas={bad}")

    # X65. Pour x = 255/2, k = 6 car 64 <= x < 128, mais x+1 = 257/2 > 128.
    # Pour y = 2^{m+1} - 1/2, la meme etape echoue, et floor(y) = 2^{m+1}-1
    # retombe dans la chaine entiere.
    real_bad = 0
    half = Fraction(255, 2)
    if not (2**6 <= half < 2**7 and half + 1 == Fraction(257, 2) > 2**7):
        real_bad += 1
    for m in range(6, 41):
        y = 2 ** (m + 1) - Fraction(1, 2)
        if not (2**m <= y < 2 ** (m + 1) and y + 1 > 2 ** (m + 1)):
            real_bad += 1
        if (2 ** (m + 1) - 1) + 1 != 2 ** (m + 1):
            real_bad += 1
        if (m + 1) ** 2 > 2**m:
            real_bad += 1
    if real_bad == 0:
        out.append("PASS x=255/2 casse x+1<=2^{k+1}; le plancher la restaure")
    else:
        out.append(f"FAIL X65, cas={real_bad}")

    # a_t = 2^t - 1. Alors a_t <= x ssi t <= floor(log2(x+1)).
    count_bad = 0
    for k in range(1, 41):
        x = 2**k
        terms = [t for t in range(1, k + 3) if 2**t - 1 <= x]
        if terms != list(range(1, k + 1)):
            count_bad += 1
        if len(terms) > 1 + k:
            count_bad += 1
    if count_bad == 0:
        out.append("PASS compte de 2^t-1 : t<=k pour x=2^k, 1<=k<=40")
    else:
        out.append(f"FAIL compte exponentiel, cas={count_bad}")

    # a_t = t + ceil((5/4)^t). Alors 5/4 < 3/2, la suite croit, et
    # (5/4)^t <= a_t < (5/4)^t + t + 1. T(3) = 5 != 4 = a_2.
    def ceil_div(num: int, den: int) -> int:
        return (num + den - 1) // den

    seq_bad = 0
    if not (5 * 2 < 3 * 4 and 5 > 4 and 3 < 4):
        seq_bad += 1
    previous = 0
    for t in range(1, 81):
        term = t + ceil_div(5**t, 4**t)
        if term <= previous:
            seq_bad += 1
        if not (5**t <= term * 4**t < 5**t + (t + 1) * 4**t):
            seq_bad += 1
        previous = term
    if ceil_div(5, 4) + 1 != 3 or ceil_div(25, 16) + 2 != 4 or T(3) == 4:
        seq_bad += 1
    if seq_bad == 0:
        out.append("PASS t+ceil((5/4)^t) croit, reste sous beta, T(3)=5")
    else:
        out.append(f"FAIL suite 5/4, cas={seq_bad}")

    n = 27
    orbit = [n]
    for _ in range(220):
        n = T(n)
        orbit.append(n)
    # Forme multiplicative de l'identite de B6 :
    # pair : (T+1) = (n+1)/2 * (n+2)/(n+1) ; impair : (T+1) = 3(n+1)/2.
    height = Fraction(orbit[0] + 1)
    identity_bad = 0
    for t, current in enumerate(orbit[:-1]):
        if current % 2 == 0:
            height *= Fraction(current + 2, current + 1) / 2
        else:
            height *= Fraction(3, 2)
        if height != orbit[t + 1] + 1:
            identity_bad += 1
    align_bad = 0
    for k in range(0, 200):
        n_star = sum(1 for j in range(k + 1) if orbit[j] % 2 == 1)
        evens = sum(1 for j in range(k + 1) if orbit[j] % 2 == 0)
        if n_star + evens != k + 1:
            align_bad += 1
    hit = orbit.index(1)
    tail_ok = all(v in (1, 2) for v in orbit[hit:])
    # 3^10 = 59049 < 65536 = 2^16. Sur la queue, n in {1,2} et t>=70,
    # donc log2(n+1) <= t/10.
    ratio_ok = all((v + 1) ** 10 < 2**t for t, v in enumerate(orbit) if t >= hit)
    if identity_bad == 0 and align_bad == 0 and hit == 70 and tail_ok and ratio_ok:
        out.append("PASS identite B6 sur 27, T^70(27)=1, rapport <=1/10")
    else:
        out.append(
            f"FAIL orbite 27, identite={identity_bad}, align={align_bad}, "
            f"hit={hit}, tail={tail_ok}, ratio={ratio_ok}"
        )

    return out


def main() -> None:
    rows = passes()
    for row in rows:
        print(row)
    if any(row.startswith("FAIL") for row in rows):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
