# Agenda de recherche (priorisé)

Revues déjà traitées : [reviews.md](reviews.md). Ne pas reprendre un identifiant qui y figure.

La **première entrée** est la prochaine question à traiter. Un cycle = une expérience ciblée :
énoncé réfutable → contre-exemple (symbolique d'abord, calcul exact borné ensuite) → preuve ou
réfutation → comparaison à la littérature → `cycles/cycle-NNN.md`. Axes : **A** fonctions de descente,
certificats de terminaison ; **B** intégralité réel ↔ 2-adique ; **C** opérateurs de transfert,
analyse complexe, spectral. Mémoire : [proved](proved.md) · [hypotheses](hypotheses.md) ·
[counterexamples](counterexamples.md) · [prior_art](prior_art.md) · [abandoned](abandoned.md) · [cycles](cycles/).

## 1. [B] Seuil de Fibonacci pour le critère de Liouville — PROCHAINE QUESTION (cycle 004)
Mot $w=\prod_{k\ge1}(0\,1^{F_{k+2}})$, $F_1=F_2=1$, donc runs $2,3,5,8,\ldots$.
Alors $S_{k-1}=F_{k+3}-3$ et $R_k/S_{k-1}\to1/\varphi\approx0{,}618>\beta$.
Lemme réfutable : $Q_k\to+\infty$ (B7 s'applique) ou, au contraire, $2^{o_k+r_k+1}<3^{o_k}+P_k$
pour tout $k$ assez grand. Preuve visée : récurrence sur $F_k$, sans calculer $3^{F_n}$
très loin. Si $Q_k$ reste bornée, le critère s'arrête avant $\varphi$ et l'on passe à H5.
Dépend : B7. Une seule de ces deux issues ; pas de balayage.

## 2. [B] Frontière de la méthode de Tschakaloff (H5)
Quelles familles de mots se ramènent à des valeurs $f_q(\alpha)$ ? Runs $cj+d+p_j$ ($p$ périodique) ⇒ $l\ge2$,
hors de portée de VW ($\Gamma(2,0)<\gamma$). Rechercher des mesures p-adiques plus fortes (Bézivin, Bundschuh,
Amou–Väänänen…) **avant** toute tentative de preuve. Dépend : B2.

## 3. [A] Certificats à poids bornés et horizon $B(n)$ (H6)
Rédiger la borne $B(n)\ge\delta\log_2n-O(1)$, la comparer à Applegate–Lagarias 2003 ; puis caractériser
une classe de certificats qui échappe aux no-go (poids non bornés structurés, horizons dépendant de $v_2(n+1)$).
Garde-fou : Conway/Kurtz–Simon ⇒ la méthode doit utiliser la structure propre de $3x+1$. Dépend : A2, A5.

## 4. [C] Revue ciblée : opérateurs de transfert et équations fonctionnelles
Lire Berg–Meinardus, Wirsching (LNM 1681), Mori 2024 ; extraire **un** énoncé réfutable (par ex. une
prédiction d'un tronqué fini) avant tout calcul. Documentaire d'abord. Aucune dépendance.

## 5. [B, long terme] (C) densité orbitale positive (H1)
Pas d'attaque directe sans mécanisme nouveau. Réductions connues : pente $>1/\beta$ ⇔ (C) ;
(H) ⇒ (C) uniforme, désormais prouvé (B6), avec $\eta_N\ge1/(A+1)$. (H) elle-même est la
conjecture majeure H2 : ne pas la reprendre comme petit lemme.

## 6. [Validation] Relecture humaine du scan VW 1989, pp. 200–201
Confirmer la transcription de `prior_art.md` (ambiguïté typographique `l`/`1`). Faible coût ; consolide B2.

## Historique
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
