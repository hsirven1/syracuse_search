# Pivot méthodologique après l'audit Collatz (15 octobre 2026)

**Statut : programme de recherche, pas une découverte ni une preuve de Syracuse.**

## Diagnostic vérifié

L'audit de `msharpe248/collatz` a compilé 16 modules Lean ciblés, inspecté les axiomes de 39 énoncés, puis reproduit les identités de l'expérience 36. Les congruences et les principales limites des fenêtres sont déjà présentes dans la littérature ou le dépôt Lean après traduction des horloges. Le critère de hauteur (36.3) est redondant devant la classe initiale exacte. Les mesures de complexité de l'expérience 35 ne sont pas reproductibles à partir du ZIP de 36.

Sources locales : [audit](../audit_collatz/RAPPORT.md), [comparaison](../audit_collatz/EXPERIENCE36_COMPARAISON.md), [validation](../audit_collatz/VALIDATION.md).

**Décision :** arrêter les itérations de cribles locaux sans lemme neuf ; ne pas dépenser pour un modèle supplémentaire tant que les énoncés ne sont pas définis.

## Direction candidate : horizons adaptatifs de descente

Sur les impairs positifs, soit `U(n) = (3n+1)/2^v2(3n+1)`, et

`tau(n) = min {t >= 1 : U^t(n) < n}` (`tau(n)=infini` si aucun t n'existe).

La propriété « `tau(n)` est finie pour chaque impair `n>1` » est **équivalente à Syracuse** par récurrence forte. Nous ne devons pas la présenter comme un petit lemme. Le théorème `NoGo.no_uniform_descent_bound` empêche un horizon fixé indépendamment de l'entrée ; il n'interdit pas littéralement les horizons dépendant de la hauteur, mais cette distinction ne prouve rien à elle seule.

### Contrôle adverse élémentaire

Pour tout `h>=3`, posons `n=2^h-1`. Pour `0<=t<=h-1` :

`U^t(n)=3^t * 2^(h-t)-1`.

En effet, pour `t<=h-2`,
`3 U^t(n)+1 = 2(3^(t+1)*2^(h-t-1)-1)`,
avec facteur final impair ; la valuation vaut donc exactement 1.
Pour `1<=t<=h-1`, ce terme est strictement supérieur à `n`.
**Tout horizon de descente universel doit tenir compte de ce délai croissant.**
C'est un résultat classique, pas une découverte.

`research/mersenne_check.py` est une vérification finie de cette identité pour `h=3,...,120` et cherche des contre-exemples aux bornes naïves `tau(2^h-1)<=2h` ou `<=4h` pour `h<=50`. Les exemples trouvés ne démontrent aucune borne asymptotique.

## Une seule tâche de recherche, avec point d'arrêt

Chercher une famille infinie **explicitement décrite et non triviale** `F` d'entiers impairs pour laquelle un mécanisme arithmétique (non un ajustement statistique) prouve `tau(n)<infini` avec un horizon dépendant de `h=ceil(log2(n+1))`.

1. **Avant les calculs**, dresser la liste des familles à temps d'arrêt déjà démontré (Terras/Everett, codages de parités, classes contractantes immédiates), avec sources.
2. Énoncer le candidat `F`, l'horizon et les quantificateurs. Écarter les familles triviales telles que `n=1 mod 4`, qui descendent immédiatement.
3. Chercher immédiatement des contre-exemples exacts, en incluant les entiers de Mersenne et les classes à très longue ascension.
4. Si l'énoncé survit, construire une preuve et la comparer aux résultats Lean ; alors seulement investir dans Lean 4 et une vérification par un second modèle.
5. **Arrêt** si la famille est déjà connue, si l'énoncé est réfuté ou si aucun mécanisme de preuve n'est identifié : ne pas prolonger indéfiniment l'échantillonnage.

Un succès sur une famille infinie ne résoudrait **ni les autres départs ni les cycles**. Aucune famille non triviale et nouvelle n'est encore proposée comme théorème.

## Piste alternative, séparée : cycles diophantiens

Pour un cycle accéléré de longueur `k`, somme des valuations `S` et correction affine `C`, on obtient `(2^S-3^k)n=C`. Les bornes pour cycles à plusieurs minima ont déjà été étudiées par Simons et de Weger ; tout nouveau résultat doit d'abord être comparé à cet antécédent. Cette piste reste en attente.

## Références

- T. Tao, [Almost all orbits of the Collatz map attain almost bounded values](https://doi.org/10.1017/fmp.2022.8), *Forum of Mathematics, Pi*, 2022. Énoncé sur « presque tous » les départs en densité logarithmique, pas chaque entier.
- J. Simons, B. de Weger, [Theoretical and computational bounds for m-cycles of the 3n+1-problem](https://doi.org/10.4064/aa117-1-3), *Acta Arithmetica*, 2005.
- Dépôt Lean `msharpe248/collatz`, commit audité `ec8174b567d5cab4960024782210b5f5db02bd3a`.

**Politique de résultats :** PROUVÉ / TESTÉ FINIMENT / CONDITIONNEL / DÉJÀ CONNU / NON ÉTABLI. Un nombre de tests réussi ne doit jamais être annoncé comme une preuve de Syracuse.
