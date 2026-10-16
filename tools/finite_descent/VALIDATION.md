# Validation — issue #17

**Verdict : contrôles exécutables validés sur le périmètre décrit.**
Cela ne constitue pas une vérification formelle du programme ni une preuve
de Syracuse.

Base `main` : `f0e1ede43d94ab4d4756223cdccef51e3aa30c7d`.
Python réellement utilisé : 3.12.14, bibliothèque standard, sans dépendance
externe ni import des anciennes expériences.

Commande finale exécutée :

```sh
python3 -m unittest discover -s tools/finite_descent/tests -v
```

Résultat : **23 tests, OK**. Le contrôle CLI de l'exemple principal a aussi
été exécuté séparément :

```sh
python3 tools/finite_descent/verify.py tools/finite_descent/examples/valid_3_4.json
```

Résultat `VALID`, code 0 : six nœuds explicites, trois classes omises vides,
deux entiers certifiés, aucune lacune. Les marges exactes sont :

- n=4, mot 0 : `(2−1)·4−0=4>0`, arrivée 2 ;
- n=3, mot 1100 : `(16−9)·3−5=16>0`, arrivée 2.

Les tests incluent :

- cinq exemples JSON et codes CLI attendus : valide 0, partiel 2, invalide 1 ;
- branche non vide omise et feuille non prouvée → `PARTIAL` ;
- fausse vacuité, mot falsifié, chacun des cinq coefficients/résidu falsifié,
  égalité T⁰(n)=n et feuille expansive → `INVALID` avec diagnostic ;
- contrôle des deux extrêmes affines, omissions vides, déclarations sur
  sous-arbre vide, priorité de l'invalidité sur une couverture partielle ;
- format, intervalles, booleans, flottants, champs inconnus, clés JSON
  dupliquées dont collision de branche, fichier malformé, UTF-8 invalide,
  constantes non finies, limites de fichier, profondeur et nombre de nœuds ;
- 508 intersections de classes comparées à des listes directes ;
- **9 906 comparaisons indépendantes** mot/résidu contre itération de T,
  pour tous les mots de longueur 0–6 et les départs 3–80. Pour les mots
  réalisés, l'identité affine est contrôlée sur l'arrivée calculée directement ;
- 55 petits intervalles dans [3,12] évalués avec **le même arbre de référence**,
  pour contrôler le statut complet/partiel contre les chemins directs.

Une version intermédiaire de la suite a passé 22 tests ; le compte final
23 correspond à la version livrée après ajout du test explicite de collision
de clés enfants et remplacement d'un contrôle positif superflu par celui
de la feuille racine non prouvée. Aucun échec mathématique n'a été masqué.

La preuve générale du [README](README.md) est indépendante des échantillons
finis : classe unique par mot, partition par les deux enfants, extrema de
l'intersection et comparaison affine stricte. Les tests servent à chercher
des défauts d'implémentation, pas à remplacer cette justification.

Aucune recherche d'arbre ou de nouveau certificat, aucun calcul massif et
aucune compilation Lean. Les anciennes suites du dépôt n'ont pas été relancées.
Les exemples négatifs sont des mutations du contrôle fourni ou des entrées
malformées, pas des découvertes sur les orbites.
