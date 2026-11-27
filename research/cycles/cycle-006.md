# Cycle 006 — Runs appariés et deux valeurs de Tschakaloff

Date : 27 novembre 2026. Axe **B**.
Branche : `research/memory`. Script : [`../checks/cycle006_paired_runs.py`](../checks/cycle006_paired_runs.py).

**Verdict : la réalisation est PROUVÉE égale, dans $\mathbb Q_2$, à une combinaison
$\mathbb Q$-linéaire de deux valeurs de Tschakaloff. Cette combinaison n'est pas
exclue de $\mathbb Z_{(2)}$ par les énoncés lus. L'appartenance de $\xi_w$ à
$\mathbb Q$ reste OUVERTE.** Väänänen–Wallisser 1989 ne s'applique pas : sur ce
$q$, $\gamma>\Gamma(2,0)$. Les Satz 1 et 2 de Bundschuh 1974, lus sur le scan,
sont des énoncés archimédiens dont l'hypothèse échoue déjà pour une seule
valeur. Les originaux de Bézivin 1988 et d'Amou–Väänänen 2005 n'ont pas été
obtenus ; les énoncés cités par ailleurs ne portent pas sur la valeur
2-adique de ce $q$. Ni (C), ni Syracuse.

La comparaison de Liouville du premier jet est corrigée au §2 et au §11
(X22). Avec le run $r_{m+1}$ et $\beta=\log_2(3/2)$, on a encore
$Q_m\to-\infty$, donc B7 ne donne pas l'irrationalité. Le supremum vaut
$Q_2=\log_2(2048/217)$ : tout $\sigma=a/b$ rationnel vérifie
$\max(|a|,b)\ge10$.

## 0. Question traitée

Première entrée de l'agenda, après la revue `6081884788` sur le SHA
`0b935a943b7972fa3998ac98b2c53fcc6772ea5b`. Cette revue confirme les
corrections du cycle 005 et ne demande aucun changement ; elle est
enregistrée au §11 du cycle 005 et dans `reviews.md`.

Mot à un zéro par bloc, $r_j=j+[j\text{ impair}]$. La réalisation 2-adique
est-elle une combinaison $\mathbb Q$-linéaire de deux valeurs $f_q(\alpha_i)$ ?
Si oui, l'un des énoncés de Bézivin, de Bundschuh ou d'Amou–Väänänen
l'exclut-il de $\mathbb Z_{(2)}$ ? L'obstruction $\Gamma(2,0)<\gamma$ doit
être vérifiée sur l'énoncé cité. Dépendances utilisées : B1 et la
transcription du Satz de VW 1989 déjà en `prior_art.md`. Ce cycle ne relit
pas ce Satz.

## 1. Le mot

$[j\text{ impair}]$ vaut $1$ si $j$ est impair et $0$ sinon. Donc
$r_{2m-1}=r_{2m}=2m$ : les longueurs sont $2,2,4,4,6,6,\ldots$ Ce n'est pas
une progression arithmétique. Les écarts alternent entre $0$ et $2$.

Le $j$-ième zéro est précédé de $o_j=\sum_{i=1}^j r_i$ impairs. Par
récurrence, $o_1=2$ et
$$o_{2m-1}=2m^2,\qquad o_{2m}=2m(m+1)\qquad(m\ge1).$$
En effet $o_{2m}=o_{2m-1}+2m$ et $o_{2m+1}=o_{2m}+2(m+1)$.

## 2. Recherche de contre-exemples, avant l'identité

Dans B7, $\beta=\log_2(3/2)$ et $\delta=\log_2 3$. Le run qui entre dans
$Q_m$ est $o_{m+1}-o_m$. Sur ce mot, le $m$-ième zéro clôt le run $r_m$,
donc ce run est $r_{m+1}$, pas $r_m$. Le premier terme de $G_m$ vaut
$8/9>0$, d'où
$$Q_m=r_{m+1}+m+1-\beta o_m-\log_2(1+G_m)
=\log_2\Bigl(\frac{2^{o_m+r_{m+1}+m+1}}{3^{o_m}+P_m}\Bigr).$$
Le premier jet posait $\beta=\log_2 3$ et testait
$2^{r_m+m+1}<3^{o_m}+P_m$. L'exposant omet $o_m$ et le run est le mauvais.
Les deux phrases « $Q_m<0$ dès $m\ge4$ » et « aucun rationnel de petite
hauteur n'est exclu » sont fausses (X22). De $9>8$ on tire $\beta>1/2$,
car $\log_2(3/2)>1/2$ équivaut à $9/4>2$, et, séparément, $\delta>3/2$.

1. **$Q_4>0$.** Ici $o_4=12$ et $r_5=6$, donc l'exposant vaut $23$.
   La récurrence $P_1=2^{1+o_1}$ et $P_m=3^{r_m}P_{m-1}+2^{m+o_m}$ donne
   $P_1=8$, $P_2=136$, $P_3=13\,064$ et $P_4=1\,123\,720$. Ainsi
   $3^{12}+P_4=1\,655\,161$ et $2^{23}=8\,388\,608>1\,655\,161$.

2. **Le supremum est $Q_2$, et il exclut la hauteur $\le9$.**
   On a $o_2=4$, $r_3=4$ et $3^4+P_2=217$, donc $2^{Q_2}=2048/217$.
   Comme $9\cdot217=1953<2048<2170=10\cdot217$, on a
   $9<2^{Q_2}<10$. Les produits
   $2048\cdot17>64\cdot217$, $2048\cdot19\,625>65\,536\cdot217$ et
   $2048\cdot1\,655\,161>8\,388\,608\cdot217$ donnent
   $Q_2>Q_1,Q_3,Q_4$. Le point 3 donne $Q_m<0<Q_2$ pour tout $m\ge5$.
   Donc $\sup_m Q_m=Q_2$. Si $\sigma=a/b$ est irréductible et $b>0$,
   B7 impose $\max(|a|,b)\ge10$. La hauteur $9$ est exclue ; la hauteur
   $10$ ne l'est pas par cette seule comparaison. Pour un entier $\xi$,
   $\sigma=-2(\xi+1)$ a dénominateur $1$, donc $|\xi+1|\le4$ est exclu.

3. **Malgré cela, $Q_m\to-\infty$.** On a $r_j\le j+1$, donc
   $r_{m+1}\le m+2$, et $o_m\ge m(m+1)/2$. Puisque
   $\log_2(1+G_m)>0$ et $\beta>1/2$,
   $$Q_m<2m+3-\beta\,m(m+1)/2<2m+3-\frac{m(m+1)}{4}
   =\frac{12+7m-m^2}{4}.$$
   Le trinôme $m^2-7m-12$ vaut $6$ en $m=9$, et sa dérivée $2m-7$ est
   positive pour $m\ge4$. Il reste donc positif, et le majorant est
   négatif pour tout $m\ge9$. Ce majorant tend vers $-\infty$, donc
   $Q_m<0$ pour $m\ge9$ et $Q_m\to-\infty$. Pour $5\le m\le8$,
   l'inégalité entière $2^{o_m+r_{m+1}+m+1}<3^{o_m}+P_m$ se lit
   $$2^{30}<1\,215\,000\,977,\quad
   2^{39}<886\,809\,454\,057,$$
   $$2^{48}<5\,818\,906\,583\,881\,865,\quad
   2^{59}<38\,178\,127\,571\,825\,626\,921.$$
   L'hypothèse $\sup_m Q_m=+\infty$ de B7 est fausse. B7 n'exclut pas
   $\xi_w$ de $\mathbb Q$.

4. **Le mot n'est pas ultimement périodique.** Les runs sont non bornés.
   Cela n'interdit pas un rationnel : la réciproque du théorème de Lagarias
   est la conjecture H3.

5. **Les rapports $\alpha_i/\alpha_j$ ne sont pas des puissances de $q$.**
   Voir le §4. Ce n'est pas l'obstruction.

Aucun contre-exemple à l'identité du §3. Aucun des énoncés lus ne fournit
l'exclusion de $\mathbb Z_{(2)}$ ; cela laisse la question ouverte, sans
la réfuter.

## 3. Preuve de la combinaison

On note $f_q(x)=\sum_{n\ge0}q^{-n(n+1)/2}x^n$, comme dans VW 1989, et
$q=81/16$. La série de B1 est
$$S=\sum_{j\ge1}2^j\Bigl(\frac23\Bigr)^{o_j}=\sum_{m\ge1}(a_m+b_m),$$
où le terme impair et le terme pair valent
$$a_m=2^{2m-1}\Bigl(\frac23\Bigr)^{2m^2}=\frac{2^{2m^2+2m-1}}{3^{2m^2}},$$
$$b_m=2^{2m}\Bigl(\frac23\Bigr)^{2m(m+1)}=\frac{2^{2m^2+4m}}{3^{2m^2+2m}}.$$
Poser $u_m(\alpha)=q^{-m(m+1)/2}\alpha^m=(16/81)^{m(m+1)/2}\alpha^m$. Alors
\begin{align*}
u_m(4)
&=2^{2m(m+1)}\,3^{-2m(m+1)}\,2^{2m}
=2^{2m^2+4m}\,3^{-(2m^2+2m)}
=b_m,\\
u_m(9)
&=2^{2m(m+1)}\,3^{-2m(m+1)}\,3^{2m}
=2^{2m^2+2m}\,3^{-2m^2}
=2a_m.
\end{align*}
Donc $a_m=\tfrac12 u_m(9)$ et $b_m=u_m(4)$. Comme $f_q(\alpha)=1+\sum_{m\ge1}u_m(\alpha)$,
$$S=\tfrac12\bigl(f_q(9)-1\bigr)+\bigl(f_q(4)-1\bigr)
=\tfrac12 f_q(9)+f_q(4)-\tfrac32.$$
B1 donne $\xi_w+1=-S/2$, d'où
$$\boxed{\ 4\xi_w+1+2f_q(4)+f_q(9)=0\ }$$
dans $\mathbb Q_2$, soit
$$\xi_w=-\tfrac14-\tfrac12 f_q(4)-\tfrac14 f_q(9).$$
Les puissances négatives de $2$ se compensent : $f_q(4)$ et $f_q(9)$
commencent par $1$, et
$$-\tfrac14-\tfrac12-\tfrac14=-1,$$
tandis que $v_2(u_m(4))=2m^2+4m\ge6$ et $v_2(u_m(9))=2m^2+2m\ge4$. Ainsi
$\xi_w+1$ est dans $4\mathbb Z_2$, et $\xi_w\in\mathbb Z_2$. Le mot commence
par $11$, donc $\xi_w\equiv3\pmod4$, ce qui est le même résidu.

L'équation fonctionnelle $f_q(x)=1+(x/q)f_q(x/q)$ envoie $4$ sur $64/81$ et
$9$ sur $16/9$. Elle ne ramène pas la forme $2f_q(4)+f_q(9)$ à une seule
valeur. La convergence 2-adique vient de $|q|_2=|81/16|_2=16>1$.

$\xi_w\in\mathbb Q$ si et seulement si $2f_q(4)+f_q(9)\in\mathbb Q$.

## 4. Väänänen–Wallisser 1989 ne s'applique pas

Les paramètres naturels du Satz, pour la forme
$h_0+h_1 f_q(4)+h_2 f_q(9)$, sont $l=2$, $\sigma=0$, $p=2$,
$q=81/16$, donc $r=81$, $s=16$, $h=\max(81,16)=81$, $\alpha_1=4$,
$\alpha_2=9$.

La condition sur les rapports est satisfaite. Si $n\ge1$,
$(81/16)^n\ge81/16>9/4>4/9$. Si $n=0$, la puissance vaut $1$. Si $n\le-1$
et $k=-n$, alors $(16/81)^k\le16/81<4/9<9/4$. Aucun des deux rapports
$4/9$ et $9/4$ n'est donc une puissance entière de $q$.

L'hypothèse $\gamma<\Gamma(2,0)$ est fausse. Ici
$|s|_2=2^{-4}$ et $\log|s|_2/\log h=-\log2/\log3$, donc
$$\gamma=1-\frac{\log2}{\log3},\qquad
\Gamma(2,0)=\frac{5-\sqrt{17}}{4}.$$
De $8<9$ on tire $\log2/\log3<2/3$. De $121<153$ on tire
$2/3<(\sqrt{17}-1)/4$, car $8<3(\sqrt{17}-1)$ équivaut à $11<3\sqrt{17}$.
Donc
$$\frac{\log2}{\log3}<\frac{\sqrt{17}-1}{4},$$
et $\gamma>\Gamma(2,0)$. Le Satz exige l'inégalité stricte inverse. Il ne
donne pas l'indépendance de $1$, $f_q(4)$ et $f_q(9)$ dans $\mathbb Q_2$.

C'est bien l'obstruction annoncée dans H5, vérifiée sur ce $q$ et ces deux
points, pas seulement rappelée pour un $l=2$ générique. La remarque
$|q|_2>1$ du Satz est, elle, satisfaite.

## 5. Bundschuh 1974, Satz 1 et Satz 2

Source lue : P. Bundschuh, *Verschärfung eines arithmetischen Satzes von
Tschakaloff*, Portugaliae Math. 33 (1974), fasc. 1, 1–17. Scan public de la
Biblioteca Nacional de Portugal,
`https://purl.pt/2719/1/j-5293-b-vol33-fasc1-art1_PDF/j-5293-b-vol33-fasc1-art1_PDF_01-B-R0300/j-5293-b-vol33-fasc1-art1_0000_capa1-17_t01-B-R0300.pdf`,
SHA-256 `ce7657b2fc46fd352eab9f5caff063d7e49697fe910a6348cac7375b3f85c7c8`.
Les énoncés sont à la page imprimée 2. La preuve, pages 3–17, n'a pas été
lue et n'est pas une prémisse.

La fonction du texte est $f(z)=\sum_{n\ge0}z^n q^{-n(n-1)/2}$, entière pour
$|q|>1$. Notre $f_q$ en diffère par le décalage
$f_q(x)=f(x/q)$. Les valeurs archimédiennes $f(64/81)$ et $f(16/9)$ sont
celles qui correspondraient à $f_q(4)$ et $f_q(9)$. Ce sont d'autres nombres
que les sommes 2-adiques : le texte majore $|f(z)|$ par le module complexe.

**Satz 1.** Si $q=q_1/q_2$ dans un corps imaginaire quadratique $K$, avec
$|q_1|>|q_2|^{(3+\sqrt5)/2}$, et si $a\in\mathbb C^\times$, alors $a\notin K$
ou $f(a)\notin K$.

**Satz 2.** Si $\gamma$ est défini par $\log|q_2|=\gamma\log|q_1|$ et
$0\le\gamma<2/(3+\sqrt5)$, alors $f(a)$, pour $a\in K^\times$, n'est pas
trop bien approché par les éléments de $K$. La constante
$2/(3+\sqrt5)$ est $(3-\sqrt5)/2$, car $(3-\sqrt5)(3+\sqrt5)=4$.

Pour $q=81/16$, on a $q_1=81$, $q_2=16$ et
$\gamma=\log2/\log3$. De $2^8=256>243=3^5$ on tire
$\log2/\log3>5/8$. De $80>49$ on tire $5/8>(3-\sqrt5)/2$, car
$\sqrt5>7/4$. L'hypothèse de chaque Satz échoue. Même l'irrationalité
archimédienne d'une seule valeur n'en sort pas.

Ces Satz ne contiennent pas $\Gamma(2,0)$. L'obstruction $\Gamma(2,0)<\gamma$
du Satz de VW n'y figure pas : le $\gamma$ de Bundschuh est
$\log|q_2|/\log|q_1|$, celui de VW est $1+\log|s|_2/\log h$, et les deux
nombres sont distincts. Surtout, la conclusion est un énoncé sur
$\mathbb C$, pas sur $\mathbb Q_2$. Elle n'exclut pas $\xi_w$ de
$\mathbb Z_{(2)}$.

## 6. Bézivin 1988 et Amou–Väänänen 2005

Les PDF originaux n'ont pas été obtenus (accès Springer refusé, pas de
copie ouverte trouvée). Ils ne sont pas des prémisses.

Ce qui a été lu à leur place :

- K. Väänänen, *On arithmetic properties of $q$-series*, RIMS Kôkyûroku
  1665 (2009), 47–59,
  `https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1665-08.pdf`,
  SHA-256 `fc5045b5207441a7d2091b20e99688961be096cd506d3f5b5929a663cc4804f2`.
  Le théorème 5, attribué à Bézivin, Manuscripta Math. 61 (1988), 103–129,
  énonce une indépendance linéaire sur un corps imaginaire quadratique, et
  le texte précise qu'elle vaut pour l'ensemble des places infinies. La
  spécialisation à la fonction de Tschakaloff y demande un entier $Q$ de ce
  corps avec $|Q|>1$. Ici $81/16$ n'est pas un entier algébrique. Le
  symbole $\Gamma(2,0)$ n'apparaît pas dans cet énoncé.
- K. Väänänen et V. V. Zudilin, *Linear independence of values of
  Tschakaloff series*, Russian Math. Surveys 62 (2007), note de trois
  pages,
  `https://wain.mi-ras.ru/PS/chak-br.pdf`,
  SHA-256 `10ae0ac2b3952174e8cd227dea939d4e6aabb9148b94ddd196483e2cfad85a87`.
  Le théorème 1 suppose $q\in\mathbb Z\setminus\{0,\pm1\}$. Il cite
  Amou–Väänänen, Monatsh. Math. 144 (2005), 1–11, comme le seul résultat
  antérieur pour des paramètres distincts, et le dit très restrictif. Les
  majorations du texte sont des modules ordinaires. Le compte rendu
  zbMATH 1066.11031, signé Bundschuh, décrit le même article avec
  $q\in\mathbb Z$, $|q|>1$, et une borne inférieure $\gamma(L,m)$ sur des
  exposants entiers $s_i$. Ce $\gamma(L,m)$ n'est pas le $\Gamma(2,0)$ de
  VW. Le compte rendu n'a pas été confronté à l'original.

Aucun de ces énoncés lus n'affirme que $2f_{81/16}(4)+f_{81/16}(9)$ est
irrationnel dans $\mathbb Q_2$. Les appliquer à $\xi_w$ dépasserait le
texte. La piste « irrationalité réelle, donc irrationalité 2-adique » est
déjà abandonnée (X14).

Le même survey énonce, sous le nom d'Amou–Matala-aho–Väänänen (Acta Arith.
127, 2007), un critère en une place $v$ avec une condition « $Q$ presque
entier ». Cet article n'est pas celui que l'agenda nommait, et son
original n'a pas été lu. Il n'est pas une prémisse, ni la question
suivante.

## 7. Ce que ce cycle ne montre pas

- $\xi_w\notin\mathbb Q$, ni $\xi_w\notin\mathbb Z_{(2)}$.
- L'indépendance de $1$, $f_q(4)$ et $f_q(9)$ dans $\mathbb Q_2$.
- Rien sur les autres familles de H5 ($r_j=\lfloor j/P\rfloor$, perturbation
  périodique générale).
- Rien sur (C), ni sur Syracuse.
- Rien qui relise la preuve de VW 1989, ni celle de Bundschuh.

## 8. Mises à jour de la mémoire

- `proved.md` : B11, l'identité seulement. Pas une exclusion.
- `hypotheses.md` : H5, cette famille réduite ; irrationalité ouverte.
- `prior_art.md` : lectures du cycle.
- `abandoned.md` : ne pas relancer B7 pour prouver l'irrationalité, ni VW
  avec $l=2$, ni les Satz 1–2 de Bundschuh 1974, sur ce mot. Le correctif
  X22 ne change pas cet abandon : $Q_m\to-\infty$.
- `agenda.md` : question retirée. Prochaine question : axe C, non entamée.
- `reviews.md` : revues `6081884788` et `6081961103`.

## 9. Prochaine question

Axe **C**. Lire Berg–Meinardus, Wirsching (LNM 1681) ou Mori 2024, et en
extraire un seul énoncé réfutable, par exemple une prédiction sur un
tronqué fini, avant tout calcul. Documentaire d'abord. Ne pas rouvrir le
mot de ce cycle. Cette question n'est pas entamée : le correctif du §11
doit être revu d'abord.

## 10. Reproduire

```sh
python3 research/checks/cycle006_paired_runs.py
```
Sortie attendue : cinq lignes `PASS`. Elles couvrent les sommes jusqu'à
$m=40$, l'identité des termes pour $1\le m\le12$, les rapports pour
$|n|\le8$, les quatre comparaisons d'entiers, $Q_m>0$ pour $1\le m\le4$,
$Q_m<0$ pour $5\le m\le40$, le supremum $Q_2$ et la hauteur $9<2048/217<10$.
L'identité des termes est prouvée au §3 pour tout $m$ ; le script n'en
vérifie qu'un segment. De même, l'exclusion de toutes les puissances
$q^n$ est au §4, pas dans la boucle $|n|\le8$. La chute $Q_m\to-\infty$
pour $m\ge9$ est le majorant du §2 ; le script ne contrôle le signe du
trinôme que pour $9\le m\le20$.

## 11. Revue `6081961103`

Revue indépendante sur le SHA
`fcd6a008ed0aad5ee2033ee3b9123ba6cacd0237` (PR #27). L'identité B11,
§§1 et 3, est confirmée par cette revue. Elle n'a pas été réécrite.
L'objection sur le §2 a été reproduite en entiers : $2^{23}>1\,655\,161$
et $2048>9\cdot217$. Le test du script comparait $2^{r_m+m+1}$ à
$3^{o_m}+P_m$. Il passait, et il ne calculait pas $Q_m$. Le §2 et le
script sont corrigés. La conclusion rectifiée est prouvée ici :
$Q_m\to-\infty$, donc B7 ne donne pas l'irrationalité, tandis que
$\sup_m Q_m=Q_2$ exclut $\max(|a|,b)\le9$.

Les §§4–6 restent inchangés. La revue n'a pas relu les scans de VW 1989
ni de Bundschuh 1974 ; ce dépôt les avait déjà lus, et ce correctif ne
les rouvre pas. Elle signale que le corollaire 5.2
d'Amou–Matala-aho–Väänänen, Acta Arith. 127 (2007), échoue pour la
spécialisation $s=1$, $a(z)=1$, deux arguments, base $16/81$, parce que
$|\lambda|=\log_2 3>3/2$ et que (5.4) échoue pour $m=2$. Ce PDF n'a pas
été lu ici. L'article reste hors des prémisses, comme au §6. Cette
remarque ne prouve pas, ni ne réfute, l'irrationalité de $\xi_w$.

La question du §9 n'est pas entamée.
