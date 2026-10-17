# Audit contradictoire de la PR #18 — issue #19

**Verdict : GO POUR REVUE HUMAINE.** Aucun certificat incorrect accepté `VALID`
n'a été trouvé dans le périmètre testé. Aucun correctif de production n'est
proposé. Ce résultat fini ne prouve pas l'absence de toute faille.

Source : [PR #18](https://github.com/hsirven1/syracuse_search/pull/18), commit
`6934f312b62e80d8a7dd93709818c65cfe68bea0`.
Mission : [issue #19](https://github.com/hsirven1/syracuse_search/issues/19).
Branche de revue : `review/issue19-verifier-audit`, issue de cette tête,
avec pour base de PR `tooling/issue17-finite-descent`.

## 1. Recherche de faux VALID et indépendance de l'oracle

L'implémentation, son README, les tests et les cinq exemples ont été examinés.
Les 23 tests originaux ont été relancés **avant** l'ajout de l'audit : tous passent.

Le second vérificateur est
[`independent_oracle.py`](../tools/finite_descent/audit/independent_oracle.py).
Il n'importe aucun module du vérificateur audité, notamment ni `word_data`
ni `intersection`. Sa procédure de décision diffère :

- pour chaque entier d'un petit intervalle, il suit réellement T à travers
  les embranchements du certificat ;
- il partitionne les départs selon la parité de leur état courant, sans calcul
  de classe modulaire ou de premier/dernier représentant ;
- à chaque feuille `descent`, il compare directement T^j(n) et n pour chaque
  départ qui atteint cette feuille ;
- pour contrôler les déclarations facultatives, il calcule D par la somme
  fermée `sum 2^i 3^(nombre d'impairs strictement après i)`, et retrouve le
  résidu en itérant tous les départs 0…2^j−1, sans inversion modulaire ;
- il contrôle également les nœuds explicites vides : un faux coefficient ou
  une fausse déclaration dans une branche vide doit encore être rejeté.

Le domaine d'énumération de l'oracle est volontairement limité à
`3≤N0≤N1≤40`, profondeur ≤8. Les cas qui dépassent ces limites ne sont pas
prétendus vérifiés par cette énumération ; les limites du programme cible
font l'objet de contrôles séparés de rejet.

L'indépendance est **algorithmique**, pas une relecture par un second humain
ou une preuve vérifiée par un autre noyau. Le schéma d'entrée et la politique
`INVALID` prioritaire sur `PARTIAL` restent ceux du format annoncé. Les deux
programmes peuvent encore partager une erreur de spécification ; les contrôles
par itération cherchent surtout une erreur arithmétique ou de couverture.

## 2. Campagne déterministe exécutée

Un seul test de campagne est ajouté, dans le répertoire d'audit, sans modifier
les tests de production :
[`test_adversarial.py`](../tools/finite_descent/audit/test_adversarial.py).

| Phase | Certificats comparés au second oracle |
|---|---:|
| Cinq exemples de la PR #18 | 5 |
| Tous les 403 arbres de profondeur ≤2, trois types de feuilles, omissions permises, sur 14 intervalles | 5 642 |
| Arbres pseudo-aléatoires adverses, profondeur ≤8, graine fixée `190018` | 1 000 |
| Arbre de référence entièrement annoté avec les données indépendantes | 1 |
| Coefficients q/A/D/module/résidu falsifiés aux six nœuds | 30 |
| Mots falsifiés ou de type invalide | 24 |
| Remplacements adverses des nœuds | 42 |
| Déclarations sur les trois branches vides du contrôle | 12 |
| Tous les mots de longueur 0–6, huit départs frontières singleton | 1 016 |
| Résidus falsifiés pour ces 127 mots | 127 |
| Schémas et intervalles malformés | 14 |
| **Total comparé** | **7 913** |

Le recensement des 403 arbres est exhaustif **uniquement** pour cette petite
famille : une feuille a l'un des trois types `descent`, `empty`, `unproved` ;
un nœud `split` a chacun de ses enfants absent ou issu de la famille du niveau
précédent. Les 14 intervalles sont les dix singletons 3…12, puis [3,4], [3,8],
[4,9], [9,12]. Ce n'est pas l'exhaustivité de tous les JSON possibles.

Résultats : **706 VALID, 3 736 PARTIAL, 3 471 INVALID** ;
**zéro désaccord de statut et zéro faux VALID**. Pour chacun des 706 VALID,
l'oracle vérifie aussi que la liste des départs arrivés à une feuille de descente
est exactement l'intervalle, une fois chacun, et que le compteur d'entiers
certifiés du programme cible est correct.

Le contrôle [3,4] reste accepté : 4 suit `0` et arrive à 2 ; 3 suit `1100`
et arrive à 2. Les omissions vides 10, 111, 1101 sont distinguées des omissions
non vides. Les arbres synthétiques sont des entrées adverses d'un test logiciel,
pas une recherche de nouveau certificat mathématique ou de théorème Collatz.

### Limites de ressources et CLI, contrôles distincts

Trois cas API attendus `INVALID` : extrémité dépassant 256 bits, chaîne de
splits dépassant la profondeur 128, arbre dépassant 4 096 nœuds explicites.
Ces contrôles ne reposent pas sur l'oracle énumératif.

Quatorze invocations CLI : neuf entrées malformées ou hors limites et les cinq
exemples. Les neuf adversaires comprennent les doublons de clés racine,
enfants et correction, NaN/Infinity, JSON tronqué, nombre entier textuel de
5 000 chiffres, imbrication JSON de 1 100 niveaux, fichier >1 000 000 octets.
Ils retournent tous `INVALID` / code 1, sans traceback et avant le timeout de
5 secondes. Les exemples retournent les codes attendus 0, 2 ou 1.

## 3. Analyse des classes de défauts

| Classe recherchée | Conclusion dans le périmètre testé |
|---|---|
| Faux VALID : n non couvert, couvert deux fois ou ne descendant pas | Aucun trouvé ; comparaison directe de tous les départs de chaque certificat petit |
| Erreur affine ou ordre des bits | Aucune divergence ; correction fermée indépendante et arrivées directes |
| Résidu ou extrêmes d'intervalle erronés | Aucune divergence sur les frontières et arbres testés ; l'oracle n'utilise pas d'extrêmes modulaires |
| Mot déclaré distinct du chemin | Rejet correct, y compris quand la classe est vide |
| Fausse vacuité / correction falsifiée | Rejet correct ; aucune confiance dans les déclarations |
| Descente non stricte, profondeur zéro | Rejet correct du mot vide non vide, marge nulle ; pas de faux succès |
| Omission non vide ou feuille non prouvée | PARTIAL correct, sortie CLI non nulle ; ce n'est pas une réfutation de descente |
| Faux INVALID / faux PARTIAL sur l'interface prise en charge | Aucun désaccord avec l'oracle dans les 7 913 comparaisons |
| Disponibilité / entrée malformée | Aucun crash ni timeout sur les cas exécutés ; pas de garantie générale de temps ou mémoire |

La revue statique est cohérente avec les observations : A est impair, donc
le résidu est défini modulo 2^j ; les enfants partitionnent le parent ;
les déclarations sont comparées avant le traitement d'une classe vide.
La marge `(2^j−A)n−D` est minimisée en premier représentant si son coefficient
est positif, en dernier s'il est négatif ; une marge ≤0 rejette. Le cas nul
est également rejeté pour une feuille non vide.

La sûreté concerne les certificats JSON chargés avec le chargeur prévu. Les
objets Python personnalisés avec méthodes surchargées, les structures mutables
concurrentes et les fichiers/processus hostiles hors du contrat ne sont pas
une classe d'entrées couverte par cet audit. Les limites annoncées sont des
limites de taille, pas un budget universel de CPU pour tout environnement.

## 4. Reproduction et fichiers inchangés

Commandes réellement exécutées, Python 3.12.14, bibliothèque standard :

```sh
python3 -m unittest discover -s tools/finite_descent/tests -v
python3 -m unittest discover -s tools/finite_descent/audit -v
```

- Suite existante : **23 tests, OK**.
- Nouvelle campagne : **1 test déterministe, OK**, avec les compteurs
  `AUDIT_RESULT` imprimés dans la sortie.
- Aucun calcul massif, aucune compilation Lean, aucune recherche Syracuse.

Le script de campagne importe le programme cible uniquement pour appeler
`verify` ; les invocations CLI utilisent son exécutable. Le module oracle
est séparé et ne dépend pas des fonctions arithmétiques de ce programme.

Comparaison binaire avec la base PR #18 : `verify.py`, le README, le fichier
des 23 tests et les cinq exemples JSON sont identiques (**8 fichiers**).
Aucun correctif ni test de régression de production n'est ajouté puisqu'aucune
faille n'est reproduite. Les seuls ajouts sont ce rapport et les deux fichiers
de l'oracle/campagne dans `tools/finite_descent/audit/`.

## Publication

Les trois fichiers de cette revue ont été committés et poussés sur
`review/issue19-verifier-audit`. Les contrôles de diff indexé et depuis la
base passent. La commande suivante a réellement été tentée :

```sh
gh pr create --repo hsirven1/syracuse_search \
  --base tooling/issue17-finite-descent --head review/issue19-verifier-audit \
  --draft \
  --title 'Audit contradictoire PR #18 : oracle indépendant et recherche de faux VALID' \
  --body-file /tmp/issue19-pr-body.md
```

Résultat : `Post "https://api.github.com/graphql": Forbidden`.
**Aucune PR créée par cet accès ; aucune fusion.**
[Comparateur GitHub](https://github.com/hsirven1/syracuse_search/compare/tooling/issue17-finite-descent...review/issue19-verifier-audit?expand=1).
Le corps tenté résumait le verdict, les 23 tests relancés et la campagne de
7 913 comparaisons décrits dans ce rapport.

## 5. Décision

**GO POUR REVUE HUMAINE**, sans fusion automatique. Ce verdict porte sur la
qualité du dossier de revue et les contrôles exécutés, pas sur une preuve
formelle de correction du logiciel ni sur Syracuse. Aucun contre-exemple
à minimiser ou correctif de production n'a été identifié.

**Prochaine action unique :** demander à l'assistant GitHub connecté d'ouvrir
la PR brouillon de `review/issue19-verifier-audit` vers
`tooling/issue17-finite-descent`, pour présenter cet audit à la revue humaine.
