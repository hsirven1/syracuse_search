# Exact first descent times: a negative control for our research

**Status:** classical parity-cylinder consequence, not a new result on Syracuse. Time counts **odd-accelerated** steps, not ordinary/shortened Collatz steps.

Let \(U(n)=(3n+1)/2^{v_2(3n+1)}\) for positive odd integers, and let \(\tau_U(n)=\min\{t\ge1:U^t(n)<n\}\).

## Proposition

For every integer \(m\ge1\), infinitely many positive odd integers have **exactly** \(\tau_U(n)=m\).

### Constructive proof

Fix \(m\ge1\). Let \(q_m\pmod{2^{m+1}}\) be the unique odd residue such that

\[
3^m q_m\equiv 1+2^m\pmod{2^{m+1}}.
\]

It exists because \(3^m\) is invertible modulo \(2^{m+1}\). Choose any sufficiently large positive integer \(q\equiv q_m\pmod{2^{m+1}}\) satisfying

\[
(4^m-3^m)q>2^m-1,
\]

and set \(n=2^m q-1\). The congruence ensures \(v_2(3^m q-1)=m\).

For \(0\le t\le m-1\), induction using valuation 1 yields

\[
U^t(n)=3^t\,2^{m-t}q-1.
\]

For every \(1\le t\le m-1\), this exceeds \(n\), because \(3^t>2^t\).

At the final step,

\[
3U^{m-1}(n)+1=2(3^m q-1)
\]

has valuation \(m+1\), and hence

\[
U^m(n)=\frac{3^m q-1}{2^m}<2^m q-1=n.
\]

The strict inequality is **equivalent** to the chosen bound on \(q\). Thus \(\tau_U(n)=m\). Every sufficiently large term of the corresponding arithmetic progression modulo \(2^{2m+1}\) works. QED.

Examples for \(m=1,2,3,4,5\): \(n=9,19,87,15,863\), respectively. The proof is algebraic; these examples are not its basis.

## Research implication

This explicitly generates an infinite family for **every** desired first stopping time, but it excludes no hypothetical divergent integer **outside** the chosen congruence cylinder. Therefore our earlier goal, “prove adaptive descent for some infinite family,” is too weak to establish meaningful progress.

**Stronger success criterion:** prove a result beyond a prearranged, finitely contractive parity/valuation cylinder. Possible targets include a proved cross-scale coverage estimate or a structurally defined family not selected by prescribing a finite descent word. We have **not** achieved either here.

Do not swap quantifiers: \(\forall m\,\exists n:\tau_U(n)=m\) says nothing about \(\forall n>1\,\exists m:\tau_U(n)=m\), which is equivalent to Syracuse for odd starting numbers.

## Reproducibility

Run: python3 research/cylinder_baseline.py

The program verifies the exact formulas and first descent time for every \(1\le m\le150\). It is a finite regression test, **not** the universal proof.

## Literature

The construction is a straightforward use of classical parity coding due to Terras (1976) and Everett (1977), discussed in Lagarias's surveys. For finite convergence classes, see *The convergence classes of Collatz function*, Theoretical Computer Science 412 (2011), https://doi.org/10.1016/j.tcs.2011.05.056. No novelty is claimed.
