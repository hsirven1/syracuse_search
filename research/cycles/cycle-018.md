# Cycle 018 — Eliahou 1993 borne un cycle, pas une trajectoire divergente

Date : 28 novembre 2026. Axe **A**, puis arrêt de cette série de portées.
Branche : `research/memory`. Script : [`../checks/cycle018_eliahou_scope.py`](../checks/cycle018_eliahou_scope.py).

**Verdict.** Les phrases obtenues bornent le nombre d'éléments d'un
cycle. Une orbite positive non bornée n'est pas un cycle (B24). Aucune
de ces phrases ne l'exclut. Le PDF de *Discrete Math.* 118 (1993) n'a
pas été obtenu : la forme linéaire n'est pas adoptée, et l'estimation
de fractions continues n'est pas refaite. Aucune preuve de Syracuse.

## 0. Revue traitée, question, porte d'antériorité

La revue `6094661090` porte le marqueur `SYRACUSE_INDEPENDENT_REVIEW`
et le SHA `2a62373e03faa22836505a759d7eebfc06f5be10`, tête de la PR #27
au début de ce cycle. Elle confirme X47. Le logarithme de
\((m^2 2^m)^{1-c}3^k\le 2^{m-1}\) donne le seuil \(c/L-A_m/L\).
L'équation (4) soustrait \(A_m\) et implique l'inégalité de puissances.
Pour \(c=\tfrac45\), \(m=16\) et \(k=6\), (4) échoue et l'inégalité de
puissances tient. Pour \(k=8\), les deux échouent. B23 ne dépend pas
de l'équivalence. Elle ne demande aucune correction. Le script du
cycle 017 n'est pas relancé : la revue dit que ses chiffres viennent
de son propre calcul. Le cycle 017 n'est pas réécrit.

La fenêtre de douze cycles contient, au 28 novembre 2026 à 00:46 UTC,
les cycles 008 à 017. Le premier commit du cycle 008 est `ff58fed`,
du 27 novembre à 01:09:59 UTC. Le cycle 007, `a60a1a6`, du 27 novembre
à 00:45:58 UTC, est sorti. Ce cycle est le onzième de la fenêtre.

**Candidat.** Eliahou, *Discrete Math.* 118 (1993), 45–56, exclut une
trajectoire non périodique, ou seulement un cycle dont le minimum est
dans une plage écrite.

**Obstacle.** L'entrée de `prior_art.md` était secondaire. Une borne
sur le nombre d'éléments d'un cycle ne retire aucune orbite infinie.
Refaire l'approximation de \(\log_2 3\) ne changerait pas ce point.

**Intérêt.** Si le théorème forçait toute trajectoire non périodique à
retomber, il exclurait les orbites divergentes. S'il ne borne qu'un
cycle, il laisse ouverte la moitié (B) de la conjecture, au sens séparé
par Halbeisen–Hungerbühler.

**Résultat le plus proche.** Le texte primaire de 1993. Le PDF de
ScienceDirect répond 403 (Cloudflare). L'archive UNIGE `unige:12087`
n'a pas de fichier. La copie Wayback du 7 janvier 2023 ne contient que
le résumé. À la place, quatre textes ont été lus, et aucun n'est le
corps de l'article :

1. Le résumé, identique sur l'archive UNIGE et sur cette copie
   Wayback. \(T(n)=n/2\) si \(n\) est pair, \(T(n)=(3n+1)/2\) si \(n\)
   est impair. « We show, among other things, that any nontrivial
   cyclic orbit under iteration of \(T\) must contain at least
   17087915 elements. »
2. Le compte rendu zbMATH 0786.11012, page zbMATH de l'article. Pour
   un cycle non trivial avec \(\min\Omega>2^{40}\),
   \[
   \mathrm{Card}\,\Omega=301994\,a+17087915\,b+85137581\,c,
   \]
   \(a,b,c\ge 0\), \(b>0\), \(ac=0\).
3. Lagarias, bibliographie annotée, arXiv `math/0309224`, entrée 53.
   PDF SHA-256
   `99fd33f3fd78f24da07df625f32cdfb0edefd7c33b663fef20ff565cfd077c71`,
   74 pages, non redistribué. L'extraction de la page 23 aplatit
   l'exposant : les caractères lus sont « \(n<240\) ». Le HTML ar5iv
   du même e-print a l'annotation \(n<2^{40}\). La phrase dit que tout
   cycle non trivial a cette période, et que la méthode utilise les
   fractions continues de \(\log_2 3\) et la conjecture pour
   \(n<2^{40}\).
4. Halbeisen–Hungerbühler, *Acta Arith.* 78 (1997), 227–239 au moins
   pour les pages citées. PDF d'auteur
   `https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf`,
   SHA-256
   `5cca38671bdd8a85f7d85538029853c1d0bb0d87f973cd02ab59affce2b1cbee`,
   non redistribué. Lus : l'introduction (pp. 227–228), la définition
   de \(n(l)\) dans la proposition 1, le §4.2 et la première phrase
   du §5 (p. 238). Les théorèmes 3 et 4 et leurs preuves ne sont pas
   adoptés.

**Écart.** Le résumé quantifie sur les orbites cycliques non triviales.
Le compte rendu zbMATH met la forme linéaire sous l'hypothèse
\(\min\Omega>2^{40}\). Lagarias énonce la même forme pour tout cycle
non trivial, en nommant la vérification jusqu'à \(2^{40}\) comme
partie de la méthode. Ces deux paraphrases ne sont pas la même
quantification. Le corps de 1993 n'a pas été lu : aucune des deux
n'est adoptée. Le critère imprimé par Halbeisen–Hungerbühler est
encore un autre énoncé, attribué à Eliahou, et il borne \(|C|\) pour
un cycle.

**Classement.** ANTÉRIORITÉ NON VÉRIFIÉE pour les hypothèses exactes
du corps de 1993, confiance haute sur l'absence du PDF, pas sur le
théorème. La phrase « ceci exclut une trajectoire non périodique » ne
suit d'aucune phrase lue. Elle est plus faible que ce que ces phrases
disent, puisqu'elles ne parlent que de cycles. Le nombre
\(17087915\) est un corollaire cité, pas un calcul de ce cycle.
DÉJÀ CONNU comme borne de longueur de cycle, au niveau du résumé et
des sources secondaires. Pas une nouveauté.

**Décision.** NO-GO pour redémontrer l'estimation de fractions
continues, pour calculer \(k(2^{40})\) comme question du cycle, et
pour importer la vérification machine jusqu'à \(2^{40}\) ou au-delà.
Le seul travail de ce cycle est la portée sur les trajectoires non
périodiques, plus l'équivalence élémentaire B24 qui rend cette portée
précise. La revue `6094741450` a ensuite contrôlé ce \(k\). Le §8 le
vérifie pour le critère imprimé et ne reprend pas l'estimation. Les
théorèmes 3 et 4 de Halbeisen–Hungerbühler ne sont pas ouverts : ce
sont encore des bornes de longueur de cycle. Leur \(m\) n'est pas
celui de Simons–de Weger.

## 1. Énoncés lus

Le résumé ne dit pas qu'une trajectoire non périodique a un cardinal
fini. « Among other things » laisse ouverte la possibilité d'un autre
théorème dans le corps. Ce corps n'a pas été lu. Le titre de l'article
est une borne sur les longueurs de cycles non triviaux. Le compte
rendu zbMATH ne décrit que le résultat de cycle. Rien de lu n'attribue
à cet article l'exclusion d'une orbite divergente.

Halbeisen–Hungerbühler séparent la conjecture en deux :
(A) le seul cycle dans \(\mathbb N\) est \((1,2)\) ;
(B) toute suite de Collatz dans \(\mathbb N\) est bornée.
Leur (E), cité d'Eliahou, est une borne de longueur pour un cycle qui
ne contient pas \(1\). Leur théorème 2, attribué à Eliahou, s'énonce
ainsi. Si \(k(m)\) est le plus petit entier \(k\) tel que
\[
\frac{k}{n(k)}\le\log_2\Bigl(3+\frac1m\Bigr),
\]
alors tout cycle de Collatz \(C\) dans \(\mathbb N\) vérifie
\(|C|\ge k(\min C)\). Ils ajoutent que les fractions continues donnent
\(k(2^{40})=17087915\), et que cette valeur se relit sur la définition.
Cette valeur est établie au §8 pour ce critère imprimé. Ce calcul ne
vérifie pas les entiers inférieurs à \(2^{40}\). La fonction \(n(l)\) de leur
proposition 1 est le plancher de \(l\log_3 2\) : l'extracteur remplace
le symbole de plancher, et le lemme 6 écrit
\(l\log_3 2-1\le n\le l\log_3 2\). Le contrôle utilise
\(n(l)=\max\{n:3^n\le 2^l\}\), qui est ce plancher.

La première phrase lue du §5 dit que ces estimations de longueur, même
étendues aux cycles rationnels, ne peuvent pas prouver (A), parce que
le minimum d'un cycle rationnel croît au plus linéairement avec la
longueur. Elles ne disent rien de (B).

## 2. Équivalence élémentaire

**B24.** Soit \(n\ge 1\). Pour l'application \(T\) du résumé, les trois
propriétés suivantes sont équivalentes :

1. l'ensemble \(\{T^k(n):k\ge 0\}\) est fini ;
2. la suite des parités est ultimement périodique ;
3. un itéré appartient à un cycle.

Si l'orbite est finie, la suite infinie des valeurs répète une valeur.
Comme \(T\) est une fonction, la queue à partir de la première
répétition est périodique. Cette valeur appartient à un cycle, et la
suite des parités est ultimement périodique. Un cycle ne prend qu'un
nombre fini de valeurs, et un préfixe fini suivi d'un cycle reste
fini.

Le sens restant part de la suite des parités. Soient \(s\ge 0\) le
début de sa périodicité et \(p\ge 1\) une période. Posons
\(x=T^s(n)\) et \(y=T^{s+p}(n)\). Les parités de \(x\) et de \(y\)
coïncident à tout rang. Le cycle 015 §10 traite ce cas pour un entier
positif quelconque : \(k\) parités communes donnent une congruence
modulo \(2^k\). Un pas pair envoie la différence sur sa moitié. Un pas
impair la multiplie par \(3\) puis la divise par \(2\), et \(3\) est
impair. Une période dès le rang \(0\) donne donc la congruence modulo
toute puissance de \(2\), et \(x=y\).

La même identité s'écrit
\[
T^j(x)-T^j(y)=\frac{3^{a_j}(x-y)}{2^j},
\]
où \(a_j\) compte les pas impairs parmi les \(j\) premiers. Les
branches coïncident, donc les termes inhomogènes s'annulent. Le membre
de gauche est entier et \(3^{a_j}\) est impair, donc \(2^j\) divise
\(x-y\).

Ainsi \(T^{s+p}(n)=T^s(n)\). La queue des valeurs est périodique,
l'orbite est finie, et \(T^s(n)\) appartient à un cycle. Pour \(5\),
la suite commence par \(5,8,4,2,1,2,1\). Le premier rang d'une
période \(2\) est \(s=3\), car \(T^3(5)=T^5(5)=2\). On peut aussi
prendre \(s=4\) : \(T^4(5)=T^6(5)=1\). La parité du rang \(2\) est
paire et celle du rang \(4\) est impaire, donc aucune période \(2\)
ne commence à un rang \(s\le 2\) (X49).

La phrase « une suite ultimement périodique d'entiers positifs ne
prend qu'un nombre fini de valeurs » porte sur la suite des valeurs.
Elle ne ferme pas le sens qui part des parités (X48). Ce sens est le
cycle 015 §10 appliqué à \(x\), pas un théorème nouveau. Terras,
théorème 1.2, déjà lu au cycle 015, énonce l'équivalence entre
vecteurs d'encodage et congruences. Il n'est pas relu.
Bernstein–Lagarias, §1, (1.3) et (1.5), sont cités par la revue
`6094741450` pour la même injectivité. Ce PDF n'est pas ouvert ici et
n'est pas une prémisse.

Donc une orbite positive non bornée n'est pas un cycle, et son
itinéraire de parité n'est pas ultimement périodique. Le résumé, le
compte rendu zbMATH, l'entrée 53 de Lagarias et le théorème 2 lu chez
Halbeisen–Hungerbühler concluent tous une borne sur le cardinal d'un
cycle. Aucun ne s'applique à cette orbite.

Ce n'est pas un théorème d'Eliahou. C'est le partage entre une orbite
finie et une orbite infinie. L'orbite de \(1\) est le cycle
\(\{1,2\}\). L'orbite de \(5\) entre dans ce cycle et reste finie.
Aucun entier positif dont l'orbite diverge n'est connu : B24 ne dit
pas qu'il n'en existe pas.

## 3. Le cycle trivial et la forme linéaire

\(T(1)=2\) et \(T(2)=1\). Le cardinal est \(2\). Pour \(m=1\),
\(\log_2(3+1/m)=2\). Le plus petit \(k\) tel que \(n(k)\ge 1\) et
\(k\le 2n(k)\) est \(k=2\), car \(n(1)=0\) et \(n(2)=1\). Ainsi
\(k(1)=2\), et le cycle trivial réalise l'égalité du théorème 2 tel
qu'il est imprimé. Cette égalité ne force pas la longueur
\(17087915\).

La forme linéaire avec \(b\ge 1\) vaut au moins \(17087915\). Le cycle
\(\{1,2\}\) n'y entre pas. Cela explique le mot « nontrivial » du
résumé et de Lagarias, et l'hypothèse \(\min\Omega>2^{40}\) du compte
rendu. Ce n'est pas une réfutation de ces phrases : elles excluent
déjà le cycle trivial, ou elles demandent un grand minimum. Comme les
deux paraphrases de la forme linéaire n'ont pas le même quantificateur
et que le corps n'a pas été lu, la forme n'est pas inscrite comme
théorème.

## 4. Statut

B24 est prouvé, et il est élémentaire. Le chaînon des parités est
celui du cycle 015 §10, appliqué à la queue (X48, §8). Le résumé
d'Eliahou est lu. Le fac-similé de 1993 reste non obtenu. La
transcription OCR citée par la revue n'est pas ce fac-similé, et elle
n'est pas lue ici. La forme linéaire reste non adoptée. Le nombre
\(k(2^{40})=17087915\) est celui du critère de Halbeisen–Hungerbühler,
pas une borne sur tout cycle non trivial. La vérification machine
n'est pas une prémisse. Les théorèmes 3 et 4 de
Halbeisen–Hungerbühler ne sont pas adoptés. La note ajoutée à la
page 239, qui invoque une vérification jusqu'à \(3\cdot 2^{50}\), n'est
pas une prémisse. Simons–de Weger et
Hercher ne sont pas rouverts : leur paramètre compte des minima, pas
cette longueur. Aucune orbite divergente n'est exclue. La série des
lectures de portée, cycles 014, 016, 017 et 018, s'arrête sur les
densités et sur les bornes de longueur de cycle.

## 5. Mises à jour de la mémoire

- `proved.md` : B24, équivalence élémentaire.
- `hypotheses.md` : H14, fermé pour la portée, corps non lu.
- `prior_art.md` : Eliahou passe de [S] au résumé lu ; Halbeisen–
  Hungerbühler et l'entrée 53 de Lagarias sont ajoutés.
- `abandoned.md` : ne pas redémontrer la borne, ni en tirer une
  orbite divergente.
- `agenda.md` : question suivante, axe B, hors de cette série.
- `reviews.md` : revues `6094661090` et `6094741450`.

## 6. Prochaine question

Axe **B**. Ne pas rouvrir les densités, les bornes de longueur de
cycle, Crandall, Halbeisen–Hungerbühler au-delà du §4.2 déjà lu,
Simons–de Weger, Hercher, \(P(2)\), le signe moins, ni la famille
appariée.

Bernstein–Lagarias, *Canad. J. Math.* 48 (1996), 1154–1169, est cité
par les revues `6082358798` et `6082438456` pour le §1, (1.5)–(1.6),
et le PDF n'a jamais été ouvert. Le lire seulement pour ces deux
affichages. Décider s'ils prouvent que tout rationnel de \(\mathbb Z_2\)
a un itinéraire ultimement périodique, ou s'ils laissent cette
direction comme conjecture. Si ce n'est que H3, NO-GO, et ne pas
redémontrer la conjugaison. B24 dit déjà qu'un entier positif a un
itinéraire ultimement périodique si et seulement si son orbite est
bornée : ne pas le réécrire. Ne pas ouvrir ce cycle avant la relecture
indépendante du correctif du §8.

## 7. Reproduire

```sh
python3 research/checks/cycle018_eliahou_scope.py
```

Sortie attendue : 12 lignes `PASS`.

## 8. Revue `6094741450`

Revue indépendante sur le SHA
`8e1574c1f16b9969e2fdf71bc1b4ff212568f55e` (PR #27), soumise le
28 novembre 2026 à 00:48 UTC. Ce n'est pas un nouveau cycle. Le
cycle 019 n'est pas ouvert.

B24 et la portée sur les cycles sont confirmés. Le §2, dans sa
première rédaction, n'établissait pas le retour depuis une suite de
parités ultimement périodique.

**X48.** La phrase « une suite ultimement périodique d'entiers
positifs ne prend qu'un nombre fini de valeurs » est vraie pour la
suite des valeurs. Elle ne dit rien d'une suite de parités. Le sens
manquant est ajouté au §2. Pour \(i\ge s\), les parités de période
\(p\) donnent deux entiers positifs \(x=T^s(n)\) et
\(y=T^{s+p}(n)\) dont les suites de parités coïncident dès le rang
\(0\). Le cycle 015 §10 donne alors \(x=y\). L'identité affichée par
la revue est la même descente de valuation : après \(j\) branches
communes, la différence vaut \(3^{a_j}(x-y)/2^j\). Le témoin
\(5\to 8\to 4\to 2\to 1\to 2\to 1\) admet le choix \(s=4\), car
\(T^4(5)=T^6(5)=1\). Le premier rang est \(s=3\) (X49). Les mots de
longueur \(1\le j\le 10\) sont injectifs sur \(1,\ldots,2^j\).
Bernstein–Lagarias, §1, (1.3) et (1.5), restent non ouverts.

**Accès au corps de 1993.** Le fac-similé n'est pas obtenu.
ScienceDirect sert le PDF à l'adresse payante, et l'archive UNIGE
`unige:12087` n'a toujours pas de fichier. La revue cite une
transcription OCR,
`https://www.scribd.com/document/1037372410/1-s2-0-0012365X9390052U-main`.
La page obtenue ici est un défi JavaScript de 3036 octets, intitulé
« Client Challenge ». Elle ne contient pas l'article. Cette
transcription n'est pas le fac-similé, et elle n'est pas lue. Les
calculs historiques jusqu'à \(2^{40}\) ne sont pas audités. Le
théorème 1.1 et la §4, tels que la revue les lit sur cette
transcription, ne sont donc pas adoptés. La phrase conditionnelle
\(\min\Omega>2^{40}\) reste celle du compte rendu zbMATH. La phrase
pour tout cycle non trivial reste celle de l'entrée 53 de Lagarias.
Les deux quantificateurs ne sont pas identifiés sur le corps.

**Critère imprimé.** Pour le théorème 2 de Halbeisen–Hungerbühler,
\(n(\ell)=\lfloor\ell\log_3 2\rfloor\), et \(k(m)\) est le plus petit
entier \(k\ge 1\) tel que \(n(k)\ge 1\) et
\(k/n(k)\le\log_2(3+1/m)\). Pour \(m=2^{40}\), ce \(k\) vaut
\(17087915\), et \(n(k)=10781274\).

Soient
\[
B=\frac{16785921}{10590737},\quad
M=\frac{17087915}{10781274},\quad
A=\frac{301994}{190537}.
\]
\(M\) est le médian de \(B\) et de \(A\), et
\(301994\cdot 10590737-16785921\cdot 190537=1\). Toute fraction
strictement comprise entre ces voisins a un numérateur au moins égal
à \(17087915\). Les séries de \(\log 2\) et de \(\log(3/2)\), coupées
au rang \(100\), et la série de \(\log(1+1/(3\cdot 2^{40}))\), bornée
après deux termes par en dessous et après trois termes par au-dessus,
donnent le placement des quatre nombres. Le reste de \(\log 2\) est
strictement inférieur à \(1/(101\cdot 2^{100})\). Le reste de la série
alternée de \(\log(3/2)\) est strictement plus petit que son terme
suivant, et de même signe. Ces bornes donnent
\[
B<\log_2 3<M<\log_2(3+2^{-40})<A.
\]
L'intervalle cible est donc contenu entre les voisins, et \(M\) y
appartient. De plus \(10781274<k/\log_2 3<10781275\), donc
\(n(k)\) est ce dénominateur et la fraction du critère est \(M\).

Ce calcul ne vérifie aucun entier inférieur à \(2^{40}\). Il ne
transporte pas la forme linéaire à tout cycle non trivial. La forme
n'est pas adoptée. B24 n'en dépend pas. Aucune orbite divergente
n'est exclue.

## 9. Revue `6094774532`

Revue indépendante sur le SHA
`0c4a251b62e376d1a63d20620e13642132f0828f` (PR #27), soumise le
28 novembre 2026 à 00:57 UTC. Ce n'est pas un nouveau cycle. Le
cycle 019 n'est pas ouvert.

B24, X48 et le certificat \(k(2^{40})=17087915\) sont confirmés.
L'identité de différence et l'injectivité du codage restent celles
du §2. La portée au-dessus de \(2^{40}\) reste celle du §8 : les
calculs historiques ne sont pas audités, et la forme linéaire n'est
pas adoptée. Bernstein–Lagarias, §1, (1.3) et (1.5), restent non
ouverts. Halbeisen–Hungerbühler, proposition 1 et §4.2, étaient déjà
lus ; ce PDF n'est pas rouvert.

**X49.** Les §§2 et 8 disaient que la période de \(5\) commence au
rang \(4\). La suite est \(5,8,4,2,1,2,1,\ldots\). Le premier rang
d'une période \(2\) est \(s=3\), car \(T^3(5)=T^5(5)=2\), et la
queue à partir de ce rang est \(2,1,2,1,\ldots\). La parité du rang
\(2\) est paire et celle du rang \(4\) est impaire. Une période \(2\)
commençant à un rang \(s\le 2\) identifierait ces deux parités, car
les rangs \(2\) et \(4\) seraient tous deux dans la queue et distants
de \(2\). On peut prendre \(s=4\) : \(T^4(5)=T^6(5)=1\), et la queue
est \(1,2,1,2,\ldots\). Ce choix illustre le retour ; il n'est pas le
premier rang. B24 ne dépend pas de cet exemple.

Le script donne 12 lignes `PASS`.
