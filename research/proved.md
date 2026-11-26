# Résultats prouvés

Statuts : **PROUVÉ** (preuve complète ici ou sur `main`) · **PUBLIÉ** (référence vérifiable) ·
**PROUVÉ via PUBLIÉ** (preuve ici + théorème publié accepté) · **NON VALIDÉ** (preuve écrite
dans une PR non fusionnée : ni revue ni intégrée). Une observation numérique n'est jamais une preuve.

Conventions : $T(n)=n/2$ (pair), $(3n+1)/2$ (impair) ; $U(n)=(3n+1)/2^{v_2(3n+1)}$ sur les impairs ;
$\delta=\log_23$, $\beta=\log_2(3/2)$ ; $E(t)$ = nombre de pas pairs avant $t$ ; $p_N(L)$ = nombre de
facteurs de longueur $L$ de l'itinéraire infini de $N$.

## A. Sur `main` (fusionné)

| # | Énoncé | Statut | Source |
|---|---|---|---|
| A1 | Codage de Terras/Everett : un mot de $k$ parités ↔ une classe mod $2^k$ ; $M\,T^j(n)=An+D$, réalisation ⇔ $2^j\mid 3^q n+D(w)$ | PUBLIÉ (classique) ; correction du vérificateur rédigée | `tools/finite_descent/README.md` |
| A2 | Montée de Mersenne : $T^t(2^h-1)=3^t2^{h-t}-1$ pour $0\le t\le h$ (et $U^t(2^h-1)=3^t2^{h-t}-1$, $t\le h-1$) | PROUVÉ (élémentaire, classique) | `research/REORIENTATION.md` |
| A3 | Pour tout $m\ge1$, infinité d'impairs avec $\tau_U(n)=m$ exactement (classe mod $2^{2m+1}$) | PROUVÉ (classique) | `research/EXACT_STOPPING_TIME_BASELINE.md` |
| A4 | Frontière $\theta_c=2\log_32-1$ : pour tout préfixe de longueur $\le(\theta_c-\varepsilon)k$, la proportion de non-descente au temps $k$ est $\le e^{-\varepsilon^2k/8}$ (uniformément) | PROUVÉ (classique : codage + Hoeffding) | `research/ETUDE_37_RAPPORT.md` §2 |
| A5 | Théorèmes Lean de `msharpe248/collatz@ec8174b5` compilés dans l'audit (16 modules, 39 énoncés, sans `sorryAx`) : `no_uniform_descent_bound`, `no_finite_certificate` (poids rationnels bornés, horizon fixe), `unbounded_factor_floor`, `mechanical_classification`, `shadow_modEq`, `NoncontractingTail`… | PROUVÉ en Lean (externe), portée exacte dans le rapport | `audit_collatz/RAPPORT.md`, `VALIDATION.md` |
| A6 | Vérificateur de certificats finis : `VALID` ⇒ descente stricte de chaque $n\in[N_0,N_1]$ | Argument écrit + audit adverse (7 913 cas, 0 faux VALID) ; pas une preuve formelle | `tools/finite_descent/`, `research/VERIFIER_AUDIT_ISSUE19.md` |

## B. Prouvé dans cette mémoire (cycles)

**B1 — Formule de réalisation 2-adique** (PROUVÉ, cycle 001 §3 étape 1). Si $\xi\in\mathbb Z_2$ a
l'itinéraire $w$, avec $j$-ième pas pair en $e_j$ et $o_j=e_j-(j-1)$ pas impairs avant lui :
$\xi+1=-\tfrac12\sum_{j\ge1}2^j(2/3)^{o_j}$ (somme finie si $w$ n'a qu'un nombre fini de 0).
Équivalente à la formule de Bernstein (1994). Contrôlé sur 3 000 mots aléatoires.

**B2 — Lemme C1 : runs en progression arithmétique** (PROUVÉ via PUBLIÉ, cycle 001).
Pour $c\ge1$, $d\ge-c$, $u$ fini : $w=u\,(1^{cj+d}0)_{j\ge1}$ n'est l'itinéraire d'aucun rationnel
de $\mathbb Z_{(2)}$, donc d'aucun entier. Clé : $\xi_w=-\tfrac12(1+f_{(3/2)^c}(2^{d+1}/3^d))$ et
Väänänen–Wallisser 1989, Satz ($l=1,\sigma=0,p=2$), énoncé primaire relu.
Inclut le **mot triangulaire** (PR #24 : statut conditionnel levé). Dépendance non vérifiée ici :
la preuve publiée de VW 1989.

**B3 — Corollaire C1′** (PROUVÉ via PUBLIÉ, constante non calculée). Un entier $N$ ne suit un
mot de B2 ($u$ vide) que pendant au plus $(1+\theta+\varepsilon)\log_2(2|N|+1)+C_{c,d,\varepsilon}$
pas, $\theta\approx47{,}93$.

**B4 — (H) force $B>1$** (PROUVÉ, cycle 002 §2). Pour tout réel $A$ et tout $B\le1$, la paire
$(A,B)$ échoue. Les Mersenne $M=2^h-1$ donnent $B\ge1$ ($k=1$). Pour $B\le1$, l'ordre de 3
modulo $2^m$ ($m\ge3$) fournit $r$ avec $v_2(5\cdot3^r+1)\ge m$ ; la fenêtre $M=5\cdot2^r-1$
a deux runs de somme $\ge r+m-1$, tandis que $x(M)<r+3$. Choisir $m>2A+4$. Témoin :
$r=757$, $v_2(5\cdot3^{757}+1)=16$, somme 772, et $5^3<2^7$ tue aussi $A\le6$ à pente 1.
Preuve autonome (n'invoque pas C8).

**B5 — Fenêtres de longueur $\le K$** (PROUVÉ, cycle 002 §3). $x(M_{j+1})\le\delta\,x(M_j)$ et
$r\le x$, donc $\sum_{j<k}r(M_j)\le x(M)(\delta^k-1)/\beta$. Constante $A=0$,
$B_K=(\delta^K-1)/\beta$ (donc $B_1=1$, $B_2=\log_26$). Exponentielle en $K$, pas universelle.

**B6 — (H) et les orbites non bornées** (PROUVÉ, cycle 002 §4). Identité
$\log_2(n_t+1)=\log_2(N+1)+\beta t-\delta E(t)+R(t)$. Sur une orbite non bornée les
états pairs sont distincts, donc $R=O(\log E)$, d'où $\limsup E(t)/t\le\beta/\delta$.
Sous (H), $\liminf E(t)/t\ge1/(A+1)$, constante
indépendante de $N$ : (H) implique (C) uniforme. Si $A<1/\beta$, les deux bornes se
contredisent : aucune orbite positive non bornée. Toute paire compatible avec une telle
orbite vérifie $A\ge1/\beta$ et $B>1$.

**B7 — Critère de Liouville** (PROUVÉ, cycle 003 §2). Mot $w$ avec une infinité de $0$,
$o_j$ et $\sigma=-2(\xi_w+1)$ comme en B1, $r_m=o_{m+1}-o_m$,
$G_m=\sum_{j=1}^m 2^{j+o_j}/3^{o_j}$ et
$Q_m=r_m+m+1-\beta o_m-\log_2(1+G_m)$. Si $\sup_m Q_m=+\infty$, alors $\xi_w\notin\mathbb Q$.
Mécanisme : $A_m=a\,3^{o_m}-b P_m$ vérifie $v_2(A_m)=m+1+o_{m+1}$ et
$|A_m|\le|a|3^{o_m}+b P_m$, donc $Q_m\le\log_2\max(|a|,b)$.

**B8 — Runs de longueur $2^k$** (PROUVÉ, cycle 003 §3). Le mot $\prod_{k\ge1}(0\,1^{2^k})$
satisfait $Q_k>k$. Donc son réalisateur 2-adique est irrationnel. Preuve élémentaire
(majoration $G<3778/729$ et comparaison $128/9>4507/729$). Densité des $1$ égale à $1$ :
ce n'est pas un corollaire de Monks–Yazinski 2004, thm 2.7(b). Ne retrouve pas les runs
linéaires (X18).

**B9 — Runs de Fibonacci** (PROUVÉ, cycle 004 §4). Le mot $\prod_{k\ge1}(0\,1^{F_{k+2}})$,
$F_1=F_2=1$, satisfait $Q_k>k$ pour tout $k\ge1$. Donc $\xi_w\notin\mathbb Q$.
Preuve élémentaire : $2^{F_{n+1}}\ge3^{F_n}+2^{n-2}$ pour $n\ge4$ (bases $32\ge31$,
$256\ge251$, puis produit), et cette marge fait passer la comparaison entière de
$D_k=2^{o_k+r_k+1}$ à $D_{k+1}$. Cas directs $k=1$ ($8>3$) et $k=2$ ($64>43$).
Le rapport des runs tend vers $1/\varphi>\beta$, car $\varphi>8/5>\log_23$
($125>121$ et $256>243$). Un entier $N>0$ dont les $k$ premiers runs impairs sont
$F_3,\ldots,F_{k+2}$ vérifie $N\ge2^{k-1}$. Densité des $1$ égale à $1$ : pas un
corollaire de Monks–Yazinski. Dépend de B7 pour l'irrationalité et pour la borne
entière ; l'inégalité $Q_k>k$ n'en dépend pas. Ne traite pas les runs quasi linéaires.

Revue indépendante `6080964566` (PR #27, SHA `0c90981ae61e15d4aa8505d1158ddb79039a22fd`) :
les preuves écrites de B7, B8 et X18 ont été confirmées, puis revérifiées dans ce
dépôt (télescopage de $y_t=T^t(\xi)+1$, comparaisons entières, relance du script).
Ce n'est pas une seconde preuve. La phrase expérimentale qui attribuait au balayage
borné la couverture des cycles de $3x+b$ a été réfutée (X19) et corrigée ; elle ne
faisait pas partie de B7.

Revue indépendante `6081009622` (PR #27, SHA `aeb693b5286fcb308484c91cdbeefcbe8ac576c2`) :
le certificat X19 et la forme entière de $Q_m$ pour $L\in\mathbb Z$ sont confirmés,
puis revérifiés (huit transitions bornées, $339\,789$ états et les états de sortie,
$118\,882$ valuations exactes, membre de droite $\ge6$). Aucun changement au texte
de B7. Ce n'est pas une seconde preuve.

## C. Résultats de PR non fusionnées — NON VALIDÉS

Preuves écrites, relues par leurs auteurs successifs, **non revues ni fusionnées**.
Les relectures de l'initialisation n'ont pas trouvé d'erreur, sans vérification ligne à ligne.

| # | Énoncé | Source | Remarque |
|---|---|---|---|
| C1 | Orbite non bornée ⇒ $p_N(L)\ge1+\lfloor(L-K)/\beta\rfloor$ ($N+1\le2^K$) | PR [#21](https://github.com/hsirven1/syracuse_search/pull/21) | Pente $1/\beta$ **déjà publiée** : Dubickas 2009, thm 5 |
| C2 | Pour tout $N$ : $E(t)\ge\log_2t/\log_2\delta-O_N(1)$ ; identité $H(t)=H(0)+\beta t-\delta E(t)+R(t)$ ; gain conditionnel $\liminf(p_N(L)-L/\beta)/\log_2L\ge\delta/(\beta\log_2\delta)$ | PR [#22](https://github.com/hsirven1/syracuse_search/pull/22) | Divisibilité $2^r\mid n+1$ pour un run de $r$ impairs |
| C3 | Orbite non bornée ⇒ $\sum_t1/n_t\le61344/65$, $R=O(1)$, $p_N(L)\ge L/\beta+c_*\log_2L-C_N$ ; $\limsup H/t=\beta-\delta\eta_N$ ; exclusion d'un mot à runs presque maximaux ; modèle réel montrant l'insuffisance des seules bornes archimédiennes | branche `research/even-density-structural-audit` (sans PR ; base de #23) | Sommabilité attribuée à Garcia–Tal 1999 via le dépôt externe |
| C4 | Mot triangulaire : $p_w(L)=\lfloor(L+1)^2/4\rfloor$ ($L\ge3$) ; congruence (14) ; réalisation 2-adique (B) | PR [#23](https://github.com/hsirven1/syracuse_search/pull/23) | (B) re-dérivée en B1–B2 |
| C5 | $2S+1=f_{3/2}(2)$ ; exclusion du mot triangulaire **conditionnelle** à VW 1989 | PR [#24](https://github.com/hsirven1/syracuse_search/pull/24) | Condition levée par B2 (énoncé primaire lu) |
| C6 | Récurrence des runs $r_{i+1}+1=v_2(3^{r_i}a_i+1)$, $M_i+1=2^{r_i}a_i$ ; (V) ⇒ gain log-log | branche `research/padic-successive-runs` (base de #25) | — |
| C7 | (V) : $v_2(3^ra+1)\le C(1+\log_2a)\log_2(2+r)$, $C$ absolue ; d'où, pour une orbite non bornée, $p_N(L)\ge L/\beta+c_*\log_2L+d\log_2\log_2L-O_N(1)$ | PR [#25](https://github.com/hsirven1/syracuse_search/pull/25) | Spécialisation de Yu 1999 (PDF primaire relu par l'auteur de la PR) |
| C8 | Partie impaire initiale 5 : $r_0\bmod2^{D-1}\mapsto(5\cdot3^{r_0}-1)/2\bmod2^D$ bijective sur les classes $\equiv3\bmod4$ ; tout vecteur fini de runs $(r_1\ge2,r_2,\dots)$ réalisable | PR [#26](https://github.com/hsirven1/syracuse_search/pull/26) | Élémentaire (ordre de 3 mod $2^m$) |
| C9 | KL : traduction LP ↔ opérateur F confirmée ; stricte croissance des seuils | PR #6–#8 | Antériorité Applegate–Lagarias 1995 ; abandonné comme nouveauté |
