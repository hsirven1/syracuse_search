# Hypothèses, conjectures et lemmes candidats

Statuts : **OUVERT** · **CANDIDAT** (énoncé précis, preuve esquissée non vérifiée) ·
**HEURISTIQUE** (argument non rigoureux) · **RÉFUTÉ PARTIELLEMENT** · **CAS PARTICULIER PROUVÉ**.
Conventions de `proved.md`. Orbite « non bornée » = orbite positive de $T$ non bornée.

## H1 — (C) Densité orbitale positive des pas pairs — OUVERT, majeur
$\forall N>0$ : orbite non bornée ⇒ $\eta_N:=\liminf_tE(t)/t>0$.
- Équivaut à $\limsup_tH(t)/t<\beta$ (C3, non validé : $\limsup H/t=\beta-\delta\eta_N$).
- Améliorer la pente $1/\beta$ de la complexité conditionnelle ⇔ (C) (même source).
- Toujours $\eta_N\le\beta/\delta$ pour une orbite non bornée (élémentaire : $H\ge0$ et $R=o(E)$).
- Obstacle : les bornes archimédiennes seules ne suffisent pas (X15) ; il faut l'intégralité.
- Non attaqué directement tant qu'aucun mécanisme nouveau n'est identifié.

## H2 — (H) Cible de la PR #26 — OUVERT ; régime $B\le1$ réfuté (esquisse, à consigner au cycle 2)
$\exists A,B\ \forall N>0,i\ge0,k\ge1$ : $\sum_{j=0}^{k-1}r_{i+j}\le Ak+B\log_2(M_i+1)$.
Observations de préparation (non encore consignées comme résultats) :
1. $B<1$ : faux (Mersenne, $k=1$, $r_0=h=\log_2(N+1)$).
2. $B=1$, tout $A$ : faux. $N=5\cdot2^{r_0}-1$ avec $5\cdot3^{r_0}\equiv-1\pmod{2^m}$ (X8) :
   $k=2$, $r_0+r_1\ge r_0+m-1$ contre $2A+r_0+\log_25$.
3. (H) avec $A<1/\beta$ ⇒ aucune orbite non bornée (car $\eta_N\ge1/(A+1)>\beta/\delta$).
   Avec $A\ge1/\beta$ : ⇒ (C) uniforme. **(H) n'est donc dans aucun régime un « petit lemme ».**
4. HEURISTIQUE (modèle aléatoire des parités) : (H) plausible pour $A>1$ et $B>B_0(A)$.

## H3 — Conjecture de périodicité (Lagarias 1985) — OUVERT ; CAS PARTICULIER PROUVÉ
Tout $\xi\in\mathbb Q\cap\mathbb Z_2$ a un itinéraire ultimement périodique (la réciproque est un théorème).
Pour les entiers positifs, elle équivaut à la non-divergence. Cas prouvé : runs ultimement
en progression arithmétique de raison $\ge1$ (B2, via VW 1989).

## H4 — Critère de type Liouville pour les réalisations rationnelles — CANDIDAT
Mot $w$ avec une infinité de 0, $o_j$ comme en B1, $r_m=o_{m+1}-o_m$, $G_m=\sum_{j\le m}2^j(2/3)^{o_j}$.
Si $\sup_m\,[\,r_m+m+1-\beta o_m-\log_2(1+G_m)\,]=+\infty$, alors $\xi_w\notin\mathbb Q$.
- Esquisse : $\sigma=-2(\xi+1)=a/b$ ; $A_m=b\,3^{o_m}(\sigma-\sigma_m)\in\mathbb Z\setminus\{0\}$,
  $v_2(A_m)\ge m+1+o_{m+1}$, $|A_m|\le3^{o_m}(|a|+bG_m)$.
- La correction $G_m$ est nécessaire (X12 : itinéraire de 1).
- Portée limitée : pour une orbite entière non bornée, l'identité de hauteur donne déjà
  $r_m\le\beta o_m-m+O_N(1)$ ; H4 n'apporte rien de neuf pour (C), seulement pour les rationnels.

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
