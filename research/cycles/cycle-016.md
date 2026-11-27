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

**Intérêt.** Il impliquerait \(P(2)\), puisque éviter \(7\) est plus
fort que d'éviter la paire \(\{5,7\}\).

**Résultat le plus proche.** La conjecture 4.14 elle-même, et le
cycle \(-5\to-7\to-10\to-5\), qui évite ces deux résidus (§3).

**Écart.** Aucun énoncé intermédiaire n'est proposé.

**Classement.** DÉJÀ CONNU comme conjecture ouverte. Confiance haute
sur le texte. Pas de stratégie qui n'essaie pas de résoudre cette
conjecture.

**Décision.** NO-GO. Trois candidats ont été examinés. Une seule
comparaison est écrite : l'équivalence du candidat 1.

## 2. Équivalence

Le run impair issu d'un impair \(m\) a longueur \(v_2(m+1)\) (cycle 015,
§10). Cette longueur est au moins \(3\) si et seulement si
\(m\equiv 7\pmod 8\). Dans un run de longueur \(r\), le terme d'indice
\(i\) a la valuation \(r-i\). Un terme impair \(\equiv 7\pmod 8\) force
donc le run qui le contient à avoir une longueur au moins \(3\).
Inversement, un run de longueur au moins \(3\) commence par un tel
terme. Ainsi \(P(2)\) dit que toute orbite positive de \(T\) qui ne
rencontre pas le résidu \(7\pmod 8\) atteint \(1\).

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
le résidu modulo \(8\). Ces contrôles ne remplacent pas le §2.

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
indépendante de ce cycle, ni avant le 28 novembre 2026 à 00:04 UTC.

## 7. Reproduire

```sh
python3 research/checks/cycle016_run_bound.py
```

Sortie attendue : 5 lignes `PASS`.
