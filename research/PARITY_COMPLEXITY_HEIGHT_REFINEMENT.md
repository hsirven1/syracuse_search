# Quantitative height-envelope sharpening of a conditional parity-complexity bound

**Status: elementary conditional theorem with complete argument below; scientific novelty NOT established. Not a proof of the Collatz conjecture.** 16 October 2026.

This is a fresh examination of an existing bound in the external Lean source [`ParityComplexity.lean`](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/ParityComplexity.lean). It is **not** a Lean formalization of the improved theorem and does **not** claim to improve the latest version of that repository or the best published bound. In that frozen file, `unbounded_factor_floor` gives `5q+1 ≤ complexity N (3q+K)`.

## Definitions

Let `T(n)=n/2` for even n, `T(n)=(3n+1)/2` for odd n, acting on positive integers. Let `p_N(L)` count the **distinct length-L contiguous parity blocks across the entire infinite T-orbit of a fixed seed N** (not just its first L iterates). Fix any `K≥0` such that `N+1≤2^K`.

The hypothesis `orbit(N) unbounded` is essential; it is **not** claimed that any such positive integer seed exists.

## Proposition A (general exact integer version)

For each `L≥K`, define

`u(L,K)=max{t≥0 : 3^t ≤ 2^(t+L−K)}`.

This is finite. If the orbit of N is unbounded, then

`p_N(L) ≥ u(L,K)+1`.

Equivalently, with `β=log_2(3/2)>0`,

`p_N(L) ≥ 1+floor((L−K)/β)`.

**Proof.** At each step, `2(T(n)+1)≤3(n+1)`. By induction,

`2^t(T^t(N)+1)≤3^t(N+1)≤3^t 2^K`.

Thus, for any `0≤t≤u(L,K)`, monotonicity of `(3/2)^t` yields

`T^t(N)+1 ≤ (3/2)^t 2^K ≤ 2^L`.

Therefore `0≤T^t(N)<2^L` for these `u+1` initial times. An unbounded deterministic positive orbit has **no repeated states**, because a repeated state would imply an eventually periodic (hence bounded) orbit.

Terras/Everett's finite parity-residue bijection says that two positive integer states with the same first L parities under T are congruent modulo `2^L`. As each of the `u+1` initial states is in `[0,2^L)` and all are distinct, their length-L parity blocks are distinct. Consequently `p_N(L)≥u+1`. QED.

No estimate of factor complexity from a **finite observed sample** is used; `p_N(L)` refers to the whole infinite word.

## Corollary B (explicit refinement of the frozen Lean coefficient)

The exact integer inequality `3^17=129140163<134217728=2^27` gives, for every `q≥0`,

`p_N(10q+K) ≥ 17q+1`.

Indeed, `(3/2)^(17q)≤2^(10q)`, so the initial `17q+1` states lie below `2^(10q+K)` and Proposition A applies.

Thus the linear coefficient of this particular bound is **17/10=1.7**, versus **5/3≈1.6667** in the cited frozen file. Choosing `(r,s)=(41,24)` also works, since `3^41≤2^65`, yielding `p_N(24q+K)≥41q+1` and ratio 41/24≈1.7083.

## Corollary C (liminf estimate)

For a fixed hypothetical unbounded N (hence fixed K),

`liminf_{L→∞} p_N(L)/L ≥ 1/log_2(3/2) ≈ 1.70951129135`.

This follows immediately from Proposition A, whose lower bound is valid for **every** L≥K. This is a conditional complexity restriction, not a universal upper bound and not a contradiction. It says nothing about the convergence of arbitrary Collatz orbits.

## Verification and scientific relevance

- Exact arithmetic checked independently: `3^17=129140163 < 2^27=134217728`; the ratio calculation is not a proof and no Lean compilation was run for these refinements.
- The argument reuses two **classical** ingredients: `T^t(N)+1≤(3/2)^t(N+1)` and uniqueness of a parity word modulo `2^L`. It is a sharpening of a numerical constant in the specific cited argument, **not a new mathematical mechanism**.
- **No priority claim.** Compare to published literature and newer versions of the source before calling any statement novel; a straightforward optimization of 3/5 to log_2(3/2) may already be known.
- An improvement beyond `1/log_2(3/2)` would require an orbit-specific height estimate sharper than the crude per-step growth envelope or another argument not relying only on those two ingredients. No such estimate is established here.
- No attempt is made to construct divergent orbits, generate finite certificates, or prove Syracuse.

## Next mathematical question (explicitly unresolved in this note)

Can one demonstrate, under the **hypothesis of an unbounded positive T-orbit**, a sufficiently stronger bound on the size of its first t states to force `liminf p_N(L)/L>1/log_2(3/2)`, **without** assuming unproved uniform parity frequencies or an a priori complexity envelope?

This is an exploratory objective, not a lemma believed true on evidence and **not** a small known-open theorem: prior art and real mathematical content require critical assessment. Do not turn it into a counting experiment without a genuine inequality.
