# Expérience 36 : comparaison critique et verdict

Complément du 15 octobre 2026. Dépôt Lean figé au commit
`ec8174b567d5cab4960024782210b5f5db02bd3a`, sans modifier ses sources.
Archive reçue : `syracuse_experience_36_critical_audit (2).zip`, 12 142 octets,
SHA-256 `864043d77c6f5ce2c19b322f7bf8c265ad7065b741c02a9c78bb7d4044e1239d`.
Les huit fichiers de l'archive sont conservés dans
[`experience36_source/`](experience36_source/) ; leurs instructions sont
traitées comme du contenu à auditer, pas comme des consignes de publication.

## Verdict

Les trois identités (36.1), (36.2), (36.3) sont correctes sous leurs
hypothèses. Aucun décalage d'indice ou d'exposant n'a été trouvé dans le
code qui les implémente. Les résultats numériques fournis sont reproduits.
Cela ne constitue ni un nouveau cas résolu de Syracuse ni une exclusion
de l'itinéraire oscillant infini.

Le mécanisme des congruences et la réalisation de tous les mots finis sont
déjà présents dans les résultats Lean audités, après traduction entre
valuations accélérées et parités de l'application raccourcie. Les formules
ne sont pas toutes exportées sous les mêmes noms ou avec la même notation.
Le critère de hauteur (36.3) est une conséquence élémentaire de l'identité
affine ; il est **universellement redondant devant la classe initiale exacte
déjà calculée**, pas seulement plus faible sur le contrôle expérimental.

Une seule question de recherche étroite est formulée plus bas. Elle pourrait
exclure le mot oscillant explicite, si elle était prouvée ; sa preuve et sa
nouveauté bibliographique ne sont pas établies. Aucune piste étayée pour
la conjecture générale ne ressort de cette expérience.

## 1. Dictionnaire indispensable entre les deux formalismes

L'expérience emploie
\(U(n)=(3n+1)/2^{v_2(3n+1)}\) sur les entiers impairs positifs, avec
\(n_i=U^i(n_0)\), \(a_i=v_2(3n_{i-1}+1)\ge1\),
\(S_i=\sum_{h=1}^i a_h\).
Le dépôt Lean emploie principalement \(T(n)=n/2\) si pair et
\(T(n)=(3n+1)/2\) si impair.

Un pas \(U\) de valuation \(a_i\) correspond exactement à \(a_i\) pas \(T\),
avec bloc de parités \(1\,0^{a_i-1}\). Ainsi

\[
n_i=T^{S_i}(n_0),\qquad \operatorname{oddSteps}(S_i,n_0)=i.
\]

Pour fixer aussi l'imparité de l'arrivée \(n_N\), il faut le bit de parité
supplémentaire à l'instant \(S_N\). Le mot complet de parités qui fixe
les valuations exactes a donc longueur \(S_N+1\), non \(S_N\).
Confondre nombre de pas accélérés, temps raccourci et nombre d'impairs
rendrait les comparaisons de complexité ou les puissances de 3 incorrectes.

## 2. Couverture par les théorèmes Lean

Les liens exacts des 39 déclarations initialement inspectées sont dans
[INDEX_SOURCES.md](INDEX_SOURCES.md). `Parity.lean` et `WordAffine.lean`
ont aussi été compilés comme dépendances. « Corollaire » ci-dessous
désigne une traduction mathématique explicitée ici, pas nécessairement
un théorème exporté textuellement dans le dépôt.

| Affirmation de l'expérience | Résultat Lean pertinent | Différence de portée / statut |
|---|---|---|
| Identité affine \(2^{S_i}n_i=3^in_0+C_i\) | `terras_exact_form`, `WordAffine.exact_form` | Même identité après le changement d'horloge \(T=S_i\), \(j=i\). |
| (36.1), reste déterminé par les dernières valuations | `terras_exact_form`, `shadow_modEq`, `dcoef_add` | Corollaire pour le suffixe de longueur raccourcie \(A\) à exactement \(k\) impairs. Le dépôt ne donne pas littéralement la somme à indices accélérés ; la version entière et sa somme fermée sont formalisées dans `Experience36.lean`. |
| Tout mot fini positif de valuations est réalisable | `parity_pattern_realized`, `parities_inj`, `modEq_of_parity`, `Cylinder.transport` | Utiliser les blocs \(1\,0^{a_i-1}\) et le bit terminal 1 : une unique classe modulo \(2^{S_N+1}\). Les représentants positifs sont arbitrairement grands. |
| (36.2), critère arithmétique de réalisation | `WordAffine.realizes_iff_dvd` et bijection des parités | Le critère Lean pour un mot raccourci fixé ne doit pas faire oublier le bit terminal. Le \(+1\) de l'exposant dans (36.2) est essentiel. |
| Absence de descente universelle dans une fenêtre bornée | `no_uniform_descent_bound` ; plus généralement `no_finite_certificate` | Le premier résultat couvre la conclusion existentielle. Le second exclut une famille précise de poids rationnels bornés, avec facteur de contraction fixe ; il ne réfute pas toute méthode finie. |
| Préfixes critiques proches de la ligne critique | `critical_line_sharp`, `no_descent_of_supercritical_prefix` | La construction exacte de mots diffère, mais l'existence de témoins finis près de la ligne critique et sans descente est déjà couverte. |
| Faible complexité exclue sur les orbites non bornées | `ParityComplexity.unbounded_factor_floor`, `bounded_of_linear_complexity` | Facteurs de l'itinéraire infini de parité \(T\), pas facteurs d'un échantillon de valuations \(U\). L'expérience ne fournit pas l'enveloppe globale exigée. |
| Un mot critique mécanique pourrait se réaliser indéfiniment | `no_eventual_irrational_mechanical` | Il exclut déjà ce mot critique particulier après traduction détaillée en section 5. Il ne suffit pas pour le mot oscillant modifié. |
| (36.3), minorant de taille | Identité affine / `terras_iter_eq_ideal` | Déduction élémentaire avec \(b_i\ge0\) à tous les indices nécessaires ; pas de théorème exporté identique identifié. Aucune nouveauté scientifique établie. |

`InverseBarrier` impose aussi des restrictions sur les arrivées
\(1\bmod3^K\) sous budget d'impairs et coefficient non contractant.
Il ne rend pas impossible un mot fini de valuations : il décrit des
arrivées que ses réalisations ne peuvent pas avoir. `CongruenceRelaxation`
et `CorrectionDecode` concernent des corrections libres qu'il faut prouver
atteignables ; dans (36.1), les corrections sont déjà celles du mot fixé.

## 3. Vérification exacte de (36.1), indices compris

Pour \(1\le k\le t\), posons

\[
A=\sum_{h=t-k+1}^{t}a_h,\qquad
B_j=\sum_{h=t-j}^{t}a_h\quad(0\le j<k).
\]

L'identité entière exacte est

\[
\boxed{2^A n_t=3^k n_{t-k}
       +\sum_{j=0}^{k-1}3^j2^{A-B_j}.}
\]

Tous les exposants \(A-B_j\) sont non négatifs. On obtient cette identité
en déroulant \(2^{a_i}n_i=3n_{i-1}+1\) exactement \(k\) fois.
Le terme \(j=0\) utilise seulement \(a_t\), le dernier terme utilise
\(a_t+\cdots+a_{t-k+1}\). Le terme oublié lors du passage au module est
précisément \(3^k n_{t-k}\), pas \(3^{k-1}n_{t-k}\).
Comme \(2^A\) est inversible modulo \(3^k\), la division dans cet anneau donne

\[
n_t\equiv\sum_{j=0}^{k-1}3^j2^{-B_j}\pmod{3^k},
\]

exactement (36.1). Le bord \(t=k\) conserve \(n_0\) dans le terme annulé
et ne crée aucun problème. La formule ne doit pas être appliquée avec
\(k>t\). Les puissances négatives sont des inverses modulaires, pas des
quotients entiers ni des nombres réels égaux à \(n_t\).

**Contre-exemple aux erreurs d'indices.** Partir de \(n_0=3\) donne
\(a_1=1,n_1=5,a_2=4,n_2=1\). Pour \(t=k=2\),

\[
2^{-4}+3\,2^{-5}\equiv4+6\equiv1\pmod9.
\]

Inverser l'ordre des valuations donnerait 2 modulo 9 ; remplacer \(3^j\)
par \(3^{j+1}\) donnerait 3. La somme réelle est seulement \(5/32\),
avec reste réel \(3^2\cdot3/2^5=27/32\), et non l'entier 1 à elle seule.
Les mots \((1,1)\) et \((1,3)\), pourtant de mêmes parités de valuations,
donnent respectivement les résidus 8 et 2 modulo 9 : le résultat ne permet
pas de remplacer les valuations par leurs seuls restes modulo 2.

**Formalisation locale.** `Experience36.lean` démontre pour toute suite
satisfaisant les récurrences entières : `exact_suffix`, `suffix_congruence`
et `correction_closed`. Sa convention est à indices commençant à zéro :
`a i` relie `n i` à `n (i+1)`, et son départ `s` vaut \(t-k\).
La somme fermée prouvée est
\(C=\sum_{i=0}^{k-1}3^{k-1-i}2^{\sum_{h=0}^{i-1}a_{s+h}}\).
Le changement \(j=k-1-i\) redonne la somme encadrée ci-dessus.
Le passage final aux inverses modulaires et le dictionnaire avec \(U\)
sont justifiés mathématiquement ici ; ils ne sont pas des déclarations
supplémentaires formalisées dans ce fichier. Ses trois théorèmes compilent
sans `sorry` et n'utilisent que les fondations usuelles de Lean.

## 4. (36.2) et (36.3) : correctes, mais aucune fermeture globale

### Réalisation finie et bit terminal

Avec \(C_0=0\), \(C_i=3C_{i-1}+2^{S_{i-1}}\), l'identité affine et
l'imparité de l'arrivée donnent bien

\[
3^N n_0+C_N\equiv2^{S_N}\pmod{2^{S_N+1}}.
\]

La multiplication par \(3^N\) est bijective dans cet anneau ; pour \(N\ge1\),
\(C_N\) est impair, donc la classe du départ est impaire. En remontant
la correction ou en utilisant les blocs de parité et le bit terminal,
on retrouve à chaque étape une valuation **exactement** égale à \(a_i\).
La classe contient donc une infinité de départs positifs ; la condition
de ne pas être divisible par 3 se rajoute par le théorème chinois.

Omettre le \(+1\) dans le module est faux : pour le mot \((1)\),
\(n_0=1\) vérifie \(3n_0+1\equiv0\pmod2\), mais la valuation réelle est
2, non 1. Le code livré conserve correctement ce bit. Les nouveaux tests
vérifient aussi le représentant canonique lui-même, alors que le test
aléatoire livré utilise les deux relèvements `r+M`, `r+2M`.

Ce résultat reste \(\forall N\,\exists n_0(N)\), sans fournir un départ
positif commun à tous les préfixes. La limite compatible dans \(\mathbb Z_2\)
n'est pas nécessairement un entier naturel.

### Hauteur et redondance universelle

Posons \(F_i=\lfloor i\log_2 3\rfloor\), \(b_i=F_i-S_i\),
\(q_i=3^i/2^{S_i}\). Si \(b_i\ge0\) pour \(0\le i\le t\), alors
\(q_i\ge1\), \(q_t<2^{b_t+1}\), et

\[
n_t=q_t\left(n_0+\frac13\sum_{i=0}^{t-1}q_i^{-1}\right)
 <2^{b_t+1}(n_0+t/3).
\]

Pour le représentant \(\rho_{t,k}\in[0,3^k)\) de (36.1),
\(n_t\ge\rho_{t,k}\) donne donc exactement (36.3). Le calcul de `seed_min`
utilise correctement \(\lfloor\rho/2^{b_t+1}-t/3\rfloor+1\), puisque
l'inégalité est stricte. Connaître seulement \(b_t\ge0\), sans les
déficits intermédiaires, ne justifierait pas la majoration de la somme.

**Observation générale démontrée ici, sans revendication de nouveauté.**
Fixer un mot fini \(w=(a_1,\ldots,a_N)\) avec les déficits nécessaires
non négatifs, et noter \(r_N\) son plus petit représentant positif modulo
\(2^{S_N+1}\). Pour tous \(k\le t\le N\),

\[
L_{t,k}:=\max\left(1,
 \left\lfloor\rho_{t,k}/2^{b_t+1}-t/3\right\rfloor+1\right)\le r_N.
\]

**Preuve :** \(r_N\) réalise réellement tout le mot, donc l'inégalité
(36.3), qui est nécessaire, lui est applicable. C'est tout. Aucun comptage
ni modèle aléatoire n'est nécessaire. En particulier même le maximum des
\(L_{t,k}\) ne retranche aucun départ de la classe exacte déjà connue.
Cela renforce la portée du constat expérimental « pas mieux sur notre mot »
en une redondance pour tous les mots satisfaisant ces hypothèses. Une borne
peut néanmoins être utile quand la classe exacte n'a pas encore été
calculée ; aucun gain algorithmique n'a été mesuré ici.

## 5. Le mot critique infini est déjà exclu ; pas le mot oscillant

Pour le contrôle critique \(a_i=F_i-F_{i-1}\), tous les \(q_i\) sont
strictement supérieurs à 1 pour \(i\ge1\), donc les préfixes réalisables
montent strictement aux instants accélérés. L'argument fini est correct.

La version **infinie** se traduit déjà en un cas exclu par Lean.
Écrire \(\alpha=\log_2 3\), \(\beta=1/\alpha=\log_3 2\).
Les positions impaires dans l'itinéraire raccourci seraient exactement
\(S_i=\lfloor i\alpha\rfloor\) pour \(i\ge0\). Son bit à l'instant \(u\)
est alors

\[
w_u=\lceil(u+1)\beta\rceil-\lceil u\beta\rceil.
\]

Pour \(u\ge1\), les arguments sont non entiers et ce bit égale
\(\lfloor(u+1)\beta\rfloor-\lfloor u\beta\rfloor\).
Ainsi la queue après **un pas raccourci** est le mot mécanique inférieur
de pente \(\beta\), d'intercept \(\beta\). Cette pente est irrationnelle,
car une relation rationnelle conduirait à \(2^p=3^q\) avec \(p,q>0\).
`no_eventual_irrational_mechanical` exclut cette queue pour tout départ
naturel. Il y a un vrai effet de bord : à \(u=0\), le bit supérieur vaut 1
et le bit inférieur d'intercept zéro vaut 0. Les confondre globalement
serait une erreur ; le décalage d'un pas la corrige.

Le générateur oscillant modifie les horloges par un déficit logarithmique
et des oscillations. On n'a pas démontré qu'il entre dans une famille
d'itinéraires déjà exclue, ni qu'un entier le réalise. Les théorèmes sur
la complexité de parité ne s'appliquent pas automatiquement à des comptes
finis de facteurs d'un alphabet de valuations. Aucune exclusion de ce mot
oscillant infini n'est acquise dans cet audit.

## 6. Erreurs de portée et défauts de reproductibilité

1. **Deux contrôles distincts sont mêlés dans la présentation.**
   `test_oscillations.build` utilise le bit d'oscillation déterministe
   `int(d[t]==2 and not isjump)`. Les deux scripts principaux ne réutilisent
   que son calendrier de sauts et reconstruisent un autre bit avec un
   xorshift de graine `0x2545F4914F6CDD1D`. Les mots diffèrent dès
   \(a_{14}\) : 1 pour le contrôle direct, 2 pour le contrôle xorshift.
   À longueur 1 000, leurs représentants canoniques ont respectivement
   1 562 et 1 566 bits. Le tableau (36.3) concerne **le second**.
   Les deux scripts principaux sont cohérents entre eux : leurs nombres
   ne sont pas faux, mais l'identification au même « mot de contrôle de
   l'expérience 35 » demande correction ou justification externe.
2. **Complexité de l'expérience 35 non reproductible avec ce ZIP.**
   `complexity_test.py`, annoncé comme relancé, n'est pas fourni, pas plus
   que ses sorties détaillées ou son engagement Git. Le script inclus
   `test_oscillations.py` vérifie des valuations et compte des variations ;
   il ne calcule pas la complexité en facteurs annoncée. L'exécution passée
   invoquée peut avoir eu lieu, mais cet audit ne la confirme pas.
3. **« Aucun filtre modulo \(3^k\) » est trop général sans qualification.**
   Vérifier une identité définie à partir du même mot est redondant. Un
   prédicat supplémentaire sur les résidus peut en revanche rejeter des
   mots : par exemple demander une arrivée \(1\bmod9\) rejette \((1,1)\),
   dont le résidu est 8. Ce prédicat n'est pas une condition universellement
   nécessaire pour toutes les orbites positives. Il faut donc distinguer
   identité tautologique, hypothèse externe justifiée et simple filtre
   arbitraire. Le régime \(k>t\), hors (36.1), conserve aussi un terme
   dépendant du départ ; il ne faut pas l'effacer. Exemple vérifié : les
   départs 3 et 7 ont tous deux \(a_1=1\), mais leurs arrivées 5 et 11
   diffèrent modulo 9 (5 contre 2). Une seule valuation ne détermine donc
   pas deux chiffres ternaires.
4. **Les préprints cités ne sont pas validés par les tests.**
   La phrase « la construction et les travaux 2026 démontrent pourquoi »
   attribue trop de force à une littérature que l'expérience reconnaît
   ne pas avoir auditée. L'argument élémentaire autonome suffit pour la
   redondance locale ; ces préprints ne sont pas des preuves supplémentaires
   vérifiées ici. Les affirmations de priorité restent non établies.
5. **Grande taille finie n'est pas une preuve d'absence de réalisation.**
   Les 7 900 bits à l'horizon 5 000, l'activité des oscillations et les
   préfixes critiques sans descente n'établissent aucun énoncé universel
   sur le mot infini. La colonne `modulus_bits` du CSV critique représente
   l'exposant du module \(2^m\), alors que `modulus_bits` dans le CSV de
   hauteur est le véritable `bit_length` de \(3^k\) : ne pas les comparer
   comme des mesures identiques.

## 7. Une seule piste distincte, très limitée et non démontrée

**Objectif : exclure le mot oscillant xorshift exact, pas les orbites
générales.** Cette exclusion n'a pas été identifiée comme conséquence des
théorèmes audités. Elle pourrait ajouter un résultat pour une suite
explicite, à condition d'obtenir une preuve qui dépasse la réécriture des
congruences. Sa priorité bibliographique serait encore à examiner.

Définir \(d_t=F_t-F_{t-1}\), les dates de saut

\[
J_0=0,\qquad J_j=\min\{t\ge\max(J_{j-1}+1,
\lfloor\sqrt{2^j}\rfloor):d_t=2\},
\]

et les valuations du **second** générateur, avec la graine et les trois
opérations xorshift exactes du ZIP. Noter \(r_N\in[1,2^{S_N+1})\) la classe
canonique de ce préfixe.

**Petit lemme candidat précis, non prouvé :**

\[
\forall j\ge1,\qquad r_{J_j}\ge2^j.
\]

Il suffirait à exclure un entier positif commun à tous les préfixes :
pour un tel entier fixé \(n\), lorsque \(2^{S_N+1}>n\), la congruence
imposerait \(r_N=n\), ce qui contredit la borne non bornée.
Les représentants compatibles sont non décroissants ; le problème réel
est de forcer indéfiniment des relèvements non nuls, pas de recalculer
leur reste ternaire.

**Contre-exemple à rechercher :** un indice explicite \(j\) tel que
\(r_{J_j}<2^j\), en utilisant exactement le générateur xorshift et non
le contrôle direct. Les 24 premières dates (jusqu'à \(J_{24}=4096\))
satisfont la borne dans les tests. Ces 24 cas ne la prouvent pas. Un seul
échec réfuterait ce lemme quantitatif, sans prouver pour autant la
réalisation entière du mot infini. Une longue stabilisation des \(r_N\)
serait aussi un diagnostic utile, sans être une preuve de stabilisation
éternelle.

**Appréciation : faible priorité.** Aucun mécanisme uniforme ne prouve
actuellement cette borne ; prolonger seulement les calculs ne résoudrait
pas ce manque. Il n'y a pas de deuxième piste suffisamment étayée à
recommander. Pour une preuve de Syracuse, aucune voie prometteuse n'est
établie par cette expérience.

## 8. Tests effectivement terminés

- Les trois scripts fournis ont été relancés dans une copie séparée pour
  préserver les entrées originales. `verify_dual_residues.py` reproduit
  **390 mots aléatoires et 28 874 contrôles modulo \(3^k\)**.
- `results.json`, `critical_prefixes.csv`, `shadow_height.csv` sont
  identiques après lecture structurée ; les **24 lignes** de hauteur
  et les **5 préfixes critiques** sont reproduits.
- La suite indépendante `test_experience36.py` vérifie les identités
  rationnelles exactes, tous les suffixes des mots de longueur 1 à 6
  sur l'alphabet \(\{1,2,3,4\}\), les conditions de hauteur sur de petits
  mots admissibles, les contre-exemples de mutations, la traduction du
  mot critique, la différence des générateurs et la piste limitée ci-dessus.
  Les comptes et résultats sont dans `logs/exp36_independent.json`.
- Les **trois lemmes locaux** de `Experience36.lean` compilent ; les
  requêtes d'axiomes n'indiquent que `propext`, `Classical.choice`, `Quot.sound`.
- Les **39 requêtes d'axiomes amont** de l'audit initial ont été réexécutées
  sur les artefacts du même commit, et leurs sources sont contrôlées par
  les empreintes. Cela ne prétend pas reconstruire de nouveau tous les
  modules amont ni vérifier Mathlib avec un second noyau.

Les 43 tests Python de la première phase ne sont pas présentés comme
réexécutés lors de cette comparaison. Les précisions de commandes et les
limites de validation figurent dans [VALIDATION.md](VALIDATION.md).
