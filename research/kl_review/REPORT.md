# Revue contradictoire du candidat KL : CONDITIONNEL

15 octobre 2026 — branche source `research/kl-strict-monotonicity-candidate`,
PR source [#6](https://github.com/hsirven1/syracuse_search/pull/6).
`git ls-remote` confirme que la branche et `refs/pull/6/head` désignent
`0f28b4d5415e041ac738e0714dc7377756a16526`.
La présente revue ne modifie ni le candidat ni son script.

## Verdict et limite déterminante

**Verdict global : CONDITIONNEL.** La croissance stricte résulte de
l'argument réparé pour **l'opérateur affiché dans le candidat**, sous la
traduction H. Aucun contre-exemple n'a été trouvé à A, C, D ou E dans leur
domaine déclaré. B contient une erreur de quantification littérale,
réparable et compatible avec la preuve rédigée : remplacer son membre
gauche par « il existe un certificat positif ».

**La comparaison directe demandée avec le texte original de KL 2003 n'a
pas pu être effectuée.** Les quatre accès au PDF Michigan, à ses miroirs
arXiv et à SSRN sont refusés par le tunnel réseau HTTP 403. Les domaines
ont été enregistrés dans le brouillon d'environnement, mais cet
enregistrement n'établit pas leur activation ni une publication. Voir
[source_access.json](logs/source_access.json). Les équations (L0)–(L3),
(2.8)–(2.14) et la question attribuée à la p. 24 ne sont donc **pas citées
comme ayant été lues dans l'original**. Le numéro de page doit aussi être
rattaché à une version précise du document.

L'accord avec un programme tiers ne remplace pas cette vérification.
En particulier, les seuils du programme publié et l'antériorité de
Nikpour–Rabbani 2026 restent non établis par cette revue. Il serait
incorrect de présenter le verdict comme « PROUVE pour le problème ouvert
de KL » ou comme une nouveauté scientifique.

Les tests indépendants exacts et dix déclarations Lean examinées renforcent
les étapes algébriques, mais ne formalisent ni le LP original, ni Brouwer,
ni le théorème complet de croissance des seuils.

## Références internes figées

Le [candidat audité](https://github.com/hsirven1/syracuse_search/blob/0f28b4d5415e041ac738e0714dc7377756a16526/research/KL_STRICT_MONOTONICITY_CANDIDATE.md)
et son [script](https://github.com/hsirven1/syracuse_search/blob/0f28b4d5415e041ac738e0714dc7377756a16526/research/kl_strict_monotonicity_audit.py)
sont référencés ci-dessous par leurs numéros de lignes à ce commit.

| Objet | Lignes du candidat | Conclusion de la revue |
|---|---|---|
| Définition de F et H | 30–55 | Élimination correcte pour le schéma de LP explicité ci-dessous ; conformité au papier non vérifiée. |
| A, cycle de multiplication par 4 | 59–63 | Démonstration LTE correcte. |
| B, point fixe, positivité, continuité | 65–90 | Correct après quantification existentielle à L82 et explicitation du passage à la limite. |
| C, impossibilité à 2, projection P | 92–122 | Correct pour F ; P exige bien le niveau supérieur au moins 3. |
| D, relèvement strict | 124–143 | Correct ; la bijection du type 2 modulo 9 assure une stricte coordonnée. |
| E, propagation et marge | 145–168 | Correct en suivant les différences ; l'argument ne nécessite pas la monotonie en λ. |
| Induction sur les seuils | 170–185 | Valide pour F avec B corrigé ; transfert au LP original conditionné par H. |
| Antériorités annoncées | 12–23, 207–212 | Non vérifiées à la source ; ne fondent aucune attribution de priorité ici. |

## 1. Ce que l'élimination des variables auxiliaires démontre exactement

Considérer le schéma suivant, **à comparer encore au papier**, pour
\(M_k=\{m\bmod3^k:m\equiv2\pmod3\}\), \(k\ge2\) :

- Variables principales \(c_m\), variable libre supérieure \(C\), contraintes
  \(1\le c_m\le C\).
- Une variable auxiliaire \(z_u\) par fibre \(u\in M_{k-1}\), avec
  \(z_u\le c_{u+j3^{k-1}}\), \(j=0,1,2\).
- Les trois familles de lignes principales exactement écrites aux L37–42
  du candidat, en remplaçant les minima par les \(z_u\) correspondants.
- Aucun autre couplage contraignant les auxiliaires, ni plafond C fixé
  extérieurement, ni contrainte affine non homogène supplémentaire.

Tous les coefficients auxiliaires sont non négatifs, en fait strictement
positifs sur leur branche. Remplacer chaque \(z_u\) par le minimum de sa
fibre augmente donc tous les membres droits concernés et conserve ses
trois bornes supérieures. Cela prouve LP admissible ⇒ \(c\le F(c)\).

Réciproquement, si \(c>0\), poser \(s=\min_m c_m>0\),
\(\widehat c=c/s\), \(\widehat z_u=\min_j\widehat c_{u+j3^{k-1}}\),
\(\widehat C=\max_m\widehat c_m\). L'homogénéité donne toutes les lignes
et \(1\le\widehat c_m\le\widehat C\). Si une borne auxiliaire
\(z_u\ge1\) fait partie du LP, elle est également satisfaite par ce choix.
Un objectif de minimisation de C ne change pas l'existence d'un point
admissible si C reste une variable libre.

**Points à contrôler dans l'original avant de lever H :** toutes les
variables auxiliaires et leurs éventuels niveaux, sens de chaque inégalité,
liberté de C, domaines des indices, normalisation, définition du seuil et
domaine de λ. Si des auxiliaires subissent d'autres contraintes, ou si C
est un plafond imposé, l'argument de saturation présenté ne suffit plus.

### Indices : reconstruction indépendante

Notre test n'importe aucun code du candidat ou de `msharpe248/collatz`.
Pour les branches 2 et 8, il résout respectivement dans \(M_k\)

\[
3v\equiv4m-2\pmod{3^k},\qquad
3v\equiv2m-1\pmod{3^k}.
\]

Chaque ensemble comporte trois solutions et coïncide avec la fibre du
quotient modulo \(3^{k-1}\). Le quotient est entier sur sa branche ; il
ne faut pas diviser une congruence sans réduire aussi le module.
Le terme principal utilise bien \(4m\bmod3^k\), et non un quotient
au niveau inférieur. Ces calculs contrôlent le modèle candidat, **pas la
fidélité d'une transcription dont la source primaire n'a pas été ouverte**.

## 2. Lemme A : pas de contre-exemple trouvé, preuve correcte

LTE donne \(v_3(4^{3^j}-1)=j+1\), donc l'ordre de 4 modulo \(3^k\)
est exactement \(3^{k-1}\). Comme 2 est inversible modulo \(3^k\),
l'orbite de 2 par multiplication par 4 a cette longueur et reste dans
\(M_k\), qui a précisément cette cardinalité. C'est donc un cycle unique.
Les cycles des niveaux 2 à 7 ont été vérifiés indépendamment.

Il faut suivre la direction du transport : une différence à j agit à
l'étape suivante sur la coordonnée i telle que \(4i=j\). Cette orientation
est prise en compte par les marches dans la formalisation.

## 3. Lemme B : contre-exemple littéral et réparation analytique

### Plus petit contre-exemple recherché à la lecture libre de c

L'affichage L82 dit littéralement
\(c>0\text{ et }F(c)\ge c\iff\rho\ge1\).
Pour un c arbitraire, c'est faux. Au plus petit niveau admis k=2, au plus
petit λ de l'intervalle, λ=1, dans l'ordre \((2,5,8)\) :

\[
c=(1,2,1),\qquad F(c)=(2,1,3).
\]

La ligne 5 viole l'admissibilité. Pourtant \((3,2,3)\) est strictement
admissible, avec image \((5,3,4)\), ce qui entraîne \(\rho>1\) par
l'argument de comparaison. Le test trouve \((1,2,1)\) comme premier
contre-exemple lexicographique sur \(\{1,2\}^3\). Il ne revendique pas
un « plus petit » vecteur rationnel positif, ensemble qui n'est pas bien
ordonné.

**Correction :**

\[
(\exists c>0:\ F(c)\ge c)\quad\Longleftrightarrow\quad\rho\ge1.
\]

La phrase « la réciproque prend c=v » L85–86 indique déjà cette intention.
L'erreur littérale ne réfute donc pas la croissance des seuils.

### Existence, positivité et unicité de la valeur propre

Pour le F affiché, sur le simplexe fermé \(\Delta=\{v\ge0:\sum v=1\}\),
\(\sum F(v)\ge a>0\). La normalisation \(G(v)=F(v)/\sum F(v)\)
est une application continue de \(\Delta\) dans lui-même. Brouwer donne
\(F(v)=\rho v\), avec \(\rho=\sum F(v)>0\).

Si \(v_i=0\), alors \(0=F(v)_i\ge a v_{4i}\), donc \(v_{4i}=0\).
Le cycle de A force tout v à zéro, contradiction. Cette preuve utilise
une **égalité propre** : elle ne s'applique pas automatiquement à un
simple sous-vecteur propre \(v\le F(v)\) sur la frontière.

Si u,v sont deux vecteurs propres strictement positifs, choisir
\(t=\max_i u_i/v_i\), atteint en i. Monotonie et homogénéité donnent
\(\rho_u u_i=F(u)_i\le t F(v)_i=\rho_v u_i\), donc
\(\rho_u\le\rho_v\). Échanger u et v donne l'unicité de la **valeur**
propre positive, sans avoir à supposer la continuité des vecteurs propres.
Le même raisonnement avec un certificat c établit l'équivalence corrigée.

### Passage à la limite : détail absent de la phrase L88–90

Il ne suffit pas de dire « simplexe compact » et de supposer que la limite
des vecteurs strictement positifs reste strictement positive. Voici le
complément qui ferme ce passage pour le modèle.

Sur \(1\le\lambda\le2\), \(a\ge1/4\), et, en sommant les lignes et en
majorant les minima, on peut prendre la borne grossière uniforme
\(\rho\le a+b+d\le7/2\). La relation propre donne
\(v_i\ge(a/\rho)v_{4i}\). Depuis une coordonnée maximale, au moins
\(1/N\), \(N=|M_k|\), le cycle entraîne donc

\[
\min_i v_i\ge\frac{14^{-(N-1)}}{N}>0.
\]

Cette borne est seulement qualitative à grand k ; aucun calcul géant
n'est nécessaire. Toute suite de paramètres convergente admet une
sous-suite de couples propres normalisés convergeant vers un couple
encore strictement positif. La continuité conjointe de F donne une
équation propre à la limite ; l'unicité de la valeur propre identifie
toutes les limites. Ainsi \(\rho(\lambda)\) est continue.

L'ensemble admissible est donc fermé. Il est non vide : à λ=1 le vecteur
constant 1 vérifie \(F(1)\ge1\). Compact dans [1,2], cet ensemble atteint
son supremum. On ne prétend pas ici l'avoir démontré par une simple
exploration numérique de vecteurs propres.

**Attention au paramètre :** le coefficient d augmente avec λ, alors que
a et b diminuent. La monotonie de F en λ ne doit pas être supposée. La
preuve de compacité et le prolongement local de E n'en ont pas besoin.

## 4. C et D : preuves des identités de fibres

### Somme à λ=2

Les m de type 2 modulo 9 donnent, via \((4m-2)/3\), exactement une fois
chaque fibre inférieure. Les m de type 8 font de même avec \((2m-1)/3\).
En coordonnées \(m=2+9r\) et \(m=8+9r\), les indices réduits dans
\(M_{k-1}\) avancent respectivement de 4 et de 2 en coordonnées de classes ;
ces pas sont inversibles modulo \(3^{k-2}\). D'où, exactement,

\[
\sum F(c)=\tfrac14\sum c+
\tfrac94\sum_u\min_j c_{u+j3^{k-1}}\le\sum c.
\]

Si \(F(c)\ge c>0\), toutes les différences de ces sommes sont nulles.
Dans chaque fibre, \(3\min(x,y,z)\le x+y+z\) est une égalité seulement
si les trois valeurs sont égales. Le certificat est donc constant par fibres.

### Projection P : le bord k=2 ne doit pas être ajouté

Pour k≥3, écrire \(c=L e\), et les trois relèvements de m sous la forme
\(m+r3^{k-1}\), r=0,1,2. Le terme principal a la même valeur
\(a e_{4m}\) sur ces trois relèvements. Le type modulo 9 reste constant.

Pour la branche b, le quotient avance de \(4r3^{k-2}\) modulo
\(3^{k-1}\) ; pour d, de \(2r3^{k-2}\). Chaque famille parcourt exactement
les trois classes de la fibre inférieure pertinente. Les minima du niveau
supérieur évalués sur L e deviennent des valeurs individuelles de e.
Prendre leur minimum, avec leur terme principal commun, donne P.
La branche de type 5 n'a que le terme principal et se projette aussi.

L'extension naïve à k=2 serait fausse : pour le vecteur constant 1,
a=b=d=1, le minimum des trois lignes du niveau 2 vaut 1, tandis qu'une
ligne artificielle « type 2 » au niveau 1 donnerait 2. Ce n'est pas un
contre-exemple à la version annoncée k≥3, mais un contrôle du bord essentiel.

P transmet un certificat fibre-constant au niveau inférieur. À k=2,
être fibre-constant signifie être constant partout ; la ligne de type 5
à λ=2 exigerait \(c\le c/4\), impossible. La descente par P prouve
l'inadmissibilité de λ=2 à tous les niveaux. **Avec** l'atteinte du supremum
établie dans B, on obtient bien un écart strict \(\lambda_k<2\).
L'inadmissibilité de 2 seule, sans fermeture, ne suffirait pas.

### Relèvement R et stricte coordonnée

Pour le relèvement de k à k+1, le terme principal se relève exactement.
Une fibre du minimum supérieur se réduit à une seule coordonnée u du
niveau k : elle donne \(b c_u\) ou \(d c_u\), au lieu du minimum de la
fibre contenant u au niveau k. Cela donne R, même pour des vecteurs
non négatifs comportant des zéros.

Si une fibre n'est pas constante, une valeur \(c_u\) dépasse son minimum.
La congruence \(4m\equiv3u+2\pmod{3^{k+1}}\) définit un unique m,
et \(u\equiv2\pmod3\) impose \(m\equiv2\pmod9\). C'est la bijection
utilisée en D. La différence de la branche b est strictement positive
puisque b>0. Il n'est pas nécessaire de supposer le certificat optimal
égal à son image pour cette étape.

## 5. E : propagation des différences et prolongement en λ

Poser \(z_t=F^t(v)\) et \(\delta_t=z_{t+1}-z_t\). Monotonie et
\(v\le F(v)\) donnent \(\delta_t\ge0\). Avec \((P h)_i=h_{4i}\),

\[
\delta_{t+1}\ge aP\delta_t,\qquad
\delta_t\ge a^tP^t\delta_0.
\]

Une coordonnée stricte de \(\delta_0\) est donc transportée dans chaque
coordonnée au cours des N termes t=0,…,N−1 du cycle. En les **sommant**,
\(z_N-v=\sum_{t=0}^{N-1}\delta_t>0\) partout. Cela ne dit ni que
\(F(v)>v\) partout ni que chaque différence isolée est stricte partout.
Exemple exact au niveau 2 : v=(1,1,1), λ=1, première différence (1,0,1).

La superadditivité donne, pour \(w=\sum_{t=0}^{N-1}z_t\),
\(F(w)\ge\sum_{t=1}^{N}z_t=w+z_N-v>w\).
Le vecteur w est positif. Pour ce w **fixé**, chaque coordonnée du slack
est une fonction continue de λ. Leur nombre étant fini et leur minimum
strictement positif, on peut choisir ε>0 tel que λ+ε<2 et tous les slacks
restent positifs. Ni un choix continu de w ni une monotonie globale en λ
n'est requis. La borne λ<2 de C est indispensable pour rester dans l'intervalle.

Sans couplage positif sur un cycle, le raisonnement serait faux :
F(x0,x1)=(2x0,x1), v=(1,1) a des itérés (2^t,1) et n'est jamais strict
dans sa seconde coordonnée. Ce contre-exemple concerne une hypothèse
supprimée, pas l'opérateur KL candidat dont a>0.

## 6. Chaîne finale et statut exact de la preuve

À k=2, le certificat (3,2,3) à λ=1 est strict ; la continuité donne
\(\lambda_2>1\). Un certificat au maximum \(\lambda_2\) ne peut être
constant à cause de la ligne type 5 et de \(a<1\). D puis E donnent
\(\lambda_3>\lambda_2\).

Si \(\lambda_k>\lambda_{k-1}\), un certificat positif au seuil atteint
\(\lambda_k\) ne peut être fibre-constant, car P le transmettrait au
niveau k−1 au même paramètre. D donne une stricte coordonnée au niveau
k+1 ; E augmente le paramètre. C garantit la marge sous 2. L'induction
est donc cohérente, sans hypothèse cachée d'intervalle admissible en λ.

**Pour le F affiché :** démonstration mathématique réparée, détaillée ici,
sans contre-exemple identifié. **Pour le LP original de KL :** preuve
conditionnée à H, non encore vérifiée sur la source primaire. **Pour Lean :**
preuves algébriques partielles, pas un théorème formel sur tous les seuils.
Ce sont trois niveaux de validation différents.

## 7. Formalisation réellement obtenue

[`KLAlgebra.lean`](KLAlgebra.lean) est un fichier autonome évalué dans
l'environnement Lean 4.27.0-rc1 et Mathlib du précédent audit. Il ne
déclare aucun axiome ad hoc et ne contient aucun `sorry`. Les dix
déclarations interrogées par `#print axioms` n'utilisent que
`propext`, `Classical.choice`, `Quot.sound` :

- `auxiliary_elimination` : saturation des auxiliaires **partagées** pour
  le schéma d'inégalités explicité, avec coefficients non négatifs ;
- `projection_affine`, `lift_ge`, `lift_strict`, `nonconstant_fiber` :
  minimum de trois valeurs, projection à terme commun et gain strict ;
- `min3_superadditive`, `row_propagation` : propriétés locales qui fondent
  la superadditivité et le transport des différences ;
- `difference_lower`, `strict_after_cycle`, `summed_strictification` :
  propagation quantitative sur une marche atteignant la coordonnée stricte,
  puis sommation donnant une marge dans toutes les coordonnées.

**Hypothèses non escamotées :** les fonctions F, le cycle, sa propriété
d'atteinte et la monotonie sont des paramètres explicitement supposés
dans les lemmes génériques. Les bijections d'indices modulo \(3^k\) sont
démontrées sur papier dans cette revue et testées à niveaux finis, mais
ne sont pas instanciées universellement dans Lean. Ni A par LTE, ni B par
Brouwer, ni la continuité paramétrique ne sont formalisés ici. On ne
doit donc pas annoncer « P, D et tout le théorème KL sont certifiés Lean ».

Aucune compilation massive n'a été engagée : seulement `lake env lean`
sur ce fichier, avec des dépendances déjà compilées et sans `lake update`.
Le journal final est [lean.log](logs/lean.log). Les premiers essais de
développement ont échoué sur des détails de typage/sommation puis ont été
corrigés ; seul le fichier final et son exécution réussie font foi.

Repères de lignes dans le fichier Lean final : projection L16, relèvement
L24/L29, fibre non constante L34, superadditivité L45, transport local L53,
auxiliaires partagées L61, borne des différences L101, atteinte stricte
L117, sommation stricte L159. Les paramètres non instanciés sont visibles
dans ces signatures et ne sont pas remplacés par des axiomes.

## 8. Tests indépendants et recherche de contre-exemples

Le script fourni a été rejoué séparément : il reproduit ses 468 contrôles
de relèvement, 468 projections, 156 sommes, 12 superadditivités, ses
énumérations de 125 et 19 683 vecteurs et son slack rationnel 185.
Voir [candidate_replay.log](logs/candidate_replay.log).

Notre script [`independent_checks.py`](independent_checks.py) reconstruit
les fibres en résolvant des congruences et **n'importe aucun des deux
programmes antérieurs**. Résultat : six tests réussis, 0 échec, 0 erreur.

| Contrôle indépendant | Étendue exacte |
|---|---|
| Indices de branches et cycles | 728 lignes de branches, k=2,…,7 ; cycles complets et bijections des fibres. |
| Projection, relèvement et stricte coordonnée | 59 370 cas vecteur/coefficient ; niveaux 2 et 3 exhaustifs sur {0,1,2}, 40 vecteurs rationnels chacun aux niveaux 4 et 5 ; trois triplets de coefficients. |
| Somme à λ=2 et cas d'égalité | Même collection de vecteurs ; coefficient exact (1/4,3/4,3/2) ; recherche explicite d'un certificat non nul, aucun trouvé. |
| Auxiliaires et normalisation | 1 040 cas, k=2,3, poids sur {1,2}, énumération des auxiliaires entières jusqu'au minimum ; λ=1 et λ=2. |
| Frontière des vecteurs propres | Les 516 supports propres non vides des niveaux 2 et 3 sont incompatibles avec une équation propre à cause du cycle. |
| Propagation et stricte sommation | 222 vecteurs positifs admissibles non fixes à λ=1, aux niveaux 2 et 3 ; N itérations, borne des différences et vérification de F(w)>w. |
| Erreurs de portée | Contre-exemple au B libre en c ; bord interdit de P ; défaut de propagation sans couplage cyclique. |

Les triplets de coefficients rationnels arbitraires testent des identités
algébriques, pas une grille de vrais λ : hors λ=1 et λ=2, ils ne sont pas
présentés comme égaux aux trois puissances prescrites. Les auxiliaires
réelles et tous les vecteurs propres ne sont pas couverts par une
énumération finie ; leur justification générale est analytique ou algébrique,
distincte de ces tests. Voir [independent.json](logs/independent.json).

Commandes réellement exécutées, depuis la racine du dépôt :

```sh
git fetch origin research/kl-strict-monotonicity-candidate
git switch -c review/kl-strict-monotonicity FETCH_HEAD
git ls-remote origin refs/heads/research/kl-strict-monotonicity-candidate refs/pull/6/head
python3 research/kl_strict_monotonicity_audit.py
python3 research/kl_review/independent_checks.py
```

Depuis `/workspace/collatz/lean` :

```sh
ELAN_HOME=/workspace/.elan PATH=/workspace/.elan/bin:$PATH \
  lake env lean /workspace/syracuse_search/research/kl_review/KLAlgebra.lean
```

Les empreintes et statuts d'exécution sont dans [validation.json](logs/validation.json).
Les counts regroupent plusieurs assertions et ne sont pas autant de preuves
indépendantes. Les tests du précédent audit Syracuse ne sont pas revendiqués
comme ayant été relancés pour cette mission.

## 9. Bibliographie : établi, conditionnel et non consultable

1. **Krasikov–Lagarias (2003)**, *Bounds for the 3x+1 problem using
   difference inequalities*, Acta Arithmetica 109, 237–258.
   Sources à consulter :
   https://websites.umich.edu/~lagarias/doc/krasikov.pdf et
   https://arxiv.org/abs/math/0205002.
   **Non consultées ici, accès bloqué.** La traduction L0–L3 et l'assertion
   « strictement croissant reste ouvert », attribuée à la section 6 par le
   candidat, doivent être vérifiées sur une version datée du texte.
2. **Nikpour–Rabbani (2026), SSRN 7239062** :
   https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7239062.
   Le candidat lui attribue une méthode PF non linéaire, l'infaisabilité à
   λ=2 et des calculs k=20, γ=0,914947. **Ni le contenu, ni la date, ni ces
   chiffres ne sont validés par cette revue**, faute d'accès au texte.
   Il faut lire en particulier ses énoncés de monotonie, d'irréductibilité,
   de relèvement et de stricte comparaison avant toute annonce de priorité.
3. **Cadre théorique classique** : le recours à Brouwer et aux arguments
   de comparaison de Perron–Frobenius non linéaire ne constitue pas en soi
   une méthode nouvelle. Repères bibliographiques généraux : Gaubert et
   Gunawardena, *The Perron–Frobenius theorem for homogeneous, monotone
   functions* (2004) ; Lemmens et Nussbaum, *Nonlinear Perron–Frobenius
   Theory* (2012). Ces repères ne sont pas une lecture exhaustive de leurs
   résultats ni une vérification de priorité du présent énoncé.
4. **Implémentation `msharpe248/collatz`** : le fichier local
   `analysis/kl_exponent.py` présente les mêmes trois familles de lignes et
   annonce des comparaisons à KL. Ce constat est secondaire ; il ne transforme
   pas un commentaire de code en preuve de conformité à l'article.

**Lacunes restantes pour lever le verdict conditionnel :** obtenir les
sources primaires, vérifier H ligne par ligne, contrôler la version et les
résultats exacts de Nikpour–Rabbani, faire relire la démonstration réparée et,
pour une certification intégrale, instancier les indices et formaliser les
étapes analytiques. Aucun résultat scientifique nouveau n'est revendiqué.

## 10. Livraison et actions bloquées

Les neuf fichiers de cette revue ont été committés puis poussés sur
`review/kl-strict-monotonicity`, branche issue du commit exact de la PR #6.
Les deux fichiers candidats restent inchangés. Aucun merge n'a été effectué.

La tentative réelle d'ouverture d'une PR de revue en brouillon, avec base
`research/kl-strict-monotonicity-candidate` et head
`review/kl-strict-monotonicity`, a échoué avant l'API GitHub :
`Post "https://api.github.com/graphql": Forbidden`.
**Aucune nouvelle PR n'est confirmée.** Le lien manuel visant la bonne base est :

https://github.com/hsirven1/syracuse_search/compare/research/kl-strict-monotonicity-candidate...review/kl-strict-monotonicity?expand=1

Pour terminer les points bloqués, il faut rendre accessibles les sources
primaires (`websites.umich.edu`, ou `arxiv.org`/`export.arxiv.org`, et
`papers.ssrn.com`) et l'API GitHub (`api.github.com`). Les domaines de sources
ont été ajoutés au brouillon réseau en préservant les règles connues ;
l'outil demande revue/enregistrement puis publication dans les paramètres.
Cette sauvegarde n'a pas établi un accès opérationnel. Aucun token n'a
été demandé : les échecs observés sont des refus de tunnel, pas une preuve
d'absence de l'authentification Git HTTPS, qui a fonctionné pour le push.
