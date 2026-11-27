# Cycle 014 — Tao 2022 n'exclut aucune classe de congruence

Date : 27 novembre 2026. Axe **C**.
Branche : `research/memory`. Script : [`../checks/cycle014_log_density.py`](../checks/cycle014_log_density.py).

**Verdict.** Le théorème 1.3 de Tao, *Forum of Mathematics, Pi* 10 (2022),
e12, est l'énoncé de densité logarithmique. Il a été lu sur le PDF de
la revue. Il n'exclut aucune classe de congruence : l'ensemble
exceptionnel a une densité logarithmique nulle, et un tel ensemble
peut rencontrer toutes les classes (X34). Aucune preuve de la
conjecture, et aucune orbite divergente n'est exclue.

## 0. Revue traitée, question, porte d'antériorité

La revue `6093045943` porte le marqueur `SYRACUSE_INDEPENDENT_REVIEW`
et le SHA `02bcbd97fff10f478ebbc46a5d76862a4b87946a`, tête de la PR #27
au début de ce cycle. Elle confirme le correctif du cycle 013. Elle ne
demande aucune correction. Les bilans \(-84\) et \(148\), la somme
pondérée \(64\) pour tout coefficient entier \(\beta\), les seuils
\(X_0<187\) et \(X_0<123\), et le trajet \(59\to 89\to 67\) ont été
recalculés. Le script du cycle 013 passe encore. Le cycle 013 n'est
pas réécrit.

La fenêtre de douze cycles était fermée jusqu'au 27 novembre 2026 à
21:23 UTC : le commit `adf706a` est du 26 novembre à 21:22:58 UTC. Ce
cycle commence après cet instant.

**Candidat.** Pour toute fonction \(f\) de limite \(+\infty\),
l'ensemble des entiers positifs dont l'orbite de Collatz ne passe pas
sous \(f\) a une densité logarithmique nulle. La question est de
savoir si cet énoncé exclut une classe de congruence, au sens où il
existerait \(m\ge 2\) et un résidu \(a\) tels que chaque entier de la
classe passe sous \(f\).

**Obstacle.** Les cycles 010 à 013 ne retirent aucune orbite
divergente. Une densité nulle n'est pas, à elle seule, une classe
entièrement réglée.

**Intérêt.** Exclure une classe de congruence retirerait une
infinité d'entiers. Une densité logarithmique nulle n'en retire
aucun en particulier.

**Résultat le plus proche.** Tao, *Forum Math. Pi* 10 (2022), e12,
DOI `10.1017/fmp.2022.8`. **[P]** pour la définition 1.2, le théorème
1.3, la remarque 1.4, les théorèmes 1.6 et 3.1, et l'identité (1.2).
PDF de la revue, 56 pages, SHA-256
`55c817c73498f940ed1e70f10208105922f1f7c89e378dcb629040c534151a2b`,
non redistribué. Korec (1994), Terras (1976) et Everett (1977) sont
cités par cet article pour des énoncés de densité naturelle plus
faibles ; ces trois textes ne sont pas rouverts. Le HTML ar5iv de
arXiv:1909.03562v7 (16 juillet 2026) a le même théorème 1.3, inégalité
stricte et densité logarithmique. Les versions v6 et v7 n'ont pas été
comparées au-delà de cet énoncé. L'accès 403 ancien visait une
tentative précédente ; ce PDF-ci a été obtenu.

**Écart.** Aucun sur la densité : le candidat est le théorème 1.3,
réécrit avec le complémentaire. L'exclusion d'une classe entière n'est
pas dans l'article. La remarque 1.4 dit expressément que la borne
constante, pour presque tout entier, reste hors de portée.

**Classement.** DÉJÀ CONNU pour la densité logarithmique, confiance
haute : l'énoncé a été lu sur le PDF de 2022. La phrase « ceci exclut
une classe de congruence » est une lecture trop forte. Elle est
réfutée par X34, qui ne parle pas de l'orbite de Collatz.

**Décision.** NO-GO pour une seconde preuve du théorème 1.3. Le seul
travail de ce cycle est la portée sur les classes de congruence.

## 1. Énoncé lu

La définition 1.2 fixe la densité logarithmique d'un ensemble
\(A\subset\mathbb N+1\) comme la limite, si elle existe, de
\[
\mathbb P\bigl(\mathbf{Log}(\mathbb N+1\cap[1,x])\in A\bigr)
=\frac{\sum_{N\in A,\,N\le x}1/N}{\sum_{N\le x}1/N}.
\]
Une propriété vaut pour presque tout entier positif lorsqu'elle vaut
sur un ensemble de densité logarithmique \(1\).

**Théorème 1.3.** Si \(f:\mathbb N+1\to\mathbb R\) et
\(f(N)\to+\infty\), alors \(\mathrm{Col}_{\min}(N)<f(N)\) pour
presque tout \(N\), au sens de cette densité. Ici
\(\mathrm{Col}(N)=3N+1\) si \(N\) est impair et \(N/2\) si \(N\) est
pair, et \(\mathrm{Col}_{\min}\) est le minimum de l'orbite.

Le résumé imprimé écrit \(\le f(N)\). Les deux formes sont
équivalentes pour la famille de toutes les fonctions de limite
\(+\infty\). Si la forme stricte vaut pour toute telle fonction, elle
implique la forme large. Si la forme large vaut pour toute telle
fonction, on l'applique à \(g=\max(1,f/2)\) : \(g\to+\infty\), et
\(\mathrm{Col}_{\min}\le g\) donne l'inégalité stricte dès que
\(f>0\), donc hors d'un ensemble fini. La preuve du théorème n'est
pas reproduite.

La remarque 1.4 refuse la borne constante : il n'est pas prouvé
qu'un \(C_0\) fixe satisfasse \(\mathrm{Col}_{\min}(N)\le C_0\) pour
presque tout \(N\). L'article juge cette question presque aussi dure
que la conjecture. Le théorème 1.3 équivaut, par l'argument de
diagonalisation de la note 2, à l'existence, pour tout \(\delta>0\),
d'une constante \(C_\delta\) telle que l'inégalité large vaille sur un
ensemble de densité logarithmique inférieure au moins \(1-\delta\).
La forme \(C_\delta\ll\exp(\delta^{-O(1)})\) est celle annoncée via le
théorème 3.1. La constante implicite n'est pas extraite ici.

Le théorème 3.1 donne, pour \(N_0\ge 2\) et \(x\ge 2\),
\[
\mathbb P\bigl(\mathrm{Col}_{\min}(\mathbf{Log}(\mathbb N+1\cap[1,x]))
\le N_0\bigr)
\ge 1-O\bigl(\log^{-c} N_0\bigr),
\]
avec \(c>0\) absolu, non évalué. Pour \(N_0\ge 2\),
\(\mathrm{Col}_{\min}(N)\le N_0\) vaut donc sur un ensemble de
densité logarithmique inférieure \(1-O(\log^{-c} N_0)\). Ce n'est
toujours pas une classe de congruence.

L'identité (1.2) et le théorème 1.6 transportent l'énoncé à
l'application de Syracuse sur les impairs. Pour chaque entier
\(a\ge 0\), la fibre \(v_2(N)=a\) est la classe
\(N\equiv 2^a\pmod{2^{a+1}}\). Le lemme du §2 lui donne la densité
logarithmique \(2^{-(a+1)}\). La partie de cette fibre dont le
minimum passe sous \(f\) a la même densité : le théorème 1.3 en
retire un poids \(o(\log x)\). Presque tout élément de cette classe
est donc bon. La classe entière ne l'est pas. Le paragraphe imprimé
après le théorème 1.6 écrit \(2^{-a}\) et une somme partielle
\(1-2^{-a_0}\). Ces deux valeurs sont fausses (X35, §9). La somme
des densités de \(a=0\) à \(A\) vaut \(1-2^{-(A+1)}\).

## 2. Densité d'une classe

**Lemme.** Soient \(m\ge 1\) et \(r\in\{1,\ldots,m\}\). L'ensemble des
entiers positifs congrus à \(r\) modulo \(m\) a une densité
logarithmique égale à \(1/m\).

Les logarithmes sont népériens. Pour un entier \(x\ge 1\),
\[
\log(x+1)\le\sum_{n\le x}\frac1n\le 1+\log x.
\]
La minoration est l'intégrale de \(1/t\) sur \([1,x+1]\), et la
majoration est \(1+\int_1^x dt/t\).

Soit \(K=\lfloor(x-r)/m\rfloor\), et supposons \(x\ge r\), donc
\(K\ge 0\). La somme de la classe est
\(S=\sum_{k=0}^{K}1/(r+mk)\). La fonction \(t\mapsto 1/(r+mt)\)
décroît. Pour \(0\le k\le K\),
\[
\int_k^{k+1}\frac{dt}{r+mt}\le\frac1{r+mk},
\]
donc
\[
S\ge\int_0^{K+1}\frac{dt}{r+mt}
=\frac1m\log\frac{r+m(K+1)}{r}.
\]
Comme \(r+m(K+1)>x\), on a \(S\ge(1/m)\log(x/r)\). Pour \(k\ge 1\),
\[
\frac1{r+mk}\le\int_{k-1}^{k}\frac{dt}{r+mt},
\]
donc
\[
S\le\frac1r+\frac1m\log\frac{r+mK}{r}
\le\frac1r+\frac1m\log\frac xr.
\]
Le rapport de \(S\) à la somme harmonique est donc coincé entre
\[
\frac{(1/m)\log(x/r)}{1+\log x}
\quad\text{et}\quad
\frac{1/r+(1/m)\log(x/r)}{\log(x+1)}.
\]
Les deux bornes tendent vers \(1/m\). La densité existe et vaut
\(1/m\). Le résidu \(0\) est le cas \(r=m\).

Toute classe de congruence a donc une densité logarithmique
strictement positive. Elle ne peut pas être contenue dans un ensemble
de densité logarithmique nulle. En particulier, pour le théorème 1.3,
aucune classe n'est entièrement contenue dans
\(\{N:\mathrm{Col}_{\min}(N)\ge f(N)\}\). La somme des inverses de
cet ensemble jusqu'à \(x\) est \(o(\log x)\). La somme des exceptions
dans une classe fixée l'est aussi. Divisée par la somme de la classe,
équivalente à \((1/m)\log x\), elle tend vers \(0\). Presque tout
élément de la classe passe sous \(f\). Cela ne dit pas que chaque
élément le fait.

## 3. X34

La nullité de la densité n'implique pas qu'une classe soit évitée.

Soit
\[
E=\{m!+r:m\ge 1,\ 1\le r\le m\}.
\]
Les blocs sont disjoints : pour \(m\ge 1\),
\(m!+m<(m+1)!+1\). La somme des inverses est strictement inférieure à
\(\sum_{m\ge 1}m/m!=\sum_{j\ge 0}1/j!=e\), car
\(1/(m!+r)<1/m!\). La somme harmonique jusqu'à \(x\) est au moins
\(\log x\), donc le rapport des inverses de \(E\) tend vers \(0\). La
densité logarithmique de \(E\) existe et vaut \(0\).

\(E\) rencontre chaque classe infiniment souvent. Fixons \(q\ge 1\) et
un résidu \(b\) avec \(0\le b<q\). Pour \(m\ge q\), \(m!\equiv 0\pmod q\).
Si \(b\ne 0\), les entiers \(m!+b\) avec \(m\ge\max(q,b)\) sont dans
\(E\) et valent \(b\) modulo \(q\). Si \(b=0\), les entiers \(m!+q\)
avec \(m\ge q\) sont dans \(E\) et valent \(0\) modulo \(q\).

Ainsi un ensemble de densité logarithmique nulle peut couper toutes
les classes de congruence. Le même ensemble a une densité naturelle
nulle. Pour \(m\ge 1\), \(m!\ge 2^{m-1}\) : c'est vrai pour \(m=1\),
et \((m+1)!\ge 2\cdot 2^{m-1}\). Si \(m!+1\le x\), alors
\(2^{m-1}\le x\), donc \(m\le 1+\log_2 x\). Le nombre de points de
\(E\) jusqu'à \(x\) est au plus
\(\sum_{m\le 1+\log_2 x}m=O((\log x)^2)\), et le rapport à \(x\) tend
vers \(0\). Le théorème 1.3, dont la conclusion est seulement la
nullité logarithmique, ne fournit aucun couple \((a,m)\) tel que
chaque entier de la classe passe sous \(f\). \(E\) n'est pas proposé
comme ensemble d'exceptions de Collatz.

## 4. Décision

Le théorème 1.3 n'exclut aucune classe de congruence. Il exclut un
ensemble de densité logarithmique nulle. Le corollaire du §2 est
l'énoncé le plus fort que cette nullité donne sur les classes :
presque tout élément de chaque classe fixée passe sous \(f\), et
aucune classe n'est entièrement exceptionnelle. Les deux phrases
laissent une infinité d'exceptions possible dans chaque classe.

C'est B20. La partie de densité est le théorème publié. La partie sur
les classes est élémentaire. Rien ici n'est une découverte, ni une
contrainte sur une orbite.

## 5. Ce que ce cycle ne montre pas

Rien sur (C), sur (H), ni sur Syracuse. La remarque 1.4 laisse ouverte
la borne constante pour presque tout entier, et elle dit qu'une
version explicite, jointe à une vérification numérique, pourrait au
mieux donner la conjecture sur un ensemble de densité logarithmique
positive. Cette possibilité n'est pas réalisée ici. Le remplacement
de la densité logarithmique par la densité naturelle est présenté
comme plausible, pas comme un théorème. Korec, Terras et Everett ne
sont pas relus : leurs énoncés, tels que cités par Tao, sont des
densités naturelles avec un minimum en puissance de \(N\), donc plus
faibles sur la taille du minimum et plus forts sur la densité. Ils
n'excluent pas davantage une classe entière, par le même §3 appliqué
à la densité naturelle. Cette extension n'est pas une prémisse.

Les versions arXiv du 6 et du 16 juillet 2026 ne sont pas auditées.
Seul le théorème 1.3 du HTML v7 a été confronté au PDF de 2022.

## 6. Mises à jour de la mémoire

- `proved.md` : B20.
- `counterexamples.md` : X34.
- `hypotheses.md` : H9, fermée.
- `prior_art.md` : Tao 2022, théorèmes lus.
- `abandoned.md` : ne pas utiliser ce théorème pour exclure une classe.
- `agenda.md` : prochaine question hors de cette densité.
- `reviews.md` : revue `6093045943`, puis `6093468477` au §9.

## 7. Prochaine question

Les cycles 010 à 014 n'ont pas exclu d'orbite divergente. Tao règle
presque tout élément de chaque classe fixée, et aucune classe
entière. Ne pas raffiner cette densité, ni relire le théorème 1.3
pour en tirer une borne constante. La correction de la revue
`6093468477` est au §9. Le cycle 015 n'est pas ouvert : il attend
la relecture de ce correctif, puis la fenêtre datée ci-dessous.

Axe **A**, après le budget ci-dessous. Existe-t-il un module \(m\ge 2\),
un résidu \(a\) et une borne \(T\) tels que tout entier \(n>1\)
congru à \(a\) modulo \(m\) admette un temps \(t\le T\) avec
\(U^t(n)<n\) et \(U^t(n)\equiv a\pmod m\), où
\(U(n)=(3n+1)/2^{v_2(3n+1)}\) ? Une telle classe se contracterait
dans elle-même.

Le premier candidat de la porte est le cas d'un seul vecteur de
valuations, constant sur une classe modulo \(2^L\). L'affinité de
Syracuse donne alors un coefficient \(3^t 2^{L-S}\) en la variable
de la classe. Si cette obstruction est déjà dans Terras, Everett ou
Lagarias, ne pas la redémontrer. Le travail du cycle est alors
l'union finie de vecteurs. Pas de retour à Tao, à B17, à B18, à B19,
au signe moins, au mot du cycle 006, à \(5\cdot 2^k-1\), aux
conjectures 2 et 3 de Berg–Meinardus, ni aux théorèmes 4.2.7 et
4.3.10 de Mori.

Le cycle 014 est le douzième de la fenêtre ouverte par le cycle 003.
Le premier commit de ce cycle est `0c90981`, du 26 novembre 2026 à
22:00:44 UTC. Ne pas ouvrir le cycle 015 avant le 27 novembre 2026
à 22:01 UTC.

## 8. Reproduire

```sh
python3 research/checks/cycle014_log_density.py
```

Sortie attendue : cinq lignes `PASS`. Les deux premières sont
numériques : le sandwich du §2 jusqu'à \(x=20000\), pour les modules
\(1,2,3,8,24\), et la somme des inverses du témoin comparée à
\(\sum m/m!\), toutes deux en flottants. La troisième trouve, pour
chaque module \(q\le 8\), au moins deux points de \(E\) dans chaque
résidu. La quatrième vérifie en fractions les \(78\) identités de
fibres et les deux sommes de densités. La cinquième vérifie en
entiers les blocs, les résidus pour \(q\le 30\), et la borne de
comptage. Ces contrôles ne sont pas la preuve de la limite, ni celle
de l'infinité des rencontres.

## 9. Revue `6093468477`

Revue indépendante sur le SHA
`be519ce67c3acf569e11384f3626bc758011d9e2` (PR #27), c'est-à-dire sur
B20 et X34. La définition 1.2, l'inégalité stricte du théorème 1.3,
l'hypothèse \(f(N)\to+\infty\), la forme du théorème 3.1 et X34 sont
confirmés. Une densité du §1 est corrigée. Ce n'est pas un nouveau
cycle. Le cycle 015 n'est pas ouvert.

La fibre est exacte : \(N=2^a(2k+1)=2^{a+1}k+2^a\), donc
\(N\equiv 2^a\pmod{2^{a+1}}\), et la réciproque dit que \(2^a\)
divise \(N\) sans que \(2^{a+1}\) le divise. Le §2 donne la densité
\(2^{-(a+1)}\). Pour \(a=0\), ce sont les impairs, de densité \(1/2\).
La valeur imprimée \(2^{-a}\) vaudrait \(1\) dans ce cas.

La partie bonne a la même densité. L'ensemble
\(\{N:\mathrm{Col}_{\min}(N)\ge f(N)\}\) a, par le théorème 1.3, une
somme d'inverses \(o(\log x)\). La retirer à la fibre ne change pas
la densité. On peut aussi passer par le théorème 1.6. L'identité
(1.2) se vérifie directement : si \(N=2^am\) avec \(m\) impair, les
termes de \(N\) à \(2m\) sont au moins \(m\), et chaque terme pair
ultérieur est un multiple strict d'un impair ultérieur. Le minimum
de l'orbite est donc \(\mathrm{Syr}_{\min}(m)\). La fonction
\(m\mapsto f(2^am)\) tend vers \(+\infty\). Le théorème 1.6 dit que
les impairs qui satisfont l'inégalité ont une densité absolue \(1/2\).
La dilatation \(N=2^am\) multiplie chaque inverse par \(2^{-a}\), donc
la densité absolue de la fibre bonne est \(2^{-(a+1)}\).

La somme de \(a=0\) à \(A\) des densités correctes est
\(1-2^{-(A+1)}\). Le complémentaire est la classe des multiples de
\(2^{A+1}\), de densité \(2^{-(A+1)}\). La somme des coefficients
imprimés \(2^{-a}\) vaut \(2-2^{-A}\). Elle vaut \(1\) pour \(A=0\),
et elle dépasse \(1\) pour \(A\ge 1\). La somme
imprimée \(1-2^{-a_0}\) est la densité des \(v_2<a_0\), pas celle des
\(v_2\le a_0\). Les deux valeurs du paragraphe sont donc fausses, et
elles ne s'accordent pas entre elles. La limite \(A\to\infty\) couvre
encore une densité \(1\), des deux façons. Les théorèmes 1.3 et 1.6,
eux, restent : ce paragraphe n'est pas leur preuve.

Ce paragraphe est celui de la page 4 du PDF de *Forum Math. Pi*,
empreinte SHA-256
`55c817c73498f940ed1e70f10208105922f1f7c89e378dcb629040c534151a2b`,
relu pour ce correctif. Le HTML ar5iv porte la même phrase. Elle
n'est pas recopiée. X35 est cette réfutation. Elle ne retire aucune
orbite.

Le §4 et le résumé de B20 disent désormais : presque tout élément de
chaque classe fixée. Le §2 le démontrait déjà pour une classe
arbitraire. La phrase « presque toute classe » laissait le
quantificateur ambigu.

X34 est inchangé sur la densité logarithmique. La borne de comptage
ci-dessus donne aussi la densité naturelle nulle. Pour \(m\ge q\),
les \(q\) premiers points du bloc \(m!+r\) couvrent tous les résidus
modulo \(q\), puisque \(m!\equiv 0\pmod q\). La remarque 1.4, borne
constante sur un ensemble de densité logarithmique \(1\), reste
ouverte et n'est pas la prochaine question.

Le contrôle indépendant est le script. Les \(78\) identités, pour
\(x\in\{1,2,31,256,1024,4096\}\) et \(0\le a\le 12\), comparent en
fractions la somme de la fibre à \(2^{-a}\) fois la somme des
impairs jusqu'à \(\lfloor x/2^a\rfloor\). Les sommes
\(2-2^{-A}\) et \(1-2^{-(A+1)}\) sont des égalités de fractions. Les
blocs \(1\le m\le 40\) sont disjoints, \(m!\ge 2^{m-1}\), et pour
\(1\le q\le 30\) les blocs \(m=q,q+1,q+2\) couvrent chaque résidu
dans leurs \(q\) premiers points. Le sandwich jusqu'à \(x=20000\)
reste un contrôle en flottants. Aucun de ces contrôles n'est la
preuve de la limite.
