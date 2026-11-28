# Mot triangulaire de parités : complexité exacte et réduction 2-adique

**28 octobre 2026 — audit mathématique complémentaire de l'étude sur la densité des pas pairs.**

**Verdict :** théorème combinatoire élémentaire démontré (formule exacte de complexité) et congruences (14) contrôlées. **La non-stabilisation des représentants canoniques n'est pas démontrée.** Aucune nouveauté scientifique ni résolution de Syracuse n'est revendiquée.

Référence interne : [\`EVEN_DENSITY_STRUCTURAL_AUDIT.md\`](EVEN_DENSITY_STRUCTURAL_AUDIT.md), §7, sur la branche parente \`research/even-density-structural-audit\`.

## 1. Théorème combinatoire exact

Soit le mot infini
\[
w=(1^1 0)(1^2 0)(1^3 0)\cdots
=10\,110\,1110\,11110\cdots.
\]
Noter \(p_w(L)\) le nombre de facteurs contigus *distincts* de longueur \(L\).

**Théorème.**
\[
p_w(1)=2,\qquad p_w(2)=3,\qquad
\boxed{p_w(L)=\left\lfloor\frac{(L+1)^2}{4}\right\rfloor\quad(L\ge3).}
\]

**Preuve sans recensement numérique.** Les zéros sont aux positions \(z_j=j(j+3)/2-1\), avec indices commençant à zéro. Les écarts entre les zéros consécutifs sont donc \(z_{j+1}-z_j=j+2\), soit \(3,4,5,\ldots\).

- **Aucun zéro** : un facteur, \(1^L\), qui apparaît dans des runs arbitrairement longs.
- **Un seul zéro** : exactement \(L\) facteurs \(1^a0\,1^{L-1-a}\), \(0\le a<L\). Ils sont tous réalisables autour d'un zéro assez tardif, avec des runs voisins d'au moins \(L\).
- **Au moins deux zéros** : désigner par \(a\) la position du premier zéro dans la fenêtre, et par \(d\) l'écart au deuxième. Ici \(d=j+2\ge3\) pour une unique paire consécutive de zéros du mot. Le départ de la fenêtre est licite, et le zéro précédent est exclu, exactement lorsque \(0\le a\le d-2\) ; si \(j=1\), \(z_1=1\) impose également \(a\le1=d-2\). Le deuxième zéro appartient à la fenêtre exactement lorsque \(a+d<L\). Ainsi, pour chaque \(d=3,\ldots,L-1\), il existe
\[
\min(d-1,L-d)
\]
valeurs de \(a\). Ces paramètres déterminent *un seul* facteur : le premier écart fixe \(j\), et tous les écarts suivants sont forcés par la définition du mot. Deux couples \((a,d)\) différents donnent des facteurs différents, puisque leurs deux premiers zéros sont à des positions différentes.

Par conséquent, pour \(L\ge3\),
\[
p_w(L)=1+L+\sum_{d=3}^{L-1}\min(d-1,L-d).
\]
Si \(L=2m\), la somme vaut \(m(m-1)-1\), donnant \(p_w(L)=m(m+1)\). Si \(L=2m+1\), la somme vaut \(m^2-1\), donnant \(p_w(L)=(m+1)^2\). C'est la formule annoncée. \(\square\)

**Portée :** \(p_w(L)\sim L^2/4\), très au-dessus de la borne *linéaire* qu'une orbite hypothétiquement divergente doit satisfaire. Donc ni les PR #21–22 ni leur correction logarithmique ne peuvent exclure ce mot par une simple comparaison de complexités.

## 2. Identité de blocs et congruences : vérification des indices

Soient \(Q_m=m(m+1)/2\), \(\tau_m=Q_m+m\). Écrivons \(x_i=n_{\tau_{i-1}}+1\) (avec \(x_1=N+1\)) et supposons réalisées successivement les parités \(1^i0\).

Le bloc \(1^i0\) donne exactement
\[
x_{i+1}=\frac{3^i x_i+2^i}{2^{i+1}}.
\]
En composant \(m\) blocs,
\[
2^{\tau_m}x_{m+1}
=3^{Q_m}(N+1)+C_m,\quad
C_m=\sum_{j=1}^m2^{\tau_j-1}3^{Q_m-Q_j}.
\]
Pour imposer aussi le bit initial \(1\) du bloc suivant, \(n_{\tau_m}\) est impair, donc \(x_{m+1}\) est pair. Cela équivaut à l'exigence
\[
\boxed{2^{\tau_m+1}\mid 3^{Q_m}(N+1)+C_m.}\tag{A}
\]
On retrouve **exactement (14)** du rapport précédent, y compris le \(+1\) du module.

Comme \(3^{Q_m}\) est inversible modulo \(2^{\tau_m+1}\), (A) définit une unique classe de \(N\bmod 2^{\tau_m+1}\). Son représentant canonique non négatif \(r_m\) est cohérent lorsque \(m\) augmente : \(r_{m+1}\equiv r_m\bmod2^{\tau_m+1}\).

Par passage à la limite dans \(\mathbb Z_2\), il existe une réalisation 2-adique **unique**
\[
N+1=-\sum_{j\ge1}\frac{2^{\tau_j-1}}{3^{Q_j}}
=-\frac12\sum_{j\ge1}2^j(2/3)^{j(j+1)/2}.\tag{B}
\]
La série converge 2-adiquement, car \(\nu_2\) de son \(j\)-ième terme vaut \(\tau_j-1\to\infty\).

**La question réduite, toujours non démontrée**, est de savoir si ce nombre 2-adique peut être l'entier \(N+1\ge2\). Montrer qu'il est irrationnel dans \(\mathbb Q_2\) suffirait, mais serait **strictement plus fort**. Les signes d'une somme réelle et d'une somme 2-adique ne se comparent pas directement.

## 3. Obstacles aux preuves naïves

**Faux renforcement :** « à chaque bloc supplémentaire, le représentant canonique augmente strictement ». Contre-exemple exact :
\[
r_1=1,\quad r_2=57,\quad r_3=121,\quad r_4=121.
\]
Ces représentants sont ceux de la classe complète incluant le premier bit du bloc suivant, modulo \(2^{\tau_m+1}\). Les classes peuvent donc *stagner* sur un bloc ; la monotonie simple ne garantit aucun accroissement strict à chaque étape.

**Borne archimédienne insuffisante.** Si un entier positif fixe \(N\) satisfaisait (A) pour tous les \(m\), l'entier
\(B_m=3^{Q_m}(N+1)+C_m\) serait divisible par \(2^{\tau_m+1}\), mais sa taille réelle serait de l'ordre de \(3^{Q_m}\), bien plus grande que ce diviseur de l'ordre de \(2^{Q_m+m}\). Le principe « multiple non nul plus petit que le module » ne peut donc pas créer de contradiction.

**Obstruction de complexité.** La formule quadratique précédente rend inapplicables les arguments qui excluent seulement les mots de complexité linéaire \(< 1.7095L\). Le mot a assez de facteurs pour échapper à cette méthode même si ses zéros ont densité nulle.

## 4. Correction bibliographique importante

L'article *On integer sequences generated by linear maps* d'**Artūras Dubickas**, *Glasgow Mathematical Journal* 51 (2009), 243–252, DOI [10.1017/S0017089508004655](https://doi.org/10.1017/S0017089508004655), est accessible en texte intégral auprès de [Cambridge University Press](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C40C0C07FEC20797475BB2899C436C9A/S0017089508004655a.pdf/on_integer_sequences_generated_by_linear_maps.pdf).

Il importe de **distinguer les deux applications** :
- son **corollaire 4** concerne la fonction *différente* \(x\mapsto\lceil3x/2\rceil\), avec borne \(p(L)>1.70951129L\) pour les grands \(L\) ;
- son **théorème 5** énonce déjà cette borne pour la **véritable application raccourcie de Collatz**, **sous l'hypothèse explicite que l'orbite positive tend vers l'infini**. Une orbite positive non bornée de cette application est injective, donc tend effectivement vers l'infini. La borne linéaire de #21 n'est **pas scientifiquement nouvelle**.

La constante exacte \(1/\log_2(3/2)\) et le calcul affine du dépôt sont cohérents avec cette source, sans attribuer automatiquement à Dubickas le raffinement logarithmique des PR suivantes.

Le manuscrit non expertisé d'Elias De Jesús, *A drift-sensitive complexity bound for rational points of the 3x+1 conjugacy map* (2026), [ResearchGate](https://www.researchgate.net/publication/415049049_A_DRIFT-SENSITIVE_COMPLEXITY_BOUND_FOR_RATIONAL_POINTS_OF_THE_3x_1_CONJUGACY_MAP), rappelle aussi cette antériorité ; il ne valide pas l'irrationalité du nombre (B). Le statut exact de la littérature sur les valeurs de theta partielle 2-adiques doit être établi avant toute revendication d'originalité.

## 5. Tests réellement exécutés

Un script Python **indépendant** de l'implémentation du dépôt a vérifié :
- l'égalité de la formule de complexité pour **78 longueurs** \(3\le L\le80\), en énumérant les facteurs d'un préfixe suffisamment long du mot infini ;
- (A), y compris l'ordre des bits, pour **7 valeurs** \(1\le m\le7\), en construisant le représentant canonique par inversion exacte et en **itérant indépendamment** la fonction raccourcie.

Les résultats ont tous été **PASS**. Ils illustrent les identités finies, mais la preuve de la formule quadratique et la dérivation de (A) reposent sur les arguments ci-dessus. Aucune preuve Lean, aucune démonstration de non-stabilisation, aucun calcul massif.

## Verdict et question résiduelle unique

**Démontré :** formule exacte de complexité (tout \(L\ge3\)) ; correction et indices de la congruence (14) ; existence de la représentation 2-adique (B), et contre-exemple à la croissance stricte des représentants à chaque bloc.

**Non démontré :** non-stabilisation de \(r_m\), non-intégralité positive de (B), irrationalité 2-adique, amélioration du coefficient asymptotique conditionnel de complexité, Syracuse.

La prochaine tentative mathématique sérieuse devrait viser **une obstruction d'intégralité 2-adique pour la série explicite (B)**, pas une nouvelle extension numérique des \(r_m\), ni une comparaison de complexité linéaire. Il faut commencer par vérifier des critères publiés de non-rationalité des séries de theta partielles sur \(\mathbb Q_2\), et ne pas supposer qu'ils s'appliquent automatiquement.