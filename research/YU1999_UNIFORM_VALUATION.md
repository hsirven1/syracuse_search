# Yu (1999) clôt la borne uniforme (V) : gain log-log conditionnel seulement à la divergence

**28 octobre 2026 — Résultat démontré par spécialisation d'un théorème publié, non original.**

Cette note complète [PADIC_SUCCESSIVE_RUNS.md](PADIC_SUCCESSIVE_RUNS.md), commit \`e28978447a0ddc1c8c404515cea505fe56ff6b21\`. Le rapport précédent traitait comme hypothèse non certifiée :

\[
(V)\qquad \exists C\ge1\;\forall r\ge1\;\forall a\ge1\text{ impair},\quad
v_2(3^r a+1)\le C(1+\log_2a)\log_2(2+r).
\]

**Nous pouvons décharger (V) à partir d'une source publiée antérieure et plus directement accessible : K. Yu (1999), pas nécessairement Yu (2007).** La preuve de Yu n'est pas reconstruite ni formalisée ici ; le raisonnement qui suit est une **application** de sa majoration publiée.

## 1. Source, formulation et vérification

Kunrui Yu, *p-adic logarithmic forms and group varieties II*, \`Acta Arithmetica\` **89** (1999), 337–378. DOI [10.4064/aa-89-4-337-378](https://doi.org/10.4064/aa-89-4-337-378).

- [Notice officielle de l'éditeur IMPAN](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/89/4/110761/p-adic-logarithmic-forms-and-group-varieties-ii).
- [Transcription HTML intégrale de l'article](https://paperzz.com/doc/7955773/p-adic-logarithmic-forms-and-group-varieties-ii), pages imprimées **337–339** pour l'énoncé.
- [PDF historique indexé par la Biblioteka Nauki](https://bibliotekanauki.pl/articles/1390501.pdf), [autre copie PDF indexée](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8944.pdf). **Limite de source :** les serveurs de ces PDF ont rejeté leur ouverture via le navigateur de recherche ; les formules ci-dessous ont été vérifiées à partir de la transcription HTML de l'article et de son extrait PDF indexé, non sur un fac-similé de page inspectable. Une vérification typographique du PDF reste utile, mais ce n'est pas un résultat supposé seulement à partir d'un résumé.

### Conséquence énoncée au début de l'article, p. 337

Fixer le corps de nombres \(K\) de degré \(d\), une place première \(\mathfrak p\mid p\), les paramètres \(e_{\mathfrak p}, f_{\mathfrak p}\) et \(n\) bases \(\alpha_1,\dots,\alpha_n\) non nulles. Si
- \(p=2\) implique \(\zeta_3\in K\) (condition **(1.2)** ; pour les autres \(p\), conditions différentes) ;
- \(\operatorname{ord}_{\mathfrak p}(\alpha_j)=0\) pour chaque \(j\) (condition **(1.9)**) ;
- \(b_j\in\mathbb Z\), \(\Xi=\prod_j\alpha_j^{b_j}-1\ne0\) ;
- \(B\ge\max(3,|b_1|,\dots,|b_n|)\) (condition **(1.8)**),

Yu donne explicitement, **en conséquence du théorème 1**, une constante \(A=A(n,d,p,e_{\mathfrak p},f_{\mathfrak p})>0\) telle que
\[
\operatorname{ord}_{\mathfrak p}(\Xi)
 < A\,\prod_{j=1}^n
 \max\bigl(h_{\mathrm{Weil}}(\alpha_j),\,\log p\bigr)\,\log B. \tag{Y}
\]
Son premier paragraphe fournit même un **facteur numérique explicite** en ces invariants (dont \(19\), la puissance \(2(n+1)\) et \(p^{f_{\mathfrak p}}/(f_{\mathfrak p}\log p)^2\)). Seule la dépendance de la constante est nécessaire ici, et ses paramètres restent tous fixés.

L'expression \`h_j=max(h_0(alpha_j),log p)\` figure textuellement dans cette conséquence p. 337. **Il faut utiliser cette version**, et non remplacer sans justification les hauteurs par \(\log a\), qui devient zéro pour \(a=1\). Le théorème 1 proprement dit utilise les hauteurs **modifiées** \(h'_j=\max\{h_0(\alpha_j),f_{\mathfrak p}\log p/d\}\) de la formule (1.5), où \(h_0\) est la hauteur absolue de Weil. Dans notre champ \(f_{\mathfrak p}/d=2/2=1\), donc \(h'_j=\max\{h_0(\alpha_j),\log 2\}\), exactement les hauteurs \(h_j\) figurant dans la conséquence (Y) ; il ne demande **pas** que \(\alpha_1,\alpha_2\) soient multiplicativement indépendants. La réduction à ce cas intervient dans la **preuve** (§14), pas dans son énoncé.

## 2. Specialisation UNIFORME en a

Choisir le champ **fixe**
\[
K=\mathbb Q(\zeta_3)=\mathbb Q(\sqrt{-3}),\quad
\zeta_3^2+\zeta_3+1=0.
\]
Le polynôme \(X^2+X+1\) est irréductible modulo 2, donc \(2\) est **inerte et non ramifié** dans \(K\). Il y a une unique place \(\mathfrak p\mid2\), avec \(d=2\), \(e_{\mathfrak p}=1\), \(f_{\mathfrak p}=2\). La condition (1.2) est satisfaite par construction.

Pour tout \(r\ge1\) et tout impair \(a\ge1\), prendre **toujours deux bases, mais la seconde dépend de a**
\[
n=2,\quad \alpha_1=3,\quad \alpha_2=-a,\quad
(b_1,b_2)=(r,1),\quad B=\max(3,r).
\]
Alors
\[
\Xi=3^r(-a)^1-1=-(3^r a+1)\ne0.
\]
Ces bases (dont \(\alpha_2=-a\) varie avec \(a\)) sont toutes deux des unités \(\mathfrak p\)-adiques puisque \(3\) et \(a\) sont impairs : \(\operatorname{ord}_{\mathfrak p}\alpha_j=0\). Et pour un entier rationnel, \(\operatorname{ord}_{\mathfrak p}(\Xi)=v_2(\Xi)\), puisque \(e_{\mathfrak p}=1\).

Leurs hauteurs absolues de Weil sont
\[
h_{\mathrm{Weil}}(3)=\log3,\qquad
h_{\mathrm{Weil}}(-a)=\log a\quad(a\ge1).
\]
Par (Y),
\[
v_2(3^r a+1)
 < A\,(\log3)\max(\log a,\log2)\log\max(3,r).
\]
Or
\[
\max(\log a,\log2)\le(\log2)(1+\log_2 a),\qquad
\log\max(3,r)\le(\log2)\log_2(2+r).
\]
Il suffit donc de poser
\[
\boxed{C=\max\{1,A(\log3)(\log2)^2\}}
\]
pour obtenir **sans hypothèse supplémentaire**
\[
\boxed{\forall r\ge1,\;\forall a\ge1\text{ impair},\quad
v_2(3^r a+1)\le C(1+\log_2a)\log_2(2+r).}\tag{V}
\]
La même constante marche pour **tous** les impairs \(a\), y compris \(a=1\) et les puissances de 3. Aucun groupe complet de \(S\)-unités variable n'est introduit ; les **deux bases et le champ restent fixes**. Les hypothèses d'indépendance multiplicative ne sont **pas** requises dans (Y).

**Ce qui est publié et ce qui est prouvé ici :** le majorant (Y) est le résultat antérieur de Yu. La substitution des paramètres, le contrôle de la place au-dessus de 2 et la transformation des hauteurs en (V) sont démontrés dans cette note. Aucun argument du cas divergent de Syracuse n'entre dans la preuve de (V).

## 2 bis. Contrôle contradictoire reçu et clarification des hypothèses

Le relecteur indépendant conclut **CONDITIONNEL**, sans trouver d'erreur arithmétique ni d'erreur dans la preuve à deux runs, parce qu'il n'a pas eu accès au PDF original. Une relecture effectuée ensuite a identifié la **transcription de l'article original** [Yu 1999, pp. 337–339](https://paperzz.com/doc/7955773/p-adic-logarithmic-forms-and-group-varieties-ii), ainsi que le **texte indexé du PDF original** [IM PAN / ICM](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8944.pdf). Les passages effectivement lisibles confirment expressément :
- le corollaire en tête de la p. 337, sous la forme (Y) avec \(h_j=\max(h_0(\alpha_j),\log p)\), où \(h_0\) est la hauteur de Weil ; pour notre champ, ces hauteurs sont les mêmes que les hauteurs modifiées (1.5) ;
- (1.2) : \(\zeta_3\in K\) si \(p=2\) ; (1.8) : \(B\ge\max(3,|b_1|,\ldots,|b_n|)\) ; (1.9) : \(\mathrm{ord}_{\mathfrak p}\alpha_j=0\) ;
- l'indépendance multiplicative **n'est pas imposée** dans cet énoncé ; la condition supplémentaire (1.11) ne donne qu'une **amélioration facultative** de la constante.

La formule précise (Y) et ces conditions sont donc corroborées directement par le **texte original transcrit**, et non seulement par un programme secondaire. **Limite documentaire restante : les fac-similés PDF ne s'ouvrent pas** dans les outils actuels ; la typographie exacte des constantes n'a pas été inspectée en image. Le verdict éditorial indépendant reste **CONDITIONNEL** jusqu'à cette ultime comparaison ; ce n'est pas une réfutation.

**Cas de dépendance multiplicative, éliminé même sans (1.11).** Si \(a\) n'est pas une puissance de \(3\), \((3,-a)\) sont multiplicativement indépendants, par valuation en un premier distinct de \(3\) divisant \(a\). Si \(a=3^k\), \(k\ge0\), alors \(3^r a+1=3^{r+k}+1\), et \(v_2(3^{r+k}+1)\le2\). On peut donc choisir \(C\ge2\) et éviter toute dépendance sur une condition éventuelle d'indépendance.

**Normalisation de la valuation :** le nombre \(3^r a+1\) est rationnel ; la place au-dessus de \(2\) est non ramifiée dans \(\mathbb Q(\zeta_3)\), donc \(\mathrm{ord}_{\mathfrak p}(3^ra+1)=v_2(3^ra+1)\), sans facteur \(f_{\mathfrak p}\) supplémentaire.

**Aucun changement de portée :** l'uniformité de la constante \(C\) sous (Y) est établie ; la conséquence log-log sur les orbites reste conditionnelle à une hypothétique orbite non bornée, et n'améliore ni la pente principale ni la conjecture de Syracuse.

## 3. Conséquence sur la complexité : retirer une hypothèse du rapport précédent

Le §5 du [rapport précédent](PADIC_SUCCESSIVE_RUNS.md) établit soigneusement l'implication
\[
(V)\Longrightarrow
p_N(L)\ge\frac{L}{\beta}
+\frac{\delta}{\beta\lambda}\log_2L
+d\log_2\log_2L-O_N(1),\tag{P}
\]
sur toute orbite positive **hypothétiquement non bornée**, où
\[
\delta=\log_2 3,\quad \beta=\delta-1=\log_2(3/2),
\quad \lambda=\log_2\delta,\quad
d=\frac1{16C\lambda^2}>0.
\]
Le coefficient \(d\) est extrêmement faible si l'on utilise les constantes générales gigantesques de Yu, mais il est **strictement positif et universel**.

### Contrôle des étapes critiques de cette implication

- À l'issue de chaque run impair, \(M_i+1=2^{r_i}a_i\) et \(r_{i+1}+1=v_2(3^{r_i}a_i+1)\), y compris la branche \(r_i=0\).
- Avec \(x_i=\log_2(M_i+1)\), \(b_i=\log_2a_i=x_i-r_i\) et \(L_i=\log_2(2+x_i)\), on a \(x_{i+1}\le\delta x_i-\beta b_i\), et (V) donne \(r_{i+1}\le C(1+b_i)L_i\).
- Pour \(i\) assez grand et une orbite injective non bornée, \(CL_i\le x_i/4\). La séparation \(b_i\ge x_i/(4CL_i)\) ou non donne dans les deux cas
  \(x_{i+2}\le\delta^2x_i(1-a_0/L_i)\) avec \(a_0=\beta/(4C\delta)>0\).
- La somme harmonique le long des indices de même parité donne
  \(x_i\le A_N\delta^i/(i+1)^\kappa\), \(\kappa=\beta/(16C\delta\lambda)>0\).
- Les longueurs successives donnent \(E(t)\ge\log_2t/\lambda +(\kappa/\lambda)\log_2\log_2t-O_N(1)\).
- L'identité exacte des hauteurs et le contrôle \(R(t)=O_N(1)\), issu de la sommabilité des inverses pour une orbite non bornée, fournissent le majorant de hauteur. L'absence de répétition et la bijection parité–classe modulo \(2^L\) donnent enfin (P).

**Important :** il reste dans (P) **l'hypothèse d'une orbite non bornée**, dont on ne connaît pas l'existence. (V), lui, est inconditionnel. Ce résultat ne démontre ni une proportion inférieure strictement positive de pas pairs ni une nouvelle pente asymptotique. Il ne remet pas en cause la conjecture de Syracuse.

## 4. Obstacle préservé, sans contradiction avec Yu

Le contre-exemple exact du rapport précédent reste valide : pour \(a=5\), la valuation \(v_2(3^r a+1)\) est arbitrairement grande lorsque \(r\) varie. Cela réfute **une borne indépendante de r**, mais reste compatible avec (V), dont le membre droit croît en \(\log r\).

## 5. Statuts de preuve, limites et reproductibilité

- **THÉORÈME PUBLIÉ UTILISÉ :** conséquence initiale du théorème 1, Yu 1999, p.337, avec conditions explicites (1.2), (1.8), (1.9).
- **DÉMONSTRATION DE SPÉCIALISATION :** (V), en changeant seulement les deux bases \((3,-a)\), avec corps et constante **fixes**.
- **THÉORÈME CONDITIONNEL SUR LES ORBITES :** (P), dorénavant sans la précédente condition non vérifiée (V), mais toujours sous l'hypothèse d'orbite non bornée.
- **NON ÉTABLI :** \(\liminf E(t)/t>0\), une amélioration de la pente \(1/\beta\), un résultat inédit au sens de priorité scientifique, une preuve de Syracuse.
- **RÉSERVE DOCUMENTAIRE :** le résultat de 1999 a été lu dans une transcription HTML du texte original, confirmée par les extraits indexés du PDF, **sans visualisation directe des équations sur les pages PDF** (accès web refusé). Une relecture du fac-similé serait souhaitable pour une certification éditoriale. La dépendance au résultat publié de Yu est explicite, pas une preuve autonome de sa théorie.
- **VALIDATION NUMÉRIQUE :** aucune nouvelle recherche ni simulation n'est nécessaire pour cette implication universelle. Les scripts de la branche parente ne prouvent pas (V) ; aucune compilation Lean n'est revendiquée.

**Verdict : GO pour audit mathématique indépendant de la spécialisation publiée ; maintien du gel de toute revendication de nouveauté.**

**Prochaine action unique :** demander à un second relecteur mathématicien de contrôler sur le fac-similé de Yu 1999 la formule explicite p.337 et les trois conditions (1.2), (1.8), (1.9), puis les deux cas de la récurrence à deux runs dans §5 du rapport parental. Aucun nouveau calcul de préfixes ni nouvelle étude de densité n'est nécessaire avant cette vérification.