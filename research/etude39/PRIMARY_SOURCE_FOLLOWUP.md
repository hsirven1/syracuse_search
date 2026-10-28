# Complément primaire à l'étude 39 : Hercher corrigé et nouvelle revendication Wang m≤95

Date : 16 octobre 2026. **Ce complément est une lecture supplémentaire indépendante, NON un nouveau théorème et NON une validation de l'exclusion m≤95.** Le rapport original `ETUDE_39_RAPPORT.md` conserve son périmètre exact : Codex n'avait pas accès à ces textes lors de sa mission.

## 1. Corrigendum Hercher : source officielle accessible

- Journal of Integer Sequences, p. auteur : https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html
- **Corrigendum PDF officiel (2 pages, consultées toutes deux)** : https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf
- Répertoire du journal, qui expose aussi le fichier source `corrigendum.tex` : https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/

L'auteur reconnaît explicitement une erreur dans la dérivation des inégalités utilisées au bas de la page 14, théorème 21, dans la version publiée en 2023. Il propose un **nouvel argument par optimisation convexe**, et remercie Xinjun Wang d'avoir signalé le problème.

### Structure exacte de la correction, à auditer

Poser `δ=log_2 3`, `x_i=log_2(n_i+1)`. Pour un bloc de `h=m_2` minima sélectionné, la correction utilise
- `x_i≥1`,
- les relations de croissance cycliques `x_(i+1) < δ x_i` (dans la relaxation de l'optimisation, ≤),
- la somme `Σ_bloc x_i ≥ (h/m)K`,
- la fonction `S(x_1,...,x_h) = Σ_i 3/(2^(x_i)-1)`.

Le PDF avance que `S`, convexe sur `x_i>0`, atteint son maximum en un sommet du polyèdre défini par ces contraintes. Il exclut les sommets avec `x_i=1` grâce à la contrainte de somme et à la définition de `m_2`. Il en déduit que la somme et toutes les contraintes de croissance sauf une sont actives. Le sommet est donc, à rotation cyclique près, une progression géométrique
`(v,δv,...,δ^(h−1)v)` avec
`v=(h/m)K·(δ−1)/(δ^h−1)`.
Cela mène à la majoration d'une somme de termes `T(n_i)` par
`3/(2^v−1)+3(h−1)/(2^v−1)^δ`.

**Obligation non encore auditée :** le polyèdre est potentiellement non borné (la contrainte est `Σ x_i≥...`, non ≤). L'affirmation « maximum convexe atteint à un sommet » mérite une preuve de compacité efficace ou une étude des directions non bornées. Ce n'est **pas** ici la déclaration d'une nouvelle erreur ; il faut tester si la cyclicité des contraintes de croissance et la décroissance de `S` suffisent à rendre cette étape rigoureuse.

Le corrigendum corrige expressément la dérivation de 2023 ; ce constat ne certifie pas le théorème 21 corrigé ni le théorème 23 dans leur ensemble.

## 2. Wang : il existe un manuscrit ultérieur revendiquant m≤95

- **Texte intégral publiquement indexé** : https://www.researchgate.net/publication/408180567_NON-EXISTENCE_OF_COLLATZ_m-CYCLES_FOR_m_95
- DOI de dépôt **indiqué par le manuscrit** : https://doi.org/10.5281/zenodo.21017296
- La version ResearchGate indique le 29 juin 2026 comme date de dépôt de l'auteur.

Il s'agit d'une **prépublication non certifiée** : ses métadonnées affichent une maquette `#Axx INTEGERS 26 (2026)` et des champs `Received/Revised/Accepted/Published` vides. **Ne pas l'appeler article accepté ou publié.** Le manuscrit revendique l'exclusion de tous les cycles non triviaux ayant au plus **95 minima**, sous les entrées externes `X=2^71` (vérification exhaustive) et des bornes de Simons–de Weger. Le statut indépendant de ces prémisses doit être audité. Cette revendication, si correcte, serait plus forte que le m≤94 de la prépublication précédente, mais aucune des deux n'est certifiée ici.

### Énoncés à reconstruire/attaquer

- **Lemme 6 (bloc suffix-balanced)** : pour tout `1≤s≤m`, il existe un bloc de `s` minima consécutifs dont **chaque suffixe de longueur t** satisfait `Σ_suffixe k_i ≥ tK/m` pour `1≤t≤s`. Preuve proposée : centrer les `k_i` par `K/m`, prendre l'indice de somme partielle cumulée maximale, considérer le bloc de longueur `s` qui s'y termine (avec bouclage cyclique). Ce lemme concerne une **rotation libre**, pas l'ancrage au minimum global.
- **Lemme 5 (croissance)** : si `K_(r,s)=Σ_(j=0..s−1) k_(r+j)`, alors `n_r+1 ≥ 2^[K_(r,s)(δ−1)/(δ^s−1)]`. Attention : `n_r+1` veut ici dire le nombre `n_r` **plus 1**, et non le minimum d'indice r+1. L'emboîtement des indices est critique.
- **Lemme 7 (reste de bloc)** : pour `V_t=(tK/m)(δ−1)/(δ^t−1)`, majorer la contribution du bloc par `Σ_(t=1..s) 3/(2^V_t−1)`, et ajouter une majoration `ρ` des `m−s` minima exclus.
- **Lemme 11 et itération du lemme 12** : l'argument utilise des tests diophantiens de fractions continues et donne des bornes croissantes de `K` jusqu'à `K_0=205632218873398596256`, avec `m_* =95`, `s_j=(47,67,77,82,86,88)`. Le manuscrit revendique des calculs exacts, **non reproduits ici**.
- **Exclusion finie de m=95** : après avoir fixé le minimum global `n_1=n_min`, l'auteur revendique un certificat à profondeur 5 pour l'intervalle `X≤n_min≤24X`, de type `S_5=∅`, en filtrant puissances de 2 et résidus de l'unique paramètre initial. Le manuscrit dit que l'exclusion relève tous les `k_1` de 1 à 75, puis les `k_i,ℓ_i` dépendants. Les annexes ou scripts originaux **doivent** être trouvés et utilisés pour vérifier l'exhaustivité, plutôt que de conclure à partir de l'affirmation `S_5=∅`.

### Point de vigilance logique

Le lemme 6 n'affirme pas qu'on peut imposer librement que le bloc suffix-balanced commence au minimum global. Le manuscrit emploie une **sélection libre** pour les étapes de minorant de `K`, puis un **ancrage au minimum global** dans les certificats finis. Il faut vérifier où les deux sont combinés et que la sélection du bloc n'est pas réutilisée après ancrage arbitraire. Le contre-exemple rationnel `k=(3,1)` de notre étude 39 ne réfute pas le lemme 6 avec rotation libre.

### Ce qui est actuellement non établi

- Validité complète de l'argument polyédral de Hercher corrigé ;
- validité mathématique et calculatoire des lemmes 11–13 de Wang ;
- couverture exhaustive du certificat à profondeur cinq `S_5=∅` ;
- source et périmètre exacts de la prémisse `X=2^71` ;
- antériorité, priorité, et statut éditorial réel de Wang m≤95 ;
- absence de cycles avec m≤95.

**Recommandation : un audit contradictoire unique et borné des étapes de transition entre les lemmes suffix-balanced et le certificat `S_5=∅`.** Pas d'annonce de nouveau théorème, pas de calcul géant tant qu'il n'existe pas d'artefact de certificats reproductible, pas de nouvel épisode « étude 40 » artificiel.

Sources publiques vérifiées : la page officielle Hercher et son PDF de corrigendum, et le texte intégral indexé du manuscrit de Wang (ResearchGate). Les éditions Web et PDF peuvent avoir des mises en page différentes ; pointer les numéros de lemmes et sections plutôt que des seules pages.
