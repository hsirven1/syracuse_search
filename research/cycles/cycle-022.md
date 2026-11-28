# Cycle 022 — L'égalité \(\liminf\log_2(n_t+1)/t=0\) est la finesse de (2.31), pas son énoncé

Date : 28 novembre 2026. Axe **B**.
Branche : `research/memory`. Script : [`../checks/cycle022_liminf_height.py`](../checks/cycle022_liminf_height.py).

**Verdict.** Pour une orbite positive non bornée de \(T\), l'identité de
B6 et la convergence de \(R\) donnent l'équivalence entre
\(\liminf\log_2(n_t+1)/t=0\), \(\limsup E(t)/t=\beta/\delta\) et
\(\liminf N^*(k)/k=(\log_2 3)^{-1}\) (B29). L'équation (2.31) de
Lagarias, lue sur le TeX, est l'inégalité \(\ge\). Elle redit
\(\liminf\log_2(n_t+1)/t\ge 0\), déjà dans B6. L'équation (2.32) borne
un sous-ensemble de l'orbite. Elle n'énonce pas le rapport
\(\log_2(n_t+1)/t\). Une suite injective de croissance exponentielle a
un compte \(O(\log x)\) et satisfait toute majoration \(O(\sqrt x)\)
(X64) : ce n'est pas une orbite. L'égalité elle-même reste ouverte.
La classification d'antériorité de cette égalité, hors des équations
lues, est PRIOR ART UNVERIFIED. Le PDF du Monthly 1985 et le chapitre
de Chamberland 2010 ne sont pas obtenus.

## 0. Revue traitée et fenêtre

La revue `6095268526` porte le marqueur `SYRACUSE_INDEPENDENT_REVIEW`
et le SHA `0c1b3eb260b40ff88d889e388dc35a770bae2cd9`, tête de la PR #27
au moment de cette relecture. Elle confirme B28, X59, X61, X62 et X63.
Elle ne demande aucune correction. Le cycle 021 n'est pas réécrit.

La fenêtre est recomptée sur les commits de cycle. Ce cycle commence
le 28 novembre 2026 après 03:01 UTC. Le cycle 012, commit `41cced5`,
est du 27 novembre 2026 à 02:59:54 UTC : il est sorti. Les cycles 013
à 021 restent dans les vingt-quatre heures : neuf cycles. Celui-ci est
le dixième. Le plus ancien encore dans la fenêtre est le cycle 013,
commit `9e26d12`, du 27 novembre 2026 à 20:16:39 UTC. Le correctif
`0c1b3eb` n'est pas un cycle.

## 1. Porte d'antériorité

**Candidat.** Pour toute orbite positive non bornée de \(T\),
\[
\liminf_{t\to\infty}\frac{\log_2(n_t+1)}{t}=0.
\]

**Obstacle.** B28 et l'identité de B6 écrivent
\[
\limsup_{t\to\infty}\frac{E(t)}{t}
=\frac{\beta}{\delta}-\frac1\delta\liminf_{t\to\infty}\frac{\log_2(n_t+1)}{t},
\]
avec \(\beta=\log_2(3/2)\) et \(\delta=\log_2 3\). Le membre de droite
vaut \(\beta/\delta\) exactement lorsque la limite inférieure est nulle,
et il est strictement plus petit lorsqu'elle est positive. Ce second cas
est une croissance exponentielle uniforme, \(n_t+1\ge 2^{(\alpha/2)t}\)
pour tout \(t\) assez grand.

**Intérêt.** Exclure ce cas éliminerait une classe de trajectoires
divergentes hypothétiques, sans prouver que toute orbite est bornée.
Ce n'est pas H1. H1 est l'autre bout,
\(\limsup\log_2(n_t+1)/t<\beta\), soit \(\liminf E(t)/t>0\).

**Résultat le plus proche.** B6, déjà prouvé : \(\limsup E(t)/t\le\beta/\delta\),
parce que \(\log_2(n_t+1)\ge 1\) et \(R(t)=o(t)\). Lagarias, équations
(2.30), (2.31) et (2.32), lues ci-dessous. Tao 2022 et Garcia–Tal 1999
parlent de densité, pas du rapport \(\log_2(n_t+1)/t\) d'une seule
orbite. Dubickas 2009, théorème 5, est la pente \(1/\beta\) de la
montée, l'enveloppe supérieure, pas cette limite inférieure.

**Écart.** (2.31) a le symbole \(\ge\), pas l'égalité. (2.32) borne le
nombre de points de l'orbite qui ne redescendent jamais sous eux-mêmes.
Le passage de \(\ge\) à \(=\) n'est pas écrit.

**Classement.** « (2.31) énonce déjà l'égalité » est faux, confiance
haute : le TeX de l'équation a été lu. « (2.32) énonce le rapport
logarithmique » est faux, confiance haute. « Aucun texte publié ne
prouve l'égalité » n'est pas établi : le PDF du Monthly 1985 et le
chapitre de Chamberland ne sont pas obtenus. Classification de
l'égalité : PRIOR ART UNVERIFIED, confiance moyenne. L'équivalence
B29, elle, est un corollaire de B6 et de B28.

**Décision.** L'égalité n'est pas un NO-GO au vu des équations lues.
L'expérience est la preuve de l'équivalence, la séparation avec (2.32),
et l'échec d'une preuve de l'égalité. Une suite qui n'est pas une orbite
ne tranche pas la question.

## 2. Ce que le texte énonce

Jeffrey C. Lagarias, texte Organics du 16 janvier 1996, section « Do
divergent trajectories exist? », page
`https://www.cecm.sfu.ca/organics/papers/lagarias/paper/html/node9.html`,
SHA-256 `3746a22f406796f517b18ff420947f67f2a1537cd5cd95e87707a0202eb7d4d5`,
5200 octets. Les formules sont les fichiers TeX du même article, non
redistribués. Le PDF du *Amer. Math. Monthly* 92 (1985), 3–23, n'a pas
été obtenu. Cette page Organics est celle qui porte les numéros (2.30),
(2.31) et (2.32). Ce n'est pas une relecture du fac-similé de 1985.

Les fichiers lus, avec leur empreinte SHA-256, sont :

- `img433.tex`, `cc29a8dba539325191427d3138a547aba6dd206405e6f9dd8eb6b0dabc81ccc9` : (2.30), \(\lim_k|T^{(k)}(n_0)|=\infty\).
- `img436.tex`, `5063c68f90818d3c9ba55c5723aded41adbb9b20660bc57eef16a4e67e8cacfa` : \(N^*(k)=|\{j\le k:T^{(j)}(n_0)\equiv 1\pmod 2\}|\).
- `img437.tex`, `5be4485c4350715d1a22d176050ac4448dba3b090621cdc6bde8867efb8f0b9c` : (2.31), \(\liminf N^*(k)/k\ge(\log_2 3)^{-1}\approx 0{,}63097\).
- `img444.tex`, `5dbd4bbb9a384aa7902daa8f4bc7ef8f0de464fa3d411d8e1bafadbe5fc033b0` : (2.32), \(|\{n\in U_D:n\le x\}|\le c_1 x^{1-\eta}\).
- `img284.tex`, `c7aba17daf10353dfdf5a1053597852da959d507d5a2657fd1be367a8ac06247` : \(\eta\approx 0{,}05004\ldots\), au théorème F. Cette valeur n'est pas recalculée.

La page dit que (2.30) implique (2.31), et que le théorème F donne
(2.32). Le théorème F, équation (2.21) du fichier `img283.tex`, borne
\(|\pi^*(x)-x|\) par \(c_1 x^{1-\eta}\), où \(\pi^*(x)\) compte les
\(n\le x\) de temps d'arrêt fini. La preuve de ce théorème n'est pas
reprise. \(U_D\) est l'ensemble des points de l'orbite divergente qui
vérifient \(T^{(k)}(n)>n\) pour tout \(k\ge 1\). La phrase qui suit
(2.32) dit que les éléments d'une trajectoire divergente ne peuvent pas
tendre vers l'infini « trop lentement ». Elle ne parle pas de
\(\log_2(n_t+1)/t\).

## 3. Équivalence (B29)

Sur toute orbite positive,
\[
\log_2(n_t+1)=\log_2(N+1)+\beta t-\delta E(t)+R(t),
\]
où \(E(t)\) est le nombre de pas pairs parmi les \(t\) pas, et où \(R(t)\)
somme \(\log_2(1+1/(n_s+1))\) sur ces pas pairs. C'est l'identité du
cycle 002. La relation \(\beta+1=\delta\) est \(2\cdot(3/2)=3\). Donc
\(\beta/\delta=1-1/\delta\) et \(1/\delta=(\log_2 3)^{-1}\).

Pour une orbite positive non bornée, B28 donne la convergence de \(R\),
donc \(R(t)/t\to 0\). Alors
\[
\liminf_{t\to\infty}\frac{\log_2(n_t+1)}{t}
=\beta-\delta\limsup_{t\to\infty}\frac{E(t)}{t}.
\]
La limite inférieure est nulle si et seulement si
\(\limsup E(t)/t=\beta/\delta\).

Soit \(O(t)=t-E(t)\) le nombre de pas impairs parmi les \(t\) premiers
états \(n_0,\ldots,n_{t-1}\). L'égalité précédente équivaut à
\(\liminf O(t)/t=1/\delta\). La définition lue est
\(N^*(k)=O(k+1)\), puisque les deux comptent les indices \(0\le j\le k\).
Donc
\[
\frac{N^*(k)}{k}=\frac{O(k+1)}{k+1}\cdot\frac{k+1}{k},
\]
et \(\liminf N^*(k)/k=\liminf O(t)/t\).

Ainsi, pour une orbite positive non bornée, les trois phrases suivantes
sont équivalentes :

1. \(\liminf\log_2(n_t+1)/t=0\) ;
2. \(\limsup E(t)/t=\beta/\delta\) ;
3. \(\liminf N^*(k)/k=(\log_2 3)^{-1}\).

L'inégalité (2.31) est le sens \(\ge\) de la troisième phrase. Par
l'identité, elle équivaut à \(\liminf\log_2(n_t+1)/t\ge 0\). Cette
inégalité est immédiate, car \(\log_2(n_t+1)\ge 1\), une fois
\(R(t)=o(t)\) acquis : c'est la borne \(\limsup E/t\le\beta/\delta\) de
B6. Le symbole imprimé n'est pas une égalité.

Le contrôle vérifie la forme multiplicative de l'identité sur l'orbite
de \(27\), l'alignement de \(N^*(k)\) avec le nombre d'impairs, et
\(T^{70}(27)=1\). Ensuite les termes
restent dans \(\{1,2\}\). Comme \(3^{10}<2^{16}\) et que cette queue
commence au rang \(70\), le rapport \(\log_2(n_t+1)/t\) y est au plus
\(1/10\). Cela ne concerne que les orbites qui atteignent \(1\).

## 4. (2.32) n'impose pas l'égalité (X64)

Soit \(\alpha>0\) et \((a_t)_{t\ge 1}\) une suite d'entiers positifs
distincts telle que \(a_t+1\ge 2^{\alpha t}\). Si \(a_t\le x\), alors
\(t\le\log_2(x+1)/\alpha\). Le nombre de termes \(\le x\) est donc au
plus \(1+\log_2(x+1)/\alpha\).

Pour \(x\ge 64\), soit \(k=\lfloor\log_2 x\rfloor\ge 6\). Alors
\(2^k\le x<2^{k+1}\), donc \(x+1\le 2^{k+1}\) et
\(\log_2(x+1)\le k+1\). L'inégalité \((k+1)^2\le 2^k\) vaut pour \(k=6\), car \(49\le 64\).
Elle se propage. D'abord \(2k+3\le 2^k\) pour \(k=6\), car \(15\le 64\),
et si cela vaut alors \(2(k+1)+3=(2k+3)+2\le 2^k+2\le 2^{k+1}\). Ensuite
\[
(k+2)^2=(k+1)^2+2k+3\le 2^k+2^k=2^{k+1}.
\]
Le contrôle vérifie \((k+1)^2\le 2^k\) pour \(6\le k\le 80\), et la
chaîne sur chaque entier \(64\le x\le 4000\). Donc
\(\log_2(x+1)\le\sqrt x\) pour ces \(x\), et le compte est \(O(\sqrt x)\).

La suite \(a_t=2^t-1\) est injective, \(\log_2(a_t+1)/t=1\), et pour
\(x=2^k\) les termes \(\le x\) sont exactement \(t=1,\ldots,k\). Son
compte est logarithmique. Elle satisfait une majoration
\(O(\sqrt x)\). Ce n'est pas une orbite : \(T(1)=2\), puis le cycle, et
\(T(3)=5\neq 7\).

(2.32) majore seulement \(U_D\), un sous-ensemble de l'ensemble des
valeurs. Le membre de droite imprimé est de l'ordre \(x^{1-\eta}\), avec
\(\eta\approx 0{,}05004\) non recalculé. Pour cette valeur imprimée,
\(1-\eta>1/2\), donc un compte \(O(\sqrt x)\) reste admissible. Même
sans ce chiffre, la page n'écrit pas que le rapport logarithmique
s'annule. La comparaison montre qu'une majoration de cette forme, y
compris appliquée à toute la suite, n'interdit pas une limite inférieure
strictement positive. Elle ne fabrique pas une orbite qui réaliserait
cette limite.

## 5. Ce que ce cycle ne montre pas

Il ne prouve pas \(\liminf\log_2(n_t+1)/t=0\). Il ne le réfute pas :
une réfutation serait une orbite positive non bornée de croissance
exponentielle uniforme, donc un contre-exemple à la conjecture. Aucune
recherche finie n'en produit. La suite du cycle 021 §3 et la suite
\(2^t-1\) ne sont pas des orbites. Le PDF de 1985 n'est pas lu. Le
chapitre de Chamberland, *A \(3x+1\) survey*, dans *The Ultimate
Challenge*, AMS, 2010, pp. 57–78, n'est pas obtenu. La valeur
\(0{,}05004\) n'est pas recalculée, et la preuve du théorème F n'est
pas reprise. H1 n'est pas entamé. Aucune orbite divergente n'est exclue.

## 6. Mises à jour de la mémoire

- `prior_art.md` : les équations (2.30)–(2.32) sont lues sur le TeX Organics. Le Monthly 1985 reste non obtenu.
- `proved.md` : B29, l'équivalence. L'égalité n'y figure pas.
- `counterexamples.md` : X64.
- `hypotheses.md` : H16, l'égalité, ouverte.
- `abandoned.md` : ne pas lire (2.31) comme une égalité, ni (2.32) comme une annulation du rapport.
- `agenda.md` : le cycle 023 attend la relecture.
- `reviews.md` : revue `6095268526`.

## 7. Prochaine question

Axe **C**, cycle 023, non entamé. Obtenir le chapitre de Chamberland
cité au §5 et lire seulement les paragraphes sur les trajectoires
divergentes et leur croissance. S'ils énoncent déjà
\(\liminf_k\log|T^{(k)}(n)|/k=0\) pour une trajectoire divergente,
reclasser l'égalité de H16 comme déjà connue. S'ils ne l'énoncent pas,
le statut reste PRIOR ART UNVERIFIED hors de (2.30)–(2.32). Ne pas
deviner un PDF absent. Ne pas rouvrir le nœud 9, le théorème F, H1, la
suite synthétique du cycle 021, ni B29 pour en refaire la preuve.

Ne pas ouvrir ce cycle avant la relecture indépendante du présent
texte. La fenêtre, au début du cycle 022, contient encore le cycle 013.
Elle ne lève pas cette attente.

## 8. Reproduire

```sh
python3 research/checks/cycle022_liminf_height.py
```

Sortie attendue : 5 lignes `PASS`.
