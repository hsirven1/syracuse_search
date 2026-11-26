# Agenda de recherche (priorisé)

La **première entrée** est la prochaine question à traiter. Un cycle = une expérience ciblée :
énoncé réfutable → contre-exemple (symbolique d'abord, calcul exact borné ensuite) → preuve ou
réfutation → comparaison à la littérature → `cycles/cycle-NNN.md`. Axes : **A** fonctions de descente,
certificats de terminaison ; **B** intégralité réel ↔ 2-adique ; **C** opérateurs de transfert,
analyse complexe, spectral. Mémoire : [proved](proved.md) · [hypotheses](hypotheses.md) ·
[counterexamples](counterexamples.md) · [prior_art](prior_art.md) · [abandoned](abandoned.md) · [cycles](cycles/).

## 1. [B] Statut exact de la cible (H) de la PR #26 — PROCHAINE QUESTION (cycle 002)
Énoncer (H) avec ses quantificateurs ; consigner rigoureusement : (a) réfutation pour $B\le1$
(Mersenne ; famille $5\cdot2^{r_0}-1$, preuve redonnée sans dépendre des PR non fusionnées) ;
(b) (H) avec $A<1/\beta$ ⇒ aucune orbite non bornée, et tout (H) ⇒ (C) uniforme ;
(c) chercher une famille entière réfutant $B=1+\varepsilon$ (deux ou trois runs, petits $a$, $v_2(3^ra+1)$ grand)
ou expliquer l'obstacle. Sortie attendue : reclasser (H) comme conjecture majeure et fermer la piste « petit lemme ».
Dépend : X8 ; $\eta_N\le\beta/\delta$ (élémentaire). Voir H2.

## 2. [B] Critère de Liouville pour les réalisations rationnelles (H4)
Rédiger et vérifier la preuve ; tester sur les cycles rationnels connus ($3x+b$, $b$ petit) ;
situer par rapport à Lagarias 1985/1990, Bernstein–Lagarias 1996 et au manuscrit De Jesús 2026.
Intérêt : côté conjecture de périodicité, pas (C). Dépend : B1.

## 3. [B] Frontière de la méthode de Tschakaloff (H5)
Quelles familles de mots se ramènent à des valeurs $f_q(\alpha)$ ? Runs $cj+d+p_j$ ($p$ périodique) ⇒ $l\ge2$,
hors de portée de VW ($\Gamma(2,0)<\gamma$). Rechercher des mesures p-adiques plus fortes (Bézivin, Bundschuh,
Amou–Väänänen…) **avant** toute tentative de preuve. Dépend : B2.

## 4. [A] Certificats à poids bornés et horizon $B(n)$ (H6)
Rédiger la borne $B(n)\ge\delta\log_2n-O(1)$, la comparer à Applegate–Lagarias 2003 ; puis caractériser
une classe de certificats qui échappe aux no-go (poids non bornés structurés, horizons dépendant de $v_2(n+1)$).
Garde-fou : Conway/Kurtz–Simon ⇒ la méthode doit utiliser la structure propre de $3x+1$. Dépend : A2, A5.

## 5. [C] Revue ciblée : opérateurs de transfert et équations fonctionnelles
Lire Berg–Meinardus, Wirsching (LNM 1681), Mori 2024 ; extraire **un** énoncé réfutable (par ex. une
prédiction d'un tronqué fini) avant tout calcul. Documentaire d'abord. Aucune dépendance.

## 6. [B, long terme] (C) densité orbitale positive (H1)
Pas d'attaque directe sans mécanisme nouveau. Réductions connues : pente $>1/\beta$ ⇔ (C) ; (H) ⇒ (C).

## 7. [Validation] Relecture humaine du scan VW 1989, pp. 200–201
Confirmer la transcription de `prior_art.md` (ambiguïté typographique `l`/`1`). Faible coût ; consolide B2.

## Historique
- Cycle 001 (26 nov. 2026) : exclusion du mot triangulaire et des runs en progression arithmétique
  → **démontré via VW 1989** (B2, B3). [cycle-001](cycles/cycle-001.md)
