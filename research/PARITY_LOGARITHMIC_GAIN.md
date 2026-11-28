# Divisibility of odd runs yields a logarithmic, but not linear-rate, gain in parity factor complexity

**16 October 2026. Mathematical status: conditional propositions proved below from elementary identities; NOT formally checked in Lean; scientific novelty NOT established.** This note concerns only the *shortcut* Collatz function
\[
T(n)=\begin{cases}
n/2 & n \text{ even},\\
(3n+1)/2 & n \text{ odd},
\end{cases}
\qquad n\in\mathbb N_{>0}.
\]
It does **not** prove Syracuse. This is a follow-up to [the parent PR #21](../PARITY_COMPLEXITY_HEIGHT_REFINEMENT.md), analyzing the exact mechanisms in the frozen
[\`ParityComplexity.lean\`](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/ParityComplexity.lean)
and
[\`DefectHeight.lean\`](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/DefectHeight.lean).

Throughout, let \(n_t=T^t(N)\), \(E(t)=\#\{0\le s<t:n_s\text{ even}\}\),
\[
\delta=\log_2 3=1.5849625007\ldots,\quad
\beta=\log_2(3/2)=\delta-1=0.5849625007\ldots,
\]
and choose \(K\in\mathbb N\) with \(N+1\le 2^K\).
The function \(p_N(L)\) counts the distinct contiguous parity factors of length \(L\) in the **entire infinite** orbit of \(N\).

## Result 1 — logarithmically many even steps, without a divergence hypothesis

**Proposition 1.** For **every** positive starting value \(N\) and every \(t\ge1\),
\[
\boxed{\quad t\ \le\ \frac{(K+1)\delta^{E(t)+1}}{\beta},\qquad
E(t)\ \ge\ \frac{\log_2 t}{\log_2\delta}
-\left(1+\frac{\log_2((K+1)/\beta)}{\log_2\delta}\right).\quad} \tag{1}
\]
This is not a linear-density statement: it only forces \(E(t)=\Omega_N(\log t)\).

**Proof, including the divisibility issue.** Suppose \(r\) consecutive steps starting at an integer \(x>0\) are **odd**. Each such step satisfies
\[
T(y)+1=\frac32(y+1).
\]
Hence
\[
T^r(x)+1 = \frac{3^r(x+1)}{2^r},
\]
and since the left side is an integer and \(3\) is odd, **\(2^r\mid x+1\)**. In particular \(2^r\le x+1\).

At every time \(s\), independently of its parity,
\[
2^s(n_s+1)\le 3^s(N+1)\le 3^s2^K,\quad\text{so}\quad
\log_2(n_s+1)\le K+\beta s. \tag{2}
\]
This is exactly the height mechanism of \`DefectHeight.lean\`.

Write the first \(t\) parities as alternating **runs of odd steps** and \(e=E(t)\) even steps. Let \(s_0=0\), and, for \(0\le i<e\), let \(s_{i+1}\) be the time immediately after the \((i+1)\)-st even step. If \(r_i\) is the number of consecutive odd steps starting at \(s_i\) and immediately preceding this even step, the divisibility and (2) give
\[
r_i\le \log_2(n_{s_i}+1)\le K+\beta s_i.
\]
Therefore
\[
s_{i+1}=s_i+r_i+1\le\delta s_i+(K+1).
\]
Induction yields \(s_e\le(K+1)(\delta^e-1)/\beta\).
The final \(t-s_e\) steps are all odd, and the **same** divisibility argument gives
\(t-s_e\le K+\beta s_e\). Consequently,
\[
t\le\delta s_e+K
\le\frac{\delta(K+1)(\delta^e-1)}{\beta}+K
\le\frac{(K+1)\delta^{e+1}}{\beta}.
\]
Taking logarithms proves (1). QED.

**Critical quantifier:** the additive constant depends on \(N\) through \(K\). One cannot use the resulting lower bound on \(E(t)\) with a uniform seed-independent constant.

## Result 2 — exact parity-sensitive height identity

For any \(t\ge0\),
\[
\boxed{\quad
\log_2(n_t+1)=\log_2(N+1)+\beta t-\delta E(t)+R(t),
\quad R(t)=\sum_{\substack{0\le s<t\\n_s\text{ even}}}
\log_2\left(1+\frac{1}{n_s+1}\right).\quad} \tag{3}
\]

**Proof.** An odd step multiplies \(n+1\) **exactly** by \(3/2\), while an even step multiplies it **exactly** by
\[
\frac{n+2}{2(n+1)}=\frac12\left(1+\frac1{n+1}\right).
\]
Taking logarithms of the product of these factors proves (3). QED.

An unbounded orbit of a deterministic map on the positive integers has **no repeated states**; hence its states are all distinct, and \(n_t\to\infty\). By (1), \(E(t)\to\infty\). The summands in \(R(t)\), indexed over even steps, therefore tend to zero. Their Cesàro average tends to zero, so
\[
\boxed{R(t)=o(E(t))\quad\text{under the hypothesis that the orbit is unbounded}.} \tag{4}
\]
**No reciprocal-summability theorem is needed for (4).** The frozen external repo separately states stronger reciprocal-summability theorems in \`OrbitSummability.lean\`, but importing those is unnecessary here and they have not been recompiled in this study.

## Result 3 — rigorous logarithmic improvement for a hypothetical unbounded orbit

**Conditional theorem.** If \(N>0\) has an **unbounded** \(T\)-orbit, then
\[
\boxed{\quad
\liminf_{L\to\infty}
\frac{p_N(L)-L/\beta}{\log_2 L}
\ \ge\
\frac{\delta}{\beta\,\log_2\delta}
=4.07783364\ldots.\quad} \tag{5}
\]
In particular it strengthens \(p_N(L)\ge L/\beta-O_N(1)\) by a growing **logarithmic** term, while retaining the asymptotic **linear coefficient** \(1/\beta=1.70951129\ldots\).

**Proof.** By (3)–(4), for any fixed \(0<\varepsilon<\delta\), the sum \(R(t)\) is at most \(\varepsilon E(t)+C_{N,\varepsilon}\), giving
\[
\log_2(n_t+1)\le K+\beta t-(\delta-\varepsilon)E(t)+C_{N,\varepsilon}.
\]
Proposition 1 gives a constant \(C'_{N,\varepsilon}\) such that
\[
\log_2(n_t+1)\le K+\beta t
-\frac{\delta-\varepsilon}{\log_2\delta}\log_2 t
+C'_{N,\varepsilon}\quad(t\ge1). \tag{6}
\]
Choose any
\[
0<c<\frac{\delta}{\beta\log_2\delta}.
\]
Choose \(\varepsilon\) sufficiently small that
\(\beta c<(\delta-\varepsilon)/\log_2\delta\), and put
\[
t_L=\left\lfloor\frac{L-K}{\beta}+c\log_2 L\right\rfloor.
\]
For sufficiently large \(L\), (6) gives
\(\log_2(n_{t_L}+1)\le L\). The bound on the right of (6) is **eventually increasing in \(t\)** since its derivative is \(\beta-O(1/t)>0\), so it also yields \(0\le n_s<2^L\) for **every \(0\le s\le t_L\)** (taking care of the finitely many small \(s\) separately).

As in \`ParityComplexity.factor_floor_of_injective_prefix\`, distinct states below \(2^L\) have distinct length-\(L\) parity blocks: equality of such blocks implies congruence modulo \(2^L\) by the classical parity-coding bijection, then equality of states, impossible along an unbounded orbit. Thus
\[
p_N(L)\ge t_L+1
\ge\frac L\beta+c\log_2 L-O_{N,c}(1).
\]
Let \(c\) tend to \(\delta/(\beta\log_2\delta)\). This proves (5). QED.

**No unconditional nontrivial trajectory conclusion is claimed**: the existence of a positive unbounded orbit remains unproved, and the theorem says how complicated such an orbit *would have to be*.

## Adversarial obstruction — why this method does NOT improve the linear coefficient

The tempting statement “some fixed proportion \(\eta>0\) of every long parity word consists of even steps” is **false**, uniformly across positive starting values. For every \(r\ge1\), the seed
\[
N=2^r-1
\]
has its first \(r\) steps all odd, with
\[
T^t(N)+1=2^r(3/2)^t\qquad(0\le t\le r).
\]
Therefore the universal exponential height envelope \((3/2)^t(N+1)\) is **attained exactly** for arbitrarily long finite segments with a growing starting seed. Any universal replacement \((3/2)^t\) by \(\lambda^t\), \(\lambda<3/2\), with a fixed seed-independent multiplicative constant, is refuted by these examples.

This obstruction does **not** refute a better growth exponent restricted to one *fixed hypothetical unbounded orbit*. Such an improvement would need to control its even-step frequency much more strongly than (1), or use independent orbit-specific arithmetic rigidity.

**Precise conditional doorway, not a proven/open-by-priority lemma.** If some fixed \(\eta>0\) could be proved to satisfy
\[
\liminf_{t\to\infty}\frac{E(t)}t\ge\eta
\quad\text{for every positive unbounded orbit,}
\]
then (3)–(4) would yield an eventual growth exponent at most \(\beta-\delta\eta\), and (for \(0<\eta<\beta/\delta\)) the complexity coefficient could be raised above \(1/\beta\). If \(\eta\ge\beta/\delta\), the implications need more care: they approach or cross a fundamental growth obstruction and might exclude divergence outright. **We have proved no such linear-density lower bound.** No demonstration of novelty or current open status for this formulation is claimed.

## Relation to existing sources and scope of literature check

1. [Lean \`DefectHeight.lean\` at audited commit](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/DefectHeight.lean) proves (2) in integer form and rounds it using \(3^5\le2^8\).
2. [Lean \`ParityComplexity.lean\` at audited commit](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/ParityComplexity.lean) proves the injectivity/parity-block implication and a linear \(5/3\) bound. PR #21 refines the linear constant to \(1/\beta\); this note refines the **additive order** further.
3. [Terras (1976)](https://doi.org/10.4064/aa-30-3-241-252) and [Everett (1977)](https://doi.org/10.1016/0001-8708(77)90087-1) supply the classical finite parity coding. No newly established priority here.
4. [Tao (2022)](https://doi.org/10.1017/fmp.2022.8) proves an “almost all” result about minima, not a deterministic uniform height exponent for every hypothetical unbounded orbit.
5. The recent [Christoffel-word preprint (Fernández–Ibáñez, 2026)](https://arxiv.org/abs/2607.24844) concerns extremal cyclic words, a different setting. General web searching for “Collatz divergent parity factor complexity logarithmic lower bound” and variants did not uncover a direct published counterpart, but **non-discovery by search does not establish novelty**.

**Explicit non-results:** no proof of Syracuse; no rigorous improvement to the \(\liminf p_N(L)/L\) coefficient beyond \(1/\beta\); no new orbit-specific linear-density theorem; no Lean compilation in this follow-up.

## Reproducibility

\`research/parity_log_gain_checks.py\` performs small exact-integer checks for the run divisibility, the height envelope, and the all-odd Mersenne adversary, with independent direct iteration. The asymptotic conditional theorem follows from the proof, **not** from those finite checks.

**Research verdict:** a self-contained rigorous *logarithmic sharpening of the conditional complexity bound* has been derived and submitted for independent review; priority remains undetermined. The principled next mathematical hurdle is to beat the exponential-growth slope rather than optimize its finite-size error.