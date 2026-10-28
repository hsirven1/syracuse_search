"""Small exact controls for issue #9; stdlib only. No unbounded search."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json


def trajectory(n, j):
    states, bits = [], []
    for _ in range(j):
        states.append(n)
        b = n % 2
        bits.append(b)
        n = (3*n+1)//2 if b else n//2
    return n, tuple(bits), states


def affine(w):
    # Forward composition, independent of endpoint reconstruction.
    a, d = 1, 0
    for i, b in enumerate(w):
        if b:
            a, d = 3*a, 3*d + 2**i
    return a, d


def closed_correction(w):
    positions = [i for i, b in enumerate(w) if b]
    return sum(2**i * 3**(len(positions)-1-t)
               for t, i in enumerate(positions))


def decode(j, q, d):
    w = []
    for _ in range(j):
        b = d % 2
        w.append(b)
        if b:
            if q == 0 or d < 3**(q-1):
                return None
            d = (d-3**(q-1))//2
            q -= 1
        else:
            d //= 2
    return tuple(w) if d == q == 0 else None


def main():
    counts = dict(words=0, lifted_seeds=0, harmonic_checks=0)
    paradoxes, reversals, rows = [], [], []
    for j in range(1, 13):
        modulus = 2**j
        # Independent inverse table: direct iteration of every residue.
        inverse = {trajectory(n, j)[1]: n for n in range(1, modulus+1)}
        assert len(inverse) == modulus
        groups = {}
        for w in product((0, 1), repeat=j):
            q = sum(w)
            a, d = affine(w)
            assert a == 3**q and d == closed_correction(w)
            r = (-d*pow(a, -1, modulus)) % modulus or modulus
            assert inverse[w] == r
            assert decode(j, q, d) == w
            envelope = 2**(j-q)*(3**q-2**q)
            assert d <= envelope
            counts['words'] += 1
            for t in range(3):
                n = r + t*modulus
                end, actual, states = trajectory(n, j)
                assert actual == w and modulus*end == a*n+d
                paradox = a < modulus and end >= n
                assert paradox == (a < modulus and (modulus-a)*n <= d)
                counts['lifted_seeds'] += 1
                if q:
                    odd = [x for x in states if x % 2]
                    factors = [1+Fraction(1, 3*x) for x in odd]
                    p = Fraction(1)
                    for f in factors:
                        p *= f
                    assert Fraction(end, n) == Fraction(a, modulus)*p
                    # Exact AM-GM form of the harmonic-mean envelope.
                    mean = sum(factors, Fraction(0))/q
                    assert p <= mean**q
                    counts['harmonic_checks'] += 1
            if a < modulus:
                g = modulus-a
                low_t = max(0, (3-r+modulus-1)//modulus)
                high_t = (d-g*r)//(g*modulus)  # signed floor, never truncated
                for t in range(low_t, high_t+1):
                    n = r+t*modulus
                    assert trajectory(n, j)[0] >= n
                    paradoxes.append(dict(j=j, q=q, n=n, D=d, r=r,
                                          endpoint=trajectory(n, j)[0]))
                # Independent finite check of exact interval boundaries.
                for t in {low_t, max(low_t, high_t), max(low_t, high_t+1)}:
                    n = r+t*modulus
                    assert (trajectory(n, j)[0] >= n) == (t <= high_t)
            groups.setdefault(q, []).append((d, r, ''.join(map(str, w))))
        for q, data in groups.items():
            data.sort()
            for x, y in zip(data, data[1:]):
                if x[1] > y[1] and len(reversals) < 3:
                    reversals.append(dict(j=j, q=q, lower_D=x, higher_D=y))
        rows.append(dict(j=j, words=modulus))
    assert [(x['j'], x['n']) for x in sorted(paradoxes, key=lambda x:(x['j'],x['n']))] == [(8,n) for n in (7,9,18,19,25)]
    end, w, states = trajectory(7, 8)
    assert states[-1] == 5 and end == 8  # intermediate descent at time 7
    assert affine(w) == (243, 347)
    assert decode(16, 6, 194421) is None
    assert 729*3+194421 == 65536*3
    assert 194421 <= 2**10*(3**6-2**6)
    # Canonical representatives 1 and 2 do not satisfy n>=3 themselves.
    assert trajectory(1, 2)[0] == 1 and trajectory(5, 2)[0] < 5
    assert trajectory(2, 2)[0] == 2 and trajectory(6, 2)[0] < 6
    # Refute both universal directions of a correction/residue ordering.
    for w, expected_r in [((1, 0, 0), 5), ((0, 1, 0), 2),
                          ((1, 0), 1), ((0, 1), 2)]:
        a, d = affine(w)
        m = 2**len(w)
        assert ((-d*pow(a, -1, m)) % m or m) == expected_r
    result = dict(status='PASS', max_length=12, counts=counts,
                  all_seed_paradoxical_pairs_above_two=sorted(paradoxes,key=lambda x:x['n']),
                  correction_residue_order_reversals=reversals,
                  artificial_return=dict(j=16,q=6,D=194421,attainable=False),
                  rows=rows)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'rows'},indent=2))

if __name__ == '__main__':
    main()
