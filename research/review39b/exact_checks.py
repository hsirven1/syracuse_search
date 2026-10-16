"""Issue #13: small rational controls, not the unavailable Wang S5 certificate."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def log_interval(a, n=32):
    x = F(a-1, a+1)
    lo = 2*sum((x**(2*r+1)/F(2*r+1) for r in range(n)), F(0))
    return lo, lo+2*x**(2*n+1)/((2*n+1)*(1-x*x))


def geom(delta, h):
    return sum((delta**i for i in range(h)), F(0))


def direct_run(n):
    k = l = 0
    while n % 2:
        n = (3*n+1)//2
        k += 1
    while n % 2 == 0:
        n //= 2
        l += 1
    return k, l, n


def main():
    lo2, hi2 = log_interval(2)
    lo3, hi3 = log_interval(3)
    dlo, dhi = lo3/hi2, hi3/lo2
    assert F(158,100) < dlo < dhi < F(159,100)
    # Actual-delta counterexample to transplanting the CLOSED h-polyhedron
    # bound to an arbitrary block in a larger cycle of logarithmic variables.
    xs = (F(9), F(4), F(6))
    assert all(xs[(i+1)%3] < dlo*xs[i] for i in range(3))
    assert xs[0] > dhi*xs[1]  # the 2-block (9,4) has no internal closing edge
    # B=13: v=13/(1+delta)>5 and delta*v>7, rigorously.
    assert 13/(1+dhi) > 5 and 13*dlo/(1+dlo) > 7
    upper_closed = F(3,2**5-1)+F(3,2**7-1)
    actual_block = F(3,2**9-1)+F(3,2**4-1)
    assert actual_block > F(3,15) > upper_closed
    words = suffixes = growth_tests = 0
    delta = F(3,2)
    for m in range(1,7):
        for ks in product(range(1,4), repeat=m):
            mean = F(sum(ks),m)
            partial = [F(0)]
            for k in ks:
                partial.append(partial[-1]+k-mean)
            e = max(range(m),key=lambda i:partial[i])
            # A rational cyclic cap: ks_i <= x_i, x_(i+1) <= delta*x_i.
            caps = [max(F(ks[(i+d)%m])/delta**d for d in range(m))
                    for i in range(m)]
            assert all(caps[(i+1)%m] <= delta*caps[i] for i in range(m))
            for s in range(1,m+1):
                start = (e-s)%m
                block_sum = sum(ks[(start+d)%m] for d in range(s))
                assert F(block_sum) <= caps[start]*geom(delta,s)
                growth_tests += 1
                # Every suffix of the SAME selected block ends at e.
                for t in range(1,s+1):
                    r = (e-t)%m
                    total = sum(ks[(r+d)%m] for d in range(t))
                    assert total >= t*mean
                    assert caps[r] >= t*mean/geom(delta,t)
                    suffixes += 1
            words += 1
    residue_checks = accepted = 0
    for n in range(3,256,2):
        actual_k, actual_l, endpoint = direct_run(n)
        assert 2**(actual_k+actual_l)*endpoint == 3**actual_k*(n+1)-2**actual_k
        for k in range(1,9):
            for ell in range(1,13):
                modulus = 2**(ell+1)
                a_residue = pow(3**k,-1,modulus)*(1+2**ell)%modulus
                algebraic = ((n+1)%2**k == 0 and
                             ((n+1)//2**k)%modulus == a_residue)
                assert algebraic == ((k,ell)==(actual_k,actual_l))
                accepted += algebraic
                residue_checks += 1
    # The advertised first-run bound 75 follows from the stated height interval.
    X = 2**71
    assert 24*X+1 < 2**76
    assert X <= 2**75-1 <= 24*X
    # Non-strict suffix inequalities cannot be upgraded to strict ones.
    assert all(sum((2,2)[-h:]) == 2*h for h in (1,2))
    result = dict(status='PASS', cyclic_lists=words,
                  growth_window_checks=growth_tests,
                  same_block_suffix_checks=suffixes,
                  one_block_residue_checks=residue_checks,
                  one_block_accepted=accepted,
                  transplant_counterexample=dict(full_cycle_log_variables=[9,4,6],
                    selected_block=[9,4],B=13,actual_S=str(actual_block),
                    certified_upper_for_closed_model=str(upper_closed),
                    integer_Collatz_cycle=False),
                  Hercher_original_retrieved=False, Wang_original_retrieved=False,
                  Wang_original_filters_tested=False, S5_certificate_replayed=False,
                  new_lean_compilations=0)
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
