# Cycle 011 — L'équation de Berg–Meinardus ne donne pas de lemme de descente

Date : 27 novembre 2026. Axe **C**.
Branche : `research/memory`. Script : [`../checks/cycle011_berg_meinardus.py`](../checks/cycle011_berg_meinardus.py).

**Verdict : reformulation déjà publiée. Pas de contrainte nouvelle sur
une trajectoire, et pas de lemme de descente.**
La note de 1995 énonce deux versions analytiques de la conjecture.
Pour les entiers \(n\ge 1\), la seconde conjecture est exactement
« un itéré vaut \(1\) » (B16). La troisième quantifie sur les fonctions
holomorphes du disque. Le seul théorème prouvé dans la note au-delà de
ces énoncés, le théorème 3, dit que toute solution entière est constante.
Il n'exclut aucune orbite entière. Le PDF de 1994, où la note place les
preuves d'équivalence, n'a pas été obtenu.

La revue `6082791301` corrige le résidu du §5 (X30). L'identité de
fractions partielles reste vraie, par séries géométriques. L'équivalence
annoncée entre la conjecture 3 et l'atteinte de \(1\), pour \(n\ge 1\),
est écrite au §12 : les coefficients de (18) donnent \(a_n=a_{t(n)}\),
et le témoin indicateur est celui du théorème 1 de Meinardus 2001, lu.
Ce n'est toujours pas une descente. L'article de 1994 n'est pas une
prémisse de cet argument.

## 0. Question traitée, et porte d'antériorité

La revue `6082693818` confirme le correctif d'exemples du cycle 010 sur
le SHA `7b5a225387402859bfd0679032a73091972258b8`. Elle ne demande aucune
correction. Les sorties \(19\) et \(1367\), et les exposants extraits
\(4\) et \(1\), sont ceux déjà écrits. Le cycle 010 n'est pas réécrit.

**Candidat.** L'équivalence publiée par Berg et Meinardus entre la
conjecture et une équation fonctionnelle holomorphe donne-t-elle, pour
un entier, une contrainte qui ne soit pas déjà B12, ou bien est-elle une
reformulation globale sans lemme de descente ?

**Obstacle.** B12 est une équivalence par premier retour. Une équation
holomorphe pourrait, en principe, interdire une orbite divergente par
une obstruction de prolongement, sans passer par les classes modulo \(18\).

**Intérêt.** Si l'énoncé contrôlait une trajectoire arbitraire par une
inégalité ou par l'absence d'une singularité vérifiable, ce serait un
mécanisme d'axe C. S'il répète seulement « tout entier atteint \(1\) »,
il ne fait pas avancer l'exclusion des contre-exemples.

**Résultat le plus proche.**
- Berg–Meinardus, *Rostock. Math. Kolloq.* 48 (1995), 11–18. **[P]** pour
  les pages 11–15 : conjectures 1 à 3, théorèmes 1 à 3, équations (15)–(19)
  et (21)–(22). PostScript du dépôt de Rostock,
  `http://www.math.uni-rostock.de/math/pub/romako/heft48/berg2.ps`,
  SHA-256 `d0a1a38e8b156372415f33b1b374d0670cd54390e17495a5dd28a0540aded639`,
  8 pages, non redistribué. Les fontes sont des bitmaps : la lecture est
  celle du rendu, pas d'une couche texte.
- Le même article renvoie les preuves d'équivalence à Berg–Meinardus,
  *Results Math.* 25 (1994), 1–12, DOI `10.1007/BF03323136`. **[S]** :
  pas de PDF ouvert (unpaywall : non libre). La preuve n'est pas lue.
- B12 : pour l'application non raccourcie, atteindre \(1\) équivaut au
  premier retour sur \(\Sigma\). Le \(T\) du dépôt est l'application \(t\)
  de la note.

**Écart.** La note de 1995 ne compare pas son énoncé au premier retour
modulo \(18\), et elle ne définit pas le symbole \(\mathbb N\).

**Classification.** ALREADY KNOWN pour les deux équivalences annoncées.
La comparaison avec B12 est interne. Confiance élevée sur le texte de
1995, nulle sur la preuve de 1994.

**Décision.** NO-GO pour chercher un lemme de descente dans cette
équation. L'expérience de ce cycle est la comparaison, pas une attaque
de la conjecture 3.

## 1. Ce qui est lu

L'application de la note est
\[
t(n)=\begin{cases} n/2 & \text{si }n\equiv 0\pmod 2,\\ (3n+1)/2 & \text{si }n\equiv 1\pmod 2,\end{cases}
\]
et \(t_0(n)=n\), \(t_m=t\circ t_{m-1}\). C'est le \(T\) du dépôt.
La conjecture 1, p. 11, dit : pour tout \(n\in\mathbb N\), un itéré vaut \(1\).
Le symbole \(\mathbb N\) n'est pas défini. La référence [3] est Lagarias,
*Amer. Math. Monthly* 92 (1985) ; cet article n'est pas relu ici et
n'est pas une prémisse.

La majoration \(t_m(n)\le (3/2)^m(n+1)-1\) est vraie pour \(m,n\ge 0\),
parce que \(t(n)+1\le (3/2)(n+1)\), avec égalité si \(n\) est impair.
Les séries \(f_m\), \(g_n\) et \(F\) sont donc holomorphes pour \(|z|<1\),
\(|w|<2/3\), et dans ce polydisque. Ce disque ne dépend pas de la
conjecture : il ne sépare pas les orbites qui atteignent \(1\) des autres.

Le théorème 1 dit que chaque \(f_m\) est rationnelle,
\(f_m(z)=p_m(z)/(1-z^{2^m})^2\), avec un numérateur de degré au plus
\(2^{m+1}-1\) dont les coefficients sont des valeurs de \(t_m\). C'est
la forme affine par classes modulo \(2^m\). Ce n'est pas une prémisse
de B16.

## 2. Les deux énoncés analytiques

La conjecture 2, p. 13 : les fonctions
\(g_n(w)=\sum_{m\ge 0}t_m(n)w^m\) sont de la forme \(q_n(w)/(1-w^2)\),
avec \(q_n\in\mathbb Z[w]\). La note écrit que ceci équivaut à la
conjecture 1, et que la preuve est dans l'article de 1994.

L'équation (16) est la récurrence du pas :
\(g_{2n}(w)=2n+wg_n(w)\) et \(g_{2n-1}(w)=2n-1+wg_{3n-1}(w)\).
Elle dit \(t(2n)=n\) et \(t(2n-1)=3n-1\). Ce n'est pas une descente.

L'équation (18), obtenue en posant \(w=1\) dans l'équation homogène
associée à (17), est
\[
h(z^3)=h(z^6)+\frac1{3z}\sum_{\nu=0}^{2}\lambda^\nu h(\lambda^\nu z^2),
\qquad \lambda=e^{2\pi i/3}.
\]
Elle admet \(h(z)=h_0+h_1 z/(1-z)\). La conjecture 3, p. 14 : ce sont
les seules solutions holomorphes pour \(|z|<1\). La note écrit encore
que l'équivalence avec la conjecture 1 peut être prouvée ; la preuve
n'est pas dans ces huit pages.

En remplaçant \(z\) par \(-z\), (18) équivaut au système
\begin{align*}
h(z)+h(-z)&=2h(z^2),\\
h(z^3)-h(-z^3)&=\frac2{3z}\sum_{\nu=0}^{2}\lambda^\nu h(\lambda^\nu z^2),
\end{align*}
pour \(|z|<1\) et \(z\neq 0\), puis par continuité en \(0\). La somme des
deux formes de (18) est la première équation évaluée en \(z^3\). Tout
point du disque est un cube, donc la première équation suit pour tout
le disque. La différence est la seconde. L'addition redonne (18).

La solution générale de la première équation, écrite dans la note, est
\[
h(z)=c_0+\sum_{n\ge 1}\frac{c_n z^{2n-1}}{1-z^{2n-1}},
\]
avec des constantes arbitraires, sous réserve de convergence dans le
disque. L'espace n'est pas de dimension \(2\). La contrainte éventuelle
est entièrement dans la seconde équation.

## 3. B16 — la conjecture 2 est l'atteinte de \(1\)

**Énoncé.** Pour tout entier \(n\ge 1\), les deux assertions sont
équivalentes.
1. Il existe \(m\ge 0\) tel que \(t_m(n)=1\).
2. \(g_n(w)=q(w)/(1-w^2)\) pour un polynôme \(q\) à coefficients entiers.

**Preuve.** Si la série de la suite \(a_m=t_m(n)\) est \(q(w)/(1-w^2)\)
avec \(q\) polynôme, alors \(a_{m+2}=a_m\) pour tout \(m\) assez grand.
La queue est donc périodique de période divisant \(2\).

Il n'y a pas de point fixe positif. Si \(n\) est pair et \(t(n)=n\),
alors \(n=0\). Si \(n\) est impair et \(t(n)=n\), alors \(n=-1\).

Un cycle positif de longueur \(2\) est unique, et c'est \(\{1,2\}\).
- Deux pas pairs : \(n/4=n\), donc \(n=0\), qui n'est pas de période \(2\).
- Pair puis impair : \(n=2m\) avec \(m\) impair et \((3m+1)/2=2m\), donc
  \(m=1\) et \(n=2\). Alors \(t(2)=1\) et \(t(1)=2\).
- Impair puis pair : \((3n+1)/4=n\), donc \(n=1\), le même cycle.
- Deux pas impairs : \(3(3n+1)+2=4n\), donc \(5n=-5\) et \(n=-1\), le
  point fixe déjà vu.

La queue positive de période divisant \(2\) est donc, à partir d'un
rang \(M\), la suite \(1,2,1,2,\ldots\) ou la suite \(2,1,2,1,\ldots\).
Dans les deux cas un itéré vaut \(1\).

Réciproquement, si \(t_M(n)=1\), la queue est \(1,2,1,2,\ldots\) et
\[
g_n(w)=\sum_{j<M}t_j(n)w^j+\frac{w^M(1+2w)}{1-w^2}.
\]
Le numérateur est un polynôme à coefficients entiers, car les itérés
d'un entier positif restent des entiers positifs. Si le premier terme
du cycle rencontré est \(2\), le numérateur de la queue est \(2+w\),
encore entier.

Ceci est l'équivalence des conjectures 1 et 2, limitée aux entiers
\(n\ge 1\). L'article de 1995 l'annonce et place la preuve dans le
texte de 1994, non lu. L'argument ci-dessus ne dépend pas de ce texte.
Ce n'est pas un théorème nouveau, et ce n'est pas une descente : (1)
est la conjecture elle-même.

## 4. X29 — le point \(0\)

\(t(0)=0\), donc \(g_0(w)=0\), qui est de la forme (13), et aucun itéré
ne vaut \(1\). Si l'on lit la conjecture 2 pour tout \(n\ge 0\) et la
conjecture 1 comme « un itéré vaut \(1\) » sur le même ensemble, les
deux énoncés ne sont pas équivalents. B16 ne prend que \(n\ge 1\).
Aucun choix non écrit du symbole \(\mathbb N\) n'est ajouté.

## 5. La solution holomorphe annoncée

Pour \(h(z)=z/(1-z)\),
\[
h(z^3)-h(z^6)=\frac{z^3}{1-z^6}.
\]
Avec \(w=z^2\) et \(1-w^3=\prod_{\nu=0}^{2}(1-\lambda^\nu w)\),
\[
\sum_{\nu=0}^{2}\frac{\lambda^{2\nu}}{1-\lambda^\nu w}=\frac{3w}{1-w^3}
\]
pour \(|w|<1\). Le coefficient de \(w^j\) à gauche est
\(\sum_{\nu=0}^{2}\lambda^{\nu(j+2)}\). Cette somme vaut \(3\) si
\(j\equiv 1\pmod 3\), et \(0\) sinon. La série vaut donc
\(3\sum_{m\ge 0}w^{3m+1}=3w/(1-w^3)\).

Le nombre \(\lambda^{2\mu}\) est le coefficient devant
\((1-\lambda^\mu w)^{-1}\). Comme \(\lambda^{-\mu}=\lambda^{2\mu}\) et
\((1-\lambda)(1-\lambda^2)=3\),
\[
\lim_{w\to\lambda^{-\mu}}(1-\lambda^\mu w)\frac{3w}{1-w^3}=\lambda^{2\mu}.
\]
Ce nombre n'est pas le résidu. La dérivée de \(1-w^3\) est \(-3w^2\),
donc
\[
\mathrm{Res}\Bigl(\frac{3w}{1-w^3},\lambda^{-\mu}\Bigr)
=\frac{3\lambda^{-\mu}}{-3\lambda^{-2\mu}}=-\lambda^\mu.
\]
En \(w=1\), ce résidu vaut \(-1\). L'ancienne phrase, qui appelait
\(\lambda^{2\mu}\) le résidu, est fausse (X30). L'identité de séries
subsiste, et (18) est satisfaite pour \(h(z)=z/(1-z)\). Une constante
l'est aussi : \(\sum_{\nu=0}^{2}\lambda^\nu=0\). La combinaison (19)
suit. Le script contrôle l'identité de numérateurs dans
\(\mathbb Z[\lambda]/(\lambda^2+\lambda+1)\), le filtre
\(j\equiv 1\pmod 3\), et le résidu \(-\lambda^\mu\).

Le même calcul donne, pour \(e\) impair,
\[
\frac{z^e}{1-z^e}+\frac{(-z)^e}{1-(-z)^e}=\frac{2z^{2e}}{1-z^{2e}},
\]
qui est la première équation du système sur le terme d'indice \(e\).
Les constantes \(c_n\) restent libres. Cette équation seule ne force
pas la conjecture 3.

## 6. Le théorème 3 ne contraint pas les orbites

**Théorème 3 de la note, relu.** Toute solution entière de (18) est
constante.

La preuve de la note se réécrit ainsi. Pour \(r>1\),
\[
M(r^6)\le M(r^3)+\frac1r M(r^2)\le 2M(r^3),
\]
où \(M(r)=\max_{|z|\le r}|f(z)|\). Le passage de \(h(z^6)\) à \(h(z^3)\)
vient de (18), et \(M(r^2)\le M(r^3)\). Par récurrence sur \(k\ge 0\),
\[
M(r^6)\le 2^{k+1}M\bigl(r^{3\cdot 2^{-k}}\bigr).
\]
Le pas applique l'inégalité au rayon \(r^{2^{-(k+1)}}>1\). Pour
\(r>2^{1/3}\), le choix \(k=1+\lfloor\log_2(3\log_2 r)\rfloor\) donne
\(3\log_2 r<2^k\le 6\log_2 r\), donc \(r^{3\cdot 2^{-k}}<2\) et
\(M(r^6)\le 12 M(2)\log_2 r\). En posant ce rayon à la puissance \(1/6\),
\(M(r)\le 2M(2)\log_2 r\) pour \(r>4\). Les coefficients de Taylor en
\(0\) sont nuls dès le degré \(1\), par l'estimation de Cauchy.

La solution \(z/(1-z)\) n'est pas entière. Le théorème 3 n'élimine donc
pas la solution que la conjecture 3 veut isoler. Il ne parle pas de
\(g_n\). Comme le disque \(|w|<2/3\) est inconditionnel, une orbite qui
n'atteint pas \(1\) a quand même une série holomorphe dans ce disque.
L'analyticité n'est pas l'obstruction ; la forme rationnelle de
dénominateur \(1-w^2\) l'est, et B16 dit que cette forme est l'atteinte
de \(1\).

L'équation intégrale (20) et le tableau des coefficients de l'opérateur
\(T\) de la p. 15 ne sont pas revérifiés. Ils ne sont pas des prémisses.
Le §4, sur une autre écriture de \(f_m\), non plus.

## 7. Comparaison avec B12

Pour \(n\ge 1\), \(t\) atteint \(1\) si et seulement si l'application
non raccourcie \(f\) l'atteint. En effet, \(t(n)=f(n)\) si \(n\) est
pair, et \(t(n)=f(f(n))\) si \(n\) est impair. Chaque pas de \(t\) suit
l'orbite de \(f\), et le seul entier pair sauté est de la forme \(3m+1\).
Cet entier ne vaut pas \(1\). Réciproquement, un pas de \(t\) est un ou
deux pas de \(f\). B12 dit déjà que, pour un entier positif, \(f\)
atteint \(1\) si et seulement si \(T\) l'atteint. L'assertion (1) de B16
est donc la même conjecture que celle dont B12 donne la forme par
premier retour.

B16 remplace cette conjecture par la rationalité de \(g_n\). B12 la
remplace par le retour à \(1\) de \(P\) sur \(\Sigma\). Aucune des deux
ne donne une fonction qui décroît, ni une famille d'entiers exclue.
La conjecture 3 est un seul énoncé sur toutes les séries à la fois.
Même si l'équivalence annoncée est vraie, elle ne fournit pas, dans le
texte lu, de test applicable à un entier sans reconstruire la fonction
\(h\). Cette reconstruction n'est pas dans la note de 1995.

## 8. Ce que ce cycle ne montre pas

L'équivalence entre la conjecture 1, pour \(n\ge 1\), et la conjecture 3
est écrite au §12. Le PDF de 1994 reste non lu et n'est pas une prémisse
de cet argument. Aucune solution holomorphe autre que (19) n'est
construite sans supposer qu'un entier positif évite \(1\), et aucune
n'est exclue sans la conjecture. Le théorème 3 reste celui du §6.
Rien sur (C), sur (H), ni sur Syracuse.
Le disque \(|w|<2/3\) n'est pas une borne de temps d'arrêt.

## 9. Mises à jour de la mémoire

- `proved.md` : B16, présenté comme l'équivalence déjà annoncée, avec
  preuve autonome. La revue `6082693818` est enregistrée sous B15, sans
  changement de formule.
- `counterexamples.md` : X29, le point \(0\).
- `prior_art.md` : la note de 1995 passe en [P] pour les énoncés cités.
  L'article de 1994 reste [S].
- `abandoned.md` : ne pas chercher un lemme de descente dans les
  conjectures 2 et 3.
- `hypotheses.md` : la question de Berg–Meinardus est close comme
  reformulation.
- `agenda.md` : question suivante sur l'axe A.
- `reviews.md` : revue `6082693818`.

## 10. Prochaine question

Axe **A**, un seul énoncé. Les équivalences globales, ici et dans les
théorèmes non adoptés de Mori, ne donnent pas de descente. Wirsching
n'est pas la question suivante : ce serait une autre reformulation
fonctionnelle.

Pour tout réel \(c\), la fonction
\(V(n)=\log_2(n+1)+c\,v_2(n+1)\) n'est-elle pas une fonction de Lyapunov
stricte le long des orbites positives de \(T\) ? Le cas \(c\le\beta\) est
le premier pas impair d'un nombre de Mersenne : l'écart vaut \(\beta-c\).
Pour \(c>\beta\), H7 observe que les longues fenêtres suivent la hauteur,
sans donner d'entier. Produire un témoin explicite \(n>1\) et \(t\ge 1\)
avec \(V(T^t(n))\ge V(n)\), ou prouver la décroissance stricte hors du
cycle. Dans ce second cas, ne pas en déduire Syracuse : il resterait à
montrer que \(V\) est propre et minorée. S'arrêter au premier témoin.
Ne pas rouvrir B10, B13, X21, le signe moins, le mot du cycle 006, la
famille \(5\cdot 2^k-1\), ni les théorèmes 4.2.7 et 4.3.10 de Mori.

## 11. Reproduire

```sh
python3 research/checks/cycle011_berg_meinardus.py
```

Sortie attendue : neuf lignes `PASS`. Elles couvrent l'identité
\(3w/(1-w^3)\), le résidu \(-\lambda^\mu\) distinct du coefficient
\(\lambda^{2\mu}\), le filtre \(j\equiv 1\pmod 3\), les coefficients
de la forme multipliée par \(3z\) sur la suite \(a_j=j+1\), quatre
termes de l'équation (21), la croissance jusqu'à \(2000\), les
polynômes \(q\) pour \(1\le n\le 500\), le point \(n=0\), la récurrence
(16) jusqu'à \(500\), et les quatre équations de parité.
Le segment \(n\le 500\) n'est pas la preuve de B16. Le contrôle des
coefficients jusqu'au degré indiqué n'est pas la preuve du §12.

## 12. Revue `6082791301`

Revue indépendante sur le SHA
`ded6e1ce82163f68ba5a1611802f57d4a2b8bf92` (PR #27). B16 et X29 sont
confirmés. Les quatre cas de parité et la queue \(1,2,1,2,\ldots\) sont
ceux des §§3–4. Aucune correction de ces deux énoncés.

**X30.** La première rédaction du §5 appelait \(\lambda^{2\mu}\) le
résidu de \(3w/(1-w^3)\) en \(w=\lambda^{-\mu}\). Ce résidu vaut
\(-\lambda^\mu\). En \(w=1\), il vaut \(-1\). La valeur \(\lambda^{2\mu}\)
est la limite de \((1-\lambda^\mu w)\,3w/(1-w^3)\), donc le coefficient
devant \((1-\lambda^\mu w)^{-1}\). L'identité
\(\sum_{\nu}\lambda^{2\nu}/(1-\lambda^\nu w)=3w/(1-w^3)\) reste vraie.
Sa preuve est le développement géométrique du §5. Les solutions
\(h_0+h_1 z/(1-z)\) restent des solutions.

**Coefficients de (18).** Soit \(h(z)=\sum_{j\ge 0}a_j z^j\), holomorphe
pour \(|z|<1\). Pour \(|z|<1\), les arguments \(z^3\), \(z^6\) et
\(\lambda^\nu z^2\) restent dans le disque, et la série de \(h\) y est
absolument convergente. Alors
\[
\frac1{3z}\sum_{\nu=0}^{2}\lambda^\nu h(\lambda^\nu z^2)
=\sum_{m\ge 0}a_{3m+2}z^{6m+3},
\]
car \(\sum_{\nu=0}^{2}\lambda^{\nu(j+1)}\) vaut \(3\) si \(j\equiv 2\pmod 3\)
et \(0\) sinon. Le facteur \(1/z\) ne laisse pas de partie polaire. En
identifiant les coefficients de \(z^{6m}\) et de \(z^{6m+3}\) dans (18),
\[
a_{2m}=a_m,\qquad a_{2m+1}=a_{3m+2}.
\]
Ce sont toutes les puissances qui apparaissent. Comme \(t(2m)=m\) et
\(t(2m+1)=3m+2\), ces égalités sont \(a_n=a_{t(n)}\) pour tout \(n\ge 0\).
La réciproque redonne (18) pour \(z\neq 0\), puis en \(0\) par continuité.

**Équivalence.** Pour \(|z|<1\), les seules solutions holomorphes de (18)
sont \(h(z)=h_0+h_1 z/(1-z)\) si et seulement si tout entier \(n\ge 1\)
atteint \(1\) sous \(t\).

Si tout \(n\ge 1\) atteint \(1\), l'orbite de \(n\) entre dans le cycle
\(\{1,2\}\). Comme \(a_1=a_{t(1)}=a_2\), on a \(a_n=a_1\) pour tout
\(n\ge 1\). La relation \(a_0=a_{t(0)}\) laisse \(a_0\) libre. Donc
\(h(z)=a_0+a_1 z/(1-z)\), holomorphe sur le disque. Le point \(0\) reste
hors de cette équivalence : \(t(0)=0\) et X29 ne change pas.

Si un entier \(n\ge 1\) n'atteint pas \(1\), soit \(M\) l'ensemble de ces
entiers. Posons \(a_0=0\), \(a_n=1\) pour \(n\in M\) et \(a_n=0\) sinon.
Alors \(t(M)\subset M\) et \(t\) envoie le complémentaire dans lui-même,
donc \(a_n=a_{t(n)}\). La série a des coefficients dans \(\{0,1\}\), donc
elle est holomorphe pour \(|z|<1\) et satisfait (18). Elle n'est pas de
la forme \(h_0+h_1 z/(1-z)\) : \(1\notin M\), donc \(a_1=0\), tandis que
\(a_n=1\). L'indicateur complémentaire, celui qui vaut \(1\) sur le bassin
de \(1\), donne le même écart.

Ce témoin est celui du théorème 1 de Meinardus, *Some analytic aspects
concerning the Collatz problem*, preprint Mannheim n° 261/2001, §2.
PDF `https://madoc.bib.uni-mannheim.de/1608/1/261_2001.pdf`, SHA-256
`08ebcc736ad2c72dad634394cdd9402f90f21a31af0fb77d6709bd8bf2ce297e`,
15 pages, non redistribué. La couche texte est incomplète : les numéros
d'équations (3) et (4) ne sont pas extraits. Le paragraphe de preuve lu
donne l'énoncé adopté ici, et rien de plus. L'ensemble \(A\) est celui
des suites bornées indexées par les entiers positifs. L'application (1)
de cette note est \(t\). La conjecture est équivalente à : les seules
suites bornées invariantes par \(t\) sont les suites constantes. La
direction fausse utilise l'indicateur de l'ensemble des points qui
n'atteignent pas \(1\). Les théorèmes 2 et suivants de ce PDF, séries de
Dirichlet et noyau intégral, ne sont pas adoptés. Le préprint de 1987
cité comme [7] n'a pas été lu. La phrase de la p. 4 qui renvoie les
équivalences en séries entières aux articles de 1994 et de 1995 n'est
pas une preuve.

Pour une solution entière, les mêmes relations donnent \(a_n=a_{2^j n}\).
L'estimation de Cauchy sur \(|z|=2\) donne
\(|a_n|\le M(2)/2^{2^j n}\). Pour \(n\ge 1\), le membre de droite tend
vers \(0\), donc \(a_n=0\). Cela relit le théorème 3 du §6. La preuve
par le maximum du §6 n'est pas remplacée.

Cet argument ne produit aucun temps de descente et n'exclut aucun
entier. La conjecture 3 reste l'atteinte de \(1\) pour \(n\ge 1\), déjà
annoncée en 1995. Ce n'est pas un théorème nouveau.

La question du §10 n'est pas entamée. Ne pas ouvrir le cycle 012 avant
la relecture de ce correctif. Ne pas rouvrir les conjectures 2 et 3
pour y chercher une descente.

Mises à jour de cette revue : X30 dans `counterexamples.md` ; B16 et
l'équivalence du §12 dans `proved.md` ; Meinardus 2001 dans
`prior_art.md` ; la ligne Berg–Meinardus de `abandoned.md` ; l'agenda,
bloqué sur cette relecture ; `reviews.md`.
