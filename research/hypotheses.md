# Hypothèses, conjectures et lemmes candidats

Statuts : **OUVERT** · **CANDIDAT** (énoncé précis, preuve esquissée non vérifiée) ·
**HEURISTIQUE** (argument non rigoureux) · **RÉFUTÉ PARTIELLEMENT** · **CAS PARTICULIER PROUVÉ**.
Conventions de `proved.md`. Orbite « non bornée » = orbite positive de $T$ non bornée.

## H1 — (C) Densité orbitale positive des pas pairs — OUVERT, majeur
$\forall N>0$ : orbite non bornée ⇒ $\eta_N:=\liminf_tE(t)/t>0$.
- Équivaut à $\limsup_tH(t)/t<\beta$ (C3, non validé : $\limsup H/t=\beta-\delta\eta_N$).
- Améliorer la pente $1/\beta$ de la complexité conditionnelle ⇔ (C) (même source).
- Toujours $\eta_N\le\beta/\delta$ pour une orbite non bornée (B6 : $H\ge0$ et $R=o(E)$).
- Garcia–Tal 1999, lu au cycle 021, donne la densité de Banach nulle.
  L'inégalité (6) implique la sommabilité des réciproques, et B28 la
  prouve pour \(T\) sans Heppner : \(R(t)\) converge, et le comptage
  donne \(\sum 1/n<394<61344/65\) (X61). L'attribution de cette
  constante à Garcia–Tal reste fausse (X57). Même alors,
  \(\limsup E(t)/t=\beta/\delta-(1/\delta)\liminf\log_2(n_t+1)/t\).
  Cela ne donne pas H1. Ne pas reprendre cette lecture pour un gain
  logarithmique, ni pour attribuer la constante de C3 au PDF.
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
Le signe moins n'est pas ultimement périodique : infinité de zéros et
$r_k\to+\infty$ (X24). La phrase sans hypothèse de zéro est fausse pour
$1^\infty$ (X26). Il ne se réduit pas terme à terme à la forme de B2 ou
de B11 (X25). Si $\sigma=a/b$, alors $v_2(a-2b)=66$ et
$\max(|a|,b)\ge(2^{66}+2)/3$ (B14). Cette valuation de rang $1$ exclut
$2+2^{67}$ (X27). La fraction $2+2^{66}$ satisfait le rang $1$ et la
borne de hauteur ; elle est exclue au rang $2$, car $v_2(A_2)=74\neq96$.
L'apériodicité ne réfute pas H3. L'irrationalité reste ouverte.
Le cycle 019 a lu Bernstein–Lagarias 1996, (1.5) et (1.6), sur le PDF
d'auteur. L'égalité imprimée
\(\Phi(\mathbb Q\cap\mathbb Z_2)=\mathbb Q\cap\mathbb Z_2\) est cet
énoncé (B25). Le papier la laisse comme conjecture. L'inclusion
opposée est donnée comme connue et n'est pas redémontrée. Pour chaque
\(k\ge 1\), \(\Phi^k(\mathbb Q\cap\mathbb Z_2)=\mathbb Q\cap\mathbb Z_2\)
est la même conjecture, pas une forme plus faible. L'inclusion
séparée \(\mathbb Z^+\subseteq\Phi(\tfrac13\mathbb Z)\) est l'atteinte
de \(1\) sous \(C\) et sous \(T\) (B26). Le sens réciproque exclut
d'abord les entiers : \(\Phi(0)=0\), et \(\Phi(Q)\) est un rationnel
strictement négatif pour tout autre entier \(Q\). Elle reste ouverte.
Ne pas la rouvrir depuis ces formules, ni depuis un itéré, ni depuis
Bernstein 1994.

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
  ouverte : le cycle 009 donne $v_2(a-2b)=66$, donc
  $\max(|a|,b)\ge(2^{66}+2)/3$ (B14), l'absence de queue périodique par
  l'infinité de zéros (X24) et l'absence de forme polynomiale sur une
  progression arithmétique (X25). La valuation de rang $1$ exclut
  certaines hauteurs supérieures, et le rang $2$ exclut $2+2^{66}$ (X27).
  Ne pas la relancer sans un outil qui ne soit ni B7
  ni VW 1989. Les placements de zéros non réductibles par un préfixe fini restent
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

## H7 — Potentiels $V(n)=\log_2(n+1)+c\,v_2(n+1)$ (axe A) — RÉFUTÉ (X31, B17)
Pour tout réel $c$, $V$ n'est pas une fonction de Lyapunov stricte hors de
$\{1,2\}$ (cycle 012 §2). Le pas impair diminue bien $V$ de $c-\beta$ lorsque
$c>\beta$, mais $6\to 3$ l'augmente. Toute fonction réelle de la seule
valuation $v_2(n+1)$, ajoutée à $\log_2 n$ ou à $\log_2(n+1)$, échoue aussi
sur $U$ en l'un des trois impairs $3$, $7$, $9$ (B17). L'exception finie
et le couple $(n\bmod M, v_2(n+1))$, sans compteurs, sont fermés pour
toute hauteur strictement croissante (B18, X32). La forme qui ajoute
$\beta\omega+\gamma\Omega+R(\Omega-\omega)$ est le théorème 1 de la
note du 19 octobre 2026, vérifié au cycle 013 (B19) : la moitié
élémentaire est prouvée, et l'existence pour chaque module est une
réduction à deux théorèmes analytiques non relus. Les certificats
affichés valent pour \(X_0<187\) (\(M=24\)) et \(X_0<123\) (\(M=1\)).
X33 montre qu'un trajet premier vers premier suffit pour \(M=8\) et
\(X_0<59\). Cela ne rouvre pas l'architecture. Ne pas la relancer,
avec ou sans compteurs.

## H8 — Équivalences opératorielles de Mori 2024 (axe C) — FERMETURE RÉFUTÉE ; THÉORÈMES NON ADOPTÉS
La réduction au premier retour est prouvée (B12). Elle n'est pas une preuve
de la conjecture. L'objection « la définition 3.4.4 demande l'égalité sans
fermeture, et le lemme 4.2.2 ne la donne pas » est réfutée (X23) : la source
v2 met une barre des deux côtés. Les théorèmes 4.2.7 et 4.3.10 ne sont pas
adoptés. Leur nécessité cite Conway 2000, chapitre 2, proposition 13.3,
non lu. L'esquisse d'orbite déjà fermée par Kadison 1957, signalée par la
revue `6082060844`, n'est pas reproduite et n'est pas une prémisse. Ne pas
relancer la lecture sans barres. L'implication globale de H6 est B13.
Le signe moins est traité au cycle 009 : hauteur B14, irrationalité
ouverte. La revue `6082502361` confirme l'exclusion de $2+2^{66}$ au
rang $2$ et ne la transforme pas en irrationalité. La descente accélérée
de $5\cdot2^k-1$ est B15 : $\tau\ge k+1$ pour $k\ge3$. Pour $k$ impair,
le second bloc donne $\tau\ge k+v_2(5\cdot3^k+1)-1$, et $\tau-k$ n'est
pas borné. Il n'y a pas de formule close jusqu'à la descente, ni de
preuve que $\tau>2k$ infiniment souvent. L'équation de Berg–Meinardus
est le cycle 011 : reformulation, pas un lemme de descente, et pas un
nouveau lemme sur $\{e_{2^k}\}$. La revue `6082791301` corrige le résidu
du §5 (X30). L'équivalence de la conjecture 3 est le §12 ; elle ne donne
pas de descente. La revue `6082845312` confirme ce correctif. Le cycle 012
réfute H7 (X31, B17). La revue `6082913526` confirme ces deux énoncés
et ferme l'exception finie ainsi que le couple résidu–valuation sans
compteurs (B18, X32). Elle n'en tire pas de descente. Le théorème 1 de la note, avec
compteurs, est le cycle 013 (B19) : pas une seconde preuve, et pas
une contrainte sur une orbite divergente.

## H9 — Tao 2022 et les classes de congruence (axe C) — FERMÉ (B20, X34)
Le théorème 1.3, lu sur le PDF de *Forum Math. Pi* 10 (2022), dit que
\(\mathrm{Col}_{\min}(N)<f(N)\) pour presque tout \(N\) en densité
logarithmique, dès que \(f(N)\to+\infty\). Ce théorème n'établit, pour aucun
couple \((a,m)\), que chaque entier de la classe passe sous
\(f\). Chaque classe a densité \(1/m\) (cycle 014 §2). Presque tout
élément de chaque classe fixée passe sous \(f\). Le théorème ne
garantit pas qu'une classe entière soit bonne. Pour \(f(N)=N+1\),
\(\mathrm{Col}_{\min}(N)\le N<f(N)\) pour tout \(N\), donc chaque
classe l'est (X36). La fibre
\(v_2(N)=a\) a densité \(2^{-(a+1)}\) (X35) : ne pas recopier le
\(2^{-a}\) imprimé après le théorème 1.6. X34 est l'ensemble
\(m!+r\), de densité logarithmique nulle et de densité naturelle
nulle, qui rencontre toutes les classes. La borne constante de la
remarque 1.4 reste ouverte et n'est pas la prochaine question. Ne
pas relire ce théorème pour en tirer une classe entière.

## H10 — Retour uniforme dans une classe (axe A) — FERMÉ (B21)
Pour \(U(n)=(3n+1)/2^{v_2(3n+1)}\), aucun triple \((m,a,T)\) ne fait
revenir tout \(n>1\) de la classe \(a\pmod m\) dans la classe, en
restant strictement plus petit, en au plus \(T\) pas (B21, X37). Le
résidu autre que \(1\) échoue par comptage. La classe \(1\pmod m\)
échoue par un cylindre de montée, direct si \(4\nmid m\), et après un
pont de divisions par \(4\) sinon. Un seul vecteur de valuations a un
coefficient \(3^t 2^{L-S}\) qui ne conserve pas la classe : c'est un
corollaire du codage, pas une seconde preuve. Aucune orbite n'est
exclue. Ne pas relancer ce certificat, ni une union finie de vecteurs
de longueur bornée sur une seule classe. La revue `6093792860`
confirme B21. Le rang \(0\) reste dans la classe ; l'évitement
commence au rang \(1\). La revue `6093856144` confirme le même
énoncé. Le retour de B21 est strictement plus bas. Pour \(m=2\),
\(U(n)\) est impair, donc la classe est rejointe au premier pas.
Ce retour peut être ascendant, par exemple \(U(3)=5\), et peut
descendre, par exemple \(U(9)=7\) (X40, revue `6093923797`). Le cas
\(4\nmid m\) retarde la descente. Le cas \(4\mid m\) retarde tout
retour positif.

## H11 — Runs impairs de longueur au plus 1 — FERMÉ (élémentaire, X38)
Pour \(T\), aucun \(R\ge 1\) ne fait passer toute orbite positive de
runs impairs bornés par \(R\) strictement sous son départ : l'orbite
\(1\to 2\to 1\) a des runs de longueur \(1\). Pour \(n>1\), le cas
\(R=1\) descend en au plus deux pas. Si tous les runs valent au plus
\(1\), l'orbite atteint \(1\). La suite des longueurs de runs de
\(5\) est périodique et \(5\) ne l'est pas (X39). Une suite de
parités périodique dès le départ est un cycle. Ne pas relancer
\(R=1\). La formule close vaut jusqu'au premier pair inclus ; pour
\(n=1\), \(T^2(1)=1\) (revue `6093856144`). Soit \(P(R)\) l'atteinte
de \(1\) pour toute orbite dont chaque run impair a longueur au
plus \(R\). L'existence d'un \(R\ge 2\) tel que \(P(R)\) équivaut à
\(P(2)\). La lecture pour tout \(R\ge 2\) est plus forte et n'est
pas ouverte. Steiner (1977) n'est pas lu dans ce paragraphe : le cycle 016
ne l'obtient pas.

## H12 — Runs impairs de longueur au plus 2 — OUVERT, conjecture publiée (B22)
\(P(2)\) est la conjecture 4.13 de Yolcu, Aaronson et Heule,
arXiv:2105.14697v3 : toute trajectoire non convergente de \(C\)
rencontre \(7\pmod 8\). L'équivalence avec les runs de \(T\) est B22.
Le théorème 4.10 règle \(2,3,4,6\pmod 8\). Les conjectures 4.11,
4.12 et 4.14 restent ouvertes dans le même texte. \(P(2)\) implique
4.14 par inclusion des hypothèses (X42). L'implication inverse ne
suit pas de cette inclusion : éviter \(\{5,7\}\) est plus restrictif
qu'éviter \(7\), et l'orbite convergente de \(5\) sépare les
hypothèses. Pour déduire \(P(2)\) de 4.14, il reste la queue issue
du premier terme \(\equiv 5\pmod 8\) (cycle 016 §9). Cette réduction
ne démontre pas que 4.14 n'entraîne pas \(P(2)\). Steiner (1977)
n'est pas obtenu. Simons–de Weger, version 1.44, ne traitent que
les orbites périodiques, avec \(m\le 75\) minima. Le cycle
\(-5\to-7\to-10\) évite \(7\pmod 8\) (X41) : une preuve doit utiliser
la positivité. Ne pas relancer \(P(2)\) comme lemme frais, ni ces
quatre conjectures, dans un cycle qui n'aurait pas d'autre outil.

## H13 — Korec 1994 et les classes de congruence (axe C) — FERMÉ (B23, X43, X44)
Le théorème 1, lu sur le PDF de *Math. Slovaca* 44 (1994), 85–89, dit
que \(M_c\) a une densité asymptotique \(1\) pour \(c>\log_4 3\). La
densité relative dans chaque classe vaut \(1\). Aucune classe n'est
entièrement hors de \(M_c\). X34 montre qu'une densité naturelle \(1\)
n'inclut pas la classe. Le prédicat est un itéré \(<y^c\), pas
l'atteinte de \(1\). La descente universelle sur tout entier positif,
y compris \(1\), est fausse. L'équivalence avec la conjecture vaut
pour les \(y\ge 2\) et ne la décide pas. Le certificat \(S_m<md\) rate
\(y\equiv -1\pmod{2^m}\). La formule imprimée de \(d\) vaut
\(c/\log_2 3+\tfrac14\) et ne satisfait pas \(d<c/\log_2 3\) (X45).
La parenthèse \(\log_2 y\) n'est pas une borne de première descente
pour tout \(y\in M_c\) (X46). L'équation (4) n'est pas la transformée
logarithmique de l'inégalité de puissances (X47) : elle reste une
condition suffisante plus forte. Ne pas redémontrer ce théorème, ni
abaisser l'exposant, ni réécrire la preuve pour remplacer (4), ni
relire Tao, Terras ou Everett pour en tirer une classe qui atteint
\(1\). Inselmann (2024) reste non audité et
n'est pas la prochaine question.

## H14 — Eliahou 1993 et les trajectoires non périodiques — FERMÉ POUR LA PORTÉE (B24)
Le résumé, lu, borne une orbite cyclique non triviale. Le fac-similé
de 1993 n'a pas été obtenu. La transcription OCR citée par la revue
`6094741450` n'est pas ce fac-similé et n'a pas été lue. Le compte
rendu zbMATH met la forme linéaire sous \(\min\Omega>2^{40}\).
Lagarias, entrée 53, l'énonce pour tout cycle non trivial et invoque
la vérification jusqu'à \(2^{40}\). Ces deux phrases ne sont pas
adoptées. Halbeisen–Hungerbühler, théorème 2, attribuent à Eliahou la
borne \(|C|\ge k(\min C)\). Le cycle trivial réalise \(k(1)=2\). Pour
ce critère, \(k(2^{40})=17087915\). Ce nombre ne remplace pas la
vérification sous le seuil. Une orbite positive non bornée n'est pas
un cycle (B24) : l'itinéraire de parité ultimement périodique force
l'égalité de la queue, par le cycle 015 §10 (X48). Le §5 lu dit que
ces bornes ne prouvent pas l'unicité du cycle. Elles ne prouvent pas
non plus que toute suite est bornée. Ne pas redémontrer l'estimation,
ne pas réécrire B24, et ne pas importer une vérification machine. Ne
pas rouvrir Crandall ni les théorèmes 3 et 4.

## H15 — Progression de raison fixe et horizon non borné (axe A) — FERMÉ (B27)
Pour \(a>1\) impair et \(d>0\) pair, le rayon \(n=a+kd\) partage
exactement \(v_2(d)\) parités (B27). Un mot commun d'exposants de \(U\)
a une somme au plus \(v_2(d)-1\). S'il décrit la première descente de
chaque terme, \(\tau_U\) est constant et au plus \(v_2(d)-1\). Sans
cette comparaison au départ, un exposant au moins \(2\) ne donne pas
\(\tau_U\le v_2(d)\) (X53). Le cas \(n\equiv 1\pmod 4\) reste
\(\tau_U=1\) (X40), même si l'exposant n'est pas constant. C'est le
contre-exemple de la réciproque (X56) : sur \(5+4k\), \(\tau_U=1\),
\(v_2(3\cdot 5+1)=4\) et \(v_2(3\cdot 9+1)=2\). La progression
\(3+4k\) illustre l'implication directe. Une classe à indices
entiers et raison négative se réécrit par le plus petit terme
\(>1\), pas par le plus petit terme positif. Les classes
d'A3, leur diagonale \(n_m=2^m q_m-1\), les Mersenne et
\(5\cdot 2^k-1\) ne sont pas une autre réponse : la diagonale est le
certificat déjà prouvé, et les deux dernières familles n'ont pas de
formule jusqu'à la descente. Ne pas relancer cette recherche. Une union
finie de raisons fixes peut couvrir les impairs (X54). Ce qui est fermé
est une couverture dont chaque pièce a un mot commun de première
descente. Le quantificateur est le rayon de raison positive (X55).
