# Antériorités et littérature

Niveau de vérification : **[P]** énoncé primaire lu pendant cette initialisation · **[P-dép]** primaire lu
par un rédacteur précédent (voir la PR citée) · **[S]** secondaire ou de mémoire, **non revérifié**.
« Connu » ne veut pas dire « relu ici ». Lister une référence n'en valide pas les annonces.

## Codage des parités, dynamique 2-adique
- **Terras** (1976), *Acta Arith.* 30, 241–252 ; **Everett** (1977), *Adv. Math.* 25, 42–45. [S]
  Bijection mots de $k$ parités ↔ classes mod $2^k$ ; temps d'arrêt fini pour presque tout $n$ (densité naturelle).
- **Lagarias** (1985), *Amer. Math. Monthly* 92, 3–23. [S] Conjugaison $\Phi$ de $T$ au décalage sur $\mathbb Z_2$ ;
  itinéraire ultimement périodique ⇒ rationnel ; **conjecture de périodicité** (réciproque, H3).
  Bibliographies annotées : arXiv math/0309224 (page consultée [P], contenu non exploité), cs/0608208. [S]
- **Bernstein** (1994), *Proc. AMS* 121, 405–408. [S] $\Phi^{-1}(\sum2^{d_i})=-\sum2^{d_i}/3^{i+1}$ (positions des impairs) ; équivalente à B1.
- **Bernstein–Lagarias** (1996), *Canad. J. Math.* 48, 1154–1169 : application de conjugaison. [S]

## Densités, « presque toutes » les orbites
- **Korec** (1994) : minimum $<n^\theta$, $\theta>\log3/\log4$, densité naturelle. [S, via Tao]
- **Tao** (2022), *Forum Math. Pi* 10, e12 (arXiv 1909.03562) : minimum $<f(n)$ pour presque tout $n$ en densité **logarithmique**. [S ; accès 403 antérieurs]
- **Inselmann** (2024), arXiv 2402.03276 : $n^\varepsilon$ en densité naturelle — **préprint**, non audité. [S]
- **Krasikov–Lagarias** (2003), *Acta Arith.* 109 : $\gg x^{0,84}$ départs atteignant 1. **Applegate–Lagarias** (1995) :
  programmes linéaires, stricte croissance des seuils annoncée (PR #7). [P-dép]
- **Applegate–Lagarias** (2003), *Math. Comp.* 72 : bornes inférieures des temps d'arrêt totaux ($\ge6{,}14\log n$ infiniment souvent). [S] Pertinent pour H6.

## Cycles
- **Steiner** (1977) 1-cycles ; **Simons–de Weger** (2005), *Acta Arith.* 117 : pas de $m$-cycle pour $m\le68$. [S]
- **Hercher** (2023), *J. Integer Seq.* (arXiv 2201.00406) : $m\le91$ ; corrigendum et préprint Wang ($m\le95$) **non vérifiés** (PR #12, #14). [P-dép partiel]
- **Eliahou** (1993), *Discrete Math.* 118 : longueur minimale d'un cycle non trivial via fractions continues de $\log_23$. [S]
- Vérification numérique (Barina) jusqu'à $2^{68}$ (2020/21), annonces ultérieures plus hautes. [S] Non utilisée comme prémisse.

## Indécidabilité, opérateurs, analyse (axes A et C)
- **Conway** (1972) : problèmes de Collatz généralisés indécidables ; **Kurtz–Simon** (2007) : $\Pi^0_2$-complétude. [S]
  Conséquence de méthode : toute preuve doit exploiter la structure propre de $3x+1$.
- **Berg–Meinardus** (1994, 1995) : équations fonctionnelles holomorphes équivalentes à la conjecture. [S]
- **Wirsching** (1998), *LNM* 1681 : densités de prédécesseurs, équations fonctionnelles. [S]
- **Mori** (2024), arXiv 2411.08084 (« operator theory » et Collatz) : présent dans les références de muaijaz, non lu. [S]

## Complexité des itinéraires, valuations, transcendance
- **Dubickas** (2009), *Glasgow Math. J.* 51, 243–252, thm 5 : $p(L)>1{,}70951129\,L$ pour une trajectoire positive tendant vers l'infini. [P-dép, PR #21]
- **Yu** (1999), *Acta Arith.* 89, 337–378 : formes logarithmiques p-adiques ; conséquence p. 337 utilisée pour (V). [P-dép, PR #25]
- **Garcia–Tal** (1999), *Acta Arith.* 90, 245–250 : rareté des valeurs d'une orbite (sommabilité des inverses). [S, via dépôt externe]
- **Krattenthaler–Rochev–Väänänen–Zudilin** (2009), *Acta Arith.* 136 : irrationalité **réelle** de valeurs de Tschakaloff ; ne vaut pas dans $\mathbb Q_2$. [P-dép, PR #24]
- <a id="vw1989"></a>**Väänänen–Wallisser** (1989), *Manuscripta Math.* 65, 199–212, DOI 10.1007/BF01168299. **[P]**
  Scan GDZ : `https://gdz.sub.uni-goettingen.de/download/pdf/PPN365956996_0065/PPN365956996_0065.pdf`,
  SHA-256 `33d6870dba004ac09023ab8356466a5e3ef36bfd9db9e94d08cd6cded8b60ab2`, pp. 199–202 = indices 201–204. Non redistribué.
  **Satz (pp. 200–201), transcription :** soient $l,\sigma$ entiers $\ge0$, $q=r/s\in\mathbb Q$, $(r,s)=1$, $|r|>1$, $s\ge1$,
  $h=\max(|r|,s)$ ; $\alpha_1,\dots,\alpha_l\in\mathbb Q^\times$ avec $\alpha_i/\alpha_j\ne q^n$ ($n\in\mathbb Z$, $i\ne j$) ; $p$ premier ou $\infty$, et
  $\gamma=\delta(p)+\log|s|_p/\log h<\Gamma(l,\sigma)=\dfrac{2l(\sigma+1)+1-\sqrt{1+4l^2(\sigma+1)^2}}{2l(\sigma+1)}$, $\delta(\infty)=0$, $\delta(p)=1$.
  Pour $L=h_0f(0)+\sum_{\tau\le\sigma}\sum_{j\le l}h_{\tau,j}f^{(\tau)}(\alpha_j)$, coefficients entiers non tous nuls, et tout $\varepsilon>0$,
  il existe $\Lambda(q,p,\alpha,l,\sigma,\varepsilon)>0$ effective avec $|L|_p>\Lambda H^{-\delta(p)-\theta-\varepsilon}$,
  $\theta=\dfrac{2l(\sigma+1)-1+\sqrt{1+4l^2(\sigma+1)^2}}{2-\gamma\,(2l(\sigma+1)+1+\sqrt{1+4l^2(\sigma+1)^2})}$, $H=\max|h|$.
  Ici $f(x)=\sum_{n\ge0}q^{-\binom{n+1}2}x^n$. *Bemerkung* : (2) implique $|q|_p>1$.
  **Aucune condition sur $|\alpha|_p$** : la réserve de la PR #24 sur $\alpha=2$ est levée. Preuve non reproduite ici.
- **Väänänen–Wallisser** (1991), *J. Number Theory* 39 : cas $0<|q|_p<1$, **différent**. [P-dép]

## Travaux du dépôt et dépôts externes
- `msharpe248/collatz@ec8174b5` (Lean) : audit ciblé sur `main`. Annonces KL14 et $\Omega(x^{0,8676})$ non recompilées.
- `muaijaz/not-an-ai-collatz-proof@535044be` : VW 1989 appliqué à $q=9/4,\ \alpha=9/2$ (soit $c=2,d=-2$ dans B2), « échelle $J_m/K_m$ ». [P pour le dépôt]
- **Rozier–Terracol**, arXiv 2502.00948 v5 (*Discrete Math.* 2026) : correction extrémale, bornes harmoniques. [P-dép, PR #10]
- **De Jesús** (2026), manuscrit non expertisé sur les points rationnels de l'application de conjugaison. [S] Pertinent pour H4.
- **Cycle 003, lectures ciblées.**
  - **Monks–Yazinski** (2004), *Discrete Math.* 275, 219–236, thm 2.7(b). **[P]** Énoncé lu sur le PDF d'auteur `https://monks.scranton.edu/files/pubs/AutoConjV13.pdf` : orbite rationnelle divergente $\Rightarrow$ $\liminf \kappa_n/n\ge\ln2/\ln3$. Ne couvre pas B8 (densité des $1$ égale à $1$).
  - **López–Stoll**, arXiv:2101.12747, thm 1 et §6. **[P]** pour cette preuve. Ils annoncent l'égalité de cette densité avec $\ln2/\ln3$. Le pas final, via (15)–(16), identifie la somme réelle et la somme 2-adique. Non utilisé (même distinction que X14). Témoin local : $2^n/(1+2^n)\to1$ dans $\mathbb R$ et $\to0$ dans $\mathbb Q_2$. L'énoncé général reste non vérifié au-delà de ce pas.
  - **De Jesús**, *A drift-sensitive complexity bound…*, DOI `10.5281/zenodo.23108509`. **[S]** Résumé seul : complexité des facteurs contre dérive normalisée. Mécanisme différent de B7. Preuve non lue. La revue `6080964566` laisse aussi ce manuscrit non vérifié.
  - **Bernstein–Lagarias (1996)** : non relu dans ce dépôt. La même revue affirme que §1, (1.5)–(1.6), confirme la conjugaison et la conjecture de périodicité. Statut inchangé : non relu.
- **Cycle 004, lectures ciblées.** La comparaison $\varphi>\log_2 3$ est classique et prouvée dans le cycle par $125>121$ et $256>243$. Le mot sturmien de Fibonacci (point fixe de $0\mapsto01$, $1\mapsto0$) a des runs bornés : ce n'est pas le mot de B9. Les facteurs $0110$ et $1111$ du mot de B9 ont deux et quatre $1$, donc il n'est pas équilibré. Ce décompte est direct. La revue `6081458173` cite Lothaire, *Algebraic Combinatorics on Words*, §2.1, théorème 2.1.13, pour le critère d'équilibre ; ce texte n'a pas été relu ici et n'est pas une prémisse. La revue `6081410834` ne change pas les statuts de lecture de ce paragraphe. **De Jesús**, résumé SSRN du 23 septembre 2026 (tout mot sturmien aurait une image 2-adique irrationnelle). **[S]**, non lu, et hors sujet pour B9. Les comptages de Fibonacci liés au facteur $11$ ou à l'arbre inverse portent sur d'autres objets ; non utilisés. Monks–Yazinski, déjà [P] au cycle 003, ne donne pas B9.
- **Fernández–Ibáñez** (2026), arXiv 2607.24844 (mots de Christoffel) ; **Nikpour–Rabbani** (2026) (KL, Perron–Frobenius). [S]
