# Cycle 017 — Korec 1994 ne force aucune classe à atteindre 1

Date : 28 novembre 2026. Axe **C**.
Branche : `research/memory`. Script : [`../checks/cycle017_korec_density.py`](../checks/cycle017_korec_density.py).

**Verdict.** Le théorème 1 de Korec, *Mathematica Slovaca* 44 (1994),
85–89, est une densité naturelle. Il a été lu sur le PDF. Il ne force
aucune classe de congruence à atteindre \(1\). La densité relative de
l'ensemble bon dans chaque classe vaut \(1\) (B23). Ce n'est pas
l'inclusion de la classe, ni l'atteinte de \(1\). Le théorème n'est
pas redémontré. Aucune preuve de la conjecture, et aucune orbite
divergente n'est exclue. La revue `6094566180` confirme B23. Elle
corrige la comparaison imprimée sur \(d\) (X45) et la lecture de la
parenthèse en \(\log_2 y\) (X46). Ces deux portées ne changent pas
l'argument de densité relative.

## 0. Revue traitée, question, porte d'antériorité

La revue `6094283257` porte le marqueur `SYRACUSE_INDEPENDENT_REVIEW`
et le SHA `c3b0219856c3a13bc003e5f09671a30319bc95d2`, tête de la PR #27
au début de ce cycle. Elle confirme la réduction du cycle 016 §9.
Elle ne demande aucune correction. Le script du cycle 016 donne encore
ses 8 lignes `PASS`. Le cycle 016 n'est pas réécrit.

La fenêtre de douze cycles était fermée jusqu'au 28 novembre 2026 à
00:04 UTC : le commit `ebba330` est du 27 novembre à 00:03:27 UTC. Ce
cycle commence après cet instant. Au moment de l'écriture, les cycles
006 à 016 sont les onze cycles de la fenêtre, et celui-ci est le
douzième.

**Candidat.** Pour tout réel \(c>\log_4 3\), l'ensemble des entiers
dont un itéré de \(T\) passe sous \(y^c\) a une densité asymptotique
égale à \(1\). La question est de savoir si cette borne force une
classe de congruence entière à atteindre \(1\).

**Obstacle.** B20 et X34 montrent déjà qu'une densité, même nulle au
sens naturel, ne remplit pas une classe et n'atteint pas \(1\). Une
seconde preuve du même type de comptage ne retirerait aucune orbite.

**Intérêt.** Si la borne forçait vraiment toute une classe à atteindre
\(1\), elle exclurait une infinité d'entiers. Un comptage de densité
\(1\) n'en exclut aucun en particulier.

**Résultat le plus proche.** Korec, *Math. Slovaca* 44 (1994), no. 1,
85–89, théorème 1. **[P]** pour l'énoncé, la définition de \(T\), la
phrase d'équivalence de la page 85, le lemme 1 tel qu'il est cité, le
choix de \(d\) à la page 87, et les exemples 1 et 2. PDF
`https://dml.cz/bitstream/handle/10338.dmlcz/133225/MathSlov_44-1994-1_8.pdf`,
SHA-256 `3111bcc638a563fa4395d8a090a4b563116f1ffe30aee136f6e24a76d4d97c77`,
6 pages, non redistribué. La preuve du théorème 1, le lemme 2 et le
théorème central limite ne sont pas repris. Terras (1976) et Everett
(1977) ne sont pas rouverts. Allouche (1978/79), Heppner (1978) et
Dolan–Gilman–Manickam (1987), cités par Korec, ne sont pas ouverts.
Tao, ar5iv de arXiv:1909.03562, a été lu seulement pour les deux
phrases qui nomment Korec. Le PDF de la revue de 2022 n'est pas
rouvert.

**Écart.** Le théorème lu est exactement le candidat, avec l'inégalité
stricte \(T^n(y)<y^c\). Il ne dit pas qu'une classe atteint \(1\).
Tao écrit la forme non stricte \(\mathrm{Col}_{\min}(N)\le N^\theta\),
qui suit de l'inégalité stricte pour le même exposant. Ce n'est pas
un second théorème.

**Classement.** DÉJÀ CONNU pour la densité naturelle, confiance haute :
l'énoncé a été lu sur le PDF. La phrase « ceci force une classe entière
à atteindre \(1\) » est PLUS FAIBLE que ce que B20 et X34 empêchent
déjà de conclure, et elle ne suit pas du théorème. La densité relative
dans une classe est un COROLLAIRE DIRECT du théorème et de la densité
\(1/m\) d'une classe. Elle reste un comptage.

**Décision.** NO-GO pour une preuve du théorème 1. Le seul travail de
ce cycle est la portée sur les classes et sur l'atteinte de \(1\).

## 1. Énoncé lu

\(T(y)=(3y+1)/2\) si \(y\) est impair, et \(T(y)=y/2\) si \(y\) est
pair. C'est l'application \(T\) déjà utilisée dans cette mémoire.
\(\mathbb N\) contient \(0\).

**Théorème 1, page 85.** Pour tout réel \(c>\log_4 3\), l'ensemble
\[
M_c=\{y\in\mathbb N:\ (\exists n)\ (T^n(y)<y^c)\}
\]
a une densité asymptotique égale à \(1\). La parenthèse imprimée est
\(0{,}79248125\ldots\). Le calcul donne
\[
\log_4 3=0{,}7924812503\ldots,
\]
donc \(0{,}79248125<\log_4 3<0{,}79248126\). Les chiffres imprimés sont
le début du développement, pas un seuil qui remplacerait \(\log_4 3\).
L'hypothèse reste l'inégalité stricte. L'exposant \(0{,}7925\) du
résumé satisfait \(0{,}7925>\log_4 3\) : c'est un exposant admissible,
pas la borne du théorème.

Korec attribue à Everett et à Terras la densité \(1\) de
\(\{y:(\exists n)\ T^n(y)<y\}\). À la page 86, il écrit que \(n\) dans
(2) n'est pas borné indépendamment de \(y\), et que la preuve permet
de le borner par \(\log_2 y\). Cette parenthèse ne vaut pas pour tout
\(y\in M_c\) (X46). Elle décrit le rang \(m\) des points certifiés dans
la plage (3), pas le premier temps de descente de chaque élément. Cela
ne contredit pas B21 : B21 refuse un horizon uniforme, et X46 refuse
la lecture point par point. Le lemme 1 cite le théorème de périodicité
2.1 de Terras (1976) : \(E_m(x)=E_m(y)\) si et seulement si
\(x\equiv y\pmod{2^m}\). Ce numéro n'est pas identifié au théorème 1.2
lu au cycle 015. Terras n'est pas rouvert, et le lemme 1 n'est pas une
prémisse de B23.

À la page 87, pour \(0<\varepsilon<1\) et \(\log_4 3<c<1\), le texte
imprimé pose
\[
d=\frac12\Bigl(\frac{c}{\log_4 3}+\frac12\Bigr)
\]
et annonce \(\tfrac12<d<c/\log_2 3\). Cette comparaison est fausse
(X45) : comme \(4=2^2\), la formule vaut \(c/\log_2 3+\tfrac14\). Le
choix compatible avec l'inégalité annoncée est
\[
d=\frac12\Bigl(\frac{c}{\log_2 3}+\frac12\Bigr),
\]
ou n'importe quel réel de l'intervalle
\(\tfrac12<d<c/\log_2 3\). Cet intervalle est non vide parce que
\(c>\log_4 3\). Le critère écrit ensuite joint la plage (3), un \(m\)
assez grand, et \(S_m(y)<md\). La seule inégalité \(S_m(y)<md\) n'est
pas ce critère. Elle n'est pas relue comme une preuve du théorème 1.

La page 86 attribue à Allouche une borne plus grande,
\(\tfrac32-\log_3 2=0{,}86907\ldots\). L'identité numérique vaut :
\(\log_3 2=\ln 2/\ln 3\) et la différence commence par \(0{,}8690702464\).
Le texte d'Allouche n'est pas ouvert. Heppner est cité sans constante
explicite et n'est pas ouvert. Les exemples 1 et 2 montrent, pour
d'autres fonctions, qu'une densité \(1\) de temps d'arrêt borné ne
donne pas l'exposant. Ils ne portent pas sur \(T\).

## 2. Densité relative dans une classe

**B23.** Soit \(c>\log_4 3\). Pour tout module \(m\ge 1\) et tout
résidu \(a\), la densité relative de \(M_c\) dans la classe
\(y\equiv a\pmod m\) vaut \(1\). Aucune classe n'est contenue dans le
complémentaire. Cela ne contient pas la classe dans \(M_c\), et cela
ne fait atteindre \(1\) à aucun élément.

La densité de \(M_c\) est celle du théorème 1, non redémontrée. Soit
\(E(x)\) le nombre d'entiers \(y<x\) hors de \(M_c\). Alors
\(E(x)/x\to 0\). La classe \(C\) vérifie, pour \(x>m\),
\[
\#(C\cap[0,x))\ge \frac x m-1.
\]
Les exceptions de la classe sont au plus \(E(x)\), donc leur
proportion dans \(C\) est au plus
\[
\frac{E(x)}{x/m-1}=\frac{E(x)}{x}\cdot\frac{x}{x/m-1}\to 0.
\]
La densité relative de \(M_c\) dans \(C\) vaut donc \(1\). Comme la
classe a une densité \(1/m>0\), elle n'est pas contenue dans un
ensemble de densité \(0\).

X34 empêche de passer de cette densité à l'inclusion. L'ensemble
\(E=\{m!+r:m\ge 1,\ 1\le r\le m\}\) a une densité naturelle nulle et
rencontre chaque classe infiniment souvent. Son complémentaire a une
densité \(1\) et omet une infinité d'éléments de chaque classe. On
n'affirme pas que ce complémentaire est \(M_c\).

## 3. Atteindre 1, et le certificat du premier bloc

Le prédicat de \(M_c\) est l'existence d'un itéré strictement inférieur
à \(y^c\). Pour \(c<1\) et \(y>1\), cette valeur peut dépasser \(1\).
Le théorème 1 ne dit pas qu'elle vaut \(1\).

L'application classique \(\mathrm{Col}\) envoie un impair \(n\) sur
\(3n+1\), puis divise par \(2\). Comme \(3n+1>n\), et comme les deux
applications partagent ensuite la même suite d'impairs, le minimum de
l'orbite positive est le même. En effet, chaque pair est suivi, sous
les deux applications, de l'impair obtenu en retirant toutes les
puissances de \(2\), et cet impair est strictement plus petit. Le
minimum est donc atteint sur un impair, et les impairs coïncident.
Pour \(N\ge 1\),
\[
\mathrm{Col}_{\min}(N)=\inf_{k\ge 0}T^k(N).
\]
L'appartenance à \(M_c\) est \(\mathrm{Col}_{\min}(y)<y^c\). Le point
\(0\) est fixe : \(T(0)=0\). Pour \(c>0\), \(0^c=0\), donc aucun
itéré n'est strictement inférieur à \(0^c\), et \(0\notin M_c\). L'égalité des minima est énoncée pour
les entiers positifs. Le contrôle jusqu'à \(2000\) compare les trente
premiers impairs et les minima jusqu'au premier cycle. Il ne remplace
pas l'argument.

**X43.** La phrase de la page 85, « pour tout entier positif \(y\), il
existe \(n\) tel que \(T^n(y)<y\) », est fausse. Pour \(y=1\),
\(T(1)=2\) et \(T(2)=1\). Aucun terme n'est strictement inférieur à
\(1\).

La conjecture, appelée ici (A), est : pour tout entier \(y\ge 1\), un
itéré vaut \(1\). Soit (B') : pour tout entier \(y\ge 2\), un itéré est
strictement inférieur à \(y\). Alors (A) équivaut à (B'). Si (A) vaut
et \(y\ge 2\), l'itéré \(1\) est inférieur à \(y\). Réciproquement, si
(A) échoue, le plus petit entier positif qui n'atteint pas \(1\) est
au moins \(2\), car \(T^0(1)=1\). Par (B'), il possède un itéré
positif strictement plus petit, qui n'atteint pas \(1\) non plus.
Pour \(y\ge 1\), \(T(y)\ge 1\). Cette équivalence ne décide pas (A).
La phrase imprimée, qui quantifie sur tout entier positif y compris
\(1\), n'est pas (B'). Comme son second membre est faux, elle ne peut
être équivalente à (A) que si (A) est faux. Ce n'est pas le théorème 1,
et ce n'est pas une réfutation de la conjecture.

**X44.** La condition \(S_m(y)<md\), pour un \(d<1\), ne couvre pas
la classe \(y\equiv -1\pmod{2^m}\). Si \(y=2^m t-1\) avec \(m\ge 1\)
et \(t\ge 1\), alors, pour \(0\le i\le m\),
\[
T^i(y)=3^i\,2^{m-i}t-1.
\]
Au rang \(0\), les deux membres valent \(y\). Si la formule vaut au
rang \(i<m\), le terme est impair, car \(m-i\ge 1\). Alors
\[
3T^i(y)+1=3^{i+1}2^{m-i}t-2=2\bigl(3^{i+1}2^{m-i-1}t-1\bigr),
\]
et le pas impair de \(T\) donne la formule au rang \(i+1\). Les \(m\)
termes comptés par \(S_m\) sont les rangs \(0\le i\le m-1\). Ils sont
tous impairs, donc \(S_m(y)=m\). Le rang \(m\), égal à \(3^m t-1\),
n'est pas compté. Cette identité ne dépend pas d'une descente
ultérieure. Pour \(d<1\), \(S_m(y)<md\) est faux. Le \(d\) imprimé est
inférieur à \(1\) lorsque \(c<1\), parce qu'il vaut
\(c/\log_2 3+\tfrac14\) et que \(\log_2 3>\tfrac32\) : en effet
\(2^3=8<9=3^2\), donc
\[
d<\frac1{\log_2 3}+\frac14<\frac23+\frac14=\frac{11}{12}.
\]
On n'utilise pas la comparaison fausse \(d<c/\log_2 3\). Le témoin
\(t=1\) est le nombre de Mersenne \(2^m-1\). Ces entiers peuvent
encore appartenir à \(M_c\) par un itéré ultérieur : \(7\) atteint
\(1\). X44 ne réfute pas le théorème 1. Il dit que l'inégalité
\(S_m(y)<md\) ne place pas toute la classe dyadique dans \(M_c\). Le
critère complet de la preuve, qui contient cette inégalité, ne le
fait pas non plus.

## 4. Comparaison

B20 donne, pour toute \(f\) de limite \(+\infty\), une densité
logarithmique relative \(1\) dans chaque classe. B23 donne, pour un
seul exposant \(c>\log_4 3\), une densité naturelle relative \(1\).
La densité naturelle ne suit pas de la densité logarithmique, et
l'exposant \(y^c\) ne donne pas une fonction arbitraire de limite
infinie. Les deux énoncés ne s'ordonnent pas. Pour la question posée,
les deux sont des comptages. X34, déjà naturel, empêche d'en tirer
une classe entière. Pour tout \(y>1\), atteindre \(1\) implique
l'appartenance à \(M_c\), car \(1<y^c\). Ce n'est pas vrai en \(y=1\) :
\(T^0(1)=1\), mais aucun terme n'est strictement inférieur à \(1\),
donc \(1\notin M_c\). Sur les entiers \(y>1\), l'appartenance à
\(M_c\) reste plus faible que l'atteinte de \(1\) : un itéré peut
passer sous \(y^c\) sans valoir \(1\).

Tao, dans le HTML ar5iv de arXiv:1909.03562, écrit que Korec obtient
\(\mathrm{Col}_{\min}(N)\le N^\theta\) en densité naturelle pour
\(\theta>\log 3/\log 4\approx 0{,}7924\). L'inégalité stricte du
théorème 1 implique cette forme pour le même exposant. Le HTML n'est
pas le PDF de 2022, et le reste de l'article n'est pas relu.
Inselmann, arXiv:2402.03276, reste non audité. Ce n'est pas une raison
de recommencer une échelle d'exposants.

## 5. Statut

B23 est prouvé à partir du théorème 1 lu et du comptage d'une classe.
Le théorème 1 reste un théorème publié. X43 et X44 sont des portées,
pas des contre-exemples au théorème. X45 réfute la comparaison
imprimée sur \(d\). X46 réfute la lecture universelle de la parenthèse
en \(\log_2 y\). Ni l'un ni l'autre ne change B23, et le théorème 1
n'est pas redémontré. Aucune orbite positive n'est exclue. La ligne
de densité, ouverte au cycle 014, s'arrête ici : un raffinement
d'exposant ou une nouvelle densité presque sûre ne force pas davantage
une classe à atteindre \(1\).

## 6. Mises à jour de la mémoire

- `proved.md` : B23, corollaire seulement.
- `hypotheses.md` : H13, fermé.
- `counterexamples.md` : X43, X44, X45 et X46.
- `prior_art.md` : Korec, théorème 1 lu.
- `abandoned.md` : ne pas redémontrer cette densité, ni en tirer une
  classe qui atteint \(1\).
- `agenda.md` : question suivante, axe A, hors densité.
- `reviews.md` : revues `6094283257` et `6094566180`.

## 7. Prochaine question

Axe **A**. Ne pas rouvrir Korec, Tao, Terras, Everett, Inselmann, la
remarque 1.4, \(P(2)\), les conjectures 4.11 à 4.14, Steiner, ni les
\(m\)-cycles.

Eliahou, *Discrete Math.* 118 (1993), borne la longueur d'un cycle non
trivial par les fractions continues de \(\log_2 3\). L'entrée actuelle
est secondaire. Lire l'énoncé primaire. Décider seulement s'il exclut
une trajectoire non périodique, ou seulement un cycle dont le minimum
est dans une plage écrite. S'il ne borne que le nombre d'éléments d'un
cycle, le classer hors des trajectoires divergentes et ne pas
redémontrer l'estimation de fractions continues. Ne pas importer une
vérification machine. Simons–de Weger et Hercher restent fermés sur
leur paramètre \(m\), qui compte des minima et non cette longueur.

Ce cycle est le douzième de la fenêtre dont le plus ancien est le
cycle 006. Le premier commit de ce cycle est `fcd6a00`, du 27 novembre
2026 à 00:25:31 UTC. La fenêtre s'ouvre le 28 novembre 2026 à
00:26 UTC. Le correctif de la revue `6094566180` n'est pas un nouveau
cycle. Ne pas ouvrir le cycle 018 avant que ce correctif ait été relu
indépendamment.

## 8. Reproduire

```sh
python3 research/checks/cycle017_korec_density.py
```

Sortie attendue : 10 lignes `PASS`.

## 9. Revue `6094566180`

Revue indépendante sur le SHA
`5d4ba1bfd01c908a375345ad2c7caec0a5db305b` (PR #27), soumise le
28 novembre 2026 à 00:19 UTC. Ce n'est pas un nouveau cycle. Le
cycle 018 n'est pas ouvert.

B23, l'égalité des minima pour les entiers positifs, X43 et X44 sont
confirmés. Le PDF de Korec a été relu pour la formule de \(d\), la
plage (3), l'équation (4) et la parenthèse de la page 86. Le théorème
1 n'est pas redémontré. Tao n'est pas rouvert.

**X45.** La phrase du §1, « donc \(\tfrac12<d<c/\log_2 3<1\) », ne
suit pas de la formule imprimée. Cette formule est
\[
d=\frac12\Bigl(\frac{c}{\log_4 3}+\frac12\Bigr).
\]
Comme \(4=2^2\), \(\log_4 3=\tfrac12\log_2 3\), donc
\[
d=\frac12\Bigl(\frac{2c}{\log_2 3}+\frac12\Bigr)=\frac{c}{\log_2 3}+\frac14.
\]
L'écart avec \(c/\log_2 3\) est exactement \(\tfrac14\), pour tout
\(c\). La comparaison \(d<c/\log_2 3\) est donc fausse dès que la
formule est celle de la page 87. Pour \(c=\tfrac45\), les
développements commencent par \(0{,}75474380\ldots\) et
\(0{,}50474380\ldots\).

La chaîne \(\tfrac12<d\) reste vraie pour cette formule lorsque
\(c>\log_4 3\) : alors \(c/\log_2 3>\tfrac12\), et
\(d>\tfrac12+\tfrac14=\tfrac34\). La comparaison \(c/\log_2 3<1\)
reste vraie pour \(c<1\), car \(\log_2 3>1\). Seul le maillon
\(d<c/\log_2 3\) tombe.

L'équation (4), page 87, s'écrit
\[
\frac{k}{m}\le\frac{c}{\log_2 3}-\frac{1+2(1-c)\log_2 m}{m}.
\]
Sa dérivation ne dépend pas de la valeur de \(d\). Pour \(c=\tfrac45\) et
\(m=16\), \(\log_2 m=4\), et le terme soustrait vaut
\[
\frac{1+2\cdot\tfrac15\cdot 4}{16}=\frac{13}{80}.
\]
Avec \(k=8\), \(k/m=\tfrac12\). Ce rapport est inférieur au \(d\)
imprimé, car \(\tfrac14<c/\log_2 3\) équivaut à \(\log_2 3<\tfrac{16}5\),
donc à \(3^5=243<2^{16}=65536\). Il est supérieur au membre de droite
de (4), car \(\tfrac12+\tfrac{13}{80}=\tfrac{53}{80}\) et
\(c/\log_2 3<\tfrac{53}{80}\) équivaut à \(\log_2 3>\tfrac{64}{53}\),
donc à \(2^{64}<3^{53}\). Les deux entiers sont
\(18446744073709551616<19383245667680019896796723\). Ainsi
\(k/m<d\) n'entraîne pas (4) pour le \(d\) imprimé.

Le choix
\[
d=\frac12\Bigl(\frac{c}{\log_2 3}+\frac12\Bigr)
\]
satisfait \(\tfrac12<d<c/\log_2 3\) dès que \(\log_4 3<c<1\). En
effet \(c/\log_2 3>\tfrac12\), et ce \(d\) est la moyenne de
\(\tfrac12\) et de \(c/\log_2 3\), donc il est strictement compris
entre les deux. Pour \(c=\tfrac45\), l'hypothèse \(c>\log_4 3\) est
\(4^4=256>243=3^5\). Korec énonce que le terme soustrait tend vers \(0\). Pour \(c<1\) et
\(m\ge 2\), il est positif. N'importe quel réel \(d\) de l'intervalle
rend donc, pour \(m\) assez grand, \(k/m<d\) plus fort que (4).
Le lemme 2 demande seulement \(d>\tfrac12\). On n'en refait pas la
preuve, et on ne réécrit pas la démonstration du théorème 1.

Le critère de la page 87 n'est pas la seule inégalité \(S_m(y)<md\).
L'énoncé lu demande aussi la plage
\[
m\cdot 2^m\le y<a
\]
et \(m\ge n_1(c)\). De cette plage, \(y\ge m\cdot 2^m\), donc
\(\log_2 y\ge m+\log_2 m\) et \(m\le\log_2 y\). Si \(m\ge 2\), alors
\(m<\log_2 y\).

**X46.** La parenthèse de la page 86 ne donne pas, pour tout
\(y\in M_c\), un indice \(n\le\log_2 y\) tel que \(T^n(y)<y^c\).
Pour \(c=1>\log_4 3\) et \(y=27\), le premier tel indice est
\(n=59\), et \(T^{59}(27)=23\). Les termes d'indices \(0\) à \(58\)
sont au moins \(27\). Les cinq derniers termes lus sont
\(122,61,92,46,23\). Comme \(2^4=16<27<32=2^5\), on a
\(\log_2 27<5<59\). Le rang \(m\) de la plage (3) reste, lui, au plus
\(\log_2 y\) pour les points que ce certificat atteint. X46 ne réfute
pas le théorème 1.

**Portée de l'atteinte de \(1\).** Pour \(y>1\), un itéré égal à \(1\)
est strictement inférieur à \(y^c\), donc \(y\in M_c\). Pour \(y=1\),
\(T^0(1)=1\), mais \(1\notin M_c\). Le §4 restreint à \(y>1\) la
phrase qui comparait les deux prédicats. Le point \(0\) reste hors
de \(M_c\), et l'égalité des minima reste restreinte aux positifs.
B23 ne dépend ni de \(d\), ni de cette parenthèse.
