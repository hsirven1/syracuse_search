# Cycle 002 — La borne (H) n'est pas un petit lemme

Date : 26 novembre 2026. Axe **B**.
Branche : `research/memory`. Script : [`../checks/cycle002_run_bound.py`](../checks/cycle002_run_bound.py).

**Verdict.** (H) est reclassée conjecture majeure. Toute paire de constantes qui la satisfait
vérifie $B>1$, et $A<1/\beta$ exclurait toute orbite positive non bornée. Les fenêtres de
longueur bornée obéissent à une majoration géométrique explicite. Aucune famille à deux runs
examinée ne réfute un $B>1$. Ni (C), ni Syracuse.

## 0. Question traitée

Première entrée de l'agenda en début de cycle : consigner le statut exact de la cible (H)
de la PR #26, sans dépendre des preuves non fusionnées.

## 1. Définitions

$T(n)=n/2$ si $n$ est pair, $(3n+1)/2$ sinon. Depuis un entier $M>0$, la longueur de run
$r(M)=v_2(M+1)$, de partie impaire $a=(M+1)2^{-r(M)}$. Le run suivant commence en
$M'=(3^{r(M)}a-1)/2$. On pose $x(M)=\log_2(M+1)$, $\delta=\log_2 3$, $\beta=\delta-1=\log_2(3/2)$.
Toujours $r(M)\le x(M)$, avec égalité ssi $M+1$ est une puissance de 2.

**(H)** signifie : il existe $A,B$ tels que, pour tout départ positif, tout indice de run $i$
et tout $k\ge1$,
$$\sum_{j=0}^{k-1} r(M_{i+j}) \le Ak + B\,x(M_i).$$

## 2. Théorème B4 — toute solution de (H) a $B>1$

**Énoncé.** Pour tout réel $A$ et tout $B\le1$, la paire $(A,B)$ contredit (H).

Les Mersenne donnent déjà $B\ge1$. Pour $h\ge1$ et $M=2^h-1$, le premier run a longueur
$h=x(M)$. Le cas $k=1$ de (H) force $h\le A+Bh$ pour tout $h$, donc $B\ge1$. La pente $B=1$
survit à ce test.

Elle ne survit pas à deux runs.

**Ordre de 3.** Pour $m\ge3$, $v_2(3^2-1)=3$, et $v_2(3^{2^j}+1)=1$ dès que $j\ge1$, donc
$v_2(3^{2^{j+1}}-1)=v_2(3^{2^j}-1)+1$. On obtient $v_2(3^{2^{m-2}}-1)=m$. La seconde
identité écrite ici, $v_2(3^{2^{m-3}}-1)=m-1$, ne vaut que pour $m\ge4$ (X63). Pour
$m=3$, l'exposant $2^{0}$ donne $v_2(3-1)=1$, pas $2$. L'ordre modulo $8$ se lit
directement : $3^2\equiv1\pmod8$ et $3\not\equiv1\pmod8$, donc il vaut $2=2^{3-2}$.
Pour $m\ge4$, la remontée depuis $v_2(3^2-1)=3$ donne les deux valuations, et l'ordre
modulo $2^m$ vaut $2^{m-2}$. Cet ordre reste vrai pour tout $m\ge3$. Le sous-groupe
engendré est contenu dans les unités $\equiv1$ ou $3\pmod8$, qui ont le même cardinal, donc
il coïncide avec elles. B4 n'utilise pas l'égalité fausse au bord.

Comme $5\cdot5\equiv1\pmod8$, on a $5^{-1}\equiv5\pmod8$ et $-5^{-1}\equiv3\pmod8$. Il existe
donc un entier $r$, $1\le r<2^{m-2}$, tel que $5\cdot3^r\equiv-1\pmod{2^m}$, c'est-à-dire
$v_2(5\cdot3^r+1)\ge m$.

**Fenêtre.** Poser $M=5\cdot2^r-1$. Alors $x(M)=r+\log_25<r+3$, le premier run a longueur
$r$ et partie impaire 5, et le run suivant a longueur
$r_1=v_2(5\cdot3^r+1)-1\ge m-1$. Pour $k=2$,
$$r+r_1\ge r+m-1.$$
Parmi les pentes $B\le1$, le membre droit de (H) est maximal en $B=1$, et même alors
$$2A+B\,x(M)<2A+r+3.$$
Dès que $m>2A+4$, la fenêtre dépasse ce membre droit. Un tel $m$ existe pour chaque $A$ fini.

Le défaut à la pente 1 est non borné : $(r+r_1)-x(M)>(m-1)-3$. Aucun $A\cdot2$ ne l'absorbe.

**Témoin entier.** Le plus petit $r$ pour $m=16$ est $r=757$, et $v_2(5\cdot3^{757}+1)=16$.
Pour $M=5\cdot2^{757}-1$, la somme des deux runs vaut 772. Comme $5^3=125<128=2^7$,
$\log_25<7/3$, donc $2\cdot6+x(M)<772$. Cette seule fenêtre tue $B\le1$ et $A\le6$.

## 3. Théorème B5 — longueur de fenêtre bornée

Pour tout $M>0$ et tout $k\ge1$, si $x_j=x(M_j)$, alors $x_{j+1}\le\delta x_j$. En effet
$\log_2(3^ra+1)-1\le r\log_23+\log_2 a\le\delta x_j$. Comme $r(M_j)\le x_j\le\delta^j x(M)$,
$$\sum_{j<k}r(M_j)\le x(M)\frac{\delta^k-1}{\beta}.$$
Toute fenêtre de longueur au plus $K$ satisfait donc (H) avec $A=0$ et
$B_K=(\delta^K-1)/\beta$. On a $B_1=1$, valeur optimale, et $B_2=1+\delta=\log_26$.
La constante est exponentielle en $K$ : ce n'est pas une paire universelle.

## 4. Théorème B6 — (H), densité et absence d'orbite non bornée

**Identité, démontrée ici.** Un pas impair multiplie $n+1$ par $3/2$. Un pas pair le
multiplie par $\tfrac12\bigl(1+1/(n+1)\bigr)$. Après $t$ pas et $E(t)$ pas pairs,
$$\log_2(n_t+1)=\log_2(N+1)+\beta t-\delta E(t)+R(t),$$
où $R(t)=\sum\log_2(1+1/(n_s+1))$, somme sur les pas pairs $s<t$.

**Borne supérieure.** Une orbite positive non bornée ne se répète pas : une répétition
fermerait un cycle, et un cycle est borné. Les états pairs visités sont donc des entiers
distincts $\ge2$. Pour $n\ge2$, $\log_2(1+1/(n+1))<2/n$. La somme des $E$ plus grands
termes de cette forme, prise sur des entiers distincts, est au plus la somme sur
$2,4,\ldots,2E$, qui vaut $O(\log E)$. Donc $R(t)=O(\log E(t))$.

De plus $E(t)\to\infty$ : un run impair a longueur $v_2(n+1)<\infty$, donc une queue
infinie de pas impairs est impossible. Comme $\log_2(n_t+1)\ge0$,
$$\delta E(t)\le\log_2(N+1)+\beta t+R(t),$$
et $R(t)/t\to0$, d'où
$$\limsup_{t\to\infty} E(t)/t \le \beta/\delta.$$
En particulier $R(t)=o(E(t))$.

**(H) donne la borne inférieure uniforme.** Numéroter les runs depuis le départ $N$,
$s_0=0$, $s_{k+1}=s_k+r_k+1$. Alors $E(s_k)=k$ et, sous (H),
$s_k\le(A+1)k+B\,x(N)$. Pour $s_k\le t<s_{k+1}$ on a $E(t)=k$ et
$t\le(A+1)(k+1)+B\,x(N)$, donc
$$\liminf_{t\to\infty} E(t)/t \ge 1/(A+1).$$
La constante ne dépend pas de $N$. Ainsi (H) implique la forme uniforme de (C), avec
$\eta_N\ge1/(A+1)$.

**Seuil.** Si $A<1/\beta$, alors $1/(A+1)>\beta/\delta$. Les deux bornes sur $E(t)/t$ se
contredisent. Donc (H) avec $A<1/\beta$ exclut toute orbite positive non bornée. Toute
paire compatible avec la simple possibilité d'une telle orbite doit vérifier $A\ge1/\beta$
et, par B4, $B>1$. Dans les deux régimes, (H) est une conjecture majeure, pas un lemme de
calcul de constante.

Le départ 27 donne une contrainte numérique indépendante : ses 13 premiers runs ont longueur
$2,5,1,2,3,4,1,0,3,2,6,0,4$, somme 33. Comme $28^3<2^{16}$, $\log_228<16/3$, et
$(9/5)(13+16/3)=33$, on a $(9/5)(13+\log_228)<33$. La diagonale $A=B=9/5$ est donc fausse,
alors que $9/5>1/\beta$. La diagonale $A=B=2$ survit à cette fenêtre.

## 5. Obstacle pour $B>1$

La famille de B4 ne réfute aucun $B>1$. Tout exposant admissible vérifie
$5\cdot3^r+1\ge2^m$, donc $r>\bigl(m-\log_25-1\bigr)/\delta$ pour $m\ge2$. Si $B>1+\delta$,
le facteur $(B-1)r$ domine $m$, et un $A$ assez grand absorbe les petits $m$. Pour
$1<B\le1+\delta$, cette minoration linéaire ne tranche pas. Le plus petit $r$ calculé pour
chaque $m\le40$ et pour $a=5$ est de l'ordre de $2^{m-O(1)}$, bien au-dessus de $m/(B-1)$ ;
même observation pour $a\in\{7,13,21\}$ jusqu'à $m=32$. Ce n'est pas une preuve pour tout $m$.

Une fenêtre de deux runs ne peut pas dépasser la borne de B5 : la somme est $\le(1+\delta)\,x(M)$.
Réfuter un $B\in(1,1+\delta]$ exigerait une famille où l'exposant réalisant une grande
valuation reste plus petit qu'une fraction fixe de cette valuation, assez longtemps pour que
l'excédent $r_1-(B-1)r_0$ tende vers l'infini. Le logarithme discret 2-adique va dans l'autre
sens pour les parties impaires fixes testées. Allonger le balayage des graines impaires ne
ferait pas apparaître cette famille.

Contrôle fini, distinct de la preuve : sur chaque graine impaire $<100000$, et chaque graine
paire $<50000$, toute fenêtre issue de la graine vérifie
$\rho=(\sum_{j<k}r_j)/(k+x)<2$. Le maximum impair est $\rho=1{,}853\ldots$, atteint par les
13 premiers runs de 27. Le maximum pair observé est environ $1{,}668$, en 54.

## 6. Ce que ce cycle ne montre pas

Aucune paire $(A,B)$ n'est établie. La densité uniforme (C) reste ouverte : B6 dit seulement
que (H) l'impliquerait. La pente conditionnelle de complexité $1/\beta$ n'est pas améliorée.
Les textes des PR #21–#26 restent non validés en tant que dossiers ; B4–B6 sont prouvés
dans cette note, sans les invoquer.

## 7. Mises à jour

Les index parallèles `MEMORY.md` et `AGENDA.md`, ainsi que la rédaction
`HEIGHT_SENSITIVE_RUN_BOUND.md`, sont retirés : ils contredisaient le statut du
mot triangulaire déjà clos par le cycle 001 et faisaient de $A=B=2$ la question
suivante. L'index canonique reste `agenda.md`. Les notes importées des pointes
`eb79964` et `a0c3838` restent dans l'arbre ; leur statut est la section C de
`proved.md` (NON VALIDÉ), sauf ce que B2 et B4–B6 établissent ici.

- `proved.md` : B4, B5, B6.
- `counterexamples.md` : X16 (pente $B\le1$), X17 (diagonale $9/5$, témoin 27).
- `hypotheses.md` : H2 reclassée conjecture majeure ; le régime $B\le1$ est clos.
- `abandoned.md` : la piste « (H) comme petit lemme de pente $\le1$ » est fermée.
- `agenda.md` : l'entrée (H) est retirée de la tête. Prochaine question : H4.

## 8. Reproduire

```sh
python3 research/checks/cycle002_run_bound.py
```

Sortie attendue : une ligne `PASS` (ordre de 3, excédent $a=5$ jusqu'à $m=32$, témoin
$r=757$, Mersenne, comparaison 27, et $\rho<2$ sur les graines impaires $<100000$).
