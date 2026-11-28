# Cycle 020 — Progression de raison fixe : pas de descente commune non bornée

Date : 28 novembre 2026. Axe **A**. Branche : `research/memory`.
Script : [`../checks/cycle020_arithmetic_progression.py`](../checks/cycle020_arithmetic_progression.py).

**Verdict.** NO-GO pour une famille nouvelle. Dans le champ autorisé,
aucune progression de raison fixe n'a à la fois une trajectoire
accélérée commune et un \(\tau_U\) non borné (B27). La diagonale des
cylindres d'A3 satisfait la borne logarithmique, et c'est déjà le
certificat de `EXACT_STOPPING_TIME_BASELINE.md`. Aucune orbite
divergente n'est exclue. Aucune preuve de Syracuse.

## 0. Revue traitée, fenêtre, porte d'antériorité

La revue `6094936782` porte le marqueur `SYRACUSE_INDEPENDENT_REVIEW`
et le SHA `5faae4186f7f35921b4e9aad3d70ef475582a6ef`, tête de la PR #27
au début de ce cycle. Elle confirme X52 et la portée de B26. Avec
\(a=-2^D/3^{m+1}\) et \(r=2/3\), la somme de \(J\) termes vaut
\(P_J=L(1-r^J)\), donc
\(P_J-L=-Lr^J=+2^{D+J}/3^{m+J}\). Le témoin \(Q=-1\), \(J=1\), donne
\(P_1=-1/3\), \(L=-1\) et \(P_1-L=2/3\). L'inclusion séparée reste
ouverte. Elle ne demande aucune correction. Le cycle 019 n'est pas
réécrit.

Au 28 novembre 2026, 01:48 UTC, la fenêtre de douze cycles contient les
cycles 010 à 019. Le plus ancien est `462014b`, du 27 novembre à
02:11:58 UTC. Ce cycle est le onzième. Le cycle 021 n'est pas ouvert.

Les cycles 016 à 019 ont retrouvé des énoncés publiés. Ce cycle ne
relit pas un théorème classique pour en mesurer la portée sur une
orbite divergente.

### Candidat 1 — une classe d'A3

**Énoncé.** Pour \(m\) fixé, la progression de raison \(2^{2m+1}\)
décrite dans `EXACT_STOPPING_TIME_BASELINE.md` a une trajectoire close
et \(\tau_U=m\).

**Obstacle.** L'horizon est constant. La question demande aussi que
\(\tau_U\) soit non borné sur la famille.

**Intérêt.** Aucun, pour les deux exigences réunies : la seconde
échoue.

**Résultat le plus proche.** A3, déjà prouvé. Terras 1976, théorème 1.2,
lu au cycle 015, identifie le mot de longueur \(k\) à la classe modulo
\(2^k\). Le PDF n'est pas rouvert.

**Écart.** Aucun. Le module dépend de \(m\), et \(m\) est fixé dans une
classe.

**Classement.** DÉJÀ CONNU. Confiance haute.

**Décision.** NO-GO.

### Candidat 2 — la diagonale des représentants d'A3

**Énoncé.** Pour chaque \(m\ge 1\), soit \(q_m\) le résidu impair du
certificat, éventuellement relevé d'un multiple de \(2^{m+1}\) pour
que \((4^m-3^m)q_m>2^m-1\), et \(n_m=2^m q_m-1\). Alors
\(\tau_U(n_m)=m\) et \(m\le\log_2(n_m+1)\), avec la trajectoire
\(U^t(n_m)=3^t 2^{m-t}q_m-1\) pour \(0\le t<m\).

**Obstacle.** Une classe fixe a un horizon constant. La diagonale fait
varier \(m\).

**Intérêt.** Les deux exigences numériques sont satisfaites, puisque
\(n_m+1=2^m q_m\ge 2^m\).

**Résultat le plus proche.** La preuve constructive d'A3. Les exemples
\(m=1,\ldots,5\) y sont \(9,19,87,15,863\).

**Écart.** La comparaison \(m\le\log_2(n_m+1)\) n'était pas écrite.
Elle suit de \(q_m\ge 1\), sans argument nouveau. Chaque terme reste
défini par le cylindre de niveau \(m\).

**Classement.** COROLLAIRE DIRECT. Confiance haute : le contrôle
\(1\le m\le 40\) retrouve la formule, il n'est pas la preuve.

**Décision.** NO-GO. Ne pas adopter cette diagonale comme réponse.
L'agenda écarte une classe d'A3, et la diagonale est le même mécanisme.

### Candidat 3 — \(n\equiv 1\pmod 4\), les Mersenne, \(5\cdot 2^k-1\)

**Énoncé.** L'une de ces trois familles a une trajectoire close,
\(\tau_U\le C\log_2(n+1)\) et \(\tau_U\) non borné.

**Obstacle.** X40 donne \(\tau_U=1\) pour tout impair \(n>1\) congru à
\(1\pmod 4\). A2 donne le préfixe de \(2^h-1\) jusqu'au rang \(h-1\),
encore au-dessus du départ. B15 donne \(\tau(5\cdot 2^k-1)\ge k+1\)
pour \(k\ge 3\), sans formule jusqu'à la descente.

**Intérêt.** Aucun nouveau : les trois familles sont écartées par
l'énoncé de la question.

**Résultat le plus proche.** X40, A2, B15, X2. Pour \(h=5\),
\(U^t(31)\) suit A2 sur \(t\le 4\) et \(\tau(31)=35\). Ce nombre est
déjà le témoin de X2. Il n'ouvre pas de formule.

**Écart.** Aucun sur le préfixe. La descente complète des Mersenne et
de \(5\cdot 2^k-1\) reste hors du texte, volontairement.

**Classement.** DÉJÀ CONNU pour l'exclusion. Confiance haute.

**Décision.** NO-GO. Ne pas rouvrir ces trois familles.

### Candidat 4 — une progression arithmétique simple

**Énoncé.** Il existe des entiers \(a\) impair et \(d\) pair non nul,
et une constante \(C\), tels que la progression \(n=a+kd>1\) admette
une suite de valuations indépendante du terme, décrivant
\(U^t(n)\) jusqu'à la première descente, avec \(\tau_U\) non borné et
\(\tau_U(n)\le C\log_2(n+1)\).

**Obstacle.** Le module d'un cylindre grandit avec l'horizon. Une
raison fixe ne peut pas porter tous les mots à la fois.

**Intérêt.** C'est le seul candidat encore permis par l'agenda. S'il
existait, la famille serait explicite et infinie, sans faire varier la
raison.

**Résultat le plus proche.** Terras 1976, théorème 1.2, déjà lu : mêmes
vecteurs d'encodage de longueur \(L\) si et seulement si congruence
modulo \(2^L\). Le cycle 015 §10 a prouvé le sens « parités communes
\(\Rightarrow\) congruence ». A3 rappelle que \(\tau_U\) prend toute
valeur \(m\), mais sur un module qui dépend de \(m\).

**Écart.** Le théorème 1.2 ne parle pas de \(\tau_U\) sur une raison
fixe. L'obstruction précise est B27, ci-dessous. Elle ne dépasse pas
le codage.

**Classement.** COROLLAIRE DIRECT du codage déjà écrit, pour la borne
de longueur. La chaîne de valuations est l'arithmétique de
\(v_2((3a+1)+k\cdot 3d)\), élémentaire. Confiance haute. Ce n'est pas
une nouveauté.

**Décision.** GO pour écrire cette obstruction, parce que l'agenda
demande de trancher la progression simple et de s'arrêter s'il n'y a
pas de mécanisme. Pas de GO pour en faire un théorème original, ni
pour chercher une quatrième famille.

## 1. Théorème B27

Soient \(a\) un entier impair et \(d\) un entier pair non nul. Soit
\(r=v_2(d)\). Les termes \(n(k)=a+kd>1\) sont impairs.

**(Longueur.)** Si ces termes partagent les \(L\) premières parités
sous \(T\), alors \(L\le r\).

Deux termes consécutifs diffèrent de \(d\). Le cycle 015 §10 dit que
\(L\) parités communes donnent \(v_2(n-m)\ge L\). Donc \(2^L\) divise
\(d\). Le sens réciproque, longueur exactement \(r\), est la moitié
déjà lue du théorème 1.2 : les termes sont congrus modulo \(2^r\), et
pas tous modulo \(2^{r+1}\). Cette égalité n'est pas redémontrée. Les
échantillons du script ont la longueur \(r\). Ce contrôle fini n'est
pas la preuve.

**(Valuation constante.)** Soit \(s=v_2(3a+1)\). La valuation
\(v_2(3n(k)+1)\) est la même pour tout \(k\) si et seulement si
\(s<r\), et elle vaut alors \(s\).

En effet \(3n(k)+1=(3a+1)+k\cdot 3d\) et \(v_2(3d)=r\). Si \(s<r\), le
terme \(k\cdot 3d\) est plus divisible que \(3a+1\), donc la valuation
reste \(s\). Si \(s\ge r\), on écrit
\(3n(k)+1=2^r(\alpha+k\beta)\) avec \(\beta\) impair. La progression
\(\alpha+k\beta\) a une raison impaire : elle prend des valeurs paires
et impaires, et des valuations arbitrairement grandes. L'exposant
extrait par \(U\) n'est donc pas constant.

**(Descente uniforme.)** Si \(s\ge 2\) et \(s<r\), alors
\(U(n)=(3n+1)/2^s\le(3n+1)/4<n\) pour tout terme \(n>1\). Donc
\(\tau_U=1\).

**(Montée uniforme.)** Si \(s=1<r\), alors \(r\ge 2\) et
\(U(n)=(3n+1)/2>n\). L'image est la progression de premier terme
\((3a+1)/2\) et de raison \(3d/2\). Cette raison est paire, de
valuation \(r-1\), et le premier terme est impair.

Chaque montée de valuation \(1\) diminue donc de \(1\) la valuation de
la raison. On ne peut en enchaîner au plus \(r-1\). Au pas suivant, ou
bien la valuation est constante et au moins \(2\), et c'est une
descente, donc \(\tau_U\le r\), ou bien elle n'est plus constante.

**(Incompatibilité.)** Une suite de valuations, la même pour tous les
termes et menée jusqu'à la première descente, a une longueur au plus
\(r\). Elle ne peut pas prendre des longueurs arbitrairement grandes.
Si \(\tau_U\) n'est pas borné sur la progression, les mots de
valuations ne sont pas communs : la trajectoire n'est pas close au
sens d'une seule suite.

La réciproque est fausse, et ce n'est pas une nouvelle obstruction.
Pour \(m\ge 2\), le représentant \(n_m\) d'A3 est congru à \(3\pmod 4\),
et la classe entière de niveau \(m\) aussi, parce que \(2^m q\) est
divisible par \(4\). La progression \(3+4k\) contient donc, pour chaque
\(m\ge 2\), une sous-progression de raison \(2^{2m+1}\) sur laquelle
\(\tau_U=m\). C'est A3, pas une trajectoire commune. Le témoin local
est indépendant de cette infinité : \(\tau(3)=2\) et \(\tau(7)=4\),
alors que le seul pas commun est la valuation \(1\).

Le cas \(n\equiv 1\pmod 4\) reste X40. Sur \(1+4k\), l'exposant
\(v_2(3n+1)\) n'est pas constant, et \(\tau_U=1\) quand même, parce que
cet exposant vaut au moins \(2\). B27 n'étend pas X40.

## 2. Ce que ce cycle ne montre pas

B27 n'exclut aucune orbite hors de la progression. Il ne donne pas de
famille dont le mot grandit et reste explicite sans faire croître la
raison. Il ne borne pas \(\tau_U(2^h-1)\) ni \(\tau_U(5\cdot 2^k-1)\).
Le contrôle \(\tau(31)=35\) répète X2 sur un seul entier. Il ne prouve
pas que \(\tau\) est non borné sur \(3+4k\) autrement que par A3, déjà
écrit. Une union finie de progressions de raisons fixes ne couvre pas
les impairs : A3 rend \(\tau_U\) non borné, et chaque pièce n'a qu'un
mot commun de longueur bornée. Cette phrase est le même corollaire.
Elle n'est pas numérotée à part, et elle n'est pas la question
suivante.

Les cycles 016 à 020 sont cinq cycles d'identifications ou de
corollaires. Cette direction s'arrête : ni cylindre, ni progression de
raison fixe, ni lecture dont le seul produit est la portée d'un
théorème classique.

## 3. Mises à jour de la mémoire

- `proved.md` : B27.
- `hypotheses.md` : H15, fermé.
- `prior_art.md` : Terras 1.2 n'est pas relu ; il est appliqué à une raison fixe.
- `abandoned.md` : ne pas relancer la recherche de famille close dans une raison fixe.
- `agenda.md` : le cycle 021 est une porte, pas une variante.
- `reviews.md` : revue `6094936782`.

## 4. Prochaine question

Axe **B**. Sur une orbite positive non bornée, B6 prouve
\(R(t)=O(\log E(t))\) dans l'identité de hauteur, par une somme
harmonique sur des entiers pairs distincts. Le dossier non validé C3
attribue une somme des réciproques bornée à Garcia–Tal 1999. Ce texte
n'a pas été lu.

La question du cycle 021 est seulement la porte d'antériorité. Le
texte primaire donne-t-il \(R(t)=O(1)\), et cette borne exclut-elle
une orbite que la limite
\(\limsup E(t)/t\le\beta/\delta\) de B6 n'exclut pas ? Si elle ne
change pas cette limite, ou si le PDF n'est pas obtenu, NO-GO.
S'arrêter sans lemme de remplacement. Ne pas invoquer C3 comme
prémisse. Ne pas rouvrir les cylindres, les progressions de raison
fixe, H1, H2, H3, \(P(2)\), le signe moins, ni les lectures de portée
des cycles 016 à 019.

Ne pas ouvrir le cycle 021 avant la relecture indépendante de ce
cycle. Recompter la fenêtre à ce moment-là. Le plus ancien cycle
encore dans la fenêtre au début de celui-ci est le cycle 010.

## 5. Reproduire

```sh
python3 research/checks/cycle020_arithmetic_progression.py
```

Sortie attendue : 6 lignes `PASS`.
