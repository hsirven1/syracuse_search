Refs #11.

Premier audit ciblé des cycles : verdict de recherche **ARRÊT**, zéro lemme nouveau retenu. **Audit du lemme exact suffix-balanced de Wang incomplet ; exclusion m≤94 NON VÉRIFIÉE.** Ne pas présenter ce travail comme une réfutation de Wang ou du corrigendum Hercher.

Le rapport identifie deux défauts dans la dérivation du théorème 21 du préprint Hercher v3 effectivement obtenu sur un miroir GitHub. Il distingue cette version du corrigendum de juin 2026 inaccessible, les résultats 2005/2010 de Simons–de Weger et la formalisation conditionnelle jusqu'à m≤82. La couverture annoncée à 2^71 n'est pas utilisée comme prémisse acquise.

Contrôles exacts : `python3 research/etude39/exact_checks.py` passe sur 1 092 listes cycliques et 6 015 fenêtres, avec contre-exemples à l'ancrage arbitraire, fermeture rationnelle, inversion et convexité. Encadrement rationnel des logarithmes. Aucun test du lemme Wang sans son texte, aucun calcul massif ni compilation Lean.

Rapport : `research/ETUDE_39_RAPPORT.md`. Tests, résultats, sources et provenance : `research/etude39/`.

PR brouillon de revue uniquement ; ne pas fusionner.
