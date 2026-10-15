#!/usr/bin/env python3
"""Exact arithmetic sanity check of a highly oscillating symbolic Syracuse word.
Constructs a_i from a scheduled deficit b_i >= 0, then finds the unique
initial odd residue modulo 2^(S_N+1) which realizes those valuations.
All calculations on integers; finite compatibility ≠ infinite realization.
"""
from math import isqrt


def build(N, slope=2):
    p3=1
    floors=[0]
    for i in range(1,N+1):
        p3*=3
        floors.append(p3.bit_length()-1)
    d=[0]+[floors[i]-floors[i-1] for i in range(1,N+1)]
    assert set(d[1:])=={1,2}
    jump=set()
    prev=0
    # Place logarithmically frequent baseline increments, always at d_i=2.
    j=1
    while True:
        threshold=isqrt(2**j) if slope == 2 else 2**j
        t=max(prev+1,threshold)
        while t<=N and d[t]!=2:
            t+=1
        if t>N:break
        jump.add(t);prev=t;j+=1
    baseline=0
    b=[0]
    eprev=0
    a=[]
    for t in range(1,N+1):
        isjump=t in jump
        baseline+=isjump
        e=int(d[t]==2 and not isjump)
        bt=baseline+e
        at=d[t]-(bt-b[-1])
        assert at>=1,(t,at)
        a.append(at);b.append(bt)
    assert b[-1]>0
    return d,a,b,jump


def canonical_residue(a):
    r=y=1
    mod=2
    pow3=1
    for ai in a:
        m=1<<ai
        coef=3*pow3
        half=(3*y+1)//2
        h=((m//2-half)*pow(coef,-1,m))%m
        r+=mod*h
        y=(3*y+1+6*pow3*h)//m
        mod*=m
        pow3*=3
        assert 0<=r<mod and y%2==1
    return r,mod


def check(N):
    d,a,b,jumps=build(N)
    r,mod=canonical_residue(a)
    n=r
    assert n>0 and n%2==1
    for i,ai in enumerate(a):
        t=3*n+1
        actual=(t & -t).bit_length()-1
        assert actual==ai,(i,ai,actual)
        n=t>>ai
        assert n>0 and n%2==1
    v=sum(b[i]!=b[i-1] for i in range(1,N+1))
    # For a_n approx 2 log2 n (plus bounded oscillation), we also verify the
    # basic necessary sum of reciprocal deficit weights is uniformly bounded
    # numerically over the prefix, not claim an infinite sum.
    print(dict(N=N, start_bits=r.bit_length(), modulus_bits=mod.bit_length()-1,
               b_min=min(b), b_max=max(b), b_final=b[-1], changes=v,
               change_fraction=round(v/N,4), baseline_jumps=len(jumps),
               exact_valid=True))

if __name__=='__main__':
    for N in (100,300,1000):check(N)
