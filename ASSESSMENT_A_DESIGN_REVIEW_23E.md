# Assessment A — Critique design (23e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2731 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v50) · **Base :** `img/mycoquebec.json` (3938 entrées, 3396 avec `nomFr`, 0 doublon de latin)
**Méthode :** lecture statique seule (Assessment A, aucun navigateur, aucun détecteur). Vérification des 8 findings de la passe 22E (P3-1 à P3-7 + patron tabs) dans le code ET sur les données : diff complet de `5e4afc9` relu, base JSON interrogée en Python par identité (latin), comparateur de suggestions (l.1618-1639) répliqué avec `normNom` sur 13 requêtes dangereuses, existence des fichiers sur disque, greps ARIA/opacity (batterie Python io.open — aucune ligne citée ne vient de search_files).
**Note globale :** les 8 findings de 22E sont **corrigés en code** — 8/8, vérifiés ligne par ligne. Le comparateur répliqué tient : 13/13 requêtes (accents ou non, espaces ou tirets) servent la bonne espèce du guide en position 1. Nouveau passif : 1 P2 (pré-remplissage qui perd les signaux de sécurité) + 5 P3 (a11y, copy, doc). Score **39/40 — baisse honnête de 0,5** : les 8 correctifs sont confirmés, mais le P2-1 est une dette de sécurité non détectée avant, qui docke H5 (4 → 3,5).

---

## 1. Verdict de spécificité design : 9/10 (inchangé)

La grammaire Memphis tient sur les nouveaux éléments : la pastille de suggestion (🍄 sur rayures ambre 45°, l.1645) reprend exactement le langage des vignettes du système (DESIGN.md l.180) — un repli qui REMPLACE une image cassée par un élément du vocabulaire, pas par un placeholder générique. 0 couleur hors palette (grep : tous les hex du CSS sont dans le frontmatter DESIGN.md), 0 ombre floutée, 0 uppercase, 0 boîte système (`window.confirm` n'apparaît qu'en commentaire, l.235).

**Axes :** conceptuel ~90 % (carnet de chasse, vocabulaire mycologique québécois, antipoison, « Identité » / « Détails & photo ») · visuel ~90 % (une capture sans texte révèle Memphis-automne-champignon). Verdict : spécifique sur les deux axes.

## 2. Évaluation holistique

- **Hiérarchie visuelle** — tenue. h1 unique (header), h2 par vue en pastille inclinée, détail : `<h2>` nom d'espèce (l.1453) + sections h3. La barre d'étapes annonce l'étendue du formulaire.
- **Architecture de l'information** — le découpage 2 étapes reste sain ; Enregistrer n'existe que sur l'étape 2 (l.692). Les suggestions pleine largeur (l.639, hors `grille2`) ont gagné l'espace qu'elles méritent — plus de puces compressées à ~150 px.
- **Adéquation émotionnelle** — la vallée 22E (miniatures cassées hors-ligne dans les suggestions) est refermée : plus aucune requête ne peut afficher une image cassée, le repli rayures est chaleureux et hors-ligne par nature. Nouvelle petite vallée, inversée : sur une identification « À vérifier », « Ajouter comme variété » ouvre un formulaire qui dit silencieusement « ✅ Comestible » (P2-1) — un faux réconfort au pire moment du doute.
- **Découvrabilité** — rien au hover ; l'encart d'aide IA est visible dès l'étape 1 ; le bandeau clé (l.2383-2386) guide vers Paramètres.
- **Composition** — colonne 640 px, feuille 84 vh, grilles 2 colonnes conservées. P3-2 22E corrigé : `#e-nom-suggestions` est pleine largeur entre les deux grilles (l.639).
- **Typographie** — Fredoka 400-700 chargée exactement (grep 900/300 : 0) ; `.etape` 13 px/700. Drift doc : DESIGN.md annonce Meta « 600, 12.5 px, opacité 0.75 », le code exécute 400 + opacité .85 (l.140) — le .85 est la correction de contraste AA qui n'a jamais été reportée dans la doc (P3-5).
- **Couleur** — 0 dérive de palette. Contrastes stables depuis 22E : Identifier actif `#B3540B` sur blanc ≈ **4,64:1** (AA à 11,5 px, le plus faible des 5 onglets) ; toxique blanc sur `#B45309` ≈ **4,65:1** ; comestible noir sur `#6F8F3E` ≈ **4,62:1** ; MORTEL blanc sur rouge ≈ **6,5:1** ; textes opacité .85 sur blanc = **4,91:1** composé (AA à 12-13 px). La Règle du Rouge Mortel tient (numéros de pilules = compteur, documenté).
- **Accessibilité** — patron tabs désormais complet : `aria-controls` (l.624, 626), tabindex roving synchronisé (l.1731-1732), flèches ←/→ (l.1736-1742) ; l'activation par flèche déplace le focus dans le panneau (variante « activation automatique » de l'APG — conforme). Focus à l'ouverture opérationnel : `ouvrirFeuille` AVANT `etapeEspece(1)` (l.1752-1753, 1767-1768) + rAF (l.1734). Trois trous nouveaux : checklist sans `aria-pressed` (P3-1), nav sans `aria-current` (P3-2), ARIA des barres en kg pendant que l'œil lit des lb (P3-3). `aria-invalid` : 0 (résidu, validation toast-only).
- **États** — boutons désactivés pendant les appels IA (l.1883-1884, 2317), restauration sur tous les chemins, états vides partout — et désormais COHÉRENTS entre les deux autocomplétions (P3-4 22E : message explicite l.1648). Échec IA → `messageErreurIA` par cause ; « aucune image trouvée » mappe vers un message orienté solution (l.1670).
- **Copy** — toasts à valence alignée (vérifié branche par branche, inchangé). Nouveau point de fragilité : « 3 938 espèces » en dur dans l'état vide (l.1648) — vrai aujourd'hui (base = 3938, vérifié), mais c'est le pattern « 5/5 en dur » retiré en 15E qui revient (P3-4).
- **Cas limites** — dates locales (`aujourdhui()`), `toISOString` uniquement pour la métadonnée d'export (l.2547, usage correct), import versionné (l.2562-2575), orphelins `caches` nettoyés, checklist réindexée au retrait d'item (l.2296-2312), séquence de rechargement gardée (`seqRecharger`).

## 3. Évaluation de charge cognitive : 1 échec / 8 (inchangé)

1. Focus unique ✅ · 2. Chunking ≤ 4 ✅ · 3. Regroupement visuel ✅ · 4. Hiérarchie ✅ · 5. Une chose à la fois ✅ · 6. Choix minimaux ≤ 4 ❌ — **étape 1 = 5 champs** (nom, latin, comestibilité, saison, prudence) + 2 boutons + 1 encart ; étape 2 = 4 champs + zone photo + 8 boutons. Inchangé depuis 21E : le point reste en échec, exactement comme jugé. · 7. Mémoire de travail ✅ · 8. Divulgation progressive ✅.

**1 échec franc sur 8.** Le claim « lève l'échec ≤ 4 » (`326f57c`) reste partiel après trois passes.

## 4. Voyage émotionnel

Ouverture chaleureuse (dégradé, formes flottantes, zigzag) → guide → fiche hybride inchangés. **La vallée 22E est fermée :** en forêt, hors-ligne, chercher « lactaire » n'affiche plus 6 images cassées mais 6 pastilles rayures 🍄 + noms lisibles — l'aide visuelle est intacte là où elle existe (guide) et honnête là où elle n'existe pas (le reste de la base). **Pic de création de variété** inchangé (recette en 2 temps, bascule auto après IA). **Nouvelle vallée de confiance, au pire moment :** l'utilisateur photographie un champignon, l'app répond « ⚠️ À vérifier » ou « Comestible — prudence », il touche « Ajouter comme variété »… et le formulaire s'ouvre sur « ✅ Comestible », case prudence décochée, sans un mot sur ce que l'IA avait dit. Le toast dit « vérifiez l'identité » — mais l'app vient de réécrire l'identité vers la valeur la plus permissive (P2-1). Fin de journée : rappel d'export (« Jamais exporté », l.2537-2544) — pic de réassurance honnête, pas de faux pic.

## 5. Scores heuristiques Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 4 | Bascule auto étape 2 après IA, toasts guidés, boutons désactivés, focus d'ouverture enfin opérationnel (rAF l.1734) |
| 2 | Correspondance monde réel | 4 | Réplication : 13/13 requêtes dangereuses (accents ou non, espaces/tirets) → bon taxon du guide en position 1 |
| 3 | Contrôle et liberté | 4 | Retour entre étapes, garde-fou (voile/poignée/Escape, l.1042-1049, 1088-1103), annulable partout |
| 4 | Cohérence et standards | 4 | États vides unifiés (P3-4 22E ✓), grammaire tenue sur la pastille rayures ; drifts doc en P3 |
| 5 | Prévention des erreurs | 3,5 | Le fail-safe statut→inconnu existe (l.2418-2419) mais ne se propage pas au pré-remplissage : défaut permissif silencieux (P2-1) |
| 6 | Reconnaissance vs mémorisation | 4 | Noms enseignés requêtables dans toutes leurs formes de saisie ; normNom appliqué requête + données |
| 7 | Flexibilité / efficacité | 4 | ✨ IA remplit les 2 étapes, retry + repli modèle, ordre des images persistant, FAB contextuel |
| 8 | Esthétique minimaliste | 3,5 | Étape 1 dépasse toujours la barre ≤4 ; étape 2 garde ~13 éléments d'attention (inchangé) |
| 9 | Aide à la récupération d'erreurs | 4 | messageErreurIA par cause, parserJSONIA tolérant, séries interrompues avec état restauré, import versionné |
| 10 | Aide et documentation | 4 | Encart onboarding, carte « Comment identifier », DESIGN.md documente les étapes — mais drift filtres/meta (P3-5) |

**Total : 39/40 — baisse honnête de 0,5.** Les 8 correctifs 22E sont vérifiés ; le seul dock est H5 (3,5), pour la dette de sécurité non détectée avant (P2-1). Profil : sécurité, état du système et prévention excellents ; frottements restants : densité du formulaire variété (structurel) et le trou de transfert des signaux de sécurité.

## 6. Forces spécifiques

1. **La fermeture de la vallée hors-ligne est faite dans la grammaire du système.** P3-1 22E demandait « pas d'image cassée » ; la réponse (l.1643-1645) ne masque pas l'image mais la remplace par une pastille rayures ambre 🍄 — le langage exact des vignettes sans photo (DESIGN.md l.180). Aucune requête ne peut plus afficher une image cassée hors-ligne, et la hiérarchie visuelle reste intacte : seules les 21 espèces du guide (vignettes locales) montrent une photo.
2. **La discipline des données tient toujours, par identité.** 21/21 entrées `guide:true` = exactement les 21 latins du guide (0 faux positif/négatif), 21/21 img locales présentes sur disque ET dans `FICHIERS` du SW (cqm-v50), 0 doublon de latin. Réplication du comparateur réel : « amanite phalloide » (sans accent), « ange destructeur », « fausse morille », « pied de mouton » ET « pied-de-mouton », « tue mouches » → la bonne espèce (mortelle comprise) en position 1, 13/13.
3. **Le patron tabs est passé au complet en une passe, sans casser le reste.** `aria-controls` + tabindex roving + flèches ←/→ (l.623-627, 1731-1742) cohabitent avec la validation du nom (le fléchage vers l'étape 2 sans nom ne passe pas, l.1720-1723) et avec le focus au premier champ par rAF. C'est la variante « activation automatique » de l'APG, appliquée proprement.

## 7. Problèmes prioritaires

**P2-1 (NOUVEAU, SÉCURITÉ) — le pré-remplissage depuis l'identification photo perd les signaux de sécurité.** `preparerVarieteDepuisResultat` (l.2471-2485) transfère nom, latin, statut, description, caractéristiques, confusions et photo — mais PAS `r.prudence` : la case « ⚠️ Prudence » reste décochée (reset l.1749), donc une morille identifiée « prudence requise » devient une variété sans avertissement de cuisson. Pire : quand le statut IA est hors vocabulaire, le fail-safe le force à `'inconnu'` (l.2418-2419) — or le select `e-statut` n'a pas d'option « inconnu » (l.642-647), `ouvrirSheetEspece` l'a remis à `'comestible'` (l.1749) et le transfert n'écrase que si la valeur est dans le vocabulaire (l.2478) : l'espèce « à vérifier » s'ouvre silencieusement sur « ✅ Comestible ». C'est l'inverse exact du principe produit n° 1 (toute ambiguïté penche vers la prudence), au moment où l'utilisateur a le plus de doutes. *Fix :* transférer `$('e-prudence').checked = !!r.prudence` ; ajouter `<option value="inconnu">⚠️ Inconnu</option>` au select et présélectionner `'inconnu'` quand le statut est invalide (ou forcer un choix manuel avec un toast « statut à confirmer »).*

**P3-1 (NOUVEAU, A11Y) — la checklist terrain n'expose pas son état coché.** `.spec-carte` est `role="button" tabindex="0"` (l.1430) mais `aria-pressed` n'existe nulle part (grep : 0 occurrence). L'état coché (fond olive + barré) est purement visuel : un lecteur d'écran ne peut pas savoir quels critères sont vérifiés sur l'écran le plus important pour la sécurité, et le compteur « n/5 » change sans région live. *Fix :* `aria-pressed="true/false"` mis à jour dans `basculerSpec` (l.1474-1488) + `aria-live="polite"` sur `#spec-compteur`.*

**P3-2 (NOUVEAU, A11Y) — les onglets de navigation n'exposent pas l'onglet actif.** `nav.tabs button.actif` (l.86-96) est signalé uniquement par couleur et translation, sans `aria-current` (grep : 0). Ironie de la passe : la barre d'étapes vient de recevoir sa sémantique complète, la navigation principale n'en a aucune. *Fix :* `b.setAttribute('aria-current', ...)` dans `naviguer` (l.1015).*

**P3-3 (NOUVEAU, A11Y/unités) — les ARIA des barres de stats parlent kg pendant que l'œil lit des lb.** `aria-valuenow`/`aria-valuemax` (l.2501) et le `aria-label` des tiges mensuelles (« J : 2.5 kg », l.2532) utilisent les kg bruts des données, alors que l'affichage visible passe par `fmtKg` (conversion lb). En mode lb, l'utilisateur voyant lit « 4,8 lb » et le lecteur d'écran annonce « 2,2 » — deux vérités contradictoires pour la même barre. *Fix :* formater les valeurs ARIA avec la même unité que l'affichage (passer par `fmtKg` ou retirer l'unité des labels).*

**P3-4 (NOUVEAU, COPY/DONNÉES) — « 3 938 espèces » en dur dans l'état vide.** l.1648. Le compte colle aujourd'hui (base = 3938 entrées, vérifié en Python), mais c'est un compte statique dans une copie dynamique — le pattern exact du « 5/5 vérifiés » en dur retiré en 15E. La base grossira. *Fix :* interpoler `base.length` dans le message (`'…dans les ' + base.length + ' espèces…'`).*

**P3-5 (NOUVEAU, DOC) — DESIGN.md décrit des composants qui n'existent plus, et un typo qui n'est pas exécuté.** (a) DESIGN.md l.193 : « Filtres du guide : puces blanches cerclées ; l'active se colore… » — les filtres sont deux `<select>` depuis `4929c4d` (index.html l.1347-1355) ; le drift a survécu ~8 passes. (b) Typography : « Meta (600, 12.5 px…, opacité 0.75) » vs code `.item .meta` 400 + opacity .85 (l.140) — le .85 est la correction de contraste AA (4,91:1) jamais reportée dans la doc ; le 0.75 documenté échouerait à ~3,5:1. (c) PRODUCT.md l.38 : « ~140 Ko » vs 169 Ko réels (173 045 octets). *Fix :* mettre à jour les trois — la doc doit décrire le système réel, pas le système rêvé.*

## 8. Red flags par persona

- **Jonathan en forêt, une main, sans réseau** : le pire moment 22E est refermé — chercher un lactaire hors-ligne montre des pastilles rayures lisibles, pas des images cassées ; les 21 espèces du guide restent en vignette locale, position 1. Restant : l'étape 2 dense (13 éléments) en fin de journée. Le P2-1 ne le touche pas en forêt (c'est un flux maison), mais il le touche au retour, quand il transforme sa récolte incertaine en fiche.
- **Proche débutant (via export/import)** : la chaîne nom → taxon → fiche tient 21/21 dans toutes les formes de saisie ; l'encart d'aide guide la génération IA ; l'enregistrement passe par l'étape 2. Nouveau red flag : s'il photographie un champignon et que l'app dit « À vérifier », « Ajouter comme variété » lui présente un statut « Comestible » pré-rempli — un débutant peut le prendre pour un verdict.
- **Utilisateur au clavier / lecteur d'écran** : la feuille variété s'ouvre désormais avec le focus dans le premier champ (les deux flux, l.1752-1753, 1767-1768) et le patron tabs est complet. Mais la checklist — le cœur de la fiche — n'a ni `aria-pressed` ni compteur live (P3-1), la nav n'a pas d'`aria-current` (P3-2), et les barres de stats annoncent des kg en mode lb (P3-3). Pire moment : cocher un critère sur une fiche mortelle et ne recevoir aucun retour.

## 9. Observations mineures

**Nouveaux :**
- Les deux zones de suggestions (Myco l.1612-1650, cueillettes l.1516-1530) ne sont annoncées par aucune région live et n'ont pas de sémantique combobox/listbox (`aria-autocomplete`, `aria-expanded`) — l'autocomplétion existe pour les yeux seulement (l'`aria-live` du fichier est uniquement le toast, l.744).
- Le pré-remplissage variété n'est pas le seul à ignorer `prudence` : le chemin `e-generer` le transfère (l.1890), le chemin idphoto non — l'incohérence entre les deux flux IA du même formulaire est en soi un mini-drift (fixé par P2-1).
- `COULEURS_MOIS` (l.2496) reste un cycle de 6 couleurs répété 2×/an (résidu 16E) ; les couleurs ne portent aucune saison — janvier (rouille) ≠ juin (rouille). La même couleur pour deux mois sans signification partagée est une encodation décorative dans un graphique qui en annonce une informative.
- Les barres `role="progressbar"` (l.2501) n'ont pas de `aria-valuemin` — implicite 0, acceptable.

**Résidus inchangés (non re-scorés, listés pour mémoire, tous re-confirmés présents en 23E) :** `rendreBandeauCle` insère un `<button>` dans un `<p class="note">` (l.2385, HTML invalide) · `p-cle` sans label (l.460) · `connue` compare sans `normNom` (l.2425 — une réponse IA sans accent rate le bouton « Voir la fiche ») · `choisirNomMyco` ne remplit le latin que si vide (l.1656) · échec silencieux de `chargerBaseMyco` (l.1609) · champ recherche du guide sans label visible (l.411) · focus perdu sur les selects de filtre (re-rendu `rendreFiltres`) · `alt="photo"` générique (l.1181) · « Dernière sortie » 24 px en carte 2 colonnes · `ouvrirMyco` sans message hors-ligne (l.2344-2346) · `.mois-col .lab` 10,5 px (l.339) · cache SW non borné pour les GET réussis (l.162) · `aria-invalid` : 0 partout, validation toast-only · navigation ↑/↓ des suggestions (16E).

## 10. Questions provocatrices

1. Le fail-safe « statut inconnu » s'arrête à la carte de résultat : l'option « ⚠️ Inconnu » doit-elle exister dans le formulaire variété, ou le statut doit-il être un choix forcé (pas de défaut silencieux, jamais « Comestible » pré-coché) ?
2. `r.prudence` est affiché sur la carte de résultat puis jeté au transfert : quels champs le pré-remplissage a-t-il le droit d'abandonner, et un toast « vérifiez l'identité » est-il une excuse suffisante pour réécrire un signal de sécurité vers sa valeur la plus permissive ?
3. « 3 938 espèces » en dur dans l'état vide : le compte vivra-t-il dans le message (base.length) ou hors du texte — et qui se souviendra de le mettre à jour quand la base passera à 4 000 ?
4. La checklist est le seul composant à bascule sans état exposé : `aria-pressed` arrive-t-il avant ou après qu'un utilisateur de lecteur d'écran doive décider de manger un champignon vérifié 0/5 ?
5. La barre d'étapes a reçu sa sémantique complète cette passe ; les 5 onglets de navigation n'ont toujours pas d'`aria-current` — la priorité ARIA est-elle « nouveaux composants d'abord » ou « surface la plus utilisée d'abord » ?
6. Les ARIA des barres annoncent des kg pendant que l'œil lit des lb : l'accessibilité doit-elle parler la même unité que l'affichage, ou les données brutes suffisent-elles ?
7. DESIGN.md décrit des puces de filtre disparues depuis 8 passes : le design system documente-t-il le système réel, ou seulement ses intentions au moment de l'écriture — et une passe de doc est-elle due après chaque refonte de composant ?
8. La doc Meta dit 600/0.75, le code exécute 400/.85 (la correction AA) : les futures corrections de contraste auront-elles le droit de diverger du doc, ou le doc doit-il être mis à jour dans le même commit que le CSS ?

---

**Correctifs de la passe 22E vérifiés (8/8) :**
- **P3-1 ✅ corrigé.** l.1643-1645 : image rendue seulement si `x.img.startsWith('img/')`, sinon pastille rayures ambre 45° + 🍄 (26 px, bordure noire 2 px) — aucune requête ne peut plus casser hors-ligne. Vérifié sur données : 0 des 21 `guide:true` a une img distante.
- **P3-2 ✅ corrigé.** `#e-nom-suggestions` déplacé hors du `grille2` (l.639), pleine largeur entre les deux grilles.
- **P3-3 ✅ corrigé.** PRODUCT.md l.38 : « le numéro courant vit dans `sw.js`, jamais dans cette doc » — le pattern « actuellement vN » est supprimé (grep : 0). SW = cqm-v50, cohérent.
- **P3-4 ✅ corrigé.** l.1648 : « Aucune correspondance dans les 3 938 espèces — vous pouvez saisir un nom libre. » — l'état vide Myco est explicite et aligné sur celui des cueillettes (l.1529). Compte vérifié : la base fait bien 3938 entrées.
- **P3-5 ✅ corrigé.** `ouvrirFeuille` avant `etapeEspece(1)` dans `ouvrirSheetEspece` (l.1752-1753) ET `editerEspece` (l.1767-1768) ; le focus passe par `requestAnimationFrame` (l.1734) — plus de focus no-op sur `visibility:hidden`.
- **P3-6 ✅ corrigé.** `role="progressbar"` + `aria-valuenow` + `aria-valuemax` + `aria-label` (l.2501) ; tiges mensuelles `role="img"` + `aria-label` avec la valeur (l.2532) ; planchers `Math.max(4,/Math.max(6,` supprimés (grep : 0), remplacés par `Math.min(100, Math.max(2, pct))` pour les valeurs > 0 (le zéro garde un moignon neutre `#D8C9AC` documenté).
- **P3-7 ✅ corrigé.** Le repli IA redondant est retiré (l.1992 : seul `throw` honnête) ; la boucle sur l'ordre choisi reste la seule source d'appels, et l'erreur mappe vers « essayez un autre ordre ou une autre espèce » (l.1670).
- **Patron tabs ✅ complété.** `aria-controls="etape-1/2"` (l.624, 626), tabindex roving 0/-1 synchronisé (l.1731-1732), flèches ←/→ avec `preventDefault` (l.1736-1742) ; activation automatique avec focus déplacé dans le panneau (variante APG conforme) ; la validation du nom garde la porte (l.1720-1723).

**Claims `5e4afc9` vérifiés** (`git show --stat` : PRODUCT.md ±1, index.html +25/−18, sw.js bump — conforme) : les 8 items du message existent dans le code et dans les données, avec une seule réserve notée (P3-3 : les valeurs ARIA restent en kg bruts).

**Non corrigés (nouveaux de cette passe) :** P2-1 et P3-1 à P3-5 ci-dessus, et les résidus de la section 9.
