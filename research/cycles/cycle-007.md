# Cycle 007 — Premier retour sur les classes modulo 18

Date : 27 novembre 2026. Axe **C**.
Branche : `research/memory`. Script : [`../checks/cycle007_first_return.py`](../checks/cycle007_first_return.py).

**Verdict : l'équivalence entre la conjecture de Collatz, pour l'application
non raccourcie, et le retour de $1$ sous le premier retour $P$ sur
$\Sigma=N_1\cup N_2$, est PROUVÉE ici. Ce n'est pas une preuve de la
conjecture. Les théorèmes opératoriels 4.2.7 et 4.3.10 de Mori ne sont
pas adoptés.**

## 0. Question traitée

Première entrée de l'agenda, après la revue `6081994521` sur le SHA
`a2886972de6371d3302dd9a17bc3bc59c98e479f`. Cette revue confirme le
correctif X22 du cycle 006 et ne demande aucun changement. Elle est
enregistrée au §12 du cycle 006 et dans `reviews.md`. Le mot du cycle 006
n'est pas rouvert.

L'agenda demandait une lecture de Berg–Meinardus, de Wirsching (LNM 1681)
ou de Mori 2024, puis un seul énoncé réfutable, avant tout calcul.
La source lue est Mori, parce que le PDF d'arXiv est public. Les deux
autres ne sont pas lus. L'énoncé retenu est la proposition 4.3.3 : la
conjecture équivaut à $1\in\mathrm{orb}(n;P)$ pour tout $n\in\Sigma$.
Le texte imprimé de la proposition 4.3.2, dont elle dépend, a deux défauts
d'écriture : la paire de résidus, et une inégalité laissée sans argument.
La paire est fausse, l'inégalité est justifiée au §4. La preuve du §3
est autonome. La première rédaction du §5 lisait la définition 3.4.4
sans ses barres de fermeture. Cette lecture est retirée au §10.

## 1. Source

**Mori**, *Application of Operator Theory for the Collatz Conjecture*,
arXiv:2411.08084v2, 3 février 2025, 27 pages. **[P]** pour les énoncés
cités aux §§2–4. PDF `https://arxiv.org/pdf/2411.08084`, SHA-256
`e852509294f8698923aa31aa827cbdc0353b861fc24441b73558946b2874c92b`.
Non redistribué. La définition cyclique et le lemme 4.2.2 ont été relus
dans la source TeX de l'e-print v2 ; les empreintes sont au §10. La
version d'*Advances in Operator Theory* n'a pas été lue. Les
généralisations du §5, et Conway, *A course in operator theory* (2000),
cité pour le théorème 3.4.6 et pour la proposition 13.3 du chapitre 2,
ne sont pas des prémisses.

L'application du papier est
$$f(n)=\begin{cases}3n+1&n\text{ impair},\\ n/2&n\text{ pair.}\end{cases}$$
Ce n'est pas l'application raccourcie $T$ du dépôt. Pour $n\ge1$, $f$
atteint $1$ si et seulement si $T$ atteint $1$. En effet, tant que le
terme est pair, $f$ et $T$ divisent par $2$. Au premier impair $q$, le
prochain impair est $(3q+1)/2^{v_2(3q+1)}$ pour les deux applications :
$T$ regroupe ces divisions, $f$ les fait une par une après le pas
$3q+1$. La suite des impairs coïncide, et $1$ est impair. Rien de ceci
n'est une preuve de la conjecture.

## 2. L'énoncé

Soient $N_1=\{n\ge1:n\equiv1\text{ ou }5\pmod6\}$,
$N_2=\{n\ge1:n\equiv4\text{ ou }16\pmod{18}\}$ et $\Sigma=N_1\cup N_2$.
Le premier retour $P:\Sigma\to\Sigma$ est $P(n)=f^{\tau(n)}(n)$, où
$\tau(n)\ge1$ est minimal avec $f^{\tau(n)}(n)\in\Sigma$.

**B12.** $P$ est défini sur tout $\Sigma$, sans hypothèse sur la
conjecture. La restriction de $P$ à $N_1$ est la bijection
$n\mapsto3n+1$ sur $N_2$. La restriction de $P$ à $N_2$ est injective et
son image est $\Sigma$. Tout entier $n\ge1$ possède un itéré par $f$
dans $N_1$. Les deux assertions suivantes sont équivalentes :

1. pour tout $n\ge1$, il existe $m\ge0$ avec $f^m(n)=1$ ;
2. pour tout $n\in\Sigma$, $1$ appartient à l'orbite de $n$ sous $P$.

Mori énonce (2)$\Leftrightarrow$(1) comme proposition 4.3.3. L'antériorité
est la sienne. La preuve ci-dessous ne dépend pas de la sienne.

## 3. Preuve

Les classes de $\Sigma$ modulo $18$ sont exactement
$\{1,4,5,7,11,13,16,17\}$ : les impairs $\equiv1\pmod6$ donnent
$1,7,13$, les impairs $\equiv5\pmod6$ donnent $5,11,17$, et $N_2$ donne
$4,16$.

**Image de $N_1$.** Si $n=6t+1$, alors $3n+1=18t+4$. Si $n=6t+5$, alors
$3n+1=18t+16$. Réciproquement, $18t+4=3(6t+1)+1$ et
$18t+16=3(6t+5)+1$, avec $6t+1$ et $6t+5$ dans $N_1$. Donc
$N_2=f(N_1)$, et $n\mapsto3n+1$ est une bijection de $N_1$ sur $N_2$.
Pour $n\in N_1$, $f(n)=3n+1$ est déjà dans $\Sigma$, donc
$P(n)=3n+1$.

**Aucun élément de $N_2$ n'est divisible par $3$.** En effet
$4\equiv1\pmod3$ et $16\equiv1\pmod3$.

**Tout entier atteint $N_1$.** Soit $q$ la partie impaire de $n$, atteinte
en divisant par $2$. Si $q\in N_1$, c'est terminé. Sinon $q$ est impair et
$q\equiv3\pmod6$, donc $3\mid q$. Posons $3q+1=2^v q'$ avec $q'$ impair et
$v\ge1$. Alors $2^v q'\equiv1\pmod3$. Si $3\mid q'$, le membre de gauche
serait $\equiv0\pmod3$. Donc $3\nmid q'$. Comme $q'$ est impair, 
$q'\equiv1\text{ ou }5\pmod6$, d'où $q'\in N_1$. Cet itéré est un itéré
de $n$ par $f$.

**$P$ est défini sur $N_2$.** Soit $n\in N_2$ et $q$ sa partie impaire.
Alors $3\nmid q$. Comme $q$ est impair, $q\in N_1\subset\Sigma$. La chaîne
$n,n/2,\ldots,q$ est faite de divisions par $2$ et rencontre $\Sigma$. Le
premier terme strictement après $n$ qui est dans $\Sigma$ est $P(n)$, et
$n=2^a P(n)$ pour un entier $a\ge1$.

**Injectivité sur $N_2$.** Supposons $P(m)=P(n)=r$ avec $m,n\in N_2$.
Le paragraphe précédent donne $m=2^a r$ et $n=2^b r$ avec $a,b\ge1$, et
aucun terme strictement intermédiaire de chaque chaîne n'est dans $\Sigma$.
Si $a>b$, alors $f^{a-b}(m)=n$. Or $n\in\Sigma$ et $a-b\ge1$, et
$n=2^b r\ge2r>r$. Le premier retour partant de $m$ rencontre donc $n$
avant $r$, ce qui contredit $P(m)=r$. Le cas $b>a$ est symétrique. Donc
$a=b$ et $m=n$.

**Surjectivité sur $N_2$.** L'appartenance de $2^j r$ à $N_2$ ne dépend
que de $r$ modulo $18$. Pour chaque classe de $\Sigma$, le plus petit
$k\ge1$ tel que $2^k r\in N_2$ existe, et vaut au plus $4$ :

| $r\pmod{18}$ | $k$ | $2^k r\pmod{18}$ | produit témoin |
|---|---|---|---|
| $1$ | $2$ | $4$ | $4\cdot1=4$ |
| $4$ | $2$ | $16$ | $4\cdot4=16$ |
| $5$ | $3$ | $4$ | $8\cdot5=40=2\cdot18+4$ |
| $7$ | $4$ | $4$ | $16\cdot7=112=6\cdot18+4$ |
| $11$ | $1$ | $4$ | $2\cdot11=22=18+4$ |
| $13$ | $2$ | $16$ | $4\cdot13=52=2\cdot18+16$ |
| $16$ | $4$ | $4$ | $16\cdot16=256=14\cdot18+4$ |
| $17$ | $1$ | $16$ | $2\cdot17=34=18+16$ |

Pour $m=2^k r$, il reste à voir que $k$ est minimal, afin que la chaîne
de divisions par $2$ rencontre $r$ en premier. Les intermédiaires sont
pairs, donc hors de $N_1$. Leurs résidus modulo $18$ sont :
$2$ pour $r\equiv1$ ;
$8$ pour $r\equiv4$ ;
$10,2$ pour $r\equiv5$ ;
$14,10,2$ pour $r\equiv7$, soit les nombres $14,28,56$ ;
$8$ pour $r\equiv13$ ;
$14,10,2$ pour $r\equiv16$, soit les nombres $32,64,128$.
Aucun n'est dans $\{4,16\}$, donc aucun n'est dans $\Sigma$. Les classes
$11$ et $17$ ont $k=1$, sans intermédiaire. Ainsi $P(m)=r$.

**Équivalence.** Supposons (2), et soit $n\ge1$. Un itéré $y=f^{t}(n)$
tombe dans $N_1$, par le troisième point. Alors $1$ est un itéré de $y$
par $P$, donc un itéré de $y$ par $f$, donc un itéré de $n$ par $f$.

Supposons (1), et soit $n\in\Sigma$. L'orbite de $n$ par $f$ contient $1$,
puis reste dans $\{1,2,4\}$. L'orbite de $n$ par $P$ en est une sous-suite,
donc elle est finie : il existe $0\le l<s$ avec $P^l(n)=P^s(n)$. Posons
$k=P^l(n)$ et $d=s-l\ge1$. Alors $k$ est un itéré de $n$ par $f$, donc
l'orbite de $k$ atteint $1$ puis reste dans $\{1,2,4\}$. De plus
$P^{Nd}(k)=k$ pour tout $N\ge1$. Chaque temps de retour vaut au moins $1$,
donc le temps $\tau_N$ de $f$ composé le long de ces $Nd$ retours tend
vers l'infini. Pour $N$ assez grand, $k=f^{\tau_N}(k)$ est dans
$\{1,2,4\}$. Comme $k\in\Sigma$, on a $k\in\{1,4\}$. Enfin $P(1)=4$ et
$P(4)=1$, car $4,2,1$ est la chaîne et $2\notin\Sigma$. Dans les deux
cas, $1$ est un itéré de $k$ par $P$, donc de $n$.

## 4. Le résidu imprimé, l'inégalité, et la recherche d'un contre-exemple

La proposition 4.3.2 affirme que $P$ restreint à $N_2$ est injective, puis
écrit : si $m>n$ et $P(m)=P(n)$, alors $m$ est un multiple de $n$, « donc »
$P(m)\ge n$. L'inégalité est justifiée, et elle suffit à la contradiction.
Posons $r=P(m)=P(n)$. Le §3 donne $m=2^a r$ et $n=2^b r$ avec $a>b\ge1$,
donc $n\ge2r>r$. La suite $m,m/2,\ldots,r$ est strictement décroissante
et contient $n$. Comme $n\in\Sigma$, le premier terme de cette suite,
après $m$, qui tombe dans $\Sigma$ arrive au plus tard en $n$. Ce terme
est $P(m)$, et tout terme de la suite jusqu'à $n$ inclus est $\ge n$.
Donc $P(m)\ge n$. Or $P(m)=r<n$.

Sous la même hypothèse de collision, l'égalité $P(m)=n$ est vraie aussi :
$P(m)=r$ exclut tout intermédiaire dans $\Sigma$, et $n$ est le premier
point de $\Sigma$ rencontré. Elle est plus forte que nécessaire. Elle
n'est pas vraie pour un point ultérieur quelconque de la même chaîne.
La chaîne $16,8,4,2,1$ donne $P(16)=4$, et $1\in\Sigma$, avec $4>1$.

Le même texte dit : si $n\equiv7,16\pmod{18}$, alors
$16n\equiv16,4\pmod{18}$. Les deux produits valent $4$ :
$112-108=4$ et $256-252=4$. Les deux résidus sont dans $N_2$.
L'appartenance annoncée reste vraie ; la paire de résidus imprimée est
fausse.

Ni la paire de résidus, ni l'inégalité une fois justifiée, ne fournit un
contre-exemple à B12. Le script
cherche en outre une collision de $P$ parmi les $2\,222$ éléments de $N_2$
jusqu'à $20\,000$, et un impair $q\equiv3\pmod6$, $q\le30\,000$, dont
l'impair suivant sortirait de $N_1$. Il n'en trouve pas. Ce segment n'est
pas la preuve.

## 5. Ce qui n'est pas adopté

La première rédaction de ce paragraphe ôtait les barres de fermeture de
la définition 3.4.4 et du lemme 4.2.2, puis concluait que la densité ne
satisfaisait pas la définition. Cette lecture est réfutée (X23, §10).

Dans la source arXiv:2411.08084v2, la définition intitulée « Cyclic
vectors », numérotée 3.4.4 dans le HTML ar5iv, demande
$$\overline{\mathcal A x}=\overline{\{Tx:T\in\mathcal A\}}=\mathcal H.$$
Le lemme libellé `lem:Equality 1`, numéroté 4.2.2 dans le même HTML,
demande
$$\overline{C^*(T_1,T_2)e_n}=\overline{\mathrm{span}}\{e_m:m\sim n\}.$$
Le paragraphe de notation de la source pose que $\overline Y$ est la
fermeture de $Y$. Le théorème 4.2.3 écrit ses deux sens avec ces
fermetures. La densité qu'il énonce satisfait donc la définition
imprimée.

Le calcul écrit dans la source place chaque $e_m$, pour $m\sim n$, égal
à un mot fini en $T_1,T_2$ et leurs adjoints, appliqué à $e_n$. Ce
vecteur de base est dans l'orbite, pas seulement dans sa fermeture. La
fermeture de l'espace engendré est alors contenue dans la fermeture de
l'orbite. L'inclusion réciproque est renvoyée par la source au lemme
4.1.1 ; elle n'a pas été réécrite ici.

Les théorèmes 4.2.7 et 4.3.10 ne sont pas adoptés. Leur nécessité passe
par 4.2.6 et 4.3.9. Ces deux textes identifient l'absence de sous-espace
réducteur non trivial au commutant $\mathbb C I$, en citant que le
commutant, algèbre de von Neumann, est l'adhérence des combinaisons
linéaires de ses projections (Conway 2000, chapitre 2, proposition 13.3).
Ce livre n'a pas été lu. Le corollaire 4.1.3 reste une condition
suffisante, pas une réduction utilisée ici. Le §5 de Mori et les
sections suivantes ne sont pas vérifiés.

La revue `6082060844` esquisse en outre que l'orbite
$C^*(T_1,T_2)e_1$ est déjà fermée, par $U=T_2^2T_1$ et le théorème 1 de
Kadison (1957). Cette esquisse n'est pas reproduite. L'article de
Kadison n'a pas été lu. La définition imprimée ne demande que la
fermeture, déjà dans le lemme cité. Ce n'est pas une prémisse, ni la
question suivante.

## 6. Ce que ce cycle ne montre pas

- La conjecture, ni pour $f$, ni pour $T$.
- L'isomorphisme de $C^*(S_1,S_2)$ avec l'algèbre de Cuntz $\mathcal O_2$.
- L'absence de sous-espace réducteur non trivial.
- Rien sur le mot du cycle 006, ni sur (C), ni sur (H).
- Rien qui relise Berg–Meinardus, Wirsching, ou la preuve publiée de
  Mori au-delà des énoncés cités.

## 7. Mises à jour de la mémoire

- `proved.md` : B12, l'équivalence seulement.
- `hypotheses.md` : H8. L'objection de fermeture est réfutée (X23).
  Les théorèmes 4.2.7 et 4.3.10 restent non adoptés.
- `prior_art.md` : Mori passé en lecture primaire pour ces énoncés, et
  pour la définition cyclique et le lemme 4.2.2 dans la source v2.
- `abandoned.md` : ne pas invoquer 4.2.7 ou 4.3.10 comme équivalence
  déjà prouvée, et ne pas relancer la lecture sans barres.
- `counterexamples.md` : X23.
- `agenda.md` : l'égalité du §5 est retirée. Prochaine question : axe A,
  l'implication globale de H6.
- `reviews.md` : revues `6081994521` et `6082060844`.

## 8. Prochaine question

Axe **A**, un seul énoncé. Soient $0<\ell\le W\le h$ et $0<\rho<1$. Si
une fonction $B$ vérifie : tout entier $n\ge N_0$ admet un temps
$t\le B(n)$ avec $T^t(n)\le\rho n$, alors
$B(n)\ge\delta\log_2 n-O(1)$ pour une infinité de $n$. Sinon, exhiber
un poids et une fonction $B(n)=o(\log n)$ qui rendent la prémisse vraie.
Ne pas relancer B10, ni X21, ni le mot du cycle 006, ni la lecture sans
barres réfutée au §10. Conway 2000 et Kadison 1957 n'ont pas été lus.
Cette question n'est pas entamée dans le présent correctif.

Note postérieure (revue `6082099628`, cycle 008). La prémisse écrite
ci-dessus est $T^t(n)\le\rho n$, sans le poids. C'est le cas $K=\rho<1$
de l'estimation du cycle 005 §5, et $\rho\cdot2^t>3^L$ en découle. Ce
n'est pas l'énoncé initial de H6. La forme pondérée
$T^t(n)\,W(T^t(n))\le\rho\,n\,W(n)$, pour tout $K=\rho h/\ell$, est
prouvée au cycle 008.

## 9. Reproduire

```sh
python3 research/checks/cycle007_first_return.py
```

Sortie attendue : six lignes `PASS`. Elles couvrent les huit produits,
les chaînes $112\to7$, $16\to4$ et $4\to1$, l'identité $P(n)=3n+1$ pour
les $n\in N_1$ jusqu'à $3\,000$, l'absence de collision de $P$ sur $N_2$
jusqu'à $20\,000$ ($2\,222$ valeurs), le saut vers $N_1$ pour les
$5\,000$ impairs $q\equiv3\pmod6$ jusqu'à $30\,000$, et l'inégalité
$P(m)\ge x$ pour chaque point de $\Sigma$ sur la chaîne de divisions
issue d'un $m\in N_2$ jusqu'à $20\,000$, avec le témoin $P(16)=4>1$.
L'injectivité, la surjectivité et l'équivalence sont prouvées au §3
pour tout entier. L'inégalité du §4 l'est aussi ; le script n'en voit
qu'un segment.

## 10. Revue `6082060844`

Revue indépendante sur le SHA
`a60a1a6a6b64386a25c3de11d18aab48819ddf11` (PR #27). B12, §§2–3, est
confirmée. La preuve du §3 n'a pas été réécrite.

L'objection de fermeture du §5 a été reproduite contre la source, et
elle tombe. Le fichier
`Application_of_Operator_Theory_for_the_Collatz_Conjecture.tex` de
l'e-print `https://arxiv.org/e-print/2411.08084v2` contient les deux
barres. Empreinte SHA-256 du fichier :
`19ab8b0a912a81b3f0aa3a98a7db8a16ef7fb097f641b7001efb485726e50372`.
Empreinte de l'archive :
`cdcece33cb131fb77be007076cb992ceefa12b0e86b6f338a44b22376817964d`.
Le HTML ar5iv de la même version numérote ces énoncés 3.4.4 et 4.2.2
et affiche les barres. L'extraction texte du PDF déjà empreinté au §1
les efface : c'est l'origine de la lecture fausse. X23 enregistre cette
réfutation. Elle ne valide ni le théorème 4.2.7, ni le théorème 4.3.10,
ni le §5 de l'article.

L'inégalité $P(m)\ge n$ est celle justifiée au §4. Le témoin
$P(16)=4>1$ montre que $P(m)=n$ n'est pas une identité générale le long
de la chaîne. Les deux résidus $16n$ pour $n\equiv7,16\pmod{18}$ valent
$4$, comme le §4 le disait déjà : $112-108=4$ et $256-252=4$.

L'esquisse d'orbite fermée de la revue, et le théorème 1 de Kadison
(1957) qu'elle cite, ne sont pas des prémisses. La question du §8
ancien, qui demandait l'égalité exacte sur $\{e_{2^k}\}$ pour combler
des barres absentes, est retirée avec ces barres. Elle n'est pas
entamée.
