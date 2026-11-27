# Agenda de recherche (priorisé)

Revues déjà traitées : [reviews.md](reviews.md). Ne pas reprendre un identifiant qui y figure.

La **première entrée** est la prochaine question à traiter. Un cycle = une expérience ciblée :
énoncé réfutable → contre-exemple (symbolique d'abord, calcul exact borné ensuite) → preuve ou
réfutation → comparaison à la littérature → `cycles/cycle-NNN.md`. Axes : **A** fonctions de descente,
certificats de terminaison ; **B** intégralité réel ↔ 2-adique ; **C** opérateurs de transfert,
analyse complexe, spectral. Mémoire : [proved](proved.md) · [hypotheses](hypotheses.md) ·
[counterexamples](counterexamples.md) · [prior_art](prior_art.md) · [abandoned](abandoned.md) · [cycles](cycles/).

## 1. [B] Frontière de Tschakaloff sur un run quasi linéaire — PROCHAINE QUESTION (cycle 006)
Mot à un zéro par bloc, $r_j=j+[j\text{ impair}]$. La réalisation 2-adique est-elle une
combinaison $\mathbb Q$-linéaire de deux valeurs $f_q(\alpha_i)$ ? Si oui, l'un des énoncés
de Bézivin, Bundschuh ou Amou–Väänänen l'exclut-il de $\mathbb Z_{(2)}$ ? Lire l'énoncé avant
toute preuve et y vérifier l'obstruction $\Gamma(2,0)<\gamma$. Dépend : B1, B2. Pas une
relecture de VW 1989.

## 2. [C] Revue ciblée : opérateurs de transfert et équations fonctionnelles
Lire Berg–Meinardus, Wirsching (LNM 1681), Mori 2024 ; extraire **un** énoncé réfutable (par ex. une
prédiction d'un tronqué fini) avant tout calcul. Documentaire d'abord. Aucune dépendance.

## 3. [B, long terme] (C) densité orbitale positive (H1)
Pas d'attaque directe sans mécanisme nouveau. Réductions connues : pente $>1/\beta$ ⇔ (C) ;
(H) ⇒ (C) uniforme, désormais prouvé (B6), avec $\eta_N\ge1/(A+1)$. (H) elle-même est la
conjecture majeure H2 : ne pas la reprendre comme petit lemme.

## 4. [Validation] Relecture humaine du scan VW 1989, pp. 200–201
Confirmer la transcription de `prior_art.md` (ambiguïté typographique `l`/`1`). Faible coût ; consolide B2.

## Historique
- Cycle 005 (26 nov. 2026) : si $\rho h/\ell\le3/2$, alors $5\cdot2^t>2\cdot3^L$
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
