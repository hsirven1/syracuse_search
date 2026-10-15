# Décision de recherche : ABANDONNER le candidat comme projet de nouveauté

15 octobre 2026. Revue de la PR [#7](https://github.com/hsirven1/syracuse_search/pull/7),
au commit `191ce7e2476143f80962db5aaad15607ba036092`.
La branche et les fichiers de la PR ne sont pas modifiés par cette revue.

## Portée du verdict

**ABANDONNER comme programme de nouveau théorème ou de nouvelle campagne de
calcul/formalisation.** Aucune contribution scientifique nouvelle n'est
actuellement établie. Le dossier contient une explicitation utile d'un
mécanisme déjà attribué à 1995, une correction de quantification et des
preuves Lean génériques partielles. Ce ne sont pas, à ce stade, des raisons
suffisantes pour prolonger le projet de nouveauté.

Ce verdict est une **décision de recherche**, pas l'affirmation que nous
avons définitivement certifié la preuve historique de 1995. Les sources
primaires restent inaccessibles dans cette exécution. Il serait trompeur
de déclarer « preuve complète en 1995 » ou « lacune nouvelle découverte en
1995 » à partir d'un résumé. Une preuve nouvelle d'un énoncé ancien pourrait
être une contribution ; son absence n'est pas déduite du seul fait que
l'énoncé était déjà affirmé.

## 1. Pièces effectivement lues et pièces manquantes

Lus dans Git :

- [`PRIMARY_SOURCE_PRIORITY.md`](PRIMARY_SOURCE_PRIORITY.md), L14–25
  (transcription et vérification de H rapportées), L29–43 (antériorité et
  conflit de statut), L47–50 (résumé de Nikpour–Rabbani) ;
- [`REPORT.md`](REPORT.md), notamment L146–195 pour le point fixe et
  l'atteinte, sections 4–6 pour projection, relèvement et propagation ;
- [`KLAlgebra.lean`](KLAlgebra.lean), notamment L101–179 : le transport des
  différences et la sommation stricte ;
- le candidat A–E corrigé, au même état que la PR source.

La page HTML publique de la PR #7 a aussi été téléchargée avec succès.
Elle est en brouillon, vise `research/kl-strict-monotonicity-candidate` et
reprend le diagnostic du fichier de priorité. Son corps et le commentaire
bibliographique ne contiennent pas les passages primaires complets.
Ce sont des déclarations du même dossier de recherche, **pas une validation
externe supplémentaire**. L'API GitHub, elle, reste bloquée.

Les copies auteur/publisher de 1995, les copies de 2003 et les pages 2026
ont été demandées directement. Les requêtes échouent par HTTP 403, y
compris un essai de téléchargement de la copie auteur en exécution hors
sandbox. Les métadonnées et la recherche d'errata Crossref sont également
bloquées. Les requêtes et erreurs sont conservées dans
[`priority_logs/`](priority_logs/).

Des citations intégrales ont été demandées. L'utilisateur a fourni deux
citations, dont celle de 1995 avec une ellipse, et des précisions sur la
note et l'équivalence : voir
[`PROVIDED_EXCERPTS.md`](priority_logs/PROVIDED_EXCERPTS.md).
Le texte intégral de la note et des paragraphes d'équivalence manque
toujours. Ces citations fournies et les comptes rendus de lecture sont
distingués d'une extraction que nous aurions vérifiée dans les PDF.

## 2. Les deux affirmations portent-elles sur les mêmes seuils ?

Définir, sans supposer l'atteinte,

\[
S_k^{95}=\{\lambda: L_k^{NT,95}(\lambda)
\text{ possède une solution positive}\},\quad
S_k^{03}=\{\lambda: L_k^{NT,03}(\lambda)
\text{ possède une solution positive}\}.
\]

Le document de priorité rapporte explicitement, L41, une équivalence des
programmes au sens des **mêmes valeurs de λ**, à **niveau k identique**,
dans KL 2003, pp. 240 et 255–256. La réponse de l'utilisateur confirme
que cette équivalence concerne les solutions strictement positives.
Sous cette transcription, on a exactement

\[
S_k^{95}=S_k^{03}\quad\Longrightarrow\quad
\sup S_k^{95}=\sup S_k^{03}.
\]

L'affirmation de 1995 sur \(\lambda^*(L_k^{NT})\) et celle de 2003 sur
\(\lambda_k\) concernent donc **les mêmes seuils sous cette équivalence**.
Le nom de la variable n'est pas la raison : c'est l'identité des ensembles
admissibles. Une borne numérique certifiée ou un exposant arrondi n'est
pas ce supremum exact. Le programme tronqué \(L_k^T\) ne doit pas être
substitué à \(L_k^{NT}\). Le passage à \(\gamma=\log_2\lambda\), strictement
croissant, ne changerait pas le caractère strict de la comparaison.

### Différences qui ne suffisent pas à expliquer le conflit

- **Auxiliaires saturées.** Le minimum des trois coordonnées d'une fibre
  élimine les auxiliaires si les contraintes sont exactement celles
  transcrites à L16–23 du document de priorité.
- **Normalisation et plafond.** Un C_max libre et une normalisation par
  homothétie ne changent pas l'ensemble des paramètres admissibles.
- **Maximum contre supremum.** Ils ont la même valeur si le maximum
  existe ; l'absence d'une preuve d'atteinte peut créer une lacune dans
  l'argument, pas une autre famille de valeurs par simple changement de nom.
- **Positif contre non négatif non nul, dans notre modèle.** Si
  \(0\ne c\ge0\), \(c\le F(c)\), alors les itérés sont croissants et
  \(F(c)\ge aPc\), avec a>0 et P un cycle. La somme
  \(w=\sum_{t=0}^{N-1}F^t(c)\) est strictement positive ; la superadditivité
  donne \(F(w)\ge w\). Ainsi cette différence éventuelle de convention
  ne produit pas deux seuils pour le F étudié. Ce raisonnement ne permet
  pas de présumer quelles conventions figurent effectivement dans chaque PDF.

**Statut exact de cette comparaison :** conclusion logique ferme à partir
de l'équivalence rapportée ; l'authenticité, les qualifications et la
pagination de cette équivalence n'ont pas été contrôlées indépendamment
dans le texte primaire lors de cette mission. La mention « H confirmée »
dans la PR est attribuée à son auteur, pas présentée comme une seconde
lecture indépendante que nous aurions effectuée.

## 3. 1995 : preuve complète, esquisse ou affirmation sans justification ?

Le compte rendu L33 de `PRIMARY_SOURCE_PRIORITY.md` contient trois éléments :

1. l'affirmation explicite de croissance stricte ;
2. un relèvement d'un certificat annoncé non optimal ;
3. une note : à défaut, rigidité par fibres, descente de niveau, puis
   contradiction au niveau 2.

**Classification du passage tel qu'il est rapporté : ESQUISSE de preuve.**
Ce n'est pas une affirmation nue, puisqu'un mécanisme de démonstration
est donné. Mais le résumé ne constitue pas une preuve complète vérifiable.
La précision de l'utilisateur indique que l'analyse d'existence et
d'atteinte n'est pas développée dans la note. C'est une lacune
d'explicitation identifiée dans le passage décrit, pas la démonstration
d'une erreur ou d'une impossibilité de compléter la preuve. Ces
justifications pourraient être fondées sur des résultats précédents de
l'article, que nous n'avons pas pu lire. La classification définitive du
texte intégral reste donc **non tranchée dans cette exécution**.

Les obligations logiques à retrouver dans l'article sont précises :

- disposer d'un certificat positif au seuil, ou contourner son atteinte ;
- déduire d'une fibre non constante une coordonnée de relèvement stricte ;
- transformer ce seul slack en marge sur toutes les lignes ;
- préserver cette marge en augmentant λ ;
- justifier la rigidité et la descente, avec une base traitée séparément.

L'affirmation « le relèvement n'est pas optimal » ne remplace pas à elle
seule ces étapes. En particulier un slack dans une seule contrainte n'est
pas, pour un programme quelconque, une preuve que l'on peut améliorer le
paramètre. Réciproquement, ces étapes peuvent être assez courtes pour
former une esquisse correcte si leurs hypothèses ont déjà été établies.

Le statut « ouvert » rapporté pour 2003, p. 255, ne constitue pas à lui
seul un erratum de 1995. Il ne dit ni où une preuve échoue ni pourquoi les
auteurs ont changé de présentation. On ne déduit pas une rétractation,
une confusion de seuils ou une lacune d'atteinte sans document explicite.

La citation de 2003 fournie dans la conversation appuie bien cette
qualification « ouvert ». C'est un conflit de **statut documentaire**,
pas une contradiction mathématique P et non-P : « c'est ouvert » n'affirme
pas que les seuils sont égaux ou que la croissance stricte est fausse.
La mention ultérieure de l'atteinte comme condition d'une solution
exponentielle exacte ne prouve pas non plus qu'un supremum n'est pas
atteint. Elle ne désigne pas à elle seule l'erreur historique supposée.

## 4. Comparaison d'A–E avec le mécanisme de 1995

| Partie de notre dossier | Mécanisme attribué à 1995 | Apport démontré de notre rédaction |
|---|---|---|
| A : cycle de multiplication par 4 | Non détaillé dans le compte rendu de la note | Justification LTE explicite d'une irréductibilité particulière, pas une notion nouvelle. |
| B : point fixe, positivité, continuité, atteinte | Le compte rendu ne précise pas ces étapes | Un argument fini de Brouwer/PF et une borne uniforme empêchant la limite sur la frontière. Développement réel de la justification ; nouveauté historique non établie. |
| C/P : projection et rigidité par fibres | Présentes dans le résumé de la note | Formule exacte de projection et traitement du bord k=2. |
| D : relèvement non constant donc slack | Cœur explicitement anticipé | Détail des indices et de la bijection de la branche 2 modulo 9. |
| E : propagation puis augmentation de λ | Nécessaire pour rendre « non optimal » rigoureux | Développement du pont logique, avec preuves Lean génériques partielles. |
| Induction finale | Descente vers le niveau 2 explicitement anticipée | Mise en ordre des dépendances et des hypothèses. |

Ces ajouts ont une valeur de **vérification et d'explication**. Ils ne
suffisent pas à établir une contribution mathématique originale : le
compte rendu ne dit pas que ces éléments sont absents de 1995, ni qu'aucun
texte postérieur ne les traite. À l'inverse, l'ancienneté de l'énoncé seule
ne permet pas de nier la valeur possible d'une nouvelle preuve complète.
La bonne conclusion est « contribution nouvelle non établie », non
« absence de contribution nouvelle démontrée ».

L'apport technique réel d'A–E ne doit donc pas être effacé : il donne
explicitement une voie d'existence positive, d'atteinte et de propagation
que la note, selon la réponse fournie, ne développe pas. Ce pourrait être
une complétion utile d'une esquisse ancienne. Mais établir que ce serait
la première preuve complète demanderait justement la lecture des
résultats antérieurs et postérieurs manquants. Le caractère classique des
outils n'est pas une preuve d'antériorité de cette application particulière.

## 5. Nouvelle recherche de faille : analyse, sans expérience supplémentaire

### B et l'atteinte

La correction existentielle de B reste nécessaire : le c arbitraire
(1,2,1) à k=2, λ=1 n'est pas admissible, alors que (3,2,3) l'est
strictement. C'est le contre-exemple exact déjà documenté, pas un nouveau
calcul lancé ici.

Pour la version corrigée, l'argument de point fixe reste cohérent : F
normalisé agit continûment sur le simplexe ; le cycle et a>0 rendent le
vecteur propre strictement positif ; la comparaison de rapports donne
l'unicité de la valeur propre. La borne déjà justifiée
\(\min v_i\ge14^{-(N-1)}/N\) empêche la perte de positivité lorsque λ varie
dans [1,2]. Elle ferme le passage de compacité. Aucune nouvelle faille
mathématique n'a été identifiée dans cette chaîne pour le F affiché.

Cela ne constitue pas une preuve que l'atteinte était la lacune historique
de 1995 : cette attribution reste une conjecture bibliographique.

### Un slack local n'est pas une marge globale

Le contre-modèle abstrait F(x0,x1)=(2x0,x1), v=(1,1), a un slack local
mais jamais de slack dans sa seconde coordonnée. Il réfute une inférence
générale « un slack suffit » sans irréductibilité. Ce n'est pas un
contre-exemple KL : il ne possède pas le couplage positif sur le cycle
utilisé dans E.

Dans notre modèle, avec \(z_t=F^t(v)\),
\(\delta_t=z_{t+1}-z_t\ge0\), on a
\(\delta_{t+1}\ge aP\delta_t\). La somme des N premières différences est
strictement positive dans toutes les coordonnées. La somme des itérés
donne alors un w>0 tel que F(w)>w partout. C'est exactement le pont que
l'on doit chercher dans le contexte du texte de 1995, sans affirmer qu'il
en est absent.

La dépendance en λ n'introduit pas de faille supplémentaire : w est fixé,
il y a un nombre fini de slacks positifs et les coefficients sont
continus. Cela suffit à augmenter λ localement ; aucune monotonie globale
en λ n'est supposée. Le coefficient d croît d'ailleurs avec λ.

### Projection et bords

P est utilisée du niveau k au niveau k−1 uniquement pour k≥3. Les types
modulo 9 restent alors constants entre relèvements. Descendre cette
identité jusqu'au niveau 1 serait incorrect ; la base k=2 est séparée.
Le relèvement strict utilise bien une valeur au-dessus du minimum de sa
fibre et la branche b>0. Aucun usage de tests finis comme preuve
universelle n'est nécessaire dans cet examen.

**Bilan contradictoire :** pas de contre-exemple nouveau à A–E corrigé,
pas de certification de la preuve historique et pas de lemme ouvert
nouvellement identifié. Les hypothèses structurelles des lemmes Lean
restent explicites ; leur compilation antérieure ne prouve pas une
assertion d'antériorité.

## 6. Errata, citations et Nikpour–Rabbani (2026)

Demandés pendant cette mission : copies auteur/éditeur de 1995, copie
de 2003, métadonnées des deux DOI, recherche Crossref contenant les noms
et « erratum correction », page SSRN 7239062 et page ResearchGate indiquée
par la PR. Les accès hors GitHub sont refusés. Par conséquent :

- **Aucun erratum n'est vérifié ici.** Cela ne signifie pas qu'il n'en
  existe aucun ; une recherche bloquée n'est pas un résultat négatif.
- **Aucune chaîne de citations postérieures n'est vérifiée.** La phrase
  de 2003 rapportée dans la PR ne remplace pas cette recherche.
- **Nikpour–Rabbani : texte intégral non lu.** Le dossier lui attribue un
  résumé PF non linéaire, un niveau 20 et l'exposant 0,914947. Ni ces chiffres
  ni une preuve de stricte monotonie ne sont nouvellement certifiés ici.
- **Méthode et résultat doivent rester distincts.** Un résumé annonçant
  PF non linéaire ne suffit pas à attribuer à ces auteurs notre B exact,
  l'atteinte de tous les seuils ou le théorème de croissance stricte.

Références à résoudre dans les textes, et non attestations de lecture :

1. Applegate–Lagarias, *Density Bounds for the 3x+1 Problem II. Krasikov
   Inequalities*, Math. Comp. 64 (1995), 427–438, DOI
   `10.1090/S0025-5718-1995-1270613-2`, section 4 et sa note ;
2. Krasikov–Lagarias, *Bounds for the 3x+1 problem using difference
   inequalities*, Acta Arith. 109 (2003), 237–258, DOI
   `10.4064/aa109-3-4`, section 6, pages imprimées 255–256 selon le dossier ;
3. Nikpour–Rabbani, SSRN 7239062 et ResearchGate 412124726, document daté
   2026 par le dossier ; contenu complet et statut de publication non vérifiés.

## 7. Y a-t-il un unique lemme mathématique à poursuivre ?

**Aucun lemme authentiquement encore ouvert n'a été identifié.** Il n'est
pas justifié d'inventer une nouvelle cible pour prolonger le projet.

Le pont minimal pertinent pour *évaluer l'esquisse rapportée* est :

\[
\lambda<2,\ v>0,\ F_{k,\lambda}(v)\ge v,
\quad\exists i:\ F_{k,\lambda}(v)_i>v_i
\Longrightarrow
\exists\varepsilon>0,\ w>0:\
\lambda+\varepsilon<2,\quad F_{k,\lambda+\varepsilon}(w)\ge w.
\]

Mais ce pont est déjà démontré pour notre modèle par la propagation de E,
la superadditivité et la continuité, comme expliqué ci-dessus et dans le
rapport précédent. Les parties algébriques sont déjà traitées par
`difference_lower`, `strict_after_cycle`, `summed_strictification`.
Il n'est donc **pas proposé comme un lemme nouveau à démontrer**.
L'atteinte nécessaire à l'induction est également traitée par B sur le
modèle. Le problème non résolu de ce dossier est la vérification des
sources et de l'apport historique, pas une lacune mathématique établie.

## 8. Commandes et périmètre de l'exécution

Commandes Git réellement exécutées :

```sh
git ls-remote origin refs/pull/7/head
git fetch origin refs/pull/7/head
git switch -c review/kl-priority-decision FETCH_HEAD
git show FETCH_HEAD:research/kl_review/PRIMARY_SOURCE_PRIORITY.md
```

La page PR a été obtenue par :

```sh
curl -fL --max-time 25 https://github.com/hsirven1/syracuse_search/pull/7 \
  -o /workspace/kl-pr7.html
```

Les requêtes primaires et bibliographiques avec leurs erreurs sont dans
`priority_logs/access_initial.json` et `priority_logs/bibliographic_access.json`.
Les deux liens auteur Michigan ont également échoué, dont un essai hors
sandbox sur `https://websites.umich.edu/~lagarias/doc/applegateII.pdf`.
`gh pr view 7` a échoué sur `api.github.com/graphql`, tandis que le HTML
public a fonctionné.

**Aucun nouveau test numérique, aucune nouvelle expérience, aucune
recompilation Lean et aucun calcul massif n'ont été lancés.** Les six tests
et dix interrogations Lean des rapports précédents sont des résultats
antérieurs réexaminés, pas présentés comme réexécutés.

## Conclusion de décision

Ne pas poursuivre la revendication de nouveau théorème, ni créer une
campagne supplémentaire pour soutenir sa nouveauté. L'énoncé et le
mécanisme sont déjà attribués à 1995 par la PR ; nos détails apportent une
justification plus explicite sans nouveauté historique établie. La
contradiction de statut rapportée en 2003 ne rétablit pas automatiquement
une priorité pour nous. Une nouvelle preuve d'une vieille affirmation
pourrait compter, mais cette contribution n'est pas démontrée ici.

**Verdict : ABANDONNER.** Il s'agit d'un arrêt du projet de nouveauté au vu
des preuves disponibles, avec réserve explicite sur le jugement historique
définitif que les accès bloqués ne permettent pas de rendre.

**Prochaine action unique :** soumettre la comparaison 1995/2003, avec
les passages primaires intégraux, à un spécialiste indépendant.
