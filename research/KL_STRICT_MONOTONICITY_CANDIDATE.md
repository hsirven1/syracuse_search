# Candidat de démonstration : monotonie stricte des seuils de Krasikov-Lagarias

Date : 15 octobre 2026.

**STATUT : ARGUMENT MATHEMATIQUE A AUDITER, NON CERTIFIE PAR LEAN, NON SOUMIS A RELECTURE INDEPENDANTE.**
Ce dossier n'est PAS une « experience 38 » et ne prouve PAS Syracuse. On conserve une proposition
de preuve parce que l'enonce concerne une question explicitement ouverte dans Krasikov-Lagarias (2003),
p. 24, et que les controles contradictoires initiaux n'ont pas detecte d'erreur.

## 1. Contexte et priorite

Dans *Bounds for the 3x+1 problem using difference inequalities*, Acta Arith. 109 (2003),
Krasikov et Lagarias definissent le supremum des parametres admissibles lambda_k pour le
programme L_k^NT(lambda). Leur section 6, p. 24, prouve lambda_k <= lambda_(k+1) et dit
explicitement que prouver la stricte croissance est une question ouverte.
Original : https://websites.umich.edu/~lagarias/doc/krasikov.pdf

Les certificats de densite existent maintenant jusqu'a des niveaux bien superieurs a 11,
dont des annonces a k=17 dans msharpe248/collatz et un preprint de Nikpour-Rabbani
(SSRN 7239062, aout 2026) a k=20, gamma=0.914947. Ces annonces n'ont pas ete toutes
reproduites ici. L'approche de l'operateur non lineaire Perron-Frobenius existe donc
independamment avant notre travail et n'est pas revendiquee comme nouvelle.
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7239062

La question etudiee ici est DIFFERENTE : peut-on etablir lambda_(k+1)>lambda_k
pour **chaque** k>=2 ? Cela ne demontrerait ni lambda_k -> 2, ni convergence de Syracuse.

## 2. Definitions exactes et hypothesis a revalider a la source

Pour k>=2, M_k = {m mod 3^k : m = 2 mod 3}. Pour tout vecteur positif
c=(c_m)_(m dans M_k), posons alpha=log_2(3), et

 a=lambda^(-2), b=lambda^(alpha-2), d=lambda^(alpha-1).

On definit F_(k,lambda) par

 F(c)_m = a*c_(4m)
           + [m=2 mod 9]*b*min{c_v : v dans M_k, v=(4m-2)/3 mod 3^(k-1)}
           + [m=8 mod 9]*d*min{c_v : v dans M_k, v=(2m-1)/3 mod 3^(k-1)}.

Pour m=5 mod 9, seul le terme a*c_(4m) apparait. Les indices du premier terme
sont reduits mod 3^k, ceux des fibres min mod 3^(k-1).

**Hypothese de traduction H :** le programme L_k^NT(lambda), avec ses variables
auxiliaires et sa normalisation 1<=c_m<=C_max, est admissible si et seulement
s'il existe c>0 avec c<=F_(k,lambda)(c), pour 1<=lambda<=2.

La raison : chaque variable auxiliaire peut etre maximisee a la valeur min
de sa triple fibre; l'homogeneite autorise la normalisation du minimum
du vecteur positif a 1 et C_max son maximum. Cette correspondance doit etre
comparee ligne par ligne aux equations originales (L0)-(L3) et (2.8)-(2.14).
La construction coincide avec analysis/kl_exponent.py du depot msharpe248/collatz,
mais l'accord de deux programmes ne remplace pas un audit de l'article.

Soit lambda_k = sup {lambda dans [1,2] : il existe c>0, c<=F_(k,lambda)(c)}.

## 3. Lemmes proposes et chaine de preuve

### Lemme A : connectivite de 4

Pour k>=2, la multiplication m -> 4m modulo 3^k est un cycle unique de M_k.
En effet v_3(4^(3^j)-1)=j+1 (Lifting the exponent), donc 4 est d'ordre
3^(k-1), ce qui est egal a |M_k|. La permutation agit transitivement.

### Lemme B : vecteur propre positif et atteinte du seuil

Fixons k et lambda dans [1,2]. L'operateur F est continu, monotone,
positivement homogene et superadditif : F(x+y)>=F(x)+F(y) coordonnee par
coordonnee (min(x_i+y_i)>=min x_i+min y_i).

Sur le simplexe des vecteurs non negatifs de somme 1, l'application
c -> F(c)/sum F(c) est continue et bien definie (a>0, la permutation
m->4m impose sum F(c)>=a>0). Le theoreme de Brouwer produit un
vecteur v>=0 et un rho>0 tels que F(v)=rho*v.

La positivite stricte v>0 vient de la transitivite du terme a*c_(4m) :
si v_m=0, alors v_(4m)=0, donc toutes ses coordonnees seraient nulles.
La valeur propre rho est unique parmi les vecteurs propres strictement
positifs, par domination avec le rapport maximal de deux vecteurs.
Le meme argument montre :

       c>0 et F(c)>=c  <=>  rho>=1.

En effet au point ou c_m/v_m est maximal, F(c)_m <=
(max c/v)*rho*v_m; si F(c)_m>=c_m, alors rho>=1. La reciproque
prend c=v.

Par compacite du simplexe et unicite de rho, rho_(k,lambda) est
continu en lambda. Ainsi l'ensemble des lambda admissibles est ferme
et le supremum lambda_k est atteint.

### Lemme C : lambda_k<2 pour chaque niveau fini

A lambda=2, (a,b,d)=(1/4,3/4,3/2).
Chaque type de terme b ou d visite une fois toutes les fibres de M_(k-1).
Il s'ensuit, pour tout c>0 :

 sum_(m in M_k) F(c)_m
   = (1/4) sum c_m + (9/4) sum_(u in M_(k-1)) min_(j=0,1,2) c_(u+j*3^(k-1))
   <= sum c_m.

Si F(c)>=c, toutes les egalites sont necessaires. Donc c est constant
sur chaque fibre modulo 3^(k-1).

Au niveau k=2, cela impose c constant, impossible puisque la ligne
m=5 mod 9 impose c_m <= c_(4m)/4.

Au niveau k>=3, **identite de projection des fibres** : si c au niveau k
est un releve constant d'un vecteur e au niveau k-1, alors pour tout
m dans M_(k-1),

 min_(j=0,1,2) F_(k,lambda)(c)_(m+j*3^(k-1))
   = F_(k-1,lambda)(e)_m.                                     (P)

Le premier terme se projette sans changer; les trois valeurs de
(4m-2)/3 ou (2m-1)/3 parcourent les trois releves de la fibre
pertinente (4 ou 2 est inversible modulo 3). Le type modulo 9
ne change pas parmi les trois releves pour k>=3.

Si c>=0 est fibre-constant et F_k(c)>=c, alors (P) implique
F_(k-1)(e)>=e. Par induction descendante, lambda=2 est impossible
a tous les niveaux. Lemme B et fermeture donnent bien lambda_k<2.

### Lemme D : le releve strict existe des que c n'est pas fibre-constant

Definir (Lc)_m = c_(m mod 3^k) sur M_(k+1).
Pour tout c>0,

      F_(k+1,lambda)(Lc) >= L(F_(k,lambda)(c)).                (R)

Pour le terme a, on a egalite. Pour les termes b,d, une fibre de min
du niveau k+1 projette sur **une** classe u de M_k, donnant le terme
b*c_u ou d*c_u, tandis que le niveau k prenait le minimum des trois
classes modulo 3^k issues d'une fibre modulo 3^(k-1). D'ou (R).

Si c n'est pas constant sur l'une de ces fibres, choisir une classe
u avec c_u > le minimum de sa fibre. La correspondance
m -> (4m-2)/3 est bijective des classes m=2 mod 9 du niveau k+1
vers M_k. Il existe donc un m du type 2 mod 9 dont le terme b
augmente STRICTEMENT dans (R), car b>0. Ainsi

   c<=F_k(c), c non fibre-constant
   => Lc<=F_(k+1)(Lc), avec au moins une coordonnee stricte.

### Lemme E : une seule coordonnee stricte suffit

Supposons v>0, F(v)>=v, avec une inegalite stricte.
Les iteres F^t(v) sont croissants. Par

  F(x+h)_m >= F(x)_m + a*h_(4m)      pour h>=0,

une stricte augmentation se propage selon la permutation m->4m,
transitive par le lemme A. Pour N=|M_k|, on obtient

       F^N(v)>v   dans toutes les coordonnees.

Posons w=v+F(v)+...+F^(N-1)(v). Par superadditivite :

 F(w)>=F(v)+...+F^N(v)=w+F^N(v)-v>w.

Toutes les inegalites sont donc strictes; par continuite en lambda
et finitude du nombre de coordonnees, le meme w satisfait
F_(k,lambda+epsilon)(w)>=w pour un epsilon>0 suffisamment petit,
si lambda<2.

**Attention** : la preuve de propagation doit suivre la DIFFERENCE
F^(t+1)(v)-F^t(v), non supposer gratuitement que chaque iterand devient
strict en une seule etape. La somme des differences donne F^N(v)>v.

### Consequence candidate : stricte croissance

Au niveau 2, (c_2,c_5,c_8)=(3,2,3) est strictement admissible pour
lambda=1, donc lambda_2>1; et lambda_2<2 (lemme C). Un certificat
optimal c_2 ne peut etre constant, vu la ligne m=5. Par D puis E,
lambda_3>lambda_2.

Supposons lambda_k>lambda_(k-1) pour k>=3. Prenons un certificat
optimal c_k (lemme B). S'il etait constant par fibres, (P) produirait
un certificat de niveau k-1 a lambda_k, contredisant
lambda_k>lambda_(k-1). Donc c_k n'est pas fibre-constant. Par D,
son releve produit au moins une inegalite stricte au niveau k+1,
et par E, celle-ci peut etre rendue stricte partout puis prolongee
a un lambda>lambda_k puisque lambda_k<2. En consequence :

        ***lambda_(k+1) > lambda_k pour tout k>=2.***

**Statut : resultat conditionne a la correction INDEPENDAMMENT VERIFIEE
de chaque lemme et de la traduction H; ce texte n'est pas un certificat formel.**
Le programme de preuve est explicite, mais aucune originalite n'est revendiquee
sans revue bibliographique exhaustive et evaluation par mathematiciens.

## 4. Objections et pistes de contre-exemples

1. Peut-il exister une solution propre non strictement positive sur la
   frontiere du simplexe, rendant fausse l'atteinte de lambda_k ?
   Obstruction proposee : le terme a*c_(4m) sur un cycle transitif.
2. Peut-on projeter un releve constant sans perdre l'une des trois
   inegalites ? Controle par l'identite (P), validee en entiers rationnels.
3. (R) peut-elle etre une egalite partout malgre un fibre non constant ?
   Controle par la bijection de la classe type 2 modulo 9 vers M_k.
4. Une stricte coordonnee peut-elle rester localisee ? Controle par
   propagation de la difference et le cycle multiplicatif de 4.
5. La preuve λ_k<2 aurait-elle un faux comptage de fibres ? Controle
   par somme exacte, voir script.
6. Le schema de F est-il fidele au LP et ses variables auxiliaires ?
   **A REVERIFIER SUR LA VERSION PUBLIEE**, notamment la definition des
   sections et des bornes superieures des poids.
7. Des travaux posterieurs a 2003 prouvent-ils deja la stricte
   croissance ou les lemmes B-E ? Bibliographie actuellement
   **NON EXHAUSTIVE**. Nikpour-Rabbani (2026) couvre deja l'idee de
   Perron-Frobenius et l'infaisabilite pour lambda=2.

## 5. Verifications vraiment executees

La suite jointe est **independante du code numpy amont**. Uniquement
Python standard, arithmetique rationnelle Fraction, sans flottants.

Commande :

    python3 research/kl_strict_monotonicity_audit.py

Executions realisees :
- 468 tests des identites de releve, dont 408 avec une augmentation stricte;
- 468 tests de projection exacte (P);
- 156 identites de sommation pour lambda=2;
- 12 tests de superadditivite;
- verification des orbites de 4 modulo 3^k pour k=2,3,4,5;
- 125 vecteurs exhaustifs (valeurs 1..5) au niveau 2;
- 19683 vecteurs exhaustifs (valeurs 1..3) au niveau 3;
- certificat rationnel positif a k=3 et gamma=1/2 avec un slack minimum 185,
  pour coefficients minores exactement par 1/2, 43/50, 61/50.

Tous les tests ont passe. Ce sont des controles FINIS des identites
structurelles, pas une preuve generale ni une recompilation Lean.

## 6. Suite recommandee

1. Faire une relecture contradictoire **independante** du schema H et des
   lemmes A-E, chercher le PLUS PETIT contre-exemple exact.
2. Si elle survit, demander a Codex de formaliser les lemmes combinatoires,
   projection, releve et propagation en Lean 4 (sans sorry ni axiome ad hoc).
3. Ensuite seulement, examiner le lemme analytique de point fixe
   et la priorite bibliographique avec un mathematicien.

Pas de computation geante KL k=21, pas de modele Astra Pro,
pas de nouvelle experience numerotee.