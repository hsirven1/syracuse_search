# Cycle 010 — Préfixe de \(5\cdot2^k-1\) : sortie et second bloc au-dessus du départ

Date : 27 novembre 2026. Axe **A**.
Branche : `research/memory`. Script : [`../checks/cycle010_accelerated_descent.py`](../checks/cycle010_accelerated_descent.py).

**Verdict : B15 et le second bloc sont prouvés. Pas de formule de
\(\tau\) jusqu'à la descente, et pas de preuve que \(\tau>2k\) pour une
infinité de \(k\).**
Le préfixe accéléré \(t\le k-1\) est connu. Pour \(k\ge3\), la sortie
reste strictement au-dessus de \(n_k\), donc \(\tau(n_k)\ge k+1\) (B15).
Pour \(k\) impair \(\ge3\), les orbites de \(n_k\) et de \(n_{k+1}\) se
rejoignent au pas \(k+1\). Si aucun temps de descente n'existe,
\(\tau=+\infty\) : les comparaisons n'exigent pas la terminaison.
Le bloc suivant est explicite. Avec \(L=v_2(5\cdot3^k+1)-1\), on a
\(U^{k+s}(n_k)=3^s(5\cdot3^k+1)/2^{s+1}-1>n_k\) pour \(0\le s<L\), donc
\(\tau(n_k)\ge k+L\). La longueur \(L\) et l'exposant extrait au pas
\(k+L\) dépendent de \(k\). Comme \(L\) n'est pas bornée sur les impairs,
\(\tau(n_k)-k\) ne l'est pas non plus. Cela ne donne pas \(\tau>2k\)
infiniment souvent. L'inégalité universelle \(\tau\le2k\) est fausse
(X28). Le segment \(2\le k\le1000\) montre les deux signes ; il ne prouve
pas l'infinité. Ce n'est pas une preuve de Syracuse, ni une contrainte
sur une trajectoire arbitraire.

## 0. Question traitée, et porte d'antériorité

La revue `6082502361` confirme le correctif de `6082438456` sur le SHA
`c5ab64394914d91280442ab479f264a840dd5942`. Elle ne demande aucune
correction. Le résidu qu'elle exhibe est revérifié au §7. Le cycle 009
n'est pas réécrit.

**Candidat.** Pour \(k\ge2\), \(n_k=5\cdot2^k-1\) et
\(U(n)=(3n+1)/2^{v_2(3n+1)}\), le temps
\(\tau(n)=\min\{t\ge1:U^t(n)<n\}\) admet-il, sur \(n=n_k\), une borne
explicite en \(k\), donnée par une trajectoire en forme close ? Sinon,
a-t-on \(\tau(n_k)>2k\) pour des \(k\) arbitrairement grands ? Si
l'ensemble est vide, \(\tau(n)=+\infty\). Les inégalités de temps
s'entendent dans les réels étendus.

**Obstacle.** \(n_k\equiv3\pmod4\), donc \(U(n_k)>n_k\). La longueur de
la queue de uns est \(k=v_2(n_k+1)\). Une formule close de la première
descente donnerait une famille infinie, non prescrite par un cylindre
fini, avec \(\tau\) borné explicitement. A3 rappelle que le quantificateur
inverse, un cylindre pour chaque \(m\), n'exclut rien hors du cylindre.

**Intérêt.** Un seul départ par échelle \(k\). Même une formule close ne
contraindrait pas les autres trajectoires. L'agenda demandait de
s'arrêter si aucun mécanisme clos n'apparaissait après l'antériorité et
un contre-exemple borné.

**Résultat le plus proche.**
- Montée de Mersenne A2, cas \(b=1\) : \(U^t(2^h-1)=3^t2^{h-t}-1\) pour
  \(t\le h-1\).
- `FIXED_ODD_PART_MULTIRUN_OBSTRUCTION.md`, (i) : pour le Terras
  \(T\), \(T^t(5\cdot2^{r_0}-1)+1=5\cdot3^t2^{r_0-t}\) tant que
  \(t\le r_0\). Les états \(t\le k-1\) sont impairs et chaque pas a
  valuation \(1\), donc \(U^t=T^t\) sur ce préfixe.
- Wikipedia, page « Collatz conjecture », section Syracuse function, lue
  dans le rendu obtenu pour ce cycle : pour \(p\ge1\) et \(h\) impair,
  \(f^{p-1}(2^ph-1)=2\cdot3^{p-1}h-1\). Ce n'est pas une source primaire.
  Pour \(h=5\) et \(p=k\), c'est \(U^{k-1}(n_k)\).
- Wiltrout–Landquist, *Furman University Electronic Journal of
  Undergraduate Mathematics* 17 (2016), 1–5. Le rendu du dépôt
  `article=1028` a été lu ; l'en-tête de ce rendu porte aussi la date
  2013. Le PDF brut a répondu 403, donc pas d'empreinte SHA-256.
  **Théorème 1, lu :** si \(k,b\ge1\) et \(2^kb-1>1\), alors
  \(T^{(k)}(2^kb-1)=3^kb-1\), où \(T\) est le Terras du dépôt.
  **Théorème 4, lu :** si \(b\ge3\) est impair, \(b\equiv1\pmod4\) et
  \(k\ge2\) est pair, alors les deux orbites de Terras se rejoignent en
  \((3^kb-1)/4\), et les temps totaux d'atteinte de \(1\) diffèrent de
  \(1\). Le cas \(b\equiv3\pmod4\) est l'autre puce, non utilisée.
  **§4, lu :** une formule explicite pour le temps total
  \(\sigma_\infty(2^kb-m)\) est laissée ouverte. Leur \(\sigma_\infty\)
  compte les pas de Terras jusqu'à \(1\). Ce n'est pas \(\tau\).
- Le cylindre de `EXACT_STOPPING_TIME_BASELINE.md` suppose
  \(v_2(q\cdot3^m-1)=m\). Pour \(q=5\) cette valuation vaut \(1\) ou \(2\),
  jamais \(k\) dès que \(k\ge3\). Le cylindre ne descend donc pas \(n_k\).

**Écart.** Le théorème 1 s'arrête sur l'entier pair \(5\cdot3^k-1\).
La propriété de Syracuse s'arrête au pas accéléré \(k-1\), encore
au-dessus de \(n_k\). Aucun des deux ne compare \(U^k(n_k)\) à \(n_k\),
ni ne parle de \(\tau(n_k)\) contre \(2k\).

**Classification.** Le préfixe \(t\le k-1\) est **ALREADY KNOWN**.
La valeur de jonction \((5\cdot3^{k+1}-1)/4\) est un **DIRECT COROLLARY**
du théorème 4 pour \(b=5\), une fois les pas pairs du Terras regroupés
en pas de \(U\). La comparaison \(\tau\ge k+1\) n'y figure pas. Le second
bloc du §4 non plus : c'est la même identité \(U(x)+1=(3/2)(x+1)\) tant
que \(x\equiv3\pmod4\), poursuivie jusqu'à épuisement de la valuation.
Une formule complète de \(\tau\) est **PRIOR ART UNVERIFIED**. Le §4 de
Wiltrout–Landquist porte sur le temps total de Terras jusqu'à \(1\), pas
sur \(\tau\). Il ne fournit pas cette formule et ne l'exclut pas. Rien
de lu ne donne \(\tau\). Ce n'est pas une preuve de nouveauté.

**Décision.** **NO-GO** pour une formule complète de \(\tau\), et
**NO-GO** pour une preuve que \(\tau>2k\) infiniment souvent. La raison
n'est pas le §4 de Wiltrout–Landquist. Après le second bloc, l'exposant
extrait \(v_2(3^Lm-1)\) dépend de \(k\) et la suite est la dynamique
générale de \(U\). La non-bornitude de \(L\) ne force pas \(L>k\).
**GO** initial pour la comparaison de taille et pour le relevé borné.
Le second bloc est la correction de la revue `6082611497`, vérifiée par
le même script, pas un second candidat. La famille \(a=1\) et la classe
\(n\equiv1\pmod4\), \(n>1\), restent écartées. \(U(1)=1\).

## 1. Préfixe et sortie

**Lemme.** Soient \(k\ge2\) et \(n_k=5\cdot2^k-1\). Pour \(0\le t\le k-1\),
\[
U^t(n_k)=5\cdot3^t\cdot2^{k-t}-1,
\]
et cette valeur est \(>n_k\) dès que \(t\ge1\). De plus
\(v_2(5\cdot3^k-1)=1\) si \(k\) est impair et \(=2\) si \(k\) est pair.
Alors
\[
U^k(n_k)=\frac{5\cdot3^k-1}{2^{\varepsilon(k)}},
\]
avec \(\varepsilon(k)\) cette valuation.

**Preuve.** Le pas \(t=0\) est \(n_k\). Si la formule vaut pour un
\(t\le k-2\), alors
\[
3U^t(n_k)+1=2\bigl(5\cdot3^{t+1}\cdot2^{k-t-1}-1\bigr).
\]
Le facteur entre parenthèses est impair : \(5\cdot3^{t+1}\) est impair et
l'exposant de \(2\) vaut au moins \(1\). La valuation est donc \(1\), et
\(U^{t+1}\) a la forme annoncée. Pour \(1\le t\le k-1\),
\(3^t>2^t\), donc \(U^t(n_k)>n_k\).

Modulo \(8\), \(3^2\equiv1\). Si \(k\) est impair, \(3^k\equiv3\) et
\(5\cdot3^k-1\equiv6\pmod8\), valuation \(1\). Si \(k\) est pair,
\(3^k\equiv1\) et \(5\cdot3^k-1\equiv4\pmod8\), valuation \(2\).

Enfin \(U^{k-1}(n_k)=10\cdot3^{k-1}-1\), donc
\(3U^{k-1}(n_k)+1=2(5\cdot3^k-1)\) et la valuation de ce nombre est
\(1+\varepsilon(k)\). \(\square\)

Le préfixe \(t\le k-1\) est la propriété de Syracuse rappelée au §0, et
aussi le calcul (i) déjà écrit pour \(T\) avec partie impaire \(5\). La
valuation modulo \(8\) et l'expression de \(U^k\) sont le pas manquant
entre cet entier pair \(5\cdot3^k-1=T^k(n_k)\) et le prochain impair.

## 2. La sortie reste au-dessus du départ (B15)

**Proposition.** \(\tau(n_2)=2\), avec \(U(n_2)=29\) et \(U^2(n_2)=11\).
Pour tout \(k\ge3\), \(U^k(n_k)>n_k\), donc \(\tau(n_k)\ge k+1\).

**Preuve.** \(n_2=19\), \(3\cdot19+1=58=2\cdot29\) et
\(3\cdot29+1=88=8\cdot11\). Donc \(U^2(n_2)=11<19\) et le pas précédent
vaut \(29>19\).

Pour \(k\ge4\), \(\varepsilon(k)\le2\), donc il suffit de minorer par la
division par \(4\) :
\[
\frac{5\cdot3^k-1}{4}>5\cdot2^k-1
\iff 3^k+\frac35>2^{k+2}.
\]
Or \(3^4=81>64=2^6\). Si \(3^k>2^{k+2}\), alors
\(3^{k+1}>3\cdot2^{k+2}>2^{k+3}\). Ainsi \(3^k>2^{k+2}\) pour \(k\ge4\),
et l'inégalité stricte suit. Pour \(k\) impair la vraie division est par
\(2\), donc la valeur est encore plus grande.

Pour \(k=3\), \(\varepsilon=1\) et la minoration par \(4\) est fausse :
\((5\cdot27-1)/4=33{,}5<39\). Le calcul direct est
\(U^3(n_3)=(5\cdot27-1)/2=67>39=n_3\). \(\square\)

Les pas \(1\le t\le k-1\) étaient déjà au-dessus. Avec le pas \(k\),
aucun des \(k\) premiers itérés ne descend. C'est un cran après la
propriété de Syracuse, qui ne contrôle que \(t\le k-1\).

## 3. Jonction de \(k\) impair et de \(k+1\)

**Proposition.** Si \(k\ge1\) est impair, alors
\[
U^{k+1}(n_k)=U^{k+1}(n_{k+1})=\frac{5\cdot3^{k+1}-1}{4}.
\]
Si de plus \(k\ge3\), cette valeur commune est \(>n_{k+1}>n_k\), les
orbites coïncident à partir du pas \(k+1\), et
\(\tau(n_k)\ge\tau(n_{k+1})\ge k+2\).

**Preuve.** Ici \(\varepsilon(k)=1\), donc \(U^k(n_k)=(5\cdot3^k-1)/2\) et
\[
3U^k(n_k)+1=\frac{5\cdot3^{k+1}-1}{2}.
\]
L'exposant \(k+1\) est pair, donc \(v_2(5\cdot3^{k+1}-1)=2\) et le
quotient par \(4\) est impair. La valuation du membre de gauche est \(1\),
et \(U^{k+1}(n_k)\) est le quotient annoncé. Le même quotient est
\(U^{k+1}(n_{k+1})\) par le lemme du §1 appliqué à l'indice pair \(k+1\).

Pour \(k\ge3\), l'indice \(k+1\ge4\) tombe sous la proposition du §2 :
\(U^{k+1}(n_{k+1})>n_{k+1}\). Et
\(n_{k+1}=2n_k+1>n_k\). Les orbites sont égales à partir du rang \(k+1\).
Pour \(1\le t\le k\), \(U^t(n_k)>n_k\). Pour
\(k+1\le t<\tau(n_{k+1})\), la valeur commune est \(\ge n_{k+1}>n_k\).
Donc \(\tau(n_k)\ge\tau(n_{k+1})\). Si \(\tau(n_{k+1})=+\infty\), cette
queue ne descend jamais sous \(n_{k+1}\), donc jamais sous \(n_k\), et
\(\tau(n_k)=+\infty\). La borne \(k+2\) est le §2 à l'indice
\(k+1\). \(\square\)

Le cas \(k=1\) montre que l'hypothèse \(k\ge3\) est nécessaire pour
l'ordre des temps : \(n_1=9\), \(U(9)=7<9\), donc \(\tau(n_1)=1\), tandis
que \(\tau(n_2)=2\). L'identité de jonction, elle, vaut déjà :
\(U^2(9)=U^2(19)=11\).

La valeur \((5\cdot3^{k+1}-1)/4\) est celle du théorème 4 de
Wiltrout–Landquist, pour \(b=5\equiv1\pmod4\) et leur indice pair
\(k+1\) : les deux orbites de Terras s'y rejoignent. Leur énoncé compare
les temps d'atteinte de \(1\), pas les temps de première descente sous
\(U\). Le décompte accéléré, exactement \(k+1\) pas des deux côtés, vient
des valuations \(1\) et \(2\) du §1. Il n'ajoute pas de trajectoire
au-delà de ce point.

## 4. Le second bloc, de longueur variable

La formule dont la valuation ne dépend que de la parité de \(k\) s'arrête
au pas \(k\). Elle se prolonge d'un second bloc. La longueur de ce bloc
et l'exposant extrait à sa sortie dépendent de \(k\). La revue
`6082611497` refuse la lecture « aucun prolongement explicite n'existe ».
Les états ci-dessous sont ce prolongement. Aucun entier fixe n'est égal
à \(U^{k+2}(n_k)\) pour tout impair \(k\) : les valeurs \(19\) et \(1367\)
diffèrent.

**Proposition.** Soit \(k\ge1\) impair et
\(L=v_2(5\cdot3^k+1)-1\). Alors \(L\ge2\). Pour \(0\le s<L\),
\[
U^{k+s}(n_k)=\frac{3^s(5\cdot3^k+1)}{2^{s+1}}-1.
\]
Si de plus \(k\ge3\), ces valeurs sont \(>n_k\), donc
\(\tau(n_k)\ge k+L\), et la même borne vaut pour \(\tau(n_{k+1})\).
Par ailleurs
\[
U^{k+2}(n_k)=\frac{5\cdot3^{k+2}+1}{2^{v_2(5\cdot3^{k+2}+1)}}.
\]
Cette valuation vaut \(3\) si \(L\ge3\), et elle est \(\ge4\) si \(L=2\).
À la sortie du bloc, avec \(m=(5\cdot3^k+1)/2^{L+1}\) impair,
\[
U^{k+L}(n_k)=\frac{3^Lm-1}{2^{v_2(3^Lm-1)}}.
\]

**Preuve.** Comme \(k\) est impair, \(3^k\equiv3\pmod8\), donc
\(5\cdot3^k+1\equiv0\pmod8\) et \(L\ge2\). Le §1 donne
\(U^k(n_k)+1=(5\cdot3^k+1)/2\), de valuation \(L\).

Si \(x\equiv3\pmod4\), alors \(v_2(x+1)\ge2\), donc \(v_2(3x+1)=1\) et
\(U(x)+1=(3/2)(x+1)\). Chaque tel pas diminue la valuation de \(1\).
Le cas \(s=0\) est le §1. Supposons la forme annoncée à un indice
\(s\le L-2\). Alors \(v_2(U^{k+s}(n_k)+1)=L-s\ge2\), donc cet état est
\(\equiv3\pmod4\), et l'état d'indice \(s+1\) a la même forme. Cela donne
la formule pour \(0\le s<L\). Le quotient est entier parce que
\(v_2(5\cdot3^k+1)=L+1>s\).

Pour \(k\ge3\) et \(s=0\), le §2 donne \(U^k(n_k)>n_k\). Pour
\(1\le s<L\),
\[
U^{k+s}(n_k)+1=(3/2)^s\bigl(U^k(n_k)+1\bigr)>U^k(n_k)+1,
\]
donc \(U^{k+s}(n_k)>n_k\). Les pas \(1\le t\le k+L-1\) restent au-dessus
de \(n_k\), et \(\tau(n_k)\ge k+L\).

Le pas \(k+1\) est la jonction \(y\) du §3, avec \(y>n_{k+1}\) et
\(v_2(y+1)=L-1\). Si \(L\ge3\), les pas suivants jusqu'à l'indice
\(k+L-1\) sont encore des multiplications par \(3/2\) : l'état y est
\((3/2)^{t-k-1}(y+1)-1\), et \((3x+1)/2>x\) dès que \(x>1\). Ces états
sont donc \(>y>n_{k+1}\). Les pas \(1\le t\le k+1\) de \(n_{k+1}\) sont
déjà au-dessus par le §2. Si \(L=2\), il n'y a pas de pas intermédiaire
entre la jonction et l'indice \(k+1\). Dans les deux cas,
\(\tau(n_{k+1})\ge k+L\).

L'identité en \(k+2\) est un pas de \(U\) appliqué à \(y\) :
\(3y+1=(5\cdot3^{k+2}+1)/4\). Si \(L\ge3\), alors \(y\equiv3\pmod4\),
la valuation extraite sur \(3y+1\) est \(1\), et
\(v_2(5\cdot3^{k+2}+1)=3\). Si \(L=2\), alors \(y\equiv1\pmod4\) et
cette valuation est au moins \(4\).

À l'indice \(s=L-1\), la valuation résiduelle est \(1\), donc l'état
\(x\) vérifie \(x+1=2\cdot3^{L-1}m\) avec \(m\) impair. Alors
\(3x+1=2(3^Lm-1)\), et le pas suivant est le quotient annoncé.
\(\square\)

**Exemples.** Pour \(k=3\), \(v_2(5\cdot27+1)=3\), donc \(L=2\) et
\(U^5(n_3)=19\). Pour \(k=5\), \(v_2(5\cdot243+1)=6\), donc \(L=5\) et
\(U^7(n_5)=1367\). Les exposants extraits au pas \(k+2\) sont \(6\) et
\(3\).

**Excès non borné, sans forcer le franchissement de \(k\).** Pour chaque
\(m\ge3\), le cycle 002 §2 donne un entier \(r\) avec
\(v_2(5\cdot3^r+1)\ge m\). Un tel \(r\) est impair : la congruence
entraîne \(5\cdot3^r\equiv-1\pmod8\), et \(3^r\equiv3\pmod8\) si et
seulement si \(r\) est impair. Comme \(5\cdot3^r+1\ge2^m\), on a
\(r\to\infty\) avec \(m\). Pour \(m\ge8\), \(3^3=27<(2^8-1)/5\), donc
\(r\ge5\). Alors \(L\ge m-1\) et \(\tau(n_r)-r\ge m-1\). L'excès
\(\tau-k\) n'est pas borné sur les impairs \(k\ge5\).

Il n'en suit pas que \(\tau>2k\). La minoration dépasse \(k\) seulement
si \(L>k\), ce qui n'est pas montré. Le témoin \(r=757\) a la valuation
\(16\), donc \(L=15\) et \(k+L=772<2\cdot757\). Le temps complet calculé
au §5 vaut \(1840\), qui dépasse \(1514\), mais c'est une valeur finie.

**Portée.** Le §4 de Wiltrout–Landquist, tel qu'il a été lu, laisse
ouverte une formule du temps total de Terras jusqu'à \(1\). Ce temps
n'est pas \(\tau\). Cette lacune n'interdit pas une formule de première
descente, et elle n'en donne pas une. La formule uniforme en la parité
s'arrête au pas \(k\). Le bloc suivant a une longueur \(L(k)\) et un
exposant de sortie \(v_2(3^Lm-1)\), tous deux variables. Poursuivre
au-delà reprend la dynamique générale de \(U\). Aucune formule complète
de \(\tau\) n'est obtenue ici.

## 5. La comparaison à \(2k\)

**X28.** L'inégalité \(\tau(n_k)\le2k\) pour tout \(k\ge2\) est fausse :
\(\tau(n_5)=13>10\). La trajectoire est
\(159,239,359,539,809,607,911,1367,2051,3077,577,433,325,61\).
Le témoin est entier. Il ne dit pas que l'excès revient pour des \(k\)
arbitrairement grands. La borne \(k+L\) du §4 non plus.

Le script calcule \(\tau(n_k)\) pour \(2\le k\le1000\). Dans cet intervalle,
\(\tau\le2k\) exactement pour les vingt-cinq couples
\[
\begin{align*}
&(2,2),\ (3,5),\ (4,5),\ (7,14),\ (8,14),\ (11,21),\ (12,21),\\
&(17,32),\ (18,32),\ (19,31),\ (20,31),\ (27,54),\ (28,51),\\
&(52,104),\ (73,145),\ (74,142),\ (83,152),\ (84,152),\\
&(206,388),\ (207,388),\ (208,388),\ (232,463),\ (235,463),\\
&(236,462),\ (324,648).
\end{align*}
\]
Partout ailleurs dans l'intervalle, \(\tau>2k\). Le rapport maximal y est
\(\tau(n_{21})/21=110/21\). Le plus grand \(k\le1000\) avec \(\tau\le2k\)
est \(324\), et \(\tau(n_{324})=648\).

Pour \(k=757\), \(v_2(5\cdot3^{757}+1)=16\) et
\(\tau(n_{757})=\tau(n_{758})=1840\). Comme \(2\cdot757=1514<1840\), ce
témoin dépasse \(2k\). La borne du second bloc ne l'explique pas :
\(k+L=772\). C'est une valeur dans le relevé, pas une infinité.

Ce segment est un contrôle fini. Il ne prouve ni que \(324\) est le
dernier, ni que \(\tau>2k\) pour tout \(k>324\), ni que l'excès est
infini. Aucune formule lue sur ces valeurs n'a été promue au rang de
preuve.

## 6. Statut

B15 est prouvé. C'est une comparaison de taille sur un préfixe déjà
publié, plus le transport de la jonction de Terras vers \(U\). Le §4
y ajoute le second bloc : pour \(k\) impair \(\ge3\),
\(\tau(n_k)\ge k+v_2(5\cdot3^k+1)-1\), et \(\tau-k\) n'est pas borné sur
cette sous-suite. Ce n'est pas une borne supérieure de \(\tau\), ni
\(\tau>2k\) infiniment souvent, ni une exclusion de trajectoire
divergente. La question de l'agenda reste **INCONCLUSIVE** sur ses deux
branches : pas de forme close jusqu'à la descente, pas de théorème
d'excès au-dessus de \(2k\). X28 réfute seulement la majoration
universelle par \(2k\). Le §4 de Wiltrout–Landquist ne ferme aucune des
deux branches.

Antériorité utilisée : Wiltrout–Landquist, théorèmes 1 et 4 et §4, lus
sur le rendu ; la puce Syracuse de Wikipedia, lue, non primaire ; le
calcul (i) du fichier à partie impaire \(5\) ; A2 pour le cas \(b=1\),
non repris. Le préprint Zenodo sur la « résistance » modulaire, rencontré
dans la recherche, répète le préfixe \(t\le m-1\) pour \(n=2^mq-1\). Il
n'a pas été lu et n'est pas une prémisse.

## 7. Revue `6082502361`

Revue indépendante sur le SHA
`c5ab64394914d91280442ab479f264a840dd5942` (PR #27), c'est-à-dire sur
l'exclusion de \(2+2^{66}\) au rang \(2\). Le correctif est confirmé :
valuations croissantes \(1,66,96\), dénominateur impair, borne B14, et
les trois candidats. Pour \(2+2^{66}\), \(v_2(A_2)=74\neq96\) par les cinq
doublements depuis \(v_2(3^2-1)=3\). Aucune correction.

La revue ajoute un résidu compatible avec les deux rangs, sans en faire
une correction : \(b=1\) et \(a=2+2^{66}u\) avec \(u=956973825\). Ce
résidu est impair. Ici \(v_2(a-2b)=66\) et, avec
\(A_2=3^{64}a-P_2\), \(v_2(A_2)=96\). Cela montre seulement que les deux
conditions nécessaires peuvent être satisfaites ensemble. L'irrationalité
du signe moins reste ouverte, déjà au cycle 009. Ce mot n'est pas rouvert.
Rozier, arXiv:1805.00133, §3.3, conjecture 1, est de nouveau cité comme
conjecture sur \(\mathbb Z_2\). Le PDF n'est pas rouvert et n'est pas une
prémisse.

## 8. Mises à jour de la mémoire

- `proved.md` : B15, comparaison de taille, puis second bloc après la
  revue `6082611497`.
- `counterexamples.md` : X28. La borne \(k+L\) ne prouve pas l'infinité
  de l'excès sur \(2k\).
- `prior_art.md` : Wiltrout–Landquist, rendu lu, PDF non empreinté. Leur
  §4 ne porte pas sur \(\tau\).
- `abandoned.md` : ne pas chercher une formule complète de \(\tau(n_k)\)
  au-delà du second bloc, ni une preuve que \(\tau>2k\) infiniment souvent.
- `agenda.md` : question suivante sur l'axe C, non entamée tant que cette
  correction n'est pas revue.
- `reviews.md` : revues `6082502361` et `6082611497`.

## 9. Prochaine question

Axe **C**, un seul énoncé. Le préfixe de \(5\cdot2^k-1\), second bloc
compris, ne contraint pas les trajectoires arbitraires. Le prolonger
au-delà de l'exposant \(v_2(3^Lm-1)\) est la dynamique générale de \(U\).
Ce n'est pas la question suivante.

Lire l'énoncé primaire de Berg–Meinardus (1994 ou 1995) qui rend la
conjecture équivalente à une équation fonctionnelle holomorphe. Cette
équivalence donne-t-elle une contrainte sur une trajectoire individuelle
qui ne soit pas déjà B12, ou bien est-elle une reformulation globale sans
nouveau lemme de descente ? Si le texte primaire n'est pas obtenu,
s'arrêter et consigner l'antériorité comme non vérifiée. Ne pas rouvrir
la famille \(5\cdot2^k-1\), le signe moins, le mot du cycle 006, B10,
B13, X21, ni les théorèmes 4.2.7 et 4.3.10 de Mori.

## 10. Reproduire

```sh
python3 research/checks/cycle010_accelerated_descent.py
```

Sortie attendue : cinq lignes `PASS`. Elles couvrent le préfixe et la
sortie pour \(2\le k\le60\), la jonction et l'ordre des temps pour les
impairs de \(3\) à \(59\), les trois valuations \(4,3,6\), le second
bloc pour les impairs de \(1\) à \(999\) avec \(\tau\ge k+L\) dès
\(k\ge3\), les valeurs \(19\), \(1367\) et
\(\tau(n_{757})=\tau(n_{758})=1840\), et le relevé \(2\le k\le1000\).
Le relevé n'est pas la preuve de B15. L'infinité de l'excès sur \(2k\)
n'est pas un contrôle du script.

## 11. Revue `6082611497`

Revue indépendante sur le SHA
`462014b889458b90b481bf567cfcd57a0ddb89be` (PR #27), c'est-à-dire sur
B15. Les §§1–3 sont confirmés, ainsi que X28 et la trajectoire de
\(n_5\). Trois corrections, intégrées ci-dessus. Ce n'est pas un nouveau
cycle.

La convention \(\tau=+\infty\) est ajoutée à la définition. Sans elle,
la comparaison \(\tau(n_k)\ge\tau(n_{k+1})\) supposait qu'un temps de
descente existe. Le cas infini est le §3 : la queue commune ne peut pas
descendre sous \(n_k\) si elle ne descend pas sous \(n_{k+1}\).

La phrase « la formule uniforme s'arrête là », lue comme une impossibilité
de prolonger le préfixe, est fausse. Le §4 donne les états
\(0\le s<L\) et la sortie \(U^{k+L}\). Pour \(k=3\), le pas suivant la
jonction vaut \(19\). Pour \(k=5\), il vaut \(1367\). La longueur \(L\)
et l'exposant extrait varient avec \(k\). Comme les solutions du cycle
002 §2 sont impaires, \(\tau(n_k)-k\) n'est pas borné. Le témoin
\(r=757\) a \(L=15<757\), donc cette minoration ne dépasse pas \(k\).

Le §4 de Wiltrout–Landquist ne suffit pas à exclure une formule de
première descente : il porte sur le temps total. Le PDF brut reste non
empreinté. La revue signale que le texte intégral a répondu HTTP 403 et
ne confirme pas la numérotation des théorèmes 1 et 4. Le rendu déjà lu
n'est pas rouvert, et l'identité de jonction est revérifiée sans ce
numéro. Aucune source nouvelle n'est une prémisse.

Le contrôle indépendant, en entiers exacts, est le script : impair
\(1\le k\le999\) pour la formule, \(k\ge3\) pour \(\tau\ge k+L\), et
\(\tau(n_{757})=\tau(n_{758})=1840\). Ce segment n'est pas la preuve.
L'existence d'une formule complète de \(\tau\), et l'infinité des \(k\)
avec \(\tau>2k\), restent ouvertes. La question de Berg–Meinardus n'est
pas entamée.
