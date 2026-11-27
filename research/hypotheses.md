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
$r_{k+1}/r_k\to\lambda>\log_2 3$, y compris après un préfixe fini (cycle 004 §8, via B7) ;
au seuil $\lambda=\log_2 3$, la seule famille de signe plus du même paragraphe.

## H4 — Critère de type Liouville — PROUVÉ (B7, cycle 003)
Mot $w$ avec une infinité de $0$, $o_j$ comme en B1, $r_m=o_{m+1}-o_m$,
$G_m=\sum_{j=1}^m 2^j(2/3)^{o_j}$. Si $\sup_m Q_m=+\infty$ avec
$Q_m=r_m+m+1-\beta o_m-\log_2(1+G_m)$, alors $\xi_w\notin\mathbb Q$.
- La valuation est exacte : $v_2(A_m)=m+1+o_{m+1}$, pas seulement $\ge$.
- La correction $G_m$ est nécessaire (X12). La somme commence à $j=1$.
- Cas non vide : B8 (runs $2^k$), B9 (runs de Fibonacci, $Q_k>k$, rapport limite
  $1/\varphi>\beta$), et tout mot à un zéro par bloc avec
  $r_{k+1}/r_k\to\lambda>\log_2 3$, y compris après un préfixe fini
  (cycle 004 §8 : $o_k/r_k\to1/(\lambda-1)$, $Q_k\to+\infty$). Cas aveugle : le mot
  triangulaire, $Q_m\to-\infty$ (X18) ; et, par le même critère,
  $1<\lambda<\log_2 3$ donne $Q_k\to-\infty$. À $\lambda=\log_2 3$, les deux
  familles $r_1=64$, $r_k=\lfloor\beta o_k\rfloor\pm\lfloor\sqrt{o_k}\rfloor$
  ($k\ge2$) ont le même rapport limite : $Q_k\to+\infty$ pour le signe plus,
  $Q_k\to-\infty$ pour le signe moins. L'irrationalité du signe moins reste
  ouverte. Les placements de zéros non réductibles par un préfixe fini restent
  ouverts. Les runs quasi linéaires restent H5 : la famille appariée est
  l'identité B11. Sur ce mot $\sup Q_m=Q_2=\log_2(2048/217)$, donc
  $\max(|a|,b)\ge10$, puis $Q_m\to-\infty$ : B7 ne tranche pas, et
  l'irrationalité reste ouverte.
- Les contrôles du cycle 003 testent les fenêtres atteintes depuis les départs
  choisis. Ils ne recensent pas les cycles de $3x+b$ (X19).
- Portée : rien de neuf pour (C). Une orbite entière non bornée a déjà
  $r_m\le\beta o_m-m+O_N(1)$ par l'identité de hauteur.

## H5 — Au-delà de VW : runs quasi linéaires — OUVERT
Exemples encore ouverts : $r_j=cj+d+p_j$ avec $p$ périodique non constant,
$r_j=\lfloor j/P\rfloor$. Pour $l\ge2$,
$\Gamma(2,0)=(5-\sqrt{17})/4<\gamma=1-\log2/\log3$ : VW 1989 ne s'applique pas.
La famille $r_j=j+[j\text{ impair}]$ est réduite (B11) :
$4\xi+1+2f_{81/16}(4)+f_{81/16}(9)=0$ dans $\mathbb Q_2$. Sur ce $q$,
$\gamma>\Gamma(2,0)$ est prouvé par $8<9$ et $121<153$. Les Satz 1 et 2 de
Bundschuh 1974 sont archimédiens et leur hypothèse échoue ($256>243$,
$80>49$). Les originaux de Bézivin 1988 et d'Amou–Väänänen 2005 n'ont pas
été lus ; les énoncés cités ne donnent pas l'exclusion 2-adique. B7 donne
seulement $\max(|a|,b)\ge10$, car $\sup Q_m=Q_2=\log_2(2048/217)$, puis
$Q_m\to-\infty$ (X22). L'irrationalité de cette famille reste ouverte.
Ne pas la relancer sans un énoncé p-adique dont l'hypothèse est satisfaite
par $q=81/16$. Ce n'est pas la prochaine question.

## H6 — Certificats à poids bornés et horizon dépendant de la hauteur (axe A) — PROUVÉ (B13)
L'énoncé initial est prouvé : si $0<\ell\le W\le h$, $0<\rho<1$, et si tout
$n\ge N_0$ admet un temps de contraction $t\le B(n)$ de $\Phi(n)=n\,W(n)$, alors
$B(n)>\log_2 3\cdot\log_2 n-C$ pour une infinité de $n$. La constante
$C=\log_2 K+J(\log_2 3)^2$ ne dépend que de $K=\rho h/\ell$ et de $\rho$
(cycle 008 §4–§5). Ici $t_*$ est le maximum de $\{0\}\cup\{t\ge1:(3/2)^t<2K\}$,
et $J=(m_*-1)\,t_*$. Aucun poids borné ne rend la prémisse vraie avec
$B(n)=o(\log n)$. X21 ne la réfute pas : $\ell=1$, $h=2$, $\rho=5/6$ certifie
les Mersenne seulement, en un pas. Il réfute l'obstruction locale sans seuil.
Si $K\le3/2$, le témoin est le Mersenne et $t>\delta L-\log_2 K$, déjà dans
la preuve de B10. La forme uniforme $3\cdot2^t>2\cdot3^L$ est plus faible
pour $K\le3/4$ : $h=\ell$, $\rho=1/4$ donne $J=0$ et $C=-2$. Elle est plus
forte pour $K>3/4$, où $J\ge1$. La forme sans poids $T^t(n)\le\rho n$ est le
cas $K=\rho$ de la même estimation : $\rho\cdot2^t>3^L$ (cycle 008 §1). Si
$\rho\le0$, aucune contraction n'existe.
Le coefficient de tête reste sous Applegate–Lagarias 2003, (4) et théorème 1.1.
L'existence d'un certificat n'est pas montrée. Ne pas relancer B13, ni B10, ni X21.

## H7 — Potentiels cohomologues $V(n)=\log_2(n+1)+c\,v_2(n+1)$ (axe A) — OBSERVATION
Pour $c>\beta$, $V$ décroît strictement à chaque pas impair d'un run (neutralise Mersenne),
mais $V-\log_2(n+1)=c\,r$ est une correction de bord : sur de longues fenêtres $V$ suit la hauteur.
Horizon fixe encore impossible (adversaire $2(2^Ra-1)$, $R>B$). Ne pas relancer sans nouvelle idée.

## H8 — Équivalences opératorielles de Mori 2024 (axe C) — FERMETURE RÉFUTÉE ; THÉORÈMES NON ADOPTÉS
La réduction au premier retour est prouvée (B12). Elle n'est pas une preuve
de la conjecture. L'objection « la définition 3.4.4 demande l'égalité sans
fermeture, et le lemme 4.2.2 ne la donne pas » est réfutée (X23) : la source
v2 met une barre des deux côtés. Les théorèmes 4.2.7 et 4.3.10 ne sont pas
adoptés. Leur nécessité cite Conway 2000, chapitre 2, proposition 13.3,
non lu. L'esquisse d'orbite déjà fermée par Kadison 1957, signalée par la
revue `6082060844`, n'est pas reproduite et n'est pas une prémisse. Ne pas
relancer la lecture sans barres. L'implication globale de H6 est B13.
La question suivante est la rationalité du signe moins au seuil
$\log_2 3$, pas un nouveau lemme sur $\{e_{2^k}\}$.
