# Cycle 001 — Mots de parités à runs en progression arithmétique

Date : 26 novembre 2026. Axe **B** (contraintes d'intégralité réel ↔ 2-adique).
Branche : `research/memory`. Script : [`../checks/cycle001_linear_runs.py`](../checks/cycle001_linear_runs.py).

**Verdict : lemme DÉMONTRÉ, sous réserve de la preuve publiée de Väänänen–Wallisser (1989).
Énoncé primaire du théorème relu sur le scan original pendant l'initialisation.
Aucune revendication de nouveauté : c'est une application d'un théorème publié.
Ni la conjecture (C) de densité, ni Syracuse ne sont démontrées.**

## 0. Question traitée (tête de l'agenda au début du cycle)

> Le mot triangulaire `10 110 1110 …` (PR #23–#24, non fusionnées) est-il exclu
> inconditionnellement, et la méthode s'étend-elle à une famille infinie de mots
> à densité nulle de pas pairs ?

Contexte. La PR #24 réduisait l'exclusion du mot triangulaire à l'irrationalité
de $f_{3/2}(2)$ dans $\mathbb Q_2$, en laissant ouverte une condition possible
sur $\alpha=2$ dans le théorème de Väänänen–Wallisser (VW 1989). Pendant
l'initialisation, le volume *Manuscripta Math.* 65 a été téléchargé depuis GDZ
Göttingen (SHA-256 `33d6870dba004ac09023ab8356466a5e3ef36bfd9db9e94d08cd6cded8b60ab2`,
pages imprimées 199–202 = indices 201–204 du PDF) ; l'énoncé du Satz (pp. 200–201)
est transcrit dans [`../prior_art.md`](../prior_art.md#vw1989). **Il n'impose
aucune condition sur $\alpha$ autre que $\alpha\in\mathbb Q^\times$** (et des
conditions sur les rapports $\alpha_i/\alpha_j$, vides pour $l=1$).

## 1. Énoncé (hypothèses explicites)

Application raccourcie $T(x)=x/2$ si $x$ pair, $(3x+1)/2$ si $x$ impair, sur
$\mathbb Z_2$. Tout mot $w\in\{0,1\}^{\mathbb N}$ est l'itinéraire de parités
d'un unique $\xi_w\in\mathbb Z_2$ (codage de Terras/Everett ; $w_t=1$ ssi $T^t(\xi)$ impair).

**Lemme C1.** Soient $c\ge1$ et $d\ge-c$ des entiers, $u\in\{0,1\}^k$ ($k\ge0$)
un mot fini quelconque, et
$$w=u\,(1^{r_1}0)(1^{r_2}0)(1^{r_3}0)\cdots,\qquad r_j=cj+d .$$
Alors $\xi_w\notin\mathbb Q$. En particulier **aucun entier (positif ou négatif)
et aucun rationnel à dénominateur impair** n'a $w$ pour itinéraire ; aucune orbite
entière n'adopte, à partir d'un instant quelconque, un motif de runs en progression
arithmétique de raison $c\ge1$.

Le mot triangulaire est le cas $(c,d)=(1,0)$, $u$ vide. Tous ces mots ont une
densité de pas pairs nulle ($E(t)\asymp\sqrt t$).

**Corollaire quantitatif C1′** (même hypothèses, $u$ vide). Pour tout $\varepsilon>0$
il existe $\Lambda=\Lambda(c,d,\varepsilon)>0$ effectivement calculable (non calculée ici)
telle que, pour tout entier $N$, la longueur $k$ du plus long préfixe commun aux
itinéraires de $N$ et $w$ vérifie
$$k<(1+\theta+\varepsilon)\log_2(2|N|+1)+\log_2(1/\Lambda),\qquad
\theta=\frac{1+\sqrt5}{2-\gamma(3+\sqrt5)}\approx47{,}93,\quad\gamma=1-\frac{\log2}{\log3}.$$

## 2. Recherche active de contre-exemples (avant la preuve)

1. **Raison nulle ($c=0$).** Les runs constants donnent les mots périodiques
   $(1^d0)^\infty$, réalisés par des rationnels (Lagarias 1985) : le script
   retrouve exactement $\xi=0,1,-5,-19/11,-65/49,\dots$ pour $d=0,\dots,7$,
   par la même formule $\xi=-(1+f_q(\alpha))/2$ avec $q=1$, $f_1(\alpha)=1/(1-\alpha)$.
   **L'hypothèse $c\ge1$ est donc nécessaire** ; elle correspond à $|r|=3^c>1$ dans VW.
2. **Raison négative** : impossible (runs négatifs à partir d'un rang).
3. **Préfixe et alignement des blocs** : couverts par $u$ (étape 4 de la preuve) ;
   contrôlé numériquement (préfixes aléatoires de longueur ≤ 6).
4. **Cas limites de $d$** : $d=-c$ donne $r_1=0$ (mot commençant par 0) ;
   $\alpha=2^{d+1}/3^d$ peut avoir un 3 au numérateur. Contrôlé pour $1\le c\le4$, $-c\le d\le4$.
5. **Hypothèses de VW** : aucune exception — $\gamma$ ne dépend pas de $c$ (§3, étape 3).
6. **Calcul exact borné** (observation, pas preuve) : orbites des rationnels $a/b$,
   $b$ impair $\le63$, $|a|\le300$ (19 232 orbites, 4 000 pas, via la dynamique
   entière $a\mapsto a/2$ ou $(3a+b)/2$) : **aucune** queue de 12 runs en
   progression de raison $\ge1$ ; aucune orbite non décidée.

Aucun contre-exemple ; le lemme résiste.

## 3. Preuve

**Étape 1 — formule de réalisation (élémentaire, démontrée ici).** Poser
$y_t=T^t(\xi)+1$. Un pas impair donne $y_{t+1}=\tfrac32y_t$, un pas pair
$y_{t+1}=(y_t+1)/2$. Par récurrence, avec $o(t)$ le nombre de 1 parmi $w_0\dots w_{t-1}$,
$$2^ty_t=3^{o(t)}y_0+\sum_{e<t,\ w_e=0}2^e\,3^{o(t)-o(e)} .$$
(Pas impair : multiplier par 3 ; pas pair en $t$ : ajouter $2^t$.) Diviser par
$3^{o(t)}$ et faire $t\to\infty$ dans $\mathbb Z_2$ ($2^ty_t/3^{o(t)}\to0$) :
$$\xi_w+1=-\sum_{w_e=0}\frac{2^e}{3^{o(e)}}=-\frac12\sum_{j\ge1}2^j\Bigl(\frac23\Bigr)^{o_j},$$
où $e_j$ est la position du $j$-ième 0 et $o_j=o(e_j)=e_j-(j-1)$. La série
converge ($v_2$ du terme $=j+o_j\to\infty$). C'est l'analogue, en variable $x+1$,
de la formule de Bernstein (1994) indexée par les positions des 1.
Contrôle : 3 000 mots aléatoires de longueur 64 (script, §1).

**Étape 2 — mots à runs linéaires ($u$ vide).** Ici $o_j=\sum_{i\le j}r_i=c\,\tfrac{j(j+1)}2+dj\ge0$, donc
$$2^j(2/3)^{o_j}=\alpha^j q^{-j(j+1)/2},\qquad q=(3/2)^c,\quad \alpha=2^{d+1}/3^d ,$$
et $\sum_{j\ge1}=f_q(\alpha)-1$ avec $f_q(x)=\sum_{n\ge0}q^{-n(n+1)/2}x^n$, la
fonction de VW (leur (1)). D'où
$$\boxed{\ \xi_w=-\tfrac12\bigl(1+f_q(\alpha)\bigr)\ \text{ dans }\mathbb Q_2.}$$
Pour $(c,d)=(1,0)$ on retrouve $N+1=-S$, $2S+1=f_{3/2}(2)$ de la PR #24.
Contrôle : identité vérifiée mod $2^{160}$ pour 30 couples $(c,d)$, à la fois en
entiers et avec la normalisation exacte de VW en `Fraction`.

**Étape 3 — application du Satz de VW 1989** avec $l=1$, $\sigma=0$, $p=2$,
$q=r/s$, $r=3^c$, $s=2^c$, $\alpha_1=\alpha$ :
- $(r,s)=1$, $|r|=3^c>1$, $s\ge1$, $h=\max(|r|,s)=3^c$ ;
- $\alpha\in\mathbb Q^\times$ ; la condition sur $\alpha_i/\alpha_j$ est vide ;
- $\gamma=\delta(2)+\log|s|_2/\log h=1-\dfrac{c\log2}{c\log3}=1-\dfrac{\log2}{\log3}$, **indépendant de $c$** ;
- $\Gamma(1,0)=(3-\sqrt5)/2$ ; $2^8>3^5\Rightarrow\gamma<3/8$, et $3/8<(3-\sqrt5)/2\iff81>80$.

Le Satz donne $|h_0+h_1f_q(\alpha)|_2>\Lambda H^{-1-\theta-\varepsilon}>0$ pour tout
$(h_0,h_1)\in\mathbb Z^2\setminus\{0\}$. Donc $1$ et $f_q(\alpha)$ sont
$\mathbb Q$-linéairement indépendants dans $\mathbb Q_2$ : $f_q(\alpha)\notin\mathbb Q$,
et par l'étape 2, $\xi_w\notin\mathbb Q$.

**Étape 4 — préfixe $u$.** $T$ envoie $\mathbb Q\cap\mathbb Z_2$ dans lui-même.
Si $\xi_{uv}\in\mathbb Q$, alors $T^{|u|}(\xi_{uv})=\xi_v\in\mathbb Q$, contradiction. ∎

**Corollaire C1′.** Avec $h_0=2N+1$, $h_1=1$ : $L=2N+1+f_q(\alpha)=2(N-\xi_w)$.
Un préfixe commun de longueur $k$ équivaut à $N\equiv\xi_w\pmod{2^k}$, d'où
$|L|_2\le2^{-k-1}$ ; comparer à $\Lambda(2|N|+1)^{-1-\theta-\varepsilon}$. ∎

### Étapes non justifiées dans ce dépôt

- **La preuve du Satz de VW 1989** (méthode de Hermite–Perron–Skolem) n'est ni
  reconstruite ni formalisée ; elle est acceptée comme résultat publié et évalué.
  C'est la seule dépendance externe.
- La lecture de l'énoncé repose sur un scan rendu en image (typographie `l`/`1`
  à machine à écrire) : $\Gamma(l,\sigma)=(2l(\sigma+1)+1-\sqrt{1+4l^2(\sigma+1)^2})/(2l(\sigma+1))$
  redonne bien $(3-\sqrt5)/2$ pour $l=1,\sigma=0$, comme la transcription secondaire
  utilisée par muaijaz. Une relecture humaine du scan reste souhaitable.
- $\Lambda$ n'est pas calculée : C1′ est effectif en principe, pas numériquement.

## 4. Comparaison avec la littérature et le dépôt

- **Conjecture de périodicité de Lagarias (1985)** : tout rationnel de $\mathbb Z_{(2)}$
  aurait un itinéraire ultimement périodique. C1 en est un **cas particulier démontré**
  pour une famille à deux paramètres (plus préfixes arbitraires).
- **PR #24** (non fusionnée) : seul le cas $(1,0)$, conditionnel. Statut levé ici.
- **muaijaz/not-an-ai-collatz-proof** (commit `535044be…`, §19.6 de `PROJECT_JOURNEY.md`) :
  application du même théorème à $q=9/4$, $\alpha=9/2$, c'est-à-dire **$c=2$, $d=-2$**
  (leur « échelle $J_m/K_m$ »), propagée par l'équation fonctionnelle. La famille
  générale $(c,d,u)$ n'y figure pas ; antériorité dans la littérature publiée **non vérifiée**.
- **Bernstein (1994)** : formule de réalisation équivalente (non revérifiée sur le texte ici).
- **Branche `even-density-structural-audit` (§5)** : exclut des mots à runs
  presque maximaux par un argument archimédien ; C1 traite des runs **courts**
  ($r_j\ll\beta o_j$) qui échappent à cet argument, au prix d'un théorème de transcendance.

## 5. Ce que ce cycle ne montre pas

- Rien sur les mots à densité nulle dont les runs ne sont pas ultimement en
  progression arithmétique (par ex. $r_j=\lfloor j/2\rfloor$, ou $r_j=cj+d+p_j$ avec
  $p$ périodique : il faudrait $l\ge2$ dans VW, et $\Gamma(2,0)=(5-\sqrt{17})/4\approx0{,}219<\gamma$).
- Rien sur (C) (densité positive des pas pairs sur toute orbite non bornée), ni sur Syracuse.

## 6. Mises à jour de la mémoire

- `proved.md` : B1 (formule de réalisation), B2 (lemme C1), B3 (C1′).
- `counterexamples.md` : X11 (nécessité de $c\ge1$), X12 (critère de Liouville naïf réfuté par 1, remarque de préparation).
- `hypotheses.md` : H3 (périodicité de Lagarias : cas particulier démontré), H5 (extension au-delà de VW).
- `prior_art.md` : transcription du Satz de VW 1989 ; statut de PR #24 mis à jour.
- `agenda.md` : entrée traitée retirée ; prochaine question = statut exact de la cible (H) de la PR #26.

## 7. Reproduire

```sh
python3 research/checks/cycle001_linear_runs.py   # ~20 s, Python 3 standard
```
Sortie attendue : six lignes `PASS` (formule générale 3000 ; cycles rationnels pour c=0 ;
30 couples (c,d) ; représentants triangulaires 1, 57, 121, 121, … ; seuils VW ; 19 232 orbites, 0 suspect).
