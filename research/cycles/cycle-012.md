# Cycle 012 — Aucun potentiel \(\log_2(n+1)+c\,v_2(n+1)\) n'est une fonction de Lyapunov stricte

Date : 27 novembre 2026. Axe **A**.
Branche : `research/memory`. Script : [`../checks/cycle012_lyapunov.py`](../checks/cycle012_lyapunov.py).

**Verdict : X31 et B17 sont prouvés.** Pour tout réel \(c\),
\(V(n)=\log_2(n+1)+c\,v_2(n+1)\) n'est pas une fonction de Lyapunov
stricte le long des orbites positives de \(T\) hors de \(\{1,2\}\).
Plus généralement, aucune fonction réelle de la seule valuation
\(v_2(n+1)\) ne répare \(\log_2(n)\) ni \(\log_2(n+1)\) sur l'application
accélérée \(U\), si la décroissance est exigée pour tout impair \(>1\).
Ce n'est pas une preuve de Syracuse. Le cas d'un ensemble fini
d'exceptions, et le cas d'une correction qui voit à la fois un résidu
fixe et la valuation, restent ouverts.

## 0. Revue traitée, question, porte d'antériorité

La revue `6082845312` porte le marqueur `SYRACUSE_INDEPENDENT_REVIEW`
et le SHA `a29ba6992d54dedee90f4e443998dba5dadd5d08`, qui est la tête
de la PR #27. Elle confirme le résidu \(-\lambda^\mu\), le coefficient
\(\lambda^{2\mu}\), l'équivalence \(a_n=a_{t(n)}\) et le témoin de
Meinardus 2001. Elle ne demande aucune correction. Le cycle 011 n'est
pas réécrit. L'article de 1994 reste non lu, déjà dit au §12 de ce cycle.

**Candidat.** Soit \(\beta=\log_2(3/2)\). Pour tout réel \(c>\beta\) et
tout entier \(n>2\),
\(V(T(n))<V(n)\), où \(V(n)=\log_2(n+1)+c\,v_2(n+1)\) et
\(T(n)=n/2\) si \(n\) est pair, \((3n+1)/2\) si \(n\) est impair.
Hors du cycle \(\{1,2\}\), la décroissance stricte le long de toute
orbite positive est la même exigence : un témoin est un entier \(n>2\)
et un temps \(t\ge 1\) avec \(V(T^t(n))\ge V(n)\).

L'énoncé effectivement prouvé est plus ferme, et c'est lui qui passe
la porte. Pour toute fonction \(\Phi:\mathbb Z_{\ge 1}\to\mathbb R\),
ni \(\log_2(n)+\Phi(v_2(n+1))\) ni \(\log_2(n+1)+\Phi(v_2(n+1))\) ne
vérifie \(V(U(n))<V(n)\) pour tout impair \(n>1\), où
\(U(n)=(3n+1)/2^{v_2(3n+1)}\).

**Obstacle.** Un pas impair de \(T\) ajoute exactement \(\beta\) à
\(\log_2(n+1)\) et retire \(1\) à la valuation. La correction
\(c\,v_2(n+1)\) annule cette hausse dès que \(c>\beta\). H7 le notait,
sans entier. La question est de savoir si cette annulation laisse une
descente stricte.

**Intérêt.** Une fonction de Lyapunov stricte, propre et minorée,
prouverait la conjecture. Réfuter cette forme-ci ne prouve rien sur
les orbites : elle retire seulement une famille explicite de
certificats. C'est l'énoncé que l'agenda demandait de trancher, et la
variante que le préprint de Chang laisse ouverte.

**Résultat le plus proche.** Lightman Chang, *No Finite Local Potential
Function Is a Strict Lyapunov Function for the Accelerated Collatz Map*,
préprint indépendant, PDF
`https://collatz-research-report.proof.weiqi.kids/paper-b/paper.pdf`,
SHA-256
`01bdca4bde966ed815f10dce307e6627e7fba4e14873f510361b96238e5e254b`,
6 pages, non redistribué. **[P]** pour la définition 2.1, le théorème 3.1
et le §4(2) seulement. Son \(S\) est notre \(U\). Le théorème 3.1 exclut
\(\log_2 n+g(n\bmod 2^k)\) pour \(k\) fixé et \(g\) quelconque. Le §4(2)
écrit que \(\log_2 n+h(t(n))\), avec \(t(n)=v_2(n+1)\), « n'est pas
directement couvert », esquisse un argument, et « laisse l'énoncé complet
au lecteur ». Cette esquisse ne donne pas notre preuve : elle est
discutée au §4. Lagarias 1985, lemme 2.1, cité par Chang pour la forme
des blocs de uns, n'a pas été rouvert. Les identités de ce cycle sont
calculées sur trois entiers.

Une note du 19 octobre 2026, lue sur
`https://rstation.ai/problems/collatz/papers/3`, affirme une obstruction
pour \(H(n)+\Phi(n\bmod M,v_2(n+1))\) plus des compteurs de facteurs
premiers, hors d'un ensemble fini. Ce n'est pas une publication primaire.
Le crible n'a pas été revérifié. Ce texte n'est pas une prémisse. Notre
énoncé ne conclut ni pour un module, ni hors d'un ensemble fini.

**Écart.** Le théorème 3.1 de Chang fixe le module et ne voit pas
\(v_2(n+1)\). Le §4(2) vise \(\log_2 n+h(v_2(n+1))\) mais ne le prouve
pas. Nous prouvons cette forme, et la forme \(\log_2(n+1)\), par trois
pas exacts, sans bloc de uns arbitrairement long. Le candidat linéaire
sur \(T\), lui, est l'observation H7 : aucun entier n'y était écrit.

**Classement.** POTENTIELLEMENT NOUVEAU pour l'énoncé complet sur
\(\Phi\), confiance modérée : le théorème 3.1 et le §4(2) ont été lus,
le reste de la littérature des potentiels n'a pas été réinventorié.
L'argument est élémentaire. Ce n'est pas une découverte sur les
trajectoires arbitraires. Signification : fermer H7 et la variante
laissée ouverte au §4(2). Pas une contrainte sur un contre-exemple
hypothétique.

**Décision.** GO pour cette réfutation. Pas de GO pour en déduire
Syracuse. Le cas \(c\le\beta\) est déjà le premier pas d'un Mersenne ;
le travail nouveau est le témoin \(c>\beta\), puis la forme arbitraire
\(\Phi\), qui est le même calcul.

## 1. Pas impairs et pas pairs

Si \(n\) est impair, \(T(n)+1=3(n+1)/2\), donc
\(\log_2(T(n)+1)=\log_2(n+1)+\beta\) et
\(v_2(T(n)+1)=v_2(n+1)-1\). L'écart de \(V\) vaut \(\beta-c\).

Si \(n=6\), \(T(6)=3\), \(v_2(7)=0\) et \(v_2(4)=2\). Donc
\[
V(3)-V(6)=2+2c-\log_2 7.
\]
Pour \(c>\beta\),
\[
2+2c-\log_2 7>2+2\beta-\log_2 7=\log_2 9-\log_2 7=\log_2(9/7)>0,
\]
car \(2+2\beta=\log_2 4+\log_2(9/4)=\log_2 9\) et \(9>7\).

Si \(c=\beta\), le pas \(3\to 5\) a un écart nul :
\((5+1)/(3+1)=3/2\). Si \(c<\beta\), le même pas augmente \(V\) de
\(\beta-c\). En particulier \(\beta>1/2\), car \(9>8\).

## 2. Famille linéaire sur \(T\) (X31)

**Proposition.** Pour tout réel \(c\), \(V\) n'est pas une fonction de
Lyapunov stricte sur les entiers \(\ge 1\) hors de \(\{1,2\}\).

Si \(c<\beta\), \(V(T(3))-V(3)=\beta-c>0\). Si \(c=\beta\), cet écart
est nul. Si \(c>\beta\), \(V(T(6))-V(6)>\log_2(9/7)>0\). Dans les trois
cas, \(n>2\) et \(t=1\).

Le cycle \(\{1,2\}\) est exclu de l'énoncé : \(T(1)=2\) et \(T(2)=1\).
Le pas \(1\to 2\) a pour écart \(\beta-c\), donc il décroît lorsque
\(c>\beta\), tandis que \(2\to 1\) augmente. Cela ne répare pas le pas
\(6\to 3\).

## 3. Toute correction de la seule valuation (B17)

**Proposition.** Soit \(\Phi:\mathbb Z_{\ge 1}\to\mathbb R\). Posons
\(t(n)=v_2(n+1)\) pour \(n\) impair. Aucune des deux fonctions
\[
V_0(n)=\log_2 n+\Phi(t(n)),\qquad
V_1(n)=\log_2(n+1)+\Phi(t(n))
\]
ne vérifie \(V(U(n))<V(n)\) pour tout impair \(n>1\).

Les trois pas utilisés sont \(U(3)=5\), \(U(7)=11\) et \(U(9)=7\).
Pour \(n=3\) et \(n=7\), la valuation de \(3n+1\) vaut \(1\), et
\[
U(n)+1=3(n+1)/2.
\]
Donc \(t(3)=2\), \(t(5)=1\), \(t(7)=3\), \(t(11)=2\), et
\(\log_2(U(n)+1)=\log_2(n+1)+\beta\). Enfin \(t(9)=1\) et \(t(7)=3\).

*Cas \(V_1\).* Si \(\Phi(2)-\Phi(1)\le\beta\), alors
\(V_1(5)-V_1(3)\ge 0\). Sinon, si \(\Phi(3)-\Phi(2)\le\beta\), alors
\(V_1(11)-V_1(7)\ge 0\). Sinon les deux écarts sont stricts, donc
\(\Phi(3)-\Phi(1)>2\beta=\log_2(9/4)\) et
\[
V_1(7)-V_1(9)=\log_2(4/5)+\Phi(3)-\Phi(1)>\log_2(4/5)+\log_2(9/4)=\log_2(9/5).
\]
Comme \(9>5\), cet écart est strictement positif.

*Cas \(V_0\).* Si \(\Phi(2)-\Phi(1)\le\log_2(5/3)\), alors
\(V_0(5)\ge V_0(3)\). Sinon, si \(\Phi(3)-\Phi(2)\le\log_2(11/7)\), alors
\(V_0(11)\ge V_0(7)\). Sinon
\(\Phi(3)-\Phi(1)>\log_2(55/21)\) et
\[
V_0(7)-V_0(9)>\log_2(7/9)+\log_2(55/21)=\log_2(385/189).
\]
Comme \(385>189\), cet écart est strictement positif.

Les deux dichotomies couvrent toutes les fonctions réelles \(\Phi\).
Le point \(n=1\) est exclu : \(U(1)=1\).

La famille linéaire de l'agenda est le cas \(\Phi(v)=c v\) de \(V_1\),
transporté sur \(T\) par le §2. Pour \(c>\beta\), le pas accéléré
\(9\to 7\) donne déjà \(V_1(7)>V_1(9)\), puisque
\(\Phi(3)-\Phi(1)=2c>2\beta\). Le témoin demandé par l'agenda reste
\(6\to 3\), qui est un seul pas de \(T\).

## 4. Ce que le §4(2) de Chang ne prouve pas

Dans la preuve de son théorème 3.1, l'oscillation \(G\) de \(g\) est
finie et indépendante de la longueur \(\ell\), parce que \(g\) ne prend
qu'un nombre fini de valeurs. On choisit ensuite
\(\ell\cdot\log_2(3/2)>G+1\).

Pour \(h(t(n))\), la même construction compare des valuations
\(t(n_M)=\ell+k\) et \(t(S^\ell(n_M))=k\). La différence
\(h(k)-h(\ell+k)\) dépend de \(\ell\). Elle n'est pas bornée avant le
choix de \(\ell\). Si \(h(t)=1000\,t\), cette différence vaut
\(-1000\ell\), et \(\ell\beta-1000\ell<0\) : la minoration du théorème 3.1
ne passe pas. Le même \(h\) est tout de même exclu par B17. En effet
\(h(3)-h(1)=2000>\log_2(55/21)\), et
\(V_0(7)-V_0(9)=\log_2(7/9)+2000>0\) dès que \(7\cdot 2^{2000}>9\).

Le théorème 3.1, lui, n'est pas mis en cause. Il ne porte pas sur
\(h(t(n))\). Nous n'adoptons pas sa preuve : les trois pas ci-dessus
sont autonomes. Nous n'en tirons pas non plus l'infinité des témoins
pour une fonction \(\Phi\) qui aurait le droit d'échouer en \(3\), \(7\)
et \(9\).

## 5. Ce que ce cycle ne montre pas

Rien sur (C), sur (H), ni sur Syracuse. Une fonction qui décroît pour
tout impair assez grand, mais pas en \(3\), \(7\) ou \(9\), n'est pas
exclue. Une correction \(\Phi(n\bmod M, v_2(n+1))\), pour un module
\(M\) fixé, n'est pas exclue non plus : les trois pas n'imposent plus
la même valeur de \(\Phi\) à valuation égale. Les variantes (1), (3) et
(4) du §4 de Chang, précision adaptative, ordinaux et quantités non
locales, ne sont pas traitées. Le poids \(h(t)=1000\,t\) montre seulement
que l'esquisse du §4(2) ne couvre pas les fonctions à croissance rapide.
Il ne ferme pas la question hors d'un ensemble fini.

## 6. Mises à jour de la mémoire

- `proved.md` : B17. La revue `6082845312` est enregistrée sous B16,
  sans changement de formule.
- `counterexamples.md` : X31.
- `hypotheses.md` : H7 est réfutée pour la famille écrite.
- `prior_art.md` : Chang, théorème 3.1 et §4(2).
- `abandoned.md` : ne pas relancer cette forme de potentiel.
- `agenda.md` : question suivante, et budget de cycles.
- `reviews.md` : revue `6082845312`.

## 7. Prochaine question

Axe **B**, un seul énoncé, et seulement après le budget du §8 de
l'agenda. Le théorème 3.1 de Chang et B17 laissent ouverte une
correction qui dépend du couple \((n\bmod M, v_2(n+1))\). La note du
19 octobre 2026 citée au §0 affirme que cette forme, même augmentée de
compteurs de facteurs premiers, ne peut pas être non croissante sur
tous les grands pas impairs de \(U\).

Le cycle suivant commence par la porte d'antériorité sur cet énoncé,
pas par un nouveau potentiel. Ou bien la preuve lue a un trou précis,
ou bien l'obstruction est déjà écrite et ne doit pas être refaite.
Ne pas rouvrir B10, B13, X21, le signe moins, le mot du cycle 006, la
famille \(5\cdot 2^k-1\), les conjectures 2 et 3 de Berg–Meinardus, ni
les théorèmes 4.2.7 et 4.3.10 de Mori. Ne pas déduire Syracuse d'une
descente partielle.

## 8. Reproduire

```sh
python3 research/checks/cycle012_lyapunov.py
```

Sortie attendue : deux lignes `PASS`. Elles couvrent les trois images
accélérées, les deux identités de hauteur, les trois comparaisons
entières, le poids \(1000\,t\), le pas \(6\to 3\), l'égalité au seuil
sur \(3\to 5\), et cinq rationnels \(c>\beta\). Ces contrôles ne sont
pas la preuve : la dichotomie sur \(\Phi\) est au §3.
