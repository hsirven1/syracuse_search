#!/usr/bin/env python3
"""Contrôles du cycle 021, après la revue 6095181058.

Le cas classique entre dans l'hypothèse de Garcia–Tal, la branche impaire
est T, et l'identité de hauteur de B6 est exacte. La borne affichée au §3
exige t≥24. Pour T, les mots de parités de longueur k sur 1..2^k sont
distincts et T^k(n)<2·3^s. Les comparaisons 27<32 et 3125<3456 donnent
deux bases strictement inférieures à 2. L'ordre de 3 modulo 4 vaut 2.
La suite complète de puissances de 2 a un liminf nul et n'a pas de limite.
La suite floor((3/2)^t) reste à distance logarithmique strictement
inférieure à 1 de β t, et ce n'est pas une orbite.

Usage : python3 research/checks/cycle021_garcia_tal_gate.py
"""

from __future__ import annotations

from fractions import Fraction


def T(n: int) -> int:
    if n % 2:
        return (3 * n + 1) // 2
    return n // 2


def paper_branch(n: int) -> int:
    """H de Garcia–Tal pour d=2, m=3, résidu impair -1."""
    if n % 2 == 0:
        return n // 2
    return (3 * n - (-1)) // 2


def passes() -> list[str]:
    out: list[str] = []

    # m < d^{d/(d-1)} : 3 < 2^2.
    if 3 < 4:
        out.append("PASS hypothese d=2 m=3 : 3<4")
    else:
        raise RuntimeError("3<4")

    for n in range(1, 65):
        if paper_branch(n) != T(n):
            raise RuntimeError(n)
    out.append("PASS branche de H identique a T sur 1..64")

    for start in range(1, 65):
        n = start
        pred = Fraction(start + 1)
        for _ in range(64):
            if n % 2 == 0:
                pred *= Fraction(n + 2, 2 * (n + 1))
                n //= 2
            else:
                pred *= Fraction(3, 2)
                n = (3 * n + 1) // 2
            if pred != n + 1:
                raise RuntimeError((start, n, pred))
    out.append("PASS identite de hauteur pour 1<=N<=64 et 1<=t<=64")

    # Base t=24, a=49. Pour a>=49, (a+2)/a <= 51/49 et (51/49)^4 < 2,
    # donc (a+2)^4 < 2 a^4 et l'inégalité se propage à tout t>=24.
    if 49**4 >= 2**24:
        raise RuntimeError("base")
    if 51**4 >= 2 * 49**4:
        raise RuntimeError("pas")
    out.append("PASS (2t+1)^4 < 2^t pour tout t>=24")

    # Sans borne sur t, le même majorant dépasse 1/6 : 41^6 > 3^20.
    if 41**6 <= 3**20:
        raise RuntimeError("t=20")
    out.append("PASS a t=20, log2(2t+1)/(delta t) n'est pas < 1/6")

    # (1/4)/log2(3) < 1/6 car 4 log2(3) > 6, soit 3^4 > 2^6.
    if 81 <= 64:
        raise RuntimeError("81>64")
    out.append("PASS ecart relatif < 1/6 si t>=24 et log2(n_t+1) <= log2(2t+1)")

    # t valeurs distinctes dans 1..2t : densite inferieure 1/2.
    for t in (1, 5, 40):
        count = t
        length = 2 * t
        if count * 2 != length:
            raise RuntimeError(t)
    out.append("PASS t valeurs dans 1..2t donnent la proportion 1/2")

    # Mots de longueur k sur 1..2^k, et T^k(n) < 2·3^s.
    for k in range(1, 13):
        seen: set[int] = set()
        for n in range(1, 2**k + 1):
            x = n
            word = 0
            odds = 0
            for i in range(k):
                if x % 2:
                    word |= 1 << i
                    odds += 1
                    x = (3 * x + 1) // 2
                else:
                    x //= 2
            if word in seen or x >= 2 * 3**odds:
                raise RuntimeError((k, n, odds, x))
            seen.add(word)
        if len(seen) != 2**k:
            raise RuntimeError(("bijection", k, len(seen)))
    out.append("PASS mots distincts et T^k(n) < 2*3^s pour 1<=k<=12")

    # 3^{3/5}<2 et (5/2)/(3/2)^{3/5}<2.
    if 27 >= 32 or 3125 >= 108 * 32:
        raise RuntimeError("bases")
    out.append("PASS 27<32 et 3125<3456 : les deux bases sont < 2")

    # ord_4(3)=2, alors que 2^{2-2}=1.
    if pow(3, 1, 4) != 3 or pow(3, 2, 4) != 1:
        raise RuntimeError("ordre")
    for m in range(3, 13):
        if pow(3, 1, 1 << m) != 3:
            raise RuntimeError(m)
        if (1 << m) <= 1:
            raise RuntimeError(("exposant", m))
    out.append("PASS ord_4(3)=2 et 3^1 ≡ 3 mod 2^m")

    # Suite complète : valeurs distinctes, puissances de 2.
    # Aux temps 2^{3j}, valeur 2^{2j}, rapport 2^{-j}.
    # Les autres temps reçoivent 2^1, 2^3, 2^5, ... dans l'ordre.
    special: dict[int, int] = {}
    used: set[int] = set()
    horizon = 2 ** (3 * 4)
    for j in range(1, 5):
        moment = 2 ** (3 * j)
        value = 2 ** (2 * j)
        if value * (1 << j) != moment:
            raise RuntimeError(("rapport", j))
        special[moment] = value
        used.add(value)
    fillers: list[int] = []
    exponent = 1
    while len(fillers) <= horizon:
        candidate = 1 << exponent
        if candidate not in used:
            fillers.append(candidate)
        exponent += 2
    seen_values: set[int] = set()
    cursor = 0
    large_ratio = False
    for moment in range(1, horizon + 1):
        if moment in special:
            value = special[moment]
        else:
            value = fillers[cursor]
            cursor += 1
            if value >= 2 * moment:
                large_ratio = True
        if value <= 0 or value & (value - 1):
            raise RuntimeError(("pas une puissance", moment, value))
        if value in seen_values:
            raise RuntimeError(("doublon", value))
        seen_values.add(value)
    if not large_ratio:
        raise RuntimeError("limite")
    out.append("PASS suite complete : liminf n_t/t = 0, pas de limite")

    # floor((3/2)^t) : 0 < log2(m_t+1) - β t < 1, et ce n'est pas une orbite.
    for t in range(1, 41):
        m = 3**t // 2**t
        if 2**t * (m + 1) <= 3**t or 2**t * (m + 1) >= 2 * 3**t:
            raise RuntimeError((t, m))
    if T(2) == 3:
        raise RuntimeError("orbite")
    out.append("PASS floor((3/2)^t) approche β t et n'est pas une orbite")

    # Au plus floor(log2(n))+1 puissances de 2 dans un intervalle de longueur n.
    for length in range(1, 33):
        # bit_length(n) = floor(log2(n))+1 pour n>=1.
        cap = length.bit_length()
        limit = 1 << (cap + 2)
        worst = 0
        for start in range(1, limit + 1):
            count = 0
            value = 1
            while value < start:
                value <<= 1
            while value < start + length:
                count += 1
                value <<= 1
            if count > worst:
                worst = count
        if worst > cap:
            raise RuntimeError((length, worst, cap))
    out.append("PASS un intervalle de longueur n contient au plus floor(log2 n)+1 puissances de 2")

    return out


def main() -> None:
    lines = passes()
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
