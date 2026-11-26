# Revue ciblée de la source primaire Väänänen–Wallisser (1989)

**28 octobre 2026 — Verdict : APPLICATION PLAUSIBLE MAIS NON CERTIFIÉE.**
**Ne pas changer le statut de la PR #24 en « prouvé » sans lire l'énoncé intégral de 1989.**

La mission était précisément de vérifier les hypothèses du résultat publié aux pages **200–201**, en particulier pour le paramètre \(\alpha=2\) de la fonction de Tschakaloff. **Ces pages n'ont pas pu être consultées dans les outils accessibles.** Ce rapport conserve la séparation indispensable entre l'arithmétique démontrée et l'invocation conditionnelle d'un théorème externe.

## 1. Sources effectivement examinées

**Primaire, métadonnées et résumé seulement :**

- K. Väänänen, R. Wallisser, *Zu einem Satz von Skolem über lineare Unabhängigkeit von Werten gewisser Thetareihen*, *Manuscripta Mathematica* **65** (1989), **199–212**, DOI [10.1007/BF01168299](https://doi.org/10.1007/BF01168299), notice éditeur : https://link.springer.com/article/10.1007/BF01168299 .
- L'éditeur confirme la fonction \(f(qx)=xf(x)+1\), les arguments rationnels et l'indépendance linéaire **aussi dans le cadre p-adique**, mais affiche seulement un **résumé** avec accès payant au corps du texte. **Aucun texte de théorème ni hypothèse détaillée n'est visible**.
- Un exemplaire numérisé du volume et de l'article de **14 pages** est répertorié au [GDZ Göttingen](https://gdz.sub.uni-goettingen.de/id/PPN365956996_0065?tify=%7B%22view%22%3A%22info%22%2C%22pages%22%3A%5B201%5D%7D) ; le fichier PDF de volume et les pages de scans via API IIIF n'ont pas pu être récupérés dans cet environnement. La [notice Geodesic/EuDML](https://geodesic.mathdoc.fr/item/MM2_1989__65_3_155434/) confirme les pages 199–212 mais ne donne pas les hypothèses.
- Le texte de **1991** Väänänen–Wallisser, *A linear independence measure for certain p-adic numbers* (*J. Number Theory* 39(2), 225–236, DOI 10.1016/0022-314X(91)90045-D) est **un autre article** : son résumé suppose \(0<|q|_p<1\). Il ne doit **pas** être invoqué automatiquement pour notre \(q=3/2\), car \(|3/2|_2=2>1\).

**Secondaire, texte et code effectivement lus :**

- [muaijaz/not-an-ai-collatz-proof — rapport JSON](https://github.com/muaijaz/not-an-ai-collatz-proof/blob/main/docs/reports/pecm_tschakaloff_boundary_exclusion.json) et [implémentation](https://github.com/muaijaz/not-an-ai-collatz-proof/blob/main/collatz_exp/tschakaloff_boundary.py).
- Cette autre équipe attribue au théorème 1989, pour l'instance **différente** \((q,\alpha)=(9/4,9/2)\), un critère impliquant \(\ell=1,\sigma=0,\gamma<\Gamma(1,0)=(3-\sqrt5)/2\), avec \(\gamma=1+\log|s|_2/\log h\).
- **Cela demeure une transcription secondaire**, pas une lecture du texte original. Le script tiers vérifie les hypothèses qu'il a lui-même transcrites, et n'élimine donc pas le risque qu'une condition ait été omise ou mal interprétée.

## 2. Application arithmétique que l'on peut démontrer sans l'article

Définir dans \(\mathbb Q_2\)
\[
f_q(x)=\sum_{n\ge0}q^{-n(n+1)/2}x^n,\quad
S=\tfrac12\sum_{n\ge1}2^n(2/3)^{n(n+1)/2}.
\]
Pour \(q=3/2,\alpha=2\), on a **terme à terme**, de manière indépendante de la littérature :
\[
\boxed{f_{3/2}(2)=1+2S}.
\]
Chaque terme de \(f_{3/2}(2)\) possède valuation \(v_2=n+n(n+1)/2\), tendant vers \(+\infty\). La série est donc bien définie dans \(\mathbb Q_2\); l'équation \(f_q(qx)=1+xf_q(x)\) découle en décalant les indices.

Pour l'instance candidate de **1989** :
\[
(r,s,h,p,\ell,\sigma,\alpha)=(3,2,3,2,1,0,2).
\]

Les **conditions rapportées** suivantes passent exactement :

| Condition rapportée | Vérification exacte |
|---|---|
| \(r,s\) copremiers | \(\gcd(3,2)=1\) |
| \(q=r/s\), \(|q|_2>1\) | \(q=3/2\), \(v_2(q)=-1\), \(|q|_2=2\) |
| \(h=\max(|r|,s)\) | \(h=3\) |
| Un seul point, indice \(\ell=1\), ordre \(\sigma=0\) | Conditions entre *points distincts* vacantes |
| Point rationnel non nul | \(\alpha=2\), \(v_2(\alpha)=+1\) |
| \(\gamma<\Gamma(1,0)\) | \(\gamma=1-\log2/\log3<3/8<(3-\sqrt5)/2\) |
| Comparaison stricte sans flottants | \(2^8=256>243=3^5\), \(9^2=81>80=16\cdot5\) |

**Attention décisive :** \(\alpha=2\) a \(|\alpha|_2=1/2\), tandis que le point \(\alpha=9/2\) de l'autre équipe a \(|\alpha|_2=2\). **Il n'est pas permis de déduire** l'admissibilité de \(\alpha=2\) de l'admissibilité secondaire de \(\alpha=9/2\), avant d'avoir contrôlé toute éventuelle condition du théorème sur la valuation ou sur les points exceptionnels.

La relation de congruence [équation (14)](EVEN_DENSITY_STRUCTURAL_AUDIT.md) exige, pour un entier positif qui réaliserait indéfiniment \(w=10\,110\,1110\,11110\cdots\), \(N+1=-S\) dans \(\mathbb Q_2\). Donc :
\[
\boxed{\bigl[f_{3/2}(2)\not\in\mathbb Q\bigr]\Longrightarrow
\bigl[\text{aucun entier positif ne réalise le mot triangulaire}\bigr].}
\]
Cette **implication** est démontrée. **Sa prémisse** reste dépendante de l'instanciation à valider du théorème de 1989.

Une vérification directe complémentaire donne \(v_2(S)=1\) (premier terme de valuation 1, suivants de valuation \(\ge4\)). Donc toute hypothétique graine entière positive vérifierait \(N\equiv1\pmod4\). Cette restriction est cohérente avec les premiers représentants canoniques et **n'est pas une contradiction**.

## 3. Échec ou blocage des autres voies

1. **Irrationalité réelle.** Impossible d'inférer l'irrationalité dans \(\mathbb Q_2\) d'une propriété analogue de la limite réelle de la même série de rationnels.
2. **Troncatures ordinaires.** Une forte valuation 2-adique de l'erreur n'est pas suffisante quand le dénominateur est simultanément de l'ordre de \(3^{Q_m}\). Aucun entier non nul de taille archimédienne inférieure à \(2^{v_2}\) n'a été produit.
3. **L'équation fonctionnelle seule.** Elle donne des relations exactes entre valeurs déplacées, mais pas une preuve de non-rationalité sans contrôle indépendant de non-annulation et de hauteurs.
4. **Preuve du théorème 1989.** Non reconstruite et non formalement vérifiée. La réutilisation d'une méthode de Padé sur la base d'un résumé bibliographique serait une nouvelle preuve hypothétique, pas la vérification de la référence publiée.

## 4. Calculs réellement relancés

Dans cette mission, un contrôle Python indépendant utilisant \`fractions.Fraction\` et les entiers exacts a vérifié **14 cas** \(1\le m\le14\) de l'identité fonctionnelle tronquée, de l'identité \((f_m(2)-1)3^{Q_m}=2C_m\) et de l'unique résidu canonique de la congruence (14). Les représentants commencent par
\(r_1=1,r_2=57,r_3=121,r_4=121\).
Les deux comparaisons de seuil en entiers ont également réussi.
**Ces vérifications ne constituent pas une preuve d'irrationalité** et ne prouvent pas les hypothèses non lues du théorème publié.

## Verdict et condition de clôture

**STATUT : CONDITIONNEL / SOURCE PRIMAIRE INACCESSIBLE.**

Il serait abusif de publier maintenant « mot triangulaire exclu » sans réserve. Le résultat mathématique final deviendra établi par théorème publié seulement lorsque la totalité des conditions p-adiques de Väänänen–Wallisser (1989), pages 200–201, sera contrôlée **sur le texte original**, en particulier pour \(\alpha=2\). Si aucune condition manquante n'existe, l'application sera immédiate par \(f_{3/2}(2)=1+2S\).

Aucune nouveauté, aucun théorème Syracuse et aucune exclusion générale des mots de densité nulle ne sont revendiqués. Pas de nouveau calcul de préfixes massifs, pas de Lean, pas de fusion.
