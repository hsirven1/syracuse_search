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
\(j+r\), avec \(j+1\le j+r\le j+s-2\). Si \(s=2\), cet intervalle
est vide.

Les temps \(1\le i\le j\) sont déjà hors de la classe, par la
valuation. Donc, pour tout \(1\le t\le j+s-2\),
\(U^t(n)\not\equiv 1\pmod m\). Le rang \(0\) reste dans la classe :
\(U^0(n)=n\). Ce n'est pas une descente. On choisit
\(s\ge\max(2,T-j+2)\), de sorte que \(j+s-2\ge T\). Aucun temps
\(1\le t\le T\) n'est dans la classe, et le rang \(0\) ne descend
pas. Le script contrôle huit modules, dont \(m=4\), \(s=6\),
\(n=3497\) : les cinq premiers itérés sont congrus à \(3\) modulo
\(4\), et le premier retour dans la classe au-dessous du départ est
\(U^8(3497)=701\).

## 5. Énoncé

**B21.** Soit \(U(n)=(3n+1)/2^{v_2(3n+1)}\). Il n'existe pas d'entiers
\(m\ge 2\), \(a\) et \(T\ge 1\) tels que, pour tout entier \(n>1\)
congru à \(a\) modulo \(m\), il existe \(t\le T\) avec \(U^t(n)<n\) et
\(U^t(n)\equiv a\pmod m\).

Les §§3 et 4 couvrent tous les résidus. Le résidu est lu dans
\(\{0,1,\ldots,m-1\}\). La même formule définit \(U\) sur les pairs :
\(3n+1\) est alors impair, et \(U(n)=3n+1\). Le §3 compte les positifs
de la classe et n'évalue pas \(U\). Les classes sans impair restent
dans l'énoncé.

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

Axe **B**. Les formulations écrites ici avant la revue `6093792860`
sont fermées au §10. Ne pas les rouvrir. Ne pas rouvrir B21, ni Tao,
ni les potentiels, ni le signe moins, ni le mot du cycle 006, ni
\(5\cdot 2^k-1\), ni le cas \(R=1\).

Soit \(P(R)\) l'énoncé : toute orbite positive de \(T\) dont chaque
run impair a une longueur au plus \(R\) atteint \(1\). Si
\(R\le R'\), toute orbite admissible pour \(R\) l'est pour \(R'\),
donc \(P(R')\) implique \(P(R)\). L'existence d'un entier \(R\ge 2\)
tel que \(P(R)\) équivaut à \(P(2)\). En effet, \(P(2)\) est un cas
de cette existence. Inversement, si \(P(R)\) vaut pour un \(R\ge 2\),
l'emboîtement donne \(P(2)\). Si \(P(2)\) est fausse, la même orbite
appartient à chaque famille \(R\ge 2\). La lecture
universelle, « pour tout \(R\ge 2\), \(P(R)\) », est plus forte.
Une orbite qui contient un run de longueur \(3\) est hors de la
famille \(R=2\). Cette lecture n'est pas la question.

La question du cycle 016 est \(P(2)\). Lire d'abord l'énoncé
primaire de Steiner (1977) sur l'absence de \(1\)-cycle non trivial.
S'il exclut déjà toute orbite de runs de longueur au plus \(2\), et
pas seulement les cycles, ne pas le redémontrer. Une suite de
parités périodique dès le départ est déjà un cycle (§10) : ne pas
la chercher par force brute. Simons–de Weger n'est pas ouvert dans
ce correctif : ne pas identifier leur entier \(m\) avec la borne
\(R\), et ne pas redémontrer leurs bornes si le texte lu les
contient déjà.

Le cycle 015 est le douzième de la fenêtre dont le plus ancien est
le cycle 004. Le premier commit de ce cycle est `8bc44f7`, du
26 novembre 2026 à 23:16:52 UTC. Le §11 est un correctif, pas le
cycle 016. Ne pas ouvrir le cycle 016 avant une relecture
indépendante de ce correctif, ni avant le 27 novembre 2026 à
23:17 UTC.

## 9. Reproduire

```sh
python3 research/checks/cycle015_self_contraction.py
```

Sortie attendue : trois lignes `PASS`, une ligne `EXAMPLES`, puis
deux lignes `PASS`.
La première vérifie, pour \(2\le m\le 40\) et chaque résidu autre que
\(1\), qu'aucun positif plus petit que le minimum de la classe n'y
appartient. La deuxième construit, pour cinq modules non divisibles
par \(4\), un cylindre de A3 dans la classe \(1\) et en contrôle la
montée. La troisième construit le pont pour huit modules divisibles
par \(4\) et vérifie que les rangs \(1,\ldots,j+s-2\) sortent de la
classe. Deux lignes ensuite contrôlent le rang \(0\), le pont
\(s=2\), l'orbite de \(1\), le mot de runs de \(5\), et la descente
du cas \(R=1\). Cette dernière ligne contrôle aussi la formule
close jusqu'au premier pair, le terme impair \(T^2(1)\), le retour
immédiat dans la classe \(1\pmod 2\), et la montée stricte de
\(2911\) pour \(1\le t<5\). La ligne d'exemples contient `4:3497`
et `6` n'y figure pas : le cylindre direct \(2911\) pour \(m=6\),
\(s=5\), est contrôlé par la deuxième ligne, pas imprimé. Ces
contrôles ne remplacent pas les quantificateurs des §§3, 4, 10
et 11.

## 10. Revue `6093792860`

Revue indépendante sur le SHA
`c6737c04df5adfc6cde037a0f6904365c4f0595a` (PR #27). Ce n'est pas un
nouveau cycle. Le cycle 016 n'est pas ouvert.

B21 et les §§2–6 sont confirmés, puis revérifiés. Le résidu autre
que \(1\) n'a aucun positif plus petit que son minimum. Pour
\(4\nmid m\), le cylindre de montée se place dans la classe \(1\) et
son premier temps de descente est \(s\). Pour \(4\mid m\), le pont
puis ce cylindre évitent la classe pendant un temps arbitraire. Les
témoins restent \(n_0=3\), \(y=2911\) et \(n=3497\). Sur ce dernier,
\(U^5(3497)=13283\equiv 3\pmod 4\), \(U^6(3497)=19925\equiv 1\pmod 4\)
mais \(19925>3497\), et le premier retour strictement plus bas dans
la classe est \(U^8(3497)=701\). La nouveauté de B21 reste celle du
§1 : potentiellement nouvelle pour la négation complète, confiance
moyenne, Terras et Everett n'étant pas les prémisses du pont. Aucune
orbite divergente n'est exclue.

**Quantificateur.** La phrase « pour tout \(t\le j+s-2\),
\(U^t(n)\not\equiv 1\pmod m\) » est fausse au rang \(0\). Pour
\(n=3497\) et \(m=4\), on a \(j=1\), \(s=6\) et \(j+s-2=5\), mais
\(U^0(3497)=3497\equiv 1\pmod 4\). L'argument écrit couvrait déjà
\(1\le i\le j\) et \(1\le r\le s-2\). Le §4 dit maintenant
\(1\le t\le j+s-2\). Le rang \(0\) est le départ : il est dans la
classe, et il ne satisfait pas \(U^t(n)<n\). On prend
\(s\ge\max(2,T-j+2)\). Si \(s=2\), la montée \(1\le r\le s-2\) est
vide et le pont couvre \(1\le t\le j\). L'énoncé B21 ne change pas.

La formule de \(U\) reste celle du §5, y compris sur les pairs, où
\(U(n)=3n+1\). Le §3 ne l'évalue pas. Restreindre l'énoncé aux
classes qui contiennent un impair n'est pas nécessaire.

**X38.** Il n'existe aucun entier \(R\ge 1\) tel que toute orbite
positive de
\[
T(n)=\begin{cases}n/2&n\text{ pair},\\(3n+1)/2&n\text{ impair},\end{cases}
\]
dont chaque run impair a une longueur au plus \(R\), passe
strictement sous son départ. L'orbite de \(1\) est \(1\to 2\to 1\).
Le run impair issu de \(1\) a longueur \(v_2(2)=1\), et aucun entier
positif n'est strictement plus petit que \(1\).

Avec les départs \(n>1\), le cas \(R=1\) est déjà vrai, et il est
élémentaire. Si \(n\) est pair, \(T(n)=n/2<n\). Si \(n\) est impair
et si son premier run a longueur au plus \(1\), alors
\(v_2(n+1)=1\), donc \(n\equiv 1\pmod 4\), et
\(T^2(n)=(3n+1)/4<n\). On ne traite pas cette descente comme une
question ouverte.

Si tous les runs impairs de l'orbite ont longueur au plus \(1\),
l'orbite atteint \(1\). Soit \(n\) impair et \(r=v_2(n+1)\). Alors
\(r\ge 1\). La récurrence du pas impair donne
\[
T^i(n)+1=\frac{3^i(n+1)}{2^i}
\]
pour \(0\le i\le r\), c'est-à-dire jusqu'au premier terme pair,
inclus. En effet, la formule au rang \(0\) est \(n+1\). Si elle
vaut au rang \(i<r\), le membre de droite a la valuation \(r-i\ge 1\),
donc \(T^i(n)\) est impair, et le pas impair produit la formule au
rang \(i+1\). La formule vaut donc jusqu'au rang \(r\). À ce rang,
la valuation est nulle, donc \(T^r(n)\) est pair. Les rangs
\(0,\ldots,r-1\) du bloc initial sont impairs, et le rang \(r\) est
pair. La longueur du run initial est donc \(r\).

Cette formule ne décrit pas l'orbite au-delà du rang \(r\). Pour
\(n=1\), on a \(r=1\) et \(T(1)=2\), mais \(T^2(1)=1\) est impair.
On n'écrit pas que \(T^i(n)\) est impair exactement pour
\(0\le i<r\) sur l'orbite entière.

Si chaque run impair a longueur au plus \(1\), alors, pour chaque
terme impair \(m\) de l'orbite, le run qui en part a longueur
\(v_2(m+1)=1\), donc \(m\equiv 1\pmod 4\) et \(v_2(3m+1)\ge 2\). Le
terme impair suivant est \(U(m)\le(3m+1)/4\). Pour \(m>1\),
\((3m+1)/4<m\), donc \(U(m)<m\). La suite des impairs positifs décroît
jusqu'à \(1\). Ce fait est le codage d'un run de longueur \(1\),
déjà la définition \(r(M)=v_2(M+1)\) du cycle 002. Ce n'est pas un
résultat nouveau, et il ne dit rien pour \(R\ge 2\). X38 et cette
conclusion restent vrais.

**X39.** La phrase « un mot périodique de runs bornés est un cycle »
est fausse si le mot est la suite des longueurs de runs impairs.
L'orbite de \(5\) est \(5\to 8\to 4\to 2\to 1\to 2\to 1\to\cdots\).
Ses longueurs de runs impairs sont \(1,1,1,\ldots\), et \(5\) n'est
égal à aucun itéré ultérieur de cette liste.

Si le mot est la suite complète des parités, et s'il est périodique
de période \(p\) dès le rang \(0\), alors \(n=T^p(n)\). On montre
d'abord que \(k\) parités communes donnent \(v_2(n-m)\ge k\), la
valuation de \(0\) étant infinie.

Un pas de même parité baisse la valuation d'exactement un. Si \(n\)
et \(m\) sont pairs, \(T(n)-T(m)=(n-m)/2\). S'ils sont impairs,
\(T(n)-T(m)=3(n-m)/2\), et \(3\) est impair. La parité commune donne
déjà \(v_2(n-m)\ge 1\), donc
\(v_2(T(n)-T(m))=v_2(n-m)-1\).

Pour \(k=0\), il n'y a pas de condition. Si les \(k+1\) premières
parités de \(n\) et de \(m\) coïncident, l'hypothèse de récurrence
donne \(v_2(n-m)\ge k\). Les \(k\) premiers pas suivent la même
branche, donc \(v_2(T^k(n)-T^k(m))=v_2(n-m)-k\). La parité suivante
est commune, donc cette valuation est au moins \(1\), et
\(v_2(n-m)\ge k+1\).

Une période \(p\) dès le rang \(0\) donne donc \(n\equiv T^p(n)\)
modulo toute puissance de \(2\). Ces deux entiers positifs sont
égaux, et l'orbite est un cycle. On ne le cherche pas par un
balayage.

Terras, *Acta Arith.* 30 (1976), théorème 1.2, lu sur le rendu du
PDF, énonce la même équivalence : mêmes vecteurs d'encodage de
longueur \(k\) si et seulement si congruence modulo \(2^k\).
L'application du papier est \(T\). La preuve imprimée n'est pas
recopiée. L'empreinte et le statut de lecture sont dans
`prior_art.md`. Everett (1977) n'est pas rouvert. Steiner (1977)
n'est pas ouvert : il reste la première lecture du cycle 016, qui
n'est pas commencé.

## 11. Revue `6093856144`

Revue indépendante sur le SHA
`3679167ba7d201b1239b3eee80d4e5a8eea58025` (PR #27), soumise le
27 novembre 2026 à 22:15 UTC. Ce n'est pas un nouveau cycle. Le
cycle 016 n'est pas ouvert.

B21, X38, X39 et le cas \(R=1\) sont confirmés. Les deux
formulations locales ci-dessous étaient fausses. Les énoncés
corrigés sont revérifiés. Steiner (1977) et Simons–de Weger ne
sont pas ouverts : leur entier \(m\) n'est pas identifié à \(R\).

**Formule du run.** La phrase du §10 qui disait que \(T^i(n)\) est
impair exactement pour \(0\le i<v_2(n+1)\) ne vaut pas sur l'orbite
entière. Le témoin est \(n=1\) : \(v_2(2)=1\), et \(T^2(1)=1\) est
impair. La formule \(T^i(n)+1=3^i(n+1)/2^i\) vaut pour
\(0\le i\le r\), avec \(r=v_2(n+1)\), jusqu'au premier pair inclus.
Les rangs \(0,\ldots,r-1\) sont impairs et le rang \(r\) est pair.
Cette récurrence suffit pour la longueur du run initial. X38 et
l'atteinte de \(1\) lorsque tous les runs valent au plus \(1\)
restent vrais : ils n'utilisent la formule que sur ce bloc.

**Retour strictement plus bas.** Dans `abandoned.md`, le mot
« retour » de B21 est le premier retour strictement plus bas dans
la classe. Pour \(m=2\), tout entier \(n\ge 1\) a \(U(n)\) impair :
si \(n\) est pair, \(3n+1\) est impair ; si \(n\) est impair, \(U\)
retire tous les facteurs \(2\). Tout départ de la classe
\(1\pmod 2\) y revient donc au premier pas. Ce retour peut être
ascendant, par exemple \(3\to 5\). Il peut aussi descendre :
\(U(9)=7<9\) (X40, §12). Le cas \(4\nmid m\) de la preuve retarde
la descente, par \(U^t(y)>y\) pour \(1\le t<s\). Il ne dit pas que
ces itérés quittent la classe. Le cas \(4\mid m\) retarde tout
retour positif : aucun rang \(1\le t\le j+s-2\) n'est dans la
classe. Dans X37, la montée de \(2911\) est stricte pour
\(1\le t<5\). Au rang \(0\), \(U^0(2911)=2911\). Les cinq valeurs
suivantes sont \(4367\), \(6551\), \(9827\), \(14741\) et \(691\).

**Quantificateur de la question suivante.** Il est écrit au §8.
\(P(2)\) est la question. L'existence d'un \(R\ge 2\) qui convient
lui équivaut. La lecture pour tout \(R\ge 2\) n'est pas ouverte.

## 12. Revue `6093923797`

Revue indépendante sur le SHA
`2a6474b8416668076dfc3aee4b7e62e2e30243d0` (PR #27), soumise le
27 novembre 2026 à 22:22 UTC. Ce n'est pas un nouveau cycle. Le
cycle 016 n'est pas ouvert.

La formule du bloc impair initial, le cas \(R=1\), B21, la fenêtre
de \(2911\) et la réduction du §8 à \(P(2)\) sont confirmés.
\(P(2)\) n'est pas entamé. Steiner (1977) n'est pas ouvert. La revue
cite Simons–de Weger, §§1.1–1.2 ; ce PDF n'est pas ouvert ici et
n'est pas une prémisse.

**X40.** La phrase « pour \(m=2\), le retour au premier pas n'est
pas une descente » est trop générale. Elle figurait dans X37, dans
le §11, dans le résumé de l'agenda et dans le commentaire du
script. \(U(n)\) est impair pour tout entier \(n\ge 1\). Le retour
dans la classe \(1\pmod 2\) a donc lieu au premier pas. Son signe
dépend du résidu modulo \(4\).

Soit \(n\) impair.
- Si \(n\equiv 3\pmod 4\), alors \(3n+1\equiv 2\pmod 4\), donc
  \(v_2(3n+1)=1\) et \(U(n)=(3n+1)/2\). Cette valeur dépasse \(n\),
  car \(n+1>0\). Le retour est une montée. Témoin : \(U(3)=5\).
- Si \(n\equiv 1\pmod 4\) et \(n>1\), alors \(3n+1\) est divisible
  par \(4\), donc \(v_2(3n+1)\ge 2\) et
  \(U(n)\le(3n+1)/4\). Cette borne est strictement plus petite que
  \(n\), car \(n>1\). Le retour est une descente. Témoin :
  \(3\cdot 9+1=28\) et \(U(9)=7\). Le même cas donne \(U(5)=1\).
- Si \(n=1\), \(U(1)=1\).

Le retour a lieu au premier pas et peut être ascendant, par
exemple \(3\to 5\). B21 ne change pas : aucun temps ne fait
descendre tous les départs de la classe. Les entiers
\(n\equiv 3\pmod 4\) montent dès le premier pas, donc \(T=1\) ne
couvre pas la classe. Ce partage est élémentaire. Ce n'est pas un
théorème nouveau, ni une contrainte sur une orbite divergente.
