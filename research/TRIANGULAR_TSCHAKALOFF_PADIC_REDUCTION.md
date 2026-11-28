# Mot triangulaire : réduction à une valeur 2-adique de Tschakaloff et théorème de Väänänen–Wallisser

**28 octobre 2026. Verdict : conditionnel à l'applicabilité exacte d'un théorème publié de 1989 ; application arithmétique vérifiée, TEXTE INTÉGRAL DU THÉORÈME 1989 NON RELU directement dans cette mission.** Aucun résultat scientifique original revendiqué. Cette note **ne prouve pas Syracuse**.

Parent : [PR #23](https://github.com/hsirven1/syracuse_search/pull/23), \`research/TRIANGULAR_PARITY_WORD_AUDIT.md\`, et équation (14) de \`research/EVEN_DENSITY_STRUCTURAL_AUDIT.md\`.

## 1. L'identification exacte, sans approximation

Soit le mot de parité **raccourci** \(w=10\,110\,1110\,11110\cdots\).
Le rapport antérieur a démontré que sa réalisation éventuelle par un entier \(N\ge1\) imposerait dans \(\mathbb Q_2\)
\[
N+1=-S,\qquad
S=\frac12\sum_{n=1}^\infty 2^n(2/3)^{n(n+1)/2}.
\]

Pour \(q\in\mathbb Q^\times\) et \(x\in\mathbb Q\), écrire
\[
f_q(x):=\sum_{n=0}^\infty q^{-n(n+1)/2}x^n.
\]
Cette série converge dans \(\mathbb Q_2\) lorsque \(v_2(q)<0\) et \(x\in\mathbb Q\) est fixé, car sa valuation de terme est
\(-v_2(q)\,n(n+1)/2+n\,v_2(x)\to+\infty\).

**Identité terme à terme dans \(\mathbb Q_2\) :**
\[
\boxed{2S+1=f_{3/2}(2).} \tag{A}
\]
En effet, \((3/2)^{-Q_n}2^n=2^n(2/3)^{Q_n}\), avec \(Q_n=n(n+1)/2\). Il n'y a aucune manipulation d'ordre de convergence et aucun appel à une valeur réelle.

La fonction satisfait exactement
\[
f_q(qx)=xf_q(x)+1. \tag{B}
\]
Preuve : en multipliant le terme d'indice \(n\) par \(q^n\), on décale la somme pour retrouver \(x f_q(x)\), avec le terme \(n=0\) égal à \(1\). Cette équation **est celle de l'article historique** ci-dessous.

**Conséquence logique.** Si \(f_{3/2}(2)\notin\mathbb Q\) comme élément de \(\mathbb Q_2\), alors \(S\notin\mathbb Q\), puisque \(f=2S+1\); aucune égalité \(N+1=-S\) avec \(N\in\mathbb Z_{\ge1}\) n'est possible. Tous les préfixes finis du mot restent réalisables ; seule la réalisation *infinie* est exclue. C'est un cas particulier, pas la conjecture de Syracuse.

## 2. Antériorité primaire pertinente : Väänänen–Wallisser, 1989

**Source bibliographique vérifiée chez l'éditeur :**

K. Väänänen et R. Wallisser, *Zu einem Satz von Skolem über lineare Unabhängigkeit von Werten gewisser Thetareihen*, \`Manuscripta Mathematica\` **65** (1989), 199–212, DOI [10.1007/BF01168299](https://doi.org/10.1007/BF01168299).

[Résumé officiel Springer](https://link.springer.com/article/10.1007/BF01168299) : l'article étudie la fonction résolvant \(f(qx)=xf(x)+1\) et obtient des mesures de **linéarité indépendante des valeurs**, dans le cas **archimédien ET p-adique**.

**Limite d'accès matérielle.** Le texte intégral des théorèmes pp. 200–201 est sous accès restreint chez Springer et le PDF numérisé [Göttingen GDZ](https://gdz.sub.uni-goettingen.de/download/pdf/PPN365956996_0065/PPN365956996_0065.pdf) n'a pas pu être relu directement dans cet environnement. Son existence et sa référence ont été corroborées. Il est donc **interdit de qualifier cette mission de vérification primaire indépendante de tous les quantificateurs de l'article**.

Une autre équipe travaillant *indépendamment* sur Collatz a consigné une application de ce même théorème 2-adique à la valeur \(f_{9/4}(9/2)\), avec les paramètres, seuil et limites dans :
- [rapport de certification \`pecm_tschakaloff_boundary_exclusion.json\`](https://github.com/muaijaz/not-an-ai-collatz-proof/blob/main/docs/reports/pecm_tschakaloff_boundary_exclusion.json) ;
- [code d'instanciation \`tschakaloff_boundary.py\`](https://github.com/muaijaz/not-an-ai-collatz-proof/blob/main/collatz_exp/tschakaloff_boundary.py) ;
- [récit scientifique §19.6](https://github.com/muaijaz/not-an-ai-collatz-proof/blob/main/docs/PROJECT_JOURNEY.md).

Ces pièces **ne sont pas une autre édition de l'article de 1989**. Elles rapportent un critère de Väänänen–Wallisser à \(\ell=1,\sigma=0\) de forme :
\[
\gamma=1+\frac{\log|s|_p}{\log h} <
\Gamma(1,0)=\frac{3-\sqrt5}{2},\quad
q=r/s,\ h=\max(|r|,s),\ |q|_p>1,
\]
avec \(r,s\) premiers entre eux, \(p\) premier, et \(\alpha\in\mathbb Q^\times\) non nul. Pour un seul point, les exclusions entre rapports de points sont vides. **Selon cette transcription secondaire**, la conclusion est l'indépendance sur \(\mathbb Q\) de \(1=f_q(0)\) et \(f_q(\alpha)\) à l'intérieur de \(\mathbb Q_p\).

### Paramètres EXACTS de notre série

\[
(r,s,h,p,\ell,\sigma,\alpha)=(3,2,3,2,1,0,2).
\]
Contrôles :
- \(r=3,s=2\) premiers entre eux, \(h=3\), \(q=3/2\) ;
- \(v_2(q)=-1\), donc \(|q|_2=2>1\);
- \(\alpha=2\neq0\), \(\ell=1\), \(\sigma=0\), et les rapports entre points sont sans objet;
- \(\gamma=1+\log(1/2)/\log3=1-\log2/\log3\);
- **sans flottants** : \(2^8=256>3^5=243\) implique \(\gamma<3/8\); et \(3/8<(3-\sqrt5)/2\), car \(9^2=81>16\cdot5=80\).
Ainsi \(\gamma<\Gamma(1,0)\) **strictement** et exactement.

**Conclusion CONDITIONNELLE au texte complet de la source primaire :** si le théorème s'énonce et s'applique à \(q=3/2,\alpha=2\) exactement comme le décrit le dossier secondaire de 2026, il fournit
\[
f_{3/2}(2)\notin\mathbb Q\subset\mathbb Q_2,
\]
donc par (A) **aucun entier positif ne réalise le mot triangulaire**. L'article publié fournit alors tout le mécanisme irrationnel ; l'apport de notre projet est uniquement l'application, **aucune découverte mathématique de priorité établie**.

> **Obligation principale restant à décharger** : consulter l'énoncé primaire intégral (p. 200–201), et vérifier toutes ses hypothèses, notamment l'absence de restriction supplémentaire sur \(\alpha=2\), sur \(v_2(\alpha)\) et sur les points d'évaluation. Les paramètres (3,2) diffèrent de ceux de l'autre équipe (9,4). La vérification secondaire de (9,4) ne garantit pas automatiquement le cas (3,2).

## 3. Trois fausses preuves activement écartées

### 3.1 Irrationalité réelle \(\not\Rightarrow\) irrationalité 2-adique

[Krattenthaler–Rochev–Väänänen–Zudilin, *Acta Arithmetica* 136 (2009), théorème 2](https://arxiv.org/pdf/0812.2921) couvre **dans \(\mathbb R\)** \(f_{3/2}(2)\). Leur \(\gamma_{\infty}=\log 3/\log2\approx1.58496\) dépasse le seuil publié \(1.53237645\) pour \(\lambda=0\) (par exemple \(3^{13}>2^{20}\) montre \(\gamma_\infty>20/13>1.53237645\)). Donc la **somme réelle** \(f_{3/2}(2)\) est irrationnelle.

Cette conclusion **ne prouve rien** pour la somme 2-adique du **même** développement rationnel : les deux séries peuvent converger à des rationnels distincts dans les deux corps. La preuve 2009 n'a pas été transférée illicitement.

### 3.2 Un critère classique de rationalité ne passe pas les constantes

Les troncatures 2-adiques \(F_m=\sum_{n=0}^m 2^n(2/3)^{Q_n}\) satisfont :
\[
v_2(f_{3/2}(2)-F_m)
=Q_{m+1}+m+1
\]
(la première valeur omise, car ses valuations sont strictement croissantes).
Leur dénominateur réduit est \(3^{Q_m}\) (les autres termes sont entiers sur ce dénominateur), et leurs numérateurs croissent dans la norme usuelle au moins exponentiellement en \(Q_m\).

Pour la forme linéaire entière \(3^{Q_m}f_{3/2}(2)-3^{Q_m}F_m\), la valuation 2-adique est \(Q_{m+1}+m+1\), tandis que l'échelle de hauteur est de l'ordre de \(3^{Q_m}\). Le rapport asymptotique
\[
\frac{v_2(\text{erreur})}{\log_2\big(3^{Q_m}\big)}
\longrightarrow\frac1{\log_2 3}=0.63093\ldots<1.
\]
Il n'est donc **pas possible** d'utiliser la contradiction « entier non nul avec valeur absolue usuelle plus petite que \(2^{v_2}\) » à partir de ces *seules* troncatures. Cela **ne réfute pas** la possibilité d'approximants de Padé ou de Hankel plus puissants.

### 3.3 Équation fonctionnelle sans contrôle des dénominateurs

L'identité \(f(qx)=xf(x)+1\) est vraie, mais les valeurs \(f(q^k x)\) qui en découlent ne donnent pas à elles seules une suite d'entiers impossiblement divisibles. Le passage de rationalité supposée à une contradiction dépend de bornes globales de hauteur et de non-annulation, précisément du type étudié en 1989.

## 4. Tests reproductibles et limites

Le fichier \`research/triangular_tschakaloff_checks.py\` contrôle par entiers et \`fractions.Fraction\` :
- \(\gcd(r,s)=1\), les paramètres \(q,\alpha\), les valuations et les deux témoins d'inégalités exacts;
- l'identité **terme à terme** \(2S+1=f_q(\alpha)\);
- l'équation fonctionnelle \(f(qx)=xf(x)+1\) sur les troncatures avec indices alignés;
- la correspondance avec (14) pour de très petits \(m\), **sans prolongation de recherches de préfixes**;
- le décalage d'une troncature et la valuation 2-adique de son reste.

**Ces tests n'exécutent pas le théorème de Väänänen–Wallisser** et ne le remplacent pas. La preuve conditionnelle dépend de l'article complet. Aucune compilation Lean, aucun calcul massif, aucune conjecture de Syracuse résolue.

## Verdict scientifique

1. **PROUVÉ indépendamment dans cette note :** l'identification exacte (A), l'équation (B), l'inégalité numérique de seuil, et l'implication logique « irrationalité 2-adique de \(f_{3/2}(2)\) \(\Rightarrow\) non-réalisation du mot ».
2. **RÉSULTAT PUBLIÉ, INSTANTIATION EN ATTENTE DE CONTRÔLE PRIMAIRE :** le théorème p-adique de Väänänen–Wallisser (1989), appliqué avec \(q=3/2,\,\alpha=2\). Une équipe externe l'a utilisé avec \(q=9/4,\,\alpha=9/2\), ce qui renforce la plausibilité de la bonne transcription sans suffire à la valider ici.
3. **PAS ÉTABLI par cette mission :** une preuve indépendante de l'irrationalité 2-adique, une nouvelle priorité scientifique, une exclusion de tous les mots à densité nulle de pairs, ou la conjecture de Syracuse.

**Prochaine action mathématique unique :** audit exact du théorème publié pp. 200–201 avec la spécialisation \((3,2,3,2,1,0,2)\). Si l'énoncé correspond, le sous-problème triangulaire est **résolu par application d'un théorème existant** ; il ne faut pas relancer des préfixes ni une tentative de preuve de cette même valeur.