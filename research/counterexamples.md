# Contre-exemples et réfutations exactes

Chaque entrée : énoncé réfuté, témoin exact, reproduction, statut de la source
(`main` = fusionné ; PR non fusionnée = **non validé**, mais témoin vérifiable).

| # | Énoncé réfuté | Témoin exact | Reproduction / source |
|---|---|---|---|
| X1 | **C37** : $\exists c>0$, pour tout préfixe de longueur $\lceil k/3\rceil$, proportion de non-descente $\le e^{-ck}$ | Préfixe tout impair : la proportion tend vers 1 (0,958 à $k=400$) ; seuil $\theta_c\approx0{,}2619$ | `main` : `research/etude37_conditional_cover.py` |
| X2 | Bornes naïves $\tau(2^h-1)\le2h$ et $\le4h$ (première descente, Syracuse accéléré) | $\le2h$ : $h=5$ (35), $6,11,12,13,15,17,\dots$ ; $\le4h$ : $h=5$ (35), $h=6$ (34) | `main` : `python3 research/mersenne_check.py` |
| X3 | Tout horizon de descente uniforme / certificat fini à poids rationnels bornés | Montées de Mersenne $T^t(2^L-1)$ | `main` : audit Lean `NoGo.lean:134,205` |
| X4 | « La classe mod $2^k$ détermine la classe image mod $2^k$ » | $3\equiv35\pmod{32}$, $T(3)=5$, $T(35)=53\equiv21$ | `main` : `audit_collatz/RAPPORT.md` (`ResidueMapAudit.lean`) |
| X5 | Corrections libres dans une enveloppe = corrections de mots | $3^6\cdot3+194421=2^{16}\cdot3$, mais 194421 n'est la correction d'aucun mot de longueur 16 à 6 impairs | `main` : `CongruenceRelaxation.lean` |
| X6 | Le critère de hauteur (36.3) apporte une contrainte | Toujours ≤ plus petit représentant de la classe exacte du préfixe | `main` : `audit_collatz/EXPERIENCE36_COMPARAISON.md` |
| X7 | Croissance stricte, bloc par bloc, des représentants canoniques du mot triangulaire | $r_3=r_4=121$ (mod $2^{\tau_m+1}$) | PR #23 (non validée) ; **reproduit** par `research/checks/cycle001_linear_runs.py` |
| X8 | $v_2(3^ra+1)\le C(1+\log_2a)$ (borne indépendante de $r$) | $a=5$ : $\langle3\rangle=\{1,3\bmod8\}$ mod $2^m$ et $-5^{-1}\equiv3$ ⇒ $\exists r$, $5\cdot3^r\equiv-1\pmod{2^m}$ ; ex. $N=159$ | branche `padic-successive-runs` ; preuve relue |
| X9 | $\sum_{j=1}^kr_j\le F(k,a_0)$ sur toutes les orbites | $a_0=5$, $W=(1^R0)^k$ ; ex. $N=639$, runs $(7,2,3)$ | PR #26 (non validée) |
| X10 | Lemme B (KL) lu universellement | $k=2,\ \lambda=1,\ c=(1,2,1)$ | PR #7 (non validée) |
| X11 | Lemme C1 sans l'hypothèse $c\ge1$ (runs constants) | $c=0$ : $(1^d0)^\infty$ réalisé par $0,1,-5,-19/11,-65/49,\dots$ | cycle 001 ; script, test 2 |
| X12 | Critère de Liouville **naïf** : « $r_m+m-\beta o_m\to\infty$ ⇒ réalisation irrationnelle » | Itinéraire de $1$ : $(10)^\infty$, $r_m=1$, $o_m=m$, $r_m+m-\beta o_m=1+(1-\beta)m\to\infty$, or $\xi=1$ | Remarque de préparation du cycle 001 ; la correction $-\log_2(1+G_m)$ est nécessaire (voir `hypotheses.md` H4) |
| X13 | Exposant 11 dans la borne « sibling correction » avec membre droit linéaire | $S_N$ = entiers $5<x\le N$, résidus $1,7,11,13,17,19,23\bmod24$ : rapport $\asymp N^{5/72}$ | PR #16 (non validée) ; preuve asymptotique |
| X14 | « Signe de la somme réelle = signe de la somme 2-adique » | $3\sum_j(a_j-a_{j+1})$, $a_j=2^{2^j}/(1+2^{2^j})$ : $-1$ dans $\mathbb R$, $2$ dans $\mathbb Q_2$ | branche `even-density-structural-audit` §7 |
| X15 | « Les bornes archimédiennes (hauteur, $R$ borné, $r\le\log_2(n+1)$) imposent une densité de pairs positive » | Modèle réel à branches prescrites $1^i0$ depuis $x_0=257$ ; échec de réalisation visible dès $290\to871/2$ | branche `even-density-structural-audit` §6 (pas un contre-exemple à (C)) |
| X16 | (H) pour un $B\le1$ et un $A$ fini | Tout $A$ : $m>2A+4$, $M=5\cdot2^r-1$ avec $v_2(5\cdot3^r+1)\ge m$ (B4). Témoin $A\le6$ : $r=757$, somme des deux runs $=772$, $5^3<2^7$ | cycle 002 ; `research/checks/cycle002_run_bound.py` |
| X17 | Diagonale $A=B=9/5$ dans (H) | Graine 27, treize premiers runs somme 33 ; $28^3<2^{16}$ donc $(9/5)(13+\log_228)<33$. Ne tue pas $A=B=2$ | cycle 002 ; même script |
| X18 | « B7 retrouve les runs en progression arithmétique » | Mot triangulaire $(1^j0)_{j\ge1}$ : $Q_m\le-\log_2 E(m)$ avec $E(m)=3^{o_m-1}/2^{o_m+2m}\to+\infty$, donc $Q_m\to-\infty$ | cycle 003 §4 ; `research/checks/cycle003_liouville.py` |
