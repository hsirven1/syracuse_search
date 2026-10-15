# Audit critique du dépôt `msharpe248/collatz`

## Périmètre et traçabilité

Audit commencé le 14 octobre 2026 (America/Toronto). Copie de travail :
`/workspace/collatz`, obtenue par `git clone` HTTPS, sans écriture distante.
Commit examiné : **`ec8174b567d5cab4960024782210b5f5db02bd3a`**.
Les fichiers suivis du dépôt externe restent inchangés. Ses sous-modules de
bibliographie n'ont pas été initialisés ; cet audit porte sur `lean/Collatz`,
pas sur les preuves des dépôts référencés dans `library/`.

Outils : Python 3.12.14 ; Lean **4.27.0-rc1**, version prescrite par
`lean/lean-toolchain` ; Mathlib fixé par le manifeste au commit
`359769ac56adab9784ed43b8809a3ede33c202a9`.
Le fichier [provenance.json](logs/provenance.json) contient les empreintes des
95 sources Lean principales et de l'archive du compilateur.

L'[index des 39 énoncés ciblés](INDEX_SOURCES.md) donne les liens vers les
sources figées et leurs lignes exactes.

**Complément du 15 octobre 2026 : ZIP reçu et comparé.** Les identités
(36.1)–(36.3) sont correctes sous leurs hypothèses ; les résultats JSON/CSV
sont reproduits. Les mécanismes principaux sont déjà couverts par les
théorèmes Lean après changement d'horloge. Le minorant de hauteur est
redondant devant la classe initiale exacte pour tous les préfixes concernés.
Deux générateurs différents sont mêlés dans la présentation et la complexité
de l'expérience 35 n'est pas reproductible avec cette archive.

La [comparaison détaillée de l'expérience 36](EXPERIENCE36_COMPARAISON.md)
donne les preuves avec indices, les différences d'hypothèses, les
contre-exemples et une seule piste de recherche étroite, non démontrée.
Aucune nouveauté scientifique n'est revendiquée.

## Résultat principal de la lecture

Ce dépôt ne fournit pas une preuve générale de Syracuse. Il contient des
preuves proposées de restrictions précises sur des familles de certificats
et d'itinéraires, des équivalences qui déplacent le problème et des calculs
exploratoires. Il faut distinguer leurs énoncés des commentaires interprétatifs.
Le statut de recompilation locale est donné dans `VALIDATION.md` ; la lecture
et les tests Python ne suffisent pas à certifier les théorèmes Lean.

**Vérification locale obtenue :** compilation réussie des 16 modules ciblés
et de leurs dépendances ; inspection réussie des axiomes de 39 énoncés,
sans `sorryAx` ni axiome spécifique supplémentaire, avec les fondations
usuelles de Lean/Mathlib. Les 43 tests Python sélectionnés et les contrôles
indépendants sont également passés. Ce n'est pas un audit de tous les
modules du dépôt, ni une vérification par un second noyau indépendant.

La convention centrale est l'application raccourcie

\[
T(n)=\begin{cases}n/2&n\text{ pair},\\(3n+1)/2&n\text{ impair}.\end{cases}
\]

Ce n'est ni l'application ordinaire `collatz`, ni l'application accélérée
sur impairs `syracuse`. Un « pas », une densité d'impairs et un horizon
doivent être traduits avant toute comparaison entre expériences.
Dans la suite, \(j_t(n)\) compte les pas impairs parmi les \(t\) premiers pas
de \(T\), et \(d_t(n)\) désigne `dcoef t n`.

## Fenêtres finies : une impossibilité précise, pas universelle

Dans `NoGo.lean:134`, `no_uniform_descent_bound` énonce

\[
\forall B,N_0\quad\exists n\ge N_0\quad
\forall t\le B,\ T^t(n)\ge n.
\]

La famille de témoins est explicite : pour \(0\le t\le L\),
\(T^t(2^L-1)=3^t2^{L-t}-1\). Le témoin dépend de l'horizon.
Passer de « pour chaque horizon il existe un entier » à « il existe un
entier qui survit à tous les horizons » serait une permutation illégitime
des quantificateurs. Une limite 2-adique peut être \(-1\), sans être un
entier naturel positif.

Dans `NoGo.lean:205`, `no_finite_certificate` exclut exactement ceci :
un poids \(W:\mathbb N\to\mathbb Q\), des constantes
\(0<\ell\le W(n)\le h\), un horizon fixe \(B\), un seuil fixe \(N_0\),
et \(\rho\in[0,1)\cap\mathbb Q\), tels que chaque \(n\ge N_0\) admette
un \(1\le t\le B\) vérifiant

\[
T^t(n)W(T^t(n))\le\rho nW(n).
\]

La preuve chaîne les contractions dans une montée de Mersenne trop longue :
le poids devrait finalement descendre sous sa borne inférieure.
`no_finite_state_certificate` (`:289`) spécialise cette impossibilité aux
poids positifs rationnels indexés par un ensemble fini d'états.

**Limites de portée :** cela ne réfute pas tout raisonnement par résidus,
toute induction, toute preuve finiment décrite, ni toute méthode avec
mémoire finie. Des horizons dépendant de l'entrée et non uniformément
bornés, des poids sans ces deux bornes, ou d'autres formes de certificats
échappent aux hypothèses. Le commentaire qui évoque `exp(Φ)` réel dépasse
littéralement l'énoncé formalisé à poids rationnels ; une extension aux réels
demanderait son propre argument. Les formules générales « no bounded-memory
argument » du texte explicatif doivent être lues avec ces restrictions.

`Critical.lean:139`, `critical_line_sharp`, réalise aussi des survivants
arbitrairement grands avec \(2^B\le3^{j_B}\le3\,2^B\).
Cela montre qu'un horizon fini peut imiter la ligne critique
\(j_B/B\approx\log 2/\log 3\). Ce n'est ni une orbite infinie critique,
ni la nécessité pour toute orbite divergente de rester dans cette bande
étroite à toutes les échelles. Une borne inférieure de densité ne donne
pas l'égalité à la densité critique.

## Complexité symbolique : conditions fortes et hypothèses manquantes

`ParityComplexity.lean` définit \(p_N(L)\), le nombre de facteurs distincts
de longueur \(L\) de **l'itinéraire infini entier** de \(N\). Un compte sur
un préfixe observé ne donne qu'une borne inférieure de cette quantité.

| Énoncé | Portée exacte |
|---|---|
| `unbounded_factor_floor` (`:75`) | Si l'orbite est non bornée et \(N+1\le2^K\), alors \(p_N(3q+K)\ge5q+1\) pour tout \(q\). |
| `bounded_of_linear_complexity` (`:82`) | Une enveloppe globale \(A p_N(L)\le B L+C\), avec \(3B<5A\), implique la bornitude. |
| `bounded_of_additive_linear_complexity` | En particulier, \(p_N(L)\le L+C\) à toutes les longueurs implique la bornitude. |
| `no_sturmian_complexity` (`:111`) | Aucun entier naturel n'a exactement \(p_N(L)=L+1\) pour tout \(L\). |

Le mécanisme relie égalité de blocs de parité et congruence des états modulo
\(2^L\). Une borne universelle de hauteur rend les premiers états distincts
effectivement distincts modulo cette puissance. Le seuil \(5/3\) vient
de la majoration de croissance en bits utilisée ; ce n'est pas une barrière
optimale établie. Aucune enveloppe universelle sous ce seuil n'est démontrée.
La bornitude d'une orbite déterministe sur les naturels entraîne un cycle
éventuel, mais n'identifie pas ce cycle comme le cycle trivial.

`MechanicalComplexity.lean:56` démontre l'enveloppe \(p_N(L)\le L+1\)
sous l'hypothèse d'un codage mécanique exact
\(\lfloor(t+1)\alpha+\rho\rfloor-\lfloor t\alpha+\rho\rfloor\).
`no_irrational_mechanical` (`:154`) exclut alors toutes les pentes
irrationnelles et tous les intercepts, ainsi que les queues correspondantes.
Ce résultat est plus général que les seules familles métalliques décrites
ailleurs dans le README.

`RationalMechanical.lean:122`, `mechanical_classification`, va plus loin :
si un entier **positif** a un itinéraire global exactement mécanique,
alors \(\alpha=1/2\) et \(N\in\{1,2\}\).
`eventual_mechanical_reaches_one` (`:135`) traite une queue mécanique.
Cela ne prouve pas que toute orbite possède une telle queue ; cette
hypothèse constitue précisément une restriction majeure.
Un motif numériquement presque équilibré ou peu complexe sur un préfixe
n'établit aucune de ces hypothèses infinies.

Les résultats de `ParityDefects.lean` et `DefectHeight.lean` proposent aussi
des certificats **finis**, à horizons explicites, de retour à une période
\(q\) lorsque les désaccords de parité sont assez rares. Ils ne démontrent
pas cette rareté pour toutes les orbites. Pour une période générale, retour
et bornitude ne signifient toujours pas convergence vers 1.

## Contraintes 3-adiques et couplage arithmétique

Dans `Shadow.lean`, l'identité exacte est

\[
2^tT^t(n)=3^{j_t(n)}n+d_t(n).
\]

La correction et le nombre d'impairs dépendent seulement du préfixe de
parité, lui-même déterminé par \(n\bmod2^t\). `shadow_modEq` (`:144`)
en déduit que deux départs congrus modulo \(2^t\) ont des arrivées congrues
modulo \(3^{j_t}\). La composition conserve le couplage :

\[
d_{s+t}(n)=3^{j_t(T^s n)}d_s(n)+2^s d_t(T^s n).
\]

`shadow_compression` (`:324`) borne le **nombre de paires**
\((j,T^t(n)\bmod3^j)\) de l'ensemble `shadowSet t` :

\[
2^{\lfloor17(t-1)/27\rfloor}|\mathrm{shadowSet}(t)|\le3^t
\]

(avec soustraction naturelle tronquée pour \(t=0\)). Le taux asymptotique
de cette majoration vaut \(\log_2 3-17/27\approx0{,}95533\) bit par pas.
Il s'agit d'un comptage de supports, pas d'une preuve de loi uniforme,
d'indépendance, d'entropie probabiliste d'une orbite, ni de complexité de
Kolmogorov. Les fibres ont des moduli \(3^j\) variables ; on ne doit pas
confondre leur union avec un seul espace uniforme fixé.

`surviving_shadow_mem` (`:355`) exige notamment \(n\ge2^t\) et la
non-descente jusqu'à \(t\). Pour un entier de départ **fixe**, cette
hypothèse de taille cesse d'être satisfaite quand \(t\) augmente.
L'utiliser pour tous les horizons du même départ serait incorrect sans
argument supplémentaire de décalage et de contrôle des échelles.
La formule interprétative « divergence = compression soutenue » dans les
commentaires n'est pas à elle seule un théorème d'équivalence qui exclut
la divergence. Même un ensemble très mince peut contenir un entier.

`density_floor` (`:276`) exige à la fois une borne inférieure \(N\ge1\)
sur les états intermédiaires et une arrivée au moins égale au départ.
Il donne \(2^tN^{j_t}\le(3N+1)^{j_t}\), donc une contrainte de densité
nécessaire. Il ne fournit pas l'équidistribution ou le défaut de
compression qui permettrait de conclure.

`InverseBarrier.lean:55` exclut une arrivée congrue à 1 modulo \(3^{j_t}\)
pour un segment de longueur positive dont \(3^{j_t}\ge2^t\).
`bounded_odd_inverse_obstruction` (`:96`) en déduit que si
\(y\equiv1\pmod{3^K}\) et \(j_t\le K\), tout segment arrivant en \(y\)
doit avoir un coefficient strictement contractant.
L'énoncé ne dit pas que ces cibles sont divergentes ou non contractantes,
ni qu'on peut fixer \(K\) pour toutes les histoires possibles. Une absence
de prédécesseur sous un budget d'impairs n'est pas une absence absolue.

`NoncontractingTail.lean:79` établit une réduction plus forte : pour un
départ positif, non-bornitude équivaut à l'existence d'une queue où
\(2^t\le3^{j_t}\) à tous les horizons. Le fichier ne construit ni n'exclut
une telle queue. `all_orbits_bounded_iff_all_contract` (`:99`) reformule
la non-divergence, sans régler les cycles non triviaux.

## Pourquoi les relaxations numériques ne ferment pas le problème

`PruningLimit.lean:22` construit, pour chaque préfixe fixé et toute longueur
cible suffisamment grande, un budget d'impairs que l'enveloppe de correction
actuelle ne peut éliminer. La version pour une collection finie est à `:55`.
Ce résultat limite **cette enveloppe relâchée**, pas tout algorithme
d'élagage possible ; il ne produit aucune complétion réelle.

`CongruenceRelaxation.lean:11` construit même une correction artificielle
qui ferme exactement un retour tout en respectant une borne d'enveloppe.
Il manque que cette correction provienne d'un mot de parité.
Exemple vérifié : \(3^6\cdot3+194421=2^{16}\cdot3\), mais la correction
194421 n'est pas atteignable par un mot de longueur 16 à 6 impairs.

En revanche, `WordCongruence.lean:9` est exact **pour un mot fixé** :

\[
\operatorname{Realizes}(n,w)\iff
2^{|w|}\mid3^{\#1(w)}n+D(w).
\]

Il n'y a pas contradiction : ici \(D(w)\) est la véritable correction du
mot, et non un entier libre situé dans un intervalle.
`CorrectionDecode.lean:44` caractérise exactement l'atteignabilité via
reconstruction déterministe et vérification finale de la longueur, du
nombre d'impairs et de la correction. Il ne démontre pas une borne
uniforme sur les longueurs acceptées.

Enfin, `ResidueMapAudit.lean` montre une erreur possible dans des graphes
finis de résidus : \(3\equiv35\pmod{32}\), mais
\(T(3)=5\) et \(T(35)=53\equiv21\pmod{32}\).
La classe d'entrée modulo 32 ne définit donc pas une transition
déterministe vers la classe de sortie au même module. Il faut conserver
la précision supplémentaire, le quotient, ou toutes les branches possibles.

## Comparaison avec l'expérience 36 : verdict final

Le [complément détaillé](EXPERIENCE36_COMPARAISON.md) remplace la grille
provisoire de la première phase. Il établit notamment :

- La congruence modulo `3^k` est exacte, avec les `k` dernières valuations,
  les sommes cumulées inverses et les puissances `3^j` pour `0 ≤ j < k`.
- Le module `2^(S_N+1)` de réalisation est correct : le bit terminal est
  indispensable. Tous les mots finis positifs sont réalisables, ce qui
  ne fournit pas un entier fixé pour tous les horizons.
- Le mot critique infini non modifié est déjà exclu par le théorème Lean
  sur les queues mécaniques irrationnelles, après un décalage d'un pas
  raccourci. Cette traduction ne s'étend pas automatiquement au contrôle oscillant.
- Le minorant de hauteur (36.3) ne peut jamais dépasser le plus petit
  représentant positif de la classe exacte du préfixe ; ce fait est général.
- Les deux scripts principaux utilisent un contrôle xorshift distinct du
  contrôle direct inclus, avec une première différence à l'indice 14.
  Le fichier annoncé `complexity_test.py` est absent de l'archive.
- Une seule piste supplémentaire est proposée à faible priorité : une
  borne non bornée précise sur les représentants canoniques du mot
  oscillant fixé. Les 24 premiers cas passent, sans preuve générale.

La nouvelle validation comporte huit tests indépendants, trois lemmes Lean
locaux compilés et la réexécution des 39 requêtes d'axiomes amont.
Voir [VALIDATION.md](VALIDATION.md) pour les nombres de cas et les commandes.

## Ce qui reste ouvert et pistes à poursuivre

La non-divergence pour tous les entiers positifs et l'exclusion de tous les
cycles non triviaux restent ouvertes dans le travail examiné. Les théorèmes
conditionnels ne démontrent ni une faible complexité universelle, ni une
queue mécanique universelle, ni l'épuisement de tous les cylindres.

1. **Conserver l'arithmétique exacte des complétions.** Associer chaque
   préfixe à sa classe binaire, à sa correction atteignable et aux
   contraintes ternaires, plutôt qu'à leur seule enveloppe. Le décodage
   existant offre un vérificateur utile. Le véritable objectif supplémentaire
   serait un invariant qui se renforce avec la profondeur et une preuve de
   terminaison ou d'épuisement pour chaque départ ; ce résultat manque.
2. **Certificats à horizons adaptatifs avec preuve de couverture.** Le
   no-go rend peu prometteuse la recherche d'une contraction uniforme sur
   fenêtre bornée dans sa famille. Un horizon dépendant d'une hauteur ou
   d'une valuation reste permis, mais il faut prouver sa finitude, et pas
   seulement la constater sur un échantillon. La famille de Mersenne et les
   témoins près de la ligne critique sont des tests adverses indispensables.
3. **Complexité et défauts avec contrôle de hauteur.** Les critères finis
   de retour peuvent transformer certains motifs expérimentaux en
   certificats vérifiables. Chercher une majoration pour une famille bien
   définie est plus concret que postuler une faible complexité pour toutes
   les orbites. Une amélioration de la borne de hauteur pourrait améliorer
   le seuil \(5/3\), mais ne fournirait pas la majoration manquante.
4. **Compatibilité inter-échelles et frontière des entiers ordinaires.**
   `Cylinder.lean` conserve un même quotient pour tous les préfixes.
   Pour une hauteur fixée \(H<2^k\), le quotient doit être zéro : c'est une
   contrainte concrète absente d'un simple argument de compacité 2-adique.
   Il faudrait montrer que la branche compatible d'un entier fixé finit
   par descendre, sans remplacer cet entier par des témoins croissants.
5. **Traiter séparément les cycles.** Une preuve de bornitude générale ne
   suffirait pas à Syracuse. Les exclusions de familles mécaniques et de
   petites périodes sont utiles, sans couvrir tous les mots périodiques.

Ces pistes sont des objectifs de recherche, pas des annonces de résultats.
L'identité affine et le codage des parités appartiennent à un cadre classique
(Terras et travaux connexes). Le dépôt cite également des travaux antérieurs
sur les mots mécaniques et les cycles. Une attribution précise ou une
revendication de priorité demanderait une étude bibliographique indépendante,
qui n'a pas été faite ici.

## Réserves sur la présentation et les expériences du dépôt

- Le fichier livré `analysis/theorem_audit.json` porte un autre commit
  (`f439efff…`), une date antérieure et un état de travail modifié. C'est
  un artefact d'audit antérieur, pas une validation indépendante du commit
  présent. Ses descriptions de portée peuvent aussi être dépassées par
  des résultats ultérieurs dans `OrbitSummability.lean`.
- L'absence de `sorry` et d'axiome ajouté dans un scan lexical est un bon
  contrôle préliminaire, pas une compilation. « Sans axiomes » doit aussi
  être distingué de « sans axiomes supplémentaires » : les fondations
  usuelles `propext`, `Classical.choice`, `Quot.sound` peuvent être utilisées.
- `shadow_experiments.py` observe notamment 70 489 ombres pour 116 280 mots
  à \(t=21,j=14\). Cela reste un comptage fini. Le rapport nombre de paires
  observées / produit des supports n'est pas une mesure d'information
  mutuelle : l'échantillonnage et les contraintes de poids limitent déjà
  les paires possibles. Il ne démontre pas une rigidité inter-échelles.
- L'échantillon mécanique de 400 mots donnant 167 ombres contre 400 pour
  l'échantillon aléatoire n'est pas contrôlé pour le nombre de mots distincts,
  la distribution des poids et les répétitions. On ne peut attribuer tout
  cet écart à des collisions 3-adiques supplémentaires.
- `itinerary_inverse.py` vérifie quatre identités rationnelles modulo
  \(2^{512}\). Observer 512 chiffres d'un candidat ne prouve pas que sa
  réalisation 2-adique est, ou n'est pas, un entier ordinaire. Les pentes
  sont aussi approchées en virgule flottante ; ce script ne certifie pas
  un mot mécanique irrationnel infini.

Les journaux et scripts locaux joints permettent de distinguer ce qui a
été effectivement calculé de ce qui reste une lecture ou une proposition.
