# Cycle 008 — Horizon global d'un certificat pondéré

Date : 27 novembre 2026. Axe **A**.
Branche : `research/memory`. Script : [`../checks/cycle008_weighted_horizon.py`](../checks/cycle008_weighted_horizon.py).

**Verdict : l'implication globale de H6 est PROUVÉE pour tout facteur $K>0$.**
Si $0<\ell\le W\le h$, $0<\rho<1$ et si tout entier $n\ge N_0$ admet un temps
$t\le B(n)$ avec $T^t(n)\,W(T^t(n))\le\rho\,n\,W(n)$, alors
$$
B(n)>\log_2 3\cdot\log_2 n-C
$$
pour une infinité de $n$, où $C$ ne dépend que de $K=\rho h/\ell$ et de $\rho$.
La branche « exhiber un poids et un horizon $o(\log n)$ » est impossible.
Ce n'est pas une preuve de Syracuse. Pour $K\le3/2$, le témoin est le
Mersenne et la borne directe est $t>\delta L-\log_2 K$ ; B10 n'en garde
que la forme uniforme en $\log_2(3/2)$. X21 ne contredit pas l'énoncé :
ce poids ne certifie pas tous les entiers.

## 0. Question traitée

Première entrée de l'agenda, après la revue `6082099628` sur le SHA
`eeaeb41ff7f030cd5b0c59715e2614e56f1243ed`. Cette revue confirme le
correctif X23 et l'inégalité de premier retour. Elle est enregistrée au
§7. Elle observe que la question alors écrite dans l'agenda et au cycle
007 §8 a pour prémisse $T^t(n)\le\rho n$. Cette prémisse est le cas
$W\equiv1$, $K=\rho<1$, de l'estimation du cycle 005 §5. Le §1 la
redonne en une page, pour fermer cette formulation. L'énoncé initial de
H6 est la contraction de $\Phi(n)=n\,W(n)$. C'est l'objet du §3. Le mot
du cycle 006 n'est pas rouvert. Conway 2000 et Kadison 1957 ne sont pas
lus.

## 1. Le cas sans poids, déjà dans le cycle 005

Soient $0<\rho<1$, $L\ge2$ et $n_0=2^L-1$. Si $T^t(n_0)\le\rho\,n_0$, alors
$t>L$ et $\rho\cdot2^t>3^L$. Donc $t>\log_2 3\cdot L-\log_2\rho$.

Pour $1\le t\le L$, le cycle 005 §2 donne $T^t(n_0)>(3/2)^t n_0\ge(3/2)n_0$.
Comme $\rho<1<3/2$, ce temps ne satisfait pas $T^t(n_0)\le\rho\,n_0$. On écrit
$t=L+s$ avec $s\ge1$ et $y=T^s(3^L-1)$. Chaque pas vérifie $T(x)\ge x/2$, donc
$y\ge(3^L-1)/2^s$. La contraction donne $(3^L-1)/2^s\le y\le\rho(2^L-1)$, d'où
$$
\rho\cdot2^t\ge2^L\frac{3^L-1}{2^L-1}.
$$
Or $2^L(3^L-1)-3^L(2^L-1)=3^L-2^L>0$, donc le membre de droite est
strictement supérieur à $3^L$, et $\rho\cdot2^t>3^L$.

C'est l'estimation du cycle 005 §5 spécialisée à $K=\rho\le3/2$, sous la
forme directe annoncée par la revue, plutôt que sous la forme plus faible
$3\cdot2^t>2\cdot3^L$. Un horizon admissible pour tous les entiers est en
particulier admissible pour les Mersenne. Aucun $B(n)=o(\log n)$ ne satisfait
la prémisse non pondérée. Cette prémisse n'est pas H6 : le poids n'y figure
pas, et la clause qui demandait d'exhiber un poids ne portait sur aucune
quantité de l'hypothèse.

## 2. Notation

$T(n)=n/2$ si $n$ est pair, $(3n+1)/2$ si $n$ est impair. Pour
$0<\ell\le W(n)\le h$ et $0<\rho<1$, on pose $\Phi(n)=n\,W(n)$ et
$K=\rho h/\ell$. Un temps de contraction de $n$ est un entier $t\ge1$ tel
que $\Phi(T^t(n))\le\rho\,\Phi(n)$. Il entraîne $T^t(n)\le K n$, car
$\ell\,T^t(n)\le\Phi(T^t(n))\le\rho\,n\,W(n)\le\rho h\,n$. On pose
$\delta=\log_2 3$.

Pour $L\ge1$ et $0\le j\le L$,
$$
n_j=3^j\,2^{L-j}-1.
$$
La suite est la montée de $n_0=2^L-1$ : si $j<L$, $n_j$ est impair et
$T(n_j)=n_{j+1}$. Pour $1\le t\le L-j$,
$$
2^t\,T^t(n_j)-3^t\,n_j=3^t-2^t>0,
$$
donc $T^t(n_j)>(3/2)^t n_j$. Le calcul est celui du cycle 005 §2, avec
le départ $3^j$ à la place de $1$.

## 3. Potentiel le long de la montée

**Lemme.** Soit $\Psi(j)=\Phi(n_j)\,2^j/3^j$. Pour $0\le j\le L$,
$$
\ell(2^L-1)\le\Psi(j)<h\,2^L.
$$
Si $t\ge1$, $j+t\le L$ et $\Phi(n_{j+t})\le\rho\,\Phi(n_j)$, alors
$$
\Psi(j+t)\le\rho\,(2/3)^t\,\Psi(j)\le(2\rho/3)\,\Psi(j).
$$

Le membre de droite de la première inégalité : $n_j<3^j\,2^{L-j}$, donc
$\Psi(j)\le h\,n_j\,2^j/3^j<h\,2^L$. Le membre de gauche :
$$
\Psi(j)\ge\ell\,(3^j\,2^{L-j}-1)\,2^j/3^j=\ell\bigl(2^L-2^j/3^j\bigr).
$$
Comme $2^j/3^j\le1$, ceci est au moins $\ell(2^L-1)$. L'égalité de cette
dernière comparaison n'a lieu qu'en $j=0$.

La seconde inégalité est la définition de $\Psi$ et le facteur $\rho$.
Pour $t\ge1$, $(2/3)^t\le2/3$.

## 4. Bornes entières sur une contraction qui reste dans la montée

Posons $m_*$ le plus petit entier $\ge1$ tel que
$$
\Bigl(\frac{3}{2\rho}\Bigr)^{m_*}\ge\frac{2K}{\rho}=\frac{2h}{\ell},
$$
et $t_*$ le maximum de $\{0\}\cup\{t\text{ entier}\ge1:(3/2)^t<2K\}$.
Si $2K\le3/2$, le second ensemble est vide et $t_*=0$. Si $K\le1/2$,
l'ensemble $\{t\ge0:(3/2)^t<2K\}$ est lui-même vide, y compris à
l'égalité $2K=1$, puisque $(3/2)^0=1$. Le maximum qui contient $0$ est
alors la convention du lemme : l'ancienne formule, « le plus grand
$t\ge0$ », ne désigne rien. L'entier $J=(m_*-1)\,t_*$ ne dépend que de
$K$ et de $\rho$.

**Lemme.** Une contraction de $n_j$ dont l'image est encore un $n_{j+t}$
avec $t\ge1$ et $j+t\le L$ vérifie $t\le t_*$. Au plus $m_*-1$ telles
contractions peuvent se suivre.

S'il existait une telle contraction de longueur $t$, le §3 donnerait
$\ell(2^L-1)\le\Psi(j+t)<\rho\,(2/3)^t\,h\,2^L$, donc
$(3/2)^t<K\cdot2^L/(2^L-1)$. Pour $L\ge1$, $2^L/(2^L-1)\le2$, et
$(3/2)^t<2K$. Donc $t\le t_*$.

Partant de $\Psi(j_0)<h\,2^L$, chaque contraction de la chaîne multiplie
$\Psi$ par au plus $2\rho/3$. Après $m$ contractions,
$\Psi<\bigl(2\rho/3\bigr)^m h\,2^L$. Le minorant $\ell(2^L-1)$ donne
$$
\Bigl(\frac{3}{2\rho}\Bigr)^m<\frac{h\,2^L}{\ell(2^L-1)}\le\frac{2h}{\ell}.
$$
La dernière comparaison est $2^L\le2(2^L-1)$, vraie pour $L\ge1$, et
l'inégalité qui la précède est stricte à cause de $\Psi<h\,2^L$. Pour
$m\ge m_*$, le membre de gauche est au moins $2h/\ell$. Contradiction.
La chaîne compte donc au plus $m_*-1$ sauts, chacun de longueur au plus
$t_*$.

Pour $K\le3/2$, le §2 interdit déjà toute contraction avec $t\le L-j$ :
$T^t(n_j)>(3/2)^t n_j\ge(3/2)\,n_j\ge K n_j$. Le premier sommet est
$j_*=0$, et $J$ n'est qu'une majoration. Le critère $(3/2)^t<2K$ est
plus lâche que la comparaison directe à $K$ : $t_*$ peut être positif
alors qu'aucun saut n'existe. Sur le Mersenne, l'estimation du §5
donne $t>\delta L-\log_2 K$. La preuve de
B10 contient déjà $K\cdot2^t>3^L$ (cycle 005 §5) et n'en retient, dans
l'énoncé, que la conséquence uniforme $t>\delta L-\log_2(3/2)$, égale
au seuil $K=3/2$ et plus faible en dessous.

Le seuil $3/4$ sépare les deux constantes. On a $m_*=1$ si et seulement
si $3/(2\rho)\ge2K/\rho$, c'est-à-dire $K\le3/4$, et $t_*=0$ dans le
même cas. Donc $J=0$ et $C=\log_2 K\le\log_2(3/4)<\log_2(3/2)$. Si
$K>3/4$, alors $m_*\ge2$ et $t_*\ge1$, donc $J\ge1$ et
$C\ge\log_2 K+(\log_2 3)^2>\log_2(3/4)+(\log_2 3)^2$. Or
$\log_2(3/4)+(\log_2 3)^2-\log_2(3/2)=-1+(\log_2 3)^2>0$,
car $3>2$. Donc $C>\log_2(3/2)$. Pour
$h=\ell$ et $\rho=1/4$, on est dans le premier cas : $K=1/4$,
$t_*=0$, $J=0$ et $C=-2$. Sur $n=2^L-1$, $L\ge2$,
$$
\delta\log_2 n-C-(\delta L-\log_2(3/2))>\delta(\log_2 n-(L-1))>0,
$$
puisque $2^L-1>2^{L-1}$ et $C=-2=\log_2(3/2)-\delta-1$. La borne
uniforme de B10 est alors la plus faible.

## 5. L'implication globale (B13)

**Proposition.** Soient $0<\ell\le W\le h$, $0<\rho<1$ et $K=\rho h/\ell$.
Soit $C=\log_2 K+J\,(\log_2 3)^2$, avec $J$ comme au §4. Comme $K>0$,
ce logarithme est défini ; il est négatif lorsque $K<1$. L'écriture
$\log_2(2K)$ majore cette constante d'exactement une unité. Si une fonction
$B$ vérifie : tout entier $n\ge N_0$ admet un temps de contraction
$t\le B(n)$, alors, pour une infinité de $n$,
$$
B(n)>\delta\log_2 n-C.
$$

Soit $L>\max(J,1)$ assez grand pour que $2^L-1\ge N_0$. La montée
$(n_j)_{0\le j\le L}$ est strictement croissante, donc chaque terme est
au moins $N_0$ et possède un temps de contraction.

On construit des indices $0=j_0<j_1<\cdots$ tant qu'il existe un entier
$t$ avec $1\le t\le L-j_r$ tel que $\Phi(T^t(n_{j_r}))\le\rho\,\Phi(n_{j_r})$.
Pour un tel temps, l'image est $n_{j_r+t}$, encore dans la montée, sommet
inclus. On choisit le plus petit $t$ et l'on pose $j_{r+1}=j_r+t$. Le §4
arrête la construction avant $m_*$ sauts, à un indice $j_*\le J<L$. Au
point $n=n_{j_*}$, aucune contraction n'a donc une longueur $t$ avec
$1\le t\le R$, où $R=L-j_*\ge1$ : aucune contraction jusqu'au sommet
inclus. Le procédé ne contrôle pas un retour ultérieur de l'orbite sur
la liste $(n_j)$. Tout temps de contraction, que l'orbite y revienne ou
non, vérifie $t>R$.

Soit $t=R+s$ un tel temps, $s\ge1$. Alors $T^R(n)=3^L-1$ et
$y=T^s(3^L-1)\ge(3^L-1)/2^s$. La contraction donne $y\le K n$, donc
$$
K\cdot2^t\ge2^R\frac{3^L-1}{n}.
$$
Comme $n=3^{j_*}\,2^R-1$ et $L=j_*+R$,
$$
2^R(3^L-1)-3^R n=3^R-2^R>0.
$$
Le quotient est strictement supérieur à $3^R$, et $K\cdot2^t>3^R$. Ainsi
$t>\delta R-\log_2 K$. Par ailleurs $n<3^{j_*}\,2^R$, donc
$\log_2 n<R+j_*\delta$ et $\delta\log_2 n<\delta R+j_*\delta^2$. Comme
$j_*\le J$,
$$
t>\delta R-\log_2 K>\delta\log_2 n-J\delta^2-\log_2 K=\delta\log_2 n-C.
$$
Tout horizon admissible vérifie $B(n)\ge t$, donc $B(n)>\delta\log_2 n-C$.

Pour chaque $L$ assez grand, l'entier $n$ ainsi obtenu dépend de $L$ et
vérifie $n\ge2^{L-J}-1$. La suite tend vers l'infini. Il y a donc une
infinité de tels entiers. La constante $C$ ne dépend pas de $L$, ni du
choix de $W$ à l'intérieur des bornes $\ell$ et $h$.

Pour $\rho=5/6$ et $K=5/3$, les entiers du §4 sont $m_*=3$, $t_*=2$ et
$J=4$ : $(9/5)^2=81/25<4$ et $(9/5)^3=729/125\ge4$, tandis que
$(3/2)^2=9/4<10/3$ et $(3/2)^3=27/8>10/3$. Ce couple est celui de X21.
Le poids de X21 contracte chaque Mersenne en un pas, mais $W=1$ sur le
successeur $3\cdot2^{L-1}-1$, qui n'est pas un Mersenne, et sur toute la
montée restante. Le §2 y interdit la contraction jusqu'au sommet. X21
n'est pas un contre-exemple à B13.

## 6. Ce que ce cycle ne montre pas

- La conjecture, ni l'existence d'un certificat global. S'il en existe
  un, itérer $\Phi\le\rho\Phi$ fait entrer l'orbite dans un segment
  fini, comme le cycle 005 §8 le disait déjà. Ce texte n'en construit pas.
- Un remplacement de B10. Pour $K\le3/2$ le témoin du §5 est le
  Mersenne, et $t>\delta L-\log_2 K$ est déjà dans la preuve du cycle
  005 §5. L'énoncé de B10 n'en garde que la forme uniforme. Cette
  forme est plus faible que $C$ lorsque $K\le3/4$, et plus forte
  lorsque $3/4<K\le3/2$, parce que $J\ge1$ (cycle 008 §4).
- Le coefficient d'Applegate–Lagarias 2003 sur le temps d'atteinte de
  $1$. B13 borne le premier temps de contraction de $\Phi$, pas
  $\sigma_\infty$. Le théorème 1.1 et la recherche d'arbres ne sont pas
  relus. `no_finite_certificate` (A5) exclut seulement un horizon fixe ;
  sa preuve n'est pas une prémisse, le rapport d'audit en a fixé la
  portée.
- Rien sur le mot du cycle 006, ni sur la phrase du cycle 007 §4 rappelée
  au §7.

## 7. Revue `6082099628`

Revue indépendante sur le SHA
`eeaeb41ff7f030cd5b0c59715e2614e56f1243ed` (PR #27), c'est-à-dire sur le
correctif X23. Trois points.

La relecture des barres dans la source arXiv v2, aux numéros HTML 3.4.4,
4.2.2 et 4.2.3, est confirmée. Le cycle 007 §§5 et 10 n'est pas réécrit.
Les théorèmes 4.2.7 et 4.3.10 restent non adoptés.

L'inégalité $P(m)\ge n$ est confirmée. La revue demande de retirer, au
cycle 007 §4, la phrase « $n$ est le premier point de $\Sigma$
rencontré ». Cette phrase est placée sous l'hypothèse de collision
$P(m)=P(n)=r$. Dans cette hypothèse, $P(m)=r$ exclut tout intermédiaire
dans $\Sigma$, et $n$ est sur la chaîne avant $r$, donc $n$ est bien ce
premier point, et $P(m)=n$. Le même paragraphe dit déjà que cette
égalité est plus forte que $P(m)\ge n$, et qu'elle est fausse pour un
point ultérieur quelconque : $P(16)=4>1$. La phrase n'est pas une erreur.
Elle est conservée. Le témoin $16\to8\to4\to2\to1$ reste celui du texte.

La prémisse non pondérée de l'agenda est confirmée comme conséquence du
cycle 005 §5. Le calcul du §1 est cette conséquence, pas un nouvel
énoncé. La question traitée ici est la forme pondérée, que la revue
laissait non vérifiée. Le cas $K>3/2$ ne se déduit pas de B10 ; c'est le
contenu du §5.

La revue a contrôlé en JavaScript les chaînes de divisions pour
$2\le m\le40\,000$. Ce segment n'est pas repris : l'inégalité du cycle
007 §4 est déjà prouvée pour tout entier, et le script de ce cycle-là
couvre un segment plus court. Le script du présent cycle a été exécuté.

## 8. Antériorité

Le mécanisme est la montée de Mersenne, déjà A2, et le chaînage de
contractions qui prouve l'horizon fixe dans `no_finite_certificate`.
Cette extension au horizon variable, avec la constante $C$, n'est pas
dans B10 ni dans le rapport d'audit : les deux s'arrêtent, l'un au seuil
$K\le3/2$ sur les Mersenne, l'autre à un $B$ indépendant de $n$.
Applegate–Lagarias 2003, théorème 1.1 et formule (4), bornent un autre
temps. Aucune source nouvelle n'a été lue pour ce cycle. Aucune
nouveauté hors de ce dépôt n'est revendiquée.

## 9. Mises à jour de la mémoire

- `proved.md` : B13.
- `hypotheses.md` : H6, implication globale prouvée.
- `prior_art.md` : pas de lecture nouvelle.
- `abandoned.md` : ne pas relancer l'implication globale, ni la forme
  non pondérée.
- `agenda.md` : prochaine question sur l'axe B.
- `reviews.md` : revue `6082099628`.
- `counterexamples.md` : inchangé. X21 reste local.

## 10. Prochaine question

Axe **B**, un seul énoncé. Pour le mot du cycle 004 §8 à un zéro par
bloc, avec $r_1=64$ et, pour $k\ge2$,
$r_k=\lfloor\beta o_k\rfloor-\lfloor\sqrt{o_k}\rfloor$, la série de
réalisation 2-adique est-elle rationnelle ? Le critère B7 ne s'applique
pas : $Q_k\to-\infty$. Chercher d'abord si une queue périodique est
compatible avec ces longueurs. Si elle ne l'est pas, écrire la série et
dire si elle se ramène à une valeur de Tschakaloff dont un théorème déjà
lu dans ce dépôt exclut la rationalité. Ne pas réutiliser B7, ne pas
rouvrir le mot du cycle 006, ne pas relancer B10, B13 ni X21.

## 11. Reproduire

```sh
python3 research/checks/cycle008_weighted_horizon.py
```

Sortie attendue : sept lignes `PASS`. Elles couvrent le corollaire non
pondéré pour quatre valeurs de $\rho$ et $2\le L\le40$, l'identité de
montée partielle jusqu'à $L=30$, le successeur de X21 pour $2\le L\le30$,
les entiers $m_*=3$, $t_*=2$, $J=4$, la descente $K\cdot2^t>3^R$ sur les
retours tardifs de sept fractions $K$ pour $2\le L\le17$, l'identité
$2^R(3^L-1)-3^R n_j=3^R-2^R$, et la convention $t_*=0$ lorsque
$K\le1/2$, avec $C=-2$ pour $\rho=1/4$. L'implication B13 est prouvée
au §5 pour tout réel $K>0$ et tout $L$ assez grand. Le script n'en voit
qu'un segment.

## 12. Revue `6082191024`

Revue indépendante sur le SHA
`ff58fed0501768dabaa980ee5d0668b347d8b898` (PR #27), c'est-à-dire sur
B13. Le verdict de la revue est que l'implication est prouvée. Trois
corrections de rédaction, intégrées ci-dessus. Ce n'est pas un nouveau
cycle.

La définition littérale « le plus grand $t\ge0$ tel que
$(3/2)^t<2K$ » a un ensemble vide lorsque $K\le1/2$, y compris à
$2K=1$. La phrase qui posait alors $t_*=0$ était la convention utile,
pas le maximum de cet ensemble. Le §4 définit désormais $t_*$ comme
le maximum de $\{0\}$ et des entiers $t\ge1$ vérifiant l'inégalité.
Pour $\rho=5/6$ et $K=5/3$, on a encore $t_*=2$ et $J=4$. Le lemme et
la majoration $j_*\le J$ restent ceux du texte relu.

Au §5, un saut est un temps $1\le t\le L-j_r$. La construction
s'arrête sur l'absence de contraction jusqu'au sommet inclus. Elle ne
contrôle pas un retour ultérieur sur la liste $(n_j)$. L'inégalité
$t>R$ suffit à l'estimation, et elle vaut aussi pour un tel retour.

L'identité $2^R(3^L-1)-3^R n_{j_*}=3^R-2^R$ remplace la comparaison
$3^R-1>3^R/2$. On en tire $K\cdot2^t>3^R$, donc
$t>\delta R-\log_2 K$. La constante passe de $\log_2(2K)$ à
$\log_2 K$. L'ancienne valeur reste un majorant, d'exactement une
unité. Sur l'exemple $h=\ell$, $\rho=1/4$, l'ancienne constante vaut
$\log_2(1/2)=-1$ et la nouvelle vaut $-2$. Les deux sont inférieures
à $\log_2(3/2)$ : pour $C=-1$, l'écart sur $n=2^L-1$ est
$\delta(\log_2 n-(L-1))>0$. La forme uniforme de B10 n'est donc pas
toujours plus serrée. La comparaison pertinente, pour $K\le3/2$ et
$j_*=0$, est $t>\delta L-\log_2 K$, déjà écrite dans la preuve du
cycle 005 §5 avant le passage à $3/2$.

La revue a contrôlé en JavaScript, pour $2\le L\le70$, $1\,272$
chaînes et $1\,268$ retours. Ce segment n'est pas repris. Le script
Python a été exécuté : il vérifie l'identité, la convention
$t_*=0$, le seuil $3/4$ et la descente stricte $K\cdot2^t>3^R$.
Applegate–Lagarias 2003 n'est pas relu. Aucune source nouvelle.
