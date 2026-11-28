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
continues, pour calculer \(k(2^{40})\), et pour importer la
vérification machine jusqu'à \(2^{40}\) ou au-delà. Le seul travail
est la portée sur les trajectoires non périodiques, plus l'équivalence
élémentaire B24 qui rend cette portée précise. Les théorèmes 3 et 4
de Halbeisen–Hungerbühler ne sont pas ouverts : ce sont encore des
bornes de longueur de cycle. Leur \(m\) n'est pas celui de
Simons–de Weger.

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
Cette valeur n'est pas recalculée ici. La fonction \(n(l)\) de leur
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

Si l'orbite est finie, la suite infinie des itérés répète une valeur.
Comme \(T\) est une fonction, la queue à partir de cette valeur est
périodique. Un cycle ne prend qu'un nombre fini de valeurs, et un
préfixe fini suivi d'un cycle reste fini. Une suite ultimement
périodique d'entiers positifs ne prend qu'un nombre fini de valeurs.

Donc une orbite positive non bornée n'est pas un cycle, et son
itinéraire n'est pas ultimement périodique. Le résumé, le compte rendu
zbMATH, l'entrée 53 de Lagarias et le théorème 2 lu chez
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

B24 est prouvé, et il est élémentaire. Le résumé d'Eliahou est lu.
Le corps de 1993 reste non obtenu. La forme linéaire reste non
adoptée. Le nombre \(17087915\) n'est pas recalculé. La vérification
machine n'est pas une prémisse. Les théorèmes 3 et 4 de
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
- `reviews.md` : revue `6094661090`.

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
indépendante du présent cycle.

## 7. Reproduire

```sh
python3 research/checks/cycle018_eliahou_scope.py
```

Sortie attendue : 6 lignes `PASS`.
