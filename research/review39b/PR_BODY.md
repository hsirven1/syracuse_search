Refs #13 ; revue indépendante de la PR #12, sans modifier les anciens rapports.

Verdict global : **NON VÉRIFIABLE pour m≤95**, ARRÊT de recherche additionnelle. Aucun résultat de Wang ou du corrigendum original n'est déclaré réfuté.

Le rapport prouve l'atteinte et la réduction aux sommets pour le modèle convexe cyclique transcrit, sous B>G_h. Il distingue ce modèle d'un bloc ouvert et fournit un contre-exemple exact au transfert automatique. Il reconstitue les lemmes 5–7 selon le suivi et ne trouve pas de faute dans cette chaîne. Le raccord du corrigendum officiel, les lemmes 11–13, X=2^71 et le certificat S5 demeurent non vérifiés : sources et artefacts inaccessibles.

Tests : `python3 research/review39b/exact_checks.py` PASS ; 1 092 listes, 6 015 fenêtres, 19 956 suffixes et 12 192 contrôles d'un paquet exact. Aucun calcul massif, aucun script original Wang exécuté, aucune compilation Lean.

Rapport : `research/REVIEW_39B_HERCHER_WANG.md`. Tests et provenance : `research/review39b/`.

PR brouillon de revue uniquement, aucune fusion demandée.
