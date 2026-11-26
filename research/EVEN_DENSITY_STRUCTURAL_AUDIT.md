# Densité des pas pairs : audit, rigidité partielle et borne critique de complexité

**Conclusion centrale : question restant ouverte dans ce travail. La pente
1/log₂(3/2) n'est pas dépassée.** Nous démontrons ci-dessous un renforcement
conditionnel du reste logarithmique, une exclusion arithmétique explicite de
mots infinis clairsemés, et un obstacle précis à la seule relaxation réelle.
Aucune nouveauté scientifique ni preuve de Syracuse n'est revendiquée.

Sources de départ figées : [PR #21](https://github.com/hsirven1/syracuse_search/pull/21),
`4b2a31e262e4fdf3b6dc26588e71a3b7e04bb9a7`, et
[PR #22](https://github.com/hsirven1/syracuse_search/pull/22),
`57d894cbff791d7c8084a1d04affbee52a22ae47`.
Branche de ce résultat : `research/even-density-structural-audit`, issue de #22.
Les textes et programmes précédents sont laissés intacts.

## 1. Énoncé et contrôle des PR #21–22

On travaille avec T(n)=n/2 si n est pair, (3n+1)/2 sinon.
Poser n_t=T^t(N), E(t)=nombre de pas pairs parmi les t premiers pas,
δ=log₂3, β=δ−1=log₂(3/2), H(t)=log₂(n_t+1), et N+1≤2^K.
La complexité p_N(L) compte les facteurs de longueur L sur **tout l'itinéraire
infini**, pas uniquement un échantillon initial.

La conjecture auxiliaire demandée se quantifie ainsi :

\[
 \forall N>0\ \bigl[\text{orbite non bornée}\Longrightarrow
 \eta_N:=\liminf_{t\to\infty}E(t)/t>0\bigr].                 \tag{C}
\]

Elle n'affirme pas l'existence d'une même constante η>0 pour toutes les
orbites. La version uniforme de la porte d'entrée mentionnée dans #22 est
plus forte que (C). Même démontrée, (C) ne supprimerait pas les orbites
non bornées ayant une fréquence de pairs positive mais inférieure au seuil
critique ; elle n'est pas présentée comme une preuve de Syracuse.

### PR #21 : argument correct

L'inégalité `2(T(n)+1)≤3(n+1)` implique
`n_s+1≤2^K(3/2)^s`. Les états initiaux de temps
`0≤s≤floor((L−K)/β)` sont donc <2^L.
Une orbite entière non bornée n'a pas de répétition d'état, sinon elle devient
périodique. Deux états ayant le même facteur de L parités sont congrus modulo
2^L ; sous 2^L ils sont égaux. Les facteurs sont donc distincts, ce qui donne

\[
 p_N(L)\ge1+\lfloor(L-K)/\beta\rfloor.
\]

Les comparaisons `3^17<2^27` et `3^41<2^65` sont les versions rationnelles
annoncées. Il n'y a aucune amélioration cachée de la pente par ces approximants.

### PR #22 : argument correct, mais gain seulement logarithmique

Un segment de r pas impairs depuis x vérifie
`T^r(x)+1=3^r(x+1)/2^r`, donc `2^r | x+1` et `r≤log₂(x+1)`.
Si s_i est le temps immédiatement après le i-ème pas pair, alors
`s_(i+1)≤δs_i+K+1`. La queue impaire finale donne bien

\[
 t\le (K+1)\delta^{E(t)+1}/\beta,
 \qquad E(t)\ge\frac{\log_2t}{\log_2\delta}-B_N.          \tag{1}
\]

Les suites de pas pairs consécutifs correspondent à des runs impairs de
longueur zéro et sont bien couvertes. La constante B_N dépend de N.

L'identité exacte est

\[
 H(t)=H(0)+\beta t-\delta E(t)+R(t),\qquad
 R(t)=\sum_{s<t,\ n_s\text{ pair}}\log_2(1+1/(n_s+1)).    \tag{2}
\]

Pour une orbite non bornée, les états distincts tendent vers l'infini ;
E(t)→∞ par (1), et les termes du reste tendent vers zéro, donc R=o(E).
L'enveloppe obtenue dans #22 est éventuellement croissante : elle contrôle
bien **tout** le préfixe de temps, pas seulement son dernier état. L'inversion
et l'injectivité donnent correctement

\[
 \liminf_{L\to\infty}\frac{p_N(L)-L/\beta}{\log_2L}
 \ge c_*:=\frac{\delta}{\beta\log_2\delta}.               \tag{3}
\]

En revanche, (3) ne dit pas encore
`p_N(L)≥L/β+c_*log₂L−O_N(1)` : le défaut au coefficient critique pourrait
être o(log L) mais non borné, comme un défaut −sqrt(log L).
La section 3 décharge cette obligation plus forte.

## 2. Ce que les antériorités donnent, et le sens de la densité

Les codages finis Terras/Everett sont utilisés dans les deux PR. Les résultats
de densité sur **l'ensemble des départs** n'imposent pas une fréquence à
chaque orbite exceptionnelle individuelle. La heuristique de bits indépendants
ne peut être appliquée à une telle orbite fixée sans preuve.

Le dépôt externe figé
[`msharpe248/collatz`](https://github.com/msharpe248/collatz/tree/ec8174b567d5cab4960024782210b5f5db02bd3a)
contient `Shadow.lean`, notamment `density_floor`, `OrbitSummability.lean`,
`NoncontractingTail.lean` et `paper/orbit_summability.tex`.
Les sources ont été relues statiquement, sans compilation nouvelle.
La contrainte classique sur une orbite échappante va dans le sens

\[
 \liminf\frac{\#\text{impairs}}t\ge1/\delta,
 \quad\text{donc}\quad \limsup E(t)/t\le\beta/\delta.
\]

C'est une **borne supérieure** sur les pairs, pas la borne inférieure cherchée.
La formulation interprétative « densité critique » ne démontre pas une égalité.
L'existence d'une queue dont le coefficient ne contracte jamais ne fournit
pas non plus la borne inférieure (C).

Le texte `orbit_summability.tex`, section bibliographique, attribue une
estimation quantitative de rareté des valeurs d'une orbite à Garcia–Tal,
*A note on the generalized 3n+1 problem*, Acta Arith. 90 (1999), 245–250,
[DOI](https://doi.org/10.4064/aa-90-3-245-250). Il en déduit la sommabilité des
inverses ; **densité de Banach nulle seule ne suffirait pas**. La preuve
élémentaire de la section suivante est reconstruite ici pour ne pas dépendre
de l'importation de ce théorème ou d'un artefact Lean.

Limite de recherche bibliographique : les accès directs à
[Terras](https://doi.org/10.4064/aa-30-3-241-252),
[Everett](https://doi.org/10.1016/0001-8708(77)90087-1),
[Garcia–Tal](https://doi.org/10.4064/aa-90-3-245-250),
[la bibliographie Lagarias](https://arxiv.org/abs/math/0309224),
[Tao](https://arxiv.org/abs/1909.03562) et
[la discussion citée par le dépôt](https://mathoverflow.net/questions/513539)
ont tous renvoyé un tunnel HTTP 403. Nous ne certifions donc ni un état de
l'art exhaustif, ni l'absence d'un résultat antérieur impliquant (C).
« Question ouverte ici » ne signifie pas « priorité mondiale de la formulation
contrôlée ». Aucune source accessible relue n'a fourni la borne inférieure (C).

## 3. Renforcement démontré : coefficient logarithmique critique avec reste borné

**Théorème conditionnel.** Toute orbite positive entière non bornée vérifie

\[
 \boxed{p_N(L)\ge\frac L\beta+c_*\log_2 L-C_N}
 \quad\text{pour L assez grand, avec une constante finie }C_N.       \tag{4}
\]

C'est plus précis que (3), mais la pente demeure **exactement 1/β**.
L'ingrédient supplémentaire est un reste R uniformément borné.

### 3.1 Sommabilité reconstruite par empaquetage fini

Soit O l'ensemble des valeurs d'une orbite non bornée. Pour tout k, T^k est
injective sur O : si T^k(n_i)=T^k(n_j), i<j, on obtient une répétition d'états
aux temps i+k et j+k, contradiction.

Un mot de longueur k à q impairs, de positions i_0<…<i_(q−1), a correction

\[
 D=\sum_{h=0}^{q-1}2^{i_h}3^{q-1-h}
 \le2^{k-q}(3^q-2^q),                                      \tag{5}
\]

car i_h≤k−q+h. Pour un départ n<2^k réalisant ce mot, l'identité affine donne
`T^k(n)<2·3^q`.

Appliquer cela à S=O∩[0,32^m), k=5m. Les q≤3m ont des images dans
[0,2·27^m), donc sont au nombre d'au plus 2·27^m par injectivité.
Pour q>3m, la bijection classique des parités sur les résidus modulo 2^(5m)
et le binôme donnent

\[
 \#\{n\in S:q>3m\}
 \le\sum_{q>3m}\binom{5m}q
 \le 2^{-3m}\sum_q2^q\binom{5m}q=(243/8)^m.
\]

Ainsi `|S|≤2·27^m+(243/8)^m`. Sur la coquille [32^m,32^(m+1)),
la somme des inverses est donc au plus

\[
 54(27/32)^m+(243/8)(243/256)^m.
\]

Les deux séries géométriques convergent, d'où, en utilisant l'injectivité
**en temps** pour ne pas perdre les multiplicités,

\[
 \sum_{t\ge0}1/n_t\le C_0:=1728/5+7776/13=61344/65.         \tag{6}
\]

L'argument ne s'appliquerait pas à un cycle : la somme sur ses valeurs
distinctes est finie, la série en temps diverge.

### 3.2 Reste borné et inversion au coefficient exact

Par `log(1+u)≤u`, (6) implique

\[
 0\le R(t)\le C_0/\log 2.                                  \tag{7}
\]

Combiner (1), (2), (7). Avec `a=δ/log₂δ`, il existe une constante A_N telle que

\[
 H(t)\le\beta t-a\log_2t+A_N\quad(t\ge1).                  \tag{8}
\]

Pour une constante D_N assez grande, choisir
`t_L=floor(L/β+(a/β)log₂L−D_N)`.
Comme `log₂t_L=log₂L−log₂β+o(1)`, le membre droit de (8) est ≤L en t_L.
Il est éventuellement croissant en t ; les temps initiaux restants sont
absorbés en prenant L assez grand. Tous les états de temps 0…t_L sont donc
<2^L, distincts, et donnent des facteurs distincts. Cela prouve (4).

Cette démonstration réutilise un empaquetage déjà décrit dans le dépôt
externe et des ingrédients classiques. Elle ne revendique ni le premier
théorème de sommabilité, ni une priorité du raffinement (4).

## 4. La conjecture est exactement un déficit de croissance orbitale

Définir `h_N=limsup H(t)/t`. Par (2) et (7),

\[
 \boxed{h_N=\beta-\delta\eta_N,\qquad
 \eta_N=\liminf E(t)/t.}                                   \tag{9}
\]

Ainsi (C) équivaut à `h_N<β` pour chaque orbite non bornée : on ne gagne rien
en l'appelant simplement « amélioration de hauteur ».

On a 0≤h_N≤β et donc η_N≤β/δ. Plus précisément, (2) et (7) donnent aussi la
borne supérieure classique `E(t)≤(β/δ)t+O_N(1)`, compatible avec η_N=0.

Si η_N>0 et h_N>0, le même argument de hauteur donne

\[
 \liminf_{L\to\infty}p_N(L)/L\ge1/h_N>1/\beta.
\]

Si h_N=0, pour chaque ε>0 on a éventuellement H(t)≤εt ; l'argument donne
`liminf p_N(L)/L=+∞`. Le cas η_N=β/δ n'exclut donc pas automatiquement une
orbite non bornée à croissance sous-exponentielle. Une valeur η_N>β/δ serait
incompatible avec (9). Sans borne inférieure **uniforme** sur η_N, il n'y a
pas de gain numérique uniforme pour toutes les orbites.

## 5. Représentants canoniques : exclusion effective d'un mot clairsemé

Pour un mot w de longueur t, soit r_t son représentant dans [0,2^t), déterminé
par `3^q r_t+D(w)≡0 (mod 2^t)`. La cohérence des préfixes donne

\[
 r_{t+1}\in\{r_t,r_t+2^t\}.                                \tag{10}
\]

La suite r_t est donc non décroissante. Un mot infini correspond à un entier
**non négatif** fixé si et seulement si r_t est bornée, donc se stabilise.
Pour un entier positif N, la stabilisation est à N dès que 2^t>N.
Le cas limite 0 est le mot tout pair et doit être séparé.
Les représentants d'un entier **négatif**, par exemple −1, peuvent croître
sans borne ; (10) ne prouve pas l'irrationalité 2-adique.

### 5.1 Une borne finie sensible aux pas pairs antérieurs

Pour tout entier positif, un pas impair multiplie n+1 par 3/2. Si n est pair,
n≥2 et `(T(n)+1)/(n+1)=(n+2)/(2(n+1))≤2/3`.
Donc pour toute trajectoire entière positive, sans hypothèse de divergence,

\[
 n_s+1\le(N+1)(3/2)^{s-2E(s)}.                             \tag{11}
\]

Si le mot prescrit ensuite r≥1 pas impairs, `2^r | n_s+1`.
Le préfixe contient alors un bit 1, donc son représentant canonique est
strictement positif. Appliquer (11) à ce représentant, pour la longueur s+r :

\[
 \boxed{r_{s+r}+1\ge2^r(2/3)^{s-2E(s)}.}                   \tag{12}
\]

Cette assertion utilise la **réalisation entière** du préfixe canonique ;
elle n'est pas une estimation probabiliste de résidus.

### 5.2 Un mot infini à densité de pairs nulle, mais sans graine positive

Commencer par huit 1. Poser s_0=8, puis pour i≥0 définir

\[
 k_i=\lfloor\beta s_i-i\rfloor,\qquad
 s_{i+1}=s_i+k_i+1,
\]

et concaténer à partir de s_i le bloc `1^(k_i)0`.
Comme β>1/2, on a par induction s_i≥8+2i et k_i≥1. De plus,

\[
 s_{i+1}\ge\delta s_i-i
 \ge(\beta+1/2)s_i+4,
\]

donc s_i croît exponentiellement. La borne opposée `s_(i+1)≤δs_i+1`
donne aussi s_i≤Cδ^i pour une constante C. E(s_i)=i et la densité E(t)/t tend
vers 0, y compris entre les fins de blocs ; E(t) est de l'ordre de log t.

Ce mot satisfait les contraintes grossières `k_i≤βs_i` et E(t)≫log t ; le
seul majorant initial de #22 ne l'élimine pas. Pourtant (12) donne

\[
 r_{s_i+k_i}+1
 \ge2^{\beta s_i-i-1}(2/3)^{s_i-2i}
 =\tfrac12(9/8)^i\longrightarrow\infty.                    \tag{13}
\]

Par (10), aucun entier positif fixé ne réalise ce mot. Chaque préfixe fini
est néanmoins réalisable par une infinité d'entiers positifs dans sa classe,
et le mot entier possède une unique réalisation dans Z₂ par cohérence des
classes. **Existence 2-adique et réalisation entière positive sont distinctes.**
L'éventuelle rationalité de cette réalisation 2-adique n'est pas tranchée ici.

C'est une exclusion structurelle d'une famille précise de runs presque
maximaux, pas une preuve de (C) et pas une amélioration générale de pente.
Des runs bien plus courts, par exemple k_i=i, échappent à (12).

## 6. Obstacle démontré à la seule relaxation archimédienne

Il serait incorrect de conclure (C) de (1), de l'identité de hauteur, du reste
borné et de la seule conséquence de divisibilité `r≤log₂(n+1)`.
Un modèle explicite satisfait ces propriétés et a densité de branches paires 0.

Prescrire les blocs `1^i0`, i=1,2,…, et partir du réel x_0=257. À un bit 1,
appliquer la fonction affine (3x+1)/2, et à un bit 0 appliquer x/2,
**sans demander la parité du réel courant**. Ce n'est pas l'application T
sur les entiers.

Soit u_i=x+1 au début du i-ème bloc, Q_(i−1)=i(i−1)/2. On a exactement

\[
 u_{i+1}=\frac{3^i}{2^{i+1}}u_i+\frac12,
 \qquad
 \log_2u_i\ge\log_2 258+\beta Q_{i-1}-(i-1).
\]

Puisque log₂258>8 et β>1/2,

\[
 \log_2u_i-i>
 (i^2-9i+36)/4>0.
\]

Ainsi chaque run satisfait sa borne de taille i≤log₂u_i. Pour i≥2, les débuts
de blocs croissent au moins géométriquement de facteur 9/8 ; la somme des
inverses sur chaque bloc est au plus quatre fois l'inverse de son premier
état. La série totale des inverses et le reste R sont donc bornés.
L'identité (2) reste exacte pour ces branches affines réelles. Or après m
blocs, le temps est m(m+3)/2 et E=m : E(t)/t→0 et H(t)/t→β.

La faute de réalisation est visible sans calcul massif :
`257 → 386 → 193 → 290`, puis la quatrième branche prescrite est impaire et
donne 871/2, alors que 290 est pair. Le modèle n'a pas les divisibilités
2-adiques de la vraie trajectoire. Les identités de récurrence modulo 3^k,
interprétées sur ces rationnels à dénominateur puissance de 2, ne réparent
pas cette perte : 2 est inversible modulo 3^k.

**Portée exacte de l'obstacle :** les seules estimations archimédiennes
énumérées ne peuvent imposer une densité inférieure positive. Cela ne condamne
ni les contraintes intégrales complètes, ni une preuve croisée réelle/2-adique.
Le modèle n'est pas un contre-exemple à (C).

## 7. Ce qui demeure non démontré et prochaine expérience mathématique

L'implication encore manquante est : pour **tout** mot de parités d'une orbite
positive fixée avec `liminf E(t)/t=0`, forcer la non-stabilisation des r_t,
ou obtenir directement un déficit strict h_N<β. La borne (12) règle certains
runs presque maximaux, mais pas des pairs rares répartis beaucoup plus
régulièrement. Une fréquence nulle le long d'une sous-suite est également
plus générale que la limite nulle du mot construit en section 5.

**Prochaine expérience mathématique précise, une seule :** traiter le mot
triangulaire `w=10 110 1110 11110…`, par une preuve de non-stabilisation des
représentants, et non par un recensement prolongé. Il satisfait E(t)/t→0,
mais ses runs i sont trop courts pour (12).

Le problème arithmétique exact est le suivant. Poser

\[
 Q_m=m(m+1)/2,\quad \tau_m=Q_m+m,\quad
 C_m=\sum_{j=1}^m2^{Q_j+j-1}3^{Q_m-Q_j}.
\]

Pour un entier positif fixé N réalisant tous les blocs et le bit impair qui
suit le m-ème bloc, il faudrait, pour **tout** m,

\[
 2^{\tau_m+1}\mid3^{Q_m}(N+1)+C_m.                         \tag{14}
\]

Cette formule vient de la récurrence en x=n+1 ; le +1 dans le module impose
l'imparité du minimum suivant. Pour chaque m elle détermine une unique classe
N modulo 2^(τ_m+1). L'expérience consiste à démontrer ou réfuter que ces
représentants non négatifs tendent vers l'infini. Une preuve doit fournir
un argument de valuations/non-stabilisation pour tous les m ; de nouveaux
préfixes numériques seuls ne suffiraient pas.

La série 2-adique correspondante est
`N+1=−sum_(j≥1) 2^(Q_j+j−1)/3^Q_j`. Bien qu'elle converge aussi dans R,
sa somme réelle négative **ne prouve pas** que sa somme 2-adique ne soit pas
un entier positif : les deux limites ne peuvent être identifiées sans
théorème supplémentaire. Ce raccourci a même un contre-exemple exact :
poser `a_j=2^(2^j)/(1+2^(2^j))`. La série de termes rationnels négatifs
`3 sum_(j≥0)(a_j−a_(j+1))` converge dans R vers −1, mais dans Q₂ vers
l'entier positif 2, car a_j→1 dans R et a_j→0 dans Q₂. Le signe de la limite
réelle n'impose donc pas celui d'un éventuel entier somme 2-adique.

Le simple argument « entier non nul plus petit que le diviseur » échoue aussi
pour (14). Si S est la somme réelle positive des termes
`2^(Q_j+j−1)/3^Q_j`, alors, pour N fixé positif,

\[
 \frac{3^{Q_m}(N+1)+C_m}{2^{\tau_m}}
 \sim(N+1+S)(3/2)^{Q_m}2^{-m}\longrightarrow+\infty.
\]

La taille archimédienne laisse largement la place à un multiple du module.
Il faudrait un argument effectif sur la **valuation**, pas seulement la taille.
La non-réalisation de ce seul mot resterait un résultat restreint, pas (C),
et n'augmenterait pas à elle seule la pente universelle de complexité.

## 8. Vérification exécutée et bilan

Le programme original de #22 a été **réellement relancé depuis sa tête** :

```sh
python3 research/parity_log_gain_checks.py
```

Toutes les assertions passent : 65 792 contrôles de hauteur, 32 880 de runs
impairs, 65 536 contrôles rationnels du nombre de pairs et 860 identités
Mersenne. Ce sont des contrôles de régression des ingrédients finis, pas une
validation expérimentale des orbites non bornées ou des limites.
Aucune nouvelle compilation Lean, aucun calcul massif, aucun nouveau script
numérique publié. Les nouveaux résultats reposent sur les preuves ci-dessus.

**Bilan net :** (4), (12)–(13) et l'obstacle de la section 6 sont démontrés
avec leur portée exacte. La conjecture (C) reste non résolue dans ce travail ;
aucun théorème général dépassant la pente 1/β n'est obtenu. L'antériorité
scientifique des raffinements n'est pas établie.
