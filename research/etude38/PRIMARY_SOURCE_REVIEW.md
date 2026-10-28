# Étude 38 : vérification primaire des travaux Rozier–Terracol (complément)

15 octobre 2026. Ce complément est une lecture **nouvelle et indépendante** des textes en accès libre ; il ne change pas rétroactivement ce que Codex a pu lire pendant son audit. L'étude 38 garde le verdict **ARRÊT**, aucun lemme original retenu.

## Accès confirmé

- **Texte intégral HTML officiel, auteurs, v5 (17 mai 2026)** : https://arxiv.org/html/2502.00948v5
- **PDF intégral des auteurs, v5 (17 mai 2026)** : https://arxiv.org/pdf/2502.00948v5
- **Fiche arXiv avec historique des cinq versions et référence du journal** : https://arxiv.org/abs/2502.00948
- **Article publié, référence de l'éditeur** : https://doi.org/10.1016/j.disc.2026.115167 ; *Discrete Mathematics* 349 (2026), article 115167.

**Restriction :** le PDF des auteurs v5 n'est pas le PDF final mis en page par l'éditeur. Il constitue néanmoins un texte primaire complet des auteurs, explicitement rattaché à la publication. La comparaison mot à mot avec le fichier définitif Elsevier n'a pas été faite et ne doit pas être prétendue. Ne pas republier le PDF dans un dépôt GitHub public : utiliser les URL vers l'hébergement officiel.

## Comparaison des résultats de notre étude 38 à la source originale

1. **Définition 1.1** : les trajectoires paradoxales pour la fonction raccourcie `T` satisfont `3^q<2^j`, `T^j(n)>=n`, `n>2`. C'est exactement l'événement examiné par notre étude 38.
2. **Identité (2)**, introduction : `T^j(n)=(3^q/2^j)n+E_j(n)`. Avec `D(w)=2^j E_j(n)`, la décomposition est celle de notre audit.
3. **Lemme 2.3 / théorème 2.4** : comparaison des corrections par ordre partiel sur les mots de parité, et borne `E_j(n) <= (3^q-2^q)/2^q`, atteinte uniquement par le mot `0^(j-q)1^q`. Notre borne `D(w)<=2^(j-q)(3^q-2^q)` en découle exactement par multiplication par `2^j`. La source est **le théorème 2.4**, et non un « théorème 2.2 » : la définition 2.2 introduit l'ordre partiel.
4. **Théorème 4.2**, avec corollaires 4.3 et 4.4 : contrainte de `E/n` et du ratio `q/j` à l'aide de la moyenne harmonique `h` des états impairs ; c'est le même mécanisme AM-GM que celui recomposé par Codex.
5. **Section 5 et annexe C** : exactement cinq trajectoires paradoxales de longueur `j=8`, `q=5`, commencées à `n=7,9,18,19,25`. Correspondance avec `research/etude38/results.json` pour les longueurs jusqu'à 12. Le texte des auteurs évoque au total 593 trajectoires dans la plage étudiée et des résultats conditionnels distincts sur l'ensemble global.
6. **Théorème 3.2** : lien entre temps d'arrêt infini et infinité de trajectoires paradoxales ; les affirmations d'une finitude globale restent conjecturales. Rien dans le travail de Codex ne démontre cette finitude ni Syracuse.

## Portée scientifique

Le blocage documentaire principal pour les bornes utilisées et la classification `j=8` est levé par lecture du **texte intégral des auteurs v5**. Le PDF éditeur demeure non inspecté, mais cette réserve ne justifie plus de demander à l'utilisateur de fournir manuellement un PDF dans l'issue #9. Le verdict **ARRÊT de la piste « couplage correction–résidu »** est renforcé ; aucune antériorité nouvelle ou preuve de Syracuse n'est revendiquée.

Liens primaires directs suffisamment explicites pour être réutilisés par Codex sans nouvel essai HTTP 403 :
- https://arxiv.org/html/2502.00948v5#S2
- https://arxiv.org/html/2502.00948v5#S4
- https://arxiv.org/html/2502.00948v5#A3
