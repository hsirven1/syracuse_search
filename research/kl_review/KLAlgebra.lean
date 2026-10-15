import Mathlib.Tactic

/- Algebraic interfaces for the candidate operator; NOT a formalization of
   the KL 2003 LP or the universal strict-threshold theorem.
   Index bijections, Brouwer and parameter continuity remain outside scope. -/
namespace KLReview

def min3 (x y z : ℝ) : ℝ := min x (min y z)

theorem min3_le_first (x y z : ℝ) : min3 x y z ≤ x := min_le_left _ _
theorem min3_le_second (x y z : ℝ) : min3 x y z ≤ y :=
  (min_le_right _ _).trans (min_le_left _ _)
theorem min3_le_third (x y z : ℝ) : min3 x y z ≤ z :=
  (min_le_right _ _).trans (min_le_right _ _)

theorem projection_affine (base b x y z : ℝ) (hb : 0 ≤ b) :
    min3 (base+b*x) (base+b*y) (base+b*z) = base+b*min3 x y z := by
  simp only [min3, min_def]
  split_ifs <;> nlinarith

theorem cyclic_min (x y z : ℝ) : min3 y z x = min3 x y z := by
  simp only [min3, min_left_comm, min_comm]

theorem lift_ge (base b x y z : ℝ) (hb : 0 ≤ b) :
    base+b*min3 x y z ≤ base+b*x := by
  have h := mul_le_mul_of_nonneg_left (min3_le_first x y z) hb
  linarith

theorem lift_strict (base b x y z : ℝ) (hb : 0 < b) (hx : min3 x y z < x) :
    base+b*min3 x y z < base+b*x := by
  have h := mul_lt_mul_of_pos_left hx hb
  linarith

theorem nonconstant_fiber (x y z : ℝ) (h : x ≠ y ∨ y ≠ z) :
    min3 x y z < x ∨ min3 x y z < y ∨ min3 x y z < z := by
  by_contra hn
  push_neg at hn
  have h0 := min3_le_first x y z
  have h1 := min3_le_second x y z
  have h2 := min3_le_third x y z
  rcases h with h | h
  · apply h; linarith
  · apply h; linarith

theorem min3_superadditive (x y z u v w : ℝ) :
    min3 x y z + min3 u v w ≤ min3 (x+u) (y+v) (z+w) := by
  apply le_min
  · exact add_le_add (min3_le_first _ _ _) (min3_le_first _ _ _)
  · apply le_min
    · exact add_le_add (min3_le_second _ _ _) (min3_le_second _ _ _)
    · exact add_le_add (min3_le_third _ _ _) (min3_le_third _ _ _)

theorem row_propagation (a b x0 y0 x y z u v w : ℝ) (hb : 0 ≤ b)
    (hx : x ≤ u) (hy : y ≤ v) (hz : z ≤ w) :
    (a*x0+b*min3 x y z) + a*(y0-x0) ≤ a*y0+b*min3 u v w := by
  have hm : min3 x y z ≤ min3 u v w := min_le_min hx (min_le_min hy hz)
  have hh := mul_le_mul_of_nonneg_left hm hb
  nlinarith only [hh]

/-- Saturation of shared auxiliary variables, conditional on this LP schema. -/
theorem auxiliary_elimination {I J : Type*} (c base b : I → ℝ) (u : I → J)
    (x y z : J → ℝ) (hb : ∀ i, 0 ≤ b i) :
    (∃ aux : J → ℝ,
      (∀ j, aux j ≤ x j ∧ aux j ≤ y j ∧ aux j ≤ z j) ∧
      ∀ i, c i ≤ base i+b i*aux (u i)) ↔
    ∀ i, c i ≤ base i+b i*min3 (x (u i)) (y (u i)) (z (u i)) := by
  constructor
  · rintro ⟨aux, haux, hc⟩ i
    have hm : aux (u i) ≤ min3 (x (u i)) (y (u i)) (z (u i)) :=
      le_min (haux _).1 (le_min (haux _).2.1 (haux _).2.2)
    have hh := mul_le_mul_of_nonneg_left hm (hb i)
    linarith [hc i]
  · intro hc
    refine ⟨fun j => min3 (x j) (y j) (z j), ?_, hc⟩
    intro j
    exact ⟨min3_le_first _ _ _, min3_le_second _ _ _, min3_le_third _ _ _⟩

variable {I : Type*}

def orbit (F : (I → ℝ) → (I → ℝ)) (v : I → ℝ) : ℕ → (I → ℝ)
  | 0 => v
  | t+1 => F (orbit F v t)

def walk (σ : I → I) : ℕ → I → I
  | 0, i => i
  | t+1, i => walk σ t (σ i)

theorem orbit_step (F : (I → ℝ) → (I → ℝ)) (v : I → ℝ)
    (hmono : Monotone F) (hv : v ≤ F v) :
    ∀ t, orbit F v t ≤ orbit F v (t+1) := by
  intro t
  induction t with
  | zero => exact hv
  | succ t ih => exact hmono ih

theorem orbit_monotone (F : (I → ℝ) → (I → ℝ)) (v : I → ℝ)
    (hmono : Monotone F) (hv : v ≤ F v) : Monotone (orbit F v) :=
  monotone_nat_of_le_succ (orbit_step F v hmono hv)

/-- Propagate the increments, not a claim of immediate strictness everywhere. -/
theorem difference_lower (F : (I → ℝ) → (I → ℝ)) (σ : I → I)
    (a : ℝ) (ha : 0 ≤ a) (v : I → ℝ)
    (hmono : Monotone F) (hv : v ≤ F v)
    (hprop : ∀ x y, x ≤ y → ∀ i,
      F x i + a*(y (σ i)-x (σ i)) ≤ F y i) (t : ℕ) (i : I) :
    a^t * (F v (walk σ t i)-v (walk σ t i)) ≤
      orbit F v (t+1) i-orbit F v t i := by
  induction t generalizing i with
  | zero => simp [orbit, walk]
  | succ t ih =>
    have hm := orbit_step F v hmono hv t
    have hp := hprop (orbit F v t) (orbit F v (t+1)) hm i
    have hh := mul_le_mul_of_nonneg_left (ih (σ i)) ha
    simp only [walk, pow_succ, orbit] at *
    nlinarith only [hp, hh]

theorem strict_after_cycle (F : (I → ℝ) → (I → ℝ)) (σ : I → I)
    (a : ℝ) (ha : 0 < a) (v : I → ℝ)
    (hmono : Monotone F) (hv : v ≤ F v)
    (hprop : ∀ x y, x ≤ y → ∀ i,
      F x i + a*(y (σ i)-x (σ i)) ≤ F y i)
    (j : I) (hj : v j < F v j) (N : ℕ)
    (hreach : ∀ i, ∃ t < N, walk σ t i = j) :
    ∀ i, v i < orbit F v N i := by
  intro i
  obtain ⟨t, ht, he⟩ := hreach i
  have hl := difference_lower F σ a ha.le v hmono hv hprop t i
  rw [he] at hl
  have hpos : 0 < a^t * (F v j-v j) := mul_pos (pow_pos ha t) (sub_pos.mpr hj)
  have hm := orbit_monotone F v hmono hv
  have h0 := hm (show 0 ≤ t by omega) i
  have hN := hm (show t+1 ≤ N by omega) i
  simp only [orbit] at h0
  linarith

def sumVec (x : ℕ → I → ℝ) (N : ℕ) : I → ℝ :=
  fun i => ∑ t ∈ Finset.range N, x t i

theorem superadditive_sum (F : (I → ℝ) → (I → ℝ))
    (hzero : (fun _ => 0) ≤ F (fun _ => 0))
    (hadd : ∀ x y, F x + F y ≤ F (x+y)) (x : ℕ → I → ℝ) (N : ℕ) :
    sumVec (fun t => F (x t)) N ≤ F (sumVec x N) := by
  induction N with
  | zero => simpa [sumVec] using hzero
  | succ N ih =>
    have he : sumVec x (N+1) = sumVec x N + x N := by
      funext i; simp [sumVec, Finset.sum_range_succ]
    have hf : sumVec (fun t => F (x t)) (N+1) =
        sumVec (fun t => F (x t)) N + F (x N) := by
      funext i; simp [sumVec, Finset.sum_range_succ]
    rw [he, hf]
    intro i
    have hi := ih i
    have hh := hadd (sumVec x N) (x N) i
    change sumVec (fun t => F (x t)) N i + F (x N) i ≤ F (sumVec x N + x N) i
    change F (sumVec x N) i + F (x N) i ≤ F (sumVec x N + x N) i at hh
    linarith

theorem summed_strictification (F : (I → ℝ) → (I → ℝ)) (v : I → ℝ)
    (hzero : (fun _ => 0) ≤ F (fun _ => 0))
    (hadd : ∀ x y, F x + F y ≤ F (x+y)) (N : ℕ)
    (hstrict : ∀ i, v i < orbit F v N i) :
    ∀ i, sumVec (orbit F v) N i < F (sumVec (orbit F v) N) i := by
  intro i
  have hs := superadditive_sum F hzero hadd (orbit F v) N i
  have ht : (∑ t ∈ Finset.range N, orbit F v (t+1) i) + v i =
      (∑ t ∈ Finset.range N, orbit F v t i) + orbit F v N i := by
    have h1 := Finset.sum_range_succ' (fun t => orbit F v t i) N
    have h2 := Finset.sum_range_succ (fun t => orbit F v t i) N
    change (∑ t ∈ Finset.range (N+1), orbit F v t i) =
      (∑ t ∈ Finset.range N, orbit F v (t+1) i) + v i at h1
    linarith
  change (∑ t ∈ Finset.range N, F (orbit F v t) i) ≤ _ at hs
  have he : (∑ t ∈ Finset.range N, F (orbit F v t) i) =
      ∑ t ∈ Finset.range N, orbit F v (t+1) i := rfl
  rw [he] at hs
  have hh := hstrict i
  dsimp [sumVec]
  linarith

end KLReview

#print axioms KLReview.projection_affine
#print axioms KLReview.lift_ge
#print axioms KLReview.lift_strict
#print axioms KLReview.nonconstant_fiber
#print axioms KLReview.difference_lower
#print axioms KLReview.strict_after_cycle
#print axioms KLReview.summed_strictification
#print axioms KLReview.auxiliary_elimination
#print axioms KLReview.min3_superadditive
#print axioms KLReview.row_propagation
