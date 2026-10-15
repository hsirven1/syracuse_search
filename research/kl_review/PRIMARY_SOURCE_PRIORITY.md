# Vérification des sources primaires et antériorité (15 octobre 2026)

**Verdict : l'hypothèse H est confirmée pour le programme publié en 2003. En revanche, la croissance stricte avait déjà été explicitement AFFIRMÉE en 1995. Ne pas annoncer un nouveau théorème.**

Ce document complète `research/kl_review/REPORT.md`, qui ne pouvait pas accéder aux PDF. Il ne modifie ni les preuves Lean ni les tests de Codex.

## 1. Contrôle direct du programme linéaire de 2003

Source primaire : I. Krasikov et J. C. Lagarias, *Bounds for the 3x+1 problem using difference inequalities*, Acta Arithmetica 109 (2003), 237–258.
- ArXiv de l'auteur : https://arxiv.org/abs/math/0205002
- PDF de l'article publié : https://scispace.com/pdf/bounds-for-the-3x-1-problem-using-difference-inequalities-56fbm0zt98.pdf
- DOI : https://doi.org/10.4064/aa109-3-4

Lecture effectuée de la page imprimée **240** (formulation générale et L0), **241** (L1–L4, (2.9)–(2.15)), **255** (monotonie et question ouverte), et **256** (équivalence avec Applegate–Lagarias 1995).

Correspondance littérale aux trois branches de `F` de notre candidat :
- `m≡2 (mod 9)` : `c_m ≤ λ^-2 c_(4m) + λ^(α-2) c'_{(4m-2)/3}`.
- `m≡5 (mod 9)` : `c_m ≤ λ^-2 c_(4m)`.
- `m≡8 (mod 9)` : `c_m ≤ λ^-2 c_(4m) + λ^(α-1) c'_{(2m-1)/3}`.
- L4 impose que chaque auxiliaire `c'_u` soit inférieure aux trois représentants principaux de sa fibre. (2.15) définit explicitement la valeur maximale de l'auxiliaire comme le **minimum de ces trois valeurs**.
- Le texte précise que `C_k^max` est libre et ne contraint pas l'existence d'un certificat ; sa valeur peut être choisie égale au maximum des poids principaux. La normalisation `min c_m=1` est obtenue par homothétie.

Cela ferme le blocage **H** : la faisabilité de `L_k^NT(λ)` pour `1≤λ≤2` équivaut bien à l'existence d'un vecteur `c>0` tel que `c≤F_(k,λ)(c)`, avec le même niveau et les mêmes trois coefficients. La réciproque vient du choix des minima comme auxiliaires et de la normalisation. Aucun plafond exogène sur `C^max` ni autre contrainte auxiliaire n'apparaît dans les lignes du LP publiées.

**Limite :** il s'agit d'une vérification mathématique par lecture, pas d'une nouvelle formalisation Lean de l'équivalence avec le document original.

## 2. Antériorité particulièrement importante : Applegate–Lagarias 1995

Source primaire : D. Applegate et J. C. Lagarias, *Density Bounds for the 3x+1 Problem II. Krasikov Inequalities*, Math. Comp. 64 (1995), 427–438.
- Copie de l'auteur : https://math.lsa.umich.edu/~lagarias/doc/applegateII.pdf
- Publication AMS : https://community.ams.org/journals/mcom/1995-64-209/S0025-5718-1995-1270613-2/S0025-5718-1995-1270613-2.pdf

**Section 4, p. 14 du PDF de la copie auteur :** les auteurs écrivent explicitement que `λ*(L_k^NT)` est *strictement croissant* avec `k`, que cela serait facile à prouver en relevant un certificat, et que le relèvement ne serait pas optimal. Leur note de bas de page explique que, sinon, les coefficients devraient devenir constants par fibres, puis constants à tous niveaux, contredisant l'optimalité à `k=2`.

Cela **anticipe le cœur de notre argument de relèvement/projection/rigidité**. Même si le passage est assez succinct, la conclusion et l'idée principale ne peuvent pas être revendiquées comme nouvelles.

## 3. Incohérence publiée en 2003

**Page imprimée 255, section 6 :** Krasikov–Lagarias (2003) écrivent que `λ_k≤λ_(k+1)` et que prouver `λ_k<λ_(k+1)` reste une question ouverte.

**Pages 240 et 255–256 :** ils précisent pourtant que leur programme de 2003 est équivalent, au sens de l'ensemble des valeurs `λ` admettant des solutions positives, au programme `L_k^NT` de 1995. Les deux familles partagent donc les mêmes seuils sous cette notion de faisabilité.

**Diagnostic :** les deux textes contiennent des affirmations apparemment contradictoires. Sans explication ou erratum, il est incorrect de simplement effacer l'énoncé de 1995 et de proclamer que notre preuve résout une question inédite. Le texte de 1995 peut être lu comme un argument esquissé plutôt que comme une démonstration intégrale ; celui de 2003 présente la stricte croissance comme ouverte. Nous ne concluons pas pourquoi les auteurs ont changé de statut. Le rôle de l'**atteinte des seuils** est une piste de compréhension, mais cette explication n'est pas établie historiquement.

## 4. Nikpour–Rabbani 2026

Le résumé public de P. Nikpour et M. Rabbani, *A Certified Density Exponent for the 3x+1 Problem and the Smallest Atom of the Syracuse Random Variable*, est accessible :
https://www.researchgate.net/publication/412124726_A_Certified_Density_Exponent_for_the_3x_1_Problem_and_the_Smallest_Atom_of_the_Syracuse_Random_Variable

Il annonce une approche Perron–Frobenius non linéaire et un certificat `k=20` d'exposant `0.914947`. Le **texte intégral** est indisponible dans cette vérification, et nous ne savons pas s'il fournit une preuve de croissance stricte. Sa méthode de vecteur propre indique clairement une antériorité potentielle du mécanisme de notre lemme B. Il s'agit d'un préprint, pas d'une validation indépendante de ses chiffres.

## 5. Statuts révisés

| Objet | Statut au 15 octobre |
|---|---|
| Équivalence H du candidat avec les LP (L0–L4) de 2003 | **CONFIRMÉE par lecture des sources primaires** |
| Correction du quantificateur de B | **NÉCESSAIRE**, contre-exemple exact connu |
| Argument A–E pour F corrigé | **DÉMONSTRATION MATHÉMATIQUE CANDIDATE**, audit indépendant favorable, non entièrement certifiée Lean |
| Dix lemmes algébriques Lean | **VÉRIFIÉS par Codex**, mais hypothèses structurelles non toutes instanciées |
| Croissance stricte `λ_(k+1)>λ_k` | **DÉJÀ AFFIRMÉE en 1995**, explicitement dite ouverte en 2003 ; conflit bibliographique à résoudre |
| Nouveauté scientifique | **NON ÉTABLIE, forte antériorité** |
| Conjecture de Syracuse | **NON RÉSOLUE** |

**Recommandation : geler les nouvelles expériences et la formalisation massive de la croissance stricte.** Seul un audit externe rigoureux du statut exact de l'argument de 1995, de la différence historique de statut en 2003 et de la valeur ajoutée du point fixe pourrait justifier une note mathématique nouvelle. Aucun merge automatique.
