# Exact first descent times: negative control

**Status:** elementary classical parity-cylinder consequence, not a new Collatz result. Time counts **odd-accelerated** steps, not ordinary or shortened steps.

Let (U(n)=(3n+1)/2^{v_2(3n+1)}) on positive odd integers and (	au_U(n)=min\{t\ge1: U^t(n)<n\}).

## Proposition

For **each** (m\ge1), infinitely many odd positive integers (n) have **exact** first descent time (	au_U(n)=m).

### Constructive proof

Fix (m\ge1). Choose the unique odd residue (q_m\pmod{2^{m+1}}) satisfying

[
3^m q_m\equiv 1+2^m\pmod{2^{m+1}}.
]

This exists since (3) is invertible modulo (2^{m+1}). For any sufficiently large positive integer (q\equiv q_m\pmod{2^{m+1}}) with

[
(4^m-3^m)q>2^m-1,
]

set (n=2^m q-1). The congruence ensures (v_2(3^m q-1)=m).

For each (0\le t\le m-1), induction using valuation 1 gives

[
U^t(n)=3^t2^{m-t}q-1.
]

For (1\le t\le m-1), this exceeds (n), since (3^t>2^t). At step (m), (3U^{m-1}(n)+1=2(3^m q-1)), whose valuation is (m+1), hence

[
U^m(n)=\frac{3^m q-1}{2^m}<2^m q-1=n,
]

the last inequality being exactly the chosen bound on (q).

Thus (	au_U(n)=m). All sufficiently large terms of the arithmetic progression of starting values modulo (2^{2m+1}) work. QED.

For (m=1,2,3,4,5), example seeds are (9,19,87,15,863) respectively. They first descend after (1,2,3,4,5) odd-accelerated steps. The proof is **not** based on simulations.

## Consequence for issue #3

An infinite family with a proven adaptive descent horizon is too weak a success criterion: finite parity/valuation cylinders can **manufacture** one for *any* stopping time. Such a result does not rule out a single divergent orbit outside the family.

The meaningful next target must go **beyond a prearranged finite contractive cylinder**. Possibilities: a rigorously proved cross-scale coverage theorem or a structurally defined family whose descent is not selected by prescribing its finite word. Neither has been obtained here. This construction is **already known in essence** through Terras/Everett parity coding and later convergence-class work.

Do not swap quantifiers: (orall m,exists n,	au_U(n)=m) does not imply (orall n,exists m,	au_U(n)=m), which is the Syracuse conjecture for odd (n>1).

## Reproduction

Run `python3 research/cylinder_baseline.py`. It checks the exact formulas and (	au_U(n)=m) for every (1\le m\le150); this is a regression test, not a universal proof.

References: Terras (1976), Everett (1977), Lagarias surveys; *The convergence classes of Collatz function*, Theor. Comput. Sci. 412 (2011), https://doi.org/10.1016/j.tcs.2011.05.056.
