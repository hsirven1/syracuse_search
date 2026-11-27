# Cycle 005 — Horizon d'un certificat à poids borné

Date : 26 novembre 2026. Axe **A**.
Branche : `research/memory`. Script : [`../checks/cycle005_certificate_horizon.py`](../checks/cycle005_certificate_horizon.py).

**Verdict : PROUVÉ pour $K\le3/2$ ; l'obstruction locale sans ce seuil est RÉFUTÉE ; l'implication globale de H6 reste OUVERTE.**
Si $0<\ell\le W\le h$ et $0<\rho<1$ vérifient $K=\rho h/\ell\le3/2$, toute
contraction de $2^L-1$ ($L\ge2$) attend un temps $t$ tel que
$3\cdot2^t>2\cdot3^L$. Donc $B(2^L-1)\ge\delta L-\log_2(3/2)$, avec
$\delta=\log_2 3$. La forme d'abord écrite, $5\cdot2^t>2\cdot3^L$, en
découle. Si $K>3/2$, cette borne sur les Mersenne est fausse : le poids
de X21 contracte chaque Mersenne en un pas. X21 ne réfute pas l'implication
initiale de H6, qui demande un certificat pour tout entier. Ni (C), ni
Syracuse. Le coefficient de tête est celui de la montée de Mersenne ; il
est inférieur à la borne d'Applegate–Lagarias (2003) sur le temps d'arrêt
total. Ce cycle n'en refait pas la preuve par arbres.

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
$0<\ell\le W(n)\le h$ et $0<\rho<1$, on pose $\Phi(n)=n\,W(n)$ et
$K=\rho h/\ell$. Un temps de contraction de $n$ est un entier $t\ge1$ tel
que $\Phi(T^t(n))\le\rho\,\Phi(n)$. Un horizon $B$ est admissible pour $n$
lorsqu'un tel $t$ vérifie $t\le B(n)$. On écrit $H(n)=\log_2(n+1)$,
$\beta=\log_2(3/2)$ et $\delta=\log_2 3=1+\beta$. Si $\rho\le0$, alors
$\Phi(T^t(n))\ge\ell\,T^t(n)>0\ge\rho\,\Phi(n)$ pour tout $t\ge1$ et tout
$n\ge1$ : aucune contraction n'existe.

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

Pour $K>0$ et $L\ge1$, la différence
$(K+1)2^L-\bigl(K(2^L-1)+1\bigr)$ vaut $2^L+K-1$. Ce nombre est
strictement positif. Si $K\ge1$, il est au moins $2^L$. Si $0<K<1$, il
reste supérieur à $2^L-1\ge1$, et la comparaison avec $2^L$ échoue. Pour
$L=2$ et $K=1/2$, la différence vaut $7/2$, tandis que
$K(2^L-1)+1=5/2<(K+1)2^L=6$. Ainsi, si $y\le K(2^L-1)$, alors
$$H(y)\le\log_2(y+1)\le\log_2\bigl(K(2^L-1)+1\bigr)<L+\log_2(K+1).$$

## 5. Borne sous le seuil (B10)

**Proposition.** Soient $0<\ell\le W\le h$, $0<\rho<1$, $K=\rho h/\ell\le3/2$,
$L\ge2$ et $t$ un temps de contraction de $n_0=2^L-1$. Alors
$3\cdot2^t>2\cdot3^L$. Par suite $t>\delta L-\log_2(3/2)$ et tout horizon
admissible vérifie
$$B(2^L-1)\ge\delta L-\log_2(3/2).$$
La forme $5\cdot2^t>2\cdot3^L$, donc $t>\delta L-\log_2(5/2)$, en découle :
$5\cdot2^t>3\cdot2^t$.

Le §3 interdit $t\le L$. On écrit $t=L+s$ avec $s\ge1$ et
$y=T^t(n_0)=T^s(3^L-1)$. Pour tout $x\ge1$, $T(x)\ge x/2$, avec égalité
lorsque $x$ est pair. Donc $y\ge(3^L-1)/2^s$. La contraction donne
$y\,W(y)\le\rho\,n_0\,W(n_0)$. Comme $W(y)\ge\ell$ et $W(n_0)\le h$,
$y\le K n_0$. On en tire
$$K\cdot2^t\ge2^L\frac{3^L-1}{2^L-1}.$$
Or $2^L(3^L-1)-3^L(2^L-1)=3^L-2^L>0$, donc le membre de droite est
strictement supérieur à $3^L$, et $K\cdot2^t>3^L$. Avec $K\le3/2$,
$$\frac32\cdot2^t\ge K\cdot2^t>3^L,$$
soit $3\cdot2^t>2\cdot3^L$. Ainsi
$t>\log_2(2\cdot3^L/3)=\delta L-\log_2(3/2)$. Un horizon admissible est au
moins égal à cet entier $t$, donc au moins égal au nombre réel
$\delta L-\log_2(3/2)$.

L'estimation de hauteur du §4, une fois la différence $2^L+K-1$ écrite
sans la comparaison fausse avec $2^L$, donne la borne plus faible qui avait
été écrite en premier. Elle utilise $H(y)>\delta L-s$ et
$H(y)<L+\log_2(K+1)$, d'où $t>\delta L-\log_2(K+1)$. Pour $K\le3/2$,
$K+1\le5/2$, donc $t>\delta L-\log_2(5/2)$ et $5\cdot2^t>2\cdot3^L$.
La constante $\log_2(3/2)$ n'est pas présentée comme optimale : l'écart
$3^L-2^L$ est strict.

Pour $L=2$, $3\cdot2^2=12<18=2\cdot3^2$, donc $t\le2$ est exclu, et
l'orbite de $3$ vérifie $2y\le3\cdot3$ pour la première fois à $t=3$
($y=4$). Pour $L=4$, $3\cdot2^5=96<162=2\cdot3^4$, et le retour a lieu à
$t=6$ ($y=20$). Pour $L=6$, $3\cdot2^8=768<1458=2\cdot3^6$, et le retour
a lieu à $t=9$ ($y=91$).

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
retourne : $2^{L-1}\ge(K-1)/(2K-3)$. Cette condition est nécessaire et
suffisante pour $x\le Kn$ lorsque le poids vaut $h$ au départ et $\ell$ à
l'arrivée. Pour tout $L$ assez grand, $x\le K n$. L'image n'est pas un
Mersenne, comme ci-dessus. Le poids vaut donc $h$ en $n$ et $\ell$ en $x$,
et $x\ell\le K n=\rho n h$. Le temps $t=1$ contracte tous ces Mersenne. Le
seuil $3/2$ est exact pour cette obstruction locale, au sens asymptotique.
Cette construction ne fournit pas un certificat pour tous les entiers :
seulement pour les Mersenne.

## 7. Applegate–Lagarias, 2003

L'énoncé lu est arXiv:math/0103054, introduction jusqu'au théorème 1.1.
La preuve par arbres jusqu'à la profondeur $60$ n'a pas été refaite. Leur
application (1) est le $T$ de ce cycle, et leur $\log$ est le logarithme
naturel : ils écrivent $\gamma(3)=5/\log3\approx4{,}5512$.

Leur formule (4) dit que le temps d'arrêt total des Mersenne vérifie
$$\gamma(2^k-1)=\frac{\sigma_\infty(2^k-1)}{\log(2^k-1)}\ge\frac{\log2+\log3}{(\log2)^2}\approx3{,}729.$$
Après $k$ pas on est à $3^k-1$. Chaque pas vérifie $T(x)\ge x/2$, donc
atteindre $1$ demande encore au moins $\log_2(3^k-1)$ pas. La phrase
d'abord écrite, $\log_2(3^k)$, est fausse pour $k=2$ : $8\to4\to2\to1$ en
trois pas, et $\log_2 9>3$. L'article retient ce cas : $3^k-1$ ne rejoint
pas $1$ plus vite qu'une puissance de $2$, ce qui a lieu pour $k=2$. Le
coefficient de (4) reste correct pour $k\ge2$. Soit $p=\log_2 3>1$ et
$N=2^k\ge4$. Pour $0<u<1$, $(1-u)^p<(1-u)$, donc
$N^p-(N-1)^p>N^{p-1}\ge2^{p-1}=3/2>1$, et $(2^k-1)^p<3^k-1$. Ainsi
$\log_2(3^k-1)>p\log_2(2^k-1)$. Comme $k>\log_2(2^k-1)$,
$$k+\log_2(3^k-1)>(1+p)\log_2(2^k-1).$$
Le temps total est au moins le membre de gauche. Divisé par
$\log(2^k-1)=\log_2(2^k-1)\cdot\log2$, le quotient dépasse
$(\log2+\log3)/(\log2)^2$. L'inégalité large de (4) en résulte. Le
coefficient de B10, ramené au même quotient par $\log n$, tend vers
$\log3/(\log2)^2$. La différence avec le coefficient de (4) est $1/\log2$ :
les numérateurs diffèrent de $\log2$, et le dénominateur commun est
$(\log2)^2$. Leur (4) borne le temps d'atteinte de $1$ ; B10 borne le
premier retour sous $K n$ avec $K\le3/2$. Le théorème 1.1 du même article,
qu'ils présentent comme une amélioration de (4), donne
$\sigma_\infty(n)>6{,}14316\log n$ pour une infinité de $n$, avec le
coefficient exact $29/(29\log2-14\log3)$, par une autre famille. Cette
comparaison n'a pas été recalculée ici. Le théorème 1.1, la recherche
d'arbres et le théorème Lean `no_finite_certificate` ne sont pas des
prémisses de B10. Rien dans ce cycle n'améliore ces bornes.

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

X21 ne dit pas qu'un certificat global peut prendre $B=1$ sur les Mersenne.
L'énoncé initial de H6 demandait un temps de contraction pour chaque
$n\ge N_0$, puis $B(n)\ge\delta\log_2 n-O(1)$ pour une infinité de $n$.
Le poids de X21 certifie seulement les Mersenne. Il réfute l'obstruction
locale sans seuil, et l'esquisse « tout poids borné doit traverser le
sommet $3^L$ ». Avec $K\le3/2$, la constante $O(1)$ de cette esquisse peut
être prise égale à $\log_2(3/2)$, et la borne vaut pour tout $L\ge2$.
L'implication globale, elle, reste ouverte.

Le contrôle $2\le L\le30$ du script retrouve le premier retour sous
$(3/2)(2^L-1)$ et la comparaison $3\cdot2^t>2\cdot3^L$. Il ne remplace
pas le §5. Les ascensions $L\le40$ et le contre-exemple $L\le80$ sont des
vérifications des identités déjà prouvées, sur un segment fini. Le cas
$L=2$, $K=1/2$ contrôle que $2^L+K-1$ est positif et strictement inférieur
à $2^L$. L'orbite $8\to4\to2\to1$ contrôle la phrase corrigée du §7.

## 9. Prochaine question

Axe **B**, frontière de Tschakaloff (H5). Pour le mot à un zéro par bloc
dont le $j$-ième run impair vaut $r_j=j+[j\text{ impair}]$, la réalisation
2-adique est-elle une combinaison $\mathbb Q$-linéaire de deux valeurs de
Tschakaloff, et l'un des énoncés de Bézivin, de Bundschuh ou
d'Amou–Väänänen l'exclut-il de $\mathbb Z_{(2)}$ ? Lire l'énoncé avant
toute preuve : l'obstruction $\Gamma(2,0)<\gamma$ de Väänänen–Wallisser
doit être vérifiée sur le théorème cité, pas seulement rappelée.

## 10. Revue `6081843230`

Revue indépendante sur le SHA `ebba3309f617204d844c241d84c5442af3e35c85`
(PR #27). B10, sous la forme $5\cdot2^t>2\cdot3^L$, et le certificat X21
sont confirmés. Trois corrections de portée sont intégrées ci-dessus ; la
prochaine question du §9 n'est pas entamée.

La comparaison $2^L+K-1\ge2^L$ du §4 est fausse pour $0<K<1$. Pour $L=2$
et $K=1/2$, la différence vaut $7/2<4$, et $5/2<6$ conserve l'inégalité de
hauteur. L'hypothèse s'écrit $0<\rho<1$ : si $\rho\le0$, le membre de
gauche de la contraction est positif et le membre de droite ne l'est pas.
La descente $T(x)\ge x/2$ renforce la borne en $3\cdot2^t>2\cdot3^L$, donc
$t>\delta L-\log_2(3/2)$. La forme $5\cdot2^t>2\cdot3^L$ en découle.

X21 est une réfutation locale. L'image d'un Mersenne vérifie
$T(n_0)+1=3\cdot2^{L-1}$, donc le poids de l'exemple y vaut $1$. L'écart
$5n_0-3T(n_0)=2^{L-1}-2$ est positif pour $L>2$ et nul pour $L=2$, où
$3\to5$. Pour $K>3/2$, la condition de contraction en un pas, avec poids
$h$ au départ et $\ell$ à l'arrivée, est $2^{L-1}\ge(K-1)/(2K-3)$. Le seuil
$3/2$ est exact pour cette obstruction, au sens asymptotique. L'implication
initiale de H6, un certificat pour chaque $n\ge N_0$, n'est pas réfutée.

La formule (4) d'Applegate–Lagarias a été relue sur le HTML ar5iv de
arXiv:math/0103054, de l'introduction au théorème 1.1. Après le sommet, le
nombre de pas est au moins $\log_2(3^k-1)$. Pour $k=2$, ce nombre est $3$.
Le coefficient $(\log2+\log3)/(\log2)^2$ suit de
$(2^k-1)^{\log_2 3}<3^k-1$ et de $k>\log_2(2^k-1)$, pour $k\ge2$. Le
théorème 1.1 et la recherche d'arbres jusqu'à la profondeur $60$ ne sont
pas des prémisses de B10 ; cette recherche n'a pas été refaite.

Contrôles indépendants, en arithmétique entière : pour $2\le L\le120$, le
premier $t$ tel que $2T^t(2^L-1)\le3(2^L-1)$ vérifie $t>L$ et
$3\cdot2^t>2\cdot3^L$. Les retours $L=2,4,6$ sont $t=3,6,9$, avec images
$4$, $20$ et $91$. Le script Python a été exécuté : cinq lignes `PASS`.

## 11. Revue `6081884788`

Revue indépendante sur le SHA `0b935a943b7972fa3998ac98b2c53fcc6772ea5b`
(PR #27), c'est-à-dire sur les corrections du §10. B10 sous la forme
$3\cdot2^t>2\cdot3^L$, la comparaison $2^L+K-1>0$, le certificat local
X21 et le décompte $\log_2(3^k-1)$ sont confirmés. L'implication globale
de H6 reste ouverte, comme le texte le disait déjà. Aucune correction.
La question du §9 est traitée ensuite, dans le cycle 006. Ce n'est pas
une seconde preuve de B10.
