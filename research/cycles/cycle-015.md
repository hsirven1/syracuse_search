# Cycle 015 — aucune classe ne se contracte dans elle-même en temps borné

Date : 27 novembre 2026. Axe **A**.
Branche : `research/memory`. Script : [`../checks/cycle015_self_contraction.py`](../checks/cycle015_self_contraction.py).

**Verdict.** Pour l'application \(U(n)=(3n+1)/2^{v_2(3n+1)}\), il n'existe
aucun module \(m\ge 2\), aucun résidu \(a\) et aucune borne \(T\) tels
que tout entier \(n>1\) congru à \(a\) modulo \(m\) admette un temps
\(t\le T\) avec \(U^t(n)<n\) et \(U^t(n)\equiv a\pmod m\) (B21). Aucune
orbite divergente n'est exclue. Ce n'est pas une preuve de Syracuse.

## 0. Revue traitée, fenêtre

La revue `6093548562` porte le marqueur `SYRACUSE_INDEPENDENT_REVIEW`
et le SHA `8428d6cf3a98f91dcc2bfa102002c0de829c647e`, tête de la PR #27
au début de ce cycle. Elle confirme le correctif X36. Pour
\(f(N)=N+1\), la définition lue au cycle 014 donne
\(\mathrm{Col}_{\min}(N)\le N<f(N)\) pour tout \(N\ge 1\). Aucune
correction. Le cycle 014 n'est pas réécrit.

La fenêtre de douze cycles était fermée jusqu'au 27 novembre 2026 à
22:01 UTC : le commit `0c90981` est du 26 novembre à 22:00:44 UTC. Ce
cycle commence après cet instant.

## 1. Porte d'antériorité

**Candidat 1.** Un seul vecteur de valuations, constant sur une classe
modulo \(2^L\), envoie toute la classe dans elle-même par une affinité
de coefficient \(3^t 2^{L-S}\), avec une descente stricte.

**Obstacle.** Sans retour dans la classe, une descente uniforme ne
réduit pas la classe à un segment fini.

**Intérêt.** Un tel vecteur serait le cas le plus simple d'un
certificat de descente sur une progression.

**Résultat le plus proche.** Le codage de Terras et d'Everett (A1) :
\(U^t(n)=(3^t n+M)/2^S\) sur le cylindre du vecteur. X4 dit déjà qu'un
pas de l'application raccourcie ne conserve pas la classe modulo
\(2^k\). Le théorème C de Terras, tel que Lagarias le rapporte dans
l'enquête de 1985 (texte du PDF d'enquête, pas l'article de 1976),
fixe le temps d'arrêt sur une classe admissible. Il ne demande pas que
l'image revienne dans la classe. Terras (1976) et Everett (1977) ne
sont pas rouverts.

**Écart.** Le coefficient \(3^t 2^{L-S}\) a pour valuation \(L-S\).
Si \(1\le S\le L\), elle est strictement plus petite que \(L\), donc
le pas en la variable de la classe n'est pas nul modulo \(2^L\). Si
\(S=0\), l'itéré vaut \(3^t n+(3^t-1)/2>n\). Si \(S>L\), le vecteur
n'est pas constant sur toute la classe : \(2^S\) devrait diviser
\(3^t 2^L\).

**Classement.** COROLLAIRE DIRECT du codage, confiance haute pour
cette obstruction arithmétique. Elle n'est pas un théorème nouveau.

**Décision.** NO-GO pour une preuve présentée comme originale. Le
travail du cycle est l'union finie de vecteurs, c'est-à-dire
l'énoncé quantifié de la question.

**Candidat 2.** Il existe \(m\ge 2\), un résidu \(a\) et une borne
\(T\) tels que tout \(n>1\) congru à \(a\) modulo \(m\) admette un
\(t\le T\) avec \(U^t(n)<n\) et \(U^t(n)\equiv a\pmod m\).

**Obstacle.** Tao règle presque toute la classe, pas la classe
entière. Une contraction uniforme dans la classe réduirait cette
classe à un segment fini.

**Intérêt.** Une réponse positive prouverait la conjecture sur une
progression infinie. Une réponse négative ferme ce certificat.

**Résultat le plus proche.** A3 : pour tout \(s\ge 1\), le cylindre
\(y=2^s q-1\) de `EXACT_STOPPING_TIME_BASELINE.md` a un temps de
première descente égal à \(s\). Le théorème `no_uniform_descent_bound`
interdit un horizon uniforme pour tous les entiers, sous l'application
raccourcie, sans condition de retour. Ni l'un ni l'autre ne parle du
retour dans une classe fixée. La moitié « résidu différent de \(1\) »
est un comptage. Elle n'a pas été trouvée comme théorème nommé. Le
texte d'enquête de Lagarias, au théorème C, ne contient pas la
négation cherchée.

**Écart.** L'énoncé demande un temps uniforme et un retour dans la
même classe, pour \(U\), sur une seule progression. A3 donne le
contraire sur un cylindre mince : le temps de descente y est grand.
Le pont du §4 place un tel cylindre dans l'orbite d'un entier de la
classe \(1\pmod m\) lorsque \(4\) divise \(m\).

**Classement.** POTENTIELLEMENT NOUVEAU pour la négation complète,
confiance moyenne. La moitié élémentaire et le cylindre classique ne
sont pas revendiqués. Terras (1976) et Everett (1977) n'ont pas été
relus : l'enquête de Lagarias ne remplace pas ces articles. Aucune
revendication de découverte au-delà de cette portée.

**Décision.** GO. Une seule expérience : prouver la négation.

## 2. Deux lemmes de trajectoire

**Lemme de division.** Si \(v_2(n-1)\ge 3\), alors \(v_2(3n+1)=2\) et
\[
U(n)-1=\frac{3(n-1)}{4}.
\]
En effet, \(n-1=2^v t\) avec \(v\ge 3\) et \(t\) impair. Alors
\(3n+1=4(1+3\cdot 2^{v-2}t)\). L'entier \(1+3\cdot 2^{v-2}t\) est
impair, donc la valuation vaut exactement \(2\), et
\(U(n)=1+3\cdot 2^{v-2}t\).

**Lemme de montée.** Soient \(s\ge 2\) et \(q\) un entier positif tels
que \(3^s q\equiv 1+2^s\pmod{2^{s+1}}\) et
\((4^s-3^s)q>2^s-1\). Posons \(y=2^s q-1\). Pour \(0\le r\le s-1\),
\[
U^r(y)=3^r 2^{s-r}q-1,
\]
et cette valeur est strictement supérieure à \(y\) si \(r\ge 1\). De
plus \(U^s(y)=(3^s q-1)/2^s<y\). En particulier, pour
\(1\le r\le s-2\), \(U^r(y)\equiv 3\pmod 4\).

La forme au rang \(0\) est la définition de \(y\). Si elle vaut au
rang \(r\le s-2\), alors \(s-r\ge 2\) et
\[
3U^r(y)+1=2\bigl(3^{r+1}2^{s-r-1}q-1\bigr).
\]
Le facteur entre parenthèses est impair, donc la valuation vaut \(1\)
et le rang \(r+1\) a la forme annoncée. Pour \(1\le r\le s-1\),
\(3^r>2^r\), donc \(U^r(y)>y\). Au dernier pas,
\(3U^{s-1}(y)+1=2(3^s q-1)\) et \(v_2(3^s q-1)=s\), d'où la valeur de
\(U^s(y)\). L'inégalité stricte finale est l'hypothèse sur \(q\). Pour
\(r\le s-2\), le facteur \(2^{s-r}\) est divisible par \(4\), donc
\(U^r(y)\equiv -1\pmod 4\).

Un tel \(q\) existe : \(3^s\) est inversible modulo \(2^{s+1}\), et
\(q_s\equiv(1+2^s)(3^s)^{-1}\) convient pour tout représentant assez
grand de cette classe, car \(4^s>3^s\). C'est le cylindre déjà écrit
dans `EXACT_STOPPING_TIME_BASELINE.md`. La preuve ci-dessus n'en
dépend pas.

## 3. Résidu différent de \(1\)

Soit \(m\ge 2\). On prend le résidu \(r\) dans \(\{0,1,\ldots,m-1\}\).
Si \(r\neq 1\), soit \(n_0=r\) lorsque \(r>1\), et \(n_0=m\) lorsque
\(r=0\). Alors \(n_0>1\) et \(n_0\equiv r\pmod m\). Tout entier
positif congru à \(r\) modulo \(m\) est au moins \(n_0\). Aucun itéré
ne peut donc être à la fois strictement plus petit que \(n_0\) et
dans la classe. Le triple \((m,r,T)\) échoue pour toute borne \(T\).

Le témoin \(n_0=3\), classe \(3\pmod 4\), a pour orbite \(3\to 5\to 1\).
Aucun terme positif plus petit que \(3\) n'est congru à \(3\) modulo
\(4\). Le script contrôle le même comptage pour \(2\le m\le 40\).

## 4. Classe \(1\pmod m\)

**Cas où \(4\) ne divise pas \(m\).** Soit \(s\ge 2\) et \(y=2^s q-1\)
le cylindre du lemme de montée. On cherche \(y\equiv 1\pmod m\). Le
module \(2^{2s+1}\) du cylindre et \(m\) ont pour pgcd \(1\) ou \(2\).
Le représentant de base est impair, comme \(1\). Le théorème chinois
donne une infinité de solutions, et la condition de taille sur \(q\)
est vraie pour les grandes. Pour un tel \(y\), le lemme dit
\(U^t(y)>y\) pour tout \(1\le t<s\). On choisit \(s>T\). Aucun temps
\(t\le T\) ne descend. Le script en donne cinq : pour \(m=6\) et
\(s=5\), \(y=2911\), et \(U^5(2911)=691<2911\).

**Cas où \(4\) divise \(m\).** Écrivons \(m=2^L M\) avec \(M\) impair
et \(L\ge 2\). Si \(L\) est impair, posons \(j=(L-1)/2\) et
\(v_0=L\). Si \(L\) est pair, posons \(j=L/2\) et \(v_0=L+1\). Dans
les deux cas \(v_0=2j+1\ge 3\) et \(j\ge 1\).

Soit \(s\ge 2\), et soit \(q\) un entier du lemme de montée tel que
\[
2^{s-1}q\equiv 1\pmod{3^j M}.
\]
Le module \(3^j M\) est impair, donc premier avec \(2^{s+1}\). Le
théorème chinois s'applique, et l'on peut prendre \(q\) assez grand
pour la condition de taille. Posons
\[
t=\frac{2^{s-1}q-1}{3^j}.
\]
C'est un entier. Il est impair, car le numérateur est impair et
\(3^j\) est impair. Comme \(3^j M\) divise le numérateur, \(M\) divise
\(t\). Posons
\[
n=1+2^{v_0}t.
\]
Alors \(2^L M\) divise \(n-1\), donc \(n\equiv 1\pmod m\), et \(n>1\).

On applique le lemme de division \(j\) fois. Au départ,
\(v_2(n-1)=v_0=2j+1\ge 3\). Après \(i\) pas, \(0\le i<j\),
\[
v_2\bigl(U^i(n)-1\bigr)=v_0-2i=2(j-i)+1\ge 3,
\]
donc le pas suivant divise exactement par \(4\), et
\[
v_2\bigl(U^{i+1}(n)-1\bigr)=v_0-2i-2.
\]
Au rang \(j\),
\[
y:=U^j(n)=1+2\cdot 3^j t=2^s q-1.
\]
Pour \(1\le i\le j\), la valuation \(v_0-2i\) est au plus \(v_0-2\).
Si \(L\) est impair, \(v_0-2=L-2<L\). Si \(L\) est pair,
\(v_0-2=L-1<L\). Le cofacteur \(3^i t\) est impair. Donc
\(2^L\) ne divise pas \(U^i(n)-1\), et \(U^i(n)\not\equiv 1\pmod m\).

Sur la montée, le lemme donne, pour \(1\le r\le s-2\),
\(U^r(y)\equiv 3\pmod 4\). Comme \(4\) divise \(m\),
\(U^r(y)\not\equiv 1\pmod m\). Le temps global de cet itéré est
\(j+r\le j+s-2\).

Ainsi, pour tout \(t\le j+s-2\), \(U^t(n)\not\equiv 1\pmod m\). On
choisit \(s\ge T-j+2\). Aucun temps \(t\le T\) ne satisfait les deux
conditions. Le script contrôle huit modules, dont \(m=4\), \(s=6\),
\(n=3497\) : les cinq premiers itérés sont congrus à \(3\) modulo
\(4\), et le premier retour dans la classe au-dessous du départ est
\(U^8(3497)=701\).

## 5. Énoncé

**B21.** Soit \(U(n)=(3n+1)/2^{v_2(3n+1)}\). Il n'existe pas d'entiers
\(m\ge 2\), \(a\) et \(T\ge 1\) tels que, pour tout entier \(n>1\)
congru à \(a\) modulo \(m\), il existe \(t\le T\) avec \(U^t(n)<n\) et
\(U^t(n)\equiv a\pmod m\).

Les §§3 et 4 couvrent tous les résidus. Le résidu est lu dans
\(\{0,1,\ldots,m-1\}\).

## 6. Portée

Le certificat visé est fermé : aucune progression arithmétique ne
revient dans elle-même, strictement plus bas, en un temps uniforme.
Cela ne force aucun entier particulier à atteindre \(1\). Une orbite
peut quitter la classe, ou y revenir seulement après un temps qui
grandit avec le départ. Le cylindre de A3 et le codage de Terras ne
sont pas redémontrés comme résultats nouveaux. La moitié \(r\neq 1\)
est un comptage. Le pont du §4 est la partie qui n'est pas ce
comptage ; sa nouveauté reste au classement du §1.

## 7. Mises à jour de la mémoire

- `proved.md` : B21.
- `counterexamples.md` : X37, trois témoins des trois cas.
- `hypotheses.md` : H10, fermée.
- `prior_art.md` : porte du cycle, sans rouverture de Terras.
- `abandoned.md` : ne pas relancer cette contraction uniforme.
- `agenda.md` : question suivante, axe B.
- `reviews.md` : revue `6093548562`.

## 8. Prochaine question

Axe **B**, après la relecture de ce cycle et après la fenêtre
ci-dessous. Les cycles 010 à 015 ne retirent aucune orbite
divergente. Ne pas rouvrir B21, ni Tao, ni les potentiels, ni le
signe moins, ni le mot du cycle 006, ni \(5\cdot 2^k-1\).

Lire d'abord l'énoncé primaire de Steiner (1977) sur l'absence de
\(1\)-cycle non trivial. La question est la suivante. Existe-t-il un
entier \(R\ge 1\) tel que toute orbite positive dont chaque run
impair a une longueur au plus \(R\) repasse strictement sous son
départ ? Un mot périodique de runs bornés est un cycle : ne pas le
traiter par une recherche bornée, et ne pas redémontrer les bornes de
Simons–de Weger si l'énoncé lu les contient déjà. Si Steiner exclut
déjà toute orbite à runs bornés, et pas seulement les cycles, ne pas
le redémontrer.

Le cycle 015 est le douzième de la fenêtre dont le plus ancien est
le cycle 004. Le premier commit de ce cycle est `8bc44f7`, du
26 novembre 2026 à 23:16:52 UTC. Ne pas ouvrir le cycle 016 avant
une relecture indépendante de B21, ni avant le 27 novembre 2026 à
23:17 UTC.

## 9. Reproduire

```sh
python3 research/checks/cycle015_self_contraction.py
```

Sortie attendue : trois lignes `PASS`, puis une ligne `EXAMPLES`.
La première vérifie, pour \(2\le m\le 40\) et chaque résidu autre que
\(1\), qu'aucun positif plus petit que le minimum de la classe n'y
appartient. La deuxième construit, pour cinq modules non divisibles
par \(4\), un cylindre de A3 dans la classe \(1\) et en contrôle la
montée. La troisième construit le pont pour huit modules divisibles
par \(4\) et vérifie l'absence de retour avant le temps \(j+s-1\).
La ligne d'exemples contient `4:3497` et `6` n'y figure pas : le
cylindre direct \(2911\) pour \(m=6\), \(s=5\), est contrôlé par la
deuxième ligne, pas imprimé. Ces contrôles ne remplacent pas les
quantificateurs des §§3 et 4.
