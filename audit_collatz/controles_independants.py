"""Contrôles finis indépendants, en entiers exacts ; aucune preuve générale."""
from itertools import product
import json


def orbit(n, t):
    values, j, d = [n], 0, 0
    for i in range(t):
        b = n % 2
        j += b
        d = 3*d + (1 << i) if b else d
        n = (3*n+1)//2 if b else n//2
        values.append(n)
    return values, j, d


def correction(word):
    d = j = 0
    for i, b in enumerate(word):
        if b:
            d = 3*d + (1 << i)
            j += 1
    return j, d


def main():
    counts = dict(affine=0, cylinder_shadow=0, cocycle=0,
                  bijection_mod2=0, inverse_obstruction=0, mersenne=0,
                  word_divisibility=0, compression=0)
    for t in range(13):
        words = set()
        shadows = set()
        for r in range(1 << t):
            vs, j, d = orbit(r, t)
            assert (1 << t)*vs[-1] == 3**j*r+d
            counts['affine'] += 1
            words.add(tuple(v % 2 for v in vs[:-1]))
            if 1 << t < 2*3**j:
                shadows.add((j, vs[-1] % 3**j))
            for q in (0, 1, 2, 7):
                ws, k, e = orbit(r+(1 << t)*q, t)
                assert k == j and e == d
                assert ws[-1] == vs[-1]+3**j*q
                assert ws[-1] % 3**j == vs[-1] % 3**j
                counts['cylinder_shadow'] += 1
            if t and 1 << t <= 3**j:
                assert vs[-1] % 3**j != 1
                counts['inverse_obstruction'] += 1
        assert len(words) == 1 << t
        counts['bijection_mod2'] += 1
        exponent = 17*max(t-1, 0)//27
        assert (1 << exponent)*len(shadows) <= 3**t
        counts['compression'] += 1
    for n in range(201):
        for s in range(9):
            a, j, d = orbit(n, s)
            for t in range(9):
                _, k, e = orbit(a[-1], t)
                _, _, f = orbit(n, s+t)
                assert f == 3**k*d+(1 << s)*e
                counts['cocycle'] += 1
    for t in range(9):
        for w in product((0, 1), repeat=t):
            j, d = correction(w)
            for n in range(65):
                vs, _, _ = orbit(n, t)
                actual = tuple(v % 2 for v in vs[:-1]) == w
                assert actual == ((3**j*n+d) % (1 << t) == 0)
                counts['word_divisibility'] += 1
    for L in range(1, 101):
        n = (1 << L)-1
        vs, _, _ = orbit(n, L)
        for j, v in enumerate(vs):
            assert v == 3**j*(1 << (L-j))-1 and v >= n
            counts['mersenne'] += 1
    assert orbit(3, 1)[0][-1] % 32 == 5
    assert orbit(35, 1)[0][-1] % 32 == 21
    assert 3**6*3+194421 == (1 << 16)*3
    actual = tuple(v % 2 for v in orbit(3, 16)[0][:-1])
    assert correction(actual) != (6, 194421)
    print(json.dumps({'status': 'passed', 'counts': counts,
                      'scope': 'finite exact arithmetic only'}, indent=2))


if __name__ == '__main__':
    main()
