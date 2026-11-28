# Cycle 020 — Progression de raison fixe : pas de descente commune non bornée

Date : 28 novembre 2026. Axe **A**. Branche : `research/memory`.
Script : [`../checks/cycle020_arithmetic_progression.py`](../checks/cycle020_arithmetic_progression.py).

**Verdict.** NO-GO pour une famille nouvelle. Dans le champ autorisé,
aucun rayon de raison positive n'a à la fois un mot de valuations
commun jusqu'à la première descente et un \(\tau_U\) non borné (B27).
La revue `6095039362` retire l'inférence \(\tau_U\le r\) et la phrase
sur l'union finie ; le détail est au §6. La diagonale des cylindres
d'A3 satisfait la borne logarithmique, et c'est déjà le certificat de
`EXACT_STOPPING_TIME_BASELINE.md`. Aucune orbite divergente n'est
exclue. Aucune preuve de Syracuse.

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

Soient \(a>1\) un entier impair et \(d\) un entier pair strictement
positif. Soit \(r=v_2(d)\). Les termes \(n(k)=a+kd\), \(k\ge 0\),
forment un rayon infini d'impairs supérieurs à \(1\). Si l'on part
d'une raison paire négative, on la remplace par sa valeur absolue et
l'on prend le plus petit terme positif : ce rayon est le seul
quantificateur du théorème. La lecture \(k\ge 0\) avec une raison
négative est X55.

**(Longueur des parités.)** Ces termes partagent exactement les \(r\)
premières parités sous \(T\).

Deux termes du rayon diffèrent d'un multiple de \(d\), donc l'écart a
une valuation au moins \(r\). Deux termes adjacents diffèrent de \(d\),
de valuation exactement \(r\).

Le sens « \(k\) parités communes impliquent \(v_2(n-m)\ge k\) » est le
cycle 015 §10. Le sens inverse utilise la même identité de pas. Si
\(v_2(n-m)\ge k\ge 1\), alors \(n\) et \(m\) ont la même parité, et
\(v_2(T(n)-T(m))=v_2(n-m)-1\) : le pas pair divise l'écart par \(2\),
le pas impair le multiplie par \(3\), qui est impair. La récurrence
donne les \(k\) premières parités. Si la valuation de l'écart vaut
exactement \(k\), la parité suivante diffère. Le PDF de Terras n'est
pas rouvert. Cette égalité remplace la moitié qui n'était pas écrite.

**(Somme des exposants.)** Soit \((s_1,\ldots,s_m)\), \(m\ge 1\), un
mot d'exposants exacts de \(U\), le même pour deux termes adjacents
\(n\) et \(n+d\). Alors \(s_1+\cdots+s_m\le r-1\), donc \(m\le r-1\).

On pose \(D_0=d\). Si le premier exposant commun est \(s_1\), alors
\(2^{s_1}\) divise \(3d\), donc \(s_1\le r\). Les deux images sont
impaires, donc leur écart \(D_1=3d/2^{s_1}\) est un entier pair et
\(s_1\le r-1\). Au pas suivant, le même raisonnement s'applique à
\(D_j\) : l'exposant commun \(s_{j+1}\) est strictement inférieur à
\(v_2(D_j)\), et
\(v_2(D_{j+1})=r-(s_1+\cdots+s_{j+1})\ge 1\). La somme des \(m\)
exposants vaut donc au plus \(r-1\).

**(Valuation constante au premier pas.)** Soit \(s=v_2(3a+1)\). La
valuation \(v_2(3n(k)+1)\) est indépendante de \(k\ge 0\) si et
seulement si \(s<r\), et elle vaut alors \(s\).

En effet \(3n(k)+1=(3a+1)+k\cdot 3d\) et \(v_2(3d)=r\). Si \(s<r\), le
terme \(k\cdot 3d\) est plus divisible que \(3a+1\) dès que \(k\neq 0\),
donc la valuation reste \(s\). Si \(s\ge r\), on écrit
\(3n(k)+1=2^r(\alpha+k\beta)\) avec \(\beta\) impair. Deux indices
consécutifs donnent des quotients de parités opposées : l'un a la
valuation \(r\), l'autre une valuation au moins \(r+1\). Comme
\(\beta\) est inversible modulo \(2^N\), le rayon contient, pour chaque
\(N\), un indice dont la valuation dépasse \(r+N\). Cette infinité
utilise tout le rayon. Un ensemble fini d'indices ne la donne pas.

**(Descente au premier pas.)** Si \(s\ge 2\) et \(s<r\), alors
\(U(n)=(3n+1)/2^s\le(3n+1)/4<n\) pour tout terme \(n>1\). Donc
\(\tau_U=1\).

**(Montées.)** Si \(s=1<r\), alors \(U(n)=(3n+1)/2>n\). L'image est le
rayon de premier terme \((3a+1)/2\) et de raison \(3d/2\), de valuation
\(r-1\). Chaque pas commun d'exposant \(1\) abaisse de \(1\) la
valuation de la raison. La somme des exposants en interdit plus de
\(r-1\). Ceci ne borne pas \(\tau_U\).

**(Chute locale.)** Un exposant commun au moins \(2\), apparu après
une ou plusieurs montées, donne
\(U(m)=(3m+1)/2^s\le(3m+1)/4<m\) pour l'itéré précédent \(m>1\). Il ne
donne pas \(U(m)<n(k)\). Le mot commun peut continuer après cette
chute. Avant d'appeler première descente l'itéré affine, on le compare
à \(a+kd\). Les témoins sont X53. L'inférence retirée est
« donc \(\tau_U\le r\) ».

**(Incompatibilité.)** Supposons qu'un même mot \((s_1,\ldots,s_m)\)
décrive, pour chaque terme du rayon, les pas jusqu'à la première
descente : \(U^t(n)\ge n\) pour \(t<m\) et \(U^m(n)<n\). Alors
\(\tau_U(n)=m\) pour tout le rayon, et la somme des exposants donne
\(m\le r-1\). Un tel mot ne peut pas avoir une longueur non bornée.
Si \(\tau_U\) n'est pas borné sur le rayon, les mots de première
descente ne sont pas communs.

La réciproque est fausse, et ce n'est pas une nouvelle obstruction.
Pour \(m\ge 2\), le représentant \(n_m\) d'A3 est congru à \(3\pmod 4\),
et la classe entière de niveau \(m\) aussi, parce que \(2^m q\) est
divisible par \(4\). La progression \(3+4k\) contient donc, pour chaque
\(m\ge 2\), une sous-progression de raison \(2^{2m+1}\) sur laquelle
\(\tau_U=m\). C'est A3, pas une trajectoire commune. Le témoin local
est indépendant de cette infinité : \(\tau(3)=2\) et \(\tau(7)=4\),
alors que le seul pas accéléré commun est la valuation \(1\), et
\(r=2\).

Le cas \(n\equiv 1\pmod 4\) reste X40. Sur \(1+4k\), pour les termes
\(n>1\), l'exposant \(v_2(3n+1)\) n'est pas constant, et \(\tau_U=1\)
quand même, parce que cet exposant vaut au moins \(2\). B27 n'étend
pas X40.

La longueur d'un préfixe commun peut différer de \(\tau_U\). Sur
\(9+16k\), le premier exposant vaut \(2\), donc \(\tau_U=1\), et le
second vaut encore \(1\) pour tout \(k\) : le préfixe commun dépasse
la première descente. Sur \(27+32k\), le préfixe commun \((1,2,1)\)
laisse tous les termes au-dessus du départ (X53).

## 2. Ce que ce cycle ne montre pas

B27 n'exclut aucune orbite hors du rayon. Il ne donne pas de
famille dont le mot grandit et reste explicite sans faire croître la
raison. Il ne borne pas \(\tau_U(2^h-1)\) ni \(\tau_U(5\cdot 2^k-1)\).
Le contrôle \(\tau(31)=35\) répète X2 sur un seul entier. Il ne prouve
pas que \(\tau\) est non borné sur \(3+4k\) autrement que par A3, déjà
écrit. Une union finie de rayons de raisons fixes peut couvrir tous
les impairs positifs : \(1+4k\) et \(3+4k\), \(k\ge 0\), le font (X54).
L'énoncé qui reste est celui du certificat. Si chaque pièce d'une
famille finie porte un mot de valuations commun décrivant la première
descente de chacun de ses termes, alors \(\tau_U\) y est borné par la
plus grande de ces longueurs. A3 rend \(\tau_U\) non borné sur les
impairs, déjà sur \(3+4k\). Une telle couverture n'existe pas. Cette
phrase n'est pas une contrainte hors des pièces, et elle n'est pas la
question suivante.

Les cycles 016 à 020 sont cinq cycles d'identifications ou de
corollaires. Cette direction s'arrête : ni cylindre, ni progression de
raison fixe, ni lecture dont le seul produit est la portée d'un
théorème classique.

## 3. Mises à jour de la mémoire

- `proved.md` : B27, puis la correction du §6.
- `hypotheses.md` : H15, fermé, avec le certificat explicite.
- `prior_art.md` : Terras 1.2 n'est pas relu ; les deux sens de la baisse de valuation sont écrits au §1.
- `abandoned.md` : ne pas relancer la recherche de famille close dans une raison fixe.
- `agenda.md` : le cycle 021 attend la relecture de la correction.
- `reviews.md` : revues `6094936782` et `6095039362`.
- `counterexamples.md` : X53, X54, X55.

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

Ne pas ouvrir le cycle 021 avant la relecture indépendante de la
correction du §6. Recompter la fenêtre à ce moment-là. Le plus ancien
cycle encore dans la fenêtre au début de celui-ci est le cycle 010.

## 5. Reproduire

```sh
python3 research/checks/cycle020_arithmetic_progression.py
```

Sortie attendue : 10 lignes `PASS`.

## 6. Revue `6095039362`

La revue porte le marqueur `SYRACUSE_INDEPENDENT_REVIEW` et le SHA
`b2d466a95ecd5347bcd6620851eb7caabac2dee0`, tête de la PR #27 au moment
de la relecture. Elle confirme l'obstruction par l'écart des images et
le corollaire d'A3. Elle réfute deux phrases. Les contrôles ci-dessous
sont indépendants de son arithmétique JavaScript. Le PDF de Terras
n'est pas rouvert : les deux sens écrits au §1 sont l'identité de pas
du cycle 015 §10.

**X53.** La phrase retirée est : « Au pas suivant, ou bien la valuation
est constante et au moins \(2\), et c'est une descente, donc
\(\tau_U\le r\), ou bien elle n'est plus constante. » Un exposant
commun au moins \(2\) descend sous l'itéré précédent. Il ne descend
pas forcément sous le départ, et le mot commun peut continuer.

Sur \(n=11+16k\), \(r=4\). Les deux premiers exposants sont \(1\) puis
\(2\), pour tout \(k\ge 0\) :
\(3n+1=34+48k\), \(U(n)=17+24k\), \(3U(n)+1=52+72k\) et
\(U^2(n)=13+18k\). L'écart au départ est \(2+2k>0\). La chute
\(17+24k\to 13+18k\) est réelle, et elle reste au-dessus du départ.
Pour \(k=1\), les quatre premiers itérés sont \(41,31,47,71\), tous
supérieurs à \(27\). Le calcul fini donne \(\tau_U(27)=37\). La somme
\(1+2=3=r-1\) sature la borne : le troisième exposant n'est pas commun,
car \(3(13+18k)+1=2(20+27k)\) et \(20+27k\) a la parité de \(k\).

Sur \(n=27+32k\), \(r=5\). Le préfixe \((1,2,1)\) est commun pour tout
\(k\ge 0\), et la chute d'exposant \(2\) est au milieu :
\(U(n)=41+48k\), \(U^2(n)=31+36k\), \(U^3(n)=47+54k\). Les trois écarts
au départ sont \(14+16k\), \(4+4k\) et \(20+22k\), tous strictement
positifs. Le quatrième exposant n'est pas commun :
\(3U^3(n)+1=2(71+81k)\), et \(71+81k\) est impair exactement quand
\(k\) est pair. Le calcul fini donne \(\tau_U(27)=37\) et
\(\tau_U(59)=4\). Ces deux valeurs ne sont pas la preuve de la
positivité des écarts. On conserve \(\tau_U=1\) lorsque l'exposant
commun initial est au moins \(2\).

**X54.** La phrase retirée est : « Une union finie de progressions de
raisons fixes ne couvre pas les impairs. » Pour \(k\ge 0\), les rayons
\(1+4k\) et \(3+4k\) sont disjoints et contiennent chaque impair
positif. La phrase corrigée, au §2, exige un mot commun de première
descente sur chaque pièce. Sans ce certificat, A3 ne contredit pas la
couverture.

**X55.** La première rédaction quantifiait \(n=a+kd>1\) pour \(d\) pair
non nul, sans fixer le sens de \(k\). Lue avec \(k\ge 0\) et \(d<0\),
elle laisse des singletons. Pour \(a=3\) et \(d=-4\), le seul terme
supérieur à \(1\) est \(3\). L'implication « un préfixe commun de
longueur \(L\) force \(L\le r\) » n'a plus de seconde borne : l'orbite
de \(3\) commence par les parités \(1,1,0\), et \(r=2\). Sur ce
singleton, \(s=v_2(10)=1<2\), donc la biconditionnelle de valuation
reste vraie. Elle échoue pour \(a=5\) et \(d=-4\) : le seul terme
supérieur à \(1\) est \(5\), \(s=v_2(16)=4\ge 2=r\), et un ensemble à
un point a une valuation constante. Lu sur tous les termes positifs,
\(d=-4\) redonne le rayon \(3+4k\) ou \(5+4k\), déjà couvert par \(d>0\).

L'obstruction conservée est celle de l'écart : un mot commun jusqu'à
la première descente a une somme d'exposants au plus \(r-1\). Ce n'est
pas une nouveauté, ni une contrainte hors du rayon. Les contrôles
\(\tau_U(3)=2\), \(\tau_U(7)=4\) et \(\tau_U(31)=35\) répètent des
témoins déjà écrits. Ne pas rouvrir B27 pour chercher une autre
famille. Ne pas ouvrir le cycle 021 avant la relecture indépendante
de cette correction.
