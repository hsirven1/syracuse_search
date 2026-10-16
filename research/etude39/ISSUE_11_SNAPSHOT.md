# Étude 39 : état des contraintes diophantiennes sur les cycles non triviaux

**Nature : premier audit ciblé de nouveauté, distinct de la recherche de descentes/parités des études 31–38.** Ne pas commencer par des calculs massifs ou par un nouveau théorème inventé.

## Sources primaires indispensables
1. Christian Hercher (2023), *There are no Collatz m-Cycles with m ≤ 91*, Journal of Integer Sequences 26, Article 23.3.5 : https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html ; PDF sur la même page.
2. **Corrigendum daté du 14 juin 2026**, qui reconnaît explicitement une erreur dans la dérivation du théorème 21 et donne un argument correctif : https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf . L'auteur remercie Xinjun Wang d'avoir signalé l'erreur.
3. Simons et de Weger (2005), *Theoretical and computational bounds for m-cycles of the 3n+1 problem*, Acta Arithmetica 117, 51–70 : https://doi.org/10.4064/aa117-1-3.
4. Xinjun Wang (juin 2026), *A Corrected Suffix-Balanced Global-Minimum Certificate for Excluding Collatz m-Cycles for m ≤ 94*, prépublication **non expertisée**, Zenodo DOI https://doi.org/10.5281/zenodo.20603589 et ResearchGate https://www.researchgate.net/publication/406466331_A_Corrected_Suffix-Balanced_Global-Minimum_Certificate_for_Excluding_Collatz_m-Cycles_for_m_94 . Elle **revendique** les exclusions m=92,93,94 via un lemme de blocs suffix-balanced. Vérifier le texte/version, les hypothèses, les corrections et les calculs exacts avant de créditer le résultat.
5. Vérification exhaustive de l'orbite jusqu'à environ 2^71, souvent invoquée dans ces bornes : en vérifier indépendamment la source et le statut avant de s'en servir comme théorème.

## Une seule mission
**Arbitrer rigoureusement le maillon suffix-balanced** invoqué par Wang et sa portée par rapport au corrigendum Hercher. Reconstruire les quantificateurs exacts des lemmes de blocs et de l'exclusion m≤94 ; chercher au moins un contre-exemple exact à une version affaiblie ou abusive ; déterminer si une contribution additionnelle réalisable existe.

Les contraintes :
- distinguer m = nombre de minima locaux, K = nombre de termes impairs, j = pas raccourcis, et toutes les horloges ;
- ne jamais attribuer une preuve de l'absence de cycles sans hypothèses complètes ;
- aucun m=95 exploratoire sans justification structurale issue de l'audit ;
- comparer à l'audit `audit_collatz/RAPPORT.md` de notre dépôt et aux travaux déjà connus ;
- vérifier la robustesse mathématique des hypothèses (convexité, passage au maximum, gestion de la cyclicité, marges strictes, constantes log / approximations rationnelles), avec au plus une petite suite de contrôles exacts reproductibles ;
- identifier **au maximum un lemme précis** dont la preuve ou la correction constitue réellement un apport non déjà publié. En l'absence d'un tel lemme, **ARRÊT** et ne pas rebaptiser les bornes classiques en nouveauté ;
- présenter séparément ce qui est PROUVÉ dans une source publiée, PRÉPUBLIÉ, RELU/TESTÉ, CONDITIONNEL et NON VÉRIFIÉ ;
- si source inaccessible, rechercher une version auteur/publique ou expliquer le blocage, sans demander à l'utilisateur de télécharger un PDF.

## Livraison
Rapport contradictoire avec équations exactes, références primaires, hypothèses, contre-exemples s'il y en a, tests réellement exécutés et verdict **POURSUIVRE** ou **ARRÊT**, sur une branche de `hsirven1/syracuse_search` avec **PR brouillon**, sans merge. Si l'API Codex retourne HTTP 403, pousser la branche et donner le lien comparateur; l'assistant ChatGPT pourra ouvrir la PR par son GitHub connecté.

**Fin de tâche : exactement une prochaine action concrète**, sans courriel ni décision manuelle.
