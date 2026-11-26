# Runs impairs successifs : obstruction exacte et réduction vers un gain log-log

**Conclusion : la conjecture de densité reste ouverte dans ce travail et la
pente 1/log₂(3/2) n'est pas dépassée.** Un lemme intermédiaire trop fort est
réfuté sur de vraies trajectoires entières finies. Une amélioration en log-log
de la borne de complexité est démontrée **sous une borne p-adique uniforme
explicitement isolée**, non certifiée ici sur le texte original de Yu.
Aucune nouveauté scientifique ni preuve de Syracuse n'est revendiquée.

Cette reprise ne réédite pas le seul gain logarithmique des PR #21–22.
Sources figées : [#21](https://github.com/hsirven1/syracuse_search/pull/21),
`4b2a31e262e4fdf3b6dc26588e71a3b7e04bb9a7`, et
[#22](https://github.com/hsirven1/syracuse_search/pull/22),
`57d894cbff791d7c8084a1d04affbee52a22ae47`.
Branche : `research/padic-successive-runs`, issue de #22.

## 1. Contrôle des résultats acquis et formulation exacte de la cible

T(n)=n/2 si pair, (3n+1)/2 sinon ; n_t=T^t(N),
E(t)=nombre de pas pairs avant t,
δ=log₂3, β=δ−1, λ=log₂δ.
Le comptage p_N(L) concerne tout l'itinéraire infini.

L'argument de #21 est correct :
`n_s+1≤(N+1)(3/2)^s`, absence de répétition sur une orbite non bornée,
puis bijection parités/résidus modulo 2^L. Il donne
`p_N(L)≥1+floor((L−K)/β)` quand N+1≤2^K.

L'argument de #22 est également correct. La divisibilité des runs donne
`E(t)≥log₂t/λ−O_N(1)`. L'identité

\[
 H(t):=\log_2(n_t+1)=H(0)+\beta t-\delta E(t)+R(t),
 \quad R(t)=\sum_{s<t,\ n_s\text{ pair}}
       \log_2(1+1/(n_s+1))                                  \tag{1}
\]

avec R=o(E) permet l'inversion annoncée, en contrôlant tout le préfixe par
une enveloppe éventuellement croissante. La conclusion ne change pas la pente.

La [reprise précédente](https://github.com/hsirven1/syracuse_search/blob/a5eea5bd789f4b9956f7cf27c3ffb2d1088b3957/research/EVEN_DENSITY_STRUCTURAL_AUDIT.md)
renforce R=o(E) en R=O(1), d'où

\[
 p_N(L)\ge L/\beta+c_*\log_2 L-O_N(1),
 \quad c_*=\delta/(\beta\lambda).                          \tag{2}
\]

Ce fait est indépendant d'une invocation de Väänänen–Wallisser : l'application
à f_(3/2)(2) de la PR #24 reste non vérifiée et n'est utilisée nulle part ici.

Pour rappeler pourquoi le reste est borné sans hypothèse de fréquence :
T^k est injective sur l'ensemble O des valeurs d'une orbite non bornée.
Pour n<2^k et q impairs, l'identité affine et la correction extrémale donnent
T^k(n)<2·3^q. En séparant q≤3m et q>3m à k=5m, la bijection des parités et
le binôme donnent
`|O∩[0,32^m)|≤2·27^m+(243/8)^m`. La somme des inverses sur les coquilles
[32^m,32^(m+1)) est donc majorée par
`54(27/32)^m+(243/8)(243/256)^m`. Ainsi
`sum_t 1/n_t≤61344/65`, et `R(t)≤61344/(65 log 2)`.
Les détails de cet empaquetage sont dans la reprise citée, §3.

La conjecture demandée est **orbitale** : pour chaque N positif non borné,
`η_N=liminf E(t)/t>0`. Une constante indépendante de N serait plus forte.
Par (1) et R=O(1),

\[
 \limsup H(t)/t=\beta-\delta\eta_N.                         \tag{3}
\]

Si 0<η_N<β/δ, la pente conditionnelle est au moins
`1/(β−δη_N)>1/β`. Si η_N=β/δ, le même argument donne une complexité
superlinéaire. La valeur >β/δ est impossible ; la borne classique sur les
impairs donne au contraire une borne **supérieure** sur la fréquence des pairs.

Terras/Everett et Tao portent notamment sur des ensembles de départs : ils
ne fournissent pas par simple changement de quantificateur (3) avec η_N>0.
Le dépôt externe figé `ec8174b567d5cab4960024782210b5f5db02bd3a`,
`Shadow.lean:density_floor`, donne le sens critique opposé ;
`OrbitSummability.lean` donne la sommabilité, pas une densité inférieure positive.
Le renvoi à Garcia–Tal (Acta Arith. 90 (1999), 245–250) dans le texte externe
concerne un comptage des **valeurs** de l'orbite. Ces densités ne sont pas
la fréquence temporelle des parités. Le contrôle d'antériorité complet de
l'énoncé recherché reste non établi : les originaux antérieurement demandés
n'ont pas été obtenus, et aucun nouveau résultat de densité orbitale n'est
certifié ici à partir d'un résumé.

## 2. Une vraie contrainte reliant deux runs, sans logarithme approché

Découper la trajectoire après chaque pas pair, y compris deux pas pairs
consécutifs. Soit s_i le temps immédiatement après i pas pairs, s_0=0,
et M_i=n_(s_i). Poser

\[
 r_i=v_2(M_i+1),\quad a_i=(M_i+1)/2^{r_i}\text{ impair},
 \quad x_i=\log_2(M_i+1),\quad b_i=\log_2 a_i=x_i-r_i.
\]

Si M_i est pair, r_i=0. Sinon r_i est exactement le nombre de pas impairs
consécutifs avant le prochain pas pair. Tous ces blocs existent pour une
orbite positive, par la divisibilité des runs ; (1) de #22 impose une
infinité de pas pairs. On a

\[
 s_{i+1}=s_i+r_i+1,\qquad
 \boxed{M_{i+1}+1=(3^{r_i}a_i+1)/2},\qquad
 \boxed{r_{i+1}+1=v_2(3^{r_i}a_i+1)}.                       \tag{4}
\]

L'égalité de valuation vaut aussi pour r_i=0. L'argument de croissance seul
ne voit pas cette relation entre deux paquets.
Comme l'état avant le pas pair est ≥2, son terme correctif logarithmique
est <1. Par conséquent

\[
 x_{i+1}\le x_i+\beta r_i=\delta x_i-\beta b_i,
 \qquad x_i\le\delta^i x_0.                                \tag{5}
\]

Le problème est donc de contrôler la partie impaire a_i, pas seulement r_i≤x_i.

## 3. Contre-exemple entier à un renforcement local trop fort

Le lemme tentant suivant est faux, quelle que soit la constante C :

> Pour tout r≥1 et tout a impair positif,
> `v₂(3^r a+1)≤C(1+log₂a)`.

**Famille infinie exacte.** Fixer a=5. Pour chaque m≥3, il existe un exposant
r_m positif tel que

\[
 3^{r_m}5\equiv-1\pmod{2^m}.                               \tag{6}
\]

En effet, l'ordre de 3 modulo 2^m est 2^(m−2). Par
`v₂(3^(2^k)−1)=k+2` pour k≥1, cet ordre est exact. Le sous-groupe engendré
par 3 est précisément l'ensemble des unités congrues à 1 ou 3 modulo 8 :
il y est inclus et a le même cardinal. Or `−5⁻¹≡3 mod8`.
On choisit r_m dans [1,2^(m−2)−1] ; il est impair.

Le départ entier positif

\[
 N_m=5\cdot2^{r_m}-1
\]

a r_m pas impairs, puis un pas pair, puis au moins m−1 pas impairs.
Cela suit de (4) et (6). Le second run n'est donc pas borné en fonction de
la seule taille de a, pourtant constante égale à 5.
Par exemple r=5 donne N=159, un premier run de longueur 5, le pas pair vers
607, puis un run de longueur 5 puisque 607+1=2^5·19.

Cela contraste avec a=1 : `v₂(3^r+1)≤2`, donc le run suivant a longueur ≤1.
Le cas Mersenne ne représente pas toutes les petites parties impaires.

**Ce n'est pas un contre-exemple à la conjecture.** Les N_m varient et tendent
vers l'infini dans R : r_m→∞, car chaque exposant borné a une valuation finie
dans (6). Mais N_m→−1 dans Z₂. Leurs préfixes finissent donc par être
arbitrairement longs tout-impairs ; leur limite est le mot tout impair,
réalisé par −1, pas par un entier positif fixé. Un argument de compacité dans
Z₂ ne rétablit pas la positivité entière.

Cet obstacle est démontré sur des trajectoires **entières finies**, sans
échantillonnage ni affirmation de divergence. Il interdit de supprimer
l'entière dépendance en r d'un contrôle uniforme de (4).

## 4. Entrée p-adique précise : ce qui reste à contrôler sur la source

Le lemme uniforme utile est la proposition suivante :

\[
 \boxed{\exists C\ge1\ \forall r\ge1\ \forall a\ge1\text{ impair},\quad
 v_2(3^r a+1)\le C(1+\log_2a)\log_2(2+r).}                \tag{V}
\]

La croissance du **nombre de facteurs premiers de a** ne doit pas faire
croître C. Une borne seulement pour chaque a fixé, avec une constante
incontrôlée C_a, ne suffit pas à la démonstration suivante.

(V) est de la forme des conséquences usuelles des bornes de formes
logarithmiques p-adiques de K. Yu, *p-adic logarithmic forms and group
varieties. III*, Forum Math. 19(2) (2007), 187–280. Pour une tentative
rigoureuse de spécialisation, la forme non nulle est
`Θ−1=−3^r a−1`, avec les nombres −1, 3, a et les exposants 1,r,1.
Les a puissances de 3 se traitent directement par le cas précédent.
Sinon 3 et a sont multiplicativement indépendants, et toutes les bases
sont des unités 2-adiques. La hauteur de a est log a.

**Source effectivement lue :** la documentation et le code
[SageMath 10.6, S_unit_solver.py](https://github.com/sagemath/sage/blob/10.6/src/sage/rings/number_field/S_unit_solver.py),
fonctions `Yu_condition_115`, `Yu_modified_height`, `Omega_prime`, `Yu_bound`,
et la [bibliographie de cette version](https://github.com/sagemath/sage/blob/10.6/src/doc/en/reference/references/index.rst).
Le code renvoie au théorème 1 de Yu, pp.189–193, et décrit une borne
`ord_p(Θ−1)<c₈ log B`.

**Hypothèse cachée identifiée dans cette piste :** le code ne considère pas
que la condition (1.15) soit automatiquement satisfaite sur Q à p=2. Il passe
à l'extension quadratique engendrée par une racine cubique primitive de l'unité.
Le champ Q(ζ₃), de degré fixé 2, est donc à prendre en compte dans l'audit,
ainsi que les hauteurs modifiées. Utiliser un groupe de S-unités complet dont
le rang dépend de a serait une autre erreur : le nombre de nombres algébriques
dans la forme doit rester fixé.

**Limite décisive :** le PDF original de Yu n'a pas été obtenu ; l'accès
arXiv:1903.00977 de l'article d'implémentation et les accès éditeur essayés
renvoient HTTP 403. Sage est ici une **source secondaire**, pas une lecture du
théorème publié. Nous ne déclarons donc pas l'instanciation (V) certifiée.
Le gain log-log qui suit est explicitement conditionnel à (V). Aucune borne
en log²r ne peut être substituée silencieusement : elle ne donne pas le même
gain par le produit harmonique utilisé ci-dessous.

## 5. Proposition démontrée sous (V) : un gain effectif en log-log

**Proposition.** Sous (V), il existe une constante universelle d>0 telle que
chaque orbite positive entière non bornée vérifie, pour L assez grand,

\[
 \boxed{p_N(L)\ge L/\beta+c_*\log_2L
                  +d\log_2\log_2L-O_N(1).}                 \tag{7}
\]

La pente n'est toujours pas améliorée ; le gain log-log diverge et est donc
strictement plus fort que (2). La preuve complète de l'implication est donnée,
pas une conjecture fondée sur des préfixes calculés.

### 5.1 Déficit de hauteur sur deux blocs

Pour r_i≥1, (4) et (V) donnent, avec L_i=log₂(2+x_i),

`r_(i+1)≤C(1+b_i)L_i`.

Pour r_i=0, on a directement
`r_(i+1)+1=v₂(a_i+1)≤log₂(a_i+1)≤b_i+1` ; la même majoration est valable.
Dans une orbite non bornée, M_i→∞, donc x_i→∞.
On peut supposer `CL_i≤x_i/4` en omettant un nombre fini de blocs.

- Si `b_i≥x_i/(4CL_i)`, appliquer (5) deux fois :
  `x_(i+2)≤δ²x_i−δβx_i/(4CL_i)`.
- Sinon `r_(i+1)≤CL_i+x_i/4≤x_i/2`, puis
  `x_(i+2)≤x_(i+1)+βr_(i+1)≤(δ+β/2)x_i`.

Les deux cas impliquent, avec `a₀=β/(4Cδ)>0`,

\[
 x_{i+2}\le\delta^2x_i(1-a_0/L_i).                          \tag{8}
\]

Dans le deuxième cas, cela utilise seulement
`δ/(4CL_i)≤δ−1/2`, vraie pour C≥1, L_i≥1.

### 5.2 Accumulation du déficit et temps ordinaire

Par (5), `L_i≤iλ+log₂(2+x₀)≤2iλ` pour i assez grand.
Par (8), sur chacune des deux parités de i,

\[
 x_{i+2}\le\delta^2x_i(1-a_0/(2\lambda i)).
\]

Prendre les logarithmes naturels et utiliser `log(1-u)≤−u`.
La somme de 1/i sur une parité vaut `(1/2)log i+O(1)`. D'où

\[
 x_i\le A_N\delta^i/(i+1)^\kappa,
 \qquad \kappa=a_0/(4\lambda)>0.                            \tag{9}
\]

Pour e=E(t), le dernier bloc peut être inachevé. Comme r_i≤x_i,
`t≤sum_(i=0..e)(x_i+1)`. La somme géométrique pondérée de (9) donne

\[
 t\le B_N\delta^e/(e+1)^\kappa.                             \tag{10}
\]

Pour justifier ce passage sans monotonie supposée des x_i : après le changement
j=e−i, utiliser `(e−j+1)(j+1)≥e+1` et la convergence de
`sum_(j≥0)(j+1)^κ δ^(−j)`. Le terme e+1 s'absorbe également dans le majorant.

L'inversion de (10), puis `e≥log₂t/λ−O_N(1)`, donnent

\[
 E(t)\ge\frac{\log_2t}{\lambda}
       +\frac\kappa\lambda\log_2\log_2t-O_N(1).             \tag{11}
\]

### 5.3 Retour à la complexité

Par (1), R=O(1) et (11),

\[
 H(t)\le\beta t-\frac\delta\lambda\log_2t
                 -\frac{\delta\kappa}\lambda\log_2\log_2t+O_N(1).
\]

Cette enveloppe est éventuellement croissante. Choisir
`t_L=floor(L/β+c_*log₂L+d log₂log₂L−D_N)`, avec
`d=δκ/(βλ)>0`, puis D_N assez grand. Les logarithmes de t_L diffèrent de
ceux de L par une constante au premier ordre et par o(1) au second.
Tous les états de temps 0…t_L sont <2^L, en absorbant les temps initiaux.
Ils sont distincts, et leurs facteurs de longueur L le sont également.
Ainsi `p_N(L)≥t_L+1`, ce qui prouve (7) **sous (V)**.

## 6. Pourquoi ce progrès ne prouve pas la densité positive

Même (11) ne donne que des nombres de pairs logarithmiques. Si
`s_e=sum_(i<e)(r_i+1)`, on a exactement, avec la convention 1/∞=0,

\[
 \liminf_t E(t)/t
 =\frac1{\limsup_{e\to\infty}s_e/e}.
\]

Pour les temps à l'intérieur d'un bloc, utiliser `s_e≤t<s_(e+1)` ; le décalage
d'indice ne change pas le limsup. La densité positive requiert donc une
**moyenne bornée des longueurs r_i**, pas seulement un ralentissement de leur
enveloppe exponentielle en i. Nous ne présentons pas cette reformulation
comme un nouveau petit lemme suffisant.

Le modèle réel à branches prescrites `1^i0` de la reprise précédente montre
pourquoi les estimations de hauteur seules restent insuffisantes. Son temps
après e blocs est quadratique, sa densité de branches paires tend vers zéro,
et ses parties impaires réelles ont une hauteur quadratique ; elles satisfont
largement les inégalités de taille du type (V), sans être les parties impaires
entières des vraies trajectoires. Ce n'est ni une trajectoire de T sur N ni un
contre-exemple à (V) ou à la conjecture.

Pour un mot infini, les représentants canoniques vérifient
`ρ_(t+1)∈{ρ_t,ρ_t+2^t}`. Une réalisation par un entier non négatif fixé équivaut
à leur stabilisation. Le cas tout pair correspond à zéro, et les entiers
négatifs peuvent avoir des représentants croissants. Les familles de §3 ne
fournissent aucune stabilisation positive. Aucun argument ici n'exclut tous
les mots à liminf E(t)/t=0 ; cette propriété peut d'ailleurs ne valoir que sur
une sous-suite de temps, plus générale que les mots clairsemés réguliers.

## 7. Vérifications et conclusion exacte

Le programme de #22 a été relancé dans cette branche, sans modification :

```sh
python3 research/parity_log_gain_checks.py
```

PASS : 65 792 contrôles de hauteur, 32 880 de runs impairs, 65 536 contrôles
rationnels de pairs, 860 identités Mersenne. Ces calculs ne testent ni (V)
ni (7). Les nouvelles propositions reposent sur les démonstrations ci-dessus.
Pas de nouveau balayage, pas de compilation Lean, pas de script numérique
publié. Les sources antérieures restent intactes.

**Théorème négatif démontré :** la borne locale indépendante de r du §3 est
fausse sur une famille infinie de véritables préfixes entiers positifs.
**Proposition conditionnelle démontrée :** (V) implique (7), avec une constante
d>0 universelle. **Question restante ouverte :** la densité inférieure positive,
et donc l'objectif de dépasser réellement la pente 1/β.
Aucune antériorité scientifique des déductions nouvelles n'est établie.

**Prochaine expérience mathématique précise :** établir (ou réfuter) la
spécialisation uniforme (V) à partir du théorème 1 de Yu (2007), avec un nombre
fixé de bases, le champ fixe Q(ζ₃), la place au-dessus de 2 et les hauteurs
modifiées. Il faut démontrer que la constante finale est indépendante de a
hors du facteur `1+log₂a` et que l'exposant du logarithme en r est bien 1.
C'est le test contradictoire décisif pour transformer (7) en résultat
inconditionnel sous la seule hypothèse d'orbite non bornée ; prolonger des
préfixes numériques ou invoquer une transcription secondaire ne le ferait pas.
