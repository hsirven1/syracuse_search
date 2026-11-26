# Cycle 004 — Runs de Fibonacci et critère de Liouville

Date : 26 novembre 2026. Axe **B**.
Branche : `research/memory`. Script : [`../checks/cycle004_fibonacci.py`](../checks/cycle004_fibonacci.py).

**Verdict : PROUVÉ.** Pour le mot dont les runs impairs ont longueurs
$F_3,F_4,F_5,\ldots=2,3,5,8,\ldots$, on a $Q_k>k$ pour tout $k\ge1$ (B9).
Donc $Q_k\to+\infty$ et B7 s'applique : le réalisateur 2-adique est irrationnel.
Si l'itinéraire d'un entier positif commence par le préfixe exact, alors
$N\ge2^{k-1}$. Les seules longueurs de ces runs ne donnent pas ce préfixe (X20).
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
$182$.

**Runs impairs finis.** Pour $n$ impair, $n+1=2^v m$ avec $v\ge1$ et $m$ impair,
donc $T(n)+1=3(n+1)/2$ et $v_2(T(n)+1)=v-1$. Le run impair issu de $n$ a
longueur $v_2(n+1)$. Un entier positif a une valuation $v_2(N)$ finie : l'orbite
atteint un impair, puis un run impair fini, puis un pair, et ceci se répète.
L'itinéraire contient une infinité de zéros. L'hypothèse de B7 est donc
satisfaite par toute orbite d'entier positif. Elle ne fixe pas les longueurs
des zéros entre les runs.

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

Ce corollaire ferme la lecture où un entier suivrait une autre suite infinie
de runs de rapport $\varphi$, avec un seul zéro par bloc. Il reste deux
lectures ouvertes. Un préfixe fini est réalisable, avec la borne du §5 dans
le cas de Fibonacci. Un placement différent des zéros — plusieurs zéros entre
les runs, ou un mot qui commence par $1$ — n'entre pas dans l'énoncé. Il n'y
a pas de conclusion uniforme lorsque $r_{k+1}/r_k\to\lambda$ avec
$\lambda-1\le\beta$. Les runs quasi linéaires, ceux pour lesquels
$r_m/o_m\to0$, restent H5.

Le corollaire n'utilise que B7, l'identité $s_{k+1}=(s_k+1)/q_k$ et la
comparaison $\varphi-1>\beta$ du §2. Il ne repose pas sur un théorème
supplémentaire. Le script contrôle une famille décalée $r_k=F_{k+2}+1$
jusqu'à $k=12$ ; ce segment ne remplace pas la preuve.

## 9. Mises à jour

- `proved.md` : B9.
- `hypotheses.md` : H3 gagne le cas Fibonacci ; H4 enregistre ce second cas non vide.
- `abandoned.md` : la branche « $Q_k$ bornée avant $\varphi$ » est fermée.
- `prior_art.md` : lectures de ce cycle, marquées [S] quand le texte n'a pas été lu.
- `agenda.md` : prochaine question sur l'axe A (H6). Quatre cycles consécutifs
  ont porté sur l'axe B.
- Revue `6081410834` : X20, indice $S_{k-1}$, et le corollaire du §8.
  La prochaine question de l'agenda n'est pas entamée. Détail en §11.

## 10. Reproduire

```sh
python3 research/checks/cycle004_fibonacci.py
```

Sortie attendue : onze lignes `PASS`. Les puissances testées s'arrêtent à
$F_{21}$, aux préfixes $k\le8$ et à la famille décalée $k\le12$. Elles
contrôlent le lemme, la récurrence de $P$, les témoins de X20 et l'absence de
petit contre-exemple au préfixe exact. La preuve de B9 est le §4. La preuve
du corollaire est le §8.

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
prochaine question de l'agenda n'est pas abordée.
