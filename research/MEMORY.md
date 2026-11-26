# Research memory

Canonical cumulative record for the Syracuse/Collatz investigation. Initialized on 26 November 2026 from `main` at `d930b73` by merging both open research stacks, without conflicts and without changing their stated proof status.

- Fixed-odd-part stack tip: `origin/research/fixed-odd-part-multirun-surjectivity` at `eb79964` (PRs #21, #22, #25, #26, plus the p-adic successive-run notes).
- Triangular stack tip: `origin/research/triangular-2adic-tschakaloff` at `a0c3838` (PRs #21, #22, the even-density audit, PRs #23, #24).

Cursor automation memories are not the source of truth. This branch is.

## Proof status, preserved

| Result | Status | Where |
|---|---|---|
| Finite-descent certificate verifier | Tool, audited; not a Collatz proof | `tools/finite_descent/`, PR #18, #20 |
| Exact stopping time in every length m | Proved, classical Terras/Everett coding | `EXACT_STOPPING_TIME_BASELINE.md` |
| Conditional cover C37 | Refuted | `ETUDE_37_RAPPORT.md` |
| Conditional complexity slope 1/log₂(3/2) | Proved conditionally on an unbounded orbit; already in Dubickas 2009, Thm 5 | `PARITY_COMPLEXITY_HEIGHT_REFINEMENT.md` |
| Logarithmic gain δ/(β log₂ δ) | Proved conditionally on an unbounded orbit; priority not claimed | `PARITY_LOGARITHMIC_GAIN.md` |
| Critical log term with bounded remainder | Proved conditionally; priority not claimed | `EVEN_DENSITY_STRUCTURAL_AUDIT.md` §3 |
| Positive even density on every unbounded orbit | Open | same, conjecture (C) |
| Triangular word has quadratic factor complexity | Proved, combinatorial | `TRIANGULAR_PARITY_WORD_AUDIT.md` |
| Triangular word realized by a positive integer | Open. Equivalent to integrality of f_{3/2}(2) in Q₂. Väänänen–Wallisser 1989 not yet checked on the primary text for α = 2 | `TRIANGULAR_TSCHAKALOFF_PADIC_REDUCTION.md`, `VW1989_PRIMARY_SOURCE_REVIEW.md` |
| Uniform valuation (V) | Proved by specialization of Yu 1999, from the inspected PDF | `YU1999_UNIFORM_VALUATION.md` |
| Log-log complexity gain (P) | Proved conditionally on an unbounded orbit | same, via `PADIC_SUCCESSIVE_RUNS.md` §5 |
| Fixed odd part 5, arbitrary finite run tail | Proved surjective on finite words; not a density theorem | `FIXED_ODD_PART_MULTIRUN_OBSTRUCTION.md` |
| Uniform height-sensitive bound (H) with some B ≤ 1 | **Refuted** | `HEIGHT_SENSITIVE_RUN_BOUND.md`, Theorem 1 |
| (H) for windows of length ≤ K, with B_K = (δ^K − 1)/β and A = 0 | **Proved** | same, Theorem 2 |
| (H) for one pair (A, B) and every window length | **Open.** Any such pair must have B > 1. A = B = 2 is the next test | same |

Krasikov–Lagarias strict monotonicity, studies 38 and 39, and the strategic pause live in draft PRs #6–#8, #10, #12, #14 and #16. They were not merged into this branch. Their recorded verdicts stand: no new lemma retained, KL novelty abandoned, cycle audit stopped short of the Wang/Hercher certificates.

## Current question

Does

sum_{j < k} r_j ≤ 2k + 2 log₂(M+1)

hold for every positive run-start M and every k ≥ 1?

## Next experiment

Prove or refute that single inequality. One explicit window with ratio above 2 refutes it. A proof must be uniform in k and must use the shortness of the run that follows a long run. Do not repeat Theorem 1 and do not extend the seed scan by brute force.

## Reproducibility checked while initializing this branch

From this tree: `parity_log_gain_checks.py`, `triangular_word_checks.py`, `triangular_tschakaloff_checks.py`, `cylinder_baseline.py`, `mersenne_check.py`, and the 23 finite-descent unit tests all passed. `height_sensitive_run_bound_checks.py` passed afterwards.
