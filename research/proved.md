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
($125>121$ et $256>243$). Si l'itinéraire d'un entier $N>0$ commence par le
préfixe exact $\prod_{j=1}^{k}(0\,1^{F_{j+2}})\,0$, alors $N\ge2^{k-1}$. Les
seules longueurs de ces runs ne déterminent pas le préfixe (X20). Tout mot à
un zéro par bloc avec $r_{k+1}/r_k\to\lambda$ pour un $\lambda>\log_2 3$
vérifie $o_k/r_k\to1/(\lambda-1)$ et $Q_k\to+\infty$ (cycle 004 §8), donc son
réalisateur est irrationnel par B7. Le cas $\varphi$ en fait partie. Un préfixe
fini quelconque, y compris un premier bloc de $1$, ne restaure pas la
rationalité : chaque branche de $T$ est une bijection de $\mathbb Q$. Densité
des $1$ égale à $1$ : pas un corollaire de Monks–Yazinski, et ce théorème n'est
pas une prémisse. Dépend de B7 pour l'irrationalité et pour la borne entière ;
l'inégalité $Q_k>k$ n'en dépend pas. Toute orbite d'entier positif a une
infinité de pas pairs : un pas impair positif fait chuter $v_2(n+1)$ de $1$.
Le point $n=-1$ est fixe et reste hors de cette phrase. Pour
$1<\lambda<\log_2 3$, $Q_k\to-\infty$ et B7 ne s'applique pas. À
$\lambda=\log_2 3$, la seule limite $r_k/o_k\to\beta$ ne fixe pas le signe.
Les deux familles $r_1=64$ et $r_k=\lfloor\beta o_k\rfloor\pm\lfloor\sqrt{o_k}\rfloor$
pour $k\ge2$ ont le même rapport limite $\log_2 3$ (cycle 004 §8). Le signe
plus donne $Q_k\to+\infty$, donc un réalisateur irrationnel. Le signe moins
donne $Q_k\to-\infty$ : B7 ne s'applique pas, et l'irrationalité reste ouverte.
Les placements de zéros qui ne se ramènent pas au mot de taux
$\lambda>\log_2 3$ en supprimant un préfixe fini restent ouverts, ainsi que
les runs quasi linéaires.

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

Revue indépendante `6081410834` (PR #27, SHA `8bc44f73615fd5fcf0b59797f59ec74cf8cece10`) :
B9 (§§2–4) et la borne du préfixe exact sont confirmés, puis revérifiés par le
script du cycle 004. L'implication « longueurs des runs ⇒ préfixe exact » est
réfutée (X20) et retirée de l'énoncé. L'indice $S_{k-1}$ de l'ancien agenda
désignait $o_k$, et $o_k+r_k=S_k$. Le corollaire du §8, pour un zéro par bloc et
$r_{k+1}/r_k\to\varphi$, est prouvé dans le cycle. Ce n'est pas une seconde
preuve de B9.

Revue indépendante `6081458173` (PR #27, SHA `4696589434762ecf662475990fe6bbdfc0818726`) :
X20, la borne du préfixe exact et le corollaire en $\varphi$ sont confirmés.
La phrase sur les runs finis est restreinte aux impairs positifs ($T(-1)=-1$).
Les deux prémisses de B7 sont séparées. L'extension à tout $\lambda>\log_2 3$,
la chute $Q_k\to-\infty$ pour $1<\lambda<\log_2 3$, et l'invariance par préfixe
fini sont prouvées dans le §8 corrigé. Ce n'est pas une seconde preuve de B9,
ni le cycle suivant.

Revue indépendante `6081531962` (PR #27, SHA `33c22a38802bdaf810304c02ad9df895883ec445`) :
les seuils stricts, le préfixe fini et X20 sont confirmés. L'annonce d'un
signe non uniforme au seuil $\lambda=\log_2 3$ dépassait la limite
$r_k/o_k\to\beta$. Les deux familles du cycle 004 §8 sont prouvées dans ce
cycle : $Q_k\to+\infty$ pour le signe plus, $Q_k\to-\infty$ pour le signe
moins. Ce n'est pas une seconde preuve de B9, ni le cycle suivant.

Revue indépendante `6081622758` (PR #27, SHA `3bdc5daa042aef655c84e4ea36d16c55774f5a6c`) :
la proposition du seuil est confirmée. Le test du signe plus vérifie désormais
$Q_k>k$, pas seulement $Q_k>0$. Pour $k\ge2$, le §8 donne déjà $Q_k>k+3$.
L'inégalité sur $w_{16+t}$ est large. Le signe moins n'est pas exclu comme
itinéraire d'un entier : seule son irrationalité reste ouverte. Ce n'est pas
une seconde preuve de B9, ni le cycle suivant.

Revue indépendante `6081702521` (PR #27, SHA `7120654a69a0bd4849816b2e83a60dfbf79d6d77`) :
les comparaisons $Q_k>k$ et $Q_k<0$, la borne $Q_k>k+3$ pour $k\ge2$ et
l'invariance par préfixe fini sont confirmées. L'irrationalité du signe
moins reste ouverte, comme le §8 le dit déjà. Aucun changement au texte de
B9. Ce n'est pas une seconde preuve, ni le cycle suivant.

**B10 — Horizon Mersenne d'un poids borné** (PROUVÉ, cycle 005 §5).
Si $0<\ell\le W\le h$, $0<\rho<1$ et $K=\rho h/\ell\le3/2$, tout temps de
contraction $t$ de $2^L-1$ ($L\ge2$) vérifie $3\cdot2^t>2\cdot3^L$. Donc
$B(2^L-1)\ge\log_2 3\cdot L-\log_2(3/2)$. La forme $5\cdot2^t>2\cdot3^L$ en
découle. Mécanisme : l'ascension A2 reste strictement au-dessus du facteur
$3/2$ jusqu'au temps $L$, puis $T(x)\ge x/2$. Si $K>3/2$, la borne locale
sans seuil est fausse (X21). Cela ne réfute pas l'implication globale de H6.
Le coefficient de tête est inférieur aux bornes d'Applegate–Lagarias 2003
sur le temps d'arrêt total ; leur programme d'arbres n'est pas refait.
Aucun certificat global n'est construit.

Revue indépendante `6081843230` (PR #27, SHA `ebba3309f617204d844c241d84c5442af3e35c85`) :
B10 et X21 sont confirmés. La comparaison $2^L+K-1\ge2^L$ est fausse pour
$0<K<1$ ; la différence $2^L+K-1$ reste positive, et la borne s'écrit
$3\cdot2^t>2\cdot3^L$. L'implication globale de H6 reste ouverte. La
justification de la formule (4) compte $\log_2(3^k-1)$ pas après le sommet.
Ce n'est pas une seconde preuve de l'ascension, ni le cycle suivant.

Revue indépendante `6081884788` (PR #27, SHA `0b935a943b7972fa3998ac98b2c53fcc6772ea5b`) :
la forme $3\cdot2^t>2\cdot3^L$, la positivité de $2^L+K-1$, X21 et le
décompte après le sommet sont confirmés. H6 globale reste ouverte. Aucun
changement au texte de B10. Ce n'est pas une seconde preuve, ni le cycle
suivant : le cycle 006 vient après.

**B11 — Réalisation des runs appariés** (PROUVÉ, cycle 006 §3). Pour le mot
à un zéro par bloc et $r_j=j+[j\text{ impair}]$, avec $q=81/16$ et
$f_q(x)=\sum_{n\ge0}q^{-n(n+1)/2}x^n$,
$$4\xi_w+1+2f_q(4)+f_q(9)=0\quad\text{dans }\mathbb Q_2.$$
Les termes pairs et impairs sont exactement $u_m(4)$ et $\tfrac12 u_m(9)$.
Donc $\xi_w\in\mathbb Q$ si et seulement si $2f_q(4)+f_q(9)\in\mathbb Q$.
Ce n'est pas une exclusion : $\gamma>\Gamma(2,0)$ pour ce $q$ (cycle 006 §4),
les Satz 1 et 2 de Bundschuh 1974 ne s'appliquent pas (§5), et les énoncés
lus de Bézivin 1988 et d'Amou–Väänänen 2005 ne portent pas sur cette valeur
2-adique (§6). Sur ce mot, $\sup_m Q_m=Q_2=\log_2(2048/217)$ (cycle 006 §2) :
tout $\sigma=a/b$ rationnel vérifie $\max(|a|,b)\ge10$, mais $Q_m\to-\infty$,
donc B7 ne donne pas l'irrationalité. Elle reste ouverte.

Revue indépendante `6081961103` (PR #27, SHA `fcd6a008ed0aad5ee2033ee3b9123ba6cacd0237`) :
B11 est confirmée. La comparaison $Q_m<0$ dès $m\ge4$ est réfutée (X22) et
corrigée. Le test du script omettait $o_m$ et prenait $r_m$ au lieu de
$r_{m+1}$. Le supremum $Q_2$ et la chute $Q_m\to-\infty$ sont prouvés dans
le cycle. Ce n'est pas une seconde preuve de l'identité, ni le cycle suivant.

Revue indépendante `6081994521` (PR #27, SHA `a2886972de6371d3302dd9a17bc3bc59c98e479f`) :
le correctif X22 est confirmé, y compris $\sup_m Q_m=Q_2$ et $Q_m\to-\infty$.
L'irrationalité reste ouverte, comme le texte le dit déjà. Aucun changement
à B11. Ce n'est pas une seconde preuve, ni le cycle suivant : le cycle 007
vient après.

**B12 — Premier retour modulo $18$** (PROUVÉ, cycle 007 §3). Pour
$f(n)=3n+1$ si $n$ est impair et $n/2$ si $n$ est pair, soient
$N_1=\{n\equiv1\text{ ou }5\pmod6\}$, $N_2=\{n\equiv4\text{ ou }16\pmod{18}\}$
et $\Sigma=N_1\cup N_2$. Le premier retour $P$ de $f$ sur $\Sigma$ est
défini partout. Sa restriction à $N_1$ est la bijection $n\mapsto3n+1$
sur $N_2$. Sa restriction à $N_2$ est injective et d'image $\Sigma$. Tout
entier atteint $N_1$. La conjecture « $f$ atteint $1$ » équivaut à
« $1$ est dans l'orbite de $P$ pour tout point de $\Sigma$ ». Pour un
entier positif, $f$ atteint $1$ si et seulement si l'application
raccourcie $T$ du dépôt atteint $1$. Antériorité : Mori,
arXiv:2411.08084v2, proposition 4.3.3 ; la preuve d'ici est autonome.
La paire de résidus imprimée $16n\equiv16,4\pmod{18}$ pour
$n\equiv7,16$ est fausse : les deux produits valent $4$. Elle ne réfute
pas l'énoncé. L'inégalité $P(m)\ge n$ de la même proposition est
justifiée par la chaîne de divisions décroissante (cycle 007 §4). Ce
n'est pas une preuve de la conjecture. L'objection de fermeture sur la
définition 3.4.4 est réfutée (X23). Les théorèmes 4.2.7 et 4.3.10 du
même article ne sont pas des prémisses (cycle 007 §5).

Revue indépendante `6082099628` (PR #27, SHA `eeaeb41ff7f030cd5b0c59715e2614e56f1243ed`) :
X23 et $P(m)\ge n$ sont confirmés. La phrase sur le premier point de
$\Sigma$ est conservée. La prémisse non pondérée n'est pas rouverte :
c'est le cas $K=\rho$ du cycle 005. Ce n'est pas une seconde preuve de
B12. Le cycle 008 vient après.

**B13 — Horizon global d'un certificat pondéré** (PROUVÉ, cycle 008 §5).
Si $0<\ell\le W\le h$, $0<\rho<1$, $K=\rho h/\ell$, et si tout entier
$n\ge N_0$ admet un temps $t\le B(n)$ avec
$T^t(n)\,W(T^t(n))\le\rho\,n\,W(n)$, alors
$B(n)>\log_2 3\cdot\log_2 n-C$ pour une infinité de $n$. La constante
$C=\log_2 K+J(\log_2 3)^2$ est celle du cycle 008 §4–§5 :
$J=(m_*-1)\,t_*$, et $t_*$ est le maximum de
$\{0\}\cup\{t\ge1:(3/2)^t<2K\}$. L'écriture $\log_2(2K)$ majore $C$
d'une unité. Aucun horizon $o(\log n)$ ne convient. Pour $K\le3/2$, le
témoin est le Mersenne et $t>\delta L-\log_2 K$, déjà dans la preuve de
B10 ; la forme uniforme en $\log_2(3/2)$ est plus faible lorsque
$K\le3/4$ et plus forte lorsque $K>3/4$, car alors $J\ge1$. La forme
sans poids $T^t(n)\le\rho n$ donne $\rho\cdot2^t>3^L$ (cycle 008 §1) ;
ce n'est pas un énoncé nouveau. X21 reste local. Antériorité du
mécanisme : la montée A2 et l'horizon fixe de `no_finite_certificate`
(A5). Pas une preuve de la conjecture, ni une construction de certificat.

Revue indépendante `6082191024` (PR #27, SHA
`ff58fed0501768dabaa980ee5d0668b347d8b898`) : B13 est confirmée. La
définition de $t_*$ est corrigée pour $K\le1/2$, la constante perd le
facteur $2$, et la comparaison avec la forme uniforme de B10 est
restreinte comme ci-dessus. Ce n'est pas une seconde preuve, ni le
cycle suivant.

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
