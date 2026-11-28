# Cycle 003 — Critère de Liouville pour les réalisations rationnelles

Date : 26 novembre 2026. Axe **B**.
Branche : `research/memory`. Script : [`../checks/cycle003_liouville.py`](../checks/cycle003_liouville.py).

**Verdict : PROUVÉ.** Si la quantité $Q_m$ définie ci-dessous n'est pas bornée, la
réalisation 2-adique n'est pas rationnelle (B7). Le mot dont les runs impairs ont
longueurs $2,4,8,16,\ldots$ vérifie $Q_k>k$ (B8) : son réalisateur est irrationnel,
par un argument élémentaire. Le mot triangulaire donne $Q_m\to-\infty$ (X18) : B7
ne retrouve pas B2. Ni (C), ni Syracuse.

## 0. Question traitée

Première entrée de l'agenda : rédiger le critère H4, le confronter aux cycles
rationnels ($3x+b$, $b$ impair petit, et plus généralement tout mot périodique court),
et le situer par rapport à Lagarias, Bernstein–Lagarias, Monks–Yazinski,
López–Stoll et au manuscrit de De Jesús.

## 1. Définitions

$T$ est l'application raccourcie. Un mot $w\in\{0,1\}^{\mathbb N}$ est l'itinéraire
d'un unique $\xi_w\in\mathbb Z_2$, avec $w_t=1$ si et seulement si $T^t(\xi_w)$ est
impair. On suppose $w$ a une infinité de $0$. Le $j$-ième $0$ est en position $e_j$
(positions à partir de $0$) et $o_j$ est le nombre de $1$ strictement avant $e_j$,
donc $o_j=e_j-(j-1)$. On pose $r_m=o_{m+1}-o_m$.

La formule B1 s'écrit $\xi_w+1=-\frac12\sum_{j\ge1}2^j(2/3)^{o_j}$. On pose
$$\sigma=-2(\xi_w+1)=\sum_{j\ge1}\frac{2^{j+o_j}}{3^{o_j}}\in\mathbb Z_2,$$
$G_m=\sum_{j=1}^m 2^{j+o_j}/3^{o_j}$ (somme partielle, rationnel positif) et
$P_m=3^{o_m}G_m=\sum_{j=1}^m 2^{j+o_j}3^{o_m-o_j}\in\mathbb N$. Enfin $\beta=\log_2(3/2)$,
$\delta=\log_23$ et
$$Q_m=r_m+m+1-\beta o_m-\log_2(1+G_m).$$
La somme qui définit $G_m$ commence à $j=1$ : c'est la somme partielle de B1, sans
terme d'indice $0$.

## 2. Théorème B7

Si $\sup_m Q_m=+\infty$, alors $\xi_w\notin\mathbb Q$.

**Preuve.** Supposons $\sigma=a/b$ irréductible, $b>0$. Chaque terme de la série a
une valuation $j+o_j\ge1$, donc $\sigma\in\mathbb Z_2$ et $b$ est impair.
$A_m=a\,3^{o_m}-b P_m$ est un entier. Il est non nul : le reste
$\sigma-G_m=\sum_{j\ge m+1}2^{j+o_j}/3^{o_j}$ n'est pas nul dans $\mathbb Q_2$, puisqu'il
existe un $(m+1)$-ième $0$.

La valuation est exacte. Dans $\mathbb Q_2$,
$$3^{o_{m+1}}(\sigma-G_m)=\sum_{j\ge m+1}2^{j+o_j}3^{o_{m+1}-o_j}.$$
Le terme $j=m+1$ vaut $2^{m+1+o_{m+1}}$. Pour $j\ge m+2$,
$j+o_j\ge m+2+o_{m+2}\ge m+2+o_{m+1}$. Pas d'annulation, donc le membre de gauche a
pour valuation $m+1+o_{m+1}$. Or ce membre vaut $3^{r_m}A_m/b$, et $b$ comme $3$ est
impair, d'où $v_2(A_m)=m+1+o_{m+1}$. En particulier
$|A_m|\ge2^{m+1+o_{m+1}}$.

Côté archimédien, les termes sont positifs, donc $G_m$ est la valeur réelle de la
somme partielle et $|a-b G_m|\le|a|+b G_m$. Ainsi
$$|A_m|\le|a|\,3^{o_m}+b P_m\le\max(|a|,b)\,(3^{o_m}+P_m)=\max(|a|,b)\,3^{o_m}(1+G_m).$$
En prenant $\log_2$ et en écrivant $o_{m+1}=o_m+r_m$,
$$Q_m\le\log_2\max(|a|,b).$$
Le supremum est fini. ∎

La forme entière qu'on teste suppose $L\in\mathbb Z$. Posons
$E=o_m+r_m+m+1-L$. Alors $Q_m>L$ si et seulement si $2^E>3^{o_m}+P_m$.
Si $E\ge0$, les deux membres sont entiers. Si $E<0$, on chasse le dénominateur :
l'inégalité équivaut à $1>(3^{o_m}+P_m)\,2^{-E}$. Or $P_m\ge2$ et $-E\ge1$, donc
le membre de droite est un entier $\ge6$, et $Q_m>L$ est faux. La preuve ci-dessus
n'utilise pas cette forme : elle passe par $\log_2$.

## 3. Théorème B8

Soit $w=\prod_{k\ge1}(0\,1^{2^k})$. Alors $o_k=2^k-2$, $r_k=2^k$ et $Q_k>k$ pour
tout $k\ge1$. Donc $\xi_w\notin\mathbb Q$.

La densité des $1$ vaut $1$ : après $K$ blocs, il y a $2^{K+1}-2$ symboles $1$ et
$K$ symboles $0$.

**Preuve.** $Q_k>k$ équivaut à $2^{o_k+r_k+1}>3^{o_k}+P_k$. L'exposant vaut
$2^{k+1}-1$.

Pour $k=1$ : $o_1=0$, $P_1=2$ et $2^3=8>3$.

Pour $k\ge2$, on majore la somme réelle $t_j=2^{j+o_j}/3^{o_j}$. On a $t_1=2$,
$t_2=16/9$, $t_3=512/729$, et pour $j\ge2$
$$t_{j+1}/t_j=2\,(2/3)^{2^j}\le2\,(2/3)^4=32/81<1/2,$$
puisque $64<81$. Donc $\sum_{j\ge3}t_j<2 t_3=1024/729$ et
$$G_k<2+\frac{16}{9}+\frac{1024}{729}=\frac{3778}{729},\qquad 1+G_k<\frac{4507}{729}.$$
Par ailleurs
$$\frac{2^{2^{k+1}-1}}{3^{2^k-2}}=8\Bigl(\frac43\Bigr)^{2^k-2}.$$
Pour $k\ge2$ l'exposant $2^k-2$ est au moins $2$, donc ce rapport est au moins
$8\cdot(4/3)^2=128/9$. Et $128/9>4507/729$, car $128\cdot729=93312>40563=9\cdot4507$.
Ainsi $2^{2^{k+1}-1}>3^{o_k}(1+G_k)$. ∎

## 4. Ce que B7 ne voit pas (X18)

Sur le mot triangulaire $(1^j0)_{j\ge1}$, on a $o_m=m(m+1)/2$ et $r_m=m+1$. Le
premier terme de $P_m$ est $s_1=4\cdot3^{o_m-1}$. Posons
$E(m)=3^{o_m-1}/2^{o_m+2m}$. Alors
$$Q_m=\log_2\Bigl(\frac{2^{m+1+o_{m+1}}}{3^{o_m}(1+G_m)}\Bigr)\le\log_2\Bigl(\frac{2^{o_m+2m+2}}{s_1}\Bigr)=-\log_2 E(m),$$
dès que $E(m)>0$, ce qui est toujours vrai. Le rapport des $E$ est
$E(m+1)/E(m)=3^{m+1}/2^{m+3}$. Pour $m=8$, $3^{35}>2^{52}$, donc $E(8)>1$, et
$3^9>2^{11}$. Si $3^{m+1}>2^{m+3}$, alors $3^{m+2}>2^{m+4}$ parce que $3>2$. Donc
pour tout $m\ge8$,
$$E(m+1)/E(m)\ge(3^9/2^{11})\,(3/2)^{m-8}>9,$$
et $E(m)>9^{m-8}\to+\infty$. Ainsi $Q_m\to-\infty$. Le supremum est fini : B7 ne
s'applique pas. L'irrationalité de ce mot reste celle de B2, qui dépend de
Väänänen–Wallisser. Le script constate en outre que l'inégalité stricte
$2^{m+1+o_{m+1}}<3^{o_m}+P_m$ est déjà vraie pour $6\le m\le14$.

## 5. Contrôles sur les rationnels

La direction facile du théorème de périodicité est élémentaire : le mot périodique
$w$ de longueur $s$, avec $q$ symboles $1$ et terme constant $B$ de la branche affine,
est réalisé par $B/(2^s-3^q)$. Le dénominateur $2^s-3^q$ est impair. On a vérifié,
en entiers exacts :

- les $8178$ mots de longueur $1$ à $12$ qui contiennent au moins un $0$ ($187\,885$
  fenêtres) : $v_2(A_m)=m+1+o_{m+1}$ et la borne triangulaire ;
- les préfixes de longueur $\le4$ devant un cycle de longueur $\le6$ ($3720$
  réalisations, toutes dans $\mathbb Z_{(2)}$, $56\,420$ fenêtres) ;
- les départs $a/b$ avec $b$ impair $\le63$ et $|a|\le120$ ($7712$ orbites,
  $118\,882$ fenêtres). Seules les fenêtres atteintes depuis ces départs, dans la
  limite de $250$ pas ou $18$ zéros, sont testées. Ce balayage ne couvre pas les
  cycles de $3x+b$ : pour le paramètre $13$,
  $227\to347\to527\to797\to1202\to601\to908\to454\to227$ est un cycle exact.
  Les points $n/13$ forment un cycle de $T$ de dénominateur réduit $13$, et aucun
  n'est visité (X19). Le mot $(11110100)^\infty$, de longueur $8$, est déjà dans
  le contrôle des mots périodiques de longueur $\le12$ ;
- les témoins $\xi=0$, $\xi=1$, $\xi=-5$, et l'identité $A_m=-2^{2m+2}$ pour
  l'itinéraire de $1$.

Aucun rationnel testé ne viole $Q_m\le\log_2\max(|a|,b)$. Ce n'est pas une preuve
de plus : c'est la recherche de contre-exemple demandée avant d'accepter B7. Elle
n'en a pas produit.

## 6. Littérature

- **Lagarias (1985)** et **Bernstein–Lagarias (1996)** : la conjecture de périodicité
  est exactement « $\xi_w$ rationnel $\Rightarrow$ $w$ ultimement périodique ».
  B8 en est un cas, pour un mot de densité de $1$ égale à $1$. L'article de 1996
  n'a pas été relu dans ce dépôt. La revue `6080964566` indique que son §1,
  (1.5)–(1.6), confirme la convention de conjugaison et l'énoncé de la conjecture
  de périodicité : ce passage reste **non relu** ici. La formule du point fixe
  périodique utilisée pour les tests est élémentaire et vérifiée par l'orbite.
- **Monks–Yazinski (2004)**, *Discrete Math.* 275, théorème 2.7(b), lu sur le PDF
  d'auteur (`monks.scranton.edu`, fichier `AutoConjV13.pdf`) : une orbite rationnelle
  divergente a une densité inférieure de $1$ au moins $\ln2/\ln3$. La densité $1$
  de B8 satisfait cette borne. B8 n'en est pas un corollaire.
- **López–Stoll**, arXiv:2101.12747, théorème 1, preuve du §6 lue : ils affirment
  que cette densité inférieure vaut exactement $\ln2/\ln3$. Le dernier pas invoque
  (15) et (16) pour passer de l'irrationalité de la somme réelle $\Phi_{\mathbb R}$ à
  l'apériodicité de la somme 2-adique. Ces deux limites d'une même suite de
  rationnels ne sont pas le même objet (même distinction que X14). Témoin local,
  vérifié directement : $2^n/(1+2^n)$ tend vers $1$ dans $\mathbb R$ et vers $0$
  dans $\mathbb Q_2$. L'énoncé général de López–Stoll reste non utilisé.
- **De Jesús (2026)**, note de dérive, DOI `10.5281/zenodo.23108509` : seul le
  résumé a été lu. L'obstruction y est la complexité des facteurs face à une dérive
  normalisée. B7 compare la valuation 2-adique du reste à la taille de la somme
  partielle. Rien ici ne prétend être indépendant de ce préprint au-delà de la
  preuve écrite ; la preuve n'en dépend pas.
- **Bernstein (1994)** : la série de B1, déjà enregistrée. Pas de relecture du texte.

## 7. Ce que ce cycle ne montre pas

Aucune paire $(A,B)$ pour (H). Rien sur (C). Rien sur les runs de croissance
géométrique de raison $\le\log_23$, ni sur Fibonacci. Le mot de B8 n'est pas une
orbite d'entier positif : B8 parle du réalisateur 2-adique du mot, pas de Syracuse.

## 8. Mises à jour

- `proved.md` : B7, B8.
- `counterexamples.md` : X18. Correction ultérieure : X19 (revue `6080964566`).
- `hypotheses.md` : H4 prouvée ; H3 gagne le cas B8.
- `abandoned.md` : le critère de Liouville ne remplace pas VW sur les runs linéaires.
- `prior_art.md` : lectures de ce cycle.
- `agenda.md` : prochaine question, le seuil de croissance entre $\varphi$ et $\log_23$.

## 9. Reproduire

```sh
python3 research/checks/cycle003_liouville.py
```

Sortie attendue : six lignes `PASS` (8178 cycles purs ; témoins ; 3720 mots
ultimement périodiques ; 7712 orbites $a/b$, avec `cycle13_visite: 0` ; silence
triangulaire dès $m=6$ ; famille $2^k$ jusqu'à $k=8$).

## 10. Revue `6080964566`

Revue indépendante sur le SHA `0c90981ae61e15d4aa8505d1158ddb79039a22fd`
(26 novembre 2026). Elle confirme les preuves écrites de B7, B8 et X18. Ce n'est
pas une seconde preuve : les identités ont été revérifiées ici.

- La variante $y_t=T^t(\xi_w)+1$ redonne les mêmes relations : $2y_{t+1}=3y_t$ sur
  un bit $1$, $2y_{t+1}=y_t+1$ sur un bit $0$, puis
  $2^s y_s/3^{h_s}=y_0+\sum_{e_j<s}2^{e_j}/3^{o_j}$ avec $e_j=j+o_j-1$. La valuation
  du reste reste $m+1+o_{m+1}$. Rien à modifier dans §2, hors la précision sur $L$
  entier.
- Les comparaisons de B8 ($128/9>4507/729$, $32/81<1/2$, cas $k=1$) et la limite
  $Q_m\to-\infty$ de X18 sont inchangées. Dans le script, le commentaire disait
  « dès $m\ge4$ » ; l'assertion, et §4, disent que l'inégalité stricte commence à
  $m=6$. Le commentaire a été aligné.
- La troisième puce de §5 attribuait à tort au balayage borné la couverture des
  cycles de $3x+b$. C'est X19. Le script a été relancé : les six comptes annoncés
  sont inchangés, et le cycle de paramètre $13$ a $0$ visite.

B7, B8 et X18 restent **PROUVÉS** par le texte des §§2–4. La prochaine question
de l'agenda n'est pas abordée dans cette correction.

## 11. Revue `6081009622`

Revue indépendante sur le SHA `aeb693b5286fcb308484c91cdbeefcbe8ac576c2`
(26 novembre 2026). Elle confirme le certificat de X19 et la comparaison entière
de §2. Ce n'est pas une seconde preuve. Revérification locale, d'abord hors du
script, puis par relance du script. Aucun texte des §§1–9 n'est modifié.

- Huit transitions, avec arrêt imposé au huitième pas :
  $227\to347\to527\to797\to1202\to601\to908\to454\to227$. Chaque numérateur est
  premier à $13$. Le mot est $11110100$. L'orbite de $T$ sur $n/13$ et la formule
  du point fixe redonnent $227/13$. La correspondance avec la branche
  $n\mapsto n/2$ ou $(3n+13)/2$ se vérifie par substitution ; elle ne dépend pas
  d'une relecture de Bernstein–Lagarias.
- Balayage des $7712$ départs : $339\,789$ états examinés, plus les $7712$ états
  atteints juste après $18$ zéros ou $250$ pas. Aucune visite de $\{n/13\}$.
  Les $118\,882$ fenêtres de §5 satisfont $v_2(A_m)=m+1+o_{m+1}$, et le quotient
  $A_m/2^{m+1+o_{m+1}}$ est impair.
- Forme entière : $Q_m-L=\log_2\bigl(2^E/(3^{o_m}+P_m)\bigr)$ avec
  $E=m+1+o_{m+1}-L$. Pour $L\in\mathbb Z$ et $E<0$, multiplier par $2^{-E}>0$
  donne $1>(3^{o_m}+P_m)\,2^{-E}$. Le terme $j=1$ donne $P_m\ge2$, et
  $2^{-E}\ge2$, donc le membre de droite est un entier $\ge6$. Ainsi $Q_m>L$
  est faux. Le cas $m=1$, $o_1=0$, $E=-1$ atteint $6$. L'argument de B7 passe
  par $\log_2$ et n'utilise pas cette réduction.
- La revue note qu'une boucle non bornée dans le script ne tomberait pas si la
  transition cessait de ramener $227$. Le certificat ci-dessus est borné à huit
  pas, et l'assertion du script fixe déjà la liste des huit numérateurs. Le
  script n'est pas modifié.

X19 et la précision de §2 sont **confirmés** sur ce SHA. B7, B8 et X18 sont
inchangés. La prochaine question de l'agenda n'est pas abordée.
