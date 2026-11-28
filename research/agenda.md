# Agenda de recherche (priorisé)

Revues déjà traitées : [reviews.md](reviews.md). Ne pas reprendre un identifiant qui y figure.

La **première entrée numérotée** est la prochaine question à traiter, sauf si le blocage ci-dessous est encore ouvert. Un cycle = une expérience ciblée :
énoncé réfutable → contre-exemple (symbolique d'abord, calcul exact borné ensuite) → preuve ou
réfutation → comparaison à la littérature → `cycles/cycle-NNN.md`. Axes : **A** fonctions de descente,
certificats de terminaison ; **B** intégralité réel ↔ 2-adique ; **C** opérateurs de transfert,
analyse complexe, spectral. Mémoire : [proved](proved.md) · [hypotheses](hypotheses.md) ·
[counterexamples](counterexamples.md) · [prior_art](prior_art.md) · [abandoned](abandoned.md) · [cycles](cycles/).

## Blocage
Le cycle 017 est le douzième de la fenêtre dont le plus ancien est
le cycle 006. Le commit `fcd6a00` est du 27 novembre 2026 à
00:25:31 UTC. Ne pas ouvrir le cycle 018 avant le 28 novembre 2026
à 00:26 UTC. La revue `6094283257` est enregistrée dans ce cycle :
confirmation du cycle 016 §9, sans correction.

## 1. [A] La borne d'Eliahou et les trajectoires non périodiques — PROCHAINE QUESTION (cycle 018), non entamée
Ne pas rouvrir Korec, Tao, Terras, Everett, Inselmann, la remarque
1.4, \(P(2)\), les conjectures 4.11 à 4.14, Steiner, ni les
\(m\)-cycles. Ne pas redémontrer une densité.

Eliahou, *Discrete Math.* 118 (1993), est une source secondaire :
une borne de longueur d'un cycle non trivial, par les fractions
continues de \(\log_2 3\). Lire l'énoncé primaire. Décider seulement
s'il exclut une trajectoire non périodique, ou seulement un cycle
dont le minimum est dans une plage écrite. S'il ne borne que le
nombre d'éléments d'un cycle, le classer hors des trajectoires
divergentes et ne pas redémontrer l'estimation. Ne pas importer une
vérification machine. Le paramètre \(m\) de Simons–de Weger et de
Hercher compte des minima, pas cette longueur. Ne pas ouvrir ce
cycle avant la fin du blocage ci-dessus.

## 2. [B, long terme] (C) densité orbitale positive (H1)
Pas d'attaque directe sans mécanisme nouveau. Réductions connues : pente $>1/\beta$ ⇔ (C) ;
(H) ⇒ (C) uniforme, désormais prouvé (B6), avec $\eta_N\ge1/(A+1)$. (H) elle-même est la
conjecture majeure H2 : ne pas la reprendre comme petit lemme.

## 3. [Validation] Relecture humaine du scan VW 1989, pp. 200–201
Confirmer la transcription de `prior_art.md` (ambiguïté typographique `l`/`1`). Faible coût ; consolide B2.

## Historique
- Cycle 017 (28 nov. 2026) : le théorème 1 de Korec, lu, donne la
  densité naturelle de \(M_c\) pour \(c>\log_4 3\). La densité
  relative dans chaque classe vaut \(1\) (B23). X34 empêche l'inclusion,
  et le prédicat n'est pas l'atteinte de \(1\). La phrase universelle
  de descente est fausse en \(y=1\) (X43). Le certificat \(S_m<md\)
  manque la classe \(-1\pmod{2^m}\) (X44). Pas une découverte, ni une
  contrainte sur une orbite. [cycle-017](cycles/cycle-017.md)
- Revue `6094283257` (27 nov. 2026, SHA `c3b02198`) : confirmation de
  la réduction du cycle 016 §9. \(P(2)\) équivaut à la conjecture
  4.14 et à la queue issue du premier \(5\pmod 8\). Aucune correction.
  Aucune des deux conjectures n'est résolue. Cycle 017 ensuite.
  Détail : [reviews.md](reviews.md).
- Revue `6094246430` (27 nov. 2026, SHA `6bd08925`) : B22, la
  valuation et l'implication directe de X42 confirmées. La
  formulation catégorique « 4.14 n'implique pas \(P(2)\) » est
  retirée. La queue issue du premier \(5\pmod 8\) reste à traiter.
  Aucune des deux conjectures n'est résolue. Le cycle 017 n'est pas
  ouvert. Détail : [reviews.md](reviews.md).
- Revue `6094223904` (27 nov. 2026, SHA `bab008e`) : B22, X41 et le
  seuil en un pas confirmés. La phrase « la conjecture 4.14
  impliquerait \(P(2)\) » est fausse (X42). L'orbite
  \(5\to 8\to 4\to 2\to 1\) évite \(7\pmod 8\) et rencontre \(5\).
  \(P(2)\) implique 4.14. La valuation \(r-i\) est celle de
  \(T^i(m)+1\). Le cycle 017 n'est pas ouvert.
  Détail : [reviews.md](reviews.md).
- Revue `6093952309` (27 nov. 2026, SHA `db5009a`) : X40 et B21
  confirmés. Aucune correction. Cycle 016 ensuite : \(P(2)\) est la
  conjecture 4.13 de Yolcu–Aaronson–Heule, arXiv:2105.14697v3 (B22).
  Elle reste ouverte. Steiner (1977) n'est pas obtenu.
  Simons–de Weger, version 1.44, ne traitent que les orbites
  périodiques. Détail : [reviews.md](reviews.md).
- Cycle 016 (27 nov. 2026) : l'évitement des runs impairs de longueur
  au moins \(3\) est l'évitement du résidu \(7\pmod 8\). Pour \(C\) et
  pour \(T\), ce résidu est rencontré ensemble, car \(3m+1\) ne vaut
  jamais \(7\pmod 8\). \(P(2)\) est donc la conjecture 4.13, non
  résolue. Le cycle \(-5\to-7\to-10\) évite ce résidu (X41). Pas une
  preuve de Syracuse. [cycle-016](cycles/cycle-016.md)
- Revue `6093923797` (27 nov. 2026, SHA `2a6474b`) : formule du
  bloc initial, cas \(R=1\), B21 et réduction à \(P(2)\) confirmés.
  La phrase « le retour au premier pas n'est pas une descente » est
  fausse (X40) : \(U(3)=5\) monte et \(U(9)=7\) descend. Le partage
  modulo \(4\) est élémentaire. \(P(2)\) n'est pas entamé. Steiner
  n'est pas ouvert. Simons–de Weger est cité et n'est pas ouvert.
  Le cycle 016 n'est pas ouvert.
  Détail : [reviews.md](reviews.md).
- Revue `6093856144` (27 nov. 2026, SHA `3679167`) : B21, X38, X39
  et le cas \(R=1\) confirmés. La formule close ne vaut pas au-delà
  du premier pair (X38 reste vrai). Le retour de B21 est strictement
  plus bas. La phrase alors écrite, « sans être une descente », est
  corrigée par la revue `6093923797` (X40). La montée de \(2911\)
  est écrite pour \(1\le t<5\). La question suivante est \(P(2)\).
  Steiner et Simons–de Weger ne sont pas ouverts. Le cycle 016
  n'est pas ouvert.
  Détail : [reviews.md](reviews.md).
- Revue `6093792860` (27 nov. 2026, SHA `c6737c04`) : B21 confirmé.
  Le rang \(0\) du pont reste dans la classe ; l'évitement commence
  au rang \(1\), avec \(s\ge\max(2,T-j+2)\). X38 : l'orbite
  \(1\to 2\to 1\) refuse la descente uniforme pour tout \(R\ge 1\).
  Le cas \(R=1\) est élémentaire. X39 : le mot de runs de \(5\) est
  constant et \(5\) n'est pas périodique ; une suite de parités
  périodique dès le départ est un cycle. Le théorème 1.2 de Terras
  est lu pour cette équivalence. Le cycle 016 n'est pas ouvert.
  Détail : [reviews.md](reviews.md).
- Revue `6093548562` (27 nov. 2026, SHA `8428d6cf`) : confirmation de
  X36. Aucune correction. Cycle 015 ensuite : aucune classe ne revient
  dans elle-même en temps uniforme (B21). Détail : [reviews.md](reviews.md).
- Cycle 015 (27 nov. 2026) : pour \(U\), aucun triple \((m,a,T)\) ne
  fait revenir toute la classe \(a\pmod m\) strictement plus bas en
  au plus \(T\) pas (B21). Le résidu autre que \(1\) n'a aucun terme
  positif plus petit que son minimum. La classe \(1\pmod m\) reçoit
  un cylindre de montée, directement si \(4\nmid m\), après un pont
  de divisions par \(4\) sinon. Pas une contrainte sur une orbite.
  [cycle-015](cycles/cycle-015.md)
- Revue `6093505644` (27 nov. 2026, SHA `8ec0299d`) : la densité
  \(2^{-(a+1)}\) est confirmée. La phrase « la classe entière ne
  l'est pas » est fausse pour \(f(N)=N+1\) (X36). Le théorème ne
  garantit pas qu'une classe entière soit bonne. Le cycle 015 n'est
  pas ouvert. Détail : [reviews.md](reviews.md).
- Revue `6093468477` (27 nov. 2026, SHA `be519ce6`) : la densité
  \(2^{-a}\) du cycle 014 §1 est fausse. La fibre \(v_2=a\) a densité
  \(2^{-(a+1)}\) (X35), et la somme jusqu'à \(A\) vaut
  \(1-2^{-(A+1)}\). Presque tout élément de chaque classe fixée passe
  sous \(f\). X34 est confirmé, y compris en densité naturelle. Le
  cycle 015 n'est pas ouvert. Détail : [reviews.md](reviews.md).
- Revue `6093045943` (27 nov. 2026, SHA `02bcbd97`) : correctif du
  cycle 013 confirmé. Bilans \(-84\) et \(148\), somme \(64\), seuils
  \(X_0<187\) et \(X_0<123\), trajet \(59\to 67\). Aucune correction.
  Cycle 014 ensuite : Tao 2022, théorème 1.3, n'exclut aucune classe
  de congruence (B20, X34). Détail : [reviews.md](reviews.md).
- Cycle 014 (27 nov. 2026) : le théorème 1.3 de Tao, lu sur le PDF de
  *Forum Math. Pi* 10 (2022), dit que l'ensemble exceptionnel a une
  densité logarithmique nulle. Chaque classe a densité \(1/m\), donc
  presque toute la classe passe sous \(f\), et aucune classe n'est
  entièrement exceptionnelle. X34 montre qu'une densité nulle peut
  couper toutes les classes. Pas une découverte, ni une contrainte
  sur une orbite. [cycle-014](cycles/cycle-014.md)
- Revue `6093000151` (27 nov. 2026, SHA `9e26d12`) : lemme 2, identité
  pondérée et réduction des lemmes 3 et 4 confirmés. Thorner–Zaman et
  Ramaré, cités par la revue, ne sont pas ouverts ici.
  Montgomery–Vaughan reste non obtenu. Correction : le bilan \(-84\)
  et \(148\) est celui de \(M=1\) ; les certificats finis s'arrêtent à
  \(X_0<187\) et \(X_0<123\) ; un trajet premier vers premier suffit
  pour \(M=8\) et \(X_0<59\) (X33). Le cycle 014 n'est pas ouvert.
  Détail : [reviews.md](reviews.md).
- Cycle 013 (27 nov. 2026) : la porte sur les compteurs est NO-GO.
  Le théorème 1 de la note du 19 octobre 2026 est l'énoncé demandé.
  Le lemme 2 et l'identité pondérée sont réécrits (B19). Les lemmes 3
  et 4 réduisent l'existence pour chaque module au théorème des nombres
  premiers en progression fixe et à Brun–Titchmarsh ; les PDF ne sont
  pas ouverts. Certificats élémentaires pour $M=24$ si $X_0<187$, et
  pour $M=1$ si $X_0<123$. Pas une
  découverte, ni une contrainte sur une orbite divergente.
  [cycle-013](cycles/cycle-013.md)
- Revue `6082966513` (27 nov. 2026, SHA `b033647`) : B18 confirmé.
  Aucune correction. Le cycle 013 vient après, une fois la fenêtre des
  douze cycles ouverte. Détail : [reviews.md](reviews.md).
- Revue `6082913526` (27 nov. 2026, SHA `41cced5e`) : X31 et B17
  confirmés. L'exception finie et le couple $(n\bmod M, v_2(n+1))$ sans
  compteurs sont fermés (B18, X32). Le théorème 1 de la note, avec
  compteurs, n'est pas adopté. Le cycle 013 n'est pas entamé.
  Détail : [reviews.md](reviews.md).
- Revue `6082845312` (27 nov. 2026, SHA `a29ba699`) : le correctif du
  cycle 011 est confirmé. Résidu \(-\lambda^\mu\), coefficient
  \(\lambda^{2\mu}\), équivalence \(a_n=a_{t(n)}\). Aucune correction.
  Cycle 012 ensuite : X31 et B17. Aucune fonction de la seule valuation
  \(v_2(n+1)\) n'est une fonction de Lyapunov stricte sans exception.
  Détail : [reviews.md](reviews.md).
- Cycle 012 (27 nov. 2026) : pour tout réel $c$,
  $\log_2(n+1)+c\,v_2(n+1)$ échoue hors de $\{1,2\}$ (X31). Pour toute
  fonction réelle $\Phi$, $\log_2 n+\Phi(v_2(n+1))$ et
  $\log_2(n+1)+\Phi(v_2(n+1))$ échouent sur $U$ en l'un de $3$, $7$, $9$
  (B17). Le §4(2) de Chang laisse cet énoncé ouvert ; son esquisse ne
  couvre pas une croissance rapide. Pas une preuve de Syracuse.
  [cycle-012](cycles/cycle-012.md)
- Revue `6082791301` (27 nov. 2026, SHA `ded6e1ce`) : B16 et X29
  confirmés. Le résidu du cycle 011 §5 vaut \(-\lambda^\mu\), pas
  \(\lambda^{2\mu}\) (X30). L'identité de séries reste vraie. La
  conjecture 3 équivaut à l'atteinte de \(1\) pour \(n\ge 1\) (§12),
  via \(a_n=a_{t(n)}\) et le théorème 1 de Meinardus 2001, lu. Pas de
  descente. Le cycle 012 n'est pas entamé. Détail : [reviews.md](reviews.md).
- Cycle 011 (27 nov. 2026) : la conjecture 2 de Berg–Meinardus 1995 est
  l'atteinte de $1$ pour $n\ge 1$ (B16). Le point $0$ s'en sépare (X29).
  La conjecture 3 est globale. Le théorème 3 ne contraint pas les orbites.
  Pas de lemme de descente. L'article de 1994 n'est pas lu.
  [cycle-011](cycles/cycle-011.md)
- Revue `6082693818` (27 nov. 2026, SHA `7b5a225`) : le correctif
  d'exemples du cycle 010 est confirmé. Exposants extraits $4$ et $1$,
  sorties $19$ et $1367$. Aucune correction. Cycle 011 ensuite.
  Détail : [reviews.md](reviews.md).
- Revue `6082671838` (27 nov. 2026, SHA `27bbb65a`) : le second bloc,
  \(\tau\ge k+L\) et la non-bornitude de \(\tau-k\) sont confirmés. Dans
  les exemples du cycle 010 §4, \(6\) et \(3\) sont les valuations du
  numérateur \(5\cdot3^{k+2}+1\), pas les exposants extraits par \(U\).
  Ceux-ci valent \(4\) et \(1\). Les formules ne changent pas. Prochaine
  question non entamée. Détail : [reviews.md](reviews.md).
- Revue `6082611497` (27 nov. 2026, SHA `462014b8`) : B15 et X28
  confirmés. La lecture « la formule uniforme s'arrête à la jonction »
  est corrigée. Pour $k$ impair $\ge3$, le second bloc de longueur
  $L=v_2(5\cdot3^k+1)-1$ reste explicite et $\tau\ge k+L$. L'excès
  $\tau-k$ n'est pas borné. Cela ne prouve pas $\tau>2k$ infiniment
  souvent. Le §4 de Wiltrout–Landquist porte sur le temps total, pas
  sur $\tau$. Convention $\tau=+\infty$ si l'ensemble est vide. Prochaine
  question non entamée. Détail : [reviews.md](reviews.md).
- Cycle 010 (27 nov. 2026) : le préfixe accéléré de $5\cdot2^k-1$ est
  connu. Pour $k\ge3$, la sortie $U^k$ reste au-dessus du départ, donc
  $\tau\ge k+1$ (B15). Pour $k$ impair $\ge3$, les orbites de $n_k$ et
  de $n_{k+1}$ se rejoignent au pas $k+1$, encore au-dessus (Wiltrout–
  Landquist, théorème 4, transporté vers $U$). Le second bloc est
  explicite et $\tau\ge k+L$. $\tau\le2k$ pour tout $k$ est faux
  (X28, $k=5$, $\tau=13$). Le relevé $2\le k\le1000$ ne prouve pas
  l'infinité de l'excès au-dessus de $2k$.
  [cycle-010](cycles/cycle-010.md)
- Revue `6082502361` (27 nov. 2026, SHA `c5ab6439`) : l'exclusion de
  $2+2^{66}$ au rang $2$ est confirmée. Aucune correction. Le résidu
  $u=956973825$ satisfait les deux valuations ; l'irrationalité reste
  ouverte. Cycle 010 ensuite. Détail : [reviews.md](reviews.md).
- Revue `6082438456` (27 nov. 2026, SHA `645ee7b8`) : les corrections
  de `6082358798` sont confirmées. Le candidat $2+2^{66}$ satisfait le
  rang $1$ et la borne de hauteur, mais $v_2(A_2)=74\neq96$ : il est
  exclu au rang $2$. L'irrationalité reste ouverte. Le cycle 010 n'est
  pas engagé. Détail : [reviews.md](reviews.md).
- Revue `6082358798` (27 nov. 2026, SHA `886b3059`) : B14, X24 et X25
  confirmés. Correction : $1^\infty$ réfute la phrase générale sur les
  runs périodiques (X26) ; la réciproque est H3, pas une réfutation ;
  $2+2^{67}$ est exclu par $v_2(a-2b)=66$ (X27) ; $U(1)=1$. Le cycle
  010 n'est pas engagé. Détail : [reviews.md](reviews.md).
- Revue `6082253067` (27 nov. 2026, SHA `e7c52409`) : B13 confirmée.
  Aucune correction. Cycle 009 ensuite : le signe moins n'est pas
  périodique (X24), $o_j$ n'est pas polynomiale sur une progression
  arithmétique (X25), et $\max(|a|,b)\ge(2^{66}+2)/3$ (B14).
  L'irrationalité reste ouverte. Prochaine question : descente
  accélérée de $5\cdot2^k-1$, non entamée.
  Détail : [reviews.md](reviews.md).
- Revue `6082191024` (27 nov. 2026, SHA `ff58fed`) : B13 confirmée.
  La définition de $t_*$ est corrigée pour $K\le1/2$. La constante $C$
  est $\log_2 K+J(\log_2 3)^2$. La forme uniforme de B10 n'est plus
  dite toujours plus serrée. Prochaine question inchangée, non entamée.
  Détail : [reviews.md](reviews.md).
- Revue `6082099628` (27 nov. 2026, SHA `eeaeb41`) : X23 et
  l'inégalité $P(m)\ge n$ confirmés. La phrase « premier point de
  $\Sigma$ » est vraie sous l'hypothèse de collision ; elle est conservée.
  La prémisse non pondérée est le cas $K=\rho$ du cycle 005. Cycle 008
  ensuite : B13, horizon global pondéré. Détail : [reviews.md](reviews.md).
- Cycle 008 (27 nov. 2026) : si un poids borné certifie une contraction
  $\Phi(T^t(n))\le\rho\Phi(n)$ pour tout $n\ge N_0$, alors
  $B(n)>\log_2 3\cdot\log_2 n-C$ pour une infinité de $n$ (B13). La
  constante est $C=\log_2 K+J(\log_2 3)^2$. Pour $K\le3/2$, la borne
  directe sur les Mersenne est $t>\delta L-\log_2 K$. [cycle-008](cycles/cycle-008.md)
- Revue `6082060844` (27 nov. 2026, SHA `a60a1a6`) : B12 confirmée.
  L'objection de fermeture est réfutée (X23). L'inégalité $P(m)\ge n$
  est justifiée. Les théorèmes 4.2.7 et 4.3.10 restent non adoptés.
  Prochaine question : l'implication globale de H6, non entamée.
  Détail : [reviews.md](reviews.md).
- Revue `6081994521` (27 nov. 2026, SHA `a288697`) : correctif X22
  confirmé. Aucune correction supplémentaire. Cycle 007 ensuite.
  Détail : [reviews.md](reviews.md).
- Cycle 007 (27 nov. 2026) : l'application non raccourcie atteint $1$
  si et seulement si le premier retour $P$ sur $\Sigma=N_1\cup N_2$
  ramène tout point à $1$ (B12). Antériorité Mori, prop. 4.3.3 ; preuve
  autonome. La paire de résidus de la prop. 4.3.2 est fausse ; les deux
  produits valent $4$. L'inégalité $P(m)\ge n$ est justifiée. L'objection
  de fermeture est réfutée (X23). Les théorèmes 4.2.7 et 4.3.10 ne sont
  pas adoptés.
  [cycle-007](cycles/cycle-007.md)
- Revue `6081961103` (27 nov. 2026, SHA `fcd6a00`) : B11 confirmée. La
  comparaison $Q_m<0$ dès $m\ge4$ est réfutée (X22). Avec $r_{m+1}$ et
  $\beta=\log_2(3/2)$, $\sup Q_m=Q_2=\log_2(2048/217)$ et $Q_m\to-\infty$.
  B7 n'exclut pas la rationalité. Prochaine question non entamée.
  Détail : [reviews.md](reviews.md).
- Cycle 006 (27 nov. 2026) : le mot $r_j=j+[j\text{ impair}]$ a pour réalisation
  $4\xi+1+2f_{81/16}(4)+f_{81/16}(9)=0$ dans $\mathbb Q_2$ (B11). VW 1989 ne
  s'applique pas ($\gamma>\Gamma(2,0)$). Les Satz 1 et 2 de Bundschuh 1974,
  lus, sont archimédiens et leur hypothèse échoue. Bézivin 1988 et
  Amou–Väänänen 2005 : originaux non obtenus, énoncés cités non 2-adiques
  pour ce $q$. Irrationalité ouverte. [cycle-006](cycles/cycle-006.md)
- Revue `6081884788` (27 nov. 2026, SHA `0b935a9`) : corrections du cycle 005
  confirmées. Aucune correction supplémentaire. Cycle 006 ensuite.
  Détail : [reviews.md](reviews.md).
- Revue `6081843230` (27 nov. 2026, SHA `ebba330`) : B10 et X21 confirmés.
  La comparaison $2^L+K-1\ge2^L$ est corrigée pour $0<K<1$. La borne s'écrit
  $3\cdot2^t>2\cdot3^L$. X21 ne réfute que l'obstruction locale ; l'implication
  globale de H6 reste ouverte. Prochaine question non entamée.
  Détail : [reviews.md](reviews.md).
- Cycle 005 (26 nov. 2026) : si $\rho h/\ell\le3/2$, alors $3\cdot2^t>2\cdot3^L$
  pour tout temps de contraction de $2^L-1$ (B10). Sans cette hypothèse, X21
  contracte chaque Mersenne en un pas. Le coefficient reste sous la borne
  d'Applegate–Lagarias 2003. [cycle-005](cycles/cycle-005.md)
- Revue `6081702521` (26 nov. 2026, SHA `7120654`) : comparaisons $Q_k>k$ et
  $Q_k<0$, borne $k+3$ et préfixe fini confirmés. Irrationalité du signe moins
  laissée ouverte, déjà dans le texte. Aucune correction. Cycle 005 ensuite.
  Détail : [reviews.md](reviews.md).
- Revue `6081622758` (26 nov. 2026, SHA `3bdc5da`) : proposition du seuil
  confirmée. Le test du signe plus compare désormais $Q_k>k$. Le signe moins
  n'exclut aucun réalisateur. Prochaine question non entamée.
  Détail : [reviews.md](reviews.md).
- Revue `6081531962` (26 nov. 2026, SHA `33c22a3`) : seuils stricts, préfixe
  fini et X20 confirmés. Le signe au seuil $\lambda=\log_2 3$ est justifié par
  deux familles (cycle 004 §8). Prochaine question non entamée.
  Détail : [reviews.md](reviews.md).
- Revue `6081458173` (26 nov. 2026, SHA `4696589`) : X20, la borne du préfixe
  exact et le corollaire en $\varphi$ confirmés. Portée corrigée : impairs
  positifs, préfixe fini fermé, extension à $\lambda>\log_2 3$. Prochaine
  question non entamée. Détail : [reviews.md](reviews.md).
- Revue `6081410834` (26 nov. 2026, SHA `8bc44f7`) : B9 et la borne du préfixe
  exact confirmés. L'implication « longueurs des runs ⇒ préfixe exact » est
  réfutée (X20) et le texte corrigé. $S_{k-1}$ désignait $o_k$. Prochaine
  question non entamée. Détail : [reviews.md](reviews.md).
- Cycle 004 (26 nov. 2026) : runs de Fibonacci, $Q_k>k$ pour tout $k$ (B9). Le réalisateur
  est irrationnel via B7. La branche « $Q$ bornée avant $\varphi$ » est fermée.
  Prochaine question : axe A, horizon d'un certificat à poids borné.
  [cycle-004](cycles/cycle-004.md)
- Revue `6081009622` (26 nov. 2026, SHA `aeb693b`) : certificat X19 et forme entière
  de $Q_m$ confirmés, revérifiés. Aucune correction. Prochaine question inchangée.
  Détail : [reviews.md](reviews.md).
- Revue `6080964566` (26 nov. 2026, SHA `0c90981`) : B7, B8 et X18 confirmés. La couverture
  du balayage borné (cycle 003 §5) est réfutée (X19) et le texte corrigé. Prochaine
  question inchangée. Détail : [reviews.md](reviews.md).
- Cycle 003 (26 nov. 2026) : critère de Liouville prouvé (B7). Le mot de runs $2^k$ est
  irrationnel (B8). Le mot triangulaire échappe au critère (X18). [cycle-003](cycles/cycle-003.md)
- Cycle 002 (26 nov. 2026) : (H) reclassée conjecture majeure. $B\le1$ réfuté pour tout $A$ (B4) ;
  fenêtres de longueur $\le K$ majorées (B5) ; (H) ⇒ (C) uniforme, et $A<1/\beta$ exclut les
  orbites non bornées (B6). Obstacle pour $1<B\le1+\delta$ consigné. [cycle-002](cycles/cycle-002.md)
- Cycle 001 (26 nov. 2026) : exclusion du mot triangulaire et des runs en progression arithmétique
  → **démontré via VW 1989** (B2, B3). [cycle-001](cycles/cycle-001.md)
