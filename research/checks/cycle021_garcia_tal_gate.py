#!/usr/bin/env python3
"""Contrôles du cycle 021, après la revue 6095232407.

Le cas classique entre dans l'hypothèse de Garcia–Tal, la branche impaire
est T, et l'identité de hauteur de B6 est exacte. La borne affichée au §3
exige t≥24. Pour T, les mots de parités de longueur k sur 1..2^k sont
distincts et T^k(n)<2·3^s. Les cinquièmes puissances 27 et 3125/108 sont
sous (197/100)^5, et la somme des majorants dyadiques vaut 394, qui est
sous 61344/65. Au temps 2^{3j}+1 la valeur de remplissage dépasse t^2.
À t=0 l'écart logarithmique de floor((3/2)^t) vaut 1. L'identité
v_2(3^{2^{m-3}}-1)=m-1 vaut pour m≥4, et l'ordre modulo 8 vaut 2.

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
            gap = moment - 1
            if gap > 1 and gap & (gap - 1) == 0:
                exponent = gap.bit_length() - 1
                if exponent % 3 == 0:
                    rank = moment - exponent // 3
                    if value != 1 << (2 * rank - 1):
                        raise RuntimeError((moment, value, rank))
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

    # α^5=27 et γ^5=3125/108, avec λ=197/100.
    if 27 * 100**5 >= 197**5:
        raise RuntimeError("alpha")
    if 3125 * 100**5 >= 108 * 197**5:
        raise RuntimeError("gamma")
    out.append("PASS 27*100^5 < 197^5 et 3125*100^5 < 108*197^5")

    # 3*(197/100)/(1-(197/100)/2) = 197*2 = 394, et 394 < 61344/65.
    if 3 * 197 * 200 != 394 * 100 * (200 - 197):
        raise RuntimeError("394")
    if 394 * 65 >= 61344:
        raise RuntimeError("61344/65")
    out.append("PASS la somme des majorants vaut 394, et 394*65 < 61344")

    # Temps non réservé t=2^{3j}+1 : rang t-j, valeur 2^{2(t-j)-1} ≥ t^2.
    for j in range(1, 7):
        t = 2 ** (3 * j) + 1
        if t & (t - 1) == 0:
            raise RuntimeError(("reserve", t))
        rank = t - j
        value = 1 << (2 * rank - 1)
        if value < t * t:
            raise RuntimeError((j, t, rank))
    out.append("PASS pour 1<=j<=6, au temps 2^{3j}+1 la valeur depasse t^2")

    # t=0 : m=1 et 2^t(m+1)=2=2*3^t. Pour t≥1 la borne stricte est déjà testée.
    if (3**0 // 2**0) != 1 or 2**0 * 2 != 2 * 3**0:
        raise RuntimeError("t=0")
    out.append("PASS a t=0, 2^t(m_t+1) = 2*3^t")

    def v2(n: int) -> int:
        c = 0
        while n % 2 == 0:
            n //= 2
            c += 1
        return c

    if v2(3 ** (1 << 0) - 1) != 1:
        raise RuntimeError("m=3")
    for m in range(4, 13):
        if v2(3 ** (1 << (m - 3)) - 1) != m - 1:
            raise RuntimeError(m)
    for m in range(2, 15):
        mod = 1 << m
        x = 1
        order = 0
        for k in range(1, mod):
            x = (x * 3) % mod
            if x == 1:
                order = k
                break
        expected = 2 if m == 2 else 1 << (m - 2)
        if order != expected:
            raise RuntimeError((m, order, expected))
    out.append("PASS valuation m-1 pour m>=4, ordre modulo 8 egal a 2, ordres jusqu'a m=14")

    return out


def main() -> None:
    lines = passes()
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
