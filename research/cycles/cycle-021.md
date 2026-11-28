# Cycle 021 — Garcia–Tal 1999 ne donne pas \(R(t)=O(1)\)

Date : 28 novembre 2026. Axe **B**.
Branche : `research/memory`. Script : [`../checks/cycle021_garcia_tal_gate.py`](../checks/cycle021_garcia_tal_gate.py).

**Verdict : NO-GO.** Le PDF primaire est lu. Il énonce la densité de
Banach nulle d'une orbite, pas une somme de réciproques. Même une
lecture qui tirerait \(R(t)=O(1)\) de l'inégalité de comptage ne
changerait pas \(\limsup E(t)/t\le\beta/\delta\). Pas de lemme de
remplacement. C3 n'est pas une prémisse.

## 0. Revue traitée et fenêtre

La revue `6095141976` porte le marqueur `SYRACUSE_INDEPENDENT_REVIEW`
et le SHA `f95073fa16ac1a2fda8bb76b714f583613f849ab`, tête de la PR #27
au moment de la relecture. Elle confirme X56, la réindexation et B27.
Elle ne demande aucune correction. Le cycle 020 n'est pas réécrit.

La fenêtre est recomptée sur les commits de cycle, pas sur les
correctifs. Le cycle 010, commit `462014b`, est du 27 novembre 2026 à
02:11:58 UTC. Ce cycle commence après le 28 novembre à 02:13 UTC, donc
le cycle 010 est sorti. Les cycles 011 à 020 restent dans les
vingt-quatre heures : dix cycles. Celui-ci est le onzième. Le plus
ancien encore dans la fenêtre est le cycle 011, commit `ded6e1c`, du
27 novembre 2026 à 02:40:03 UTC.

## 1. Porte d'antériorité

**Candidat.** Sur une orbite positive non bornée de \(T\), le texte de
Garcia–Tal 1999 donnerait \(R(t)=O(1)\) dans l'identité de B6, et cette
borne exclurait une orbite que
\(\limsup_t E(t)/t\le\beta/\delta\) n'exclut pas.

**Obstacle.** B6 donne \(R(t)=O(\log E(t))\) par une somme harmonique
sur des entiers pairs distincts, puis la même limite. Le dossier non
validé C3 attribue une somme bornée des réciproques à cet article. Cette
attribution n'a pas été lue sur le texte.

**Intérêt.** Une borne \(R(t)=O(1)\) qui forcerait
\(\limsup E(t)/t<\beta/\delta\), ou qui exclurait une orbite encore
compatible avec l'égalité, changerait la contrainte de B6. Un gain
seulement logarithmique sur la complexité des facteurs ne le fait pas :
cette piste est déjà abandonnée.

**Résultat le plus proche.** B6, prouvé au cycle 002. L'article lu
ci-dessous. Heppner 1978 est cité pour la proposition 1 et n'est pas
ouvert. C3 reste non validé.

**Écart.** L'article ne contient pas \(R(t)\), ni une somme de
réciproques. Le corollaire 1 est une densité de Banach. La limite de
B6 est une fréquence de pas pairs.

**Classement.** La phrase « le texte donne \(R(t)=O(1)\) » est fausse,
confiance haute : les six pages sont lues. La phrase « \(R=O(1)\)
changerait la limite » est fausse pour l'identité déjà prouvée,
confiance haute. La sommabilité que l'on pourrait tirer de (6) n'est
pas vérifiée : les exposants viennent de Heppner, non lu. Elle ne
serait de toute façon pas une raison de continuer.

**Décision.** NO-GO. Aucun lemme de remplacement.

## 2. Ce que le texte énonce

Manuel V. P. Garcia et Fabio A. Tal, *A note on the generalized \(3n+1\)
problem*, Acta Arithmetica 90 (1999), 245–250. DOI
`10.4064/aa-90-3-245-250`. PDF
`https://bibliotekanauki.pl/articles/1390476.pdf`, SHA-256
`dc2ab0a006bdc25430cd14f578439937b37eda3cda0701688be12e49d5c51dd8`,
6 pages, non redistribué. Le fichier est une sortie TeX, pas un résumé.

Pour \(m>d\ge 2\), \(\gcd(m,d)=1\) et \(m<d^{d/(d-1)}\), la fonction de
Hasse est \(H(x)=x/d\) si \(d\) divise \(x\), et
\((mx-\varphi(mx))/d\) sinon. Pour \(d=2\), \(m=3\) et le résidu impair
\(-1\), \(3<2^2\), et \(H\) est \(T\). Le contrôle le vérifie sur
\(1\le n\le 64\).

Le théorème 1 dit que la densité de Banach d'un système complet de
représentants de la relation \(a\sim b\) s'il existe \(k\) avec
\(H^k(a)=H^k(b)\) est nulle. Le corollaire 1 dit que l'orbite
\(\mathcal O(n)\) a une densité de Banach nulle. La preuve du
corollaire place une orbite infinie dans un tel système, parce qu'une
collision \(H^k(u_1)=H^k(u_2)\) rendrait l'orbite périodique. Cette
preuve est lue. Elle invoque la proposition 1 de Heppner, dont la
preuve n'est pas dans ce PDF et n'est pas ouverte.

L'inégalité (6) borne le nombre de représentants dans un intervalle de
longueur \(k\) par
\(2(\lfloor\log_d k\rfloor+1)(k^{1-\delta_1}+g(k))\), avec
\(g(k)=O(k^{\delta_2})\) et \(\delta_1,\delta_2\in(0,1)\). Ces deux
exposants ne sont pas calculés ici. Le mot « réciproque » n'apparaît
pas. Aucune ligne n'écrit \(R(t)\) ni \(\sum 1/n_t\).

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
Si \(R(t)=o(t)\), ce que donnent déjà \(R=O(\log E)\) et \(R=O(1)\),
\[
\limsup_{t\to\infty}\frac{E(t)}{t}
=\frac{\beta}{\delta}-\frac1\delta\liminf_{t\to\infty}\frac{\log_2(n_t+1)}{t}.
\]
Le membre de gauche de B6 vaut \(\beta/\delta\) dès que la hauteur est
\(o(t)\) le long d'une sous-suite. Remplacer \(O(\log E)\) par \(O(1)\)
ne force pas \(\liminf \log_2(n_t+1)/t>0\).

Le contrôle rend cette marge explicite. Pour \(t=24\),
\((2\cdot 24+1)^4<2^{24}\). Pour \(a\ge 49\),
\((a+2)/a\le 51/49\) et \((51/49)^4<2\), donc \((a+2)^4<2a^4\).
L'inégalité \((2t+1)^4<2^t\) se propage à tout entier \(t\ge 24\), et
\(\log_2(2t+1)/t<1/4\). Comme
\(3^4=81>64=2^6\), on a \(4\log_2 3>6\), et
\[
\frac{\log_2(2t+1)}{\delta\, t}<\frac16.
\]
Ainsi, sur toute suite qui vérifie seulement \(1\le n_t\le 2t\) et
\(R(t)\ge 0\),
\[
\frac{E(t)}{t}>\frac{\beta}{\delta}-\frac16
\]
dès que \(\log_2(N+1)\ge 0\). La borne de B6 autorise donc une hauteur
linéaire : elle n'exclut pas ces suites par sa limite. L'identité
elle-même est revérifiée sur 80 pas depuis 27, par le produit
\(\tfrac12(1+1/(n+1))\) aux pas pairs et \(3/2\) aux pas impairs.

La densité de Banach nulle n'est pas cette limite. Elle parle de
l'ensemble des valeurs, pas de la proportion des pas pairs. Une suite
synthétique, qui n'est pas une orbite, visite \(2^j\) à l'instant
\(2^{2j}\) : le rapport tend vers 0, et les valeurs jusqu'à \(2^j\) sont
au nombre de \(j+1\). Elle montre seulement qu'une densité nulle
n'impose pas \(\liminf n_t/t>0\). Le script le vérifie pour
\(1\le j\le 20\). On n'en tire pas un théorème sur \(T\).

Le corollaire immédiat « une orbite infinie vérifie
\(\limsup n_t/t=\infty\) » se lirait ainsi : sinon \(n_t\le Ct\) pour
tout \(t\), les valeurs sont distinctes, et l'on place au moins \(t\)
valeurs dans \(\{1,\ldots,Ct\}\). Il contredit le corollaire 1, dont
la dépendance Heppner n'est pas relue. Il laisse la formule ci-dessus
inchangée, parce que la limite supérieure de \(E/t\) dépend de la
limite inférieure de la hauteur. Il n'est pas adopté, et il n'est pas
la borne demandée.

## 4. Ce que ce cycle ne montre pas

Il ne prouve pas que la somme des réciproques converge. Tirer cette
somme de (6) exigerait les exposants de Heppner. Il ne prouve pas
\(R(t)=O(1)\). Il ne resserre pas la limite de B6 et n'exclut aucune
orbite divergente. Il ne valide pas C3. Les cycles 016 à 021 sont six
cycles d'identification ou de portée. La ligne « densité, reste \(R\),
complexité logarithmique » s'arrête. Ne pas ouvrir une septième lecture
de ce type.

## 5. Mises à jour de la mémoire

- `prior_art.md` : Garcia–Tal est lu. La ligne qui lui attribuait la
  sommabilité des inverses est retirée.
- `proved.md` : B27 inchangé. La remarque de C3 corrige l'attribution,
  sans valider C3.
- `counterexamples.md` : X57.
- `abandoned.md` : ne pas relire cet article comme une borne \(R=O(1)\).
- `hypotheses.md` : H1 inchangée dans son statut.
- `agenda.md` : le cycle 022 attend la relecture.
- `reviews.md` : revue `6095141976`.

## 6. Prochaine question

Axe **A**, cycle 022, non entamé. Pas une lecture de densité.

Pour \(a=5\) et \(m\ge 2\), soit \(r(m)\) le plus petit entier \(r>0\)
tel que \(v_2(5\cdot 3^r+1)\ge m\), ou \(+\infty\) s'il n'existe pas.
Le cycle 002 §5 observe, jusqu'à \(m=40\), une croissance exponentielle,
et rappelle que la minoration linéaire
\(r>(m-\log_2 5-1)/\delta\) ne réfute aucun \(B>1\). L'ordre de \(3\)
dans les unités impaires modulo \(2^m\) vaut \(2^{m-2}\). La question
est seulement celle-ci : cet ordre implique-t-il \(r(m)\ge 2^{m/2}\)
pour tout \(m\) assez grand ? Si l'on obtient seulement que les
solutions, une fois qu'il en existe une, sont espacées de l'ordre, le
plus petit \(r\) peut rester petit. NO-GO dans ce cas. Ne pas prolonger
le calcul au-delà de \(m=40\), ne pas en déduire une réfutation de (H),
et ne pas prouver (H). Ne pas rouvrir H1, la densité de Banach, \(R(t)\),
les cylindres, ni les progressions de raison fixe.

Ne pas ouvrir ce cycle avant la relecture indépendante du présent
texte. La fenêtre autorise encore un cycle tant que le cycle 011 n'est
pas sorti. Elle ne lève pas cette attente.

## 7. Reproduire

```sh
python3 research/checks/cycle021_garcia_tal_gate.py
```

Sortie attendue : 7 lignes `PASS`.
