# Cycle 004 — Runs de Fibonacci et critère de Liouville

Date : 26 novembre 2026. Axe **B**.
Branche : `research/memory`. Script : [`../checks/cycle004_fibonacci.py`](../checks/cycle004_fibonacci.py).

**Verdict : PROUVÉ.** Pour le mot dont les runs impairs ont longueurs
$F_3,F_4,F_5,\ldots=2,3,5,8,\ldots$, on a $Q_k>k$ pour tout $k\ge1$ (B9).
Donc $Q_k\to+\infty$ et B7 s'applique : le réalisateur 2-adique est irrationnel.
Si l'itinéraire d'un entier positif commence par le préfixe exact, alors
$N\ge2^{k-1}$. Les seules longueurs de ces runs ne donnent pas ce préfixe (X20).
Un préfixe fini devant un mot à un zéro par bloc et de taux $\lambda>\log_2 3$
ne restaure pas la rationalité (§8). Au seuil $\lambda=\log_2 3$, les deux signes
de $r_k-\beta o_k$ sont réalisés par des familles explicites : l'une donne
$Q_k\to+\infty$, l'autre $Q_k\to-\infty$.
L'alternative de l'agenda ($2^{o_k+r_k+1}<3^{o_k}+P_k$ pour tout $k$ grand) est fausse
pour chaque $k$. Ni (C), ni Syracuse. La preuve est une récurrence sur $F_n$ ;
elle ne calcule aucune puissance $3^{F_n}$ au-delà de $3^5$.

## 0. Question traitée

Première entrée de l'agenda. Mot $w=\prod_{k\ge1}(0\,1^{F_{k+2}})$, avec
$F_1=F_2=1$ et $F_n=F_{n-1}+F_{n-2}$. Les notations $o_k$, $r_k$, $P_k$, $G_k$,
$Q_k$, $\beta=\log_2(3/2)$ et $\delta=\log_2 3$ sont celles du cycle 003.
L'agenda demande de trancher : $Q_k\to+\infty$, ou bien
$2^{o_k+r_k+1}<3^{o_k}+P_k$ pour tout $k$ assez grand.

## 1. Sommes de Fibonacci

Le $k$-ième run impair a longueur $r_k=F_{k+2}$. Le mot commence par $0$, donc
$o_1=0$ et $o_k=\sum_{j=1}^{k-1}r_j$ pour $k\ge2$. L'identité
$\sum_{i=1}^{n}F_i=F_{n+2}-1$ donne
$$o_k=\sum_{i=3}^{k+1}F_i=F_{k+3}-3.$$
En particulier $o_k+r_k=F_{k+4}-3=o_{k+1}$. L'agenda antérieur à ce cycle
notait $S_{k-1}=F_{k+3}-3$, c'est-à-dire $o_k$. La somme $o_k+r_k$ est $S_k$.
Le rapport $r_k/o_k=F_{k+2}/(F_{k+3}-3)$ n'est défini que pour $k\ge2$.

## 2. Le rapport tend vers $1/\varphi$, et $1/\varphi>\beta$

Posons $q_n=F_{n+1}/F_n$. Alors $q_n=1+1/q_{n-1}$ pour $n\ge2$.

**Identité de Cassini.** Pour $n\ge2$, $F_{n+1}F_{n-1}-F_n^2=(-1)^n$.
Pour $n=2$ : $F_3F_1-F_2^2=1$. Si l'identité vaut en $n$, alors
$$F_{n+2}F_n-F_{n+1}^2=F_n^2-F_{n+1}F_{n-1}=(-1)^{n+1}.$$

Donc
$$q_n-q_{n-1}=\frac{(-1)^n}{F_n F_{n-1}},\qquad
q_n-q_{n+1}=\frac{(-1)^n}{F_{n+1}F_n}.$$
En additionnant deux écarts consécutifs,
$$q_{n+1}-q_{n-1}
=\frac{(-1)^n}{F_n}\left(\frac1{F_{n-1}}-\frac1{F_{n+1}}\right)
=\frac{(-1)^n}{F_{n+1}F_{n-1}},$$
car $F_{n+1}-F_{n-1}=F_n$. Pour $n$ pair, $q_{n+1}>q_{n-1}$ : les termes
d'indice impair croissent. Pour $n$ impair, $q_{n+1}<q_{n-1}$ : les termes
d'indice pair décroissent. Le second écart dit qu'un impair est suivi d'un pair
plus grand, et qu'un pair est suivi d'un impair plus petit. Les pairs partent de
$q_2=2$ en décroissant, donc tout impair, inférieur au pair qui le suit, est
$<2$. Les impairs partent de $q_1=1$ en croissant, donc tout pair, supérieur à
l'impair qui le suit, est $>1$. Les deux suites convergent, et
$|q_{2m}-q_{2m+1}|=1/(F_{2m+1}F_{2m})\to0$, donc elles ont la même limite
$L>0$. Comme $q_n=1+1/q_{n-1}$, $L=1+1/L$, donc $L^2-L-1=0$ et
$L=\varphi=(1+\sqrt5)/2$.

Ainsi $F_{k+3}/F_{k+2}\to\varphi$ et $(F_{k+3}-3)/F_{k+3}\to1$, d'où
$$r_k/o_k\to1/\varphi.$$
Comme $\varphi^2=\varphi+1$, on a $1/\varphi=\varphi-1$, et
$$1/\varphi>\beta\iff\varphi>\log_2 3.$$
Or $\varphi>8/5$ : $(1+\sqrt5)/2>8/5$ équivaut à $5\sqrt5>11$, et
$125>121$. Et $8/5>\log_2 3$ : $2^8=256>243=3^5$. Donc $1/\varphi>\beta$.

Le même écart est entier pour chaque $k\ge2$, pas seulement à la limite.
Le lemme du §3 donne $2^{F_{n+1}}>3^{F_n}$ pour $n\ge4$. Pour $k\ge2$,
l'indice $k+3\ge5$, donc $2^{F_{k+4}}>3^{F_{k+3}}$, puis
$2^{F_{k+4}-3}>3^{F_{k+3}-3}$, c'est-à-dire $2^{r_k}>(3/2)^{o_k}$ et $r_k>\beta o_k$.

## 3. Lemme de puissances

Pour tout $n\ge4$,
$$2^{F_{n+1}}\ge3^{F_n}+2^{n-2}.$$

**Bases.** $n=4$ : $2^{F_5}=32$ et $3^{F_4}+2^{2}=27+4=31$.
$n=5$ : $2^{F_6}=256$ et $3^{F_5}+2^{3}=243+8=251$.

**Pas.** Pour $n\ge6$, les deux indices $n-1$ et $n-2$ sont $\ge4$. Alors
$F_{n+1}=F_n+F_{n-1}$, et l'hypothèse de récurrence donne
$$2^{F_{n+1}}=2^{F_n}\,2^{F_{n-1}}\ge\bigl(3^{F_{n-1}}+2^{n-3}\bigr)\bigl(3^{F_{n-2}}+2^{n-4}\bigr).$$
Le produit vaut $3^{F_n}+2^{n-4}3^{F_{n-1}}+2^{n-3}3^{F_{n-2}}+2^{2n-7}$.
Pour $n\ge6$, $F_{n-1}\ge F_5=5$, donc $3^{F_{n-1}}\ge243\ge4$ et
$$2^{n-4}3^{F_{n-1}}\ge2^{n-2}.$$
Le produit est donc au moins $3^{F_n}+2^{n-2}$.

En particulier $2^{F_{n+1}}>3^{F_n}$ pour tout $n\ge4$.

## 4. Théorème B9

Pour ce mot, $Q_k>k$ pour tout $k\ge1$. En particulier $Q_k\to+\infty$, et
$\xi_w\notin\mathbb Q$.

La forme entière du cycle 003, pour $L=k\in\mathbb Z$ et un exposant positif, dit
que $Q_k>k$ équivaut à $D_k>3^{o_k}+P_k$, où $D_k=2^{o_k+r_k+1}$.

**Récurrence de $P$.** Par définition,
$P_{k+1}=3^{r_k}P_k+2^{(k+1)+o_{k+1}}$, donc
$$3^{o_{k+1}}+P_{k+1}=3^{r_k}(3^{o_k}+P_k)+2^{(k+1)+o_{k+1}}.$$
Comme $o_{k+1}=o_k+r_k$, le dernier terme est $2^k D_k$. Et
$D_{k+1}=2^{o_{k+1}+r_{k+1}+1}=D_k\,2^{r_{k+1}}$.

**Cas $k=1$, direct.** $o_1=0$, $r_1=2$, $P_1=2^{1+0}=2$, $D_1=2^3=8$ et
$3^0+P_1=3$. Donc $8>3$.

**Cas $k=2$, direct.** $o_2=2$, $r_2=3$,
$P_2=3^{2}\cdot2+2^{2+2}=34$, $D_2=2^{6}=64$ et $3^2+34=43$. Donc $64>43$.

**Pas, pour $k\ge2$.** Le lemme au rang $n=k+2\ge4$ est
$2^{F_{k+3}}\ge3^{F_{k+2}}+2^k$, c'est-à-dire $2^{r_{k+1}}\ge3^{r_k}+2^k$.
Si $D_k>3^{o_k}+P_k$, alors
\begin{align*}
D_{k+1}
&=D_k\,2^{r_{k+1}}
\ge D_k(3^{r_k}+2^k)
=3^{r_k}D_k+2^k D_k\\
&>3^{r_k}(3^{o_k}+P_k)+2^{(k+1)+o_{k+1}}
=3^{o_{k+1}}+P_{k+1}.
\end{align*}
L'inégalité finale est stricte parce que l'hypothèse $D_k>3^{o_k}+P_k$ l'est,
même si le lemme n'est pas strict. Le cas $k=2$ amorce la récurrence :
$D_k>3^{o_k}+P_k$ pour tout $k\ge2$, et le cas $k=1$ a été vu à part.
Le pas $k=1\to2$ n'est pas invoqué : pour $k=1$, $2^{F_4}=8<11=3^{F_3}+2^1$.

Ainsi $Q_k>k$ pour tout $k\ge1$. Le supremum est infini. B7, déjà prouvé au
cycle 003, donne $\xi_w\notin\mathbb Q$.

## 5. Deux conséquences

**Préfixe exact.** Si l'itinéraire d'un entier $N>0$ commence par
$$\prod_{j=1}^{k}(0\,1^{F_{j+2}})\,0,$$
les quantités $o_j$, $r_k$ et $P_k$ coïncident avec celles de $w$ sur cette
fenêtre, donc $Q_k>k$. Pour $\xi=N$, $\sigma=-2(N+1)$ en forme réduite de
dénominateur $1$, et B7 donne $Q_k\le\log_2\bigl(2(N+1)\bigr)$. Donc
$k<\log_2\bigl(2(N+1)\bigr)$, soit $2^{k-1}<N+1$. Comme $N+1$ est entier,
$N\ge2^{k-1}$.

Les longueurs des $k$ premiers runs impairs ne déterminent pas ce préfixe.
Elles ne fixent ni la parité initiale ni le nombre de zéros intercalés (X20).
Le départ $3$ a un premier run de longueur $2$ et commence par $110$. Le départ
$12$ commence par $00110$. Le départ $91$ a pour deux premiers runs $2,3$ et
commence par $1101110$. Le préfixe exact de $k=2$ est $01101110$, réalisé par
$182$. Le départ $422$ commence par $011001110$ : un seul zéro initial, puis
les runs $2$ et $3$, séparés par deux zéros.

**Runs impairs finis.** Pour $n$ impair positif, $n+1=2^v m$ avec $v\ge1$ et
$m$ impair, donc $T(n)+1=3(n+1)/2$ et $v_2(T(n)+1)=v-1$. Le run impair issu de
$n$ a longueur $v_2(n+1)$. Cette phrase ne vaut pas pour tout impair : $n=-1$
est fixe, $T(-1)=-1$, et $n+1=0$ n'a pas de valuation finie. Un entier positif
a une valuation $v_2(N)$ finie : l'orbite atteint un impair positif, puis un
run impair fini, puis un pair, et ceci se répète. L'itinéraire contient une
infinité de zéros. C'est l'une des deux prémisses de B7. L'autre,
$\sup_m Q_m=+\infty$, dépend du mot : c'est elle qui donne l'irrationalité.
La seule infinité des zéros ne la fournit pas, et elle ne fixe pas les
longueurs des zéros entre les runs.

Cette borne est grosse. Elle dit seulement qu'un entier trop petit ne peut pas
suivre le préfixe exact. Le script calcule, pour $k\le8$, le plus petit entier
positif de ce préfixe : il satisfait la borne, et il est bien plus grand
($k=8$ : un entier de $148$ bits, contre la borne $2^{7}$). Ce calcul borne
cherche un contre-exemple au préfixe exact ; il ne renforce pas la constante.

**Densité.** Le préfixe qui s'arrête sur le $k$-ième zéro contient $k$ zéros et
$o_k$ uns, soit une proportion de zéros $k/(k+o_k)$. Jusqu'au zéro suivant on
n'ajoute que des uns, donc un préfixe qui se termine dans cet intervalle a une
proportion de zéros au plus $k/(k+o_k)$. Comme $o_k=F_{k+3}-3$ croît plus vite
que $k$, cette proportion tend vers $0$. Après $K$ blocs il y a $K$ zéros et
$F_{K+4}-3$ uns : la densité des $1$ vaut $1$. Comme pour B8, ce n'est pas un
corollaire de Monks–Yazinski 2004, théorème 2.7(b), qui borne inférieurement la
densité des $1$ d'une orbite rationnelle divergente.

## 6. Pourquoi la somme partielle ne compense pas

Pour $r\ge2$, $2^{1+r}/3^r=2(2/3)^r$ décroît en $r$, et $r_j=F_{j+2}\ge2$.
Le rapport des termes de $G$ vaut donc au plus sa valeur en $r=2$ :
$$t_{j+1}/t_j=2^{1+r_j}/3^{r_j}\le8/9,$$
avec égalité seulement pour $j=1$. Ainsi $t_1=2$, $t_2=16/9$, et
$t_j<2(8/9)^{j-1}$ pour $j\ge3$. La série géométrique $\sum_{i\ge0}2(8/9)^i$
vaut $18$, donc $G_k<18$ et $\log_2(1+G_k)<\log_2 19$. La correction
archimédienne reste bornée. Jointe à $r_k-\beta o_k\to+\infty$ (§2), elle
redonne $Q_k\to+\infty$, sans la précision $Q_k>k$. Le théorème du §4 n'utilise
pas cette majoration.

## 7. Littérature

La comparaison $\varphi>\log_2 3$ est classique ; elle n'est pas un résultat de
Syracuse. La preuve de B9 dépend de B7 et des identités de Fibonacci ci-dessus.
Elle n'utilise pas Väänänen–Wallisser.

- Le mot de Fibonacci sturmien (point fixe de $0\mapsto01$, $1\mapsto0$) a des
  runs bornés. Ce n'est pas $w$ : ici les runs de $1$ sont non bornés, donc $w$
  n'est pas sturmien. Les facteurs $0110$ et $1111$ contiennent deux et quatre
  symboles $1$. Leur écart vaut $2$, donc $w$ n'est pas équilibré.
- **Monks–Yazinski** (2004), thm 2.7(b), déjà lu au cycle 003 : densité
  inférieure des $1$ pour une orbite rationnelle divergente. Ne donne pas
  l'irrationalité d'un mot prescrit.
- **De Jesús**, résumé SSRN du 23 septembre 2026 (mots sturmiens envoyés sur un
  2-adique irrationnel par un argument de Liouville). **[S]**, non lu. Même si
  l'annonce est exacte, elle ne couvre pas $w$. Le manuscrit Zenodo déjà
  consigné au cycle 003 reste non lu ; il n'est pas utilisé.
- Les comptages de Fibonacci dans le $3x+1$ (mots évitant le facteur $11$,
  étiquettes de l'arbre inverse) portent sur d'autres objets. Ils ne sont pas
  utilisés. Aucune de ces sources n'a été prise comme prémisse.

## 8. Portée

Rien sur (C), rien sur (H), rien sur la conjecture de Syracuse. B9 dit que
le mot infini n'est l'itinéraire d'aucun rationnel. Ses préfixes exacts
exigent $N\ge2^{k-1}$. Tout mot fini de longueur $L$ est l'itinéraire initial
d'une seule classe modulo $2^L$ (cycle 003 §1), donc d'un entier positif. Le
script calcule ce résidu pour les préfixes de Fibonacci, $k\le8$. X20 empêche
de passer des longueurs de runs à ce résidu.

**Corollaire.** Soit $(r_k)_{k\ge1}$ une suite d'entiers $\ge1$ telle que
$r_{k+1}/r_k\to\varphi$. Le mot $\prod_{k\ge1}(0\,1^{r_k})$, à exactement un
zéro par bloc, vérifie $o_k/r_k\to\varphi$ et $Q_k\to+\infty$. Son réalisateur
2-adique est irrationnel, par B7.

**Preuve.** Ici $o_1=0$ et $o_{k+1}=o_k+r_k$. La suite $s_k=o_k/r_k$ satisfait
$$s_{k+1}=\frac{s_k+1}{q_k},\qquad q_k=\frac{r_{k+1}}{r_k}.$$
Le §2 donne $\varphi>8/5$, et $8/5>3/2$ car $16>15$. Il existe donc $K$ tel que
$q_k\ge3/2$ pour tout $k\ge K$. Le point fixe de $s\mapsto(s+1)/\varphi$ est $\varphi$ :
$\varphi=1+1/\varphi$, donc $1/(\varphi-1)=\varphi$. Posons $e_k=s_k-\varphi$.
Comme $\varphi^2=\varphi+1$,
$$s_{k+1}-\varphi=\frac{s_k+1-\varphi q_k}{q_k}
=\frac{e_k-\varphi(q_k-\varphi)}{q_k}.$$
Pour $k\ge K$,
$$|e_{k+1}|\le\frac23|e_k|+\delta_k,
\qquad\delta_k=\frac{2\varphi}3\,|q_k-\varphi|.$$
Donc $\delta_k\to0$. En itérant,
$$|e_{K+n}|\le\Bigl(\frac23\Bigr)^n|e_K|
+\sum_{j=0}^{n-1}\Bigl(\frac23\Bigr)^{n-1-j}\delta_{K+j}.$$
Soit $\varepsilon>0$. Pour $j$ assez grand, $\delta_{K+j}<\varepsilon/6$. La
partie correspondante de la somme est au plus
$(\varepsilon/6)\sum_{i\ge0}(2/3)^i=\varepsilon/2$. Le terme $(2/3)^n|e_K|$ et
la partie finie de la somme tendent vers $0$. Ainsi $e_k\to0$, et
$s_k\to\varphi$. Pour $k\ge2$, $r_k/o_k\to1/\varphi=\varphi-1$. Le §2 donne
$\varphi-1>\beta$, donc $r_k-\beta o_k\to+\infty$ : l'écart
$r_k/o_k-\beta$ est ultimement minoré par le nombre positif $(\varphi-1-\beta)/2$,
et $o_k\ge k-1$.

Comme $q_k\to\varphi>8/5>1$, la suite $(r_k)$ est ultimement strictement
croissante, donc $r_k\ge2$ à partir d'un rang $J$. Pour $r\ge2$,
$t_{j+1}/t_j=2(2/3)^{r_j}\le8/9$. La queue de $G$ à partir de $J$ est majorée
par $t_J\sum_{i\ge0}(8/9)^i=9t_J$, et $\sum_{j<J}t_j$ est finie. Ainsi $G_k$
reste bornée, $\log_2(1+G_k)$ aussi, et
$$Q_k=r_k+k+1-\beta o_k-\log_2(1+G_k)\to+\infty.$$
B7 donne l'irrationalité. Après $M$ blocs il y a $M$ zéros et $o_{M+1}$ uns.
Comme $r_j\to+\infty$, pour tout entier $A$ on a $r_j>2A$ à partir d'un rang,
et la moyenne $(1/M)\sum_{j=1}^{M}r_j$ dépasse $A$ pour $M$ grand. La densité
des $1$ vaut $1$. ∎

Ce corollaire ferme le mot à un seul zéro par bloc dont le rapport des runs
tend vers $\varphi$. La même récurrence couvre tout taux strictement
supérieur à $\log_2 3$.

**Extension.** Soit $(r_k)_{k\ge1}$ une suite d'entiers $\ge1$ telle que
$q_k=r_{k+1}/r_k\to\lambda$ avec $\lambda>1$. Le mot
$\prod_{k\ge1}(0\,1^{r_k})$ vérifie $s_k=o_k/r_k\to1/(\lambda-1)$.

Le point fixe de $s\mapsto(s+1)/\lambda$ est $\sigma=1/(\lambda-1)$, car
$\sigma+1=\sigma\lambda$. Avec $e_k=s_k-\sigma$,
$$s_{k+1}-\sigma=\frac{s_k+1-\sigma q_k}{q_k}
=\frac{e_k-\sigma(q_k-\lambda)}{q_k}.$$
Choisissons $\rho$ tel que $1/\lambda<\rho<1$. À partir d'un rang $K$,
$q_k\ge1/\rho$, donc
$$|e_{k+1}|\le\rho\,|e_k|+\delta_k,
\qquad\delta_k=\frac{\sigma}{q_k}|q_k-\lambda|,$$
et $\delta_k\to0$. En itérant,
$$|e_{K+n}|\le\rho^n|e_K|
+\sum_{j=0}^{n-1}\rho^{n-1-j}\delta_{K+j}.$$
Soit $\varepsilon>0$. Pour $j$ assez grand,
$\delta_{K+j}<\varepsilon(1-\rho)/2$. La partie correspondante de la somme est
au plus $(\varepsilon(1-\rho)/2)\sum_{i\ge0}\rho^i=\varepsilon/2$. Le terme
$\rho^n|e_K|$ et la partie finie tendent vers $0$. Donc $e_k\to0$.

Comme $\beta=\log_2 3-1$, on a $\lambda-1>\beta$ si et seulement si
$\lambda>\log_2 3$. Si $\lambda>\log_2 3$, alors
$r_k/o_k\to\lambda-1>\beta$. L'écart $r_k/o_k-\beta$ est ultimement minoré
par $(\lambda-1-\beta)/2$, et $o_k\to+\infty$, donc
$r_k-\beta o_k\to+\infty$. De plus $r_k\to+\infty$ : à partir d'un rang,
$r_{k+1}\ge\mu r_k$ pour un $\mu$ avec $1<\mu<\lambda$. Donc $r_k\ge2$ à
partir d'un rang, le rapport des termes de $G$ est au plus $8/9$, et $G$
reste bornée comme au §6. Ainsi $Q_k\to+\infty$. Le mot a une infinité de
zéros. B7 donne l'irrationalité. Le cas $\varphi$ est celui du corollaire :
$\varphi>\log_2 3$ est le §2.

Si $1<\lambda<\log_2 3$, alors $r_k/o_k\to\lambda-1<\beta$. Pour un $c>0$,
$r_k-\beta o_k\le -c\,o_k$ à partir d'un rang. Comme $G_k\ge0$,
$$Q_k\le r_k+k+1-\beta o_k\le -c\,o_k+k+1.$$
Puisque $\lambda>1$, $r_k$ croît géométriquement à partir d'un rang, et $o_k$
aussi. Donc $Q_k\to-\infty$. B7 ne s'applique pas. L'irrationalité de ces
mots reste ouverte par ce critère.

Si $\lambda=\log_2 3$, la même récurrence donne seulement $r_k/o_k\to\beta$.
Cette limite ne fixe pas le signe de $r_k-\beta o_k$. Les deux familles
suivantes montrent que les deux signes se produisent, avec la même limite
des rapports de runs.

**Proposition.** Pour $\varepsilon\in\{+1,-1\}$, soit $r_1=64$ et, pour
$k\ge2$,
$$r_k=\lfloor\beta o_k\rfloor+\varepsilon\lfloor\sqrt{o_k}\rfloor,$$
où $o_1=0$ et $o_{k+1}=o_k+r_k$. Alors $r_k\ge1$ pour tout $k$,
$r_k/o_k\to\beta$ et $r_{k+1}/r_k\to\log_2 3$. Pour $\varepsilon=+1$,
$Q_k\to+\infty$ : le réalisateur 2-adique est irrationnel, par B7. Pour
$\varepsilon=-1$, $Q_k\to-\infty$ : B7 ne s'applique pas. L'irrationalité
de cette seconde famille reste ouverte par ce critère.

**Preuve.** D'abord $\beta>1/2$, car $(3/2)^2=9/4>2$. Pour tout entier
$o\ge64$,
$$\sqrt o+1\le\frac9{64}o.$$
Les deux membres de $\sqrt o\le(9o-64)/64$ sont positifs ou nuls. Élever au
carré est donc une équivalence, et l'inégalité équivaut à
$h(o)\ge0$, où $h(o)=(9o-64)^2-4096\,o$. En $o=64$,
$(9\cdot64-64)^2=512^2=262144$ et $4096\cdot64=262144$, donc $h(64)=0$.
Avec $a(o)=9o-64$, on a $a(o+1)=a(o)+9$ et
$$h(o+1)-h(o)=18a(o)+81-4096=18(9o-64)+81-4096=162o-5167.$$
Pour $o\ge64$, ce pas vaut au moins $162\cdot64-5167=5201>0$. Donc $h$
croît strictement sur les entiers $\ge64$, et $h(o)\ge0$. De plus
$9/64<\beta/2$ : $\beta/2>1/4=16/64$. Ainsi, pour tout entier $o\ge64$,
$$\sqrt o+1\le\frac9{64}o<\frac\beta2\,o.$$

Ici $o_2=r_1=64$. Pour $k\ge2$, les deux signes vérifient
\begin{align*}
r_k
&\ge\lfloor\beta o_k\rfloor-\lfloor\sqrt{o_k}\rfloor
>\beta o_k-1-\sqrt{o_k}
=\beta o_k-(\sqrt{o_k}+1)\\
&\ge\beta o_k-\frac9{64}o_k
>\frac\beta2\,o_k.
\end{align*}
La comparaison stricte avec $\beta o_k-1$ vient de $\lfloor y\rfloor>y-1$,
et $\lfloor\sqrt{o_k}\rfloor\le\sqrt{o_k}$. Comme $\beta/2>1/4$, on a
$r_k>o_k/4$, donc $r_k\ge1$ et $o_{k+1}>5o_k/4$. Par récurrence
$o_k\ge64$ pour tout $k\ge2$, et $o_k>64\cdot(5/4)^{k-2}$ pour $k\ge3$.
En particulier $o_k\to+\infty$.

Le second ordre est encadré. Comme $-1<\lfloor\beta o\rfloor-\beta o\le0$,
$$\lfloor\sqrt o\rfloor-1<r-\beta o\le\lfloor\sqrt o\rfloor$$
si $\varepsilon=+1$, et
$$-\lfloor\sqrt o\rfloor-1<r-\beta o\le-\lfloor\sqrt o\rfloor$$
si $\varepsilon=-1$. Dans les deux cas
$|r_k-\beta o_k|\le\lfloor\sqrt{o_k}\rfloor+1\le\sqrt{o_k}+1$, donc
$(r_k-\beta o_k)/o_k\to0$ et $r_k/o_k\to\beta$. Alors
$o_{k+1}/o_k=1+r_k/o_k\to1+\beta=\log_2 3$. Comme $r_k/o_k\to\beta>0$,
$$\frac{r_{k+1}}{r_k}
=\frac{r_{k+1}}{o_{k+1}}\cdot\frac{o_{k+1}}{o_k}\cdot\frac{o_k}{r_k}
\to\beta\cdot(1+\beta)\cdot\frac1\beta=1+\beta=\log_2 3.$$

La somme $G$ reste bornée. On a $t_1=2$ et, pour $r\ge2$,
$t_{j+1}/t_j=2(2/3)^r\le8/9$. Or $r_1=64$ et, pour $k\ge2$,
$r_k>(\beta/2)o_k>(\beta/2)\cdot64>16$. Tous les rapports sont donc
$\le8/9$, et
$$G_k\le\sum_{i=0}^{k-1}2\cdot\Bigl(\frac89\Bigr)^i<18.$$
Ainsi $1+G_k<19<32=2^5$, et $\log_2(1+G_k)<5$.

Signe plus. L'encadrement donne
$Q_k>\lfloor\sqrt{o_k}\rfloor-1+k+1-5=\lfloor\sqrt{o_k}\rfloor+k-5$.
Pour $k\ge2$, $o_k\ge64$, donc $\lfloor\sqrt{o_k}\rfloor\ge8$ : $8^2=64$
et $o_k$ croît. Ainsi
$Q_k>\lfloor\sqrt{o_k}\rfloor+k-5\ge k+3$. L'inégalité de gauche est
stricte, donc $Q_k>k+3$, et en particulier $Q_k>k$.
Pour $k\ge3$, $\sqrt{o_k}>8\cdot(5/4)^{(k-2)/2}$. Posons $m=k-2$ et
$w_m=(5/4)^m/m^2$. Pour $m\ge2$, $k=m+2\le2m$, donc
$\sqrt{o_k}/k>4\sqrt{w_m}$. Pour $m\ge16$, $m/(m+1)\ge16/17$ et
$$\frac{w_{m+1}}{w_m}
=\frac54\Bigl(\frac{m}{m+1}\Bigr)^2
\ge\frac54\cdot\frac{256}{289}
=\frac{320}{289}.$$
Or $320/289>11/10$, car $3200>3179=11\cdot289$. Pour $t\ge0$,
$w_{16+t}\ge w_{16}\cdot(11/10)^t$, avec égalité en $t=0$.
L'inégalité $(1+1/10)^t\ge1+t/10$ vaut
en $t=0$. Si elle vaut en $t$, multiplier par $11/10$ donne
$(1+1/10)^{t+1}\ge(1+t/10)(11/10)=1+(t+1)/10+t/100\ge1+(t+1)/10$.
Comme $w_{16}>0$,
$w_m\to+\infty$, puis $\sqrt{o_k}/k\to+\infty$ et
$\lfloor\sqrt{o_k}\rfloor/k\to+\infty$. Ainsi $Q_k\to+\infty$. Le mot
contient un zéro par bloc, donc une infinité de zéros. B7 donne
l'irrationalité.

Signe moins. Comme $\log_2(1+G_k)\ge0$,
$Q_k\le-\lfloor\sqrt{o_k}\rfloor+k+1$. La même limite
$\lfloor\sqrt{o_k}\rfloor/k\to+\infty$ donne $Q_k\to-\infty$. B7 ne
s'applique pas. ∎

Cette proposition justifie l'absence de conclusion uniforme au seuil. Le
signe plus est un cas d'irrationalité au rapport limite $\log_2 3$ : B7
exclut tout réalisateur rationnel, donc tout entier positif. Le signe
moins vérifie $Q_k\to-\infty$. Ce critère n'exclut alors aucune classe de
réalisateurs. Un mot infini peut être l'itinéraire d'un entier positif.
L'équivalence de rationalité sous suppression d'un préfixe fini vaut pour
les deux signes, par les inverses affines des branches. Seule
l'irrationalité du signe moins reste ouverte.

**Préfixe fini.** Un premier bloc de $1$ ne laisse pas un cas ouvert. Si le
mot commence par $1^a$ et que la queue à partir du premier $0$ est un mot du
cas $\lambda>\log_2 3$, ou la famille de signe plus, chaque pas impair vérifie
$$T(\xi)+1=\frac{3\xi+1}{2}+1=\frac32(\xi+1),$$
donc $T^a(\xi)+1=(3/2)^a(\xi+1)$. Ainsi $\xi\in\mathbb Q$ si et seulement si
$T^a(\xi)\in\mathbb Q$. La queue est le réalisateur du mot réduit, déjà
irrationnel, donc $\xi\notin\mathbb Q$.

Le même passage vaut pour un préfixe fini quelconque. La branche $0$ a pour
inverse $x=2T(x)$, la branche $1$ a pour inverse $x=(2T(x)-1)/3$. Les deux
sont des bijections de $\mathbb Q$. Si $u$ a longueur $L$, $\xi$ est
rationnel si et seulement si $T^L(\xi)$ l'est. Supprimer $u$ ne change pas
la rationalité. Cette équivalence vaut pour les deux familles du seuil,
et pour tout mot. Si la queue est un mot
du cas $\lambda>\log_2 3$, ou la famille de signe plus, elle est
irrationnelle, donc $\xi$ aussi. La famille de signe moins a la même
équivalence ; sa queue n'a pas été montrée irrationnelle, donc la
conclusion d'irrationalité reste ouverte pour elle.

La question ouverte sur les zéros se limite aux placements qui ne deviennent
pas un mot à un zéro par bloc de taux $\lambda>\log_2 3$ après suppression
d'un préfixe fini. Plusieurs zéros entre les runs, répétés infiniment souvent,
en font partie. Un préfixe fini du mot infini reste réalisable par un entier
positif, avec la borne du §5 dans le cas de Fibonacci. Les runs quasi
linéaires, $r_m/o_m\to0$, restent H5.

L'extension et le lemme de préfixe n'utilisent que B7, la récurrence de
$s_k$ et la comparaison de $\lambda-1$ à $\beta$. La proposition du seuil
ajoute la borne entière sur $\sqrt o+1$, la croissance $5/4$ et le rapport
des $w_m$. Le script contrôle l'identité $(3/2)^a$ sur les impairs positifs
jusqu'à $200$, le point fixe $T(-1)=-1$, le retour par les branches
inverses, le témoin $422$, la famille décalée $r_k=F_{k+2}+1$ jusqu'à
$k=12$, et les deux familles critiques pour $2\le k\le16$. Pour le signe
plus, la comparaison est $2^{o_k+r_k+1}>3^{o_k}+P_k$, soit $Q_k>k$.
L'exposant $o_k+r_k+k+1$ ne teste que $Q_k>0$. Pour le signe moins, elle
reste $2^{o_k+r_k+k+1}<3^{o_k}+P_k$, soit $Q_k<0$. Ces contrôles
ne remplacent pas la preuve. La proposition ne calcule aucune puissance
$3^{o_k}$.

## 9. Mises à jour

- `proved.md` : B9.
- `hypotheses.md` : H3 gagne le cas Fibonacci ; H4 enregistre ce second cas non vide.
- `abandoned.md` : la branche « $Q_k$ bornée avant $\varphi$ » est fermée.
- `prior_art.md` : lectures de ce cycle, marquées [S] quand le texte n'a pas été lu.
- `agenda.md` : prochaine question sur l'axe A (H6). Quatre cycles consécutifs
  ont porté sur l'axe B.
- Revue `6081410834` : X20, indice $S_{k-1}$, et le corollaire du §8.
  Détail en §11.
- Revue `6081458173` : portée du §5 et du §8. Le cas d'un premier bloc de $1$
  est fermé. La prochaine question de l'agenda n'est pas entamée. Détail en §12.
- Revue `6081531962` : les seuils stricts et le préfixe fini sont confirmés.
  Le signe au seuil $\lambda=\log_2 3$ est désormais la proposition du §8.
  La prochaine question de l'agenda n'est pas entamée. Détail en §13.
- Revue `6081622758` : la proposition du seuil est confirmée. Le test du
  signe plus comparait $Q_k>0$ ; il compare désormais $Q_k>k$. L'inégalité
  sur $w_{16+t}$ est large, avec égalité en $t=0$. La phrase sur les
  orbites est reformulée : le signe moins n'exclut aucun réalisateur.
  La prochaine question de l'agenda n'est pas entamée. Détail en §14.

## 10. Reproduire

```sh
python3 research/checks/cycle004_fibonacci.py
```

Sortie attendue : douze lignes `PASS`. Les puissances de Fibonacci testées
s'arrêtent à $F_{21}$, aux préfixes $k\le8$ et à la famille décalée $k\le12$.
Les familles critiques sont contrôlées pour $2\le k\le16$. Elles vérifient
le lemme, la récurrence de $P$, les témoins de X20 (dont $422$), l'identité
$(3/2)^a$, le point fixe $-1$, le retour par les branches inverses,
l'absence de petit contre-exemple au préfixe exact, et les comparaisons
entières $2^{o_k+r_k+1}>3^{o_k}+P_k$ (signe plus, soit $Q_k>k$) et
$2^{o_k+r_k+k+1}<3^{o_k}+P_k$ (signe moins, soit $Q_k<0$) sur ce segment. La
preuve de B9 est le §4. La preuve du corollaire, de son extension, du
préfixe fini et des deux familles du seuil est le §8.

## 11. Revue `6081410834`

Revue indépendante sur le SHA `8bc44f73615fd5fcf0b59797f59ec74cf8cece10`
(26 novembre 2026). Marqueur `SYRACUSE_INDEPENDENT_REVIEW`. Elle confirme les
preuves écrites de B9 (§§2–4) et la borne $N\ge2^{k-1}$ sous l'hypothèse du
préfixe exact. Ce n'est pas une seconde preuve. Les bases du lemme, la marge
$D_k>3^{o_k}+P_k$ et les résidus des préfixes ont été revérifiés par le script.

- L'ancienne phrase de §1 identifiait $o_k+r_k=F_{k+4}-3$ à $S_{k-1}$. L'agenda
  antérieur posait $S_{k-1}=F_{k+3}-3$, qui est $o_k$. La somme $o_k+r_k$ est
  $S_k$. Les §§2–4 n'utilisent pas ce symbole : leurs identités
  $o_k=F_{k+3}-3$ et $o_k+r_k=F_{k+4}-3$ sont inchangées.
- L'ancienne phrase de §5 déduisait le préfixe exact des seules longueurs de
  runs. C'est X20. Les témoins $3$ ($110$), $12$ ($00110$) et $91$
  ($1101110$, runs $2,3$) ont été rejoués. La borne entière est conservée, avec
  l'hypothèse « l'itinéraire commence par le préfixe exact ». Pour $k\le8$ le
  script retrouve le résidu minimal de ce préfixe, dont celui de $148$ bits à
  $k=8$, et vérifie $N\ge2^{k-1}$.
- La chute $v_2(T(n)+1)=v_2(n+1)-1$ est vérifiée pour chaque impair
  $1\le n\le200$. La longueur du run égale à $v_2(n+1)$ l'est aussi. D'où
  l'infinité de zéros sur une orbite d'entier positif.
- La phrase de l'ancien §8, sur d'autres suites de runs croissant comme
  $\varphi$, est précisée. Le corollaire ci-dessus exclut le mot infini à un
  zéro par bloc dès que $r_{k+1}/r_k\to\varphi$. Les préfixes finis et les
  autres placements de zéros restent hors de cet énoncé. Aucune conclusion
  uniforme n'est ajoutée pour un taux $\lambda$ avec $\lambda-1\le\beta$.
- Les facteurs $0110$ et $1111$ sont dans $w$. Le résumé SSRN de De Jesús et
  le théorème 2.7(b) de Monks–Yazinski ne fournissent pas B9 ; leurs statuts
  de lecture restent ceux du §7.

B9 reste **PROUVÉ** par le §4. Le corollaire du §8 est **PROUVÉ** par le texte
de ce paragraphe, conditionnellement à B7 pour le passage à l'irrationalité.
X20 est une réfutation de l'implication sur les préfixes, pas de B9. La
prochaine question de l'agenda n'est pas abordée dans cette revue. Le §12
reprend ensuite la portée : un préfixe fini ne reste pas un cas ouvert, et
le taux $\lambda$ est séparé de part et d'autre de $\log_2 3$.

## 12. Revue `6081458173`

Revue indépendante sur le SHA `4696589434762ecf662475990fe6bbdfc0818726`
(26 novembre 2026). Marqueur `SYRACUSE_INDEPENDENT_REVIEW`. Elle confirme X20,
la borne du préfixe exact et le corollaire du §8 pour $\varphi$. Ce n'est pas
une seconde preuve.

- La phrase de §5 sur les runs finis est restreinte aux impairs positifs.
  $T(-1)=-1$ : l'énoncé lu sur tous les impairs admettait cette exception.
  Les deux prémisses de B7 sont séparées. L'infinité des zéros vaut pour toute
  orbite d'entier positif. L'irrationalité demande $\sup Q_m=+\infty$.
- Le témoin $422$, d'itinéraire initial $011001110$, isole deux zéros entre
  les runs $2$ et $3$. Il ne réalise pas $01101110$.
- L'ancienne portée laissait ouvert un mot qui commence par $1$. Si la queue
  à partir du premier zéro est un mot du corollaire, l'identité
  $T^a(\xi)+1=(3/2)^a(\xi+1)$ transporte la rationalité. Le lemme vaut pour
  tout préfixe fini, parce que chaque branche est une bijection de
  $\mathbb Q$. La question ouverte se limite aux placements de zéros qui ne
  se ramènent pas à un mot de taux $\lambda>\log_2 3$ en supprimant un
  préfixe fini.
- La même récurrence donne $Q_k\to+\infty$ pour tout $\lambda>\log_2 3$, et
  $Q_k\to-\infty$ pour $1<\lambda<\log_2 3$. Ces deux cas sont prouvés dans
  le §8. Au seuil $\lambda=\log_2 3$, le texte annonçait l'absence de signe
  uniforme. Cette annonce est complétée au §13. Ce n'est pas un nouveau cycle.
- Dans `prior_art.md`, « de ce mot » suivait la mention du mot sturmien.
  La phrase désigne désormais le mot de B9. Le décompte des $1$ dans $0110$
  et $1111$ est direct. La revue cite Lothaire, *Algebraic Combinatorics on
  Words*, §2.1, théorème 2.1.13 ; ce texte n'a pas été relu ici et n'est pas
  une prémisse. Monks–Yazinski, théorème 2.7(b), reste compatible avec une
  densité $1$ et n'est pas une prémisse du corollaire.

B9, le corollaire, son extension aux taux $\lambda>\log_2 3$ et le lemme de
préfixe fini sont **PROUVÉS** par les §§4 et 8, le passage à l'irrationalité
restant celui de B7. X20 n'est pas modifié dans son énoncé. La prochaine
question de l'agenda n'est pas abordée. La phrase du §8 qui annonçait, au
seuil $\lambda=\log_2 3$, l'absence de signe uniforme n'était pas justifiée
par la seule limite $r_k/o_k\to\beta$. Le §13 la remplace par deux familles.

## 13. Revue `6081531962`

Revue indépendante sur le SHA `33c22a38802bdaf810304c02ad9df895883ec445`
(26 novembre 2026). Marqueur `SYRACUSE_INDEPENDENT_REVIEW`. Elle confirme les
seuils stricts de l'extension, l'invariance par préfixe fini et X20. Ce n'est
pas une seconde preuve. Elle demande de justifier le seuil, ou de retirer
l'annonce qui dépassait l'argument de premier ordre.

- Les cas $\lambda>\log_2 3$ et $1<\lambda<\log_2 3$ restent ceux du §8 :
  $Q_k/o_k$ a pour limite $\lambda-\log_2 3$, strictement positive ou
  strictement négative. Le script ne les recalcule pas. La borne
  $N\ge2^{k-1}$, le témoin $422$ et $T(-1)=-1$ sont inchangés.
- L'argument $r_k/o_k\to\beta$ ne décide pas du signe de $r_k-\beta o_k$.
  La proposition du §8 ajoute les deux familles $r_1=64$ et, pour $k\ge2$,
  $r_k=\lfloor\beta o_k\rfloor\pm\lfloor\sqrt{o_k}\rfloor$. Les deux ont
  $r_{k+1}/r_k\to\log_2 3$. Le signe plus donne $Q_k\to+\infty$, donc
  l'irrationalité par B7. Le signe moins donne $Q_k\to-\infty$ : B7 ne
  s'applique pas, et l'irrationalité de cette famille reste ouverte.
- Le texte annonçait que le script vérifie, pour $2\le k\le16$, $Q_k>k$ au
  signe plus et $Q_k<0$ au signe moins. La comparaison du signe moins était
  bien $2^{o_k+r_k+k+1}<3^{o_k}+P_k$. Celle du signe plus utilisait
  l'exposant $o_k+r_k+k+1$, donc $Q_k>0$. Le §14 aligne le signe plus sur
  $Q_k>k$. Le segment ne remplace pas la preuve. La borne
  $\lfloor\beta o\rfloor=\lfloor\log_2(3^o)\rfloor-o$ et $h(o)\ge0$ restent
  celles du script.
- Aucune source supplémentaire n'a été lue pour ces familles. L'argument
  est élémentaire et interne à B7. Il ne revendique pas d'antériorité, et
  il ne dit rien de (C) ni de Syracuse.

La proposition du seuil est **PROUVÉE** par le §8. Le signe plus est un cas
particulier d'irrationalité. Le signe moins est une limite où le critère est
aveugle, pas une rationalité. X20 n'est pas modifié. La prochaine question
de l'agenda n'est pas abordée. La comparaison annoncée du script et la
phrase sur les orbites sont reprises au §14.

## 14. Revue `6081622758`

Revue indépendante sur le SHA `3bdc5daa042aef655c84e4ea36d16c55774f5a6c`
(26 novembre 2026). Marqueur `SYRACUSE_INDEPENDENT_REVIEW`. Elle confirme la
proposition du seuil. Ce n'est pas une seconde preuve. Elle signale trois
écarts de portée : l'inégalité stricte sur $w_{16+t}$, ce que le test du
signe plus vérifie, et la phrase qui refusait aux deux familles le statut
d'itinéraire entier.

- Dans la preuve, $w_{16+t}>w_{16}\cdot(11/10)^t$ pour $t\ge0$ est faux en
  $t=0$ : les deux membres sont égaux. Le rapport
  $w_{m+1}/w_m\ge320/289>11/10$ pour $m\ge16$ reste vrai
  ($3200>3179=11\cdot289$). L'inégalité écrite est désormais
  $w_{16+t}\ge w_{16}\cdot(11/10)^t$, avec égalité en $t=0$. La limite
  $w_m\to+\infty$ est inchangée. Pour $k\ge2$, la borne déjà écrite
  $Q_k>\lfloor\sqrt{o_k}\rfloor+k-5$ et $\lfloor\sqrt{o_k}\rfloor\ge8$
  donnent $Q_k>k+3$. C'est une conséquence du §8, pas un contrôle fini.
- Le test du signe plus comparait $2^{o_k+r_k+k+1}$ à $3^{o_k}+P_k$. D'après
  la forme entière du cycle 003, avec $E=o_k+r_k+k+1-L$, c'est $Q_k>0$, pas
  $Q_k>k$. Les deux exposants diffèrent de $k$. Hors famille, $o=0$, $r=1$,
  $k=3$ et $P=4$ donnent $2^5>5$ et $2^2<5$. Le script compare désormais
  $2^{o_k+r_k+1}$ à $3^{o_k}+P_k$ pour le signe plus, et conserve
  $2^{o_k+r_k+k+1}$ pour le signe moins. Les §§10 et 13 décrivent ces
  exposants. Le segment $2\le k\le16$ ne remplace pas la preuve.
- La phrase « aucune des deux familles n'est une orbite d'entier positif »
  ne suit pas de ce qu'elles sont des mots infinis : l'itinéraire d'un
  entier positif est un mot infini. Le signe plus est exclu par B7, parce
  que son réalisateur est irrationnel. Le signe moins a $Q_k\to-\infty$ :
  cette preuve n'exclut aucune classe de réalisateurs. Les inverses
  $x=2T(x)$ et $x=(2T(x)-1)/3$ restent des bijections de $\mathbb Q$ pour
  les deux signes. Seule l'irrationalité du signe moins reste ouverte.
  Bernstein–Lagarias 1996, §1, (1.5)–(1.6), est cité par la revue pour le
  sens de la correspondance mot/réalisateur. Ce passage n'a pas été relu
  ici et n'est pas une prémisse : l'exclusion des entiers positifs au signe
  plus utilise seulement B7 et la rationalité de ces entiers.

Contrôle indépendant, distinct du script, pour $2\le k\le18$ : $P_k$ par sa
somme directe coïncide avec la récurrence, $2^{o_k+r_k+1}>3^{o_k}+P_k$ et
$2^{o_k+r_k-2}>3^{o_k}+P_k$ au signe plus, et
$2^{o_k+r_k+k+1}<3^{o_k}+P_k$ au signe moins. Ce segment n'est pas la preuve.
Le script du dépôt s'arrête à $k=16$, comme annoncé. Aucune source
supplémentaire n'a été lue. Ce n'est pas un nouveau cycle. La prochaine
question de l'agenda n'est pas abordée.

## 15. Revue `6081702521`

Revue indépendante sur le SHA `7120654a69a0bd4849816b2e83a60dfbf79d6d77`
(26 novembre 2026). Marqueur `SYRACUSE_INDEPENDENT_REVIEW`. Elle confirme les
comparaisons corrigées et la portée du §8. Ce n'est pas une seconde preuve,
ni une correction.

- Le signe plus compare $2^{o_k+r_k+1}$ à $3^{o_k}+P_k$, donc $Q_k>k$. Le
  signe moins conserve $2^{o_k+r_k+k+1}$, donc $Q_k<0$. Les §§10 et 14
  décrivent ces exposants. Pour $k\ge2$, la borne écrite donne déjà
  $Q_k>k+3$. L'inégalité $w_{16+t}\ge w_{16}\cdot(11/10)^t$ reste large,
  avec égalité en $t=0$.
- Pour le signe moins, $Q_k\to-\infty$ laisse B7 inapplicable. Les inverses
  affines conservent la rationalité dans les deux sens. L'irrationalité de
  cette famille reste ouverte. Le texte du §8 dit déjà cela : aucune phrase
  n'est à reprendre.
- Le segment $2\le k\le16$ du script et le contrôle jusqu'à $k=18$ ne sont
  pas la preuve. Aucune source supplémentaire n'a été lue.

La proposition du seuil, X20 et B9 restent dans l'état du §14. Cette
confirmation ne modifie pas le cycle 004. La question suivante est le
cycle 005.
