#!/usr/bin/env python3
"""Independent exact-integer verification: finite Syracuse valuation words,
2-adic initial realizer, and the backward 3-adic residue identity.
Python 3 stdlib only; no floating point or external dependencies.
"""
from random import Random
import json, csv
from pathlib import Path
rng=Random(20261014)
OUT=Path(__file__).resolve().parent

def initial_class(a):
    s=0; C=0; pow3=1
    for v in a:
        C=3*C+(1<<s)
        s+=v
        pow3*=3
    mod=1<<(s+1)
    r=((1<<s)-C)*pow(pow3,-1,mod)%mod
    assert r&1
    return r,mod

def iterate(n,a):
    seq=[n]
    for v in a:
        z=3*n+1
        actual=(z&-z).bit_length()-1
        assert actual==v, (v,actual)
        n=z>>v
        assert n&1
        seq.append(n)
    return seq

def mod3_shadow(a,t,k):
    assert k<=t
    mod=3**k
    total=0; partial=0
    for j in range(k):
        partial+=a[t-1-j]
        total=(total+3**j*pow(2,-partial,mod))%mod
    return total

def test(a,ks=(1,2,3,4,5,6),copies=1):
    r,mod=initial_class(a)
    for c in range(copies):
        n0=r+mod*(c+1)
        seq=iterate(n0,a)
        for k in ks:
            for t in range(k,len(a)+1):
                assert seq[t]%(3**k)==mod3_shadow(a,t,k), (a,t,k)
    return r,mod

rows=[]; tests=0; checked=0
# Random exact words, including a_t>=3 to avoid special binary-only assumptions.
for N,count in [(1,120),(2,100),(5,90),(15,50),(30,25),(60,5)]:
    for rep in range(count):
        a=[rng.randint(1,6) for _ in range(N)]
        r,mod=test(a,copies=2)
        tests+=1
        checked+=2*sum(max(0,N-k+1) for k in (1,2,3,4,5,6))
    rows.append(dict(family='random_all_positive_valuations',N=N,words=count,checks=checked))
# Exact critical mechanical prefixes: b_t=0 and all odd iterates > n0.
critical=[]
for N in (10,49,100,300,1000):
    pow3=1; Fprev=0; a=[]
    for t in range(1,N+1):
        pow3*=3
        Ft=pow3.bit_length()-1
        a.append(Ft-Fprev)
        Fprev=Ft
    r,mod=initial_class(a)
    n0=r+mod
    seq=iterate(n0,a)
    assert all(v>n0 for v in seq[1:])
    assert all((3*n+1)>>a[t] == seq[t+1] for t,n in enumerate(seq[:-1]))
    assert all(x in (1,2) for x in a)
    critical.append(dict(N=N,minimum_positive_residue_bits=r.bit_length(),modulus_bits=mod.bit_length()-1,seed_bits=n0.bit_length(),all_prefix_states_above_seed=True,first_valuations=''.join(map(str,a[:30]))))
    # Check 3-adic digits only at strategic positions for large N.
    for k in (1,2,3,4,5,6):
        for t in [k, min(N,k+3), min(N,19),N//2,N]:
            if t>=k:
                assert seq[t]%(3**k)==mod3_shadow(a,t,k)
                checked+=1

# Independently generated high-complexity oscillating a(t) from the previous lab.
import importlib.util
# Avoid importing module: it runs whole earlier experiment; replicate control construction
src_osc=OUT/'test_oscillations.py'
spec=importlib.util.spec_from_file_location('osc36',src_osc)
modosc=importlib.util.module_from_spec(spec);spec.loader.exec_module(modosc)
d,_,_,jumps=modosc.build(1000)
a=[]; b=[0]; g=0; state=0x2545F4914F6CDD1D
for t in range(1,1001):
    state^=(state<<13)&((1<<64)-1);state^=(state>>7);state^=(state<<17)&((1<<64)-1)
    jump=t in jumps;g+=int(jump)
    e=(state&1) if d[t]==2 and not jump else 0
    bt=g+e
    v=d[t]-(bt-b[-1]);assert v>=1
    a.append(v);b.append(bt)
r,mod=initial_class(a)
seq=iterate(r+mod,a)
for k in (1,2,3,4,5,6):
    for t in range(k,1001):
        assert seq[t]%(3**k)==mod3_shadow(a,t,k)
        checked+=1
rows.append(dict(family='oscillating_prefix_from_exp35',N=1000,words=1,checks=checked))
with (OUT/'critical_prefixes.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,critical[0].keys());w.writeheader();w.writerows(critical)
results={'random_valuation_words':tests,'tests_across_3adic_digits':checked,'tested_3adic_moduli':[3**k for k in (1,2,3,4,5,6)],'critical_prefixes':critical,'oscillating_prefix_length':1000,'verdict':'all assertions passed'}
(OUT/'results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'random_words':tests,'mod_3k_checks':checked,'critical_N':[x['N'] for x in critical], 'verdict':'PASS'},indent=2))
