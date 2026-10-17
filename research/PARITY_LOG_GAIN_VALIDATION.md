# Validation and adverse controls — conditional parity logarithmic gain

16 October 2026. **Partial independent numerical regression, no formal verification.**

The arithmetic in \`research/parity_log_gain_checks.py\` was reproduced with an equivalent independently written Python loop, executed in the current research session. **Actual counts**:

| Test | Exact cases checked |
|---|---:|
| Height inequality \`2^t(T^t(N)+1) ≤ 3^t(N+1)\` | 65,792 |
| Odd-run divisibility \`2^r | (x+1)\` | 32,880 |
| Rational proxy for logarithmic even-step lower bound | 65,536 |
| All-odd Mersenne exact equalities and parities | 860 |

Starting values \`N=1,…,256\`, times \`t=0,…,256\`; Mersenne \`2^r−1\` for \`r=1,…,40\`. **All assertions passed.**

The rational proxy uses \`3^5=243<256=2^8\`, so \`δ=log₂3<8/5\` and \`β=δ−1<3/5\`. The same recursive odd-run bound using \`8/5\` instead of \`δ\` implies the weak exact inequality
\[
3\cdot5^{E(t)}t\le 8^{E(t)+1}(K+1).
\]
This is a *testable rational consequence*, not the sharp logarithmic theorem. The simulation checks no hypothetical unbounded orbit (none is known) and therefore does not verify the limiting \`liminf\` statement. Its proof is entirely mathematical, spelled out in \`PARITY_LOGARITHMIC_GAIN.md\`.

The *pushed* repository script has not been re-executed through its own GitHub checkout in this session; its equivalent core logic was executed independently. No Lean compilation or CI was performed.

## Adversarial check

For \`N=2^r−1\`, the first \`r\` input parities are all odd, and
\[
T^t(N)+1=2^r(3/2)^t\qquad (0\le t\le r).
\]
This is an exact infinite family of finite counterexamples to any **uniform** upper growth rate below \`3/2\` with a seed-independent prefactor. It does **not** refute an orbit-specific rate improvement for a fixed hypothetical unbounded integer seed.

## Conclusions and non-results

- **Derived rigorously conditional on the existence of an unbounded positive integer orbit:** \`liminf (p_N(L)−L/β)/log₂ L ≥ δ/(β log₂δ)≈4.07783\`.
- **Not obtained:** any increase in \`liminf p_N(L)/L\` above \`1/β≈1.70951\`, any unconditional divergent orbit or contradiction, Lean formalization, or scientific-priority verification.
- Existing ingredients are classical parity coding and elementary odd-run divisibility; the first-pass online literature check did not locate an identical statement, but absence of a search hit is **not** an antériority claim.
