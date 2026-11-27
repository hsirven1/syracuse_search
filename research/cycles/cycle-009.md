# Cycle 009 — Signe moins au seuil $\log_2 3$ : hauteur, pas de réduction

Date : 27 novembre 2026. Axe **B**.
Branche : `research/memory`. Script : [`../checks/cycle009_minus_sign.py`](../checks/cycle009_minus_sign.py).

**Verdict : l'irrationalité reste OUVERTE. Deux obstructions sont prouvées,
et une borne de hauteur.**
Le mot n'est pas ultimement périodique (X24). La fonction $o_j$ n'est pas
polynomiale, même à $O(\log)$ près, sur aucune progression arithmétique :
il n'y a pas de réduction terme à terme du type B2 ou B11 (X25). Si la
somme de réalisation $\sigma=a/b$ est rationnelle irréductible avec $b>0$,
alors $v_2(a-2b)=66$ et $\max(|a|,b)\ge(2^{66}+2)/3>2^{64}$ (B14). La
valuation exclut aussi des hauteurs supérieures, par exemple $2+2^{67}$
(X27). La borne de hauteur, seule, ne tranche pas au-dessus du seuil.
Ce n'est pas une exclusion de $\mathbb Q$, ni une preuve de Syracuse.
B7 n'est pas réutilisé pour conclure : son hypothèse $\sup Q_m=+\infty$
est fausse sur ce mot.

## 0. Question traitée, et porte d'antériorité

Première entrée de l'agenda, après la revue `6082253067` sur le SHA
`e7c52409dc609e2027ac8dbebd7071b0dc1c547e`. Cette revue confirme B13.
Elle est enregistrée au §7. Elle ne demande aucune correction. Le cycle
008 n'est pas réécrit.

**Candidat.** Pour le mot du cycle 004 §8 à un zéro par bloc, avec
$r_1=64$ et, pour $k\ge2$,
$r_k=\lfloor\beta o_k\rfloor-\lfloor\sqrt{o_k}\rfloor$, la réalisation
$\xi_w$ est-elle hors de $\mathbb Q$ ?

**Obstacle.** $Q_k\to-\infty$, déjà prouvé au cycle 004 §8. B7 ne
s'applique pas.

**Intérêt.** Un cas de la conjecture de périodicité H3 : ce mot-ci ne
serait l'itinéraire d'aucun rationnel de $\mathbb Z_{(2)}$. Cela ne
contraint pas une trajectoire arbitraire. Le mot est construit pour que
le critère disponible échoue.

**Résultat le plus proche.** H3, ouverte. La direction facile (mot
ultimement périodique $\Rightarrow$ rationnel) est classique. B2 exclut
les runs en progression arithmétique, par VW 1989. B7 exclut $\sup Q=+\infty$,
donc le signe plus du même paragraphe. B11 est une autre forme quadratique,
sur un autre mot. Le cycle 006 a déjà noté qu'un run non borné n'implique
pas l'irrationalité.

**Écart.** Ici $r_{k+1}/r_k\to\log_2 3$, pas vers $1$. Les runs croissent
exponentiellement. Ce n'est pas un corollaire de B2 ni de B7.

**Classification.** Cas particulier ouvert de H3. Une recherche ciblée
(mémoire du dépôt, énoncé de la conjecture dans le HTML d'arXiv:1805.00133,
annonces sturmiennes non lues) ne fournit pas ce mot comme théorème publié.
Les annonces sturmiennes ne sont pas des prémisses : le §5 montre que le
mot n'est pas équilibré. Classification du verdict d'irrationalité :
**PRIOR ART UNVERIFIED** quant à une preuve publiée de ce cas, et
**NO-GO** pour une tentative qui conclurait $\xi_w\notin\mathbb Q$ avec
les seuls outils déjà lus. La partie exécutée est celle que l'agenda
demandait : queue périodique, puis forme de la série.

Aucun second candidat n'a été calculé. Une autre famille de mots de
parité ne serait pas un progrès sur les trajectoires arbitraires.

## 1. Le mot

$T(n)=n/2$ si $n$ est pair, $(3n+1)/2$ si $n$ est impair. Le mot est
$w=\prod_{k\ge1}(0\,1^{r_k})$, avec $o_1=0$, $o_{k+1}=o_k+r_k$, $r_1=64$
et, pour $k\ge2$,
$$
r_k=\lfloor\beta o_k\rfloor-\lfloor\sqrt{o_k}\rfloor,
\qquad\beta=\log_2(3/2).
$$
La formule B1 donne
$$
\sigma=-2(\xi_w+1)=\sum_{j\ge1}\frac{2^{j+o_j}}{3^{o_j}}\in\mathbb Z_2.
$$
Le cycle 004 §8 donne, pour $k\ge2$, $r_k>o_k/4$, $o_k\to+\infty$ et
$r_{k+1}/r_k\to\log_2 3$. De $8<9$ on tire $\log_2 3>3/2$.

## 2. Pas de queue périodique (X24)

**Lemme.** Pour $k\ge2$, $r_k>o_k/4$ et $r_k\to+\infty$. Le mot $w$
contient une infinité de zéros et n'est pas ultimement périodique.

Le cycle 004 §8 donne $r_k>o_k/4$ et $o_k\to+\infty$ pour $k\ge2$, donc
$r_k\to+\infty$. Chaque bloc est $0\,1^{r_k}$, donc il y a une infinité
de zéros.

Supposons qu'à partir d'un indice la suite des symboles soit périodique
de période $p\ge1$. Cette queue contient encore une infinité de zéros,
donc un bloc de période contient au moins un zéro. Aucun run de $1$
contenu dans la queue n'a alors longueur $\ge p$ : $p$ uns consécutifs
couvriraient toutes les positions modulo $p$, et le bloc serait $1^p$.
Comme $r_k\to+\infty$, tous les runs de $1$ sauf un nombre fini ont
longueur $\ge p$. Un seul peut chevaucher le début de la queue. L'un
des autres est donc contenu dans la queue. Contradiction.

La phrase « tout mot binaire ultimement périodique a des runs bornés
par la longueur d'une période » est fausse. Le mot $1^\infty$ a la
période $1$ et un run infini (X26). La preuve ci-dessus n'utilise pas
cette phrase : elle utilise les zéros de $w$.

La réciproque de l'implication « itinéraire ultimement périodique
$\Rightarrow$ réalisation rationnelle » est la conjecture H3. Elle n'est
pas réfutée : aucun rationnel de $\mathbb Z_2$ à itinéraire apériodique
n'est produit. L'apériodicité de $w$ n'entraîne pas
$\xi_w\notin\mathbb Q$. Le cycle 006 §2 le dit déjà pour un autre mot.
Les réalisations $(1^d0)^\infty$, pour $c=0$, restent hors de ce mot.
Bernstein–Lagarias 1996, §1, (1.5)–(1.6), cité par la revue
`6082358798`, n'a pas été relu et n'est pas une prémisse.

## 3. Borne de hauteur (B14)

**Proposition.** Si $\sigma=a/b$ en fraction irréductible, $b>0$, alors
$$
|a-2b|\ge2^{66}
\qquad\text{et}\qquad
\max(|a|,b)\ge\frac{2^{66}+2}{3}>2^{64}.
$$
En particulier $\sigma\neq2$. Cette valuation exclut aussi des
rationnels de hauteur supérieure au seuil. Pour $a=2+2^{67}$ et $b=1$,
$v_2(a-2b)=67\neq66$ et $\max(|a|,b)=2+2^{67}>(2^{66}+2)/3$ (X27). La
borne de hauteur, à elle seule, ne tranche pas au-dessus du seuil :
$a=2+2^{66}$ et $b=1$ satisfont $v_2(a-2b)=66$ et
$\max(|a|,b)=2+2^{66}>(2^{66}+2)/3$.

**Preuve.** On reprend le calcul de valuation du cycle 003 §2 au seul
rang $m=1$, sans l'hypothèse $\sup Q=+\infty$. Ici $o_1=0$, $G_1=2$,
$P_1=2$ et $A_1=a-2b$. Le reste vérifie, dans $\mathbb Q_2$,
$$
3^{o_2}(\sigma-G_1)=\sum_{j\ge2}2^{j+o_j}3^{o_2-o_j}.
$$
Le terme $j=2$ exige $o_2$. Or $3^{32}=1853020188851841$ et
$$
3^{64}=3433683820292512484657849089281,
$$
avec $2^{101}\le3^{64}<2^{102}$. Donc $\lfloor\log_2(3^{64})\rfloor=101$ et
$$
\lfloor\beta\cdot64\rfloor=101-64=37.
$$
Comme $\lfloor\sqrt{64}\rfloor=8$, on a $r_2=37-8=29$ et $o_2=r_1=64$,
$o_3=93$. Le terme $j=2$ vaut $2^{66}$. Pour $j\ge3$,
$$
j+o_j\ge3+o_3=96>66.
$$
La valuation du membre de gauche est donc $66$. Il vaut
$3^{64}(a-2b)/b$, et $b$ comme $3$ est impair, donc
$v_2(a-2b)=66$. Ainsi $a-2b\neq0$ et $|a-2b|\ge2^{66}$.

Soit $M=\max(|a|,b)$. Alors $|a-2b|\le|a|+2b\le3M$. Si
$M\le(2^{66}-1)/3$, on aurait $3M\le2^{66}-1$, contradiction. Or
$2^2=4\equiv1\pmod3$ et $66$ est pair, donc $2^{66}\equiv1\pmod3$. Ainsi
$(2^{66}-1)/3$ est entier et
$$
M\ge\frac{2^{66}-1}{3}+1=\frac{2^{66}+2}{3}.
$$
Enfin $2^{66}+2-3\cdot2^{64}=2^{64}+2>0$, donc cette borne dépasse
$2^{64}$.

Le cas $(a,b)=(2,1)$ donne $A_1=0$, dont la valuation n'est pas $66$.
Pour la série elle-même, au rang $m=2$, le terme $j=3$ vaut $2^{96}$.
Pour $j\ge4$, $j+o_j\ge4+o_4$. Comme $r_3>o_3/4>0$, on a
$o_4\ge o_3+1$ et $4+o_4\ge98>96$. La valuation du reste est donc $96$,
et $v_2(A_2)=96$ dès que $b$ est impair. Pour le candidat $\sigma=2$,
$P_2=2\cdot3^{64}+2^{66}$ et $A_2=2\cdot3^{64}-P_2=-2^{66}$, de
valuation $66\neq96$. C'est l'écart du candidat, pas une exception à
$v_2(A_m)=m+1+o_{m+1}$. ∎

Le rang $m=2$ ne sert qu'à séparer le candidat $\sigma=2$ du reste de la
série. La comparaison archimédienne des rangs suivants n'est pas reprise.
Le cycle 004 montre déjà $Q_k\to-\infty$ : elle devient plus faible que
la borne ci-dessus, et elle ne devient jamais une exclusion.

## 4. Pas de forme polynomiale, donc pas de réduction terme à terme (X25)

**Lemme.** Soit $\lambda=\log_2 3$ et $M\ge1$. Les sommes de $M$ runs
consécutifs $\Delta(n)=r_n+\cdots+r_{n-M+1}$ vérifient
$\Delta(n+M)/\Delta(n)\to\lambda^M$. Comme $\lambda>3/2$, cette limite
est strictement supérieure à $1$.

**Preuve.** Le cycle 004 §8 donne $r_{k+1}/r_k\to\lambda$. Fixons $i$
avec $0\le i<M$. Pour $n>i$,
$$
\frac{r_{n-i}}{r_n}
=\Biggl(\prod_{s=0}^{i-1}\frac{r_{n-s}}{r_{n-s-1}}\Biggr)^{-1}.
$$
Chaque facteur tend vers $\lambda$, donc le rapport tend vers
$\lambda^{-i}$. Ainsi
$$
\frac{\Delta(n)}{r_n}\to\sum_{i=0}^{M-1}\lambda^{-i}=:c_M>0.
$$
Le même calcul en $n+M$, et le produit de $M$ rapports consécutifs,
donnent $r_{n+M}/r_n\to\lambda^M$ et $\Delta(n+M)/r_{n+M}\to c_M$. Donc
$\Delta(n+M)/\Delta(n)\to\lambda^M$. ∎

**Corollaire.** Soit une progression arithmétique d'indices de raison
$M\ge1$. La suite des incréments de $o_j$ le long de cette progression
n'est pas de la forme $P(t)+\theta_t$, où $P\in\mathbb Q[t]$ et
$|\theta_t|\le K\log(t+2)$. En particulier $o_j$ n'est pas polynomiale sur
cette progression.

Si $\deg P\ge1$, le terme $\theta_t$ est négligeable devant $P(t)$, et
le rapport des incréments tend vers $1$, pas vers $\lambda^M$. Si
$\deg P\le0$, l'incrément est $O(\log t)$. Or, pour $\eta$ avec
$3/2<\eta<\lambda$, on a $r_{k+1}>\eta r_k$ à partir d'un rang, donc
$r_n$ croît au moins géométriquement et $\Delta(n)\ge r_n$ aussi. Ce
n'est pas un $O(\log t)$. ∎

B2 écrit $o_j=c\,j(j+1)/2+dj$, polynôme sur la progression de raison $1$.
B11 écrit $o_{2m-1}=2m^2$ et $o_{2m}=2m(m+1)$, polynômes sur les
progressions paires et impaires. Les deux formes sont exclues. Un facteur
polynomial $n^{\tau}$ devant un terme $q^{-n(n+1)/2}\alpha^n$ ne change
la valuation $3$-adique que d'un $O(\log n)$ : la même obstruction
s'applique à une identification terme à terme avec un jet de fonction
de Tschakaloff indexé par une progression arithmétique.

Cette obstruction ne dit pas que $\sigma$ diffère, dans $\mathbb Q_2$,
de toute combinaison linéaire de valeurs de Tschakaloff. Deux séries de
rationnels distinctes peuvent converger vers le même élément de
$\mathbb Q_2$. Aucune identité de ce type n'a été trouvée, et VW 1989
n'est pas appliqué. Les dérivées du Satz ne sont pas relues : l'énoncé
déjà transcrit dans `prior_art.md` porte sur des arguments $\alpha_j$
dont les exposants restent quadratiques en l'indice entier $n$.

## 5. Le mot n'est pas équilibré

Le cycle 004 donne $r_k>o_k/4$ pour $k\ge2$. On en tire la chaîne
entière suivante. $o_2=64$, donc $r_2\ge17$ et $o_3\ge81$. Puis
$r_3\ge21$, $o_4\ge102$, $r_4\ge26$, $o_5\ge128$, $r_5\ge33$,
$o_6\ge161$, $r_6\ge41$, $o_7\ge202$, $r_7\ge51$, $o_8\ge253$,
$r_8\ge64$, $o_9\ge317$, et $r_9\ge80$.

Le préfixe $0\,1^{64}\,0$ a longueur $66$ et contient $64$ uns. Le run
$r_9\ge80$ contient un facteur $1^{66}$, qui a $66$ uns. Deux facteurs
de longueur $66$ dont les nombres de uns diffèrent de $2$ : le mot n'est
pas équilibré, donc il n'est pas sturmien.

Les manuscrits qui annoncent l'irrationalité des mots sturmiens n'ont
pas été lus. Le décompte ci-dessus montre qu'ils ne contiennent pas ce
mot, même si leurs énoncés sont exacts. Ils ne sont pas des prémisses.

Le script calcule en outre les valeurs exactes $r_2=29$, $r_3=45$,
$r_4=69$. La chaîne $r_9\ge80$ suffit à la preuve ; ces valeurs n'en
font pas partie.

## 6. Ce que ce cycle ne montre pas

- $\xi_w\notin\mathbb Q$, ni $\sigma\notin\mathbb Q$. Parmi les fractions
  irréductibles $a/b$ avec $b>0$ impair et $v_2(a-2b)=66$, la borne de
  hauteur laisse ouvertes celles qui vérifient
  $\max(|a|,b)\ge(2^{66}+2)/3$. Elle n'épargne pas toute hauteur
  supérieure : $2+2^{67}$ est exclu par la valuation (X27).
- Une application de VW 1989, de Bundschuh 1974, ou de B7. Le mot du
  cycle 006 n'est pas rouvert.
- L'égalité réelle de la série et son égalité $2$-adique. X14 reste en
  vigueur : un signe ou une transcendance réels ne passent pas à
  $\mathbb Q_2$.
- Rien sur (C), sur (H), ni sur la conjecture de Syracuse.

## 7. Revue `6082253067`

Revue indépendante sur le SHA
`e7c52409dc609e2027ac8dbebd7071b0dc1c547e` (PR #27), c'est-à-dire sur
le correctif de B13. Le verdict est que l'implication reste prouvée, y
compris la convention $t_*$ pour $K\le1/2$, l'identité
$K\cdot2^t>3^R$, la constante $C=\log_2 K+J(\log_2 3)^2$, et la
comparaison avec la forme uniforme de B10. Aucune correction n'est
demandée. Le cycle 008 n'est pas modifié. Le contrôle JavaScript décrit
par la revue, jusqu'à $L=60$ puis $L=25$, n'est pas repris : la preuve
du cycle 008 est déjà écrite pour tout $K>0$. Applegate–Lagarias 2003
n'est pas relu.

## 8. Antériorité

La limite $r_{k+1}/r_k\to\log_2 3$ et l'inégalité $r_k>o_k/4$ sont le
cycle 004 §8. La valuation $v_2(A_m)=m+1+o_{m+1}$ est le mécanisme du
cycle 003 §2, appliqué ici au seul rang $m=1$. B2 et B11 fournissent
les deux formes polynomiales exclues. H3 est inchangée dans son énoncé
général.

Lecture de ce cycle : le HTML public d'arXiv:1805.00133, assez pour y
retrouver la conjecture de périodicité comme conjecture, pas comme
théorème. Ce n'est pas une prémisse, et le PDF n'a pas été certifié.
Aucune autre source primaire n'a été ouverte. Les annonces sturmiennes
rencontrées dans la recherche (SSRN, arXiv:2610.02601) n'ont pas été lues.

## 9. Mises à jour de la mémoire

- `proved.md` : B14, borne de hauteur seulement.
- `counterexamples.md` : X24, X25.
- `hypotheses.md` : H3 et H4, irrationalité toujours ouverte.
- `prior_art.md` : pas de théorème nouveau adopté.
- `abandoned.md` : ne pas relancer ce mot sans outil nouveau.
- `agenda.md` : prochaine question sur l'axe A.
- `reviews.md` : revues `6082253067` et `6082358798`.

## 10. Prochaine question

Axe **A**, un seul énoncé. Les mots de parité construits pour saturer
B7 ou VW ne contraignent pas les trajectoires arbitraires : ce cycle
ferme l'attaque prévue sur le signe moins sans exclure $\mathbb Q$.

Pour $k\ge2$ et $a=5$, l'entier $n_k=5\cdot2^k-1$ est congru à $3$
modulo $4$. Le pas accéléré
$U(n)=(3n+1)/2^{v_2(3n+1)}$ vérifie donc $U(n_k)>n_k$. Le temps
$\tau(n_k)=\min\{t\ge1:U^t(n_k)<n_k\}$ admet-il une borne explicite en
$k$, donnée par une trajectoire en forme close, ou la montée dépasse-t-elle
$2k$ pas accélérés pour des $k$ arbitrairement grands ?

Écarter $a=1$ (montée de Mersenne, déjà dans le dépôt) et la classe
$n\equiv1\pmod4$ pour $n>1$, qui descend en un pas de $U$. Pour
$n=4m+1$ avec $m\ge1$, $3n+1=4(3m+1)$, donc $v_2(3n+1)\ge2$ et
$U(n)\le(3n+1)/4$. L'inégalité $(3n+1)/4<n$ équivaut à $n>1$. Le cas
$n=1$ n'est pas une descente : $3\cdot1+1=4$ et $U(1)=1$. Ne pas
rouvrir le mot du signe moins, le mot du cycle 006, B10, B13 ni X21.
Si aucun mécanisme clos n'apparaît après l'antériorité et un
contre-exemple borné, s'arrêter. Ce cycle n'est pas engagé tant que
la revue `6082358798` n'a pas été revue à nouveau.

## 11. Reproduire

```sh
python3 research/checks/cycle009_minus_sign.py
```

Sortie attendue : six lignes `PASS`. Elles couvrent $3^{64}$ et
$\lfloor64\log_2(3/2)\rfloor=37$, la chaîne $r_9\ge80$ avec $r_4\ge66$,
les deux facteurs de longueur $66$, les neuf premiers runs et
$4r_k>o_k$ pour $2\le k\le18$, le candidat $\sigma=2$ avec
$v_2(A_2)=66\neq96$, les témoins $2+2^{67}$ et $2+2^{66}$, la constante
$(2^{66}+2)/3>2^{64}$, et $U(1)=1$. L'irrationalité n'est pas un
contrôle du script : elle reste ouverte.

## 12. Revue `6082358798`

Revue indépendante sur le SHA
`886b3059d09f30a5a349b9423455697f408f4333` (PR #27). B14, X24 dans la
portée corrigée, et X25 sont confirmés. Quatre phrases sont corrigées
dans cette révision.

La majoration des runs de tout mot ultimement périodique est fausse
pour $1^\infty$ (X26). La preuve de X24 passe par l'infinité de zéros.
« La réciproque est fausse » est retiré : la réciproque est la
conjecture H3. Bernstein–Lagarias 1996 n'a pas été relu.
« Cela n'exclut aucun rationnel de hauteur supérieure » est faux :
$2+2^{67}$ a une hauteur supérieure et $v_2(a-2b)=67$ (X27). La fraction
$2+2^{66}$ montre que la borne de hauteur seule ne tranche pas au-dessus
du seuil. Au §10, la descente $n\equiv1\pmod4$ est restreinte à $n>1$,
car $U(1)=1$.

L'irrationalité du mot reste ouverte. Le cycle 010 n'est pas engagé :
ces corrections attendent une nouvelle revue. Le contrôle indiqué par
la revue est repris pour les neuf premiers runs, l'inégalité
$4r_k>o_k$ jusqu'à $k=18$, la valuation $96$ et les deux témoins de
hauteur. Ce segment fini n'est pas la preuve. Le décompte des fenêtres
de longueur $66$ n'est pas repris : le facteur $1^{66}$ suit déjà de
$r_9\ge80$.
