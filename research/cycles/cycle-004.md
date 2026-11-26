# Cycle 004 — Runs de Fibonacci et critère de Liouville

Date : 26 novembre 2026. Axe **B**.
Branche : `research/memory`. Script : [`../checks/cycle004_fibonacci.py`](../checks/cycle004_fibonacci.py).

**Verdict : PROUVÉ.** Pour le mot dont les runs impairs ont longueurs
$F_3,F_4,F_5,\ldots=2,3,5,8,\ldots$, on a $Q_k>k$ pour tout $k\ge1$ (B9).
Donc $Q_k\to+\infty$ et B7 s'applique : le réalisateur 2-adique est irrationnel.
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
En particulier $o_k+r_k=F_{k+4}-3$. C'est la quantité $S_{k-1}$ de l'agenda.
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

**Préfixe entier.** Si un entier $N>0$ a ses $k$ premiers runs impairs égaux à
$F_3,\ldots,F_{k+2}$, son itinéraire commence par
$\prod_{j=1}^{k}(0\,1^{F_{j+2}})\,0$. Les quantités $o_j$, $r_k$ et $P_k$
coïncident avec celles de $w$, donc $Q_k>k$. Pour $\xi=N$,
$\sigma=-2(N+1)$ en forme réduite de dénominateur $1$, et B7 donne
$Q_k\le\log_2\bigl(2(N+1)\bigr)$. Donc $k<\log_2\bigl(2(N+1)\bigr)$, soit
$2^{k-1}<N+1$. Comme $N+1$ est entier, $N\ge2^{k-1}$.

Cette borne est grosse. Elle dit seulement qu'un entier trop petit ne peut pas
suivre le préfixe. Le script calcule, pour $k\le8$, le plus petit entier
positif du préfixe : il satisfait la borne, et il est bien plus grand
($k=8$ : un entier de $148$ bits, contre la borne $2^{7}$). Ce calcul borne
cherche un contre-exemple ; il ne renforce pas la constante.

**Densité.** Après $K$ blocs il y a $K$ zéros et $F_{K+4}-3$ uns. La densité
des $1$ vaut $1$. Comme pour B8, ce n'est pas un corollaire de
Monks–Yazinski 2004, théorème 2.7(b), qui borne inférieurement la densité des
$1$ d'une orbite rationnelle divergente.

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
  n'est pas sturmien.
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

## 8. Ce que ce cycle ne montre pas

Rien sur (C), rien sur (H), rien sur une orbite entière infinie. B9 dit que
le mot infini n'est l'itinéraire d'aucun rationnel, et que ses préfixes exacts
exigent $N\ge2^{k-1}$. Un entier peut suivre d'autres suites de runs croissant
comme $\varphi$. Les runs quasi linéaires, ceux pour lesquels $r_m/o_m\to0$ et
$Q_m$ peut tendre vers $-\infty$, restent H5. Le critère ne s'arrête pas avant
$\varphi$ : c'est l'autre branche de l'agenda qui est fermée.

## 9. Mises à jour

- `proved.md` : B9.
- `hypotheses.md` : H3 gagne le cas Fibonacci ; H4 enregistre ce second cas non vide.
- `abandoned.md` : la branche « $Q_k$ bornée avant $\varphi$ » est fermée.
- `prior_art.md` : lectures de ce cycle, marquées [S] quand le texte n'a pas été lu.
- `agenda.md` : prochaine question sur l'axe A (H6). Quatre cycles consécutifs
  ont porté sur l'axe B.

## 10. Reproduire

```sh
python3 research/checks/cycle004_fibonacci.py
```

Sortie attendue : huit lignes `PASS`. Les puissances testées s'arrêtent à
$F_{21}$ et aux préfixes $k\le8$. Elles contrôlent le lemme, la récurrence de
$P$ et l'absence de petit contre-exemple entier. La preuve est le §4.
