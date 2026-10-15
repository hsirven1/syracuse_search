# Énoncés ciblés et sources figées

Les signatures et axiomes du run sont dans `logs/lean_axioms.log`.

| Déclaration | Source au commit audité |
|---|---|
| `Collatz.no_uniform_descent_bound` | [NoGo.lean:135](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/NoGo.lean#L135) |
| `Collatz.no_finite_certificate` | [NoGo.lean:205](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/NoGo.lean#L205) |
| `Collatz.no_finite_state_certificate` | [NoGo.lean:289](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/NoGo.lean#L289) |
| `Collatz.critical_line_sharp` | [Critical.lean:139](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/Critical.lean#L139) |
| `Collatz.terras_exact_form` | [Shadow.lean:67](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/Shadow.lean#L67) |
| `Collatz.shadow_modEq` | [Shadow.lean:144](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/Shadow.lean#L144) |
| `Collatz.dcoef_add` | [Shadow.lean:194](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/Shadow.lean#L194) |
| `Collatz.density_floor` | [Shadow.lean:276](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/Shadow.lean#L276) |
| `Collatz.shadow_compression` | [Shadow.lean:324](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/Shadow.lean#L324) |
| `Collatz.surviving_shadow_mem` | [Shadow.lean:355](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/Shadow.lean#L355) |
| `Collatz.no_descent_window_bound` | [Terras.lean:164](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/Terras.lean#L164) |
| `Collatz.ParityComplexity.unbounded_factor_floor` | [ParityComplexity.lean:75](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/ParityComplexity.lean#L75) |
| `Collatz.ParityComplexity.bounded_of_linear_complexity` | [ParityComplexity.lean:82](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/ParityComplexity.lean#L82) |
| `Collatz.ParityComplexity.no_sturmian_complexity` | [ParityComplexity.lean:111](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/ParityComplexity.lean#L111) |
| `Collatz.mechanical_complexity_le` | [MechanicalComplexity.lean:56](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/MechanicalComplexity.lean#L56) |
| `Collatz.bounded_of_mechanical` | [MechanicalComplexity.lean:106](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/MechanicalComplexity.lean#L106) |
| `Collatz.no_irrational_mechanical` | [MechanicalComplexity.lean:154](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/MechanicalComplexity.lean#L154) |
| `Collatz.no_eventual_irrational_mechanical` | [MechanicalComplexity.lean:178](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/MechanicalComplexity.lean#L178) |
| `Collatz.mechanical_classification` | [RationalMechanical.lean:122](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/RationalMechanical.lean#L122) |
| `Collatz.eventual_mechanical_reaches_one` | [RationalMechanical.lean:135](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/RationalMechanical.lean#L135) |
| `Collatz.noncontracting_endpoint_not_one_mod` | [InverseBarrier.lean:55](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/InverseBarrier.lean#L55) |
| `Collatz.bounded_odd_inverse_obstruction` | [InverseBarrier.lean:96](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/InverseBarrier.lean#L96) |
| `Collatz.arbitrarily_large_inverse_obstructions` | [InverseBarrier.lean:116](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/InverseBarrier.lean#L116) |
| `Collatz.unbounded_iff_noncontracting_tail` | [NoncontractingTail.lean:79](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/NoncontractingTail.lean#L79) |
| `Collatz.all_orbits_bounded_iff_all_contract` | [NoncontractingTail.lean:99](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/NoncontractingTail.lean#L99) |
| `Collatz.WordAffine.completion_envelope_survives` | [PruningLimit.lean:22](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/PruningLimit.lean#L22) |
| `Collatz.WordAffine.finite_envelopes_eventually_survive` | [PruningLimit.lean:55](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/PruningLimit.lean#L55) |
| `Collatz.WordAffine.relaxed_closing_correction` | [CongruenceRelaxation.lean:11](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/CongruenceRelaxation.lean#L11) |
| `Collatz.WordAffine.realizes_iff_dvd` | [WordCongruence.lean:9](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/WordCongruence.lean#L9) |
| `Collatz.WordAffine.realizes_paradoxical_iff` | [WordCongruence.lean:54](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/WordCongruence.lean#L54) |
| `Collatz.WordAffine.correctionAttainable_iff` | [CorrectionDecode.lean:40](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/CorrectionDecode.lean#L40) |
| `Collatz.WordAffine.correction_injective` | [CorrectionDecode.lean:50](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/CorrectionDecode.lean#L50) |
| `Collatz.ResidueMapAudit.no_gap_map_mod32` | [ResidueMapAudit.lean:13](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/ResidueMapAudit.lean#L13) |
| `Collatz.ResidueMapAudit.gap_precision_witness` | [ResidueMapAudit.lean:8](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/ResidueMapAudit.lean#L8) |
| `Collatz.one_lt_idealLimit` | [IdealBarrier.lean:92](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/IdealBarrier.lean#L92) |
| `Collatz.uniformSupercritical_bound_gt_two` | [IdealBarrier.lean:135](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/IdealBarrier.lean#L135) |
| `Collatz.Cylinder.transport` | [Cylinder.lean:13](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/Cylinder.lean#L13) |
| `Collatz.Cylinder.mem_parameters` | [Cylinder.lean:54](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/Cylinder.lean#L54) |
| `Collatz.Cylinder.quotient_zero_of_height` | [Cylinder.lean:85](https://github.com/msharpe248/collatz/blob/ec8174b567d5cab4960024782210b5f5db02bd3a/lean/Collatz/Cylinder.lean#L85) |
