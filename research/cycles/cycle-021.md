# Cycle 021 — (6) implique la sommabilité ; \(R\) converge pour \(T\) ; la limite de B6 ne change pas

Date : 28 novembre 2026. Axe **B**.
Branche : `research/memory`. Script : [`../checks/cycle021_garcia_tal_gate.py`](../checks/cycle021_garcia_tal_gate.py).

**Verdict.** L'inégalité (6) de Garcia–Tal, lue sur le PDF, n'écrit pas
de somme de réciproques. Avec les seuls exposants \(\delta_1,\delta_2\in(0,1)\)
énoncés à la proposition 1, elle implique pourtant cette somme pour
chaque orbite infinie. Pour l'application classique \(T\), la somme et
la convergence de \(R(t)\) sont prouvées sans Heppner (B28). Même
borné, \(R\) laisse
\(\limsup E(t)/t=\beta/\delta-(1/\delta)\liminf\log_2(n_t+1)/t\).
Aucune minoration strictement positive de cette limite inférieure n'en
sort. La constante \(61344/65\) et le reste de C3 restent non validés.
NO-GO pour un resserrement de la limite. L'ordre de \(3\) n'implique
pas \(r(m)\ge 2^{m/2}\).

La première rédaction titrait que l'article ne donne pas \(R(t)=O(1)\).
Cette lecture confondait « non écrit » et « pas une conséquence ». Elle
est retirée (X58).

## 0. Revue traitée et fenêtre

La revue `6095141976` porte le marqueur `SYRACUSE_INDEPENDENT_REVIEW`
et le SHA `f95073fa16ac1a2fda8bb76b714f583613f849ab`, tête de la PR #27
au moment de cette relecture. Elle confirme X56, la réindexation et B27.
Elle ne demande aucune correction. Le cycle 020 n'est pas réécrit.

La revue `6095181058` porte le même marqueur et le SHA
`ede0b2d054bbf802eb4a1b6fdc2f05779304169d`, tête au moment de la
correction. Elle confirme les hypothèses classiques, le corollaire 1
et la formule de limite. Elle réfute le refus de la sommabilité et le
cas \(m=2\) de l'ordre. Le correctif est le §8. Le cycle 022 n'est pas
ouvert.

La fenêtre est recomptée sur les commits de cycle, pas sur les
correctifs. Le cycle 010, commit `462014b`, est du 27 novembre 2026 à
02:11:58 UTC. Ce cycle commence après le 28 novembre à 02:13 UTC, donc
le cycle 010 est sorti. Les cycles 011 à 020 restent dans les
vingt-quatre heures au début du cycle : dix cycles. Celui-ci est le
onzième. Le plus ancien encore dans la fenêtre est le cycle 011,
commit `ded6e1c`, du 27 novembre 2026 à 02:40:03 UTC. Le présent
correctif n'ajoute pas un douzième cycle.

## 1. Porte d'antériorité

**Candidat.** Sur une orbite positive non bornée de \(T\), le texte de
Garcia–Tal 1999 donnerait \(R(t)=O(1)\) dans l'identité de B6, et cette
borne exclurait une orbite que
\(\limsup_t E(t)/t\le\beta/\delta\) n'exclut pas.

**Obstacle.** B6 donne \(R(t)=O(\log E(t))\) par une somme harmonique
sur des entiers pairs distincts, puis la même limite. Le dossier non
validé C3 attribue une somme bornée des réciproques à cet article, avec
la constante \(61344/65\).

**Intérêt.** Une borne \(R(t)=O(1)\) qui forcerait
\(\limsup E(t)/t<\beta/\delta\), ou qui exclurait une orbite encore
compatible avec l'égalité, changerait la contrainte de B6. Un gain
seulement logarithmique sur la complexité des facteurs ne le fait pas.

**Résultat le plus proche.** B6, prouvé au cycle 002. L'inégalité (6),
lue ci-dessous. Heppner 1978 est cité pour la proposition 1 et n'est
pas ouvert. C3 reste non validé.

**Écart.** L'article n'écrit ni \(R(t)\), ni une somme de réciproques,
ni la constante \(61344/65\). Le corollaire 1 est une densité de Banach.
La conséquence « (6) et \(\delta_1,\delta_2\in(0,1)\) donnent la
sommabilité » n'est pas une phrase du texte : c'est B28 pour \(T\), et
le §8 pour l'énoncé général. Elle ne change pas la limite de B6.

**Classement.** « Le PDF écrit \(R(t)=O(1)\) » est faux, confiance
haute : les six pages sont lues. « (6) ne implique pas la sommabilité
sans les valeurs numériques des exposants » est faux (X58), confiance
haute. « \(R=O(1)\) change la limite » est faux pour l'identité déjà
prouvée, confiance haute. La constante de C3 reste non vérifiée.

**Décision.** NO-GO pour un lemme qui resserrerait
\(\limsup E(t)/t\). La sommabilité elle-même est prouvée au §8, parce
que la première rédaction la niait.

## 2. Ce que le texte énonce

Manuel V. P. Garcia et Fabio A. Tal, *A note on the generalized \(3n+1\)
problem*, Acta Arithmetica 90 (1999), 245–250. DOI
`10.4064/aa-90-3-245-250`. PDF
`https://matwbn.icm.edu.pl/ksiazki/aa/aa90/aa9033.pdf`, SHA-256
`dc2ab0a006bdc25430cd14f578439937b37eda3cda0701688be12e49d5c51dd8`,
6 pages, non redistribué. Le même fichier avait été lu sous l'URL
`https://bibliotekanauki.pl/articles/1390476.pdf` : l'empreinte coïncide.
Le fichier est une sortie TeX, pas un résumé.

Pour \(m>d\ge 2\), \(\gcd(m,d)=1\) et \(m<d^{d/(d-1)}\), la fonction de
Hasse est \(H(x)=x/d\) si \(d\) divise \(x\), et
\((mx-\varphi(mx))/d\) sinon. Pour \(d=2\), \(m=3\) et le résidu impair
\(-1\), \(3<2^2\), et \(H\) est \(T\). Le contrôle le vérifie sur
\(1\le n\le 64\).

Le théorème 1 dit que la densité de Banach d'un système complet de
représentants de la relation \(a\sim b\) s'il existe \(k\) avec
\(H^k(a)=H^k(b)\) est nulle. Le corollaire 1 dit que l'orbite
\(\mathcal O(n)\) a une densité de Banach nulle. La preuve du
corollaire place une orbite infinie dans un tel système : une collision
\(H^k(u_1)=H^k(u_2)\) rendrait l'orbite périodique. Cette preuve est
lue. Elle invoque la proposition 1 de Heppner, dont la preuve n'est
pas dans ce PDF et n'est pas ouverte. L'énoncé lu de cette proposition
donne \(\delta_1,\delta_2\in(0,1)\), sans en calculer les valeurs.

L'inégalité (6) borne le nombre de représentants dans un intervalle de
longueur \(k\) par
\(2(\lfloor\log_d k\rfloor+1)(k^{1-\delta_1}+g(k))\), avec
\(g(k)=O(k^{\delta_2})\). Le mot « réciproque » n'apparaît pas. Aucune
ligne n'écrit \(R(t)\), ni \(\sum 1/n_t\), ni \(61344/65\).

## 3. La limite de B6 ne bouge pas

L'identité du cycle 002 est
\[
\log_2(n_t+1)=\log_2(N+1)+\beta t-\delta E(t)+R(t),
\]
avec \(\beta=\log_2(3/2)\) et \(\delta=\log_2 3\). Donc
\[
\frac{E(t)}{t}=\frac{\beta}{\delta}
+\frac{\log_2(N+1)+R(t)-\log_2(n_t+1)}{\delta\, t}.
\]
Si \(R(t)=o(t)\), ce que donnent déjà \(R=O(\log E)\) et la convergence
prouvée au §8,
\[
\limsup_{t\to\infty}\frac{E(t)}{t}
=\frac{\beta}{\delta}-\frac1\delta\liminf_{t\to\infty}\frac{\log_2(n_t+1)}{t}.
\]
Remplacer \(O(\log E)\) par une limite finie réduit l'erreur à \(O(1/t)\).
Cela ne force pas \(\liminf \log_2(n_t+1)/t>0\).

Le contrôle rend la marge explicite sous des hypothèses qu'il faut
écrire. On suppose l'identité, \(R(t)\ge 0\), \(\log_2(N+1)\ge 0\),
\(1\le n_t\le 2t\) et \(t\ge 24\). Pour \(t=24\),
\((2\cdot 24+1)^4<2^{24}\). Pour \(a\ge 49\),
\((a+2)/a\le 51/49\) et \((51/49)^4<2\), donc \((a+2)^4<2a^4\).
L'inégalité \((2t+1)^4<2^t\) se propage à tout entier \(t\ge 24\), et
\(\log_2(2t+1)/t<1/4\). Comme \(3^4=81>64=2^6\),
\[
\frac{\log_2(2t+1)}{\delta\, t}<\frac16,
\]
donc
\[
\frac{E(t)}{t}>\frac{\beta}{\delta}-\frac16.
\]
Sans borne inférieure sur \(t\), la phrase est fausse. Pour \(t=20\),
\(41^6>3^{20}\), donc le même majorant \(\log_2(2t+1)\) ne reste pas
sous \(1/6\). L'identité elle-même est revérifiée pour
\(1\le N\le 64\) et \(1\le t\le 64\), par le produit
\(\tfrac12(1+1/(n+1))\) aux pas pairs et \(3/2\) aux pas impairs.

La densité de Banach nulle n'est pas cette limite. Elle parle de
l'ensemble des valeurs, pas de la proportion des pas pairs. Pour \(T\),
B28 donne déjà \(\limsup n_t/t=\infty\) sur une orbite non bornée : une
borne \(n_t\le Ct\) placerait au moins \(t\) valeurs distinctes dans
\(\{1,\ldots,\lfloor Ct\rfloor\}\), et contredirait \(A(x)=O(x^\theta)\)
pour \(\theta<1\). Cette déduction n'utilise pas Heppner. Elle ne force
toujours pas \(\liminf\log_2(n_t+1)/t>0\).

Deux suites, qui ne sont pas des orbites, séparent ces lectures.

- Aux temps \(2^{3j}\), \(j\ge 1\), poser \(n_t=2^{2j}\). Le rapport
  vaut \(2^{-j}\). Les autres temps reçoivent, dans l'ordre,
  \(2^1,2^3,2^5,\ldots\). Les valeurs sont des puissances de \(2\)
  distinctes. Le rapport prescrit tend vers \(0\), donc
  \(\liminf n_t/t=0\). Au temps \(1\), la valeur est \(2\) et le
  rapport vaut \(2\) : la suite complète ne tend pas vers \(0\). La
  formule \(n_{4^j}=2^{2j+1}\) a, elle, le rapport \(2\), pas
  \(2^{1-j}\) (X59). Un intervalle de \(n\) entiers consécutifs
  contient au plus \(\lfloor\log_2 n\rfloor+1\) puissances de \(2\) :
  \(r\) termes \(2^u,\ldots,2^{u+r-1}\) vérifient
  \(2^u(2^{r-1}-1)<n\), donc \(2^{r-1}\le n\). La densité de Banach
  est nulle. Le script le vérifie pour \(1\le n\le 32\).
- \(m_t=\lfloor(3/2)^t\rfloor\) vérifie
  \(0<\log_2(m_t+1)-\beta t<1\), parce que
  \(3^t<2^t(m_t+1)<2\cdot 3^t\). Donc
  \(\log_2(m_t+1)/t\to\beta\). Les valeurs jusqu'à \(x\) n'occupent
  que \(O(\log x)\) temps. Ce n'est pas une orbite :
  \(T(2)=1\neq 3\). Le comptage de B28 autorise donc la croissance
  maximale \(\beta\), et il autorise aussi un liminf nul. Il ne
  tranche pas entre les deux.

## 4. Ce que ce cycle ne montre pas

Il prouve la sommabilité et \(R(t)=O(1)\) pour toute orbite positive
non bornée de \(T\) (B28). Il ne calcule pas \(61344/65\), ni aucune
autre constante numérique uniforme. Il ne resserre pas la limite de
B6 et n'exclut aucune orbite divergente. Il ne valide pas C3. Il ne
démontre pas la proposition 1 de Heppner. Il ne prouve pas
\(\liminf\log_2(n_t+1)/t>0\), ni l'inégalité stricte opposée. Les
cycles 016 à 021 sont six cycles d'identification ou de portée. La
ligne « densité, reste \(R\), complexité logarithmique » s'arrête :
B28 est la correction de la phrase qui niait la somme, pas une
septième lecture.

## 5. Mises à jour de la mémoire

- `prior_art.md` : Garcia–Tal est lu. (6) implique la sommabilité ;
  le PDF ne l'écrit pas.
- `proved.md` : B28. La remarque de C3 sépare la conséquence de (6),
  la preuve autonome pour \(T\), et la constante non validée.
- `counterexamples.md` : X57 rétréci ; X58, X59, X60.
- `abandoned.md` : ne pas rouvrir cette lecture pour resserrer la
  limite, ni pour calculer \(61344/65\).
- `hypotheses.md` : H1 inchangée dans son statut. B28 ne la donne pas.
- `agenda.md` : le cycle 022 attend la relecture de ce correctif.
- `reviews.md` : revues `6095141976` et `6095181058`.

## 6. Prochaine question

Axe **B**, cycle 022, non entamé. Pas une nouvelle lecture de densité,
et pas la question d'ordre fermée par X60.

Pour une orbite positive non bornée de \(T\), B28 et l'identité de B6
donnent
\[
\limsup_{t\to\infty}\frac{E(t)}{t}
=\frac{\beta}{\delta}-\frac1\delta\liminf_{t\to\infty}\frac{\log_2(n_t+1)}{t}.
\]
La question est la porte : cette limite inférieure est-elle nulle pour
toute orbite positive non bornée ? Si un théorème publié le donne
déjà, ou s'il ne s'agit que de la suite synthétique du §3, NO-GO. Cette
suite n'est pas une orbite. La question n'est pas H1 : H1 est
\(\liminf E(t)/t>0\), soit
\(\limsup\log_2(n_t+1)/t<\beta\). Ne pas attaquer H1 comme petit
lemme. Ne pas rouvrir Garcia–Tal, Heppner, la constante de C3, l'ordre
de \(3\), ni les cylindres.

Ne pas ouvrir ce cycle avant la relecture indépendante du présent
correctif. La fenêtre, au début du cycle 021, contient encore le cycle
011. Elle ne lève pas cette attente.

## 7. Reproduire

```sh
python3 research/checks/cycle021_garcia_tal_gate.py
```

Sortie attendue : 13 lignes `PASS`.

## 8. Correction après la revue `6095181058`

### 8.1. Sommabilité pour \(T\) (B28)

**Énoncé.** Soit \(T(n)=n/2\) si \(n\) est pair, et \((3n+1)/2\) si \(n\)
est impair. Pour toute orbite positive non bornée, les valeurs sont
distinctes, \(\sum_{n\in\mathcal O}1/n<\infty\), et le reste
\[
R(t)=\sum_{\substack{s<t\\ n_s\text{ pair}}}\log_2\bigl(1+1/(n_s+1)\bigr)
\]
converge vers une limite finie. La majoration est uniforme en l'orbite.
Ce n'est pas la constante \(61344/65\).

**Mots.** Si \(1\le n<m\le 2^k\) ont les mêmes \(k\) premières parités,
alors \(v_2(T^j(m)-T^j(n))=v_2(m-n)-j\) tant que l'écart est non nul :
un pas pair le divise par \(2\), un pas impair le multiplie par \(3/2\).
L'écart ne s'annule pas, sinon les deux départs coïncideraient, chaque
pas de parité fixée étant injectif. Or \(|m-n|<2^k\), donc
\(v_2(m-n)\le k-1\), et la valuation après \(k\) pas serait négative.
Les \(2^k\) entiers de \(1\) à \(2^k\) portent donc des mots distincts,
et tous les mots apparaissent. Le script le vérifie pour \(1\le k\le 12\).

**Images.** Pour \(k\ge 0\), si \(s\) est le nombre de pas impairs parmi
les \(k\) premiers, \(T^k(n)<3^s(n/2^k+1)\). C'est vrai au rang \(0\).
Si \(y=T^k(n)\) est pair, \(y/2\) hérite de la même puissance de \(3\) et
la parenthèse \(n/2^k+1\) est remplacée par sa moitié, qui est plus
petite que \(n/2^{k+1}+1\). Si \(y\) est impair,
\((3y+1)/2\) gagne un facteur \(3\), et
\(3^{s+1}(n/2^{k+1}+1/2)+1/2\) reste strictement sous
\(3^{s+1}(n/2^{k+1}+1)\). Pour \(n\le 2^k\), \(T^k(n)<2\cdot 3^s\).
Le script le vérifie sur les mêmes mots.

**Comptage.** Soit \(\mathcal O\) une orbite positive non bornée. Elle
n'est pas périodique, donc \(T^k\) y est injective. Parmi les points de
\(\mathcal O\cap\{1,\ldots,2^k\}\) qui ont au plus \(\lfloor 3k/5\rfloor\)
pas impairs dans les \(k\) suivants, les images sont des entiers
distincts strictement inférieurs à \(2\cdot 3^{\lfloor 3k/5\rfloor}\).
Ils sont donc au plus \(2\cdot 3^{\lfloor 3k/5\rfloor}-1\). Les autres
ont un mot à plus de \(3k/5\) bits \(1\). Pour \(z=3/2\),
\[
\sum_{s>3k/5}\binom{k}{s}
\le z^{-3k/5}(1+z)^k
=\frac{(5/2)^k}{(3/2)^{3k/5}},
\]
car \(z^{s-3k/5}>1\) sur cette plage. D'où
\[
A(2^k)<2\cdot 3^{3k/5}+\frac{(5/2)^k}{(3/2)^{3k/5}}.
\]
Les bases \(3^{3/5}\) et \((5/2)/(3/2)^{3/5}\) sont strictement
inférieures à \(2\), puisque \(27<32\) et \(3125<3456\). Si \(\lambda\)
est leur maximum,
\(A(2^k)<3\lambda^k\). Dans le bloc \([2^j,2^{j+1})\),
\[
\sum\frac1n\le\frac{A(2^{j+1})}{2^j}<3\lambda\Bigl(\frac\lambda2\Bigr)^j.
\]
La série géométrique converge. La somme des réciproques de l'orbite est
donc finie, et la majoration ne dépend pas de l'orbite.

**Reste.** Pour \(x>0\), \(\ln(1+x)\le x\), donc
\(\log_2(1+1/(n+1))\le 1/((n+1)\ln 2)\). Sur une orbite non bornée, les
états pairs sont distincts et au moins \(2\). Comme \(1/(n+1)\le 1/n\),
la série des accroissements de \(R\) est majorée par \(1/\ln 2\) fois
la somme des réciproques, déjà convergente. Donc \(R(t)\) croît vers
une limite finie.

### 8.2. Conséquence de (6), sans valeur numérique

La proposition 1, lue, affirme l'existence de
\(\delta_1,\delta_2\in(0,1)\). L'inégalité (6) s'applique à tout
système complet de représentants. La preuve du corollaire 1, lue,
inclut une orbite infinie dans un tel système. Pour l'intervalle
\(\{1,\ldots,x\}\),
\[
A(x)=O\bigl(x^{1-\eta}\log x\bigr),
\qquad
\eta=\min(\delta_1,1-\delta_2)>0,
\]
parce que \(x^{1-\delta_1}\) et \(x^{\delta_2}\) sont tous deux
\(O(x^{1-\eta})\), et que \(\lfloor\log_d x\rfloor+1=O(\log x)\).
Le bloc \([2^j,2^{j+1})\) contribue au plus
\(O((j+1)2^{-j\eta})\). Ces termes sont sommables. Les valeurs
numériques de \(\delta_1\) et \(\delta_2\) ne sont pas utilisées. La
preuve de Heppner n'est pas lue : cette déduction repose sur l'énoncé
imprimé de (6), pas sur une seconde preuve de la proposition 1. Elle
ne produit pas \(61344/65\).

Pour \(T\), le §8.1 rend la même conclusion indépendante de cet énoncé.

### 8.3. Ordre de \(3\)

Le cycle 002 §2 prouve que l'ordre de \(3\) modulo \(2^m\) vaut
\(2^{m-2}\) pour \(m\ge 3\). Pour \(m=2\), \(3^1\equiv 3\pmod 4\) et
\(3^2\equiv 1\pmod 4\), donc l'ordre vaut \(2\), pas \(2^{0}=1\) (X60).

Cet ordre est la période exacte des solutions de \(3^r\equiv c\pmod{2^m}\)
lorsqu'une solution existe. Il ne minore pas le plus petit \(r>0\).
L'équation \(3^r\equiv 3\pmod{2^m}\) a pour plus petite solution \(r=1\),
et \(1<2^{m/2}\) pour tout \(m\ge 3\), puisque \(2^m>1\). Le même ordre
vaut pour \(c=-5^{-1}\). Il n'implique donc pas
\(r(m)\ge 2^{m/2}\). C'est le cas NO-GO déjà écrit : on n'obtient que
l'espacement. Le calcul au-delà de \(m=40\) n'est pas repris, et (H)
n'est pas réfutée.
