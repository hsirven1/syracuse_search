#!/usr/bin/env python3
"""Étude 37 : contrôle exact de la couverture conditionnelle.

T est le Collatz raccourci, pas le Syracuse accéléré.
Le préfixe de r parités est composé uniquement de 1 (impairs).
La programmation dynamique compte les suffixes de longueur k-r tels que
3^j_t > 2^t à tous les temps 1,...,k : chacun GARANTIT non-descente.
Le contrôle brute-force reconstruit directement les entiers de [2^k,2^(k+1)).
Aucune conclusion infinie n'est déduite des seuls calculs.
"""
import json
import math


def shortened(n: int) -> int:
    return (3*n + 1)//2 if n & 1 else n//2


def guaranteed_non_descent(k: int, r: int) -> int:
    assert 1 <= r <= k
    power_three = [3**j for j in range(k+1)]
    power_two = [1 << t for t in range(k+1)]
    counts = {r: 1}
    for t in range(r+1, k+1):
        following = {}
        for j, count in counts.items():
            for next_bit in (0, 1):
                jj = j + next_bit
                if power_three[jj] > power_two[t]:
                    following[jj] = following.get(jj, 0) + count
        counts = following
    return sum(counts.values())


def brute_residue_check(k: int, r: int) -> dict:
    assert k <= 20
    total = actual = guaranteed = 0
    suffixes = set()
    for n in range(1 << k, 2 << k):
        x = n
        bits = []
        never_descended = True
        for t in range(1, k+1):
            bits.append(x & 1)
            x = shortened(x)
            if x < n:
                never_descended = False
        if not all(bit == 1 for bit in bits[:r]):
            continue
        total += 1
        suffixes.add(tuple(bits[r:]))
        if never_descended:
            actual += 1
        if all(3**sum(bits[:i]) > 2**i for i in range(1, k+1)):
            guaranteed += 1
            assert never_descended
    assert total == 1 << (k-r)
    assert len(suffixes) == total
    assert guaranteed == guaranteed_non_descent(k, r)
    return {"k": k, "r": r, "total": total, "guaranteed": guaranteed,
            "actual_non_descent": actual, "fraction": guaranteed / total}


def study() -> dict:
    cases = []
    for k in (30, 60, 100, 200, 400):
        for target in (0.2, 0.27, 1/3, 0.4):
            r = math.ceil(target*k)
            survivors = guaranteed_non_descent(k, r)
            total = 1 << (k-r)
            cases.append({
                "k": k, "r": r, "theta": target,
                "guaranteed": str(survivors), "total": str(total),
                "fraction": round(survivors/total, 12)
            })
    brutes = [brute_residue_check(k, math.ceil(k/3)) for k in (10,14,18)]
    p = math.log(2)/math.log(3)
    return {
        "clock": "T(n)=n/2 if even, (3n+1)/2 if odd",
        "theta_critical": 2*p-1,
        "candidate": "Uniform exponentially small survival in every parity-prefix cylinder r=ceil(k/3)",
        "verdict": "REFUTED; all-odd cylinder has guaranteed survivor fraction -> 1",
        "dynamic_programming": cases,
        "independent_brute_force": brutes
    }


if __name__ == "__main__":
    print(json.dumps(study(), indent=2))
