# Vérificateur exact de certificats finis de descente

Livraison de [l'issue #17](https://github.com/hsirven1/syracuse_search/issues/17).
Python 3.10+ et bibliothèque standard uniquement. Aucun code du dépôt Lean
externe n'est importé. Il n'y a ni générateur de certificats ni recherche d'orbites.

```sh
python3 tools/finite_descent/verify.py tools/finite_descent/examples/valid_3_4.json
python3 -m unittest discover -s tools/finite_descent/tests -v
```

L'application est **raccourcie** : T(n)=n/2 si pair, (3n+1)/2 sinon.
Un bit décrit la parité **avant** le pas correspondant, dans l'ordre temporel.
`1100` décrit donc 3 → 5 → 8 → 4 → 2, en quatre pas.
Le Syracuse accéléré sur les seuls impairs n'est pas utilisé.

## Format JSON, version 1

L'objet racine a exactement trois champs :

```json
{
  "version": 1,
  "interval": [3, 4],
  "tree": {"kind": "split", "children": {}}
}
```

Ce petit exemple de format **ne certifie rien** : ses branches non vides
manquent et le résultat est `PARTIAL`. Utiliser le fichier
[`valid_3_4.json`](examples/valid_3_4.json) pour le certificat positif.
L'intervalle est fermé et doit satisfaire 3 ≤ N0 ≤ N1.

Chaque nœud porte `kind` parmi :

| Kind | Sens | Champs supplémentaires |
|---|---|---|
| `split` | Examiner le bit suivant | `children`, objet dont les seules clés possibles sont `0` et `1` |
| `descent` | Vérifier la descente pour toute l'intersection | Aucun |
| `empty` | Affirmer une intersection vide, vérifiée par arithmétique | Aucun |
| `unproved` | Classe laissée non certifiée | Aucun |

Tous les nœuds peuvent ajouter :

- `word` : chaîne qui doit être **exactement le chemin** depuis la racine.
  Si absent, le chemin fait toujours autorité. Aucun mot indépendant du chemin
  ne peut changer une classe.
- `claims` : objet facultatif contenant tout sous-ensemble de `q`, `A`, `D`,
  `modulus`, `residue`. Ce sont des déclarations contrôlées, jamais des entrées
  utilisées pour les calculs. Tous les coefficients sont recomposés du mot.

À la racine le chemin est vide. À un enfant de clé b il devient `chemin+b`.
Une feuille ne peut avoir d'enfants. Les nœuds terminaux sont donc sans relation
préfixe entre eux. Les champs inconnus, valeurs numériques non entières,
booleans à la place d'entiers et clés JSON dupliquées sont rejetés.
Les nombres JSON non finis (`NaN`, etc.) sont également rejetés.

Une branche omise est recalculée : si elle est vide dans l'intervalle,
l'omission est justifiée ; sinon le résultat est partiel avec un témoin.
Les nœuds explicites, y compris vides, sont contrôlés : une déclaration
falsifiée dans un sous-arbre vide n'est pas ignorée.

## Résultats et codes de sortie

| Statut JSON | Code CLI | Portée |
|---|---:|---|
| `VALID` | 0 | Pour chaque entier de l'intervalle, une unique feuille prouve une descente stricte |
| `PARTIAL` | 2 | Pas de falsification détectée, mais une classe non vide manque ou est `unproved` |
| `INVALID` | 1 | Format, limites, déclaration fausse ou preuve de descente échouée |

Une invalidité domine les éventuels trous de couverture. `INVALID` signifie
que **le certificat fourni** est rejeté ; cela ne réfute pas la descente d'une
orbite à un autre horizon. `PARTIAL` n'est jamais un succès global.
Chaque diagnostic précise son chemin et, lorsque pertinent, un entier témoin.
Les compteurs de classes sont informatifs ; seul le statut final fait autorité.
Pour `VALID` le nombre d'entiers certifiés doit égaler N1−N0+1.

Limites annoncées : fichier ≤1 000 000 octets, extrémités ≤256 bits,
profondeur ≤128, nœuds explicites ≤4096. Le nombre d'entiers de l'intervalle
n'est pas parcouru ; un intervalle large dans ces limites peut être traité
arithmétiquement. Dépasser une limite produit `INVALID`, jamais `PARTIAL` ou
une affirmation de non-descente. Le CLI intercepte aussi les erreurs de lecture,
décodage et profondeur du parseur JSON. Utiliser le CLI ou `load_certificate`
puis `verify` pour bénéficier du contrôle des doublons JSON et de la taille ;
un dictionnaire Python déjà construit a naturellement perdu ces informations.

## Justification mathématique de la correction

### 1. Identité et réalisation d'un mot

Pour un préfixe w de longueur j, le vérificateur compose des entiers
M=2^j, A=3^q et D≥0 tels que

`M T^j(n)=A n+D` pour tout départ réalisant w.

À la racine : (M,A,D)=(1,1,0). Ajouter 0 donne (2M,A,D).
Ajouter 1 donne (2M,3A,3D+M). Ces règles résultent directement des deux
branches de T ; elles fixent notamment les puissances de 2 dans D.

La réalisation de w est **équivalente** à `M | A n+D`. Preuve par induction :
pour un préfixe réalisé, poser y=(A n+D)/M=T^j(n).
La congruence de l'enfant 0 équivaut à y pair ; celle de l'enfant 1 à
`3y+1` pair, donc y impair. Réciproquement la congruence d'un enfant implique
celle de son parent : pour l'enfant 1, utiliser que 3 est premier à M.
On remonte donc à la racine et l'induction impose tous les bits.

Puisque A est impair, il est inversible modulo M. Le mot correspond à
**une unique classe**

`n ≡ r = −D A⁻¹ (mod M)`, avec 0 ≤ r < M.

Les deux enfants d'un préfixe partitionnent exactement sa classe en deux
classes modulo 2M, distinguées par la parité de y. Les chemins de l'arbre
imposent ainsi couverture et absence de collisions sans dépendre de résidus
ou de coefficients déclarés par l'auteur du certificat.

### 2. Intersection avec l'intervalle

Le premier entier de la classe dans [N0,N1], s'il existe, est
`first=N0+(r−N0) mod M`. Si first>N1, l'intersection est vide.
Sinon le dernier est `last=N1−(N1−r) mod M` et le nombre d'entiers est
`(last−first)//M+1`. Toutes ces opérations sont exactes.
C'est aussi le contrôle appliqué à chaque enfant omis.

### 3. Descente stricte à une feuille

Pour les entiers de la classe, l'identité donne l'équivalence

`T^j(n)<n  ⇔  (M−A)n−D>0`.

Cette expression est affine. Si M−A≥0, son minimum sur l'intersection est
atteint en first ; sinon en last. Une comparaison entière à ce seul extrême
prouve l'inégalité **pour tous** les entiers de la feuille. L'égalité est
rejetée. Au mot vide, M=A=1 et D=0 : la marge est nulle, donc une feuille
non vide ne peut être certifiée à profondeur zéro.

### 4. Conclusion par l'arbre

Partir de la classe racine contenant tout l'intervalle. À chaque embranchement,
les deux classes enfants sont disjointes et couvrent la classe parent.
Une branche omise d'un certificat accepté est vide. Une feuille `empty` est
vide ; une feuille non vide acceptée prouve l'inégalité précédente.
Il n'existe aucune feuille `unproved` non vide dans un résultat `VALID`.
L'induction sur l'arbre montre donc qu'un résultat `VALID` implique, pour
**chaque n∈[N0,N1]**, une unique feuille et un j fini avec T^j(n)<n.
Ce raisonnement dépend de l'implémentation inspectable ; ce n'est pas une
preuve formelle vérifiée par un noyau.

Le domaine est **fini**. Même un succès ne prouve pas Syracuse et ne constitue
pas un horizon de descente uniforme pour tous les entiers au-dessus d'un seuil.
Aucune nouveauté mathématique n'est revendiquée pour ces identités classiques.

## Exemples et contrôle principal

- [`valid_3_4.json`](examples/valid_3_4.json) : mot 0 pour 4 (M=2,A=1,D=0,r=0),
  mot 1100 pour 3 (M=16,A=9,D=5,r=3). Les marges sont 4 et 16.
  Les omissions 10, 111 et 1101 sont arithmétiquement vides dans [3,4].
- [`partial_missing_branch.json`](examples/partial_missing_branch.json) : la
  branche 1 manque, avec le témoin 3 ; `PARTIAL`.
- [`invalid_correction.json`](examples/invalid_correction.json) : correction
  du mot 0 déclarée 1 au lieu de 0 ; `INVALID`.
- [`invalid_nonstrict.json`](examples/invalid_nonstrict.json) : mot vide sur
  [3,3], T⁰(3)=3 ; marge 0 et `INVALID`.
- [`invalid_false_empty.json`](examples/invalid_false_empty.json) : classe
  impaire faussement déclarée vide ; `INVALID`.

Le test indépendant par itération directe est limité aux petits contrôles de
la suite ; il ne sert pas d'algorithme de vérification des certificats.
Les arbres des exemples sont des données de contrôle fournies, pas les résultats
d'une recherche. La réutilisation de cet arbre sur de petits intervalles dans
les tests évalue son verdict ; elle ne cherche pas de nouvel arbre.
