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
