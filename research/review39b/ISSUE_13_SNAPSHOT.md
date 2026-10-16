## Mission unique : arbitrer un résultat existant, pas fabriquer une étude 40

**Contexte :** [étude 39, PR #12](https://github.com/hsirven1/syracuse_search/pull/12), rapport `research/ETUDE_39_RAPPORT.md`. La version 2023 de Hercher contient une dérivation erronée ; un corrigendum officiel de juin 2026 **corrige explicitement cette étape**. Un manuscrit plus récent de Wang revendique l'exclusion des cycles jusqu'à **m≤95**, plus fort que la prépublication m≤94 examinée jusque-là. L'exclusion m≤95 est **NON VÉRIFIÉE**.

**LIRE D'ABORD** `research/etude39/PRIMARY_SOURCE_FOLLOWUP.md` (complément mathématique avec formules exactes et sources).
Sources :
- Corrigendum Hercher, officiel 2 p. : https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf
- Répertoire officiel contenant `corrigendum.tex` : https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/
- Wang, *Non-existence of Collatz m-cycles for m≤95*, texte intégral indexé : https://www.researchgate.net/publication/408180567_NON-EXISTENCE_OF_COLLATZ_m-CYCLES_FOR_m_95
- DOI de dépôt annoncé : https://doi.org/10.5281/zenodo.21017296

### Questions précises, dans cet ordre

1. **Hercher corrigé.** Reconstruis exactement le domaine de la maximisation convexe `S(x)=Σ3/(2^x_i−1)` sur le polyèdre `x_i≥1, x_(i+1)≤δ x_i, Σx_i≥(h/m)K`, avec contrainte de raccord cyclique. Le polyèdre peut être non borné : prouve, avec les hypothèses correctes, l'atteinte d'un maximum et la réduction aux sommets, ou exhibe un contre-exemple rigoureux. Vérifie l'argument d'activité des contraintes et la progression géométrique `(v,δv,...)`. **Ne pas conclure que le corrigendum est erroné simplement parce que le polyèdre est non borné.**
2. **Wang m≤95.** Reconstruis indépendamment les lemmes 5–7 (sélection suffix-balanced avec rotation libre, application à chaque suffixe, indices et bornes) et leur utilisation dans le bootstrap des lemmes 11–13. Cherche prioritairement une erreur d'ancrage au minimum global, de quantificateurs ou de passage de la rotation libre au certificat ancré.
3. **Certificat fini m=95.** Localise les artefacts/scripts originaux supposés certifier `S_5=∅` et la preuve de l'exhaustivité des branches. **Sans artefact accessible, conclure NON VÉRIFIABLE**, et ne pas reproduire un calcul géant ou annoncer l'exclusion. Tester au maximum une petite sous-instance exacte pour chercher un contre-exemple de correction des filtres.
4. **Entrées externes.** Vérifie spécifiquement l'affirmation `X=2^71` contre source indépendante et le statut éditorial : la maquette de Wang affiche encore `#Axx INTEGERS 26 (2026)` et des dates Received/Accepted/Published vides. **Ne pas présenter ce manuscrit comme publié dans INTEGERS.**
5. **Arrêt strict.** Une fois ces 4 points contrôlés, conclure parmi : REFUTÉ, CONDITIONNEL, VÉRIFIÉ (preuves + artefacts) ou NON VÉRIFIABLE. N'accepter au maximum qu'un petit lemme corrigé avec preuve et antériorité contrôlée. Si rien de scientifiquement nouveau : **ARRÊT**.

Aucun calcul massif, aucune nouvelle compilation Lean, pas de m=96. Garde intacts les anciens rapports ; publie une revue distincte et des tests compacts sur une branche, PR brouillon si possible, sans merge. Le réseau Codex a déjà renvoyé 403 sur certains domaines : pars de la note primaire nouvellement publiée, cite précisément les hypothèses que tu n'as pu relire, et ne transforme pas la note en source primaire indépendante.

Rends un verdict rigoureux et **exactement une prochaine action exécutable** pour le demandeur (pas de téléchargement manuel ni de courriel).
