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
d'écriture. Ils sont réparés au §4. La preuve du §3 est autonome.

## 1. Source

**Mori**, *Application of Operator Theory for the Collatz Conjecture*,
arXiv:2411.08084v2, 3 février 2025, 27 pages. **[P]** pour les énoncés
cités aux §§2–4. PDF `https://arxiv.org/pdf/2411.08084`, SHA-256
`e852509294f8698923aa31aa827cbdc0353b861fc24441b73558946b2874c92b`.
Non redistribué. La version d'*Advances in Operator Theory* n'a pas été
lue. Les généralisations du §5, et Conway, *A course in operator theory*
(2000), cité pour le théorème 3.4.6, ne sont pas des prémisses.

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

## 4. Deux défauts d'écriture, et la recherche d'un contre-exemple

La proposition 4.3.2 affirme que $P$ restreint à $N_2$ est injective, puis
écrit : si $m>n$ et $P(m)=P(n)$, alors $m$ est un multiple de $n$, « donc »
$P(m)\ge n$. Cette conséquence n'est pas justifiée. L'injectivité est
cependant vraie : la contradiction correcte est $P(m)=n$, prouvée au §3,
et non $P(m)\ge n$.

Le même texte dit : si $n\equiv7,16\pmod{18}$, alors
$16n\equiv16,4\pmod{18}$. Les deux produits valent $4$ :
$112-108=4$ et $256-252=4$. Les deux résidus sont dans $N_2$.
L'appartenance annoncée reste vraie ; la paire de résidus imprimée est
fausse.

Aucun de ces deux défauts ne fournit un contre-exemple à B12. Le script
cherche en outre une collision de $P$ parmi les $2\,222$ éléments de $N_2$
jusqu'à $20\,000$, et un impair $q\equiv3\pmod6$, $q\le30\,000$, dont
l'impair suivant sortirait de $N_1$. Il n'en trouve pas. Ce segment n'est
pas la preuve.

## 5. Ce qui n'est pas adopté

La définition 3.4.4 demande qu'un vecteur cyclique $x$ vérifie
$\{Tx:T\in\mathcal A\}=\mathcal H$, pas seulement que cette orbite soit
dense. Le lemme 4.2.2 énonce
$C^*(T_1,T_2)e_n=\overline{\mathrm{span}}\{e_m:m\sim n\}$, en appelant
cet espace fermé au lemme 4.1.1. L'argument écrit montre seulement que
chaque vecteur de base de la classe est un mot fini en $T_1,T_2,T_1^*,T_2^*$
appliqué à $e_n$, donc que les combinaisons finies sont dans l'orbite, et
que les limites en norme d'opérateurs restent dans l'espace fermé. Cela
donne la densité, pas l'égalité des ensembles.

Le sens « vecteur cyclique $\Rightarrow$ conjecture » du théorème 4.2.3
reste valide, car une orbite égale à $\mathcal H$ est dense. Le sens
réciproque, et donc les équivalences 4.2.7 et 4.3.10, ne sont pas
établis par le texte lu. Ils ne sont pas des prémisses. Le corollaire
4.1.3, qui n'est qu'une condition suffisante, n'est pas non plus une
réduction utilisable ici. Les §§5 et suivants ne sont pas vérifiés.

## 6. Ce que ce cycle ne montre pas

- La conjecture, ni pour $f$, ni pour $T$.
- L'isomorphisme de $C^*(S_1,S_2)$ avec l'algèbre de Cuntz $\mathcal O_2$.
- L'absence de sous-espace réducteur non trivial.
- Rien sur le mot du cycle 006, ni sur (C), ni sur (H).
- Rien qui relise Berg–Meinardus, Wirsching, ou la preuve publiée de
  Mori au-delà des énoncés cités.

## 7. Mises à jour de la mémoire

- `proved.md` : B12, l'équivalence seulement.
- `hypotheses.md` : H8, l'égalité cyclique laissée ouverte.
- `prior_art.md` : Mori passé en lecture primaire pour ces énoncés.
- `abandoned.md` : ne pas invoquer 4.2.7 ou 4.3.10 comme équivalence
  déjà prouvée.
- `agenda.md` : question retirée. Prochaine question : l'égalité du §5.
- `reviews.md` : revue `6081994521`.

## 8. Prochaine question

Axe **C**, encore Mori, un seul point. La définition 3.4.4 exige
$C^*(T_1,T_2)e_1=\mathcal H$. Montrer que tout vecteur de l'espace fermé
engendré par $\{e_{2^k}:k\ge0\}$ est de la forme $Te_1$ avec
$T\in C^*(T_1,T_2)$, ou donner un vecteur explicite qui ne l'est pas.
Cette demi-droite est dans la classe de $1$, sans supposer la conjecture.
Ne pas rouvrir le mot du cycle 006. Ne pas traiter le théorème 4.2.7
comme prouvé avant ce point. Conway 2000 n'a pas été lu.

## 9. Reproduire

```sh
python3 research/checks/cycle007_first_return.py
```

Sortie attendue : cinq lignes `PASS`. Elles couvrent les huit produits,
les chaînes $112\to7$, $16\to4$ et $4\to1$, l'identité $P(n)=3n+1$ pour
les $n\in N_1$ jusqu'à $3\,000$, l'absence de collision de $P$ sur $N_2$
jusqu'à $20\,000$ ($2\,222$ valeurs) et le saut vers $N_1$ pour les
$5\,000$ impairs $q\equiv3\pmod6$ jusqu'à $30\,000$. L'injectivité, la
surjectivité et l'équivalence sont prouvées au §3 pour tout entier.
