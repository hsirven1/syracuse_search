## Contexte et objectif
La piste de croissance stricte KL (PR #6-#8) est abandonnée comme contribution nouvelle. Nouvelle piste distincte : **trajectoires paradoxales**, c'est-à-dire, pour l'application raccourcie T, des segments avec (3^q<2^j) mais (T^j(n)\ge n). Source publiée : O. Rozier et C. Terracol, *Paradoxical behavior in Collatz sequences*, Discrete Mathematics 349 (2026), 115167, DOI 10.1016/j.disc.2026.115167, arXiv:2502.00948. Une version HTML plus ancienne est disponible à https://www.alphaxiv.org/abs/2502.00948v3 ; **vérifier la version publiée**. Attention : le préprint Tong Niu arXiv:2605.13886 a été marqué retiré dans une source secondaire, à vérifier directement.

## Question mathématique (une seule, pas une campagne d'énumération)
Peut-on obtenir, par **couplage exact** de la correction atteignable `D(w)` et du représentant canonique positif `r(w)` d'un mot de parité `w`, une **obstruction arithmétique nouvelle** excluant une famille infinie de paramètres `(j,q)` ou de mots paradoxaux, non couverte par le majorant de la correction via le nombre `q` et les inégalités de moyenne harmonique de Rozier–Terracol ?

Pour chaque mot de longueur j à q pas impairs, le codage classique impose un unique résidu positif r(w) dans [1,2^j], et
`2^j T^j(n)=3^q n + D(w)`.
Quand `2^j>3^q`, l'existence de n>=3 réalisant w avec `T^j(n)>=n` est **équivalente** à l'existence d'un représentant congruent à r(w) modulo 2^j satisfaisant `(2^j-3^q)n <= D(w)`. Cette équivalence est classique et non nouvelle. L'objectif n'est pas de la redémontrer, mais d'exploiter un lien non trivial entre `D(w)` et `r(w)`.

## Discipline stricte
1. Lire la version publiée ou la version arXiv la plus récente ; noter explicitement théorèmes déjà prouvés, conjectures et résultats numériques.
2. Comparer `research/EXACT_STOPPING_TIME_BASELINE.md`, `research/ETUDE_37_RAPPORT.md`, `audit_collatz/RAPPORT.md`, le décodage exact `WordCongruence.lean` et les sources citées. Ne pas confondre T, Syracuse impair, et 3n+1 ordinaire.
3. **Chercher un contre-exemple avant de conjecturer.** Autoriser seulement de petits calculs rationnels/exacts avec reproduction indépendante; pas de balayage massif ni de certification Lean avant un lemme valide.
4. Accepter au maximum **un lemme précis** portant sur une famille infinie, avec quantificateurs, preuve ou état conditionnel, et comparaison d'antériorité. Un simple programme qui énumère des cas ne suffit pas.
5. Si le mécanisme est connu, si le lemme est faux, ou si aucun progrès structurel plausible n'émerge : verdict **ARRÊT**, sans recycler l'étude suivante en expérience 39.
6. Produire un rapport de cadrage et les tests réellement exécutés sur une branche, PR si possible. Ne rien merger ni revendiquer une preuve de Syracuse.

## Bibliographie minimale
- Rozier–Terracol (2026), DOI https://doi.org/10.1016/j.disc.2026.115167 ; arXiv https://arxiv.org/abs/2502.00948
- Terras (1976), Everett (1977), et contexte Lean `msharpe248/collatz`.

**Durée de la mission** : recherche initiale ciblée. Ne pas faire de gros calculs. Terminer par un verdict et une prochaine action exécutable.
