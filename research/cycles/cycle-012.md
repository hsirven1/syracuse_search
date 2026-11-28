# Cycle 012 — Aucun potentiel \(\log_2(n+1)+c\,v_2(n+1)\) n'est une fonction de Lyapunov stricte

Date : 27 novembre 2026. Axe **A**.
Branche : `research/memory`. Script : [`../checks/cycle012_lyapunov.py`](../checks/cycle012_lyapunov.py).

**Verdict : X31 et B17 sont prouvés.** Pour tout réel \(c\),
\(V(n)=\log_2(n+1)+c\,v_2(n+1)\) n'est pas une fonction de Lyapunov
stricte le long des orbites positives de \(T\) hors de \(\{1,2\}\).
Plus généralement, aucune fonction réelle de la seule valuation
\(v_2(n+1)\) ne répare \(\log_2(n)\) ni \(\log_2(n+1)\) sur l'application
accélérée \(U\), si la décroissance est exigée pour tout impair \(>1\).
Ce n'est pas une preuve de Syracuse. L'exception finie et la
correction jointe \((n\bmod M,\ v_2(n+1))\), sans compteurs de facteurs
premiers, sont fermées par B18 (§9). La forme qui ajoute
\(\omega\), \(\Omega\) et une fonction de \(\Omega-\omega\) n'est pas
tranchée.

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
Le crible des lemmes 3 et 4 n'a pas été revérifié. Ce texte n'est pas
une prémisse de B17. La partie sans compteurs est prouvée au §9, par
une progression explicite, sans ce crible.

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
sont autonomes. Cette dichotomie ne donne pas, à elle seule, des
témoins arbitrairement grands si \(\Phi\) peut échouer en \(3\), \(7\)
et \(9\). Cette infinitude est B18, au §9, par une autre famille.

## 5. Ce que ce cycle ne montre pas

Rien sur (C), sur (H), ni sur Syracuse. B17 n'exclut pas, à lui seul,
une décroissance qui échouerait seulement en \(3\), \(7\) et \(9\) :
les trois pas n'imposent plus la même valeur de \(\Phi\) dès qu'un
résidu modulo \(M\) entre dans la correction. Cette exception finie,
et la correction jointe sans compteurs, sont B18 (§9), pas une question
ouverte. Les variantes (1), (3) et (4) du §4 de Chang, précision
adaptative, ordinaux et quantités non locales, ne sont pas traitées.
Le poids \(h(t)=1000\,t\) montre seulement que l'esquisse du §4(2) ne
couvre pas les fonctions à croissance rapide.

La forme avec compteurs reste hors de ce cycle. Sur un seul trajet,
\(\omega\) peut changer : pour \(A=2\), \(x=123=3\cdot41\) et
\(z=139\), qui est premier, donc \(\omega\) passe de \(2\) à \(1\).
Les lemmes 3 et 4 de la note, qui produisent deux trajets de signes
opposés, ne sont pas relus comme preuve.

## 6. Mises à jour de la mémoire

- `proved.md` : B17, puis B18 après la revue `6082913526`.
- `counterexamples.md` : X31, puis X32.
- `hypotheses.md` : H7 est réfutée, y compris hors d'un ensemble fini
  et pour le couple \((n\bmod M, v_2(n+1))\) sans compteurs.
- `prior_art.md` : Chang, théorème 3.1 et §4(2) ; la branche de la note
  du 19 octobre 2026, sans adoption du crible.
- `abandoned.md` : ne pas relancer la forme sans compteurs.
- `agenda.md` : la question suivante est le seul complément avec
  compteurs, non entamé. Le budget de cycles reste celui du §8.
- `reviews.md` : revues `6082845312` et `6082913526`.

## 7. Prochaine question

Axe **B**, un seul énoncé, et seulement après le budget du blocage de
l'agenda. B18 ferme la correction \(H(n)+\Phi(n\bmod M, v_2(n+1))\),
hors d'un ensemble fini, sur \(U\) et sur \(T\). La note du 19 octobre
2026 affirme davantage : la même forme, augmentée de
\(\beta\omega(n)+\gamma\Omega(n)+R(\Omega(n)-\omega(n))\), ne peut pas
être non croissante sur tous les grands pas impairs de \(U\).

Le cycle suivant commence par la porte d'antériorité sur ce seul
complément. Le théorème 1 de la note n'est pas adopté : ses lemmes 3
et 4, crible de valeurs sans facteur carré, n'ont pas été revérifiés.
Ou bien cette preuve a un trou précis, ou bien l'obstruction avec
compteurs est déjà écrite et ne doit pas être refaite. Pas de nouvel
ansatz avant cette porte. Ne pas rouvrir B10, B13, B17, B18, X21, X31,
le signe moins, le mot du cycle 006, la famille \(5\cdot 2^k-1\), les
conjectures 2 et 3 de Berg–Meinardus, ni les théorèmes 4.2.7 et 4.3.10
de Mori. Ne pas déduire Syracuse d'une descente partielle.

## 8. Reproduire

```sh
python3 research/checks/cycle012_lyapunov.py
```

Sortie attendue : trois lignes `PASS`. Les deux premières couvrent les
trois images accélérées, les deux identités de hauteur, les trois
comparaisons entières, le poids \(1000\,t\), le pas \(6\to 3\),
l'égalité au seuil sur \(3\to 5\), et cinq rationnels \(c>\beta\). La
troisième couvre la famille du §9 : identités, valuations, congruence,
bilan strict, dix mille couples \((M,q)\), cinq rationnels \(c>\beta\)
sur le pas pair, et le témoin \(123\to139\) où \(\omega\) change. Ces
contrôles ne sont pas la preuve.

## 9. Revue `6082913526` : exceptions finies et résidu joint (B18)

Revue indépendante sur le SHA
`41cced5e74fd9dcf1d3288c8a9fc4181041f2e92` (PR #27), marqueur
`SYRACUSE_INDEPENDENT_REVIEW`. X31 et B17 (§§1–3) sont confirmés. Le
pas \(3\to 5\) a l'écart \(\beta-c\). Pour \(c>\beta\),
\(V(3)-V(6)>\log_2(9/7)\). Les témoins de \(U\) sont \(3,7,9\), hors de
\(\{1,2\}\). Aucune correction de ces deux énoncés.

**Porte, pour le seul correctif.** L'énoncé ajouté est le suivant.
Soit \(M\ge 1\). Soit \(\Phi\) une fonction réelle quelconque de
\((n\bmod M,\ v_2(n+1))\).

- Si \(H\) est strictement croissante sur les impairs positifs, aucun
  entier \(N_0\) ne satisfait \(V(U(n))<V(n)\) pour tout impair
  \(n>N_0\), ni la même phrase avec \(\le\).
- Si \(H\) est strictement croissante sur les entiers \(\ge 1\), aucun
  entier \(N_0\) ne satisfait \(V(T(n))<V(n)\) pour tout entier
  \(n>N_0\), ni la même phrase avec \(\le\).

Ici \(V=H+\Phi\). L'obstacle était la phrase « reste ouvert » des §§5
et 7 de la première rédaction. La fermer retire une architecture de
certificat. Elle ne contraint pas une orbite divergente.

Le résultat le plus proche déjà certifié est le théorème 3.1 de Chang :
\(\log_2 n+g(n\bmod 2^k)\), sans valuation. Il ne voit pas
\(v_2(n+1)\). Son §4(2) ne prouve pas non plus la valuation seule. La
note du 19 octobre 2026, §3, écrit le cycle signé \(-5\xrightarrow{1}-7\xrightarrow{2}-5\) et
\(F(n)=(9n+5)/8\). Son théorème 1 ajoute les compteurs et un crible.
Ce théorème est plus fort si le crible est juste, mais les lemmes 3 et
4 ne sont pas vérifiés ici : B18 n'en est pas un corollaire. Les
formules \(x=64A-5\), \(y=96A-7\), \(z=72A-5\) ne sont pas copiées de
la note. Les deux trajets affichés au §6 de la note, \(187\to281\to211\)
et \(379\to569\to427\), sont les cas \(A=3\) et \(A=6\) de ces
formules. Classement : prouvé ici, sans revendication d'originalité.
La branche est celle de la note ; le crible reste non adopté.
Signification : fermer l'exception finie et le couple résidu–valuation.
Pas une contrainte sur un contre-exemple hypothétique de Syracuse.

**Preuve.** Soit \(q\ge 1\) et \(A=Mq\). Posons
\[
x=64A-5,\qquad y=96A-7,\qquad z=72A-5.
\]
Alors
\[
3x+1=192A-14=2y,\qquad 3y+1=288A-20=4z.
\]
Les entiers \(96A\) et \(72A\) sont pairs, donc \(y\) et \(z\) sont
impairs, \(x\) aussi. Ainsi \(v_2(3x+1)=1\), \(v_2(3y+1)=2\),
\(U(x)=y\) et \(U(y)=z\). Sous \(T\), \(T(x)=y\), \(T(y)=2z\) et
\(T(2z)=z\).

Ensuite \(z-x=8A>0\). De plus
\[
x+1=4(16A-1),\qquad z+1=4(18A-1),
\]
et \(16A-1\), \(18A-1\) sont impairs, donc \(v_2(x+1)=v_2(z+1)=2\).
Comme \(64A\) et \(72A\) sont des multiples de \(M\),
\(x\equiv z\equiv -5\pmod M\). Les deux arguments de \(\Phi\)
coïncident, et
\[
V(z)-V(x)=H(z)-H(x)>0
\]
dès que \(H(z)>H(x)\). C'est le cas si \(H\) est strictement croissante
sur les impairs, puisque \(x\) et \(z\) sont impairs.

Les départs de \(U\) sont \(x\) et \(y\), avec \(y-x=32A-2>0\). Soit
\(q=\max(N_0,0)+1\). Alors \(A\ge 1\) et \(x\ge 59\). Si \(N_0\ge 0\),
\[
x=64M(N_0+1)-5\ge 64(N_0+1)-5>N_0.
\]
Si \(N_0<0\), alors \(x\ge 59>N_0\). Dans les deux cas \(y>x>N_0\). Si
les deux pas vérifiaient \(V(U(\cdot))\le V\), on aurait
\(V(z)\le V(x)\). Contradiction. L'un des deux pas augmente donc \(V\).
La même comparaison exclut l'inégalité stricte.

Sous \(T\), les trois départs sont \(x\), \(y\) et \(2z=144A-10\), et
\(2z-y=48A-3>0\). Le même \(q\) place \(x\), \(y\) et \(2z\) au-dessus
de \(N_0\). Le bilan \(V(z)>V(x)\) force l'un des trois pas à augmenter
\(V\), pourvu que \(H\) soit définie et strictement croissante sur tous
les entiers \(\ge 1\), afin que \(V(2z)\) ait un sens. On ne désigne
pas lequel des trois pas augmente, pour un \(\Phi\) quelconque.

**Famille linéaire.** Pour \(V(n)=\log_2(n+1)+c\,v_2(n+1)\), tout pas
impair de \(T\) a l'écart \(\beta-c\), car
\(T(n)+1=3(n+1)/2\) et la valuation baisse de \(1\). Donc
\(V(y)-V(x)=V(2z)-V(y)=\beta-c\). Sur le pas pair,
\[
2z+1=9(16A-1),\qquad z+1=4(18A-1),
\]
et
\begin{align*}
V(z)-V(2z)
&=2c+\log_2\frac{4(18A-1)}{9(16A-1)}\\
&=2(c-\beta)+\log_2\frac{18A-1}{16A-1}.
\end{align*}
Le second terme est strictement positif, car \(18A-1>16A-1\). Si
\(c<\beta\), le pas \(x\to y\) augmente \(V\). Si \(c=\beta\), ce pas
a un écart nul, et \(2z\to z\) augmente \(V\). Si \(c>\beta\), le pas
\(2z\to z\) augmente \(V\). Dans les trois cas le départ est
arbitrairement grand. Pour \(c>\beta\), tout pas impair diminue \(V\) de
\(c-\beta\) : l'obstruction éventuelle est le pas pair. Le bilan des
trois pas ne dépend pas de \(c\),
\[
V(z)-V(x)=\log_2\frac{18A-1}{16A-1}>0,
\]
puisque les valuations aux extrémités sont égales.

**Ce que B18 ne reprend pas.** Le théorème 1 de la note demande deux
trajets, des extrémités sans facteur carré, et des poids positifs qui
annulent \(\omega\) et \(\Omega\). Un seul trajet ne le fait pas :
\(A=2\) donne \(x=123=3\cdot 41\) et \(z=139\), premier. Ce théorème,
ses lemmes 3 et 4, et l'argument de Brun–Titchmarsh ne sont pas
adoptés. Les variantes non additives, les temps de retour adaptatifs
et les dérives moyennes restent hors de l'énoncé, comme la note le
dit elle-même au §7. Ce n'est pas le cycle 013 : le budget de douze
cycles dans la fenêtre de vingt-quatre heures reste en vigueur, et
cette section est le correctif de la revue.
