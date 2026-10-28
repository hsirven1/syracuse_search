"""Small exact controls. These are NOT tests of the unavailable Wang lemma."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def suffix_balanced(x):
    return all(len(x)*sum(x[-h:]) >= h*sum(x) for h in range(1, len(x)+1))


def rotations(x):
    return [x[i:]+x[:i] for i in range(len(x))]


def block_cycle(ks, ls):
    word = tuple(b for k, l in zip(ks, ls) for b in [1]*k+[0]*l)
    a, d = 1, 0
    for i, b in enumerate(word):
        if b:
            a, d = 3*a, 3*d+2**i
    seed = F(d, 2**len(word)-a)
    state = seed
    states, minima = [], []
    for k, l in zip(ks, ls):
        minima.append(state)
        for _ in range(k):
            states.append(state)
            nxt = (3*state+1)/2
            assert nxt > state
            state = nxt
        for _ in range(l):
            states.append(state)
            nxt = state/2
            assert nxt < state
            state = nxt
    assert state == seed and seed > 0
    return seed, minima, states


def log_interval(a, n=32):
    # log(a)=2 sum x^(2r+1)/(2r+1), x=(a-1)/(a+1).
    x = F(a-1, a+1)
    low = 2*sum((x**(2*r+1)/F(2*r+1) for r in range(n)), F(0))
    tail = 2*x**(2*n+1)/((2*n+1)*(1-x*x))
    return low, low+tail


def main():
    words = windows = 0
    for m in range(1, 7):
        for x in product(range(1, 4), repeat=m):
            rots = rotations(x)
            assert any(suffix_balanced(y) for y in rots)
            for h in range(1, m+1):
                sums = [sum(y[:h]) for y in rots]
                assert sum(sums) == h*sum(x)
                assert m*max(sums) >= h*sum(x)
                windows += 1
            words += 1
    x = (3, 1)
    assert not suffix_balanced(x) and suffix_balanced((1, 3))
    assert sum(x) == 2*F(sum(x), len(x))  # total balance doesn't imply suffix balance
    seed, minima, states = block_cycle((3, 1), (1, 2))
    assert seed == F(73, 47) and minima == [F(73, 47), F(179, 47)]
    assert seed == min(states) and not suffix_balanced((3, 1))
    # A rational branch-labelled closed orbit, NOT an integer Collatz cycle.
    assert any(v.denominator != 1 for v in states)
    # Exact counterexample to the reciprocal inference x<U => R<3/U.
    x, upper, reciprocal_sum = F(4), F(8), F(1, 2)
    assert x < upper and reciprocal_sum < 3/x and reciprocal_sum > 3/upper
    # Convexity gives the wrong direction for an upper bound at the average.
    assert F(0)**2+F(2)**2 > 2*F(1)**2
    lo2, hi2 = log_interval(2)
    lo3, hi3 = log_interval(3)
    delta_lo, delta_hi = lo3/hi2, hi3/lo2
    assert F(158, 100) < delta_lo < delta_hi < F(159, 100)
    assert delta_lo > 1
    # For actual delta>1: delta^2>delta. For n=2, 2^delta=3,
    # so 2^(delta^2)=3^delta>3, contradicting the printed <=.
    # Independent integer-arithmetic illustration at delta=3/2, n=16.
    assert 512 > 64 and 512**4 == 16**9 and 64**2 == 16**3
    # Old X0 isn't the 2^71 bound; don't substitute it silently.
    old = 704*2**60
    assert old < 2**70 < 2**71
    result = dict(status='PASS', cyclic_sequences=words,
                  averaged_window_checks=windows,
                  arbitrary_global_anchor_counterexample=[3, 1],
                  rational_relaxation=dict(ks=[3,1],ls=[1,2],
                    minima=list(map(str,minima)),integer_collatz_cycle=False),
                  delta_enclosure=dict(lower=str(delta_lo),upper=str(delta_hi)),
                  reciprocal_inference_counterexample=dict(x='4',U='8',R='1/2'),
                  wang_lemma_tested=False, wang_fulltext_available=False,
                  hercher_corrigendum_tested=False,
                  massive_computation=False, lean_compilations=0)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='delta_enclosure'},indent=2))

if __name__ == '__main__':
    main()
