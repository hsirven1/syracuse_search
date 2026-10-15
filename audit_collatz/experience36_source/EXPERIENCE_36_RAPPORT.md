# Expérience 36 : congruences duales et limites de la complexité symbolique

**Date : 14 octobre 2026.** **Verdict :** aucune preuve nouvelle de la conjecture de Syracuse. Cette expérience confirme une obstruction générale à notre projet de renforcer la complexité symbolique par un filtre modulo `3^k` sans information de taille supplémentaire. Les preuves élémentaires ci-dessous sont autonomes ; les tests sont reproductibles ; les antériorités citées ne sont pas auditées mathématiquement dans leur intégralité.

## 1. Périmètre et bilan

Après les expériences 32–35, une famille de mots de valuations d'entiers 2-adiques demeure compatible avec des déficits logarithmiques, une variation rapide et une grande complexité locale. L'objectif était de vérifier si les restes modulo des puissances de 3 pouvaient imposer une contrainte indépendante.

**Résultat négatif démontré :** pour l'orbite impaire accélérée, le reste modulo `3^k` de l'état à la date `t >= k` est entièrement codé par les `k` dernières valuations. Une condition modulaire qui répète cette identité ne retranche donc aucun mot fini admissible.

**Résultat fini supplémentaire :** associer à cette congruence un plafond archimédien sur les états donne une borne inférieure explicite sur le départ. Elle n'améliore pas la contrainte de réalisation 2-adique sur notre construction expérimentale.

## 2. Lemme : la mémoire 3-adique est à retard fini

Pour des entiers positifs impairs, soit

\[
U(n)=(3n+1)/2^{v_2(3n+1)},\quad
n_t=U^t(n_0),\quad a_t=v_2(3n_{t-1}+1).
\]

**Proposition.** Pour chaque `1 <= k <= t`, en interprétant toutes les puissances négatives de 2 comme des inverses modulo `3^k`,

\[
\boxed{n_t\equiv\sum_{j=0}^{k-1}3^j\cdot
2^{-(a_t+\ldots +a_{t-j})}\pmod{3^k}.}
\tag{36.1}
\]

*Preuve.* Dans l'anneau `Z/(3^k)Z`, `2` est inversible et `n_t=2^{-a_t}(3n_{t-1}+1)`. Substituer cette égalité dans elle-même `k` fois donne exactement les `k` termes de (36.1), plus un multiple de `3^k` fois `n_{t-k}`, qui vaut zéro modulo `3^k`. Il n'y a aucune hypothèse statistique. `□`

Pour `k=1`, `n_t ≡ (-1)^{a_t} (mod 3)`. Pour `k=2`, `n_t ≡ 2^{-a_t} + 3·2^{-(a_t+a_{t-1})} (mod 9)`. Il ne faut pas remplacer cette congruence par une égalité ordinaire d'entiers.

## 3. Lemme : tout mot fini de valuations positives est réalisable

Soit `a_1,...,a_N` une suite quelconque d'entiers `>=1`, `S_i=sum_{h<=i} a_h`, `S_0=0`, et

\[
C_0=0,\quad C_i=3C_{i-1}+2^{S_{i-1}}.
\]

L'identité affine est `2^{S_i} n_i=3^i n_0+C_i`. La condition d'imparité finale équivaut à

\[
\boxed{3^N n_0+C_N\equiv2^{S_N}\pmod{2^{S_N+1}}.}\tag{36.2}
\]

Parce que `3^N` est inversible modulo `2^{S_N+1}`, cette congruence définit une **unique classe impaire** `r` modulo `2^{S_N+1}`. Elle suffit pour toutes les valuations prescrites : en remontant les sommes `C_N`, les termes d'indice >= `i` ont un coefficient `2^{S_i}`, le premier tel coefficient étant impair et les suivants pairs ; la divisibilité de (36.2) entraîne, pour chaque `i`, `3^i n_0+C_i ≡2^{S_i} (mod 2^{S_i+1})`. Chaque état intermédiaire est donc impair, et la récurrence donne exactement les valuations souhaitées.

Il existe ainsi **une infinité d'entiers positifs impairs** dans la classe `r`, arbitrairement grands, réalisant le même préfixe. On peut en choisir aussi une infinité non divisibles par 3, car le module est premier à 3.

**Conséquence cruciale.** Un test de congruences modulo `3^k` qui n'utilise que les valuations locales ne peut éliminer *aucun* mot fini positif : chaque réalisation positive vérifie automatiquement (36.1). Pour espérer exclure une trajectoire infinie issue d'un entier *fixé*, il faut une information qui ne soit pas simplement une reformulation de ses valuations : par exemple une borne archimédienne uniforme indépendante du nombre de bits requis par le préfixe, ou une contrainte à plusieurs échelles prouvée pour tous les temps.

### Application aux préfixes critiques

Posons `F_i=floor(i log_2 3)` et prenons `a_i=F_i-F_{i-1}∈{1,2}`. Alors `S_i=F_i`, donc `3^i/2^{S_i}>1` et l'identité affine donne `U^i(n_0)>n_0` pour **tout** départ positif réalisant ce préfixe et `i>=1`. Cette construction existe pour chaque longueur finie et pour des départs aussi grands que souhaité. Elle exclut toute preuve fondée sur une condition locale universelle de descente de longueur bornée, sans contrôle de la taille initiale.

## 4. Contrainte archimédienne : ce que modulo `3^k` peut ajouter

Supposons `b_i=F_i-S_i>=0` sur `[0,t]`. L'identité affine donne

\[
0<n_t<2^{b_t+1}(n_0+t/3),
\]

car chaque `q_r=3^r/2^{S_r}>=1` et `q_t<2^{b_t+1}`. Si `r_{t,k}` est le représentant canonique de (36.1) entre `0` et `3^k-1`, alors `n_t>=r_{t,k}`, si bien que

\[
\boxed{n_0>\frac{r_{t,k}}{2^{b_t+1}}-\frac t3.}\tag{36.3}
\]

Ce **n'est pas** une exclusion : c'est un minorant explicite sur un éventuel départ naturel réalisant le préfixe, et il dépend du choix de `k<=t`. Une information supplémentaire apparaît uniquement en joignant à la congruence un contrôle de la taille réelle des entiers. Dans les formulations inverses, cela retrouve le « realizer floor » et les reparamétrisations soulignées dans les préprints de 2026, sans garantie de nouveauté.

### Calcul sur le mot oscillant de contrôle de l'expérience 35

Calcul exact (`shadow_height.py`) :

| Horizon t | k | Déficit b_t | Bits exigés par (36.3) | Bits du représentant canonique modulo `2^(S_t+1)` |
|---:|---:|---:|---:|---:|
| 1 000 | 64 | 19 | 82 | 1 566 |
| 1 000 | 512 | 19 | 792 | 1 566 |
| 5 000 | 64 | 24 | 74 | 7 900 |
| 5 000 | 256 | 24 | 381 | 7 900 |
| 5 000 | 512 | 24 | 786 | 7 900 |

La dernière colonne est seulement la taille du **plus petit représentant positif de la classe 2-adique à cet horizon**. Les inégalités ne démontrent ni une réalisation infinie ni l'absence de réalisation infinie. Le test `3^k` n'a pas fourni de filtre plus fort sur ce mot.

## 5. Tests réellement exécutés

- `verify_dual_residues.py` : 390 mots aléatoires, valuations dans `[1,6]`, longueurs de 1 à 60, deux entiers distincts par classe.
- 28 874 vérifications de (36.1) pour les modules 3, 9, 27, 81, 243 et 729, dont le mot oscillant de 1 000 étapes.
- Préfixes mécaniques de longueurs `10,49,100,300,1000`, reconstruits par la congruence (36.2) ; pour chaque indice de ces préfixes, l'état accéléré est strictement supérieur au départ.
- `shadow_height.py` : 24 minorants obtenus avec arithmétique entière exacte, sur 4 horizons et 7 valeurs possibles de k (selon la longueur).
- Le script original `complexity_test.py` de l'expérience 35 a été relancé, et ses résultats de complexité et de répétitions reproduits.

**Pas de compilation Lean** ; pas d'exhaustivité sur tous les mots infinis ; pas d'audit indépendant de l'ensemble des préprints 2026.

## 6. Littérature comparée, et ce qu'elle évite de répéter

1. **Dubickas (2009)**, *On integer sequences generated by linear maps*, Glasgow Mathematical Journal 51(2), 243–252, DOI `10.1017/S0017089508004655`. Son résumé annonce des bornes de complexité pour des suites linéaires et une proposition/spéculation analogue relative au codage 3x+1. Attention à ne pas lui attribuer directement notre lemme accéléré de l'expérience 35 sans lire sa formulation exacte.
2. **López et Stoll (2009)**, *The 3x+1 Conjugacy Map over a Sturmian Word*, *Integers* 9(2), 141–162. Ils étudient des codages sturmiens 2-adiques de faible complexité.
3. **Elias De Jesús (sept. 2026)**, *A Drift-Sensitive Complexity Bound for Rational Points of the 3x+1 Conjugacy Map*, DOI `10.5281/zenodo.23071770`. Le résumé annonce une borne pour la complexité des **vecteurs de parité de la transformation non accélérée** en fonction de la dérive, et souligne les restrictions sur les réalisations rationnelles. Nos mots de valuations accélérées ne sont pas les mêmes objets, même si l'esprit de la méthode de divisibilité est voisin. Préprint non vérifié indépendamment ici.
4. **Elias De Jesús (sept. 2026)**, *A Global Occupation Conjecture for the Accelerated 3x+1 Map*, DOI `10.5281/zenodo.22906673`. Son résumé identifie explicitement le « pointwise realizer problem » et prévient que plusieurs coordonnées prétendument nouvelles (chiffres de relèvement, retenues, budgets de transport) sont des reparamétrisations de la même information. Préprint, non validation externe.
5. **Dépôt public `msharpe248/collatz`** (consulté en octobre 2026). Il annonce des théorèmes Lean 4 sur la limite des certificats à fenêtre bornée, sur l'échelle de complexité des mots et sur l'ombre 3-adique. Nous n'avons **pas compilé** son dépôt, ni vérifié indépendamment l'ensemble de ses théorèmes. Ces revendications sont un signal important d'antériorité pour notre approche.

Sources :
- https://doi.org/10.1017/S0017089508004655
- https://www.degruyterbrill.com/document/doi/10.1515/INTEG.2009.014/html
- https://doi.org/10.5281/zenodo.23071770
- https://doi.org/10.5281/zenodo.22906673
- https://github.com/msharpe248/collatz

## 7. Décision de recherche

**À conserver :** l'identité modulaire (36.1), la réalisation exacte (36.2), le test de taille (36.3) comme contrôles élémentaires. Ils sont faciles à formaliser dans Lean mais ne résolvent pas le problème global.

**À abandonner :** l'idée selon laquelle les restes modulo `3^k`, calculés à partir des valuations, fourniraient une contrainte « indépendante » suffisante pour éliminer des trajectoires symboliques de grande complexité. La construction de tous les mots finis et les travaux 2026 démontrent pourquoi cette stratégie, sans nouvelle hypothèse, répète une information déjà disponible.

**Piste restante plus pertinente :** chercher un énoncé de **réalisation uniforme** reliant *un même départ naturel* et des fenêtres à plusieurs échelles, avec un théorème d'exclusion quantitatif qui ne découle pas d'une reparamétrisation 2-adique. Examiner en priorité la littérature 2026 et les contre-exemples aux hypothèses d'occupation avant toute nouvelle série de calculs. Un tel énoncé n'est pas actuellement démontré et pourrait être aussi difficile que Syracuse.

**Verdict scientifique :** aucun nouveau cas de Syracuse résolu ; une voie de recherche négative identifiée précisément et étayée par un théorème élémentaire et des tests indépendants.
