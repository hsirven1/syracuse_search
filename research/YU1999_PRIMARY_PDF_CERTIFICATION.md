# Certification primaire du théorème de Yu (1999), spécialisation uniforme (V)

**Date : 28 octobre 2026. Statut : PROUVÉ PAR APPLICATION D'UN THÉORÈME PUBLIÉ.**
**La preuve de Yu n'a pas été reformalisée ; le théorème original a été lu et les hypothèses ont été vérifiées.**
Ce document clôt la réserve documentaire de [YU1999_UNIFORM_VALUATION.md](YU1999_UNIFORM_VALUATION.md), PR #25. Il ne revendique aucune priorité scientifique nouvelle ni aucune preuve de Syracuse.

## Document primaire et vérification matérielle

Kunrui Yu, *p-adic logarithmic forms and group varieties II*, **Acta Arithmetica 89.4 (1999), pp. 337–378**, DOI https://doi.org/10.4064/aa-89-4-337-378.

**Fac-similé PDF original fourni et inspecté directement, pas seulement une transcription** : fichier fourni \`aa8944.pdf\`, 42 pages, SHA-256 :
\`5caa9d90742661045332e15ac4b38f03eeff82c41b341f6b01ea5f90648c068d\`.
Les pages PDF **1, 2, 3 et 41** ont été rendues en images et relues visuellement. Elles correspondent aux pages **imprimées 337, 338, 339, 377**. L'article PDF complet a 42 pages. **Le fichier PDF lui-même n'a pas été redistribué ni poussé sur GitHub.**

### Formules vérifiées sur les originaux

- **Page 337 (PDF 1), §1, équation (1.1) et conséquence introductive du théorème 1 :** \(\Xi=\prod_{j=1}^n\alpha_j^{b_j}-1\ne0\), avec \(\alpha_j\) algébriques non nuls dans un champ \(K\). Le résultat affiche
  \[
  \operatorname{ord}_{\mathfrak p}\Xi <
  A(n,d,p,e_{\mathfrak p},f_{\mathfrak p})\,
  \prod_{j=1}^n h_j\,\log B,\qquad
  h_j=\max\{h_0(\alpha_j),\log p\}.
  \tag{Y}
  \]
  Le facteur \(A\) est explicitement numérique et ne dépend que de \(n,d,p,e_{\mathfrak p},f_{\mathfrak p}\), **pas des valeurs \(\alpha_j\)**. La page définit \(h_0\) par renvoi à la page 338.
- **Page 337 (PDF 1), condition (1.2) :** si \(p=2\), alors le champ \(K\) doit contenir \(\zeta_3\). Il n'est pas nécessaire qu'un rationnel \(a\) soit fixe pour toutes les applications du théorème.
- **Page 338 (PDF 2), condition (1.5) :** la hauteur modifiée est
  \[
  h'(\alpha_j)=\max\{h_0(\alpha_j),f_{\mathfrak p}\log p/d\},
  \]
  où \(h_0\) est **la hauteur de Weil logarithmique absolue**.
- **Page 338 (PDF 2), conditions (1.8), (1.9), théorème 1 :** \(B\ge\max(3,|b_1|,\dots,|b_n|)\), \(\operatorname{ord}_{\mathfrak p}\alpha_j=0\), \(\Xi\ne0\). Conclusion du théorème 1 :
  \[
  \operatorname{ord}_{\mathfrak p}\Xi<
  C(n,d,\mathfrak p)\prod_jh'(\alpha_j)\log B.
  \]
- **Page 339 (PDF 3), formule (1.10) :** constante explicite \(C(n,d,\mathfrak p)\), dépendant seulement des invariants de champ, de place et de \(n\). **La condition (1.11)**, qui porte sur une extension par des racines, est introduite par « Furthermore if ... » et **ne sert qu'à améliorer** la constante ; elle **n'est pas nécessaire** pour appliquer le théorème 1 avec la constante générale.
- **Page 377 (PDF 41), lemme 14.1 et §14 :** il suffit, dans la preuve du théorème 1, de considérer les bases multiplicativement indépendantes ; c'est une **réduction dans la preuve**, non une hypothèse de l'énoncé. Les bases dépendantes restent couvertes par le théorème 1.

## Spécialisation exacte

Fixer **une fois pour toutes** \(K=\mathbb Q(\zeta_3)\) avec \(d=2\). Le polynôme minimal \(X^2+X+1\) est irréductible sur \(\mathbb F_2\), de discriminant \(-3\). Donc \(2\) est inerte et non ramifié dans \(K\), avec place unique \(\mathfrak p\mid2\), \(e_{\mathfrak p}=1\), \(f_{\mathfrak p}=2\). Le champ contient \(\zeta_3\), condition (1.2) satisfaite.

Pour **chaque** entier impair \(a\ge1\) et **chaque** \(r\ge1\), poser
\[
n=2,\quad(\alpha_1,\alpha_2)=(3,-a),\quad(b_1,b_2)=(r,1),\quad B=\max(3,r).
\]
Ce sont **deux bases dont la seconde varie avec \(a\)** ; les **invariants du champ et le nombre de bases restent fixes**.

- Les deux \(\alpha_j\) sont non nuls, appartiennent à \(K\), et sont des unités \(\mathfrak p\)-adiques (impairs), d'où (1.9).
- \(\Xi=3^r(-a)-1=-(3^ra+1)\ne0\), d'où (1.1).
- \(B\) vérifie (1.8).
- \(\operatorname{ord}_{\mathfrak p}\Xi=v_2(3^ra+1)\) car \(e_{\mathfrak p}=1\).
- Hauteurs absolues de Weil : \(h_0(3)=\log3\), \(h_0(-a)=\log a\); \(\log a=0\) lorsque \(a=1\), mais les hauteurs **maximales** restent positives.
- Ici \(f_{\mathfrak p}/d=1\), donc la hauteur **modifiée** du théorème 1 coïncide exactement avec celle de la conséquence (Y) :
  \[
  h'(3)=\log3,\qquad h'(-a)=\max(\log a,\log2).
  \]
- (1.11) est facultative ; **aucune indépendance multiplicative n'est nécessaire** (confirmé par le lemme 14.1, p. 377). On peut aussi traiter séparément \(a=3^k\), donnant \(v_2(3^{r+k}+1)\le2\).

La conséquence (Y) fournit donc une **constante absolue** \(A>0\), indépendante de \(a,r\), telle que
\[
v_2(3^r a+1)<A\,(\log3)\,\max(\log a,\log2)\,\log\max(3,r).
\]
Puisque
\[
\max(\log a,\log2)\le (\log2)(1+\log_2a),\quad
\log\max(3,r)\le(\log2)\log_2(2+r),
\]
il existe un **\(C\ge1\) universel** (par exemple \(C=\max\{2,A(\log3)(\log2)^2\}\)) pour lequel
\[
\boxed{\forall a\in2\mathbb N+1,\ a\ge1,\quad\forall r\ge1,\quad
v_2(3^ra+1)\le C(1+\log_2 a)\log_2(2+r).}\tag{V}
\]

Cette **preuve de (V) est complète par invocation explicite du théorème publié de Yu (1999)**. Elle ne dépend pas de la source Yu 2007, d'une transcription tierce, ni d'une simulation.

## Application à la complexité Collatz : portée exacte

La preuve conditionnelle sous (V) dans [PADIC_SUCCESSIVE_RUNS.md](PADIC_SUCCESSIVE_RUNS.md), §5, a été relue et validée dans l'audit contradictoire reçu. Sa conséquence devient donc, **pour toute orbite positive non bornée hypothétique**,
\[
\boxed{p_N(L)\ge\frac L\beta
+\frac{\delta}{\beta\lambda}\log_2L
+\frac1{16C\lambda^2}\log_2\log_2L
-O_N(1),}\tag{P}
\]
pour les grands \(L\), où
\(\delta=\log_2 3,\quad\beta=\log_2(3/2),\quad\lambda=\log_2\delta>0\).

- **(V) : inconditionnelle** ; démontrée via Yu.
- **(P) : conditionnelle seulement** à l'existence d'une orbite positive non bornée ; telle orbite n'est pas connue.
- **Non démontré :** \(\liminf E_N(t)/t>0\), une pente de complexité strictement meilleure que \(1/\beta\), l'existence ou l'exclusion d'une orbite divergente, la conjecture de Syracuse, une priorité scientifique du raffinement log-log.
- **Pas de preuve Lean, ni nouveau test numérique nécessaires pour vérifier l'application de la source**. La preuve de Yu 1999 reste externalisée.

## Verdict et prochaine recherche

**VERDICT : PROUVÉ PAR THÉORÈME PUBLIÉ (V) ; IMPLICATION DE COMPLEXITÉ PROUVÉE SOUS HYPOTHÈSE D'ORBITE NON BORNÉE (P).**

**Prochaine étape mathématique unique :** étudier si l'on peut passer d'un contrôle de **deux runs** à une **dissipation arithmétique sur des blocs de longueur variable**, afin d'obtenir un déficit de hauteur linéaire en temps (ou une impossibilité de sous-suite de densité nulle de pas pairs). Toute proposition doit fournir une inégalité précise et chercher son contre-exemple ; il ne suffit pas d'itérer la borne de Yu ou de changer les constantes.