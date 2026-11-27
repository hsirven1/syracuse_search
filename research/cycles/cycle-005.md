# Cycle 005 — Horizon d'un certificat à poids borné

Date : 26 novembre 2026. Axe **A**.
Branche : `research/memory`. Script : [`../checks/cycle005_certificate_horizon.py`](../checks/cycle005_certificate_horizon.py).

**Verdict : PROUVÉ sous une hypothèse de rapport, et RÉFUTÉ sans elle.**
Si $0<\ell\le W\le h$ et $\rho<1$ vérifient $K=\rho h/\ell\le3/2$, toute
contraction de $2^L-1$ ($L\ge2$) attend un temps $t$ tel que
$5\cdot2^t>2\cdot3^L$. Donc $B(2^L-1)\ge\delta L-\log_2(5/2)$, avec
$\delta=\log_2 3$. Si $K>3/2$, cette borne universelle est fausse : le poids
de X21 contracte chaque Mersenne en un pas. Ni (C), ni Syracuse. Le
coefficient de tête est celui de la montée de Mersenne ; il est inférieur
à la borne d'Applegate–Lagarias (2003) sur le temps d'arrêt total, que ce
cycle ne refait pas.

## 0. Question traitée

Première entrée de l'agenda, après la revue `6081702521` sur le SHA
`7120654`. Cette revue confirme le cycle 004 et ne demande aucune
correction ; elle est enregistrée au §15 du cycle 004 et dans `reviews.md`.
L'agenda demande une constante explicite $C$ telle que
$B(2^L-1)\ge\delta L-C$ pour tout $L$ assez grand, ou bien un triplet
$(\ell,h,\rho)$ et un horizon $B(n)=o(\log n)$ qui contractent tous les
Mersenne. Dépendances utilisées : la forme close de l'ascension (A2),
reprouvée ci-dessous pour que le texte se lise seul. Le théorème Lean
`no_finite_certificate` (A5) exclut un horizon fixe ; il ne donne pas la
croissance en $L$.

## 1. Notation

$T(n)=n/2$ si $n$ est pair, $(3n+1)/2$ si $n$ est impair. Pour
$0<\ell\le W(n)\le h$ et $\rho<1$, on pose $\Phi(n)=n\,W(n)$ et
$K=\rho h/\ell$. Un temps de contraction de $n$ est un entier $t\ge1$ tel
que $\Phi(T^t(n))\le\rho\,\Phi(n)$. Un horizon $B$ est admissible pour $n$
lorsqu'un tel $t$ vérifie $t\le B(n)$. On écrit $H(n)=\log_2(n+1)$,
$\beta=\log_2(3/2)$ et $\delta=\log_2 3=1+\beta$.

## 2. Ascension

Pour $L\ge1$ et $0\le t\le L$, $T^t(2^L-1)=3^t\,2^{L-t}-1$.

À $t=0$ les deux membres valent $2^L-1$. Si la formule vaut pour un
$t<L$, l'entier $x=3^t\,2^{L-t}-1$ est impair, car $L-t\ge1$. Alors
$$T(x)=\frac{3x+1}2=\frac{3^{t+1}\,2^{L-t}-2}2=3^{t+1}\,2^{L-t-1}-1.$$
En $t=L$ on obtient $3^L-1$. C'est A2.

Pour $1\le t\le L$, ce terme $x$ vérifie $x/(2^L-1)>(3/2)^t$. En effet
$$x\cdot2^t-3^t(2^L-1)=3^t-2^t>0.$$

## 3. Le seuil $3/2$

**Proposition.** Si $K\le3/2$ et $1\le t\le L$, alors $t$ n'est pas un
temps de contraction de $n_0=2^L-1$.

Le §2 donne $x=T^t(n_0)>(3/2)^t n_0\ge(3/2)n_0\ge K n_0$. Comme
$W(x)\ge\ell>0$,
$$x\,W(x)\ge x\ell>K n_0\ell=\rho h\,n_0\ge\rho\,W(n_0)\,n_0.$$
L'inégalité est stricte même à $t=1$ et $K=3/2$, parce que le rapport du
§2 est strictement supérieur à $3/2$.

En particulier, au sommet $s=0$ : $2(3^L-1)-3(2^L-1)=2\cdot3^L-3\cdot2^L+1$.
Pour $L\ge2$, $2\cdot3^L\ge3\cdot2^L$, car $(2/3)(3/2)^L\ge(2/3)\cdot(9/4)=3/2>1$.
Donc $3^L-1>(3/2)(2^L-1)\ge K(2^L-1)$. Le pas $t=L$ ne contracte pas non
plus.

## 4. Hauteur

Pour $n\ge1$, $H(T(n))>H(n)-1$. Si $n$ est impair,
$T(n)+1=3(n+1)/2$, donc $H(T(n))=H(n)+\beta$. Si $n$ est pair,
$T(n)+1=(n+2)/2$, donc $H(T(n))=\log_2(n+2)-1>\log_2(n+1)-1$. Après
$s\ge1$ pas, $H(T^s(n))>H(n)-s$.

Pour $K>0$ et $L\ge1$, $K(2^L-1)+1<(K+1)2^L$, car la différence vaut
$2^L+K-1\ge2^L\ge2$. Ainsi, si $y\le K(2^L-1)$, alors
$$H(y)\le\log_2(y+1)\le\log_2\bigl(K(2^L-1)+1\bigr)<L+\log_2(K+1).$$

## 5. Borne sous le seuil (B10)

**Proposition.** Soient $K\le3/2$, $L\ge2$ et $t$ un temps de contraction
de $2^L-1$. Alors $5\cdot2^t>2\cdot3^L$. Par suite
$t>\delta L-\log_2(5/2)$ et tout horizon admissible vérifie
$$B(2^L-1)\ge\delta L-\log_2(5/2).$$

Le §3 interdit $t\le L$. On écrit $t=L+s$ avec $s\ge1$ et
$y=T^t(2^L-1)=T^s(3^L-1)$. Le §4 donne $H(y)>\delta L-s$. La contraction
entraîne $y\le K(2^L-1)$, donc $H(y)<L+\log_2(K+1)$. En combinant,
$\delta L-s<L+\log_2(K+1)$, c'est-à-dire
$s>\beta L-\log_2(K+1)$ et $t>\delta L-\log_2(K+1)$. Comme $K+1\le5/2$,
$$t>\delta L-\log_2(K+1)\ge\delta L-\log_2(5/2)=\log_2(2\cdot3^L/5).$$
Donc $2^t>2\cdot3^L/5$, soit $5\cdot2^t>2\cdot3^L$. Un horizon admissible
est au moins égal à cet entier $t$, donc au moins égal au nombre réel
$\delta L-\log_2(5/2)$.

La forme entière est celle qui sert. La constante additive $\log_2(5/2)$
en est une majoration commode ; elle n'est pas présentée comme optimale.
Pour $L=6$, $5\cdot2^8=1280<1458=2\cdot3^6$, donc $t\le8$ est exclu, et
l'orbite de $63$ vérifie $2y\le3\cdot63$ pour la première fois à $t=9$.
Pour $L=4$, $5\cdot2^5=160<162=2\cdot3^4$, et le retour a lieu à $t=6$.

## 6. Au-dessus du seuil (X21)

**Proposition.** Pour $\ell=1$, $h=2$ et $\rho=5/6$, on a $K=5/3>3/2$.
Le poids $W(2^L-1)=2$ pour $L\ge2$, et $W=1$ ailleurs, contracte chaque
$2^L-1$ au temps $t=1$. L'horizon constant $B=1$ est $o(\log n)$ sur cette
famille.

Ici $T(2^L-1)=3\cdot2^{L-1}-1$. L'entier $3\cdot2^{L-1}$ est divisible
par $3$ et strictement supérieur à $2$, donc ce n'est pas une puissance
de $2$ : l'image n'est pas un Mersenne, et $W$ y vaut $1$. L'écart
$$5(2^L-1)-3\bigl(3\cdot2^{L-1}-1\bigr)=2^{L-1}-2$$
est positif pour $L>2$ et nul pour $L=2$. Donc
$T(n)\cdot W(T(n))\le(5/6)\,n\cdot W(n)$, avec égalité en $L=2$. Le pas
$t=1$ est un temps de contraction, et $B(2^L-1)=1$ est admissible pour
toute cette famille.

Le seuil $3/2$ ne peut pas être relevé. Si $K>3/2$, on prend $\ell=1$,
$\rho=1/2$ et $h=2K$, de sorte que $\rho h/\ell=K$. Pour un Mersenne
$n=2^L-1$ et son image $x=3\cdot2^{L-1}-1$,
$$
\frac x n\le K
\iff 2^{L-1}(3-2K)\le1-K.
$$
Les deux facteurs $3-2K$ et $1-K$ sont négatifs, donc l'inégalité se
retourne : $2^{L-1}\ge(K-1)/(2K-3)$. Pour tout $L$ assez grand, $x\le K n$.
L'image n'est pas un Mersenne, comme ci-dessus. Le poids vaut donc $h$ en
$n$ et $\ell$ en $x$, et $x\ell\le K n=\rho n h$. Le temps $t=1$ contracte
tous ces Mersenne. Cette construction ne fournit pas un certificat pour
tous les entiers : seulement pour les Mersenne.

## 7. Applegate–Lagarias, 2003

L'énoncé lu est arXiv:math/0103054, introduction jusqu'au théorème 1.1.
La preuve par arbres jusqu'à la profondeur $60$ n'a pas été refaite. Leur
application (1) est le $T$ de ce cycle, et leur $\log$ est le logarithme
naturel : ils écrivent $\gamma(3)=5/\log3\approx4{,}5512$.

Leur formule (4) dit que le temps d'arrêt total des Mersenne vérifie
$$\frac{\sigma_\infty(2^k-1)}{\log(2^k-1)}\ge\frac{\log2+\log3}{(\log2)^2}\approx3{,}729,$$
parce qu'après $k$ pas on est à $3^k-1$, puis qu'il faut encore au moins
$\log_2(3^k)$ pas pour atteindre $1$. Le coefficient de B10, ramené au
même quotient par $\log n$, tend vers $\log3/(\log2)^2$. La différence avec
le coefficient de (4) est $1/\log2$ : les numérateurs diffèrent de $\log2$,
et le dénominateur commun est $(\log2)^2$. Leur (4) borne le temps d'atteinte
de $1$ ; B10 borne le premier retour sous $K n$ avec $K\le3/2$. Le théorème 1.1
du même article, qu'ils présentent comme une amélioration de (4), donne
$\sigma_\infty(n)>6{,}14316\log n$ pour une infinité de $n$, par une autre
famille. Cette comparaison n'a pas été recalculée ici. Rien dans ce cycle
n'améliore ces bornes.

Conway (1972) et Kurtz–Simon (2007) restent le garde-fou déjà noté dans
`prior_art.md` : l'argument n'utilise que la forme close de cette
application $T$, pas un procédé de décision pour une application
généralisée.

## 8. Portée

B10 est une condition nécessaire sur les Mersenne lorsque $K\le3/2$. Il
n'existe dans ce cycle aucun poids pour lequel la contraction serait
prouvée pour tout entier. S'il existait un horizon $B$, même très grand,
tel que chaque $n\ge N_0$ admette un temps de contraction, la relation
$\Phi\le\rho\Phi$ ferait entrer toute orbite dans $\{1,\ldots,N_0-1\}$ :
sinon $\Phi$ descendrait indéfiniment tout en restant au moins $\ell$.
Vérifier ensuite le segment fini initial serait une forme de la conjecture.
Ce texte n'en construit pas.

X21 ne dit pas non plus qu'un certificat global peut prendre $B=1$ sur les
Mersenne. Il dit que l'obstruction de l'ascension disparaît dès que
$K>3/2$ : le récit « tout poids borné doit traverser le sommet $3^L$ »
demande l'hypothèse $K\le3/2$. H6, lu sans cette hypothèse, est réfuté.
Avec elle, la constante $O(1)$ de l'esquisse est $\log_2(5/2)$, et la
borne vaut pour tout $L\ge2$, pas seulement pour une infinité de $L$.

Le contrôle $2\le L\le30$ du script retrouve le premier retour sous
$(3/2)(2^L-1)$ et la comparaison $5\cdot2^t>2\cdot3^L$. Il ne remplace
pas le §5. Les ascensions $L\le40$ et le contre-exemple $L\le80$ sont des
vérifications des identités déjà prouvées, sur un segment fini.

## 9. Prochaine question

Axe **B**, frontière de Tschakaloff (H5). Pour le mot à un zéro par bloc
dont le $j$-ième run impair vaut $r_j=j+[j\text{ impair}]$, la réalisation
2-adique est-elle une combinaison $\mathbb Q$-linéaire de deux valeurs de
Tschakaloff, et l'un des énoncés de Bézivin, de Bundschuh ou
d'Amou–Väänänen l'exclut-il de $\mathbb Z_{(2)}$ ? Lire l'énoncé avant
toute preuve : l'obstruction $\Gamma(2,0)<\gamma$ de Väänänen–Wallisser
doit être vérifiée sur le théorème cité, pas seulement rappelée.
