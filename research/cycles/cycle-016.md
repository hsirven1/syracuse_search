# Cycle 016 — \(P(2)\) est la conjecture 4.13 de Yolcu–Aaronson–Heule

Date : 27 novembre 2026. Axe **B**.
Branche : `research/memory`. Script : [`../checks/cycle016_run_bound.py`](../checks/cycle016_run_bound.py).

**Verdict.** \(P(2)\) est exactement la conjecture 4.13 de
Yolcu, Aaronson et Heule, arXiv:2105.14697v3 : toute trajectoire
non convergente de \(C\) rencontre le résidu \(7\pmod 8\). Cette
conjecture est laissée ouverte, avec une récompense annoncée de
500 dollars. Steiner (1977), lu à travers Simons–de Weger, et
Simons–de Weger eux-mêmes ne la contiennent pas. Le texte de 1977
n'a pas été obtenu. Aucune preuve de \(P(2)\) n'est tentée. Ce
n'est pas une preuve de Syracuse.

## 0. Revue traitée, fenêtre

La revue `6093952309` porte le marqueur `SYRACUSE_INDEPENDENT_REVIEW`
et le SHA `db5009a9c5b95b172b6bb43f0fa77d46a0f9c0d4`, tête de la PR #27
au début de ce cycle. Elle confirme X40 et la compatibilité avec B21.
Aucune correction de ce correctif. Le paragraphe marqué non vérifié
porte sur \(P(2)\), qui est la question de ce cycle, pas une objection
au correctif.

La fenêtre de douze cycles était fermée jusqu'au 27 novembre 2026 à
23:17 UTC : le commit `8bc44f7` du cycle 004 est du 26 novembre à
23:16:52 UTC. Ce cycle est enregistré après cet instant.

## 1. Porte d'antériorité

**Candidat 1.** \(P(2)\) : toute orbite positive de
\[
T(n)=\begin{cases}n/2&n\text{ pair},\\(3n+1)/2&n\text{ impair}\end{cases}
\]
dont chaque run impair a une longueur au plus \(2\) atteint \(1\).

**Obstacle.** Le cas \(R=1\) est élémentaire. Le premier cas ouvert
annoncé par l'agenda est \(R=2\).

**Intérêt.** Une réponse positive exclurait toute orbite divergente,
et tout cycle non trivial, dont les runs impairs sont bornés par \(2\).

**Résultat le plus proche.** Yolcu, Aaronson et Heule,
arXiv:2105.14697v3 (31 décembre 2022), conjecture 4.13, page 34 du PDF :
toute trajectoire non convergente de \(C\) contient un terme
\(n\equiv 7\pmod 8\). Le théorème 4.10, même page, règle les résidus
\(2,3,4,6\pmod 8\). Les résidus \(0,1,5,7\) restent ouverts. La
conjecture 4.14, qui demande seulement \(5\) ou \(7\), est aussi
ouverte.

**Écart.** Aucun, une fois les applications identifiées (§2). L'énoncé
demandé est cette conjecture, pas un lemme plus faible.

**Classement.** DÉJÀ CONNU comme conjecture ouverte. Confiance haute
sur le texte lu (PDF arXiv v3, pas la pagination de la revue). La
preuve publiée du théorème 4.10 n'a pas été refaite.

**Décision.** NO-GO pour une preuve de \(P(2)\).

**Candidat 2.** Pour l'application accélérée
\(U(n)=(3n+1)/2^{v_2(3n+1)}\), \(\tau(n)=1\) caractérise les impairs
\(n>1\) congrus à \(1\) ou \(5\pmod 8\).

**Obstacle.** Savoir si une contraction en un pas sort de la classe
modulo \(8\).

**Intérêt.** Une famille hors de ces deux résidus, avec \(\tau=1\),
serait un mécanisme de descente qui n'est pas \(P(2)\).

**Résultat le plus proche.** Le graphe modulo \(8\) de la même source,
figure 1 et proposition 4.7 : les arêtes en gras sont les transitions
qui augmentent. Le cas \(R=1\) du cycle 015 est la contraction
\(n\equiv 1\pmod 4\).

**Écart.** Aucun. Si \(n\equiv 1\) ou \(5\pmod 8\) et \(n>1\), alors
\(v_2(3n+1)\ge 2\), donc \(U(n)\le(3n+1)/4<n\). Si \(n\equiv 3\) ou
\(7\pmod 8\), alors \(v_2(3n+1)=1\) et \(U(n)=(3n+1)/2>n\). Pour
\(n=1\), \(U(1)=1\).

**Classement.** COROLLAIRE DIRECT du calcul modulo \(8\). Confiance
haute. Ce n'est pas une contrainte nouvelle.

**Décision.** NO-GO.

**Candidat 3.** La conjecture 4.14 du même PDF : toute trajectoire
non convergente de \(C\) rencontre \(5\) ou \(7\pmod 8\).

**Obstacle.** C'est l'affaiblissement que les auteurs disent encore
ouvert, après avoir réglé les paires \(\{1,5\}\) et \(\{1,7\}\).

**Intérêt.** Aucun pour une preuve directe de \(P(2)\). La conjecture
4.14 ne couvre directement que les orbites qui évitent les deux
résidus. Éviter \(\{5,7\}\) implique d'éviter \(7\), et l'inclusion
est stricte sur les orbites positives :
\(5\to 8\to 4\to 2\to 1\) rencontre \(5\pmod 8\) et n'atteint jamais
\(7\pmod 8\) (X42). Cette orbite converge, donc elle sépare les
hypothèses, pas les valeurs de vérité des deux conjectures.
\(P(2)\) implique 4.14 par inclusion. L'implication inverse ne suit
pas de cette inclusion. Pour déduire \(P(2)\) de 4.14, il resterait
à traiter les orbites qui évitent \(7\) et rencontrent \(5\). Après
la première visite de \(5\pmod 8\), cette question se réduit à la
queue issue de ce terme (§9). Cette réduction ne démontre pas que
4.14 n'entraîne pas \(P(2)\).

**Résultat le plus proche.** La conjecture 4.14 elle-même, et le
cycle \(-5\to-7\to-10\to-5\), qui évite ces deux résidus (§3).

**Écart.** Aucun énoncé intermédiaire n'est proposé. La réduction
du §9 laisse la queue ouverte.

**Classement.** DÉJÀ CONNU comme conjecture ouverte. Elle suit de
la conjecture 4.13 par inclusion des hypothèses. L'inverse n'est
pas établi. Confiance haute sur le texte. Prouver 4.14 laisserait
ouvertes les queues qui commencent par \(5\pmod 8\) et évitent
\(7\). Pas de stratégie qui n'essaie pas de résoudre l'une de ces
deux conjectures.

**Décision.** NO-GO. Trois candidats ont été examinés. Une seule
comparaison est écrite : l'équivalence du candidat 1.

## 2. Équivalence

Le run impair issu d'un impair \(m\) a longueur \(r=v_2(m+1)\) (cycle 015,
§10). Pour \(0\le i\le r\),
\[
v_2(T^i(m)+1)=r-i.
\]
Pour \(0\le i<r\), \(T^i(m)\) est impair, donc \(v_2(T^i(m))=0\). La
quantité \(r-i\) n'est pas la valuation du terme. Cette longueur est
au moins \(3\) si et seulement si \(m\equiv 7\pmod 8\). Si un terme
impair du run vaut \(7\pmod 8\), et si c'est \(T^i(m)\), alors
\(r-i\ge 3\) : à partir de ce terme, en le comptant, il reste au moins
trois impairs. Inversement, un run de longueur au moins \(3\) commence
par un tel terme. Ainsi \(P(2)\) dit que toute orbite positive de \(T\)
qui ne rencontre pas le résidu \(7\pmod 8\) atteint \(1\).

L'application du PDF est
\[
C(n)=\begin{cases}n/2&n\text{ pair},\\3n+1&n\text{ impair.}\end{cases}
\]
Depuis un impair \(m\), \(C\) visite \(3m+1\), puis les mêmes quotients
par \(2\) que \(T\). Pour \(m\) impair, \(3m+1\) vaut \(0,2,4\) ou
\(6\pmod 8\), jamais \(7\). Les termes pairs initiaux, avant le premier
impair, sont les mêmes pour \(C\) et pour \(T\). Les deux orbites
rencontrent donc \(7\pmod 8\) ensemble. Le point \(1\) est impair, donc
l'une atteint \(1\) si et seulement si l'autre l'atteint.

La conjecture 4.13 dit que toute trajectoire de \(C\) qui n'atteint pas
\(1\) rencontre \(7\pmod 8\). Sa contraposée est \(P(2)\).

## 3. Ce que Steiner et Simons–de Weger ne donnent pas

Le PDF de Steiner, *A theorem on the Syracuse problem*, Congressus
Numerantium 20 (1978), 553–559, n'a pas été obtenu. Le fichier
`https://www.di.ens.fr/~stern/data/St77.pdf` a été téléchargé : 15
pages, métadonnées sans ce titre, texte non identifiable comme cet
article. Il n'est pas une source.

Simons et de Weger, version 1.44 du 31 août 2010, PDF de 17 pages,
SHA-256
`974d861520e524c550e719fde5ebf5cb73234ed9fc4f5002befeee88256e99dd`,
disent que la version 1.3 est parue dans *Acta Arithmetica* 117
(2005), 51–70. Le PDF de 2005 n'a pas été ouvert. Dans la version lue :

- un \(m\)-cycle est une orbite périodique à \(m\) minima locaux,
  chacun suivi d'un bloc impair croissant puis d'un bloc pair
  décroissant (§1.1–1.2) ;
- le §1.2 restreint l'étude aux suites périodiques et écrit que les
  suites non bornées ne sont pas considérées ;
- le seul \(1\)-cycle positif est \(\{1,2\}\), attribué à Steiner
  (1977), §1.4 ;
- la version lue exclut les \(m\)-cycles non triviaux pour
  \(1\le m\le 75\).

Leur entier \(m\) est le nombre de blocs, pas la longueur maximale
d'un bloc. Une orbite qui évite \(7\pmod 8\) peut avoir autant de
blocs de longueur \(1\) ou \(2\) qu'on veut, et elle peut ne pas être
périodique. Le théorème lu n'implique pas \(P(2)\). La borne \(m\le 68\)
déjà notée pour l'article de 2005 n'a pas été revérifiée sur ce PDF.

Le cycle de \(T\) sur les négatifs
\[
-5\to -7\to -10\to -5
\]
a les résidus \(3,1,6\pmod 8\). Il évite \(7\) et n'atteint pas \(1\).
Toute démonstration qui vaudrait pour tous les entiers de ces résidus,
sans utiliser la positivité, est donc fausse. Cela ne réfute pas
\(P(2)\) sur les positifs. Le fragment \(11\to 17\to 26\to 13\) reste
dans les résidus permis et \(13>11\) : il n'y a pas de descente stricte
de l'impair en un ou deux pas sur toute la classe. Ce n'est pas un
contre-exemple à \(P(2)\), puisque \(13\) redescend ensuite.

La note rStation du 3 novembre 2026, paper 32, décrit une obstruction
plus forte pour les certificats de module fixé. Nashida, cité par
cette note, n'a pas été ouvert. Cette obstruction n'est pas une
prémisse de l'équivalence.

## 4. Statut

L'équivalence du §2 est prouvée (B22). \(P(2)\) reste la conjecture
4.13, non résolue. Le théorème 4.10 n'est pas reproduit. Aucune orbite
positive divergente n'est exclue. Le script contrôle les quatre
résidus de \(3m+1\), le cycle négatif, la montée de \(11\), l'accord
de \(C\) et de \(T\) jusqu'à \(4000\), et le signe de \(U(n)-n\) selon
le résidu modulo \(8\). Le §8 y ajoute l'orbite de \(5\) et la
valuation de \(T^i(m)+1\). Ces contrôles ne remplacent pas le §2.

## 5. Mises à jour de la mémoire

- `proved.md` : B22, équivalence seulement.
- `hypotheses.md` : H12, conjecture ouverte identifiée.
- `counterexamples.md` : X41, le cycle négatif et la montée de \(11\).
- `prior_art.md` : Yolcu–Aaronson–Heule v3, et la lecture partielle
  de Simons–de Weger.
- `abandoned.md` : ne pas reprendre \(P(2)\) comme lemme frais.
- `agenda.md` : question suivante, axe C.
- `reviews.md` : revue `6093952309`.

## 6. Prochaine question

Axe **C**. Ne pas rouvrir \(P(2)\), les conjectures 4.11 à 4.14, le
texte de Steiner, ni les \(m\)-cycles.

Korec (1994) est cité comme source secondaire, via Tao : une densité
naturelle de départs dont le minimum passe sous \(n^\theta\), avec
\(\theta>\log 3/\log 4\). Lire l'énoncé primaire, ou, s'il n'est pas
obtenu, le passage exact où Tao l'énonce. Décider seulement si cette
borne force une classe de congruence entière à atteindre \(1\). Si
elle ne donne qu'un comptage, la classer plus faible que B20 et X34,
et ne pas la redémontrer.

Le cycle 016 est le douzième de la fenêtre dont le plus ancien est le
cycle 005. Le premier commit de ce cycle est `ebba330`, du 27 novembre
2026 à 00:03:27 UTC. Ne pas ouvrir le cycle 017 avant une relecture
indépendante du correctif de la revue `6094246430`, ni avant le
28 novembre 2026 à 00:04 UTC.

## 7. Reproduire

```sh
python3 research/checks/cycle016_run_bound.py
```

Sortie attendue : 8 lignes `PASS`.

## 8. Revue `6094223904`

Revue indépendante sur le SHA
`bab008e6c4bfb8a8c858f505b743ba6bebb4582a` (PR #27), soumise le
27 novembre 2026 à 23:20 UTC. Ce n'est pas un nouveau cycle. Le
cycle 017 n'est pas ouvert.

B22, X41 et le seuil \(\tau=1\) sont confirmés. L'édition publiée
citée par la revue n'est pas rouverte. Le sens de l'implication et
la valuation se lisent sur les énoncés déjà enregistrés et sur le
calcul ci-dessous. La conjecture 4.13 reste ouverte. Ce correctif
ne la résout pas.

**X42.** La phrase du §1, « Il impliquerait \(P(2)\), puisque éviter
\(7\) est plus fort que d'éviter la paire \(\{5,7\}\) », inversait
l'inclusion. Éviter \(\{5,7\}\) implique d'éviter \(7\). La
réciproque est fausse sur les orbites positives. Sous \(T\),
\[
5\to 8\to 4\to 2\to 1\to 2\to 1.
\]
Les résidus sont \(5,0,4,2,1\pmod 8\). Cette orbite rencontre \(5\)
et n'atteint jamais \(7\). Elle converge, donc elle ne sépare pas
les deux conclusions sur une orbite divergente. Elle sépare les
hypothèses. La conjecture 4.14, lue comme « toute trajectoire qui
évite \(5\) et \(7\pmod 8\) atteint \(1\) », ne dit rien d'une
orbite qui évite \(7\) et rencontre \(5\). \(P(2)\) implique 4.14,
par inclusion des hypothèses. L'implication inverse ne suit pas de
cette inclusion. Les deux conjectures restent ouvertes. Cette
phrase ne dit pas que 4.14 n'entraîne pas \(P(2)\) (§9).

**Valuation.** La phrase du §2, « le terme d'indice \(i\) a la
valuation \(r-i\) », est fausse si elle porte sur le terme. Pour
\(m=7\), \(r=v_2(8)=3\). Les termes \(7\), \(11\) et \(17\) sont
impairs, donc de valuation \(0\), et \(v_2(T^i(7)+1)\) vaut
\(3,2,1\). Le rang suivant est \(26\), pair, et
\(v_2(27)=0\). La formule du cycle 015 §10 donne
\(v_2(T^i(m)+1)=r-i\) pour \(0\le i\le r\). Pour \(m=15\),
\(r=4\) et le second terme est \(23\equiv 7\pmod 8\), avec
\(r-i=3\) : à partir de \(23\), en le comptant, il reste
\(23,35,53\). La valuation de \(23\) est \(0\). B22 ne change pas.
Un run a longueur au moins \(3\) si et seulement s'il commence par
\(7\pmod 8\), et un terme \(7\pmod 8\) force \(r-i\ge 3\).

## 9. Revue `6094246430`

Revue indépendante sur le SHA
`6bd08925c58185587b6c7d4eee8787eb6933706c` (PR #27), soumise le
27 novembre 2026 à 23:26 UTC. Ce n'est pas un nouveau cycle. Le
cycle 017 n'est pas ouvert.

B22, la valuation du §2 et l'implication directe de X42 sont
confirmés. L'édition publiée citée par la revue n'est pas rouverte.
Les énoncés utilisés restent ceux du PDF arXiv v3 déjà lu.

**Portée.** Le §8 dit que l'implication inverse ne suit pas de
l'inclusion des hypothèses. L'inclusion stricte, et l'orbite
convergente de \(5\), ne démontrent pas que la conjecture 4.14
n'entraîne pas \(P(2)\). Les formulations « 4.14 n'implique pas
\(P(2)\) », « et non l'inverse » et « prouver 4.14 ne prouverait
pas \(P(2)\) » dépassaient cet argument. Elles sont retirées du §1
et de la mémoire.

**Réduction de l'écart.** Soit \(n\ge 1\) dont l'orbite de \(T\) ne
rencontre pas \(7\pmod 8\).

- Si elle ne rencontre pas non plus \(5\pmod 8\), elle est une
  instance directe de la conjecture 4.14, lue comme « toute
  trajectoire qui évite \(5\) et \(7\pmod 8\) atteint \(1\) ».
- Sinon, soit \(m=T^j(n)\) le premier terme \(\equiv 5\pmod 8\).
  Alors \(m\) est impair. L'orbite de \(m\) est la queue de celle
  de \(n\), donc elle évite encore \(7\pmod 8\). Elle commence par
  \(5\pmod 8\), donc 4.14 ne s'y applique pas directement. L'orbite
  de \(n\) atteint \(1\) si et seulement si celle de \(m\) l'atteint.
  En effet \(1\not\equiv 5\pmod 8\), et l'orbite de \(1\) est
  \(\{1,2\}\), qui évite \(5\). Un passage par \(1\) avant le rang
  \(j\) empêcherait tout terme ultérieur d'être \(\equiv 5\pmod 8\).

Le même entier \(m\) est le premier terme \(\equiv 5\pmod 8\) de
l'orbite de \(C\). Depuis tout impair \(k\), \(C\) insère seulement
\(3k+1\), qui est pair, donc non congru à \(5\) ni à \(7\pmod 8\).
L'atteinte de \(1\) est déjà la même pour \(C\) et pour \(T\) (§2).
Sous \(C\), l'orbite de \(1\) est \(\{1,2,4\}\), qui évite \(5\) et
\(7\).
Sous \(C\), \(5\to 16\to 8\to 4\to 2\to 1\to 4\to 2\to 1\), résidus
\(5,0,0,4,2,1,4,2,1\pmod 8\).

Ainsi 4.14 ne couvre directement que les orbites qui évitent les
deux résidus. Pour en déduire \(P(2)\), il reste à traiter celles
qui évitent \(7\) et rencontrent \(5\), et il suffit de le faire
sur la queue issue du premier terme \(\equiv 5\pmod 8\). L'évitement
de \(7\) et l'atteinte ultérieure de \(1\) se transmettent à cette
queue. Aucune des conjectures 4.13 et 4.14 n'est résolue. On ne
conclut pas que l'une n'entraîne pas l'autre.

Le script vérifie, pour chaque départ de \(1\) à \(4000\), que \(C\)
et \(T\) rencontrent \(5\pmod 8\) ensemble, et, lorsque l'orbite de
\(T\) évite \(7\), que le premier \(5\) éventuel a la même atteinte
de \(1\) et évite \(7\). Ce contrôle fini n'est pas la preuve.
