# Étude 39 — audit contradictoire des cycles et du maillon suffix-balanced

**Verdict de recherche : ARRÊT. Statut de l'exclusion de Wang m≤94 : NON VÉRIFIÉ.**

L'audit prioritaire du lemme exact de Wang reste **incomplet** : ni son manuscrit
ni le corrigendum Hercher n'ont pu être obtenus. Nous ne créditons donc pas
l'exclusion annoncée et ne la déclarons pas réfutée. Aucun lemme nouveau n'est
retenu. Les contre-exemples ci-dessous visent des versions explicitement
abusives, **pas un énoncé inventé et attribué à Wang**.

Mission : [issue #11](https://github.com/hsirven1/syracuse_search/issues/11), dont
le texte est conservé dans [le snapshot](etude39/ISSUE_11_SNAPSHOT.md).
Branche : `research/etude39-cycle-audit`, base `main`, commit
`f0e1ede43d94ab4d4756223cdccef51e3aa30c7d`. Aucun essai m=95.

## 1. Sources : comparaison, versions et niveau de vérification

| Source | Résultat ou affirmation | Statut dans cet audit |
|---|---|---|
| Simons–de Weger, *Theoretical and computational bounds for m-cycles of the 3n+1 problem*, Acta Arith. 117 (2005), 51–70, [DOI](https://doi.org/10.4064/aa117-1-3) | Contraintes diophantiennes et calculs sur m-cycles | Article publié ; original inaccessible ici. Hercher v3 p.2 lui attribue **m≥68**, puis p.3 distingue la mise à jour 2010 donnant **m≥76**. Ces chiffres sont rapportés par Hercher, pas réaudités dans l'original ; ne pas confondre 2005 et 2010, ni ≥68 et >68 |
| Hercher (2023), JIS 26, 23.3.5, [page éditeur](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.html) | Titre : aucun m-cycle avec m≤91 ; théorème 23 | Article publié. Une **copie du préprint arXiv v3 du 4 avril 2023** a été obtenue via GitHub et ses pp.2–3,12–15 relues. L'étape finale du théorème 21 p.14 est invalide ; cela ne réfute pas la conclusion arithmétique ni une correction ultérieure |
| [Corrigendum Hercher](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf), annoncé au 14 juin 2026 | Selon l'issue, reconnaît l'erreur du théorème 21, propose une correction, remercie Xinjun Wang | **NON VÉRIFIÉ** : date, texte correctif et rétablissement de la borne ne sont pas attestés directement ici |
| Xinjun Wang, *A Corrected Suffix-Balanced Global-Minimum Certificate for Excluding Collatz m-Cycles for m≤94*, [Zenodo](https://doi.org/10.5281/zenodo.20603589), [ResearchGate](https://www.researchgate.net/publication/406466331_A_Corrected_Suffix-Balanced_Global-Minimum_Certificate_for_Excluding_Collatz_m-Cycles_for_m_94) | Exclusions 92,93,94 et lemme de blocs, selon l'issue | **PRÉPUBLICATION annoncée, NON VÉRIFIÉE** : aucune version, équation, constante ou quantification exacte obtenue. Aucun théorème de Wang n'a été testé |
| [PhilNorfleet/Hercher2023_lean](https://github.com/PhilNorfleet/Hercher2023_lean/tree/2f9d1a2633cdc0c7f9238c0fc81eca054fd6afec) | Déclare une formalisation jusqu'à m≤82 avec deux hypothèses externes ; critique le théorème 21 original | Dépôt et sources relus statiquement, **pas compilés**. Ni équivalent du résultat publié corrigé, ni preuve indépendante de m≤91/94 |
| [Barina, dépôt auteur](https://github.com/xbarin02/collatz) | Code de vérification ; références 2021 et *Improved verification limit…*, J. Supercomput. 81,810 (2025) | Page auteur accessible. La couverture jusqu'à environ **2^71**, son état d'achèvement et ses certificats ne sont **pas vérifiés** ici ; site du calcul inaccessible |

Le PDF consulté provient du fichier `Hercher2023.pdf` du dépôt PhilNorfleet,
commit `2f9d1a2633cdc0c7f9238c0fc81eca054fd6afec` (4 août 2026).
Son en-tête identifie arXiv:2201.00406v3 ; on ne l'assimile pas à une version
post-corrigendum. Le contrôle de son empreinte fixe le fichier lu, sans
prétendre l'avoir authentifié contre le serveur éditeur.

La note `SUMMARY.md` du dépôt Lean contient elle-même une attribution
« m≤68 » là où le PDF Hercher parle de « m≥68 » : nous retenons le texte
précis du PDF comme compte rendu, sans résoudre ce décalage par conjecture.
Le README d'août 2026 ne discute pas le corrigendum de juin : son diagnostic
ne prouve donc pas que ce corrigendum échoue.

### Accès et recherche de copies

Les requêtes éditeur HTML/PDF, corrigendum, DOI, Zenodo (page et API),
ResearchGate ont échoué avec un tunnel HTTP 403. Un essai Zenodo hors sandbox
a également renvoyé 403. La copie auteur de la mise à jour Simons–de Weger
2010, citée dans Hercher p.21, et arXiv:2201.00406 ont aussi échoué.
La recherche GitHub de dépôts contenant « Suffix-Balanced » n'a donné aucun
résultat ; cela n'établit pas l'absence de miroir. La copie Hercher a été
trouvée via le catalogue du dépôt `msharpe248/collatz` déjà audité.

Les domaines nécessaires ont été enregistrés dans un brouillon de configuration
cloud en préservant la liste existante. Ce brouillon exige une publication et
n'a pas établi d'ouverture réseau effective. Aucune clé n'a été demandée.
Les tentatives et leurs limites sont dans [source_access.json](etude39/source_access.json).

## 2. Horloges et contraintes exactes de cycle

Employer `C(n)=n/2` si pair, `(3n+1)/2` sinon, comme Hercher, Definition 1.
Ce C est notre application raccourcie T ; **ce n'est pas 3n+1 non raccourci**.

- m : nombre de minima locaux distincts sur une période primitive.
- k_i≥1 : nombre de pas impairs consécutifs après le minimum n_i.
- l_i≥1 : nombre de pas pairs consécutifs qui suivent, jusqu'à n_(i+1).
- K=sum k_i : nombre de termes/pas impairs ; L=sum l_i : pas pairs.
- j=K+L : période en pas raccourcis. Une période répétée artificiellement
  ne doit pas augmenter m dans une borne sur une période primitive.

Les blocs satisfont exactement

\[
 2^{k_i+l_i}n_{i+1}=3^{k_i}(n_i+1)-2^{k_i},\qquad n_{m+1}=n_1.
\]

En composant le mot de parités w de longueur j et à K impairs :

\[
 (2^j-3^K)n_1=D(w),\qquad
 D(w)=\sum_{t:b_t=1}2^t3^{\sum_{s>t}b_s}.
\]

Comme D>0, un cycle positif impose `2^j>3^K`. La divisibilité, la réalisation
réelle du mot, la positivité, l'intégralité et les inégalités de minima sont
indispensables. Un retour affine rationnel ne constitue pas un cycle Collatz.

Avec δ=log(3)/log(2) et R(n_i) la somme des inverses des k_i états impairs
successifs (Hercher note cette fonction **T**, à ne pas confondre avec la map),
le télescopage fournit la contrainte classique

\[
 0<j\log2-K\log3
 =\sum_{x\text{ impair du cycle}}\log(1+1/(3x))
 <\frac13\sum_iR(n_i),
\]

soit `δ < j/K < δ + sum R(n_i)/(3K log2)`.
L'approximation diophantienne porte sur j/K, non sur m/K.
Toute valeur X utilisée pour borner les minima doit venir d'une couverture
exhaustive justifiée ; nous n'utilisons pas 2^71 comme prémisse acquise.

Notre [audit antérieur](../audit_collatz/RAPPORT.md) vérifiait des identités
finies, des limites de fenêtres et des congruences ; il ne certifiait ni ces
bornes mondiales sur les cycles, ni l'exécution d'une vérification à 2^71.

## 3. Défaut effectivement relu : Hercher v3, théorème 21, p.14

Le pigeonhole cyclique fournit **un** bloc de h=m2 minima avec
`sum k_i >= hK/m`. Les estimations `k_(i+ell) <= δ^ell log(n_i+1)/log2`
conduisent à une borne sur le **premier** minimum du bloc :

\[
 n_i\ge2^v-1,\qquad v=\frac{hK}{m}\frac{\delta-1}{\delta^h-1}.
\]

Cela ne fournit pas la même borne à chaque minimum ultérieur.
Le PDF écrit ensuite (extrait conservé avec sa provenance)

\[
 n_{i+\ell}<n_i^{\delta^\ell}\le n_i^\delta,
 \quad\text{puis}\quad R(n_{i+\ell})<3/(2^v-1)^\delta.
\]

Deux défauts indépendants :

1. Pour n_i>1, δ>1 et ell≥2, **δ^ell>δ**, donc l'inégalité entre puissances
   est dans le mauvais sens. Avec n_i=2, `2^δ=3` mais
   `2^(δ²)=3^δ>3`. Aucun arrondi numérique n'est nécessaire.
2. Même une borne supérieure correcte sur n_(i+ell) ne majorerait pas son
   inverse. `R(x)<3/x` exige une **borne inférieure** sur x pour donner une
   nouvelle majoration. Le passage affiché ne l'apporte pas.

Ceci établit une lacune dans cette dérivation de 2023. Cela ne suffit ni à
réfuter le théorème 23, ni à réfuter le corrigendum non lu. La formalisation
consultée remplace la queue contestée par `3(h−1)/X0` et son théorème principal
`no_m_cycle_le_82` prend explicitement `hbound` et `hSdW` comme hypothèses
externes : une fermeture d'axiomes standard ne prouverait pas ces prémisses.

## 4. Suffix-balanced : ce qui peut et ne peut pas être arbitré

**Nous ne disposons pas de la définition exacte de Wang.** Impossible donc
de reconstruire honnêtement ses quantificateurs, de vérifier son optimisation
convexe ou de reproduire les marges numériques pour 92–94. Le titre du texte
ne remplace pas son énoncé. Le lemme suivant sert seulement de témoin classique
pour auditer un possible abus ; ce n'est pas un candidat nouveau.

### Rotation libre versus ancrage imposé : distinction démontrée

Pour une liste réelle a=(a_0,…,a_(m−1)), de moyenne μ, il existe une rotation
pour laquelle **tous les suffixes** de longueur h ont somme ≥hμ.
Preuve classique : centrer les termes par μ, puis couper après un maximum des
sommes partielles S_0,…,S_(m−1). Les préfixes de cette rotation ont somme ≤0,
y compris après franchissement du raccord cyclique puisque la somme totale
vaut zéro. Chaque suffixe a donc somme ≥0. Les égalités sont permises.

**On ne peut pas imposer simultanément un ancrage arbitraire.** À l'ancrage
`a=(3,1)`, la moyenne est 2 et le dernier suffixe vaut 1<2. La rotation `(1,3)`
fonctionne. Un bloc de somme totale maximale n'a donc pas nécessairement tous
ses suffixes équilibrés : pour h=m tous les blocs ont la même somme totale.
À m=1, aucune inégalité stricte ne peut être déduite ; les listes constantes
montrent le même problème pour tout m.

Même l'ajout d'une fermeture **affine rationnelle** et d'un ancrage au minimum
global ne suffit pas à ce renforcement non pondéré : les blocs
`(k_1,l_1)=(3,1)` et `(k_2,l_2)=(1,2)` donnent le retour exact

\[
 73/47,133/47,223/47,358/47,179/47,292/47,146/47,73/47.
\]

Les minima sont 73/47 et 179/47 ; le minimum global est au premier bloc,
dont la liste k=(3,1) n'est pas suffix-balanced au sens précédent.
**Ce n'est pas un cycle Collatz entier**, ni un témoin satisfaisant X0, ni
un contre-exemple au lemme pondéré inconnu de Wang. C'est un contre-exemple
exact à l'argument affaibli qui n'utiliserait que les récurrences affines
positives et la fermeture. L'intégralité ne peut être omise silencieusement.

### Obligations encore NON VÉRIFIÉES dans le manuscrit

- La définition précise : suffixes de k_i, sommes pondérées par δ, ou autre
  quantité ; longueur du bloc et admissibilité de chaque coupure cyclique.
- L'ordre des quantificateurs : sélection d'une rotation, puis d'un bloc,
  ou bloc devant commencer au minimum global déjà fixé. La rotation libre
  ne démontre pas à elle seule l'énoncé avec cet ancrage.
- La compatibilité simultanée des bornes pour tous les suffixes ; un maximum
  séparé pour chacun ne produit pas nécessairement un même bloc.
- Le sens de convexité et le domaine de l'optimisation. Par exemple, x² est
  convexe, mais `0²+2²>2·1²` : la valeur à la moyenne n'est pas un majorant.
  Passer à un maximum demande un domaine admissible et des extrémités justifiés.
- La marge stricte : conserver des `<` exige un argument au-delà d'un lemme
  donnant seulement `≥`. Les constantes logarithmiques doivent être encadrées
  rationnellement dans le sens utile, surtout après bootstrap diophantien.
- Les certificats numériques et leur dépendance exacte à X, m, K, L ; une
  couverture par calcul de départs ne prouve pas une inégalité analytique.

Aucun de ces points n'est présenté comme une erreur constatée chez Wang.
Sans texte, un verdict « lemme vrai » ou « lemme faux » serait fabriqué.

## 5. Petits contrôles réellement exécutés

```sh
python3 research/etude39/exact_checks.py
```

**PASS**, Python 3.12.14, bibliothèque standard et fractions rationnelles :

- 1 092 listes cycliques de longueur 1–6 sur {1,2,3} : existence d'une rotation
  équilibrée pour tous les suffixes ; 6 015 contrôles de moyennes de fenêtres.
- Contre-exemple exact `(3,1)` à l'ancrage imposé et reproduction de la boucle
  rationnelle ci-dessus avec fermeture, croissance et décroissance des blocs.
- Contre-exemple au raisonnement réciproque : x=4<U=8 et R=1/2<3/x,
  mais R>3/U. Il réfute une inférence, pas une valeur de R d'une vraie orbite.
- Contrôle de convexité et illustration entière de l'erreur d'exposants :
  pour n=16, δ=3/2, `n^(δ²)=512>64=n^δ`. Pour le vrai δ, la preuve est celle
  de la section 3, sans substitution numérique.
- Encadrement rationnel `1,58<log3/log2<1,59`, par 32 termes de la série
  `log a = 2 sum x^(2r+1)/(2r+1)`, x=(a−1)/(a+1), avec queue majorée par
  `2 x^65/(65(1−x²))`. Aucun logarithme flottant.
- Vérification que `704·2^60 < 2^70 < 2^71` : la prémisse ancienne du dépôt
  Lean n'est pas la couverture plus récente demandée dans l'issue.

Les bornes de séries et le lemme de rotation sont prouvés par les arguments
élémentaires indiqués ; leurs tests finis ne sont pas leur preuve universelle.
Les contrôles ne testent **ni le lemme Wang**, **ni le corrigendum**,
**ni l'exclusion m≤94**. [Résultats compacts](etude39/results.json).

Commandes de source réellement exécutées : `git clone --depth 1` du dépôt
PhilNorfleet, `pdftotext -layout` de son PDF, lectures ciblées des pages et des
sources Lean, requêtes HTTP consignées, lecture HTML du dépôt auteur Barina.
Aucun calcul massif, aucune compilation Lean, aucun certificat jusqu'à 2^71.

## Publication et contrôles de livraison

La branche `research/etude39-cycle-audit` est poussée sur GitHub.
Commande de PR réellement tentée :

```sh
gh pr create --repo hsirven1/syracuse_search --base main \
  --head research/etude39-cycle-audit --draft \
  --title 'Étude 39 : audit des cycles, défaut Hercher v3 et certificat Wang non vérifié' \
  --body-file research/etude39/PR_BODY.md
```

Résultat : `Post "https://api.github.com/graphql": Forbidden`.
**Aucune PR créée par cet accès ; aucune fusion.**
[Comparateur GitHub](https://github.com/hsirven1/syracuse_search/compare/main...research/etude39-cycle-audit?expand=1).
Le [corps de PR](etude39/PR_BODY.md) est conservé pour une création automatique
par l'assistant GitHub connecté, conformément au repli prévu dans l'issue.

Le premier `git diff --cached --check` a signalé un blanc final dans l'extrait
PDF ; l'extrait a été nettoyé des blancs finaux et du saut de page. Le contrôle
final de toutes les modifications depuis la base passe. Les empreintes
concernent les sources originales, pas cet extrait normalisé.

## 6. Conclusion de recherche

**ARRÊT : zéro lemme nouveau retenu.** La faute de 2023 est déjà signalée
par les sources consultées ; la rotation classique n'est pas nouvelle ;
les contre-exemples élémentaires ne constituent pas une réfutation de Wang.
Aucune base vérifiée ne justifie une extension m=95 ni une formalisation.
L'audit complet demandé du maillon suffix-balanced demeure **NON ÉTABLI**
à cause des sources primaires inaccessibles. Ce n'est pas un arbitrage définitif
de la vérité de l'exclusion 94, ni une preuve d'absence de cycles non triviaux.

**Prochaine action unique :** faire ouvrir par l'assistant GitHub connecté
la PR brouillon de `research/etude39-cycle-audit` vers `main`, en lui demandant
explicitement de conserver le verdict « audit incomplet / exclusion 94 non vérifiée ».
