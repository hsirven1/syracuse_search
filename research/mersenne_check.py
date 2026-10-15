#!/usr/bin/env python3
"""Contrôle FINI, adversarial, de candidats d'horizon de première descente.
Aucun résultat universel sur Syracuse n'est déduit de ces calculs.
"""
import json

def U(n: int) -> int:
    assert n > 0 and (n & 1)
    y = 3*n + 1
    valuation = (y & -y).bit_length() - 1
    return y >> valuation

def first_descent(n: int, limit: int) -> int | None:
    current = n
    for step in range(1, limit + 1):
        current = U(current)
        if current < n:
            return step
    return None

def run(h_max: int = 120) -> dict:
    assert h_max >= 3
    samples = []
    for h in range(3, h_max + 1):
        n = (1 << h) - 1
        current = n
        for t in range(1, h):
            current = U(current)
            assert current == 3**t * 2**(h-t) - 1, (h,t,current)
            assert current > n, (h,t)
        if h <= 50:
            tau = first_descent(n, 20*h)
            samples.append({"h":h,"first_descent":tau})
    return {
        "checked_h": [3,h_max],
        "mersenne_prefix_exact": True,
        "first_descent_search_limit": "20*h for h<=50",
        "witnesses_over_2h": [x for x in samples if x["first_descent"] is None or x["first_descent"] > 2*x["h"]][:12],
        "witnesses_over_4h": [x for x in samples if x["first_descent"] is None or x["first_descent"] > 4*x["h"]][:12],
        "note": "None means unobserved within test horizon, NOT infinite."
    }

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
