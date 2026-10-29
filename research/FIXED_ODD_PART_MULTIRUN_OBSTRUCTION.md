# Surjectivité des fenêtres de runs après une partie impaire initiale fixée

**28 octobre 2026 — résultat exact, sans revendication de nouveauté scientifique.**

**Verdict : obstruction formelle à une classe d'arguments locaux sur trois runs ou plus.** Ce travail ne prouve ni densité positive des pas pairs sur une orbite non bornée, ni amélioration de la pente de complexité, ni la conjecture de Syracuse.

Contexte : suite de la [PR #25](https://github.com/hsirven1/syracuse_search/pull/25), qui a validé à partir du PDF original de Yu (1999) la borne uniforme
\[
v_2(3^r a+1)\le C(1+\log_2 a)\log_2(2+r)
\]
pour \(a\ge1\) impair et \(r\ge1\). **Il n'est pas nécessaire de réexaminer Yu.** L'objectif ici est de chercher une relation nouvelle entre **plusieurs** runs, puis d'essayer de la réfuter.

## 1. Lemme cible : surjectivité finie à partie impaire initiale \(a_0=5\)

Toujours considérer l'application **raccourcie**
\[
T(n)=\begin{cases}n/2& n\text{ pair}\\(3n+1)/2&n\text{ impair}.\end{cases}
\]
Un *run* de longueur \(r\ge0\) signifie le bloc de parités \(1^r0\), avec **exactement** \(r\) pas impairs puis un pas pair. L'usage de \(r=0\) autorise deux pas pairs consécutifs.

**Théorème (forme forte exacte, élémentaire).** Pour tout entier \(D\ge2\), l'application
\[
\begin{aligned}
\{\text{classes impaires }r\bmod2^{D-1}\}
&\longrightarrow \{\text{classes }y\bmod2^D:y\equiv3\bmod4\},\\
[r]&\longmapsto
\left[\frac{5\cdot3^r-1}{2}\right]\pmod{2^D}
\end{aligned} \tag{A}
\]
est une **bijection**.

Par conséquent, **pour tout mot binaire fini \(W\) commençant par \(11\)** et de longueur \(D\), il existe une **unique classe impaire \(r_0\bmod2^{D-1}\)** telle que, pour *chaque* entier positif \(r_0\) de cette classe,
\[
N=5\cdot2^{r_0}-1
\]
est un entier positif dont les \(r_0+1\) premières parités sont \(1^{r_0}0\), et dont les **\(D\) parités suivantes sont exactement \(W\)**.

En particulier, pour tout \(k\ge2\) et tout choix
\[
r_1\ge2,\quad r_2,\ldots,r_k\ge0,
\]
il existe une infinité d'entiers positifs avec **partie impaire initiale exactement \(a_0=(N+1)/2^{r_0}=5\)** et les \(k+1\) premiers runs exactement \(r_0,r_1,\ldots,r_k\).

### Preuve intégrale

**(i) Calcul exact du premier bloc.** Poser \(N=5\cdot2^{r_0}-1\), \(r_0\ge1\). Tant que la branche impaire est prise, \(T(x)+1=\frac32(x+1)\). Pour \(0\le t\le r_0\),
\[
T^t(N)+1=5\cdot3^t2^{r_0-t}.
\]
Pour \(0\le t<r_0\), l'état \(T^t(N)\) est impair. Au temps \(r_0\), il est pair car \(T^{r_0}(N)=5\cdot3^{r_0}-1\). Un pas pair plus tard,
\[
M_1=T^{r_0+1}(N)=\frac{5\cdot3^{r_0}-1}{2},
\qquad M_1+1=\frac{5\cdot3^{r_0}+1}{2}. \tag{B}
\]
La récurrence \((M_{i+1}+1)=(3^{r_i}a_i+1)/2\) de \`PADIC_SUCCESSIVE_RUNS.md\` est donc satisfaite **exactement**, avec \(a_0=5\).

**(ii) Ordre de 3.** Pour \(m\ge3\),
\[
\operatorname{ord}_{2^m}(3)=2^{m-2}. \tag{C}
\]
En effet, \(v_2(3^2-1)=3\), et pour \(j\ge1\),
\(v_2(3^{2^{j+1}}-1)=v_2(3^{2^j}-1)+v_2(3^{2^j}+1)
=(j+2)+1=j+3\).
Comme \(3\) est d'ordre une puissance de \(2\) modulo \(2^m\) et cette puissance est minimale pour atteindre la valuation \(m\), (C) suit.

**(iii) Bijection de résidus.** Pour \(r_0\) impair, \(3^{r_0}\equiv3\bmod8\) et \(5\cdot3^{r_0}\equiv7\bmod8\), d'où
\[
(5\cdot3^{r_0}-1)/2\equiv3\bmod4.
\]
Si deux exposants impairs \(r,s\) donnent le même résidu modulo \(2^D\), alors
\[
5(3^r-3^s)\equiv0\bmod2^{D+1}.
\]
Puisque \(5\cdot3^s\) est une unité, \(3^{r-s}\equiv1\bmod2^{D+1}\), et (C) équivaut à \(r\equiv s\bmod2^{D-1}\). L'application (A) est donc injective. Le domaine compte \(2^{D-2}\) classes impaires, tout comme l'ensemble d'arrivée compte \(2^{D-2}\) classes congrues à 3 modulo 4. Elle est donc bijective.

**(iv) Codage fini des parités.** Pour le \(T\) raccourci, chaque mot \(W\) de longueur \(D\) est réalisé par une unique classe \(y\bmod2^D\). Voici la justification élémentaire : si deux départs sont congrus modulo \(2^j\), ils possèdent les mêmes \(j\) premières parités ; lorsqu'on remplace un représentant \(n\) par \(n+2^j\), la formule affine de \(T^j\) montre que l'état au temps \(j\) change de \(3^q\), impair, et donc **sa parité bascule**. Par induction, chaque mot de longueur \(j\) se prolonge en exactement deux classes modulo \(2^{j+1}\), une de chaque parité. En particulier, \(W\) commence par \(11\) **si et seulement si** le représentant \(y\equiv3\bmod4\).

Par (iii) et (iv), il existe une unique classe impaire de \(r_0\bmod2^{D-1}\) telle que \(M_1\equiv y\bmod2^D\), et alors le mot de \(D\) parités de \(M_1\) est exactement \(W\). Ajouter un multiple positif de \(2^{D-1}\) à \(r_0\) conserve ce mot tout en rendant le départ positif arbitrairement grand.

Pour un vecteur de runs \(r_1,\ldots,r_k\), choisir
\(W=(1^{r_1}0)(1^{r_2}0)\cdots(1^{r_k}0)\).
Ce mot commence par \(11\) dès que \(r_1\ge2\). Le théorème assure donc **tous les runs exacts demandés**, et une infinité de graines. \(\square\)

## 2. Contre-exemples à une famille de lemmes locaux tentants

Soient \(k\ge2\) **fixé** et \(R\ge2\) arbitraire. Le choix
\[
W=(1^R0)^k
\]
produit un entier positif \(N=5\cdot2^{r_0}-1\) tel que les \(k\) runs après le premier ont **tous** longueur \(R\). Donc
\[
\sum_{j=1}^{k}r_j=kR
\]
est arbitrairement grande **même avec \(a_0=5\) fixé**.

Cela réfute chaque assertion universelle de type
\[
\text{« pour toutes les orbites positives, } \sum_{j=1}^{k}r_j
\le F(k,a_0)\text{ »},
\]
pour tout \(F(k,5)\) fini indépendant de \(r_0\). La conclusion reste vraie si l'on exige que les \(k+1\) runs soient calculés selon les *identités entières exactes*, et non selon une simple approximation réelle.

**Exemple exact compact, sans recherche massive :** \(W=1101110\) (runs \(r_1=2,r_2=3\), \(D=7\)). La classe canonique est \(y=91\bmod128\). Un exposant est \(r_0=7\), car
\[
M_1=\frac{5\cdot3^7-1}{2}=5467\equiv91\bmod128.
\]
Ainsi \(N=5\cdot2^7-1=\mathbf{639}\) a les 15 premières parités
\[
\underbrace{1111111}_{r_0=7}0\,\underbrace{11}_{r_1=2}0\,
\underbrace{111}_{r_2=3}0.
\]
Tous les temps et les signes sont de vrais entiers positifs.

**Contrôles exacts réellement exécutés en Python indépendant :** pour \(2\le D\le9\), les \(2^{D-2}\) classes impaires d'exposants modulo \(2^{D-1}\) ont produit exactement \(2^{D-2}\) classes finales distinctes, et leurs facteurs de longueur \(D\) commencent tous par \(11\). Le préfixe de \(N=639\) a été itéré directement et vérifié. Ce sont de **petits** contrôles adverses, **pas** une preuve de l'énoncé général ; celle-ci précède.

## 3. Limites logiques et relation à Yu (1999)

**On n'a PAS démontré** qu'une même orbite de départ fixé possède une moyenne non bornée des runs, ni qu'une orbite positive non bornée possède une densité nulle de pas pairs.

L'exposant initial \(r_0\) **change avec le mot fini \(W\)** et doit généralement devenir très grand pour forcer des runs ultérieurs énormes. La borne prouvée par Yu,
\[
r_1+1=v_2(3^{r_0}5+1)\le C(1+\log_2 5)\log_2(2+r_0),
\]
reste entièrement compatible avec les exemples : la somme des runs peut grandir parce que le coût du premier \(r_0\) grandit aussi. Ce théorème **ne réfute pas** une inégalité de dissipation dépendant explicitement de \(r_0\), de \(M_i\) ou de la hauteur de l'état, et n'élimine pas une argumentation sur des fenêtres de longueur \(k\to\infty\) pour une **seule orbite fixe**.

Le passage illégitime serait « tout préfixe fini a une réalisation positive » \(\Rightarrow\) « il existe un départ positif réalisant tout le mot infini ». En prenant la limite 2-adique des résidus des parités, on obtient bien un départ dans \(\mathbb Z_2\), mais **pas nécessairement un entier positif ordinaire**. Cette distinction est l'obstacle central, bien connu dans le codage des parités.

La structure globale du codage fini est classique : R. Terras (1976), C. J. Everett (1977), et D. J. Bernstein–J. C. Lagarias, [*The 3x+1 conjugacy map*](https://doi.org/10.4153/CJM-1996-060-2), *Canadian Journal of Mathematics* **48** (1996), 1154–1169. La bijection supplémentaire (A) découle simplement de ce codage et de la structure classique des unités modulo \(2^m\). **Aucune recherche d'antériorité exhaustive ni nouveauté revendiquée.**

## Verdict et unique prochaine expérience mathématique

**PROUVÉ :** bijection exacte (A), même avec \(a_0=5\) fixé ; réalisation de tous les vecteurs finis de runs commençant après le premier par \(r_1\ge2\) ; impossibilité d'une borne universelle sur ces fenêtres \(k\) lorsque le coût \(r_0\) est omis.

**NON PROUVÉ :** obstruction globale sur tous les préfixes d'un seul entier positif, borne de moyenne des runs, densité positive, amélioration de la pente, conjecture de Syracuse.

**Prochaine expérience unique :** essayer de démontrer ou **réfuter par une famille exacte d'entiers** une inégalité *sensible à la hauteur* et à une fenêtre de longueur variable :
\[
\tag{H}
\sum_{j=0}^{k-1}r_{i+j}\ \le\ A k+B\log_2(M_i+1)
\quad(\forall N>0,\ i\ge0,\ k\ge1),
\]
avec des constantes universelles \(A,B\), et \(M_i=n_{s_i}\) au début du \(i\)-ième run. **(H) n'est pas un théorème, ni une hypothèse à accepter ; c'est une cible contradictoire précise.** Une preuve de (H) sur les trajectoires entières impliquerait pour chaque départ fixe une moyenne asymptotiquement bornée des runs, donc la densité inférieure positive de pas pairs. Les exemples finis présents n'invalident pas (H), car les grandes valeurs de \(r_0\) entrent précisément dans sa correction de hauteur.

**Implication exacte de (H), si elle était démontrée.** Prendre \(i=0\) et poser
\(S_k=\sum_{j=0}^{k-1}r_j\), \(c_N=B\log_2(N+1)\). Alors (H) donnerait
\[
S_k\le Ak+c_N,\qquad s_k=S_k+k\le(A+1)k+c_N.
\]
Pour \(s_k\le t<s_{k+1}\), le nombre de pas pairs est exactement \(E(t)=k\). Or
\(t<s_{k+1}\le(A+1)(k+1)+c_N\), et donc
\[
\liminf_{t\to\infty}\frac{E(t)}{t}\ge\frac1{A+1}>0.
\]
Ainsi (H) est **strictement plus ambitieuse** qu'une simple optimisation du terme log-log. Le présent résultat de surjectivité *ne* prouve ni *ne* réfute (H).
 Toute nouvelle recherche doit commencer par chercher un contre-exemple analytique à (H), et non augmenter \(D\) dans les simulations.

Ne pas fusionner la branche ; aucun fichier de données volumineux n'est nécessaire.
