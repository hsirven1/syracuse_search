# Exécutions et reproductibilité

Commit du dépôt externe : `ec8174b567d5cab4960024782210b5f5db02bd3a`.
Les journaux se rapportent à cette copie. Le rapport critique est dans
[RAPPORT.md](RAPPORT.md).

## Vérifications terminées

| Vérification | Résultat | Journal |
|---|---|---|
| Tests Python sélectionnés, premier groupe | 25 réussis, 0 échec | [python_tests.log](logs/python_tests.log) |
| Tests Python sélectionnés, second groupe | 18 réussis, 0 échec | [python_tests_extended.log](logs/python_tests_extended.log) |
| Contrôles indépendants en entiers exacts | Tous réussis ; 97 394 cas comptabilisés dans huit catégories | [controles_independants.json](logs/controles_independants.json) |
| Expériences d'ombres 3-adiques du dépôt | Exécution terminée, code de sortie 0 ; exploratoire | [shadow_experiments.log](logs/shadow_experiments.log) |
| Inversion d'itinéraires du dépôt | Exécution terminée, code de sortie 0 ; quatre contrôles rationnels affichent `True` | [itinerary_inverse.log](logs/itinerary_inverse.log) |
| Scan des 95 fichiers Lean principaux | Aucun token `sorry`, `admit`, `axiom`, `unsafe`, `native_decide`, `implemented_by`, `extern` après retrait lexical des commentaires et chaînes | [provenance.json](logs/provenance.json) |
| Compilation Lean ciblée | 16 modules demandés et leurs dépendances : succès, code 0 | [lean_build.log](logs/lean_build.log) |
| Signatures et axiomes | 39 énoncés retrouvés ; requête Lean terminée, code 0 ; uniquement les fondations usuelles ou aucun axiome | [lean_axioms.log](logs/lean_axioms.log), [lean_result.json](logs/lean_result.json) |

Le scan n'est pas un parseur Lean. Les expériences ne constituent pas des
preuves sur les limites infinies. Les contrôles indépendants portent sur :
identité affine (8 191 cas), transport des cylindres et congruence des ombres
(32 764), cocycle (16 281), bijection des parités (13 profondeurs de 0 à 12),
obstruction inverse (1 767), formule de Mersenne (5 150), équivalence entre
mot réalisé et divisibilité (33 215), borne de compression (13 profondeurs).
Plusieurs assertions sont vérifiées par cas ; ce ne sont pas 97 394
théorèmes ou tests unitaires indépendants.

Commandes effectivement exécutées depuis `/workspace/collatz/analysis` :

```sh
python3 -m unittest -v test_parity_complexity test_theorem_audit \
  test_correction_decode test_paradoxical_pruned test_orbit_packing \
  test_ideal_barrier test_nc_collision_search
python3 -m unittest -v test_residue_correction test_sibling_correction \
  test_nc_correction_envelope test_paradoxical_cylinders test_research_certificates
```

Depuis `/workspace/collatz` :

```sh
python3 analysis/shadow_experiments.py
python3 analysis/itinerary_inverse.py
```

Depuis n'importe quel répertoire :

```sh
python3 /workspace/syracuse_search/audit_collatz/controles_independants.py
```

## Installation Lean et compilation

Lean n'était pas installé. Elan a été installé dans `/workspace/.elan`.
Le téléchargement automatique de la version prescrite a reçu un refus
HTTP 403 pour `releases.lean-lang.org`. L'archive officielle identique a
été récupérée avec vérification TLS depuis :

`https://github.com/leanprover/lean4/releases/download/v4.27.0-rc1/lean-4.27.0-rc1-linux.tar.zst`

SHA-256 local de traçabilité (pas une comparaison à un digest publié tiers) :
`0de337b3420f5bc5260bbf396beb8431fe18cb447534b1831966550b253a8832`.

```sh
tar --zstd -xf /workspace/lean-4.27.0-rc1-linux.tar.zst -C /workspace
ELAN_HOME=/workspace/.elan /workspace/.elan/bin/elan toolchain link \
  leanprover/lean4:v4.27.0-rc1 /workspace/lean-4.27.0-rc1-linux
```

Premier échec du cache : écriture interdite dans `/home/agent/.cache/mathlib`.
Correction : `XDG_CACHE_HOME=/workspace/.cache`, sans modifier `HOME`.
Deuxième échec : refus réseau du cache Azure ; aucune dépendance Mathlib
précompilée téléchargée dans cet essai. L'essai a été interrompu.
Voir `mathlib_cache.log` et
`mathlib_cache_retry.log`.

Une reconstruction depuis les sources a été lancée. Après environ 500
tâches de dépendances, elle a été interrompue avec SIGINT lorsque l'accès au
cache est devenu fonctionnel : code sous-processus `-2`, **aucune validation
des théorèmes ciblés par cet essai**. Sa fermeture transitive d'imports
représente environ 7 800 modules. Journaux conservés :
`lean_build_source_interrupted.log`,
`lean_result_source_interrupted.json`.

Le seul domaine ajouté au brouillon réseau est
`lakecache.blob.core.windows.net` ; les préréglages et la liste des dépôts
ont été préservés. L'enregistrement du brouillon a été confirmé par l'outil,
avec `requires_publish: true`. Un accès ultérieur a reçu une réponse Azure
404 sur la racine, puis le téléchargement des objets du cache a réellement
commencé. Cela établit l'accès courant, pas une publication de l'environnement.
Pour rendre la configuration durable, revoir et enregistrer le brouillon
dans les paramètres, puis publier l'environnement selon l'interface.

La reprise utilise le manifeste existant, sans `lake update` :

```sh
cd /workspace/collatz/lean
ELAN_HOME=/workspace/.elan XDG_CACHE_HOME=/workspace/.cache \
  /workspace/.elan/bin/lake exe cache get
PATH=/workspace/.elan/bin:$PATH ELAN_HOME=/workspace/.elan \
  XDG_CACHE_HOME=/workspace/.cache LEAN_NUM_THREADS=4 \
  python3 /workspace/syracuse_search/audit_collatz/verifier_lean.py /workspace/collatz
```

Le script sélectionne 16 modules couvrant les trois thèmes et les précautions
arithmétiques du rapport, puis émet `#check` et `#print axioms` pour 39 énoncés.
Les autres modules de l'application, notamment les gros certificats KL13/KL14,
ne sont pas la cible de cet audit. Le cache Mathlib contient des preuves
précompilées de dépendances ; leur noyau n'est pas rejoué indépendamment.

**Compilation ciblée réussie.** Le téléchargement final a récupéré et décompressé
les 7 764 objets demandés, puis `lake build` s'est terminé avec succès
(`Build completed successfully (7817 jobs).`). Ces 7 817 tâches comprennent
des dépendances issues du cache ; ce nombre ne signifie pas que Mathlib
entier a été reconstruit depuis les sources.
Les sources locales des modules Collatz nécessaires ont été compilées.
Les avertissements observés sont des diagnostics de lint (variables inutilisées,
suggestion `simp`, nom de lemme déprécié), sans erreur de compilation.

Les 39 requêtes `#print axioms` ont été retrouvées, sans déclaration manquante.
Les ensembles d'axiomes observés sont : ensemble vide,
`{propext, Quot.sound}` et `{propext, Classical.choice, Quot.sound}`.
Aucun `sorryAx`, axiome spécifique à Syracuse ou axiome de calcul natif
n'apparaît dans les dépendances de ces 39 énoncés. Cette conclusion vaut
pour les déclarations ciblées et leurs dépendances, pas pour tous les
fichiers du dépôt ou toutes les affirmations de ses textes.

Voir l'[index des déclarations](INDEX_SOURCES.md), la [requête Lean exécutée](Audit.lean)
et le [résultat structuré](logs/lean_result.json). Le cache final est documenté
dans `mathlib_cache_final.log`.

## Éléments non vérifiés

- Le test de complexité annoncé pour l’expérience 35 reste non reproduit :
  `complexity_test.py` et ses sorties ne figurent pas dans le ZIP reçu ensuite.
- Pas d'audit complet des 95 modules, des sous-modules bibliographiques,
  de tous les scripts exploratoires ou de toutes les affirmations du README.
- Pas de vérificateur de noyau indépendant, pas de certification du compilateur
  ni d'étude de priorité scientifique.
- Aucun envoi ou changement dans le dépôt externe `msharpe248/collatz`.
  La publication des rapports dans `hsirven1/syracuse_search` est autorisée
  dans la deuxième phase ; voir le bilan de livraison en fin de conversation.


## Comparaison de l'expérience 36 — 15 octobre 2026

L'archive reçue et ses huit entrées sont identifiées dans
[exp36_validation.json](logs/exp36_validation.json) par empreintes SHA-256.
Les entrées originales sont conservées dans `experience36_source/`.
Les scripts ont été lus, puis exécutés dans `/workspace/experience36_replay`,
une copie dédiée : ils écrivent leurs résultats et ne devaient donc pas
écraser les artefacts fournis avant la comparaison. Les essais indépendants
refont aussi les deux générateurs de fichiers dans un répertoire temporaire.

| Vérification de cette phase | Résultat réel | Journal |
|---|---|---|
| `verify_dual_residues.py` | Code 0 ; 390 mots aléatoires, 28 874 congruences, 5 préfixes critiques | [exp36_dual_replay.log](logs/exp36_dual_replay.log) |
| `shadow_height.py` | Code 0 ; 24 lignes calculées | [exp36_height_replay.log](logs/exp36_height_replay.log) |
| `test_oscillations.py` | Code 0 ; contrôles directs N=100,300,1000 ; pas un test de complexité en facteurs | [exp36_oscillations_replay.log](logs/exp36_oscillations_replay.log) |
| Comparaison des artefacts | `results.json` et les deux CSV identiques par lecture structurée | [exp36_independent.log](logs/exp36_independent.log) |
| Suite indépendante | 8 tests réussis, 0 échec, 0 erreur | [exp36_independent.json](logs/exp36_independent.json) |
| Toutes les suffixes et identités rationnelles | 208 744 cas, deux réalisations par mot ; alphabet {1,2,3,4}, longueurs 1 à 6 | Même journal structuré |
| Hauteur et redondance | 22 450 cas à déficits admissibles, mots sur {1,2} jusqu'à longueur 9 | Même journal structuré |
| Traduction du mot critique en parités raccourcies | 177 indices contrôlés ; effet de bord initial testé | Même journal structuré |
| Piste quantitative non prouvée | 24 dates de saut testées, jusqu'à J_24=4096 ; aucune réfutation finie trouvée | Même journal structuré |
| Trois lemmes Lean locaux | Code 0 ; `exact_suffix`, `suffix_congruence`, `correction_closed` | [exp36_lean.log](logs/exp36_lean.log) |
| 39 requêtes Lean amont relancées | Code 0 ; aucune déclaration manquante ; fondations usuelles seulement | [exp36_upstream_axioms.log](logs/exp36_upstream_axioms.log) |
| Sources amont | Les 95 empreintes de la première phase sont inchangées | [exp36_validation.json](logs/exp36_validation.json) |

Les comptes de cas regroupent plusieurs assertions ; ce ne sont pas des
centaines de milliers de tests unitaires indépendants. Les 43 tests Python
initiaux **n'ont pas été relancés** lors de cette phase. Les 39 requêtes
amont réutilisent les modules compilés du même commit ; elles ne prétendent
pas à une nouvelle reconstruction propre de Mathlib ou à un second noyau.

Commandes de reproduction depuis la racine de `syracuse_search` :

```sh
python3 audit_collatz/test_experience36.py
# Optionnel : ajouter --zip /chemin/vers/archive.zip pour recalculer son empreinte.
```

Pour rejouer les scripts livrés sans toucher leurs artefacts originaux :

```sh
mkdir -p /tmp/exp36-replay
cp audit_collatz/experience36_source/*.py /tmp/exp36-replay/
python3 /tmp/exp36-replay/verify_dual_residues.py
python3 /tmp/exp36-replay/shadow_height.py
python3 /tmp/exp36-replay/test_oscillations.py
```

Depuis `/workspace/collatz/lean`, avec la toolchain et les dépendances de
la première phase déjà installées :

```sh
PATH=/workspace/.elan/bin:$PATH ELAN_HOME=/workspace/.elan \
  lake env lean /workspace/syracuse_search/audit_collatz/Experience36.lean
PATH=/workspace/.elan/bin:$PATH ELAN_HOME=/workspace/.elan \
  lake env lean /workspace/syracuse_search/audit_collatz/Audit.lean
```

Les trois nouveaux lemmes sont des identités conditionnelles sur une
récurrence entière ; ils ne formalisent pas l'ensemble de la comparaison,
la caractérisation complète des mots accélérés ou l'exclusion du mot
oscillant. Le lien aux inverses modulaires est explicité dans le rapport.
Leurs axiomes sont `propext`, `Classical.choice`, `Quot.sound`, sans `sorryAx`.

Les journaux verbeux d'installation et de téléchargement de la première
phase restent locaux et sont exclus de Git par `.gitignore`. Les journaux
courts de preuves, tests, empreintes et les petites entrées de l'expérience
sont versionnés ; aucune archive de toolchain, cache ou gros résultat n'est
publiée. Base distante de la branche d'audit :
`137fc89677642209b899362ab9c6a328b4a5ee02` (README initial de `main`).

Pour tenter l'ouverture d'une pull request, l'ajout de `api.github.com` a
été enregistré dans le brouillon réseau en préservant
`lakecache.blob.core.windows.net`. Le dernier essai API et le test sans
identifiant ont rencontré un refus du tunnel CONNECT HTTP 403. Ce refus
survient avant une réponse de l'API GitHub et ne démontre pas qu'un nouveau
token est requis. L'authentification Git HTTPS existante est utilisée pour
la publication de la branche. La création effective d'une PR ne sera
annoncée que si elle est confirmée ; l'ajout de domaine reste à revoir,
enregistrer et publier dans les paramètres si nécessaire.
