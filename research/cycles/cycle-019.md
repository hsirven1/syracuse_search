# Cycle 019 — (1.5) et (1.6) de Bernstein–Lagarias 1996 sont H3

Date : 28 novembre 2026. Axe **B**. Branche : `research/memory`.
Script : [`../checks/cycle019_bernstein_lagarias.py`](../checks/cycle019_bernstein_lagarias.py).

**Verdict.** NO-GO. Les affichages (1.5) et (1.6) identifient la
conjecture de périodicité imprimée à H3. Ils ne la prouvent pas.
Aucune orbite divergente n'est exclue. Aucune preuve de Syracuse.

## 0. Revue traitée, fenêtre, porte d'antériorité

La revue `6094790973` porte le marqueur `SYRACUSE_INDEPENDENT_REVIEW`
et le SHA `5944512e23964e259f6d72b05e03f4dec0a742d9`, tête de la PR #27
au début de ce cycle. Elle confirme X49. La suite de \(5\) est
\(5,8,4,2,1,2,1\). Le premier rang de période \(2\) est \(s=3\), et
\(s=4\) reste un choix. B24 est inchangé. Elle ne demande aucune
correction. Le cycle 018 n'est pas réécrit.

La fenêtre de douze cycles contient, au 28 novembre 2026 à 01:02 UTC,
les cycles 008 à 018. Le premier commit du cycle 008 est `ff58fed`,
du 27 novembre à 01:09:59 UTC. Ce cycle est le douzième. Le cycle 020
n'est pas ouvert.

**Candidat.** Les affichages (1.5) et (1.6) de Bernstein–Lagarias,
*Canad. J. Math.* 48 (1996), 1154–1169, prouvent que tout élément de
\(\mathbb Q\cap\mathbb Z_2\) a un itinéraire ultimement périodique
sous \(T\).

**Obstacle.** H3 est exactement cet énoncé, et elle est ouverte. La
lire comme un théorème fermerait à tort la non-divergence.

**Intérêt.** Si ces deux formules prouvaient H3, toute orbite
rationnelle serait ultimement périodique. Avec B24, toute orbite
positive serait finie.

**Résultat le plus proche.** H3, déjà enregistrée comme la conjecture
de périodicité de Lagarias 1985. Le PDF de 1996 n'avait pas été ouvert.

**Écart.** Aucun, pour l'égalité. Le papier énonce l'inclusion
\(\Phi(\mathbb Q\cap\mathbb Z_2)\subseteq\mathbb Q\cap\mathbb Z_2\)
comme connue, et l'égalité comme conjecture. L'identification précise
passe par le lemme élémentaire sur les développements binaires, écrit
au §2.

**Classement.** DÉJÀ CONNU. Confiance haute : les deux affichages et
la phrase « Periodicity Conjecture » ont été lus sur le PDF d'auteur.
Ce n'est pas une nouveauté, ni un corollaire qui résoudrait H3.

**Décision.** NO-GO pour prouver H3, pour redémontrer la conjugaison,
et pour traiter un itéré \(\Phi^k\) comme une forme plus faible.

Deux autres candidats, lus sur les mêmes pages, sans seconde
expérience :

1. Remplacer H3 par \(\Phi^k(\mathbb Q\cap\mathbb Z_2)=\mathbb Q\cap\mathbb Z_2\)
   pour un \(k\ge 2\). Le papier dit que la conjecture équivaut à cette
   égalité pour chaque \(k\ge 1\). NO-GO : ce n'est pas plus faible.
2. Lire la conjecture imprimée \(\mathbb Z^+\subseteq\Phi(\tfrac13\mathbb Z)\)
   comme un théorème déduit de (1.5) et (1.6). Elle est énoncée à part,
   avec renvoi à [2] et [8], non ouverts. NO-GO. Le cycle ne l'identifie
   pas à l'atteinte de \(1\).

## 1. Source lue

PDF d'auteur
`https://websites.umich.edu/~lagarias/doc/bernstein.pdf`,
SHA-256
`476b0149d6d6f7944e9bf470a9347a14336547a116c5eb6877d020219a5b4c4e`,
16 pages, non redistribué. Pages lues : 2 et 3, pour (1.5), (1.6) et
les phrases qui disent ce que ces formules impliquent, ainsi que les
trois lignes de bibliographie qui nomment [2], [8] et [9]. Les
sections 2 à 6 et les appendices ne sont pas adoptés. Leurs théorèmes
sur les cycles de \(\Phi_n\) ne sont pas vérifiés. Le papier écrit
que ces résultats ne touchent pas la conjecture \(3x+1\) de façon
immédiate : ce n'est pas une raison de les ouvrir.

L'application est celle du dépôt :
\(T(x)=(3x+1)/2\) si \(x\) est impair, \(T(x)=x/2\) si \(x\) est pair.
Le décalage \(S\) retire le bit bas. La conjugaison imprimée en (1.3),
sur la même page, est \(\Phi\circ S\circ\Phi^{-1}=T\), avec
\(\Phi(0)=0\). L'unicité n'est pas recopiée. (1.4) est
\(\Phi(x)\equiv x\pmod 2\).

\[
(1.5)\qquad
\Phi^{-1}(x)=\sum_{i=0}^{\infty}(T^i(x)\bmod 2)\,2^i.
\]

Si \(x=\sum_l 2^{d_l}\) avec \(0\le d_1<d_2<\cdots\), alors

\[
(1.6)\qquad
\Phi(x)=-\sum_l 3^{-l}2^{d_l}.
\]

Le papier dit que (1.5) implique (1.3) et (1.4), et que (1.6) aussi.
Il dit que \(\Phi(\mathbb Q\cap\mathbb Z_2)\subseteq\mathbb Q\cap\mathbb Z_2\)
se déduit facilement de (1.6), et renvoie à [2]. Cette déduction n'est
pas refaite. [2] est Bernstein, *Proc. Amer. Math. Soc.* 121 (1994),
405–408. [8] est Lagarias, *Amer. Math. Monthly* 92 (1985), 3–23. [9]
est Lagarias, *Acta Arith.* 56 (1990), 33–53. Aucun des trois n'est
ouvert ici.

La conjecture imprimée, proposée dans [8], est

\[
\Phi(\mathbb Q\cap\mathbb Z_2)=\mathbb Q\cap\mathbb Z_2.
\]

Le papier dit qu'elle impliquerait l'absence de trajectoire divergente
de \(T\) sur \(\mathbb Z\). Il appelle divergente une trajectoire qui
prend une infinité de valeurs distinctes, et écrit
\(|T^k(n)|\to\infty\). L'équivalence annoncée avec l'absence de
trajectoire divergente de \(T_{3,k}\) pour tout \(k\equiv\pm 1\pmod 6\),
via [9, Corollary 2.1b], n'est pas adoptée.

## 2. Développements binaires

**Lemme.** Un élément \(\alpha\in\mathbb Z_2\) est dans
\(\mathbb Q\cap\mathbb Z_2\) si et seulement si ses chiffres binaires
sont ultimement périodiques. C'est un fait classique, pas un résultat
sur \(T\).

**Preuve.** Si les chiffres ont une prépériode \(p\ge 0\) et une
période \(q\ge 1\), alors
\(\alpha=A+2^p B/(1-2^q)\) avec \(A,B\in\mathbb Z\). Le dénominateur
\(1-2^q\) est une unité de \(\mathbb Z_2\), donc
\(\alpha\in\mathbb Q\cap\mathbb Z_2\).

Réciproquement, soit \(\alpha=c/d\) avec \(d>0\) impair et
\(c\in\mathbb Z\). Soit \(s_n\) la somme des \(n\) premiers chiffres,
\(0\le s_n<2^n\), et \(t_n=(d s_n-c)/2^n\). C'est un entier, car
\(s_n\equiv c\,d^{-1}\pmod{2^n}\). Le chiffre suivant est
\(b_n\equiv t_n\pmod 2\), et \(t_{n+1}=(t_n+d b_n)/2\).

Comme \(0\le s_n\le 2^n-1\),
\[
-\frac{c}{2^n}\le t_n\le d-\frac{d+c}{2^n}.
\]
Si \(c\ge 0\) et \(2^n>c\), alors \(t_n\in\{0,1,\ldots,d-1\}\).
Si \(c=-c'<0\) et \(2^n>c'\), alors \(t_n\in\{1,2,\ldots,d\}\).
Pour tout indice assez grand, \(t_n\) est donc dans un ensemble fini,
et l'indice suivant est une fonction de \(t_n\). La suite \((t_n)\)
est ultimement périodique, et les chiffres \(b_n\equiv t_n\pmod 2\)
aussi.

Le script contrôle la récurrence sur \(-1/3\), chiffres \(1,0,1,0,\ldots\),
et sur \(1\), chiffres \(1,0,0,0,\ldots\).

## 3. Identification (B25)

Par (1.5), l'itinéraire de \(x\) est ultimement périodique si et
seulement si le développement binaire de \(\Phi^{-1}(x)\) l'est. Le
lemme dit que ceci équivaut à \(\Phi^{-1}(x)\in\mathbb Q\cap\mathbb Z_2\),
donc à \(x\in\Phi(\mathbb Q\cap\mathbb Z_2)\).

Ainsi, tout \(x\in\mathbb Q\cap\mathbb Z_2\) a un itinéraire
ultimement périodique si et seulement si
\(\mathbb Q\cap\mathbb Z_2\subseteq\Phi(\mathbb Q\cap\mathbb Z_2)\).

L'inclusion opposée est celle que le papier donne comme connue. Les
deux ensemble sont l'égalité imprimée. Cette égalité est H3. Le sens
connu est la réciproque déjà écrite dans H3 : un itinéraire ultimement
périodique force un point rationnel. Il n'est pas redémontré.

B24 dit qu'un entier positif a un itinéraire ultimement périodique si
et seulement si son orbite est finie. La restriction de H3 aux entiers
positifs est donc la non-divergence, déjà enregistrée. Le papier ne
prouve pas cette restriction : il la laisse dans la conjecture, et
l'énonce pour tout \(\mathbb Z\).

La même page dit que la conjecture équivaut, pour chaque \(k\ge 1\), à
\(\Phi^k(\mathbb Q\cap\mathbb Z_2)=\mathbb Q\cap\mathbb Z_2\). Passer
à un itéré ne l'affaiblit pas.

La conjecture séparée \(\mathbb Z^+\subseteq\Phi(\tfrac13\mathbb Z)\)
n'est pas déduite de (1.5) ni de (1.6). Le contrôle
\(\Phi(-1/3)\equiv 1\pmod{2^{64}}\), avec \(-1/3\in\tfrac13\mathbb Z\),
montre seulement que \(1\) appartient à l'ensemble de droite. Il ne
montre pas l'inclusion, ni l'atteinte de \(1\).

La ligne secondaire de `prior_art.md` attribuait à Bernstein 1994 la
série \(-\sum 2^{d_i}/3^{i+1}\) comme valeur de \(\Phi^{-1}\). La
forme (1.6), avec \(l\) commençant à \(1\), est la même série, et le
papier de 1996 l'attribue à [2] comme formule de \(\Phi\). L'article
de 1994 n'est pas ouvert : le nom \(\Phi^{-1}\) de la ligne secondaire
n'est pas une prémisse, et il n'est pas corrigé ici. B1 n'est pas
redérivé. Sur l'itinéraire de \(1\), la série de B1 redonne
\(\xi\equiv 1\pmod{2^{64}}\), et (1.6) appliqué aux bits de \(-1/3\)
redonne aussi \(1\). Les deux formules calculent le point, dans cet
exemple. Cela ne tranche pas le nom porté par la ligne secondaire.

## 4. Ce que ce cycle ne montre pas

H3 reste ouverte. Aucun rationnel à itinéraire apériodique n'est
produit. Aucune orbite divergente n'est exclue. Les sections 2 à 6,
l'ordre annoncé \(2^{n-4}\) et les appendices ne sont pas des
prémisses. [2], [8] et [9] ne sont pas lus. La forme linéaire
d'Eliahou reste non adoptée. B24 n'est pas réécrit.

## 5. Mises à jour de la mémoire

- `proved.md` : B25, identification seulement.
- `hypotheses.md` : H3, même énoncé, source primaire de 1996 lue pour ces deux affichages.
- `prior_art.md` : Bernstein–Lagarias passe de [S] à [P] pour (1.5), (1.6) et la conjecture imprimée.
- `abandoned.md` : ne pas prouver H3 depuis ces formules, ni ouvrir \(\Phi_n\).
- `agenda.md` : arrêt des lectures de portée ; question suivante sur l'axe A.
- `reviews.md` : revue `6094790973`.

## 6. Prochaine question

Les cycles 016 à 019 ont retrouvé des énoncés publiés. Cette direction
s'arrête. Ne pas ouvrir un cycle dont le travail est de lire un
théorème classique pour décider s'il exclut une orbite divergente. En
particulier, ne pas ouvrir Lagarias 1985, Bernstein 1994, le
corollaire 2.1b de Lagarias 1990, ni les sections 2 à 6 du papier de
1996. Ne pas rouvrir H3, la conjugaison, \(\Phi^k\), Tao, Korec,
Eliahou, \(P(2)\), le signe moins, la famille appariée, ni B24.

Axe **A**. A3 donne, pour chaque \(m\) fixé, une classe modulo
\(2^{2m+1}\) sur laquelle \(\tau_U=m\). L'horizon y est constant, et la
classe est un cylindre de Terras. B13 interdit un horizon \(o(\log n)\)
valable pour tous les grands \(n\), sous un poids borné.

La question est la suivante. Existe-t-il une famille infinie explicite
d'impairs \(n>1\), non contenue dans un cylindre de Terras de longueur
bornée, pour laquelle une trajectoire close prouve
\(\tau_U(n)\le C\log_2(n+1)\) avec une constante \(C\) absolue ?

Si la famille est une classe d'A3, le cas \(n\equiv 1\pmod 4\) de X40,
un nombre de Mersenne, ou \(5\cdot 2^k-1\), NO-GO. Ne pas chercher
au-delà de ces familles et d'une progression arithmétique simple. Si
aucun mécanisme clos n'apparaît, s'arrêter sans lemme de remplacement.
Ne pas relancer H1 par une campagne : un préfixe sans pas pair, comme
la montée de Mersenne, ne prouve ni ne réfute (C). Ne pas ouvrir ce
cycle avant la relecture indépendante du présent cycle. La fenêtre
devra être recomptée : le cycle 008 sort à 01:09:59 UTC le 28 novembre
2026, et cette attente de relecture reste même après cette sortie.

## 7. Reproduire

```sh
python3 research/checks/cycle019_bernstein_lagarias.py
```

Sortie attendue : 11 lignes `PASS`.
