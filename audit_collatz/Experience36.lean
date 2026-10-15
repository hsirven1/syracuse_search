import Collatz.Shadow

/- Integer, denominator-cleared version of experiment 36's suffix formula.
   Valuations are zero-indexed: a i is the exponent from n i to n (i+1).
   No claim of scientific novelty, global realization or convergence. -/
namespace Experience36

def clock (a : ℕ → ℕ) (s : ℕ) : ℕ → ℕ
  | 0 => 0
  | k+1 => clock a s k + a (s+k)

def correction (a : ℕ → ℕ) (s : ℕ) : ℕ → ℕ
  | 0 => 0
  | k+1 => 3 * correction a s k + 2 ^ clock a s k

theorem exact_suffix (a n : ℕ → ℕ)
    (h : ∀ i, 2 ^ a i * n (i+1) = 3 * n i + 1) (s k : ℕ) :
    2 ^ clock a s k * n (s+k) = 3 ^ k * n s + correction a s k := by
  induction k with
  | zero => simp [clock, correction]
  | succ k ih =>
    have hs := congrArg (fun x => 2 ^ clock a s k * x) (h (s+k))
    simp only [clock, correction, pow_add, pow_succ]
    rw [show s + (k+1) = (s+k)+1 by omega]
    nlinarith only [hs, ih]

theorem suffix_congruence (a n : ℕ → ℕ)
    (h : ∀ i, 2 ^ a i * n (i+1) = 3 * n i + 1) (s k : ℕ) :
    2 ^ clock a s k * n (s+k) ≡ correction a s k [MOD 3^k] := by
  change (2 ^ clock a s k * n (s+k)) % (3^k) = _
  rw [exact_suffix a n h s k]
  simp [Nat.add_mod]

theorem correction_closed (a : ℕ → ℕ) (s k : ℕ) :
    correction a s k = ∑ i ∈ Finset.range k, 3 ^ (k-1-i) * 2 ^ clock a s i := by
  induction k with
  | zero => simp [correction]
  | succ k ih =>
    rw [correction, ih, Finset.sum_range_succ]
    simp only [Nat.add_sub_cancel, Nat.sub_self, pow_zero, one_mul]
    rw [Finset.mul_sum]
    congr 1
    apply Finset.sum_congr rfl
    intro i hi
    have hi' : i < k := Finset.mem_range.mp hi
    rw [show k-i = (k-1-i)+1 by omega, pow_succ]
    ring

end Experience36

#print axioms Experience36.exact_suffix
#print axioms Experience36.suffix_congruence
#print axioms Experience36.correction_closed
