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
- **Applegate–Lagarias** (2003), *Math. Comp.* 72, 1035–1049 ; arXiv:math/0103054. Énoncé du théorème 1.1 et formule (4) lus sur l'arXiv (cycle 005, relus jusqu'au théorème 1.1 lors de la revue `6081843230`) : $\sigma_\infty(n)>6{,}14316\log n$ infiniment souvent, coefficient $29/(29\log2-14\log3)$, et $\gamma(2^k-1)\ge(\log2+\log3)/(\log2)^2\approx3{,}729$. Après le sommet, le décompte correct est au moins $\log_2(3^k-1)$ pas, pas $\log_2(3^k)$ ; pour $k=2$, $8$ atteint $1$ en trois pas, et le coefficient de (4) subsiste. Leur $T$ est le nôtre, leur $\log$ est naturel. Preuve par arbres non refaite. Le coefficient de B10 est strictement plus petit. [P pour ces deux énoncés]

## Cycles
- **Steiner** (1977) 1-cycles ; **Simons–de Weger** (2005), *Acta Arith.* 117 : pas de $m$-cycle pour $m\le68$. [S]
- **Hercher** (2023), *J. Integer Seq.* (arXiv 2201.00406) : $m\le91$ ; corrigendum et préprint Wang ($m\le95$) **non vérifiés** (PR #12, #14). [P-dép partiel]
- **Eliahou** (1993), *Discrete Math.* 118 : longueur minimale d'un cycle non trivial via fractions continues de $\log_23$. [S]
- Vérification numérique (Barina) jusqu'à $2^{68}$ (2020/21), annonces ultérieures plus hautes. [S] Non utilisée comme prémisse.

## Indécidabilité, opérateurs, analyse (axes A et C)
- **Conway** (1972) : problèmes de Collatz généralisés indécidables ; **Kurtz–Simon** (2007) : $\Pi^0_2$-complétude. [S]
  Conséquence de méthode : toute preuve doit exploiter la structure propre de $3x+1$.
- **Berg–Meinardus** (1995), *Rostock. Math. Kolloq.* 48, 11–18. **[P]** pour les conjectures 1 à 3, les théorèmes 1 à 3 et les équations (15)–(19), (21)–(22), lus sur le rendu du PostScript `http://www.math.uni-rostock.de/math/pub/romako/heft48/berg2.ps`, SHA-256 `d0a1a38e8b156372415f33b1b374d0670cd54390e17495a5dd28a0540aded639`, 8 pages, non redistribué. La conjecture 2 est l'atteinte de \(1\) pour \(n\ge 1\) (B16). La conjecture 3 est globale. Le théorème 3 ne contraint pas les orbites. **Berg–Meinardus** (1994), *Results Math.* 25, 1–12, DOI `10.1007/BF03323136`. **[S]** : PDF non obtenu. La note de 1995 y renvoie les preuves d'équivalence. Cette preuve n'est pas une prémisse.
- **Wirsching** (1998), *LNM* 1681 : densités de prédécesseurs, équations fonctionnelles. [S]
- **Mori** (2025), arXiv:2411.08084v2, 3 février 2025. **[P]** pour la proposition 4.3.3, les définitions des §§2–4 utilisées au cycle 007, et, après X23, la définition « Cyclic vectors » et le lemme `lem:Equality 1` dans la source TeX. PDF `https://arxiv.org/pdf/2411.08084`, SHA-256 `e852509294f8698923aa31aa827cbdc0353b861fc24441b73558946b2874c92b`, 27 pages. Source TeX de l'e-print v2, SHA-256 `19ab8b0a912a81b3f0aa3a98a7db8a16ef7fb097f641b7001efb485726e50372`. Non redistribués. L'équivalence au premier retour est re-prouvée (B12). Les théorèmes 4.2.7 et 4.3.10 ne sont pas adoptés. Kadison (1957), cité par la revue `6082060844` et non par une preuve d'ici, n'a pas été lu. La version d'*Advances in Operator Theory* et le §5 ne sont pas lus comme prémisses.

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
- **Cycle 005, lectures ciblées.** Applegate–Lagarias 2003, introduction jusqu'au théorème 1.1, comme ci-dessus. La comparaison des coefficients est élémentaire : $\log3/(\log2)^2$ contre $(\log2+\log3)/(\log2)^2$. Conway 1972 et Kurtz–Simon 2007 ne sont pas relus ; ils restent le garde-fou de méthode déjà en mémoire. Aucune autre source.
- **Cycle 011, lectures ciblées.** Berg–Meinardus 1995, comme ci-dessus. Le §4 de la note et l'équation intégrale (20) ne sont pas des prémisses. L'article de 1994 n'a pas été obtenu. Lagarias 1985, cité par la note pour l'énoncé de la conjecture, n'a pas été relu. Wirsching, *Discrete Math.*, « to appear » dans la bibliographie de 1995, n'a pas été lu.
- **Cycle 007, lectures ciblées.** Mori, arXiv:2411.08084v2, comme ci-dessus. Berg–Meinardus et Wirsching (LNM 1681) ne sont pas relus dans ce cycle ; la note de 1995 est lue au cycle 011. Conway, *A course in operator theory* (2000), cité par Mori pour le théorème 3.4.6, n'a pas été lu.
- **Cycle 010, lectures ciblées.**
  - **Wiltrout–Landquist** (2016), *Furman Univ. Electron. J. Undergrad. Math.* 17, 1–5. **[P]** pour le théorème 1, le théorème 4 (cas $b\equiv1\pmod4$, $k$ pair) et le §4. Rendu du dépôt `https://scholarexchange.furman.edu/cgi/viewcontent.cgi?article=1028&context=fuejum`. L'en-tête de ce rendu porte aussi 2013. Le PDF brut a répondu 403 : pas d'empreinte SHA-256. La revue `6082611497` n'a pas non plus obtenu le texte intégral et ne confirme pas la numérotation. Leur $T$ est le Terras du dépôt. Le théorème 1 donne $T^{(k)}(2^kb-1)=3^kb-1$. Le théorème 4 donne la jonction en $(3^kb-1)/4$ et la différence des temps totaux d'atteinte de $1$. Le §4 laisse ouverte une formule de ce temps total. Ni $\tau_U$, ni la comparaison à $2k$. Ce §4 n'exclut pas une formule de première descente : le second bloc est le cycle 010 §4, et la formule complète de $\tau$ reste ouverte.
  - Wikipedia, « Collatz conjecture », section Syracuse function, puce $f^{p-1}(2^ph-1)=2\cdot3^{p-1}h-1$. **[S]** : lue sur le rendu obtenu pour ce cycle, pas une source primaire. Pour $h=5$ c'est $U^{k-1}(n_k)$.
  - Le préprint Zenodo sur la résistance modulaire avant la première descente répète le préfixe $t\le m-1$. **[S]**, non lu, pas une prémisse.
- **Cycle 009, lectures ciblées.** Aucun PDF nouveau. Le HTML public d'arXiv:1805.00133 a été lu assez pour y retrouver la conjecture de périodicité comme conjecture (leur Conjecture 1), pas comme théorème. Ce n'est pas une prémisse de B14, et le PDF n'a pas été certifié. Les annonces sturmiennes rencontrées (SSRN, arXiv:2610.02601) n'ont pas été lues. Le mot du signe moins n'est pas équilibré (cycle 009 §5) : ces annonces ne le contiennent pas et ne sont pas des prémisses. X24 et X25 sont internes. B14 est le rang $m=1$ du mécanisme de valuation du cycle 003. Le rang $m=2$ du même mécanisme exclut $2+2^{66}$ ; ce n'est pas un théorème de Tschakaloff. La revue `6082358798` cite Bernstein–Lagarias 1996, §1, (1.5)–(1.6), pour la conjugaison et pour le statut conjectural de la périodicité. La revue `6082438456` renvoie à la même source. Ce PDF n'a pas été ouvert. La correction retire seulement l'affirmation « la réciproque est fausse » et l'ouverture de $2+2^{66}$ : elle n'adopte pas cette source.
- **Cycle 008, lectures ciblées.** Aucune source nouvelle. B13 réutilise la montée de Mersenne et le chaînage déjà décrit pour `no_finite_certificate` dans l'audit ; A5 exclut un horizon fixe, pas la borne logarithmique. Applegate–Lagarias 2003, déjà [P] pour le théorème 1.1 et la formule (4), borne le temps d'atteinte de $1$, pas le premier temps de contraction de $\Phi$. Ces textes ne sont pas relus ici et ne sont pas des prémisses de B13.
- **Cycle 006, lectures ciblées.**
  - **Bundschuh** (1974), *Portugaliae Math.* 33, 1–17, Satz 1 et Satz 2, page imprimée 2. **[P]** pour ces deux énoncés. Scan `https://purl.pt/2719`, fichier PDF public, SHA-256 `ce7657b2fc46fd352eab9f5caff063d7e49697fe910a6348cac7375b3f85c7c8`. Fonction archimédienne $\sum z^n q^{-n(n-1)/2}$. Hypothèse $|q_1|>|q_2|^{(3+\sqrt5)/2}$, soit $\log|q_2|/\log|q_1|<(3-\sqrt5)/2$. Preuve non lue. Ne s'applique pas à $q=81/16$, ni à la valeur 2-adique.
  - **Väänänen** (2009), RIMS Kôkyûroku 1665, 47–59. **[P]** pour ce survey. PDF `https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1665-08.pdf`, SHA-256 `fc5045b5207441a7d2091b20e99688961be096cd506d3f5b5929a663cc4804f2`. Il cite le théorème 5 de Bézivin 1988 comme une indépendance aux places infinies, et place Amou–Väänänen 2005 parmi les résultats archimédiens à paramètre entier. Ce n'est pas une lecture des originaux.
  - **Väänänen–Zudilin** (2007), Russian Math. Surveys 62, note. **[P]** pour cette note. PDF `https://wain.mi-ras.ru/PS/chak-br.pdf`, SHA-256 `10ae0ac2b3952174e8cd227dea939d4e6aabb9148b94ddd196483e2cfad85a87`. Théorème 1 : $q\in\mathbb Z\setminus\{0,\pm1\}$. Cite Amou–Väänänen, Monatsh. Math. 144 (2005), 1–11, sans le remplacer.
  - **Bézivin** (1988), Manuscripta Math. 61, 103–129, et **Amou–Väänänen** (2005), Monatsh. Math. 144, 1–11. **[S]** : originaux non obtenus. Pas des prémisses. Le compte rendu zbMATH 1066.11031 n'a pas été confronté au PDF.
  - Le Satz de VW 1989 n'a pas été relu. L'obstruction $\gamma>\Gamma(2,0)$ pour $q=81/16$ est un calcul interne (cycle 006 §4).
- **Cycle 004, lectures ciblées.** La comparaison $\varphi>\log_2 3$ est classique et prouvée dans le cycle par $125>121$ et $256>243$. Le mot sturmien de Fibonacci (point fixe de $0\mapsto01$, $1\mapsto0$) a des runs bornés : ce n'est pas le mot de B9. Les facteurs $0110$ et $1111$ du mot de B9 ont deux et quatre $1$, donc il n'est pas équilibré. Ce décompte est direct. La revue `6081458173` cite Lothaire, *Algebraic Combinatorics on Words*, §2.1, théorème 2.1.13, pour le critère d'équilibre ; ce texte n'a pas été relu ici et n'est pas une prémisse. La revue `6081410834` ne change pas les statuts de lecture de ce paragraphe. **De Jesús**, résumé SSRN du 23 septembre 2026 (tout mot sturmien aurait une image 2-adique irrationnelle). **[S]**, non lu, et hors sujet pour B9. Les comptages de Fibonacci liés au facteur $11$ ou à l'arbre inverse portent sur d'autres objets ; non utilisés. Monks–Yazinski, déjà [P] au cycle 003, ne donne pas B9. Les deux familles du seuil $\lambda=\log_2 3$ (cycle 004 §8, revue `6081531962`) sont un argument élémentaire interne à B7. Aucune source supplémentaire n'a été lue pour elles, et elles ne sont pas présentées comme un résultat nouveau de la littérature.
- **Fernández–Ibáñez** (2026), arXiv 2607.24844 (mots de Christoffel) ; **Nikpour–Rabbani** (2026) (KL, Perron–Frobenius). [S]
