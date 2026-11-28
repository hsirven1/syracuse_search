#!/usr/bin/env python3
"""Contrôles du cycle 018.

Ils vérifient le cycle trivial, la valeur k(1) du critère attribué à
Eliahou par Halbeisen–Hungerbühler, et l'exclusion de ce cycle hors de
la forme linéaire secondaire. Ils vérifient aussi le chaînon de parité
de B24 et la valeur k(2^40) de ce critère. Ils ne redémontrent pas la
forme linéaire et ne vérifient pas les entiers inférieurs à 2^40.

Usage : python3 research/checks/cycle018_eliahou_scope.py
"""

from fractions import Fraction


def T(n: int) -> int:
    if n % 2:
        return (3 * n + 1) // 2
    return n // 2


def odd_steps(length: int) -> int:
    """Plus grand n tel que 3^n ≤ 2^length. C'est floor(length log_3 2)."""
    n = 0
    power = 1
    limit = 1 << length
    while power * 3 <= limit:
        power *= 3
        n += 1
    return n


def k_of_minimum_one() -> int:
    """Plus petit k ≥ 1 tel que k / n(k) ≤ log2(4) = 2."""
    for k in range(1, 20):
        n = odd_steps(k)
        if n > 0 and k <= 2 * n:
            return k
    raise RuntimeError("k(1) introuvable")


def forward_orbit(start: int, limit: int) -> list[int]:
    seen = []
    x = start
    while x not in seen and len(seen) < limit:
        seen.append(x)
        x = T(x)
    return seen


def v2(n: int) -> int:
    if n == 0:
        raise ValueError("valuation infinie")
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def parity_word(n: int, length: int) -> tuple[int, ...]:
    bits = []
    for _ in range(length):
        bits.append(n & 1)
        n = T(n)
    return tuple(bits)


def log_bounds(terms: int) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
    """Bornes rationnelles de log 2 et de log 3.

    log 2 = Σ 1/(n 2^n). Le reste après N est strictement inférieur à
    1/((N+1) 2^N). log(3/2) est la série alternée de mêmes termes ; le
    reste a le signe du terme suivant et une valeur absolue plus petite.
    """
    log2_sum = Fraction(0)
    alt_sum = Fraction(0)
    den = 1
    for n in range(1, terms + 1):
        den *= 2
        piece = Fraction(1, n * den)
        log2_sum += piece
        alt_sum += piece if n % 2 else -piece
    log2_rem = Fraction(1, (terms + 1) * (1 << terms))
    alt_next = Fraction(1, (terms + 1) * (1 << (terms + 1)))
    log2_lo, log2_hi = log2_sum, log2_sum + log2_rem
    if terms % 2 == 0:
        half_lo, half_hi = alt_sum, alt_sum + alt_next
    else:
        half_lo, half_hi = alt_sum - alt_next, alt_sum
    return (log2_lo, log2_hi), (half_lo + log2_lo, half_hi + log2_hi)


def main() -> None:
    assert T(1) == 2 and T(2) == 1
    trivial = {1, 2}
    assert len(trivial) == 2
    print("PASS cycle trivial {1,2}, cardinal 2")

    assert odd_steps(1) == 0
    assert odd_steps(2) == 1
    assert 3**1 <= 2**2 < 3**2
    print("PASS n(1)=0 et n(2)=1")

    # Lemme 6, pour n = n(l) : l log_3 2 - 1 ≤ n ≤ l log_3 2,
    # soit 3^n ≤ 2^l et 2^l < 3^{n+1}, donc 2^l < 3 * 3^n.
    for length in (1, 2, 16):
        n = odd_steps(length)
        assert 3**n <= 2**length < 3 ** (n + 1)
    print("PASS encadrement de n(l) pour l=1,2,16")

    k1 = k_of_minimum_one()
    assert k1 == 2
    assert len(trivial) >= k1
    print("PASS k(1)=2 et |{1,2}| = k(1)")

    # Forme linéaire secondaire, avec b ≥ 1. Le minimum est 17087915.
    minimum = 17087915
    assert minimum > len(trivial)
    for b in (1, 2):
        value = 17087915 * b
        assert value != 2
    print("PASS {1,2} hors de la forme à b>0")

    orbit = forward_orbit(5, 20)
    assert orbit[0] == 5
    assert 1 in orbit and 2 in orbit
    assert len(orbit) < 20
    print("PASS orbite de 5 finie et rencontre {1,2}")

    # Un pas de parité commune baisse la valuation de exactement un.
    for x in range(1, 65):
        for y in range(1, x):
            if (x & 1) != (y & 1):
                continue
            assert v2(T(x) - T(y)) == v2(x - y) - 1
    print("PASS un pas commun baisse v_2 de 1")

    # k parités communes sur un système complet de restes : injectivité.
    for length in range(1, 11):
        words = {parity_word(n, length) for n in range(1, (1 << length) + 1)}
        assert len(words) == 1 << length
        for n in range(1, 33):
            assert parity_word(n, length) == parity_word(n + (1 << length), length)
    print("PASS mots de longueur 1..10 injectifs sur 1..2^j")

    # Queue de 5. Le premier rang de période 2 est 3. Le rang 4 est un choix.
    tail = [5]
    point = 5
    for _ in range(6):
        point = T(point)
        tail.append(point)
    assert tail == [5, 8, 4, 2, 1, 2, 1]
    assert tail[3] == tail[5] == 2
    assert tail[4] == tail[6] == 1
    assert tail[2] % 2 == 0 and tail[4] % 2 == 1
    for start in range(3):
        assert tail[start] != tail[start + 2]
    assert all(tail[3 + k] == tail[3 + (k % 2)] for k in range(4))
    print("PASS premier rang de période 2 de 5 est s=3")
    print("PASS T^4(5) = T^6(5) = 1")

    # Identité T^j(x) - T^j(y) = 3^{a_j}(x-y)/2^j sur un préfixe commun.
    x, y = 7, 7 + (1 << 6)
    assert parity_word(x, 6) == parity_word(y, 6)
    diff = x - y
    ax, ay = x, y
    odds = 0
    for j in range(0, 7):
        if j:
            if ax & 1:
                odds += 1
            ax, ay = T(ax), T(ay)
        assert (ax - ay) * (1 << j) == (3**odds) * diff
    print("PASS identité 3^{a_j}(x-y)/2^j pour 7 et 71")

    k_value, q_value = certify_k_of_two_to_the_40()
    assert k_value == 17087915
    assert q_value == 10781274
    print("PASS k(2^40)=17087915 et n(k)=10781274")


def certify_k_of_two_to_the_40() -> tuple[int, int]:
    """Plus petit numérateur de (log2 3, log2(3+2^{-40})].

    B et A sont voisins de Farey. Le médian M est dans l'intervalle, et
    l'intervalle est entre B et A. Toute fraction strictement entre B et A
    a un numérateur au moins égal à celui de M.
    """
    (log2_lo, log2_hi), (log3_lo, log3_hi) = log_bounds(100)
    x = Fraction(1, 3 * (1 << 40))
    # x - x^2/2 < log(1+x) < x - x^2/2 + x^3/3
    log1_lo = x - x * x / 2
    log1_hi = log1_lo + (x ** 3) / 3
    beta_num_lo = log3_lo + log1_lo
    beta_num_hi = log3_hi + log1_hi

    left = Fraction(16785921, 10590737)
    right = Fraction(301994, 190537)
    mediant = Fraction(
        left.numerator + right.numerator,
        left.denominator + right.denominator,
    )
    assert mediant == Fraction(17087915, 10781274)
    assert right.numerator * left.denominator - left.numerator * right.denominator == 1
    assert left < right

    def below(frac: Fraction, num_lo: Fraction, den_hi: Fraction) -> bool:
        return frac * den_hi < num_lo

    def above(frac: Fraction, num_hi: Fraction, den_lo: Fraction) -> bool:
        return frac * den_lo > num_hi

    assert below(left, log3_lo, log2_hi)
    assert above(mediant, log3_hi, log2_lo)
    assert below(mediant, beta_num_lo, log2_hi)
    assert above(right, beta_num_hi, log2_lo)

    k = mediant.numerator
    q = mediant.denominator
    assert k * log2_lo > q * log3_hi
    assert k * log2_hi < (q + 1) * log3_lo
    return k, q


if __name__ == "__main__":
    main()
