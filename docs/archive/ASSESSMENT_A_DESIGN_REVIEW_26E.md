# Assessment A — Critique design (26e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2778 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v53) · **Méthode :** lecture statique seule (Assessment A, aucun navigateur, aucun détecteur). Vérification des 4 claims de `2751ec4` (fix critique-25e) ligne par ligne — chaque ligne citée provient de `read_file` ou de `grep` direct, aucune de search_files. HEAD = `5180488` (docs uniquement), arbre git propre : l'état évalué est exactement le commit du fix.

**Note globale :** les 4 claims de `2751ec4` sont **tenus en code** — P2-1 (filet archive pour les espèces du guide masquées/supprimées), P2-2 (glyphe du verdict selon statut), P2-3 (normalisation + `aVerifier`), P3-1 (garde-fou voile/poignée/Escape) : 4/4 vérifiés. Chaque fix laisse un résidu précis : le filet archive ignore les **variétés perso** et les **synonymes/frappe** des espèces masquées ; le garde-fou ignore les **puces d'espèces du spot** et les **selects spot/météo**, et le bouton **Annuler** le contourne. Score **39/40** : +0,5 H4 (les deux collisions de valence 25E sont fermées, vérifiées en code), H5 maintenu à 3,5 (le trou principal est fermé, mais les résidus ci-dessus plafonnent l'heuristique de prévention des erreurs).

---

## 1. Verdict de spécificité design : 9/10 (inchangé)

Le diff du commit ne contient **aucun CSS** (41 insertions/15 suppressions, tout en JS + sw.js) : 0 couleur hors palette, 0 ombre floutée, 0 uppercase, 0 boîte système (le seul « window.confirm » du fichier est le commentaire l.235). Contrastes inchangés depuis 25E (4,61–13,5:1, tous AA). **Axes :** conceptuel ~90 % (carnet de chasse, vocabulaire mycologique, antipoison, verdicts ⚠️/☠️/✅) · visuel ~90 % (une capture sans texte révèle Memphis-automne-champignon). Verdict : spécifique sur les deux axes — la passe le prouve encore en creux : trois correctifs de sécurité/cohérence se fondent dans le langage sans le dégrader.

## 2. Évaluation holistique

- **Hiérarchie visuelle** — tenue. La carte idphoto (l.2482-2504) garde sa structure : badge, alertes et bouton fiche dérivent tous du même `r.statut` muté par le croisement. Le verdict-att de la fiche hybride retrouve un langage cohérent : ⚠️ pour comestible/prudence, ☠️ pour non-comestible — prédicat identique au rendu initial (`nonComestible` l.1449 vs `glypheAtt` l.1516).
- **Architecture de l'information** — le filet du flux photo consulte désormais l'archive (`infoEspeceArchive` l.1009-1017, branché l.2456). **Résidu :** le flux cueillette garde son propre patron (l.1531-1535) au lieu de partager la nouvelle fonction — deux fonctions d'archive coexistent encore (P3, cf. §9).
- **Adéquation émotionnelle** — les deux vallées 25E sont refermées : plus de ☠️ sur la carte ambre d'une chanterelle dès le premier coche (l.1516), et la carte « ✅ Comestible » + « confiance insuffisante » simultanés ne peut plus se produire quand le guide a résolu le statut (l.2468). Une petite vallée subsiste : le toast « confirmez la comestibilité » peut s'afficher sous une carte MORTEL corrigée par le guide (P3-1, §7).
- **Découvrabilité** — inchangé : rien au hover, bandeau clé, FAB contextuel, étapes progressives.
- **Composition** — colonne 640 px, feuilles 84 vh, grille 2 colonnes conservées ; la carte idphoto reste une carte unique pleine largeur.
- **Typographie** — inchangée (aucun CSS modifié) : Fredoka 400-700 exactement, Meta 400/12,5 px/0,85 conforme à DESIGN.md l.162.
- **Couleur** — 0 dérive. Contrastes 25E toujours valides (aucun hex, aucune opacité nouveaux dans le diff) : pastilles gris 6,08:1 · olive 4,61:1 · ambre 7,59:1 · toxique 4,67:1 · mortel 6,07:1 · blanc/rose 4,95:1 · blanc/cuir 5,45:1 · vert-mesure 4,97:1 · alertes 13,3-13,5:1. La Règle du Rouge Mortel tient.
- **Accessibilité** — l'ordre des branches Escape est **le bon** : `boiteVisible()` d'abord (l.1113-1119), feuille variété ensuite (l.1120-1125), feuille générique en dernier (l.1126-1127). La régression 17E (confirmations empilées) ne réapparaît **pas** : quand le garde-fou ouvre sa propre confirmation, l'Escape suivant est capté par la branche modale. Reste : `aria-invalid` = 0 partout (re-grep confirmé), lightbox sans piège à focus (résidu).
- **États** — boutons IA désactivés pendant les appels (l.1917, 2311), états vides honnêtes. La carte idphoto ne peut plus afficher deux langages contradictoires pour un même état (cas nominal).
- **Copy** — le message du garde-fou (« Quitter sans enregistrer ? Les champs remplis seront perdus. », titre « ⚠️ Feuille non enregistrée », l.1069) est Memphis et honnête. Le toast de coercition (l.2452) tire toujours **avant** le croisement guide (P3-1).
- **Cas limites** — dates locales, import versionné, checklist réindexée au retrait (l.2333-2337). Nouveau : masquer une espèce depuis sa propre fiche laisse la fiche ouverte (recharger ne re-rend pas le détail, l.2753-2758) — et le glyphe du verdict bascule alors sur ⚠️ même pour une espèce MORTELLE (P3-2, §7).

## 3. Évaluation de charge cognitive : 1 échec / 8 (inchangé)

1. Focus unique ✅ · 2. Chunking ≤ 4 ✅ · 3. Regroupement visuel ✅ · 4. Hiérarchie ✅ · 5. Une chose à la fois ✅ · 6. Choix minimaux ≤ 4 ❌ — **étape 1 = 5 champs** (nom, latin, comestibilité, saison, prudence) + 2 boutons + 1 encart ; inchangé depuis 21E · 7. Mémoire de travail ✅ — le croisement guide/IA réduit la charge au moment critique, et le filet couvre maintenant l'espèce masquée (le rangement n'est plus une condition de sécurité pour les espèces du guide) · 8. Divulgation progressive ✅.

**1 échec franc sur 8.**

## 4. Voyage émotionnel

Ouverture chaleureuse → guide → fiche hybride inchangés. **Les trois vallées 25E sont fermées dans leurs cas nominaux, vérifiées en code :** (a) la phalloïde **masquée** croise désormais le filet — `infoEspece` (visible) ne trouve rien, `infoEspeceArchive` cherche dans `ESPECES` complet, `archivee:true`, et le surclassement GRAV s'applique quand même (l.1010-1017 → l.2456-2460) ; (b) la chanterelle cochée affiche « ⚠️ Critères manquants », le ☠️ reste réservé aux non-comestibles (l.1516-1518) ; (c) un statut IA hors vocabulaire que le guide corrige ne force plus le double langage « ✅ + confiance insuffisante » (l.2468). **Vallées restantes, plus petites :** le toast de coercition peut contredire la carte corrigée (P3-1) ; le garde-fou laisse partir sans confirmation des champs réels (puces, selects — P2-2, P2-3) ; et l'espèce masquée depuis sa propre fiche voit son verdict perdre son ☠️ (P3-2). Fin de journée : rappel d'export honnête, pas de faux pic.

## 5. Scores heuristiques Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 4 | Toasts au bon endroit, boutons désactivés, compteur live, aria-valuetext |
| 2 | Correspondance monde réel | 4 | Vocabulaire du carnet de chasse ; « le guide a le dernier mot » — métaphore juste |
| 3 | Contrôle et liberté | 4 | Garde-fou étendu à spot/cueillette (voile/poignée/Escape), ordre Escape-modal vérifié l.1113-1128 |
| 4 | Cohérence et standards | **4** (+0,5) | Les deux collisions de valence 25E sont fermées (glyphe selon statut l.1516, aVerifier l.2468) — un seul langage par état sur l'écran de décision |
| 5 | Prévention des erreurs | **3,5** (=) | Le trou 25E est fermé pour les espèces du guide (nom exact) ; plafonné par les résidus : variétés perso masquées + synonymes/frappe hors du filet archive, garde-fou aveugle aux puces/selects |
| 6 | Reconnaissance vs mémorisation | 4 | Noms requêtables sous toutes leurs formes ; croisement normNom + synonymes + Levenshtein (visible) + archive exacte |
| 7 | Flexibilité / efficacité | 4 | IA remplit les 2 étapes, retry + repli modèle, ordre des images persistant, 21 guide:true (re-vérifié) |
| 8 | Esthétique minimaliste | 3,5 | Étape 1 à 5 champs, étape 2 ~13 éléments (inchangé) |
| 9 | Aide à la récupération d'erreurs | 4 | messageErreurIA par cause, parserJSONIA tolérant, import versionné, garde-fou de confirmation |
| 10 | Aide et documentation | 4 | DESIGN.md à jour ; les commentaires de code référencent la bonne passe (P2-1 (25e) l.1009, P2-2 (25e) l.1514, P2-3 (25e) l.2449, P3-1 (25e) l.1056) |

**Total : 39/40 (+0,5 vs 25E).** Les 4 correctifs 25E sont vérifiés ; H4 récupère son 4 (les incohérences de valence sont fermées en code) ; H5 reste à 3,5 tant que le filet archive n'inclut pas les variétés perso et que le garde-fou ne couvre pas tous les champs.

## 6. Forces spécifiques

1. **Le filet archive est le bon patron, au bon prix.** `infoEspeceArchive` (l.1010-1017) ne fait qu'étendre la fonction existante : le chemin visible garde toute sa finesse (synonymes, Levenshtein), le chemin archive est volontairement **exact** (pas de sur-appariement sur des espèces invisibles), et le flag `archivee` gouverne le seul rendu qui posait question — le bouton « Voir la fiche du guide » est masqué pour une espèce archivée (l.2499). La gravité, elle, voyage sans condition (l.2458) : la sécurité ne dépend plus d'un choix de rangement.
2. **La réparation de la régression 17E a survécu à l'ajout d'un nouveau chemin de confirmation.** Le garde-fou ouvre `confirmer()` (l.1069), mais la branche Escape teste `boiteVisible()` **avant** la branche feuille (l.1113-1127) : l'Escape n°2 ferme la confirmation, il ne la re-empile pas. C'est exactement le piège que la passe 17E avait payé cher — le nouveau code l'évite par construction.
3. **La discipline Memphis tient sur une passe 100 % logique.** Le diff ne touche pas une seule règle CSS : les correctifs de sécurité s'expriment dans le langage existant (badges, alertes, glyphes déjà dans la palette sémantique), preuve qu'un système de signaux bien conçu absorbe les changements de logique sans re-design.

## 7. Problèmes prioritaires

**P2-1 (RÉSIDU DU FIX 25E, SÉCURITÉ) — le filet archive ignore les variétés perso masquées/supprimées, et les synonymes/frappe des espèces masquées.** Le fallback cherche uniquement dans `ESPECES` (l.1014), alors que la suggestion 25E disait « ESPECES + Etat.especesCustom ». Une variété perso marquée MORTEL puis masquée 🙈 (fonction de premier plan, l.1471) disparaît du filet : IA « comestible, 95 % » → `connue.id = null` → badge vert possible. Et le fallback est **exact-match** : pour une espèce du guide masquée nommée par synonyme (« ange destructeur » pour l'amanite vireuse) ou avec une faute de frappe, `normNom(x.nom) === n` échoue (le nom du guide est « amanite vireuse ange destructeur ») alors que le chemin visible aurait matché par inclusion (l.999-1005). *Fix :* chercher aussi dans `Etat.especesCustom` (sans filtre de visibilité) ; pour les synonymes, répliquer le test d'inclusion sur l'archive, ou indexer les noms complets du guide une fois pour toutes.*

**P2-2 (RÉSIDU DU GARDE-FOU) — `feuilleSaisieSale` ignore des champs réels.** Spot : les puces « Espèces qu'on y trouve » (l.552-555) basculent `Etat.spot.especes` (l.1305-1311), persisté à l'enregistrement (l.1339) — mais le garde-fou ne teste que s-nom/s-desc/s-lat/s-lng + photo (l.1059). Cueillette : les selects `c-spot` et `c-meteo` (l.587-600) ne sont pas testés (l.1062). Taper une description est protégé ; choisir son spot et sa météo ne l'est pas — le voile avale le choix sans un mot. C'est le patron documenté « dirty-form guard that ignores selects/checkboxes » (P2). *Fix :* ajouter `Etat.spot.especes.length` côté spot, et `$('c-spot').value !== ''` / `$('c-meteo').value !== '🌞 Ensoleillé'` côté cueillette.*

**P2-3 (INCOHÉRENCE DE GESTES) — le bouton Annuler contourne le garde-fou sur deux feuilles, pas sur la troisième.** `s-cancel` (l.1348) et `c-cancel` (l.1629) appellent `fermerFeuilles()` directement — perte silencieuse — pendant que `e-cancel` (l.1803) passe par `fermerFeuilleVariete()` qui consulte `formulaireEspeceSale` (l.1809-1813). Le même geste (« Annuler ») signifie « fermer sans confirmation » sur spot/cueillette et « fermer avec confirmation » sur variété. L'utilisateur apprend que le voile est sûr sur une feuille et destructeur sur l'autre — puis que le bouton le plus proche du voile ne suit pas la même règle. *Fix :* brancher `s-cancel`/`c-cancel` sur `fermerFeuilleAvecGardeFou` (ou documenter explicitement Annuler = renoncement assumé, auquel cas `e-cancel` doit suivre la même règle).*

**P3-1 (COPY/VALENCE) — le toast de coercition tire avant le croisement guide.** `toast('⚠️ Statut IA hors vocabulaire — confirmez la comestibilité')` (l.2452) précède `infoEspeceArchive` (l.2456). Si le guide surclasse en MORTEL (ex. IA sort un statut hors vocabulaire sur une phalloïde masquée), la carte affiche « ☠️ MORTEL — ne jamais consommer » + antipoison pendant que le toast, 2,2 s, dit « confirmez la comestibilité ». Contradiction au pire moment. *Fix :* déplacer le toast après le croisement et ne le tirer que si `!connue.id`, ou reformuler sans mentionner la comestibilité (« statut IA hors vocabulaire — le guide a été consulté »).*

**P3-2 (RÉGRESSION DE BORD DU FIX P2-2) — ⚠️ sur une carte rouge MORTEL si l'espèce est masquée depuis sa propre fiche.** `ouvrirDetail` affiche « 🙈 Masquer » sur la fiche de l'espèce elle-même (l.1471) ; `recharger()` ne re-rend pas la vue détail (l.2753-2758) : la fiche de l'espèce masquée reste ouverte. `basculerSpec` cherche alors l'espèce via `toutesEspeces()` (l.1515) — qui la filtre — et `esp` devient `undefined` → `glypheAtt = '⚠️'` sur une carte `verdict-danger-att` à fond rouge pour une espèce MORTELLE. Avant le fix, le glyphe était codé ☠️ et restait juste dans ce cas de bord. *Fix :* mémoriser le statut (`nonComestible`) dans `Etat` à l'ouverture de la fiche et dériver le glyphe de cette valeur, pas d'une recherche dépendante de la visibilité.*

**P3-3 (MOITIÉ NON TRAITÉE DE 25E P2-2) — le corps du verdict-att reste figé.** `basculerSpec` ne met à jour que le titre `.t` (l.1517-1518) ; le corps affiche toujours la variante nb=0 (« Cochez chaque critère sur le champignon avant de consommer… », l.1463) à 1/5. Non contradictoire (le conseil reste juste), mais la carte mélange un titre dynamique et un corps figé. Confirmé « cosmétique, laissé » par l'Assessment B (B-2). *Fix :* re-rendre la zone verdict complète à chaque `basculerSpec`, ou mettre à jour le corps avec le titre.*

## 8. Red flags par persona

- **Jonathan en forêt, une main, sans réseau** : le moment de vérité (photo ID) est protégé **même après rangement** — phalloïde masquée, IA « comestible 95 % » → MORTEL + antipoison (l.2456-2460, vérifié par traçage statique ; runtime confirmé par l'Assessment B 25e). **Pire moment :** photographier une **variété perso** MORTELLE qu'il a masquée — le filet se tait (P2-1) ; ou refermer la feuille cueillette d'un tap au voile après avoir choisi le spot et la météo — perdus sans un mot (P2-2).
- **Proche débutant (via export/import)** : la règle simple « ☠️ = ne jamais manger » est restaurée — plus de crâne sur la chanterelle (l.1516), plus de carte « ✅ + confiance insuffisante » (l.2468). **Pire moment :** lire le toast « confirmez la comestibilité » pendant que la carte sous ses yeux dit MORTEL (P3-1) — deux instructions contraires au moment où il apprend à faire confiance aux signaux.
- **Utilisateur au clavier / lecteur d'écran** : l'annonce du verdict-att est désormais cohérente en audio (⚠️ sur comestible, ☠️ sur dangereux — l.1518), et l'ordre Escape-modal est sûr (pas de double confirmation, l.1113-1127). **Pire moment :** cocher un critère sur une fiche d'espèce MORTELLE masquée en cours de consultation et entendre « ⚠️ Critères manquants » sur une carte annoncée danger (P3-2) ; la lightbox reste sans piège à focus (Tab sort derrière le dialogue).

## 9. Observations mineures

**Nouveaux :**
- Deux fonctions d'archive coexistent : `infoEspeceArchive` (photo, l.1010) et le patron P1-2 du flux cueillette (l.1533) — la question 25E « une seule fonction de croisement ? » reste ouverte.
- Commentaire l.2448 « P1-5 » : numérotation d'une ancienne passe (référent actuel : 23E-P2-1) — le prochain développeur ne retrouvera pas le finding (déjà signalé 25E).
- `feuilleSaisieSale` teste l'existence des feuilles via `document.getElementById` au lieu du helper `$` — style seulement.

**Résidus inchangés (non re-scorés, re-confirmés présents en 26E) :** `rendreBandeauCle` insère un `<button>` dans un `<p class="note">` (l.2416-2419, HTML invalide) · `p-cle` sans label (l.460) · toast de pré-remplissage sans mention du statut transféré (l.2531) · `retirerIllu` ne re-rend pas la vue détail sous-jacente (l.2329-2346) · PRODUCT.md l.39 (`especesCustom`/`cachees`) vs code (`especes`/`caches`, l.792-793) · champ recherche du guide sans label visible (l.411) · échec silencieux de `chargerBaseMyco` (l.1642) · focus perdu sur les selects de filtre (re-rendu `rendreFiltres`, l.1373-1379) · `alt="photo"` générique (l.1205) · `ouvrirMyco` sans message hors-ligne (l.2377-2379) · `.mois-col .lab` 10,5 px (l.339) · cache SW non borné pour les GET réussis (sw.js l.162) · `aria-invalid` : 0 partout (re-grep confirmé), validation toast-only · `COULEURS_MOIS` cycle 6×2 sans sémantique de saison (l.2543) · lightbox sans piège à focus (l.2380-2400).

## 10. Questions provocatrices

1. La suggestion 25E disait « ESPECES + Etat.especesCustom » : la moitié manquante (variétés perso) est-elle un choix délibéré ou un oubli — et qui décide qu'une variété perso MORTELLE masquée mérite moins de filet qu'une espèce du guide ?
2. Le filet archive est exact-match là où le chemin visible est flou (synonymes, Levenshtein) : l'exactitude est-elle le prix de la sûreté sur les espèces invisibles, ou faut-il indexer les noms complets du guide une fois pour toutes et matcher « ange destructeur » masqué ?
3. Les puces d'espèces du spot et les selects spot/météo sont-ils des champs « perdables » par conception, ou le garde-fou a-t-il simplement copié la liste des inputs texte ?
4. « Annuler » signifie-t-il « fermer sans confirmation » ou « fermer avec confirmation » ? Trois feuilles, deux réponses : quelle sémantique prime — et la réponse doit-elle aussi s'appliquer à e-cancel ?
5. Le toast de coercition tire avant le croisement guide : faut-il le retarder, le conditionner, ou l'inscrire dans la carte corrigée (méta « statut IA corrigé par le guide ») — et comment le tester sans réordonner les branches ?
6. Masquer une espèce depuis sa propre fiche laisse la fiche ouverte (recharger ne re-rend pas le détail) : la fiche d'une espèce masquée doit-elle se fermer, ou rester consultable — et dans ce dernier cas, avec quel glyphe de verdict ?
7. Le glyphe du verdict doit-il dériver d'une recherche dépendante de la visibilité (`toutesEspeces()`), ou d'un état capturé à l'ouverture de la fiche — quelle est la source de vérité du statut affiché ?
8. Le corps du verdict-att reste figé à 1/5 pendant que le titre bouge : la carte est-elle un état composite (titre + corps synchrones) ou faut-il re-rendre la zone verdict entière à chaque coche ?

---

**Claims `2751ec4` vérifiés** (`git show --stat` : index.html +41/−15, sw.js ±1 — conforme) :
- **P2-1 ✅ tenu, avec réserves.** `infoEspeceArchive` l.1009-1017 (fallback `ESPECES` + flag `archivee`), branché l.2456 ; surclassement GRAV indépendant de l'archivage (l.2457-2460) ; bouton fiche masqué si `archivee` (l.2499-2501). Phalloïde masquée → MORTEL quand même (traçage statique ; runtime confirmé par l'Assessment B 25e). **Réserves :** variétés perso (P2-1), synonymes/frappe sur masquées (P2-1), absence d'adoption côté cueillette (§9).
- **P2-2 ✅ tenu, avec réserves.** `glypheAtt` selon statut l.1515-1518 ; prédicat identique au rendu initial `nonComestible` (l.1449). Chanterelle → ⚠️, phalloïde → ☠️. **Réserves :** corps figé (P3-3), bord espèce masquée depuis sa fiche (P3-2).
- **P2-3 ✅ tenu, avec réserves.** Normalisation `toLowerCase()` l.2450-2451 ; `aVerifier = bande 60-89 || (!statutValide && !connue.id)` l.2467-2468. Le transfert variété profite de la normalisation (vocab l.2522 = options du select l.643-647, minuscules des deux côtés). **Réserve :** toast tiré avant le croisement (P3-1).
- **P3-1 ✅ tenu, avec réserves.** `feuilleSaisieSale` + `fermerFeuilleAvecGardeFou` l.1056-1071 ; voile l.1072, poignées l.1073, Escape l.1126-1127 ; ordre modal-premier préservé (l.1113-1119) — pas de régression 17E. **Réserves :** puces/selects hors du test (P2-2), Annuler contourne (P2-3).
- **SW bump ✅ tenu.** `CACHE = 'cqm-v53'` (sw.js l.4) ; FICHIERS complet (21 especes + 105 specs + 2 credits + mycoquebec.json). Arbre git propre, HEAD = docs uniquement, 21 `"guide":true` re-vérifiés dans `img/mycoquebec.json`, 0 CSS dans le diff.

**Non corrigés (nouveaux de cette passe) :** P2-1, P2-2, P2-3, P3-1, P3-2, P3-3 ci-dessus, et les résidus de la section 9.
