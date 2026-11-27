# Cycle 013 — L'obstruction avec compteurs est déjà écrite

Date : 27 novembre 2026. Axe **B**.
Branche : `research/memory`. Script : [`../checks/cycle013_two_path.py`](../checks/cycle013_two_path.py).

**Verdict : NO-GO pour une seconde preuve.** Le théorème 1 de la note
du 19 octobre 2026 est l'obstruction demandée. La moitié élémentaire,
lemme 2 et identité pondérée, est réécrite et contrôlée ici (B19).
Les lemmes 3 et 4 réduisent l'existence, pour chaque module, au
théorème des nombres premiers en progression fixe et à
Brun–Titchmarsh. Cette réduction a été lue : aucun trou précis n'y
est apparu. Ces deux théorèmes analytiques ne sont pas redémontrés,
et les PDF cités ne sont pas ouverts. Ce n'est pas une découverte,
ni une contrainte sur une orbite divergente.

## 0. Revue traitée, question, porte d'antériorité

La revue `6082966513` porte le marqueur `SYRACUSE_INDEPENDENT_REVIEW`
et le SHA `b033647064504257fe8485c0bd8ea231f20a156d`, tête de la PR #27
au début de ce cycle. Elle confirme B18. Elle ne demande aucune
correction. Le cycle 012 n'est pas réécrit. La fenêtre de douze cycles
était fermée jusqu'au 27 novembre 2026 à 20:06 UTC : le commit `416b1f1`
est du 26 novembre à 20:05:56 UTC. Ce cycle commence après cet instant.

**Candidat.** Pour tout entier \(M\ge 1\), toute fonction réelle \(\Phi\)
du couple \((n\bmod M,\ v_2(n+1))\), toute fonction réelle \(R\), tous
réels \(\beta,\gamma\), et toute fonction \(H\) strictement croissante
sur les impairs positifs, aucun seuil \(X_0\) ne satisfait
\(V(U(n))\le V(n)\) pour tout impair \(n>X_0\), où
\[
V(n)=H(n)+\Phi\bigl(n\bmod M,\ v_2(n+1)\bigr)
+\beta\,\omega(n)+\gamma\,\Omega(n)+R\bigl(\Omega(n)-\omega(n)\bigr)
\]
et \(U(n)=(3n+1)/2^{v_2(3n+1)}\). Ici \(\omega(1)=\Omega(1)=0\).

**Obstacle.** B18 ferme la forme sans \(\omega\), \(\Omega\) ni \(R\).
Le trajet \(123\to 139\) change \(\omega\) : un seul trajet ne règle
pas les coefficients.

**Intérêt.** Une fonction de Lyapunov stricte de cette forme, propre
et minorée, prouverait la conjecture. Fermer la forme retire une
architecture de certificat. Elle ne contraint pas une orbite
divergente.

**Résultat le plus proche.** La note du 19 octobre 2026,
`https://rstation.ai/problems/collatz/papers/3`, u/sylve_recursions,
relue intégralement pour ce cycle. Ce n'est pas une publication
primaire. Son théorème 1 est le candidat, y compris l'existence des
deux trajets au-dessus de tout seuil. Le §3 donne le cycle
\(-5\xrightarrow{1}-7\xrightarrow{2}-5\) et \(F(n)=(9n+5)/8\). Le
théorème 3.1 de Chang exclut \(\log_2 n+g(n\bmod 2^k)\), sans
valuation et sans compteurs. B18 est le cas \(\beta=\gamma=0\) et
\(R=0\), prouvé sans le crible. Les recherches arXiv et web de ce
cycle retrouvent la note elle-même. Les extraits obtenus pour
arXiv:2604.20181, 1906.02847, 2512.01739, 2601.15463 et 2510.06736
portent sur d'autres énoncés ; ces articles n'ont pas été lus. Cette
recherche ne prouve pas l'absence d'une source journalistique.

**Écart.** Aucun. Le candidat est le théorème 1 de la note. Chang et
B18 sont plus faibles : ils n'annulent pas un coefficient arbitraire
de \(\omega\) et de \(\Omega\).

**Classement.** DÉJÀ ÉCRIT dans la note, confiance haute pour
l'identification de l'énoncé, confiance moyenne pour l'absence d'une
autre source : la recherche n'est pas un inventaire exhaustif. La
moitié élémentaire est prouvée ci-dessous sans nouveauté. La moitié
existentielle est une réduction à deux théorèmes classiques, pas un
crible nouveau. Signification : fermer le complément de B18. Pas une
contrainte sur un contre-exemple hypothétique.

**Décision.** NO-GO pour une seconde preuve et pour tout ansatz
voisin (fonction jointe arbitraire de \(\omega\) et \(\Omega\),
distance \(v_2(n+5)\), temps de retour adaptatif). Le travail de ce
cycle est la vérification de la preuve déjà écrite.

## 1. Lemme 2, réécrit

Soit \(M=2^u 3^v N\) avec \((N,6)=1\). Posons \(K=\max(u,3)\). Si
\(N=1\), soit \(t=1\). Sinon \(t\) est l'ordre multiplicatif de
\(9\cdot 8^{-1}\) modulo \(N\). Posons \(A=9^t\), \(B=8^t\),
\(C=5(A-B)\) et \(L=2^{3t+K}3^v N\). Soit \(r\) le plus petit résidu
non négatif tel que
\[
r\equiv -5\pmod{2^{3t+K}},\qquad
r\equiv -5\pmod{3^v},\qquad
r\equiv 1\pmod N,
\]
en omettant toute congruence de module \(1\). Posons
\(s=(Ar+C)/B\) et \(D=AL/B\).

**Lemme.** Ces quotients sont des entiers. Pour tout entier \(z\ge 0\),
le mot \(U\) de \(f(z)=r+Lz\) en \(2t\) pas est \((1,2)^t\), l'extrémité
est \(g(z)=s+Dz>f(z)\), et chaque état impair du trajet est au moins
\(f(z)\). Les deux extrémités sont congrues modulo \(M\) et ont
\(v_2(n+1)=2\). Les formes \(f\) et \(g\) sont primitives et non
proportionnelles.

Le système est résoluble par le théorème chinois : les modules sont
deux à deux premiers entre eux. Comme \(r+5\) est divisible par
\(2^{3t+K}\) et que \(3t+K\ge 3t\), \(B=2^{3t}\) divise \(r+5\). Donc
\(s=A(r+5)/B-5\) est entier. De même \(D=A\cdot 2^K 3^v N\) est entier.

Écrivons \(f(z)=-5+2^{3t+K}h\) avec \(h\ge 1\). Après \(j\) blocs
\((1,2)\), l'état formel est \(-5+9^j 2^{3(t-j)+K}h\). Pour
\(0\le j<t\), la puissance de \(2\) vaut au moins \(2^{3+K}\) et
\(K\ge 3\), donc l'état est congru à \(-5\equiv 11\pmod{16}\). Si
\(x=16m+11\), alors \(3x+1=2(24m+17)\) et \(24m+17\) est impair : la
valuation vaut exactement \(1\). Ensuite \(9x+5\equiv 8\pmod{16}\), donc
\(v_2(9x+5)=3\) et le second pas retire exactement \(2\). Chaque bloc
est donc le mot réel \((1,2)\), y compris le dernier. L'image d'un
bloc est \(F(x)=(9x+5)/8=x+(x+5)/8>x\). Une application de \(F\)
multiplie le coefficient de \(h\) par \(9\) et baisse l'exposant de
\(2\) de \(3\), ce qui donne la forme annoncée au bloc suivant. Le pas intermédiaire
\((3x+1)/2\) est un impair strictement plus grand que \(x\). Les
départs de blocs croissent, et tous les états impairs restent
au moins égaux au départ du trajet.

L'extrémité vaut \(-5+9^t 2^K h\). Comme \(K\ge 3\),
\(n+1=4\bigl(-1+9^t 2^{K-2}h\bigr)\) avec le second facteur impair, donc
\(v_2(n+1)=2\). Le départ a la même forme avec une puissance de \(2\)
au moins égale. Les deux extrémités sont congrues à \(-5\) modulo
\(2^K\), donc modulo \(2^u\). Si \(v\ge 1\), \(r+5\) est divisible par
\(3^v\) et \(B\) est inversible modulo \(3^v\), donc
\(s=A(r+5)/B-5\equiv -5\pmod{3^v}\). Comme \(3^v\) divise \(D\),
\(g(z)\equiv s\) aussi. Enfin \(A\equiv B\pmod N\), donc
\(g\equiv f\equiv 1\pmod N\). Elles coïncident modulo \(M\). Si
\(v=0\) ou \(N=1\), la congruence correspondante est omise.

La primitivité de \(f\) : \(r\) est impair, premier à \(3^v\) car
\(-5\) l'est, et congru à \(1\) modulo \(N\). Celle de \(g\) : \(B\) est
une puissance de \(2\), donc \(9^t\) divise \(A(r+5)/B\) et
\(s\equiv -5\not\equiv 0\pmod 3\). Le même quotient est divisible par
\(2^K\), avec \(K\ge 3\), donc pair, et \(s\) est impair. Enfin
\(s\equiv 1\pmod N\). Les premiers de \(D\) sont \(2\), \(3\) et ceux
de \(N\).
Le déterminant \(Ls-rD=LC/B\) est strictement positif, car
\(9^t>8^t\).

Le script contrôle cet énoncé pour
\(M\in\{1,5,7,8,9,24,35,40,45,72,105,360\}\) et \(z\in\{0,1,2\}\).
Pour \(M=1\), \(r=59\), \(L=64\), \(s=67\), \(D=72\). Pour \(M=24\),
\(r=187\), \(L=192\), \(s=211\), \(D=216\), et \(z=1\) redonne
\(379\to 427\). Pour \(M=35\), \(t=12\) et
\(r=14843406974971\). Le mot \((1,2)^{12}\) est vérifié sur \(z=0,1,2\).
Aucune factorisation n'est produite à cette taille : la note dit
déjà que le module \(35\) dépasse son plafond de recherche \(10^{13}\).

## 2. Identité pondérée (B19)

**Proposition.** Soient deux trajets finis d'impairs positifs sous
\(U\), de départs \(n_\pm>X_0\) et d'extrémités \(m_\pm\), tels que :

1. chaque état intermédiaire est au moins égal au départ de son trajet ;
2. \(m_\pm>n_\pm\), et les quatre extrémités sont sans facteur carré ;
3. les quatre extrémités ont le même résidu modulo \(M\) et
   \(v_2(\,\cdot\,+1)=2\) ;
4. \(n_+\) est premier, \(\omega(m_+)\ge 2\), \(m_-\) est premier et
   \(\omega(n_-)\ge 2\).

Alors aucun potentiel \(V\) de la forme ci-dessus n'est décroissant
au sens large sur tous les pas \(U\) d'impairs \(>X_0\).

Posons \(a_+=\omega(m_+)-1>0\) et \(a_-=\omega(n_-)-1>0\). Comme les
extrémités sont sans facteur carré, \(\Omega=\omega\) et
\(\Omega-\omega=0\) aux quatre extrémités. Les accroissements
\((\omega,\Omega)\) valent \((a_+,a_+)\) et \((-a_-,-a_-)\). Les poids
\(a_-\) et \(a_+\) annulent les deux. Le terme \(R\) s'annule aussi,
et \(\Phi\) s'annule sur chaque trajet parce que les arguments
reviennent. Il reste
\[
a_-\bigl(V(m_+)-V(n_+)\bigr)+a_+\bigl(V(m_-)-V(n_-)\bigr)
=a_-\bigl(H(m_+)-H(n_+)\bigr)+a_+\bigl(H(m_-)-H(n_-)\bigr)>0,
\]
dès que \(H\) est strictement croissante. L'un des deux trajets
augmente donc \(V\). Si chaque pas au-dessus de \(X_0\) était
décroissant au sens large, le bilan du trajet serait négatif ou nul.
Contradiction.

Le trajet qui augmente dépend de \(\beta\) et de \(\gamma\). Sur les
témoins \(123\to 139\) et \(379\to 427\), avec \(H(n)=n\), les
accroissements de hauteur sont \(16\) et \(48\), et ceux de \(\omega\)
sont \(-1\) et \(+1\). Pour \(\beta=100\) et \(\gamma=0\), le premier
trajet baisse \(V\) de \(84\) et le second l'augmente. La somme
pondérée reste \(64\). On ne désigne pas le pas fautif.

Cette proposition ne produit pas les trajets. Elle dit seulement ce
qu'une paire déjà factorisée interdit.

## 3. Deux certificats élémentaires

Pour \(M=24\), les trajets de la note
\[
187\xrightarrow{1}281\xrightarrow{2}211,
\qquad
379\xrightarrow{1}569\xrightarrow{2}427
\]
sont les cas \(z=0\) et \(z=1\) du §1. Les factorisations
\(187=11\cdot 17\), \(211\) premier, \(379\) premier et
\(427=7\cdot 61\) sont exactes. Les quatre extrémités valent \(19\)
modulo \(24\) et ont la valuation \(2\). Les poids valent \(1\). La
proposition du §2 s'applique sans crible.

Pour \(M=1\), le même second trajet est l'orientation premier vers
composé, au rang \(z=5\). L'orientation opposée est \(z=1\) :
\(123=3\cdot 41\to 139\), premier. Les poids valent encore \(1\).
Même conclusion, sans crible.

## 4. Existence pour chaque module

Le lemme 3 de la note affirme que deux formes linéaires primitives
non proportionnelles \(az+b\) et \(cz+d\), avec \(a,c>0\), prennent
simultanément, pour une infinité de \(z\ge 0\), une valeur première
et une valeur positive sans facteur carré. Le lemme 4 force au moins
\(k\ge 2\) facteurs premiers distincts du côté sans facteur carré, et
échange les deux formes.

La proportion locale écrite en (9) a été confrontée au décompte
exhaustif des classes modulo \(\ell^2\), pour les huit formes du §1
aux modules \(1,5,7,8,9,24,35,45\), pour cinq autres formes primitives
non proportionnelles, et pour les premiers \(\ell\le 23\). Les
\(117\) proportions coïncident. Ce décompte ne prouve pas le lemme.

L'ordre des quantificateurs est le bon : on fixe d'abord le seuil
\(y\) des petits carrés, puis on fait tendre \(X\) vers l'infini.
Brun–Titchmarsh n'est invoqué que pour les premiers \(\ell>y\) qui ne
divisent pas le discriminant, là où la progression est réduite. Les
grands carrés sont estimés sans primalité. Dirichlet seul ne donne
pas le côté sans facteur carré : la note le dit, et c'est exact.
Aucune incompatibilité locale n'est apparue dans les cas de (9).

Les entrées analytiques sont le théorème des nombres premiers pour
un module fixé, et une forme uniforme de Brun–Titchmarsh. Les textes
cités, Thorner–Zaman (arXiv:2108.10878) et Montgomery–Vaughan
(*Mathematika* 20, 1973), n'ont pas été ouverts. Mirsky (1949) est un
antécédent d'une autre forme, prime plus \(k\)-libre en somme, et
n'a pas été ouvert. Il n'est pas une prémisse. L'existence pour
chaque \(M\) est donc acceptée comme réduction à ces deux théorèmes
classiques, pas comme une preuve autonome du crible. La note ne donne
aucune borne utile sur le premier témoin. Rien ici n'en ajoute.

Appliqués aux formes du §1, les lemmes 3 et 4 fournissent les deux
orientations au-dessus de tout seuil. Avec le §2, le théorème 1 de
la note suit. C'est B19, au sens précisé ci-dessus.

## 5. Ce que ce cycle ne montre pas

Rien sur (C), sur (H), ni sur Syracuse. Les variantes que la note
exclut de son énoncé restent exclues du nôtre : interaction non
linéaire entre la taille et les compteurs, fonction jointe arbitraire
de \(\omega\) et de \(\Omega\), distance non bornée à une ancre
rationnelle, temps de retour adaptatif, futur commun à profondeur
variable, dérive moyenne. Sur les extrémités sans facteur carré,
\(\Omega=\omega\), donc \(\beta\omega+\gamma\Omega\) n'y contribue que
par \(\beta+\gamma\). Cela suffit pour tous les coefficients réels,
et cela ne touche pas une fonction qui séparerait \(\omega\) de
\(\Omega\) hors de ces extrémités.

B17 et B18 ne sont pas repris. Le trajet \(123\to 139\) reste le
témoin qu'un seul chemin change \(\omega\). Le module \(35\) n'a pas
de certificat factorisé dans ce cycle.

## 6. Mises à jour de la mémoire

- `proved.md` : B19, avec la séparation entre la proposition élémentaire et la réduction analytique.
- `hypotheses.md` : le complément de H7 est fermé au sens de B19.
- `prior_art.md` : la note, lue pour le théorème 1 et les lemmes 2 à 4.
- `abandoned.md` : ne pas relancer cette architecture, avec ou sans compteurs.
- `agenda.md` : réévaluation, prochaine question hors de cette architecture. Le budget de cycles est celui du §7.
- `reviews.md` : revue `6082966513`.

## 7. Prochaine question

Les cycles 010 à 013 n'ont pas exclu d'orbite divergente. Le 010
prolonge un préfixe publié, le 011 reformule la conjecture, les 012
et 013 ferment une architecture de potentiel. Cette architecture est
close. Ne pas l'étendre.

Axe **C**, une seule porte d'antériorité, et seulement après le
budget ci-dessous. La mémoire cite Tao, *Forum of Mathematics, Pi*
(2022), théorème presque partout en densité logarithmique, en source
secondaire : l'accès au PDF a été refusé lors des lectures antérieures.
Le candidat est le corollaire exact de cet énoncé primaire, une fois
lu : l'ensemble des départs dont l'orbite ne passe pas sous
\(f(n)\to\infty\) est de densité logarithmique nulle. La question est
de savoir si cet énoncé, avec ses hypothèses réelles, exclut une
classe de congruence, ou seulement un ensemble de densité
logarithmique nulle. Pas de preuve de la conjecture. Pas de retour
à (1), à B17, à B18, à B19, au signe moins, au mot du cycle 006, à
\(5\cdot 2^k-1\), aux conjectures 2 et 3 de Berg–Meinardus, ni aux
théorèmes 4.2.7 et 4.3.10 de Mori.

Le cycle 013 est le douzième de la fenêtre ouverte par le cycle 002.
Le premier commit de ce cycle est `adf706a`, du 26 novembre 2026 à
21:22:58 UTC. Ne pas ouvrir le cycle 014 avant le 27 novembre 2026
à 21:23 UTC.

## 8. Reproduire

```sh
python3 research/checks/cycle013_two_path.py
```

Sortie attendue : quatre lignes `PASS`. La première couvre le
certificat \(187,211,379,427\), les valuations, le résidu \(19\)
modulo \(24\), et le fait qu'un coefficient \(\beta=-10^6\) fait
baisser un seul des deux trajets. La deuxième couvre le lemme 2 sur
les douze modules, trois valeurs de \(z\) chacune. La troisième compte
\(117\) proportions locales. La quatrième trouve les orientations de
\(M=1\) aux rangs \(z=5\) et \(z=1\). Ces contrôles ne sont pas la
preuve de l'existence pour chaque module.
