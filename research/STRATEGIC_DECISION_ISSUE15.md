# Portique de nouveauté — décision stratégique après les études 31–39

**STOP — PAUSE DE RECHERCHE DIRECTE. Zéro direction retenue, zéro nouveau lemme proposé.**

Décision pour [l'issue #15](https://github.com/hsirven1/syracuse_search/issues/15).
Ce mémo ne constitue ni une étude 40, ni une preuve que toute recherche sur
Syracuse serait vaine. Dans le dossier et les sources effectivement accessibles,
aucun petit objectif ne réunit actuellement antériorité contrôlée, plausibilité
mathématique et mécanisme de preuve distinct de nos méthodes déjà écartées.
Une contribution d'outillage peut être utile sans prétention de nouveauté scientifique.

## 1. Base documentaire et réserves

Les branches non fusionnées ont été récupérées par leurs références de PR,
et pas assimilées à `main` :

| PR | Commit de tête examiné | Pièces et décision |
|---|---|---|
| [#6](https://github.com/hsirven1/syracuse_search/pull/6) | `0f28b4d5415e041ac738e0714dc7377756a16526` | Candidat KL A–E ; hypothèses de l'opérateur et ambition de stricte croissance |
| [#7](https://github.com/hsirven1/syracuse_search/pull/7) | `191ce7e2476143f80962db5aaad15607ba036092` | Revue contradictoire, correction du quantificateur B, comparaison primaire rapportée et statut de la priorité |
| [#8](https://github.com/hsirven1/syracuse_search/pull/8) | `0df896e5526acdcf48a5a65b0c2cfc261809ef99` | Décision d'abandon du projet de nouveauté, avec réserves sur le jugement historique complet |
| [#10](https://github.com/hsirven1/syracuse_search/pull/10) | `bf071625245d3a70958fdcb41b87e3d7a28fb7ae` | Étude 38 **et** `etude38/PRIMARY_SOURCE_REVIEW.md`, complément primaire Rozier–Terracol v5 |
| [#12](https://github.com/hsirven1/syracuse_search/pull/12) | `c2b11a63e2db0a322c36e84bfc861aa4c546adc7` | Étude 39 **et** `etude39/PRIMARY_SOURCE_FOLLOWUP.md` : corrigendum et manuscrit Wang ≤95 signalés |
| [#14](https://github.com/hsirven1/syracuse_search/pull/14) | `767d4af6c245230f2f5f640993bd808f4f9e622b` | Revue 39B : modèle convexe et suffixes justifiés sous hypothèses ; certificat S₅ et exclusion ≤95 non vérifiables |

Base du présent mémo : `main` à `f0e1ede43d94ab4d4756223cdccef51e3aa30c7d`.
Les rapports historiques et leurs tests ne sont pas modifiés.

**31–35 :** leurs rapports primaires complets ne sont pas disponibles dans
le dossier examiné. L'archive 36 et sa comparaison évoquent les expériences
32–35 ; notamment, le test de complexité 35 manquait. Aucun contenu de 31
ni théorème complet de 32–35 n'est reconstruit par supposition.
Ce manque limite le bilan historique, pas le premier triage des méthodes.

Les lectures primaires annoncées dans les compléments des PR restent les
lectures de leurs rédacteurs. Les consulter ici ne constitue pas une nouvelle
vérification indépendante des PDF. C'est particulièrement important pour
l'incohérence de statut KL 1995/2003 et pour Wang.

## 2. Matrice de redondance : source → portée → lacune

| Méthode et dossier | Couverture existante | Hypothèses / limite précise | Décision |
|---|---|---|---|
| Parités, cylindres finis ; audit principal | Terras/Everett ; bijection parités↔classes modulo 2^j ; `WordCongruence.realizes_iff_dvd` | Tout mot fini est réalisable par une classe. Ce fait ne fournit ni réalisation entière d'un mot infini ni descente universelle | Ne pas rechercher une « nouvelle identité » de codage |
| Horizons adaptatifs ; `REORIENTATION.md`, `EXACT_STOPPING_TIME_BASELINE.md` | Mersenne donne des ascensions arbitrairement longues ; familles infinies à temps de première descente prescrit par un cylindre classique | `∀n>1, ∃t: U^t(n)<n` équivaut à Syracuse. `∀m, ∃∞n:τ(n)=m` ne couvre pas tous les n | Écarter ces deux faux petits objectifs |
| Fenêtres et poids finis ; audit Lean ciblé | `NoGo.no_uniform_descent_bound`, `no_finite_certificate` | Horizon uniformément borné, poids rationnels positifs encadrés et contraction uniforme ; ne condamne pas tous les arguments finiment décrits | Ne pas relancer un crible local de même forme |
| Couverture conditionnelle ; étude 37 | Codage classique, grandes déviations binomiales ; contre-exemple tout impair à C37 | Pour un préfixe de longueur ≈k/3, la non-descente conditionnelle peut tendre vers 1 ; densité moyenne et contrôle de chaque cylindre diffèrent | Uniformité C37 réfutée ; frontière classique θc=2log₃2−1 non nouvelle |
| Contraintes 2-/3-adiques ; étude 36 | Identité affine, congruences de suffixes, `shadow_modEq`, `dcoef_add` ; traduction des horloges auditée | Le reste ternaire déjà déterminé par le suffixe n'est pas une contrainte indépendante ; le plafond de hauteur testé était redondant avec la classe initiale | Ne pas multiplier ces filtres sans donnée nouvelle démontrée |
| Complexité symbolique ; audit / expériences évoquées 35–36 | Exclusions mécaniques/Sturmiennes et planchers de complexité dans le dépôt Lean | Théorèmes portant sur l'itinéraire infini ; complexité d'un préfixe ne donne pas une enveloppe globale. Aucun contrôle universel de l'orbite n'en résulte | Données 35 incomplètes ; aucune direction originale établie |
| Correction–résidu et segments paradoxaux ; PR #10 | Critère conjoint exact et décodage dans le dépôt Lean ; Rozier–Terracol v5, définition 1.1, théorème 2.4, théorème 4.2 et annexe C selon le complément primaire | Maximalité de la correction et borne harmonique sont déjà couvertes. Un segment paradoxal peut être descendu auparavant. Finitude globale : cible majeure, pas petit lemme | ARRÊT ; pas de nouvelle campagne de recensement |
| LP KL ; PR #6–8 | Applegate–Lagarias 1995 §4 annonce déjà la stricte croissance et le mécanisme relèvement/projection ; KL 2003 la dit pourtant ouverte selon la lecture rapportée | B exige une existence de certificat, pas une inégalité pour tout vecteur. Les lemmes Lean génériques ne sont pas une formalisation complète du théorème original | Geler la revendication de nouveauté ; une preuve nouvelle d'une ancienne assertion reste possible mais non établie ici |
| Cycles ; PR #12 et #14 | Simons–de Weger ; Hercher et corrigendum ; lemmes 5–7 de Wang transcrits ; optimisation convexe cyclique justifiée dans 39B | Nombre de minima m ≠ nombre d'impairs K ≠ temps j. Un bloc ouvert ne se ferme pas automatiquement. S₅, bootstrap complet et X=2^71 non vérifiés | Vérification d'un résultat existant, pas projet de nouveau record 96 |
| Densités ; étude 37, Tao, préprint Inselmann | Première descente presque partout en densité naturelle ; minimum presque borné en densité logarithmique ; minimum n^ε en densité naturelle annoncé par Inselmann | Naturelle/logarithmique, descendre/atteindre 1, et presque tous/tous sont des conclusions différentes | Un changement de quantificateur ou de mesure ne constitue pas un petit gain acquis |

Les noms Lean renvoient aux déclarations et axiomes de l'audit initial,
pas à une compilation nouvelle. Le dépôt externe annonce aussi des certificats
KL lourds non reconstruits intégralement : ils ne deviennent pas des résultats
indépendamment vérifiés par leur simple présence dans cette matrice.

### Deux mises à jour à conserver

- Le complément de la PR #10 attribue correctement la correction extrémale à
  **Rozier–Terracol v5, théorème 2.4**, pas au « théorème 2.2 » de la vieille
  source secondaire. La définition 2.2 introduit l'ordre partiel. Il rapporte
  la même borne harmonique et les cinq départs de longueur huit ; aucune
  nouveauté ne subsiste dans ce sous-dossier.
- La PR #14 ne réfute ni le corrigendum Hercher ni Wang. Elle prouve la
  maximisation sur un modèle **cyclique fermé** avec B>G_h et les lemmes
  suffixes **transcrits**, et isole les obligations de raccord et de certificat.
  L'absence d'artefacts n'est ni une preuve d'erreur, ni une invitation à refaire
  un grand calcul.

## 3. Recherche de questions auxiliaires : résultats et limites

### Sources réellement consultées cette fois

En plus du dossier ci-dessus, lecture de sources du dépôt externe figé
[`msharpe248/collatz`](https://github.com/msharpe248/collatz/tree/ec8174b567d5cab4960024782210b5f5db02bd3a) :
`paper/README.md`, `paper/odd_histories_and_collisions.md`,
`paper/sibling_correction.md`, `paper/ideal_tracking_barrier.md`,
`paper/residue_correction.md`, et début de `paper/orbit_summability.tex`.
Ce sont des textes d'auteur **non expertisés**, pas des publications certifiées.

Copie publique récupérée de
[`gotrevor/tao-collatz`](https://github.com/gotrevor/tao-collatz/tree/95a7172bb253c849404ab1c687602e0ce6b5469a),
commit **`95a7172bb253c849404ab1c687602e0ce6b5469a`**. Les pièces lues
sont `README.md`, `papers/tao-2019-almost-all-orbits.md` et une partie de
`papers/literature-review.md`. Elles donnent notamment comme piste le passage
de densité logarithmique à naturelle (renvoi à Tao, remarque 1.16).
**Ces notes sont secondaires** et leur statut de formalisation n'est pas audité.
Le PDF Tao annoncé par le dépôt n'est pas versionné dans cette copie.

Accès primaires tentés pendant cette mission, tous refusés par le tunnel HTTP 403 :

- [Tao, billet auteur](https://terrytao.wordpress.com/2019/09/10/almost-all-collatz-orbits-attain-almost-bounded-values/) ;
- [Tao, publication](https://doi.org/10.1017/fmp.2022.8) et [arXiv v5](https://arxiv.org/pdf/1909.03562v5) ;
- [Inselmann, arXiv:2402.03276](https://arxiv.org/abs/2402.03276) ;
- Rozier–Terracol, [v4](https://arxiv.org/html/2502.00948v4) puis
  [v5](https://arxiv.org/html/2502.00948v5), celle signalée par le complément.

Il serait donc excessif de déclarer ici « liste des problèmes encore ouverts
certifiée à octobre 2026 ». La recherche primaire est **partielle et bloquée**.
Nous avons des pistes bibliographiques explicites, pas un état de l'art complet.
Cette limite interdit un GO fondé sur une prétendue absence de travaux antérieurs.

### Tri 1 : une cible probabiliste réelle, mais aucun petit passage validé

Pour fixer les quantificateurs, poser `M(n)=min_(t≥0) T^t(n)`.
Une cible plus forte que le résultat de Tao serait :

\[
 \forall f:\mathbb N\to\mathbb R_{>0},\quad f(n)\to\infty
 \ \Longrightarrow\
 \lim_{X\to\infty}\frac1{\lfloor X\rfloor}
       \#\{1\le n\le X:M(n)\ge f(n)\}=0.
\]

C'est une cible de **densité naturelle**, pas une affirmation pour chaque n,
et elle n'est pas une reformulation logique de Syracuse. La note secondaire
renvoie explicitement à Tao pour l'envisager ; l'antériorité et le statut
actuel de cette version exacte restent non vérifiés à la source ici.
Le préprint Inselmann signalé dans notre bilan concerne n^ε, ce qui ne suffit
pas à conclure pour toute fonction divergente. Nous ne lui attribuons pas
une exclusion des exceptions ni une preuve de cette cible.

Cette cible entière n'est **pas un petit lemme**. Aucun mécanisme nouveau de
transport de mesure entre échelles n'a été trouvé. La remplacer par une
indépendance uniforme de toutes les classes conditionnelles réintroduirait
C37, déjà réfuté. Un test contradictoire obligatoire pour tout futur petit
énoncé de ce type serait de fixer un préfixe tout impair de longueur ceil(k/3)
et de vérifier si le quantificateur exige une proportion de non-descente
qui tend vers zéro : cela le réfuterait avant toute expérience.
Les Mersenne n'interdisent pas un théorème « presque partout » ; ils interdisent
seulement d'utiliser abusivement une borne uniforme de temps de descente.

**Décision : non retenue.** Nous ne transformons pas cette cible majeure en
mini-lemme artificiel. Aucun premier test informatique ne remplace l'étape
manquante de preuve et d'antériorité.

### Tri 2 : restrictions conjointes sur les impairs, fausse ouverture et plafond

Une ancienne note `odd_histories_and_collisions.md` présentait comme ouverte
l'amélioration pondérée issue des paires interdites. La note ultérieure
`sibling_correction.md` fournit déjà, pour tout ensemble fini S d'impairs >5,
non divisibles par 3 et sans paire n,4n+1,

\[
 \left[\prod_{x\in S}(1+1/(3x))\right]^{10}\le2|S|+1.
\]

Il ne faut donc pas proposer cette amélioration comme problème ouvert.
De même, `ideal_tracking_barrier.md` conserve un ancien « bounded-correction
case remains open », alors que `orbit_summability.tex` annonce ensuite que
toute orbite positive non bornée a une correction idéale bornée. Il faut lire
le suivi chronologique avant de transformer un ancien manque en objectif.
Ces affirmations du dépôt ne sont pas nouvellement compilées ici.

Un renforcement naturel **que nous rejetons**, pas une conjecture retenue,
serait l'existence d'une constante C telle que, pour tous ces S,

\[
 \left[\prod_{x\in S}(1+1/(3x))\right]^{11}\le C(2|S|+1).
\]

Il est faux pour une famille infinie explicite : soit S_N l'ensemble des
entiers 5<x≤N de résidus
`1,7,11,13,17,19,23 (mod 24)`. Ils sont impairs et premiers à 3. Si n≡1 mod6,
son enfant 4n+1 vaut 5 mod24 et est exclu ; si n≡5 mod6, l'enfant est divisible
par 3. Ainsi S_N respecte exactement les hypothèses de paire interdite.

Les sommes harmoniques des sept progressions donnent

\[
 |S_N|=7N/24+O(1),\qquad
 \sum_{x\in S_N}1/x=(7/24)\log N+O(1).
\]

Comme `log(1+1/(3x))=1/(3x)+O(1/x²)`, avec erreur sommable,

\[
 \log\prod_{x\in S_N}(1+1/(3x))=(7/72)\log N+O(1).
\]

Le rapport du membre gauche élevé à 11 à `2|S_N|+1` tend donc vers l'infini,
comme une constante encadrée positivement fois `N^(5/72)`. Plus généralement,
aucun exposant >72/7 ne peut marcher avec cette seule hypothèse et un membre
droit linéaire en |S|. C'est une obstruction élémentaire, **aucune priorité
scientifique n'en est revendiquée**. Ce n'est pas un contre-exemple Collatz :
S_N est une famille d'ensembles admissibles, pas une orbite.

Passer de 10 au seuil 72/7 avec une constante multiplicative n'offre pas ici
un programme convaincant : la compression déjà donnée dans
`sibling_correction.md`, puis un classement des mêmes progressions et les
sommes harmoniques, donnent le taux de puissance correspondant. Il ne faut
pas confondre optimisation d'une constante/rang classique avec nouvelle
restriction sur les **orbites réelles**. Un gain structurel demanderait une
restriction additionnelle indépendante démontrée, que nous n'avons pas.

**Décision : non retenue.** Le premier test contradictoire, avant tout calcul,
est précisément S_N ; il exclut déjà l'ambition 11 sous les hypothèses citées.
Cette restriction concerne les orbites échappantes ; même une amélioration
valide ne réglerait pas les cycles.

## 4. Ce qui est explicitement exclu du portefeuille

- Finitude du temps de descente pour tous les n, bornitude de toutes les
  orbites ou absence de tout cycle : objectifs équivalents ou composantes
  majeures du problème, pas mini-lemmes auxiliaires.
- Nouveau mot oscillant, nouveau tableau de congruences, nouveau recensement
  paradoxal sans restriction uniforme de réalisation démontrée.
- Record m=96 à partir de Wang non vérifié ; ouvrir ce chantier avant les
  artefacts ≤95 serait un défaut de fondation, pas une réorientation.
- Nouvelle formalisation massive KL ou Tao comme recherche de priorité ; une
  validation ciblée peut être utile, mais c'est une autre contribution.
- Nouveau modèle statistique ou nouveau balayage pour « trouver une piste »
  sans énoncé réfutable et comparaison primaire préalable.

**Aucune direction n'a été retenue.** Les deux tris précédents ne sont pas
un programme à financer : l'un manque de petit mécanisme validé et de contrôle
primaire de statut ; l'autre réutilise une étape déjà résolue et rencontre un
contre-exemple analytique. Ne pas interpréter le plafond de deux directions
comme une obligation d'en inventer deux.

## 5. Vérifications réellement effectuées

- Lecture des références Git des six PR, des rapports et compléments indiqués ;
  lecture des rapports principaux sur `main` et du catalogue externe.
- Récupération Git en lecture seule du dépôt secondaire Tao et lecture des
  notes bibliographiques précisées ; pas de compilation ou validation de ses
  annonces de formalisation.
- Six tentatives d'accès aux textes primaires ci-dessus, toutes HTTP 403.
- Vérification documentaire des références de fichiers aux commits cités et
  contrôle des modifications Git : ce mémo est le seul fichier ajouté.
- Aucun test des anciennes études n'est présenté comme réexécuté. **Aucune
  suite mathématique, aucun balayage, aucun calcul massif, aucun Lean.**
  L'obstruction S_N repose sur la preuve asymptotique donnée, pas sur des données.

Le dossier mérite une conservation claire de ses résultats négatifs et des
hypothèses de ses preuves. Il ne justifie pas une revendication de nouveauté
ou une nouvelle campagne de recherche directe dans les mêmes familles.

## Publication

Le seul fichier ajouté est ce mémo, sur `strategy/issue15-research-pause`.
La branche a été poussée sur GitHub. Tentative réelle de PR brouillon :

```sh
gh pr create --repo hsirven1/syracuse_search --base main \
  --head strategy/issue15-research-pause --draft \
  --title 'Décision stratégique : STOP et pause de recherche directe après études 31–39' \
  --body-file /tmp/issue15-pr-body.md
```

Résultat : `Post "https://api.github.com/graphql": Forbidden`.
**Aucune PR créée par cet accès ; aucune fusion.**
[Comparateur GitHub](https://github.com/hsirven1/syracuse_search/compare/main...strategy/issue15-research-pause?expand=1).
`git diff --check` et le contrôle du diff indexé passent. Les rapports et tests
antérieurs ne sont pas modifiés ; la vérification des six références Git a
retourné `PASS: 6 références Git vérifiées`.

## 6. Verdict et unique action recommandée

**STOP — PAUSE DE RECHERCHE DIRECTE.** Cette décision d'allocation n'affirme
ni que tout est connu dans la littérature, ni qu'aucun lemme nouveau ne puisse
exister. Elle constate qu'aucun candidat justifié n'a passé ce portique.

Une contribution utile et honnête serait un petit vérificateur indépendant
pour des certificats **finis** de descente, avec portée déclarée, sans lancer
un générateur de preuves ou faire de nouveauté mathématique une condition de
succès. L'outil ne validerait pas automatiquement Wang ni une couverture infinie.
L'intervalle doit rester **fini** : une couverture totale par arbre fini de tous
les entiers au-dessus d'un seuil réintroduirait l'horizon uniforme déjà exclu.

**Une seule prochaine action :** lancer la tâche suivante dans l'assistant
GitHub connecté, avec ce prompt complet :

> Dans `hsirven1/syracuse_search`, prépare un petit vérificateur indépendant
> de certificats finis de descente par mots de parité, pour la fonction
> raccourcie T. Un certificat décrit un arbre binaire fini de
> cylindres couvrant un intervalle fini explicite [N₀,N₁], 3≤N₀≤N₁ ; chaque
> feuille non vide doit certifier T^j(n)<n pour les entiers de sa classe dans
> cet intervalle. Les branches omises doivent avoir une intersection vide
> avec l'intervalle, à vérifier arithmétiquement. Vérifie la
> couverture de l'arbre et la contraction à partir de l'identité affine exacte,
> puis justifie par écrit la correction du vérificateur. N'effectue aucune
> recherche de nouveaux certificats, aucun grand calcul et aucun Lean.
> Critères de succès : accepter le contrôle [3,4] (mot 0 pour 4, mot 1100
> pour 3, branches vides justifiées), rejeter un arbre avec feuille non vide manquante,
> un mot/correction falsifié et un témoin au seuil où la descente n'est pas
> stricte. Si le certificat laisse un entier de l'intervalle non certifié,
> déclarer « couverture partielle », jamais « Syracuse prouvée ». Fournis tests et PR
> brouillon, sans merge ni revendication de nouveauté scientifique.

Cette tâche est de l'ingénierie de vérification, **pas une étude 40** et pas un GO
pour la recherche mathématique directe.
