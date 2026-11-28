#!/usr/bin/env python3
"""Contrôles exacts du cycle 013.

La discussion est dans research/cycles/cycle-013.md. Ce script ne remplace
pas la preuve. Il vérifie le certificat (17), la construction du lemme 2
sur plusieurs modules, et la proportion locale (9) du lemme 3.

Usage : python3 research/checks/cycle013_two_path.py
"""

from math import gcd


def v2(n):
    return (n & -n).bit_length() - 1


def U_step(n):
    x = 3 * n + 1
    e = v2(x)
    return x >> e, e


def factorint(n):
    if n <= 0:
        raise AssertionError("positive")
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2
    if n > 1:
        factors.append(n)
    return factors


def omega(n):
    return len(set(factorint(n)))


def Omega(n):
    return len(factorint(n))


def squarefree(n):
    fac = factorint(n)
    return len(fac) == len(set(fac))


def crt(congruences):
    modulus = 1
    value = 0
    for mod, residue in congruences:
        residue %= mod
        g = gcd(modulus, mod)
        if (residue - value) % g != 0:
            raise AssertionError("incompatible CRT")
        step = modulus // g
        mod_g = mod // g
        inv = pow(step % mod_g, -1, mod_g)
        k = ((residue - value) // g % mod_g) * inv % mod_g
        value = value + modulus * k
        modulus *= mod_g
        value %= modulus
    return value, modulus


def split_M(M):
    u = v2(M) if M % 2 == 0 else 0
    rest = M >> u
    v = 0
    while rest % 3 == 0:
        rest //= 3
        v += 1
    if gcd(rest, 6) != 1:
        raise AssertionError("N not coprime to 6")
    return u, v, rest


def multiplicative_order(base, modulus):
    if modulus == 1:
        return 1
    if gcd(base, modulus) != 1:
        raise AssertionError("base not a unit")
    t = 1
    power = base % modulus
    while power != 1:
        power = power * base % modulus
        t += 1
        if t > modulus:
            raise AssertionError("order")
    return t


def lemma2_forms(M):
    u, v, N = split_M(M)
    K = max(u, 3)
    if N == 1:
        t = 1
    else:
        t = multiplicative_order((9 * pow(8, -1, N)) % N, N)
    A = 9**t
    B = 8**t
    C = 5 * (A - B)
    congruences = [(1 << (3 * t + K), -5)]
    if v > 0:
        congruences.append((3**v, -5))
    if N > 1:
        congruences.append((N, 1))
    r, modulus = crt(congruences)
    L = (1 << (3 * t + K)) * (3**v) * N
    if modulus != L:
        raise AssertionError((modulus, L))
    if (A * r + C) % B != 0 or (A * L) % B != 0:
        raise AssertionError("endpoint not integral")
    s = (A * r + C) // B
    D = (A * L) // B
    return {
        "t": t,
        "K": K,
        "r": r,
        "L": L,
        "s": s,
        "D": D,
        "A": A,
        "B": B,
        "C": C,
    }


def check_path(M, z, forms):
    t = forms["t"]
    start = forms["r"] + forms["L"] * z
    expected_end = forms["s"] + forms["D"] * z
    state = start
    seen = [state]
    word = []
    for _ in range(t):
        state, e1 = U_step(state)
        state2, e2 = U_step(state)
        if (e1, e2) != (1, 2):
            raise AssertionError((M, z, e1, e2, state))
        word.append((e1, e2))
        seen.append(state)
        seen.append(state2)
        state = state2
    if state != expected_end or state <= start:
        raise AssertionError("endpoint")
    if any(x < start or x % 2 == 0 for x in seen):
        raise AssertionError("states")
    if (start - expected_end) % M != 0:
        raise AssertionError("residue")
    if v2(start + 1) != 2 or v2(expected_end + 1) != 2:
        raise AssertionError("carry")
    if gcd(forms["r"], forms["L"]) != 1 or gcd(forms["s"], forms["D"]) != 1:
        raise AssertionError("primitivity")
    det = forms["L"] * forms["s"] - forms["r"] * forms["D"]
    if det != forms["L"] * forms["C"] // forms["B"] or det <= 0:
        raise AssertionError("determinant")
    return start, expected_end, word


def certificate_17():
    paths = [(187, 281, 211), (379, 569, 427)]
    facts = {}
    for a, b, c in paths:
        x, e1 = U_step(a)
        y, e2 = U_step(x)
        if (x, e1, y, e2) != (b, 1, c, 2):
            raise AssertionError("word")
        if c <= a or any(v % 2 == 0 for v in (a, b, c)):
            raise AssertionError("growth")
        facts[a] = factorint(a)
        facts[c] = factorint(c)
    if facts[187] != [11, 17] or facts[211] != [211]:
        raise AssertionError(facts)
    if facts[379] != [379] or facts[427] != [7, 61]:
        raise AssertionError(facts)
    ends = [187, 211, 379, 427]
    if any(n % 24 != 19 or v2(n + 1) != 2 for n in ends):
        raise AssertionError("features")
    if any(not squarefree(n) for n in ends):
        raise AssertionError("squarefree")
    # Orientations: composite to prime, then prime to composite.
    d_omega = [omega(211) - omega(187), omega(427) - omega(379)]
    d_Omega = [Omega(211) - Omega(187), Omega(427) - Omega(379)]
    if d_omega != [-1, 1] or d_Omega != [-1, 1]:
        raise AssertionError((d_omega, d_Omega))
    weights = (1, 1)
    if weights[0] * d_omega[0] + weights[1] * d_omega[1] != 0:
        raise AssertionError("omega weights")
    if weights[0] * d_Omega[0] + weights[1] * d_Omega[1] != 0:
        raise AssertionError("Omega weights")
    # One large negative coefficient decreases the prime-to-composite path.
    beta = -10**6
    h_inc = [211 - 187, 427 - 379]
    v_inc = [h_inc[i] + beta * d_omega[i] for i in (0, 1)]
    if not (v_inc[1] < 0 < v_inc[0]):
        raise AssertionError(v_inc)
    weighted = weights[0] * v_inc[0] + weights[1] * v_inc[1]
    if weighted != weights[0] * h_inc[0] + weights[1] * h_inc[1] or weighted <= 0:
        raise AssertionError(weighted)


def nu_formula(ell, a, c, delta):
    if c % ell == 0:
        return (0, 1)
    if a % ell == 0:
        return (1, ell * ell)
    if delta % ell == 0:
        return (0, 1)
    return (1, ell * (ell - 1))


def nu_empirical(ell, a, b, c, d):
    mod = ell * ell
    eligible = 0
    forbidden = 0
    for z in range(mod):
        if gcd(a * z + b, ell) != 1:
            continue
        eligible += 1
        if (c * z + d) % mod == 0:
            forbidden += 1
    return forbidden, eligible


def density_checks():
    forms = []
    for M in (1, 5, 7, 8, 9, 24, 35, 45):
        data = lemma2_forms(M)
        forms.append((data["L"], data["r"], data["D"], data["s"]))
    forms.extend(
        [
            (2, 1, 4, 1),
            (3, 1, 3, 2),
            (6, 1, 15, 2),
            (15, 2, 21, 4),
            (4, 1, 9, 2),
        ]
    )
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    checked = 0
    for a, b, c, d in forms:
        if gcd(a, b) != 1 or gcd(c, d) != 1 or a <= 0 or c <= 0:
            raise AssertionError("not primitive")
        delta = a * d - b * c
        if delta == 0:
            raise AssertionError("proportional")
        for ell in primes:
            num, den = nu_formula(ell, a, c, delta)
            got_num, got_den = nu_empirical(ell, a, b, c, d)
            if got_den == 0 or got_num * den != num * got_den:
                raise AssertionError((a, b, c, d, ell, num, den, got_num, got_den))
            checked += 1
    return checked


def main():
    certificate_17()
    moduli = (1, 5, 7, 8, 9, 24, 35, 40, 45, 72, 105, 360)
    built = []
    for M in moduli:
        data = lemma2_forms(M)
        for z in (0, 1, 2):
            check_path(M, z, data)
        built.append((M, data["t"], data["r"], data["L"]))
    if built[0] != (1, 1, 59, 64):
        raise AssertionError(built[0])
    # M=24 recovers the two displayed paths at z=0 and z=1.
    data = lemma2_forms(24)
    if (data["r"], data["s"], data["L"], data["D"]) != (187, 211, 192, 216):
        raise AssertionError(data)
    if data["r"] + data["L"] != 379 or data["s"] + data["D"] != 427:
        raise AssertionError("second path")
    checked = density_checks()
    # Both orientations for M=1, by exact factorization, z bounded.
    data = lemma2_forms(1)
    plus = minus = None
    for z in range(0, 20000):
        start = data["r"] + data["L"] * z
        end = data["s"] + data["D"] * z
        if start > 2_000_000:
            break
        fs = factorint(start)
        fe = factorint(end)
        if len(fs) == 1 and squarefree(end) and omega(end) >= 2 and plus is None:
            plus = (z, start, end, fs, fe)
        if len(fe) == 1 and squarefree(start) and omega(start) >= 2 and minus is None:
            minus = (z, start, end, fs, fe)
        if plus and minus:
            break
    if plus is None or minus is None:
        raise AssertionError((plus, minus))
    scope_checks(plus, minus)
    print("PASS certificate (17) and one-sided cancellation")
    print("PASS lemma 2 on", ",".join(str(M) for M in moduli))
    print("PASS local densities", checked)
    print("PASS M=1 orientations", plus[0], minus[0])
    print("PASS example scope and the single prime-to-prime path")


def scope_checks(plus, minus):
    """Review 6093000151: M=1 balances, X_0 bounds, and X33."""
    if plus[:3] != (5, 379, 427) or minus[:3] != (1, 123, 139):
        raise AssertionError((plus, minus))
    beta = 100
    # 123 -> 139 changes omega by -1; 379 -> 427 changes it by +1.
    loss = (139 - 123) + beta * (omega(139) - omega(123))
    gain = (427 - 379) + beta * (omega(427) - omega(379))
    if (loss, gain, loss + gain) != (-84, 148, 64):
        raise AssertionError((loss, gain))
    ends = (123, 139, 379, 427)
    if any(n % 16 != 11 or v2(n + 1) != 2 for n in ends):
        raise AssertionError("M=1 features")
    if 123 % 24 != 3 or 139 % 24 != 19 or loss + 100 != 16:
        raise AssertionError("M=24 residue")
    if min(plus[1], minus[1]) != 123:
        raise AssertionError("M=1 threshold")
    if min(187, 379) != 187:
        raise AssertionError("M=24 threshold")
    states = [59]
    state = 59
    for expected in (1, 2):
        state, exponent = U_step(state)
        if exponent != expected:
            raise AssertionError((state, exponent))
        states.append(state)
    if states != [59, 89, 67]:
        raise AssertionError(states)
    if factorint(59) != [59] or factorint(67) != [67]:
        raise AssertionError("primes")
    if v2(59 + 1) != 2 or v2(67 + 1) != 2:
        raise AssertionError("valuation")
    if 59 % 8 != 3 or 67 % 8 != 3 or min(states) < 59 or 67 <= 59:
        raise AssertionError("single path")


if __name__ == "__main__":
    main()
