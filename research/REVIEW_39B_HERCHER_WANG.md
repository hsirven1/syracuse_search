# Revue 39B — corrigendum Hercher, suffixes de Wang et certificat S₅

**Verdict global : NON VÉRIFIABLE pour l'exclusion m≤95 ; ARRÊT de la recherche
additionnelle.** Aucun contre-exemple au manuscrit Wang ni au corrigendum
original n'est établi. Le modèle convexe cyclique et les lemmes 5–7 **tels que
transcrits** dans la note de suivi admettent les justifications ci-dessous.
Le passage au certificat fini et ses entrées externes ne sont pas validés.

Revue de [l'issue #13](https://github.com/hsirven1/syracuse_search/issues/13),
base [PR #12](https://github.com/hsirven1/syracuse_search/pull/12), commit
`c2b11a63e2db0a322c36e84bfc861aa4c546adc7`.
Les anciens rapports sont laissés intacts. Il ne s'agit pas d'une étude 40.

## 1. Provenance et périmètre documentaire

Lecture initiale : [`PRIMARY_SOURCE_FOLLOWUP.md`](etude39/PRIMARY_SOURCE_FOLLOWUP.md),
§§1–2, à ce commit, puis corps et commentaire de la PR #12 et issue #13.
La note est le compte rendu d'une autre lecture ; **elle ne remplace pas une
source primaire obtenue indépendamment**.

Les accès directs suivants ont tous renvoyé un tunnel HTTP 403 : corrigendum
PDF et `corrigendum.tex` du JIS, ResearchGate du nouveau manuscrit Wang,
page/API Zenodo 21017296 et site auteur du calcul Barina. Les erreurs sont
conservées dans [`source_access.json`](review39b/source_access.json).
La recherche de dépôts GitHub par l'identifiant Zenodo ne fournit aucun dépôt
identifié comme artefact ; ce n'est pas une preuve d'absence de scripts publics.
Aucun fichier de certificat, version horodatée ou empreinte d'artefact Wang
n'a pu être récupéré. Aucun script original n'a été exécuté.

Sources primaires demandées, **non relues directement dans cette revue** :

- [Hercher, corrigendum JIS](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/corrigendum.pdf),
  [répertoire et source TeX](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/).
- Wang, *Non-existence of Collatz m-cycles for m≤95*,
  [ResearchGate](https://www.researchgate.net/publication/408180567_NON-EXISTENCE_OF_COLLATZ_m-CYCLES_FOR_m_95),
  [DOI de dépôt annoncé](https://doi.org/10.5281/zenodo.21017296).

La maquette `#Axx INTEGERS 26 (2026)` et les dates éditoriales vides sont
rapportées par le suivi : ce manuscrit est traité comme **prépublication**,
aucune acceptation/publication INTEGERS n'est établie. Le résultat ≤95 ne doit
pas être confondu avec le précédent dépôt ≤94. Les bornes Simons–de Weger et
la couverture X=2^71 restent des entrées externes non recertifiées ici.

## 2. Optimisation de Hercher : le domaine cyclique fermé

Posons δ=log₂3>1, h≥1, B=hK/m, et

\[
 P_h(B)=\{x\in\mathbb R^h:x_i\ge1,\ x_{i+1}\le\delta x_i\ (i\bmod h),
                   \ \sum_i x_i\ge B\},\qquad
 f(x)=\frac3{2^x-1},\quad S(x)=\sum_i f(x_i).
\]

Cette définition inclut expressément **le raccord x₁≤δx_h**. La note évoque
ce raccord, mais ne permet pas de vérifier comment un bloc de h minima extrait
d'un cycle à m minima le satisfait quand h<m. Les deux questions sont séparées.

### Atteinte et réduction aux sommets : la non-bornitude n'est pas une faute

Le polyèdre est non vide : une constante c≥max(1,B/h) convient. Il est fermé.
Si M=max x_i et a=min x_i, les relations cycliques donnent
`M≤δ^(h−1)a`. Ainsi toute suite non bornée dans P a **toutes** ses coordonnées
qui tendent vers l'infini le long d'une sous-suite de norme croissante, et
`S≤h f(M/δ^(h−1))→0`. Or S est continue et strictement positive en tout point
fini de P. Son maximum est donc atteint dans une partie bornée.

Plus précisément, choisir x⁰∈P, puis R>max x⁰_i tel que
`h f(R/δ^(h−1))<S(x⁰)`. Sur le polytope compact `P∩[1,R]^h`, S atteint son
maximum en un sommet, par convexité. Aucun point de la face `max x_i=R` ne
peut maximiser, d'après le choix de R. Le sommet maximisant n'a donc aucune
contrainte supérieure artificielle active et est aussi un sommet de P.

La convexité employée est réelle : pour a=log2,

\[
 f'(x)=-\frac{3a2^x}{(2^x-1)^2}<0,\qquad
 f''(x)=\frac{3a^2 2^x(2^x+1)}{(2^x-1)^3}>0.
\]

Cet argument décharge l'obligation d'atteinte **sur ce domaine cyclique**.
Il ne certifie pas la transcription du domaine officiel.

### Contraintes actives et progression géométrique

Écrire `G_h=1+δ+⋯+δ^(h−1)`. L'hypothèse suffisante utilisée dans l'argument
suivant est **B>G_h**. Si une coordonnée vaut 1, les relations cycliques donnent
`sum x_i≤G_h`, contradiction. Aucune contrainte x_i=1 n'est donc active, même
sur la frontière de P.

Un sommet nécessite h normales actives de rang h. Les h contraintes de croissance
ne peuvent toutes être des égalités : leur produit imposerait `x₁=δ^h x₁`,
impossible pour x₁≥1 et δ>1. Il reste au plus h−1 de ces égalités. La somme
est donc active, ainsi qu'exactement h−1 contraintes de croissance. À rotation
près, le sommet est

\[
 (v,\delta v,\ldots,\delta^{h-1}v),\qquad
 v=B/G_h=B(\delta-1)/(\delta^h-1)>1.
\]

Le cas h=1 donne directement x₁=B et ne demande aucune égalité de croissance.
Tous les sommets candidats ont la même valeur de S. En particulier,

\[
 S(x)\le\sum_{i=0}^{h-1}f(\delta^iv)
 \le\frac3{2^v-1}+\frac{3(h-1)}{(2^v-1)^\delta}.
\]

Pour la dernière étape, `2^(δv)−1≥(2^v−1)^δ`, puisque
`(y+1)^δ≥y^δ+1` pour y>0, δ>1 ; puis utiliser la décroissance de f.
Sans B>G_h, exclure les faces x_i=1 par ce raisonnement serait injustifié.
Le seuil logarithmique rapporté pour le théorème 21 peut assurer cette condition
lorsque X est grand, mais sa formule officielle reste à relire.
Les contraintes relaxées ne créent pas à elles seules une marge stricte ;
une stricte inégalité peut venir de la borne indépendante `R(n)<3/n`
pour la somme finie des inverses d'un paquet d'impairs.

### Attention : un bloc ouvert ne se referme pas automatiquement

Dans un cycle complet à m minima, un bloc de h minima n'hérite directement que
de h−1 relations internes. Les étapes restantes donnent au mieux
`x₁≤δ^(m−h+1)x_h`, **pas** `x₁≤δx_h`.

Contre-exemple exact au transfert abusif : prendre les variables logarithmiques
cycliques `(9,4,6)` et le bloc `(9,4)`, B=13. Toutes les relations du **cycle à
3 coordonnées** sont strictement satisfaites pour le vrai δ∈(1,58;1,59).
Le bloc ne vérifie pas son raccord interne `9≤4δ`. Sa somme vaut

\[
 f(9)+f(4)=526/2555>1/5.
\]

Pour le modèle **fermé** à h=2 et B=13, v=13/(1+δ)>5 et δv>7 ; sa valeur
maximale est donc strictement inférieure à

\[
 f(5)+f(7)=474/3937<1/5.
\]

Ainsi appliquer cette borne cyclique à n'importe quel bloc ouvert est faux.
Les coordonnées peuvent être interprétées comme log₂(n_i+1) avec n_i entiers,
mais elles **ne décrivent pas un cycle Collatz réalisé** ; cet exemple ne
réfute pas le corrigendum original. Il identifie l'hypothèse de raccord à
retrouver dans son texte ou dans la sélection du bloc. Il ne suffit pas de
remarquer que les minima proviennent quelque part d'un cycle plus long.

## 3. Wang : les lemmes 5–7 transcrits sont cohérents

Noter k_i≥1 le nombre de pas impairs après le minimum n_i, K=sum k_i,
μ=K/m, `x_i=log₂(n_i+1)` ; ne pas lire `n_r+1` comme `n_(r+1)`.
L'indice i est cyclique sur les m minima du cycle complet.

**Lemme 5, version rapportée.** De `k_i≤x_i` et
`x_(i+1)≤δx_i`, on tire, pour tout r et s≥1,

\[
 K_{r,s}=\sum_{d=0}^{s-1}k_{r+d}\le x_rG_s,\qquad
 n_r+1\ge2^{K_{r,s}/G_s}.
\]

C'est une somme géométrique sur une **chaîne ouverte** : aucun raccord interne
supplémentaire n'est utilisé. Les hypothèses de croissance sont celles à
justifier pour les vrais minima ; elles étaient déjà au cœur du lemme 20
Hercher étudié précédemment.

**Lemme 6, version rapportée.** Centrer a_i=k_i−μ ; choisir une extrémité e
qui maximise les sommes partielles S₀,…,S_(m−1). Puis, pour chaque s≤m,
prendre le bloc de s termes **qui se termine en e**. Pour chaque t≤s, la
somme du suffixe de t termes est ≥tμ : c'est `S_e−S_(e−t)≥0`, avec
prolongement périodique des sommes partielles et somme totale centrée nulle.
Une **même extrémité** convient à tous les t et même à tous les s.
Aucune stricte inégalité ne suit : les listes constantes donnent l'égalité.

**Lemme 7, version rapportée.** Pour le suffixe de longueur t de ce même bloc,
son départ r=e−t satisfait le lemme 5 avec `K_(r,t)≥tμ`. D'où

\[
 x_{e-t}\ge V_t=t\mu/G_t,\quad
 n_{e-t}\ge2^{V_t}-1,\quad
 \sum_{i\text{ dans le bloc}}R(n_i)
 <\sum_{t=1}^s\frac3{2^{V_t}-1}.
\]

Chaque t correspond à un minimum distinct quand s≤m. Une borne ρ sur la
contribution du **complément du même bloc** permet de majorer la somme totale
par le membre droit +ρ. Il faut une borne valable pour ce complément ; si
celui-ci est un bloc consécutif, utiliser une majoration adaptée à sa longueur
avec les bons termes de bord. La formule exacte de ρ n'est pas dans le suivi.

**Conclusion locale :** aucune erreur de rotation/quantificateurs dans cette
chaîne telle que transcrite. Elle ne suppose jamais que le bloc commence au
minimum global. Le contre-exemple `(3,1)` de l'étude 39 ne la réfute pas.
Le bootstrap peut utiliser cette majoration d'une somme globale sans conserver
l'emplacement du bloc. Un certificat ultérieurement ancré au minimum global
est compatible avec cela **s'il ne réutilise pas la propriété suffix-balanced
à cet ancrage**. Sans les lemmes 11–13 originaux, cette condition n'est pas
vérifiée dans le manuscrit complet.

## 4. Du bootstrap au certificat : obligations non vérifiées

Le suivi rapporte `K₀=205632218873398596256` et les longueurs
`(47,67,77,82,86,88)`. Nous n'avons ni les encadrements des fractions continues,
ni les marges, ni ρ, ni les scripts exacts utilisés. Ces constantes sont
**rapportées, pas recalculées**. Le contrôle de deux inégalités à flottants ne
remplacerait pas des bornes rationnelles orientées dans le sens utile.

Pour conclure à partir de S₅=∅, il faudrait au minimum vérifier :

1. Une définition précise de S_d, de ses états et de ses intervalles entiers,
   avec la projection de **tout** cycle admissible dans S₀ puis S_d.
2. Que chaque filtre est une condition nécessaire, et que chaque enfant légal
   est engendré. Les bits perdus par division, les congruences, les bornes
   inférieures/supérieures et les plafonds doivent être propagés exactement.
3. L'exhaustivité des bornes k_i, ℓ_i dépendant des préfixes ; l'arrêt d'un
   programme ou une limite de travail ne doit pas être confondu avec un ensemble vide.
4. La couverture de tous les cas : m<95, m=95, n_min>24X et
   X≤n_min≤24X, bornes sur K et, s'il y a lieu, identification des rotations.
   Un résultat sur ce seul intervalle ne suffit pas.
5. Une liste d'artefacts et leurs empreintes, paramètres, version du code,
   compteurs de branches acceptées/rejetées et un vérificateur d'exhaustivité.

La borne du premier paquet **k₁≤75** est en revanche cohérente avec l'intervalle
annoncé : `2^k₁≤n_min+1≤24·2^71+1<2^76`. La valeur 75 ne peut pas être abaissée
sur cette seule base, puisque `2^75−1` est dans l'intervalle. Cela ne borne pas
les k_i ultérieurs, dont les minima peuvent dépasser 24X.

### Une petite sous-instance exacte, indépendante des filtres inconnus

Pour un paquet de k impairs puis ℓ pairs, écrire `n=2^k a−1`, a impair positif.
Le maximum après les pas impairs est `3^k a−1`. L'exactitude de ℓ équivaut à

\[
 a\equiv3^{-k}(1+2^\ell)\pmod{2^{\ell+1}},
\]

et le minimum suivant vaut `(3^k a−1)/2^ℓ`. Le bit supplémentaire du module
assure une valuation **exacte**, pas seulement une divisibilité minimale.
Cette identité classique a été contrôlée contre l'itération directe sur les
127 départs impairs de 3 à 255, pour k=1…8 et ℓ=1…12 : 12 192 décisions,
127 couples acceptés. Les bornes et l'intervalle sont ceux de ce petit test,
**pas ceux du certificat Wang**. Aucun filtre original n'étant accessible,
ce contrôle ne valide aucun filtre inconnu ni l'exhaustivité de S₅.

### X et statut éditorial

La couverture exhaustive X=2^71 n'a pas été reproduite ni authentifiée par
une source de résultats indépendante. Le site auteur est inaccessible ;
le dépôt de code Barina consulté lors de la revue précédente ne certifie pas,
par sa seule existence, le périmètre d'un calcul terminé. Vérifier tous les
départs <X ou ≤X impose aussi de préciser les bornes des intervalles.
Nous n'utilisons pas cette couverture comme théorème acquis.
Le DOI Zenodo est un dépôt, pas une preuve d'évaluation par INTEGERS.

## 5. Tests et preuve : portée exacte

Commande exécutée :

```sh
python3 research/review39b/exact_checks.py
```

Résultat **PASS**, Python 3.12.14, fractions rationnelles et entiers uniquement :

- encadrement de δ par 32 termes de la série logarithmique avec queue rationnelle ;
- contre-exemple `(9,4,6)` au transfert bloc fermé/bloc ouvert, pour le vrai δ ;
- 1 092 listes cycliques sur {1,2,3}, longueurs 1–6 ; 6 015 fenêtres de croissance
  et **19 956 suffixes du même bloc choisi**, avec un cap rationnel cyclique
  `x_i=max_(0≤d<m) k_(i+d)/(3/2)^d` ; ce δ rationnel sert de modèle algébrique,
  il ne remplace pas log₂3 dans le contre-exemple ni dans la preuve théorique ;
- 12 192 contrôles exacts de paquets contre itération directe ;
- borne arithmétique k₁≤75 et égalités qui empêchent une stricte version du lemme 6.

[Résultats](review39b/results.json), [programme](review39b/exact_checks.py).
Les preuves universelles des §§2–3 ne reposent pas sur ces échantillons finis.
Pas de nouveau calcul massif, pas de compilation Lean, pas de parcours de
S₅, pas de vérification des filtres Wang originaux. Les anciennes suites de
tests n'ont pas été présentées comme réexécutées.

## Publication et validation de livraison

La branche `review/issue13-hercher-wang` a été committée et poussée.
La tentative de création de PR a réellement utilisé :

```sh
gh pr create --repo hsirven1/syracuse_search \
  --base research/etude39-cycle-audit --head review/issue13-hercher-wang \
  --draft \
  --title 'Revue 39B : corrigendum convexe, suffix-balanced et certificat S5 non vérifiable' \
  --body-file research/review39b/PR_BODY.md
```

Échec : `Post "https://api.github.com/graphql": Forbidden`.
Aucune PR n'a été créée par cet accès et aucune fusion n'a été faite.
[Comparateur GitHub](https://github.com/hsirven1/syracuse_search/compare/research/etude39-cycle-audit...review/issue13-hercher-wang?expand=1).
Le corps de PR est conservé pour la création par l'assistant GitHub connecté.
`git diff --check` et `git diff --cached --check` passent ; les anciennes
sources suivies par le manifeste sont identiques à la base de la PR #12.

## 6. Verdict par étape

| Étape | Verdict |
|---|---|
| Atteinte, sommets et majoration pour P_h(B) **fermé cycliquement**, B>G_h | Justification mathématique donnée ici pour ce modèle transcrit ; pas une nouveauté revendiquée |
| Application du modèle fermé au bloc sélectionné par le corrigendum officiel | **NON VÉRIFIABLE** sans le texte ; hypothèse de raccord à contrôler |
| Lien automatique bloc ouvert → même polyèdre cyclique fermé | **RÉFUTÉ** au niveau de la relaxation, pas comme accusation envers l'auteur |
| Lemmes Wang 5–7 selon la transcription du suivi | Démonstration cohérente sous les hypothèses indiquées ; original non relu |
| Lemmes 11–13, ρ, fractions continues et ancrage du certificat | **NON VÉRIFIABLE** |
| S₅=∅ et exhaustivité des branches | **NON VÉRIFIABLE**, aucun artefact récupéré |
| Entrées externes et exclusion de tous les m≤95 | **NON VÉRIFIABLE** dans cette revue |

**ARRÊT**, aucun petit lemme nouveau proposé. L'argument convexe et les
suffixes ne justifient pas de rejeter les résultats annoncés ; ils ne suffisent
pas non plus à les certifier. Il reste une obligation analytique de raccord
et une obligation de certification calculatoire, dont on ne peut conclure
qu'elles sont des lacunes effectives des textes non accessibles.

**Prochaine action unique :** faire ouvrir par l'assistant GitHub connecté
la PR brouillon de `review/issue13-hercher-wang` vers `research/etude39-cycle-audit`,
avec le corps enregistré dans `research/review39b/PR_BODY.md`.
