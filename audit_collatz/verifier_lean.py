"""Reconstruit les modules ciblés et inspecte les axiomes des énoncés audités.

Usage : PATH=/workspace/.elan/bin:$PATH ELAN_HOME=/workspace/.elan \
        python3 verifier_lean.py /workspace/collatz
"""
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(sys.argv[1]).resolve()
OUT = Path(__file__).resolve().parent
TARGETS = {
    'NoGo': ['no_uniform_descent_bound', 'no_finite_certificate', 'no_finite_state_certificate'],
    'Critical': ['critical_line_sharp'],
    'Shadow': ['terras_exact_form', 'shadow_modEq', 'dcoef_add', 'density_floor',
               'shadow_compression', 'surviving_shadow_mem'],
    'Terras': ['no_descent_window_bound'],
    'ParityComplexity': ['ParityComplexity.unbounded_factor_floor',
                         'ParityComplexity.bounded_of_linear_complexity',
                         'ParityComplexity.no_sturmian_complexity'],
    'MechanicalComplexity': ['mechanical_complexity_le', 'bounded_of_mechanical',
                             'no_irrational_mechanical', 'no_eventual_irrational_mechanical'],
    'RationalMechanical': ['mechanical_classification', 'eventual_mechanical_reaches_one'],
    'InverseBarrier': ['noncontracting_endpoint_not_one_mod',
                       'bounded_odd_inverse_obstruction', 'arbitrarily_large_inverse_obstructions'],
    'NoncontractingTail': ['unbounded_iff_noncontracting_tail', 'all_orbits_bounded_iff_all_contract'],
    'PruningLimit': ['completion_envelope_survives', 'finite_envelopes_eventually_survive'],
    'CongruenceRelaxation': ['relaxed_closing_correction'],
    'WordCongruence': ['realizes_iff_dvd', 'realizes_paradoxical_iff'],
    'CorrectionDecode': ['correctionAttainable_iff', 'correction_injective'],
    'ResidueMapAudit': ['ResidueMapAudit.no_gap_map_mod32', 'ResidueMapAudit.gap_precision_witness'],
    'IdealBarrier': ['one_lt_idealLimit', 'uniformSupercritical_bound_gt_two'],
    'Cylinder': ['Cylinder.transport', 'Cylinder.mem_parameters', 'Cylinder.quotient_zero_of_height'],
}
WORD = {'PruningLimit', 'CongruenceRelaxation', 'WordCongruence', 'CorrectionDecode'}
names = ['Collatz.'+('WordAffine.' if m in WORD else '')+n
         for m, ns in TARGETS.items() for n in ns]
modules = ['Collatz.'+m for m in TARGETS]
result = {'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
          'modules': modules, 'theorem_count': len(names)}
with (OUT/'logs/lean_build.log').open('w') as log:
    rc = subprocess.run(['lake', 'build', *modules], cwd=ROOT/'lean', stdout=log,
                        stderr=subprocess.STDOUT).returncode
result['build_exit_code'] = rc
if rc == 0:
    query = OUT/'Audit.lean'
    query.write_text('\n'.join('import '+m for m in modules)+'\n'+
                     '\n'.join('#check '+n+'\n#print axioms '+n for n in names)+'\n')
    with (OUT/'logs/lean_axioms.log').open('w') as log:
        rc = subprocess.run(['lake', 'env', 'lean', str(query)], cwd=ROOT/'lean',
                            stdout=log, stderr=subprocess.STDOUT).returncode
    result['axiom_query_exit_code'] = rc
    text = (OUT/'logs/lean_axioms.log').read_text()
    found = dict(re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]", text))
    found.update({n: '' for n in re.findall(r"'([^']+)' does not depend on any axioms", text)})
    result['axioms'] = {n: [x.strip() for x in found[n].split(',') if x.strip()]
                        for n in names if n in found}
    result['missing'] = [n for n in names if n not in found]
    result['standard_foundations_only'] = rc == 0 and not result['missing'] and all(
        set(v) <= {'propext', 'Classical.choice', 'Quot.sound'} for v in result['axioms'].values())
(OUT/'logs/lean_result.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
sys.exit(rc or (0 if result.get('standard_foundations_only') else 1))
