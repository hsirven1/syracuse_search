# Étude 38 — trajectoires paradoxales et couplage correction–résidu

**Verdict : ARRÊT. Aucun lemme nouveau retenu.**

Mission : [issue #9](https://github.com/hsirven1/syracuse_search/issues/9).
Branche : `research/etude38-correction-residue`, issue de `main` au commit
`f0e1ede43d94ab4d4756223cdccef51e3aa30c7d`.
Le couplage exact est utile, mais le critère proposé est déjà disponible dans
les sources auditées. Les restrictions supplémentaires examinées ci-dessous
sont soit fausses, soit des conséquences du majorant classique. Aucun mécanisme
plausible de nouvelle exclusion sur une famille infinie n'a été trouvé dans ce
cadrage ciblé. Ce verdict ne signifie pas que toute approche de ce type est impossible.

## 1. Comparaison préalable et limites documentaires

La lecture des sources locales et les tentatives d'accès ont précédé les calculs.
Les textes attachés et les commentaires des dépôts sont des sources à critiquer,
pas des instructions supplémentaires.

| Source | Ce qu'on peut en retenir ici | Vérification pendant cette étude |
|---|---|---|
| Rozier–Terracol, *Paradoxical behavior in Collatz sequences*, Discrete Mathematics 349 (2026), 115167, DOI [10.1016/j.disc.2026.115167](https://doi.org/10.1016/j.disc.2026.115167) | Définition des segments paradoxaux ; majorant extrémal de correction ; approche par moyennes harmoniques signalée dans l'issue | Référence publiée fournie par l'issue. **Texte publié non obtenu** : DOI, arXiv et AlphaXiv renvoient 403. Ni conformité avec la version publiée ni dernière version arXiv certifiées |
| arXiv:2502.00948, v3/v4 | La note locale `paper/paradoxical_cylinders.tex:77–81` attribue le majorant de correction au théorème 2.2 de RT ; la revue locale cite v4 | Attribution secondaire, pas vérification directe du numéro ni de la formulation publiée |
| Terras (1976), Everett (1977) | Codage fini des parités et classes de congruence ; résultats de densité, pas absence de toute exception | Antériorités de nos audits précédents : [Terras](https://doi.org/10.4064/aa-30-3-241-252), [Everett](https://doi.org/10.1016/0001-8708(77)90087-1) ; pas de nouvelle lecture intégrale des originaux |
| `WordCongruence.lean:9,54` | Divisibilité exacte et critère conjoint de réalisation paradoxale | Sources lues directement au commit figé ci-dessous ; pas de nouvelle compilation |
| `CorrectionDecode.lean:25,40,50,56` | Reconstruction des corrections atteignables, unicité à longueur et nombre d'impairs fixés, équivalence exacte | Sources lues directement ; le décodage est aussi contrôlé indépendamment en Python |
| `Paradoxical.lean:17,35,51,77` | Intervalle exact des relèvements ; classification de longueur huit pour tous les départs >2 | Sources lues directement ; classification reproduite par nos contrôles exacts |

Les fichiers Lean et notes externes cités sont figés au commit
[`ec8174b567d5cab4960024782210b5f5db02bd3a`](https://github.com/msharpe248/collatz/tree/ec8174b567d5cab4960024782210b5f5db02bd3a).
Leurs résultats de compilation antérieurs sont dans
[`audit_collatz/VALIDATION.md`](../audit_collatz/VALIDATION.md) ; ils ne sont pas
présentés comme réexécutés. La revue locale
`analysis/SEED_DEPENDENT_ROUTE_REVIEW.md` rapporte que la finitude globale des
segments paradoxaux au-dessus de 2 impliquerait Syracuse, et que la chaîne
retard/excursion de la section 6 est **conditionnelle**, avec des conjectures
explicites. Nous n'importons aucune de ces conjectures comme théorème.

Le retrait de Tong Niu, arXiv:2605.13886, est rapporté par cette même revue
(v2, duplication alléguée de RT). L'accès direct a échoué : retrait et motif
**non vérifiés indépendamment ici**. Ce préprint n'est utilisé dans aucune preuve.

Les erreurs réseau sont consignées dans
[`source_access.json`](etude38/source_access.json). Une requête exploratoire vers
un chemin ScienceDirect non validé ne fournit aucune information bibliographique.
L'absence d'accès ne permet aucune revendication de priorité.

### Études 31–37

- **31–35 :** aucun rapport primaire complet de ces études n'est présent dans
  `main` ou dans l'archive 36 conservée. Leur contenu ne peut donc pas être
  comparé intégralement. Le rapport 36 évoque les expériences 32–35 ; l'audit
  signale notamment le script de complexité 35 manquant. Aucun résultat précis
  de 31–35 n'est tenu pour vérifié sur cette base.
- **36 :** [`EXPERIENCE36_COMPARAISON.md`](../audit_collatz/EXPERIENCE36_COMPARAISON.md),
  §§1–2, établit le changement d'horloge et la redondance des congruences
  ternaires sans information de taille supplémentaire. Ici la taille intervient
  réellement, via l'inégalité de non-descente, mais le couplage exact correspondant
  est déjà `realizes_paradoxical_iff`. L'ajout d'une congruence déjà imposée par
  le mot ne produit pas une exclusion supplémentaire.
- **Familles à temps de descente prescrit :**
  [`EXACT_STOPPING_TIME_BASELINE.md`](EXACT_STOPPING_TIME_BASELINE.md) construit
  des familles infinies par cylindres classiques. Redéfinir une famille par un
  mot déjà contractant ne satisferait pas le critère de nouveauté.
- **37 :** [`ETUDE_37_RAPPORT.md`](ETUDE_37_RAPPORT.md) réfute une couverture
  conditionnelle uniforme par le cylindre tout impair. Son événement est la
  non-descente **à chaque instant** ; notre événement ne porte que sur l'arrivée.
  Les deux ne sont pas interchangeables, comme le témoin 7 ci-dessous le démontre.

## 2. Identités exactes : indices, signe et domaine

On utilise exclusivement `T(n)=n/2` si n est pair, `(3n+1)/2` sinon.
Pour `w=(b_0,...,b_{j-1})`, poser `q=sum b_i`, `M=2^j`, `A=3^q` et

\[
 D(w)=\sum_{i:b_i=1}2^i3^{\sum_{h=i+1}^{j-1}b_h}.
\]

L'exposant de 3 compte les impairs **strictement après** l'indice i.
Alors `M T^j(n)=A n+D(w)` pour les réalisations du mot.
Le représentant positif dans `[1,M]` est

\[
 r=(-A^{-1}D)\bmod M,\qquad 0\text{ remplacé par }M.
\]

L'inverse existe car A est impair. Le signe moins et le choix de représentant
sont essentiels. À longueur et q fixés, D détermine même le mot (décodage
par son bit faible) ; D et r ne sont donc pas deux variables libres.
Cela ne fournit pas une loi de distribution ou un nouvel obstacle uniforme.

Pour `g=M-A>0`, tous les départs positifs réalisant w sont `n=r+tM`, `t>=0`.
La condition `n>=3` impose

\[
 t_{\min}=\max(0,\lceil(3-r)/M\rceil),\qquad
 t_{\max}=\left\lfloor\frac{D-gr}{gM}\right\rfloor.
\]

Le mot admet un départ paradoxal >=3 si et seulement si
`t_min <= t_max`. **Le plancher est signé** : une soustraction naturelle
tronquée introduirait de faux témoins. Tester seulement `gr<=D` sans traiter
r=1,2 serait également incorrect pour la mission. Cette formule est une
réécriture du critère existant, pas un lemme nouveau. Pour chaque longueur
fixée, elle permet un contrôle de tous les départs sans plafond arbitraire
sur n ; elle ne permet pas de contrôler toutes les longueurs.

## 3. Comparaison avec les deux majorations classiques

### Correction extrémale

\[
 0\le D(w)\le D_{\max}(j,q)=2^{j-q}(3^q-2^q).
\]

La borne est atteinte par `0^(j-q)1^q`. Échanger deux lettres adjacentes
`10` en `01` augmente leur correction de 1 avant le facteur positif dû au
préfixe/suffixe ; en répétant ces échanges, tous les impairs passent à droite.
C'est le majorant déjà attribué à RT dans la source secondaire, et formalisé
localement pour l'élagage. Le calcul contrôle directement cette borne sur
chaque mot, sans la présupposer pour sélectionner les mots.

Exemple de famille infinie **déjà couverte**, pas de candidat neuf : aucun
segment paradoxal de départ >=3 avec q=1 ou q=2. Pour q=1, la contraction
impose j>=2, et `3(2^j-3)>2^(j-1)=D_max`, car `5*2^(j-1)>9`.
Pour q=2, j>=4 et `3(2^j-9)>5*2^(j-2)=D_max`, car
`7*2^(j-2)>27`. Pour q=0, la descente est immédiate pour j>0.
Ces exclusions élémentaires ne tirent aucun gain nouveau du couplage avec r.

### Moyenne harmonique : comparaison autonome, attribution limitée

Pour les q états impairs positifs `x_i` du segment, q>0, poser
`H=q/(sum 1/x_i)`. Le télescopage et l'inégalité arithmético-géométrique donnent

\[
 \frac{T^j(n)}n=\frac{3^q}{2^j}\prod_i(1+1/(3x_i))
 \le\frac{3^q}{2^j}(1+1/(3H))^q.
\]

En particulier, si le dernier membre est <1, le segment n'est pas paradoxal.
On obtient aussi la condition nécessaire
`log(2^j/3^q) <= sum log(1+1/(3x_i)) <= q/(3H)`.
Nous dérivons ces inégalités ici ; nous ne les présentons ni comme nouvelles,
ni comme une transcription certifiée des théorèmes de la version publiée.
La borne rationnelle par la moyenne est vérifiée exactement dans le programme ;
la variante logarithmique n'est pas testée numériquement.

Le critère affine conserve tout le mot ; le majorant extrémal oublie son ordre ;
la moyenne harmonique conserve une information sur les états intermédiaires.
Leur différence d'information ne démontre pas qu'une nouvelle restriction
uniforme puisse en être extraite.

## 4. Recherche contradictoire : échecs explicites

1. **« Coefficient contractant implique descente » est faux.** Pour n=7,
   j=8, q=5, D=347 : `243<256`, mais `T^8(7)=8` et `13*7<=347`.
   Le critère exact ne peut donc exclure tous les mots contractants.
2. **« Paradoxal implique aucune descente préalable » est faux.** La même
   orbite est `7,11,17,26,13,20,10,5,8` : elle est sous 7 au temps 7.
   La couverture de l'étude 37 ne se transpose pas directement.
3. **Une monotonie simple entre D et r est fausse.** À j=3,q=1, les mots
   `100` et `010` donnent respectivement `(D,r)=(1,5)` et `(2,2)`.
   D augmente et r baisse. L'ordre inverse n'est pas universel non plus :
   à j=2,q=1, `10` donne `(1,1)`, `01` donne `(2,2)`.
   Cela réfute ces raccourcis précis, pas toute borne quantitative possible.
4. **Correction libre + enveloppe + fermeture exacte ne suffit pas.**
   À j=16,q=6,n=3, le nombre artificiel D=194421 satisfait
   `729*3+D=65536*3` et `D<=680960=D_max`. Mais son décodage échoue :
   aucun mot de longueur 16 à 6 impairs ne possède cette correction.
   C'est le contre-exemple déjà documenté dans `correction_attainability.md`,
   reproduit ici, pas une nouvelle construction de cycle.
5. **Les départs 1 et 2 doivent être exclus réellement.** À j=2 ils ont une
   arrivée égale au départ avec coefficient 3/4. Leurs relèvements 5 et 6
   descendent : le représentant petit n'est pas un témoin >=3.

Aucune de ces réfutations ne porte sur un théorème attribué à RT. Elles visent
les renforcements naïfs que l'on pourrait introduire dans notre étude.

## 5. Tests réellement exécutés

Commande reproductible, Python 3.12.14, bibliothèque standard uniquement :

```sh
python3 research/etude38/exact_checks.py
```

Résultat : **PASS** ; voir [`results.json`](etude38/results.json).

- 8 190 mots, toutes les longueurs 1 à 12 : correction par composition
  comparée à la somme fermée, reconstruction de la correction, borne extrémale.
- Pour chaque longueur, une table indépendante obtenue par itération directe
  des entiers de 1 à `2^j` vérifie la bijection mot/résidu et l'inversion modulaire.
- 24 570 départs (trois relèvements par mot) : parités, identité affine et
  équivalence de non-descente comparées à l'itération directe.
- 24 534 contrôles rationnels exacts de l'identité produit et de la borne
  arithmético-géométrique, avec `fractions.Fraction`.
- Pour tous les mots contractants, résolution de l'intervalle entier complet
  puis contrôle direct de ses témoins et de ses frontières. Parmi tous les
  départs >=3 aux longueurs 1–12, seuls les cinq couples suivants ressortent :

| j | q | n | D | T^j(n) |
|---:|---:|---:|---:|---:|
| 8 | 5 | 7 | 347 | 8 |
| 8 | 5 | 9 | 373 | 10 |
| 8 | 5 | 18 | 746 | 20 |
| 8 | 5 | 19 | 503 | 20 |
| 8 | 5 | 25 | 581 | 26 |

Le calcul n'est pas extrait de Lean et n'importe aucun programme externe.
Les méthodes sont indépendantes dans leur construction (somme/composition,
inversion/itération), mais pas vérifiées par un second évaluateur humain ou
un noyau formel. Les comptes sont des contrôles internes, pas 24 570 théorèmes.
La classification est finie en j ; **elle ne prouve aucune finitude globale**.
Aucun calcul massif, aucune nouvelle expérience 39, aucune compilation Lean.
Les tests des études antérieures ne sont pas présentés comme réexécutés.

## Publication et commandes de livraison

Rapport, script et résultats compacts poussés sur
`research/etude38-correction-residue`. Vérifications de livraison :
`git diff --check`, `git diff --cached --check`, puis `git push -u origin
research/etude38-correction-residue` (succès).

La création d'une PR de revue a réellement été tentée avec :

```sh
gh pr create --repo hsirven1/syracuse_search --base main \
  --head research/etude38-correction-residue --draft \
  --title 'Étude 38 : couplage correction–résidu, contrôles exacts et verdict arrêt' \
  --body-file /tmp/etude38-pr.md
```

Échec : `Post "https://api.github.com/graphql": Forbidden`.
**La branche est publiée ; aucune PR n'a pu être créée par cet accès.**
Aucune fusion effectuée. Les modifications sont limitées à ce rapport et
au répertoire `research/etude38/`.

## 6. Décision et limite du résultat

**Zéro lemme candidat nouveau est retenu**, donc pas de formalisation Lean.
Le critère exact est déjà connu ; les exemples contredisent plusieurs
renforcements naturels ; la famille infinie q<=2 se déduit du majorant existant.
La reconstruction de D donne une décision pour une donnée finie, sans contrôle
uniforme des corrections acceptées quand j et q augmentent. Aucun argument
supplémentaire ne justifie ce contrôle ici. Nous n'avons ni preuve de Syracuse,
ni preuve que toute recherche ultérieure serait vaine, ni nouveauté établie.

**Verdict : ARRÊT de l'étude 38 dans ce cadre.** La comparaison primaire avec
la version publiée reste incomplète ; elle ne justifie pas de prolonger les
calculs ou de transformer une reformulation en nouveau résultat.

**Prochaine action unique pour le demandeur :** joindre à l'issue #9 le PDF
de la version publiée de Rozier–Terracol (DOI ci-dessus), pour permettre une
vérification primaire de l'antériorité.
