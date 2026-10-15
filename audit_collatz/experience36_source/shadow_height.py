#!/usr/bin/env python3
"""Exact finite-scope height lower bounds from backwards 3-adic residues.
These are necessary for a fixed positive initial seed only when b_0..b_t>=0.
All arithmetic uses Python integers.
"""
from pathlib import Path
import csv,json
OUT=Path(__file__).resolve().parent

def valuations(N):
    # Independent reconstruction of prior deterministic high-complexity control.
    # Original generator is imported solely for its sparse-jump schedule.
    import importlib.util
    path=OUT/'test_oscillations.py'
    spec=importlib.util.spec_from_file_location('osc36_height',path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    d,_,_,jumps=mod.build(N)
    a=[];b=[0];g=0;state=0x2545F4914F6CDD1D
    for t in range(1,N+1):
        state^=(state<<13)&((1<<64)-1);state^=(state>>7);state^=(state<<17)&((1<<64)-1)
        jump=t in jumps; g+=int(jump)
        e=(state&1) if d[t]==2 and not jump else 0
        bt=g+e; at=d[t]-(bt-b[-1]);assert at>=1
        a.append(at);b.append(bt)
    return a,b

def mod3_shadow(a,t,k):
    mod=3**k;v=0;cum=0
    for i in range(k):
        cum+=a[t-i-1]
        v+=3**i*pow(2,-cum,mod)
    return v%mod

def canonical_seed(a):
    s=0;C=0; p3=1
    for v in a:
        C=3*C+(1<<s);s+=v;p3*=3
    mod=1<<(s+1)
    return (((1<<s)-C)*pow(p3,-1,mod))%mod

a,b=valuations(5000)
rows=[]
for t in [100,300,1000,5000]:
    orig=canonical_seed(a[:t])
    for k in (8,16,32,64,128,256,512):
        if k>t:continue
        r=mod3_shadow(a,t,k)
        denominator=3*(1<<(b[t]+1))
        numerator=3*r-t*(1<<(b[t]+1))
        seed_min=max(1,numerator//denominator+1)
        rows.append(dict(t=t,k=k,deficit_t=b[t],modulus_bits=(3**k).bit_length(),r_bits=r.bit_length(),necessary_seed_bits=seed_min.bit_length(),canonical_2adic_seed_bits=orig.bit_length(),seed_min=str(seed_min) if seed_min.bit_length()<=128 else f'bitlength:{seed_min.bit_length()}'))
with (OUT/'shadow_height.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,rows[0].keys());w.writeheader();w.writerows(rows)
print('t k deficit bits(r) minseedbits canonicalbits')
for row in rows:
    if row['k'] in (16,64,256,512):
        print(' '.join(str(row[f]) for f in ('t','k','deficit_t','r_bits','necessary_seed_bits','canonical_2adic_seed_bits')))
print('checks:',len(rows),'min modular height bounds computed')
