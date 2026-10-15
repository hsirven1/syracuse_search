# Étude 37 : couvertures de Syracuse et obstruction par cylindres

15 octobre 2026. **Verdict : aucune nouveauté démontrée. Un seul lemme candidat, réfuté.**

## 1. Résultats existants : des notions à ne pas confondre

| Source | Conclusion et mesure | Statut |
|---|---|---|
| Terras (1976), Everett (1977) | La première descente sous le départ survient pour presque tous les entiers, **densité naturelle 1** | Publié |
| Korec (1994) | Presque toutes les orbites atteignent une valeur inférieure à \(n^\theta\) pour chaque \(\theta>\log3/\log4\approx0,79248\), densité naturelle | Publié, cité dans Tao |
| Inselmann (2024) | Pour chaque \(\varepsilon>0\), presque toutes atteignent \(n^\varepsilon\), **densité naturelle 1** | **Préprint**, non réaudité |
| Tao (2022) | Pour toute \(f(n)\to\infty\), presque toutes atteignent \(<f(n)\), **densité logarithmique 1** | Article évalué et publié |
| Krasikov–Lagarias (2003) | Au moins \(\gg x^{0,84}\) départs \(\le x\) atteignent **1** | Publié |
| Dépôt Lean msharpe248/collatz (2026) | Annonce \(\Omega(x^{0,8676})\) de départs atteignant 1, avec certificat KL14 | **Annonce du dépôt** : les gros modules KL14 n'ont pas été recompilés dans notre audit ciblé ; son 0,895 est encore non validé formellement |

La densité 1 **n'implique jamais l'absence d'exceptions**. On ne peut pas non plus interchanger densité naturelle et logarithmique.

Sources : https://doi.org/10.4064/aa-30-3-241-252 ; https://doi.org/10.1016/0001-8708(77)90087-1 ; https://doi.org/10.1017/fmp.2022.8 ; https://arxiv.org/abs/2402.03276 ; https://github.com/msharpe248/collatz .

## 2. C37, le seul lemme candidat, est faux

On utilise l'application **raccourcie** \(T(n)=n/2\) si pair, et \(T(n)=(3n+1)/2\) si impair, et **non** le Syracuse accéléré sur les seuls impairs. Un mot de \(k\) parités correspond bijectivement à une classe modulo \(2^k\), d'après Terras.

**Candidat C37 (RÉFUTÉ) :** il existe \(c>0\) tel que, pour tout \(k\) suffisamment grand et **tout** mot de parité initial de longueur \(r=\lceil k/3\rceil\), la proportion des entiers \(n\in[2^k,2^{k+1})\) réalisant ce mot qui ne descendent pas sous \(n\) durant les \(k\) premiers pas soit au plus \(\exp(-ck)\).

**Contre-exemple :** choisir le préfixe \(r\) fois impair. Noter \(j_t\) le nombre d'impairs parmi les \(t\) premiers pas. L'inégalité élémentaire \(T^t(n)\ge n3^{j_t}/2^t\) garantit la non-descente dès que \(3^{j_t}>2^t\) à tous les instants \(1\le t\le k\).

Grâce à la bijection entre parités et classes binaires, les \(k-r\) bits du suffixe sont uniformes parmi les \(2^{k-r}\) réalisations dans la tranche dyadique. Après \(s\) bits, le nombre d'impairs \(X_s\) a une loi binomiale \(\mathrm{Bin}(s,1/2)\). Noter
\[
p=\log_3 2\approx0,63092975357,\qquad \theta_c=2p-1\approx0,26185950714.
\]
Il suffit que \(r+X_s>p(r+s)\) pour chaque \(0\le s\le k-r\).
Pour \(r=\lceil\theta k\rceil\), avec \(\theta>\theta_c\), l'écart entre l'espérance et ce seuil est au moins \(k\delta\), où \(\delta=(1+\theta)/2-p>0\). L'inégalité de Hoeffding et l'union sur les \(k\) instants bornent la proportion **non garantie** par
\[
k\exp(-2\delta^2k/(1-\theta))\to0.
\]
À \(\theta=1/3\), **la proportion de non-descendeurs tend vers 1 dans le cylindre tout impair**. C37 prétendait le contraire.

### De l'autre côté du seuil : corollaire classique

Dans notre audit Lean, le lemme terras_growth_bound donne, pour \(n\ge2^k\), que ne pas être descendu au temps \(k\) impose \(2^{k-1}<3^{j_k}\), donc \(j_k>p(k-1)\). Fixer tout préfixe de longueur \(r\le(\theta_c-\varepsilon)k\) laisse un suffixe binomial dont le nombre d'impairs doit dépasser sa moyenne d'au moins \(\varepsilon k/2-p\). Pour \(k\ge4p/\varepsilon\), Hoeffding donne une proportion au plus \(\exp(-\varepsilon^2k/8)\), **uniformément** sur les préfixes.

Ainsi la frontière \(\theta_c\) est un effet déjà impliqué par le codage classique et les inégalités binomiales. Aucune découverte revendiquée.

## 3. Tests réellement exécutés

Le programme research/etude37_conditional_cover.py calcule **exactement** le nombre de mots suffixes dont les puissances satisfont \(3^{j_t}>2^t\) à **chaque pas**. Il a été exécuté pour \(k=30,60,100,200,400\) et les ratios cibles 0,20 ; 0,27 ; 1/3 ; 0,40.

Pour \(r=\lceil k/3\rceil\) :

| k | r | Fraction de non-descente garantie |
|---:|---:|---:|
| 30 | 10 | 0,621936798096 |
| 60 | 20 | 0,709839336345 |
| 100 | 34 | 0,789502175862 |
| 200 | 67 | 0,877598664703 |
| 400 | 134 | 0,957999974837 |

**Second contrôle indépendant**, par simulation directe des entiers de la tranche dyadique et reconstruction de tous les suffixes :

| k | r | Nombre de départs | Non-descendus réels | Garantis par DP |
|---:|---:|---:|---:|---:|
| 10 | 4 | 64 | 38 | 38 |
| 14 | 5 | 512 | 308 | 308 |
| 18 | 6 | 4096 | 2224 | 2224 |

Toutes les assertions sont passées. Le programme a passé la compilation syntaxique Python. **Aucune nouvelle compilation Lean n'a été faite** : les théorèmes utilisés proviennent de l'audit précédent. La conclusion pour tous les \(k\) repose sur les inégalités et non sur ces tests finis.

## 4. Comparaison avec notre dépôt et verdict

Notre audit Collatz a déjà vérifié la bijection parité/résidu, la loi binomiale et les limites des certificats de fenêtre fixe (audit_collatz/RAPPORT.md). Notre recherche sur les temps de descente exacts (research/EXACT_STOPPING_TIME_BASELINE.md) montre déjà comment fabriquer une infinité de trajectoires réalisant un certificat fini. C37 est une tentative plus exigeante de contrôler chaque classe, mais elle échoue devant une concentration **conditionnelle**.

**Aucun lemme potentiellement nouveau n'a survécu.** Il n'est pas utile de continuer les études de couverture conditionnelle avec les mêmes ingrédients.

Suite possible à valeur limitée : **auditer séparément le gros certificat Lean KL14** annoncé par le dépôt externe (énoncé, axiomes et reproduction des preuves), mais son auteur annonce jusqu'à ~29 heures et 37 Go pour la compilation. Ce serait un travail de validation formelle, pas une résolution de Syracuse. Commencer par la revue statique ; ne pas dépenser de ressources lourdes sans nouveau besoin.
