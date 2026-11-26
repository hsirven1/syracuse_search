# Hypothèses, conjectures et lemmes candidats

Statuts : **OUVERT** · **CANDIDAT** (énoncé précis, preuve esquissée non vérifiée) ·
**HEURISTIQUE** (argument non rigoureux) · **RÉFUTÉ PARTIELLEMENT** · **CAS PARTICULIER PROUVÉ**.
Conventions de `proved.md`. Orbite « non bornée » = orbite positive de $T$ non bornée.

## H1 — (C) Densité orbitale positive des pas pairs — OUVERT, majeur
$\forall N>0$ : orbite non bornée ⇒ $\eta_N:=\liminf_tE(t)/t>0$.
- Équivaut à $\limsup_tH(t)/t<\beta$ (C3, non validé : $\limsup H/t=\beta-\delta\eta_N$).
- Améliorer la pente $1/\beta$ de la complexité conditionnelle ⇔ (C) (même source).
- Toujours $\eta_N\le\beta/\delta$ pour une orbite non bornée (B6 : $H\ge0$ et $R=o(E)$).
- Obstacle : les bornes archimédiennes seules ne suffisent pas (X15) ; il faut l'intégralité.
- Non attaqué directement tant qu'aucun mécanisme nouveau n'est identifié.

## H2 — (H) Cible de la PR #26 — OUVERT, conjecture majeure (cycle 002)
$\exists A,B\ \forall N>0,i\ge0,k\ge1$ : $\sum_{j=0}^{k-1}r_{i+j}\le Ak+B\log_2(M_i+1)$.
Consigne du cycle 002 (B4–B6), plus une esquisse :
1. $B\le1$, tout $A$ : **RÉFUTÉ** (B4, X16). Les Mersenne donnent seulement $B\ge1$.
2. $A<1/\beta$ : incompatible avec une orbite positive non bornée (B6). Avec $A\ge1/\beta$,
   (H) implique (C) uniforme, $\eta_N\ge1/(A+1)$.
3. Fenêtres de longueur $\le K$ : prouvées (B5), constante géométrique en $K$.
4. Aucun $B>1$ n'est prouvé ni réfuté. La famille $a=5$ ne peut pas réfuter $B>1+\delta$
   (minoration $r>(m-\log_25-1)/\delta$) ; pour $1<B\le1+\delta$ le plus petit $r$ calculé
   jusqu'à $m=40$ reste exponentiel en $m$. Obstacle : cycle 002 §5.
5. HEURISTIQUE (modèle aléatoire des parités) : (H) plausible pour $A>1$ et $B>B_0(A)$.
   La diagonale $A=B=9/5$ est fausse (X17, graine 27) ; $A=B=2$ survit aux contrôles finis
   du cycle 002. Ne pas reprendre (H) comme prochain petit lemme.

## H3 — Conjecture de périodicité (Lagarias 1985) — OUVERT ; CAS PARTICULIER PROUVÉ
Tout $\xi\in\mathbb Q\cap\mathbb Z_2$ a un itinéraire ultimement périodique (la réciproque est un théorème).
Pour les entiers positifs, elle équivaut à la non-divergence. Cas prouvés : runs ultimement
en progression arithmétique de raison $\ge1$ (B2, via VW 1989) ; runs $2^k$ (B8, élémentaire) ;
runs $F_{k+2}$ (B9, élémentaire, via B7) ; plus généralement, un zéro par bloc et
$r_{k+1}/r_k\to\varphi$ (cycle 004 §8, via B7).

## H4 — Critère de type Liouville — PROUVÉ (B7, cycle 003)
Mot $w$ avec une infinité de $0$, $o_j$ comme en B1, $r_m=o_{m+1}-o_m$,
$G_m=\sum_{j=1}^m 2^j(2/3)^{o_j}$. Si $\sup_m Q_m=+\infty$ avec
$Q_m=r_m+m+1-\beta o_m-\log_2(1+G_m)$, alors $\xi_w\notin\mathbb Q$.
- La valuation est exacte : $v_2(A_m)=m+1+o_{m+1}$, pas seulement $\ge$.
- La correction $G_m$ est nécessaire (X12). La somme commence à $j=1$.
- Cas non vide : B8 (runs $2^k$), B9 (runs de Fibonacci, $Q_k>k$, rapport limite
  $1/\varphi>\beta$), et tout mot à un zéro par bloc avec $r_{k+1}/r_k\to\varphi$
  (cycle 004 §8 : $o_k/r_k\to\varphi$, $Q_k\to+\infty$). Cas aveugle : le mot
  triangulaire, $Q_m\to-\infty$ (X18). Pas de conclusion uniforme pour un taux
  $\lambda$ avec $\lambda-1\le\beta$. Les runs quasi linéaires restent H5.
- Les contrôles du cycle 003 testent les fenêtres atteintes depuis les départs
  choisis. Ils ne recensent pas les cycles de $3x+b$ (X19).
- Portée : rien de neuf pour (C). Une orbite entière non bornée a déjà
  $r_m\le\beta o_m-m+O_N(1)$ par l'identité de hauteur.

## H5 — Au-delà de VW : runs quasi linéaires — OUVERT
Exemples : $r_j=cj+d+p_j$ avec $p$ périodique non constant, $r_j=\lfloor j/P\rfloor$.
La réalisation devient une combinaison de $l\ge2$ valeurs de Tschakaloff ; or
$\Gamma(2,0)=(5-\sqrt{17})/4\approx0{,}219<\gamma=1-\log2/\log3\approx0{,}369$ :
VW 1989 ne s'applique plus. Il faut d'autres résultats p-adiques (à rechercher) ou une obstruction.

## H6 — Certificats à poids bornés et horizon dépendant de la hauteur (axe A) — CANDIDAT
Si $0<\ell\le W\le h$ réels, $\rho<1$, et tout $n\ge N_0$ admet $t\le B(n)$ avec
$T^t(n)W(T^tn)\le\rho\,nW(n)$, alors $B(n)\ge\delta\log_2n-O(1)$ pour une infinité de $n$.
Esquisse : la chaîne vérifie $n_k\le(h/\ell)\rho^kn_0$ ; partant de $2^L-1$, elle doit sauter
la montée (temps $L$, valeur $3^L-1$) puis redescendre de $\beta L-O(1)$ pas au moins.
Probablement classique ; à comparer à Applegate–Lagarias (bornes inférieures de temps d'arrêt).

## H7 — Potentiels cohomologues $V(n)=\log_2(n+1)+c\,v_2(n+1)$ (axe A) — OBSERVATION
Pour $c>\beta$, $V$ décroît strictement à chaque pas impair d'un run (neutralise Mersenne),
mais $V-\log_2(n+1)=c\,r$ est une correction de bord : sur de longues fenêtres $V$ suit la hauteur.
Horizon fixe encore impossible (adversaire $2(2^Ra-1)$, $R>B$). Ne pas relancer sans nouvelle idée.
