# Assessment A — Critique design (7e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2345 lignes, HTML+CSS+JS mono-fichier)
**Docs de référence :** `PRODUCT.md`, `DESIGN.md` (North Star « La Récolte », palette AUTOMNE/TERRE)
**Méthode :** lecture statique du source (Assessment A), vérification des fixes des passes 4-6 (commits d00b6d8 → d707531), calculs de contrastes WCAG explicites.
**Date :** 11 août 2026

---

## 1. Verdict de spécificité design

**Axe conceptuel : ~90 %.** Le vocabulaire est celui du carnet de chasse mycologique québécois : « coin secret », « Règle d'or : en cas de doute, on ne mange pas », « centre antipoison 1-800-463-5060 », « spécificités à repérer », verdicts ⚠️/✅, « Cueillettes », « Mes spots ». Les 21 espèces avec leurs confusions dangereuses (gyromitre vs morille, lépiote brunâtre vs élevée) sont du domaine pur. Une capture d'écran sans texte révélerait immédiatement le domaine : champignons, panier, forêt.

**Axe visuel : ~85 %.** Ce n'est PAS un template de dashboard : bordures noires 3 px, coins cassés 18/5 px, ombres dures sans flou, zigzag d'en-tête, pois crème, titres inclinés -1/-2°, vignettes à rayures ambre/blanc, FAB rose, pastilles de statut inclinées. Le langage Memphis est tenu de bout en bout, y compris dans les micro-états (appui translate 3 px + ombre réduite, rebond élastique des feuilles, sortie ease-out). Seule réserve : les cartes stats (4 pastilles colorées avec gros chiffres) et les barres de rang restent proches d'une grammaire de dashboard générique — mais la bordure noire et les coins cassés les rattrapent.

**Verdict :** interface spécifique à ce produit sur les deux axes. Le test « screenshot sans texte » passe.

---

## 2. Évaluation holistique

### Hiérarchie visuelle
- Échelle typographique cohérente et documentée : display 21 px (h1, incliné -1,5°, text-shadow rose) → titre-vue 20 px en pastille blanche → titre de feuille 18 px en pastille ambre → corps 16 px → label 13 px → meta 12,5 px. `text-wrap:balance` et `tabular-nums` appliqués (index.html:45-47, 263, 294).
- **Dérive :** les `h3` des cartes Stats (« 🏆 Top espèces », « 🗺️ Top spots », « 📅 Récolte par mois », « 💾 Sauvegarde ») ne portent AUCUN style Memphis — taille navigateur par défaut, texte noir nu (index.html:400-404), alors que les titres de section du guide ont droit à la pastille cuir `.guide-sujet` (index.html:318-319). Deux grammaires de titres de section cohabitent.
- Les 4 cartes stats sont volontairement colorées différemment (jaune/cuir/olive/terracotta) — encodage redondant assumé, mais le libellé de la carte olive casse le contraste (voir Couleur).
- `.deco-tri` (triangle noir opacity .12) est si discret qu'il est quasi invisible — décoration fantôme.

### Architecture de l'information
- 5 onglets complets et cohérents avec DESIGN.md ; FAB contextuel (📍 en Spots, ＋ ailleurs, masqué en Stats/détail/Paramètres) — index.html:926-927.
- **Trou de navigation :** la vue détail (`vue-detail`) n'a ni titre-vue, ni bouton retour dans le header sticky, et **aucun onglet actif** (naviguer('detail') ne matche aucun `data-vue`, index.html:924). Le seul retour est le bouton « ← Retour » en bas de la fiche (index.html:1297-1299), après ~3000 px de scroll pour une fiche à 5 spécificités avec photos. Parcours cœur (identifier → fiche → comparer avec une autre espèce) pénalisé.
- Terminologie stable : « Masquer / Supprimer définitivement / Restaurer », « Cueillettes », « Variété perso » — pas de résidus de renommage constatés.

### Adéquation émotionnelle
- North Star « La Récolte » respecté : header chaleureux (dégradé brun→ambre, formes SVG flottantes, zigzag), états vides avec guidance émotionnelle (« Appuyez sur le bouton rose pour ajouter votre premier coin secret ! », index.html:1083), toasts noirs bordés d'ambre.
- **Valence correcte :** le rouge est strictement réservé au danger/destruction/compteur documenté ; le mode hors-ligne n'est jamais montré en rouge (c'est la normalité du produit). Aucune fausse alerte « tout va bien » : l'alerte « Jamais exporté » est honnête et pilotée par une vraie donnée (index.html:2165-2173).
- **Fausse promesse :** « Tout effacer » toaste « Toutes les données ont été effacées » (index.html:2220) alors que le store `checklist` n'est PAS vidé (voir P1-1) — les coches terrain des 21 espèces survivent à la destruction totale.

### Découvrabilité
- Bandeau clé Gemini persistant avec bouton « Configurer la clé → » qui navigue et focusse le champ (index.html:2020-2023) — excellent.
- « ✨ Générer les manquantes » (index.html:656) découvrable dans la feuille Illustrations.
- **Faible :** l'état actif des filtres de saison n'est marqué que par une rotation de -2° (voir P2-4) ; la lightbox n'a aucun indice de fermeture autre que le curseur zoom-out.

### Composition
- Colonne unique max 640 px, rythme 4/8/12/16/24 px, cartes espacées 16 px — conforme. Grille 2 colonnes pour paires de boutons et cartes stats.
- Feuilles bottom-sheet max 84 vh avec poignée étendue (hit area ::after -14 px, index.html:281) — bonne cible tactile.
- La feuille variété est très longue (10 champs + 4 boutons photo + 2 actions) : scroll important dans un sheet de 84 vh.

### Typographie
- Fredoka 400-700 uniquement, pas d'uppercase forcé, pas de graisse < 400 — conforme DESIGN.md.
- `font-variant-numeric:tabular-nums` sur compteurs dynamiques (n/5, stats, pastille header) — détail de qualité (passe 5 confirmée).
- Sous-titre header « 🍄 Carnet de champignons · édition Memphis » : noir à 90 % sur le brun du dégradé #C87224 = **4,22:1 en 12,5 px** — échec AA marginal (voir Couleur).

### Couleur
- Palette tenue : les 8 couleurs AUTOMNE/TERRE + les extensions documentées (rouge #B3261E, gris, bleu canard, vert-mesure, rose-onglet, brun-tabac, brun-header, fonds d'alertes, barre-vide). Aucune dérive hors palette constatée.
- **Contrastes calculés (luminance relative explicite) :**
  - ✅ noir/olive 4,61:1 (btn-vert, verdict-ok, st-comestible) — passe AA.
  - ✅ noir/ambre 7,59:1 ; blanc/rouge 6,07:1 ; blanc/orange 4,67:1 ; blanc/cuir 5,45:1 ; blanc/terracotta 4,95:1 ; noir/gris 6,08:1 ; noir sur fonds d'alertes 13,3:1 ; toast crème/noir 14,08:1.
  - ❌ **Libellé « Espèces » (carte stats 3, fond olive) : noir à 80 % sur olive = 3,56:1 en 12 px bold — échec AA** (index.html:295 + 293). Les passes 4-6 ont corrigé cuir/terracotta (blanc pur, opacity 1) mais ont oublié la carte olive.
  - ❌ **Sous-titre header : 4,22:1** sur la zone #C87224 du dégradé (12,5 px, 600) — échec AA marginal.
  - ⚠️ Coche ✓ blanche sur olive (`.spec-carre.fait`) : 3,44:1 — glyphe de 16 px bold, sous AA mais acceptable comme symbole graphique (P3).
- **Règle du Rouge Mortel respectée** : le rouge n'apparaît que MORTEL, suppression, pastille compteur (documentée DESIGN.md:143).

### Accessibilité
- role=button + tabindex sur puces, items guide, spec-cartes ; clavier Enter/Espace global (index.html:951-956) ; aria-live sur toast ; prefers-reduced-motion (index.html:336-338) — passes 4-5 confirmées.
- **Focus ambre incomplet :** le focus `box-shadow:0 0 0 3px var(--jaune)` n'est appliqué qu'aux champs de saisie (index.html:180). Boutons, puces, items, FAB et onglets retombent sur l'outline navigateur par défaut — incohérent avec DESIGN.md (focus ambre) et peu visible sur fond crème (P2-1).
- Lightbox sans role=dialog, sans gestion Escape, sans gestion du focus (index.html:2006-2013).
- Input `g-recherche` sans aria-label (placeholder seul, index.html:385).
- Imbrication interactive invalide : `.item` role=button contient un vrai `<button class="btn-suppr-item">` (index.html:1246-1253).
- `boite-confirm` : role=alertdialog ✓, focus initial sur « Annuler » (choix non destructif) ✓, mais pas de focus trap ni Escape.

### États
- Chargement : « Analyse en cours… » avec sous-texte explicatif (index.html:2033) ; « Génération en cours… » sur le bouton IA (index.html:1577) ; toasts de progression « Génération i/n » (index.html:1989).
- Erreur : messageErreurIA en français avec guidance réseau/clé/quota (index.html:1445-1455) — **sauf le catch d'identification photo qui affiche `err.message` brut** (index.html:2095), ex. « Failed to fetch » (P2-3).
- Vide : états vides guidés partout (spots, cueillettes, guide, stats, crédits).
- **Bug d'état :** « Tout effacer » ne vide pas la checklist (P1-1).

### Copy
- Français du Québec soigné, ton carnet de chasse tenu partout. « En cas de doute : on ne mange pas » répété aux bons endroits (guide, verdicts, identification photo).
- Une seule action, plusieurs libellés cohérents (« Masquer », « Supprimer définitivement », « Restaurer ») — pas de doublons trompeurs.
- Le toast « Spot copié 📋 — collez-le où vous voulez » promet une action réelle (presse-papiers) — pas de fausse promesse de fichier.

### Cas limites
- `aujourdhui()` construit la date en heure locale (index.html:687-690) — pas de bug UTC.
- `saisonsDe` (index.html:1223-1226) : chanterelle « Juillet à octobre » → été+automne ✓, pleurote « Septembre à décembre (et hiver en redoux) » → automne+hiver ✓, morille/gyromitre → printemps ✓. Refactor confirmé.
- Suppression d'un spot : les cueillettes liées sont conservées et affichées « Sans spot » (message explicite, index.html:1166) — comportement documenté, pas de crash dans les stats (agrégation sous « Sans spot », index.html:2148).
- Espèce supprimée/masquée : badge de sécurité conservé sur les cueillettes via especeId archivé (index.html:1343-1346) — fix confirmé.
- Réindexation des coches au retrait d'une spécificité : `splice` symétrique sur `faits` (index.html:1963-1971) — fix confirmé.
- **Trou :** `st-effacer` omet `checklist` (P1-1).

---

## 3. Évaluation de charge cognitive (8 items)

| # | Item | Verdict | Preuve |
|---|------|---------|--------|
| 1 | Focus unique (un job par écran) | ✅ | Chaque vue a un job principal ; le guide est un hub (photo/recherche/filtres) mais reste lisible. |
| 2 | Chunking ≤ 4 | ❌ | 10 puces de filtre visibles en 2 rangées (5 statuts + 5 saisons, index.html:1210-1218) ; 5 spécificités par fiche (limite haute). |
| 3 | Regroupement visuel | ✅ | Rangées de puces séparées, cartes groupées, grille2, sections guide-sujet. |
| 4 | Hiérarchie | ❌ | Échelle documentée respectée, MAIS les h3 des cartes stats sortent de l'échelle (taille navigateur par défaut). |
| 5 | Une chose à la fois | ✅ | Une feuille = un formulaire ; verdicts et compteur n/5 allègent la fiche. |
| 6 | Choix minimaux ≤ 4 | ❌ | Feuille variété : 10 champs + 4 boutons photo ; sélecteur d'espèces du spot : 21 puces affichées d'un coup (index.html:1142-1144). |
| 7 | Mémoire de travail | ✅ | Coches persistantes, compteur n/5, badge header, verdicts — rien à retenir d'un écran à l'autre. |
| 8 | Divulgation progressive | ❌ | Fiche détail déverse tout d'un bloc (description, caractéristiques, confusions, 5 photos, verdicts, 4 boutons) — pas de sections repliables. |

**Échecs : 4/8.** La charge est maîtrisée sur les parcours de lecture (guide, stats) et lourde sur les parcours de saisie (feuille variété, sélecteur d'espèces du spot) et la fiche détail.

---

## 4. Voyage émotionnel (peak-end rule)

- **Entrée :** header chaleureux (dégradé, formes flottantes, zigzag), pop élastique des vues (cubic-bezier(.2,1.6,.4,1)) — pic d'entrée réussi.
- **Milieu :** zéro boîte système navigateur (confirm Memphis stylée, DESIGN.md respecté) ; toasts avec guidance ; garde-fou « Quitter sans enregistrer ? » sur la feuille variété (index.html:1502-1505) — bonne réassurance. Vallée principale : la feuille variété longue à remplir/scroller une main en forêt.
- **Pic de fin :** « Cueillette enregistrée ✅ » + badge qui s'incrémente + stats colorées — pic authentique. **Aucun faux pic** (« tout est terminé » n'existe nulle part ; l'alerte export est honnête).
- **Réassurance à haut risque :** double confirmation pour destruction, alerte MORTEL avec antipoison systématique, verdict ⚠️ par défaut (« Rien n'est encore vérifié ») — exemplaire.
- **Fausse note :** « Toutes les données ont été effacées » alors que la checklist survit (P1-1) — le seul mensonge émotionnel du parcours.

---

## 5. Les 10 heuristiques de Nielsen

| # | Heuristique | Score | Problème clé |
|---|-------------|-------|--------------|
| 1 | Visibilité de l'état du système | 3,5/4 | Toasts, compteurs, verdicts, bandeau clé excellents ; pénalisé par les puces saison actives quasi invisibles (rotation seule). |
| 2 | Correspondance système-monde réel | 4/4 | Vocabulaire mycologique québécois exact, emojis météo, « coin secret », saisons réelles. |
| 3 | Contrôle et liberté | 4/4 | Annuler partout, garde-fou variété, restauration sélective, double confirmation, fermeture voile/poignée. |
| 4 | Cohérence et standards | 3/4 | Design system tenu, mais focus clavier non-ambre sur boutons, h3 stats non stylés, erreurs IA brutes dans un chemin. |
| 5 | Prévention des erreurs | 4/4 | Verdict ⚠️ par défaut, double confirmation destruction, garde-fou saisie, réindexation des coches, validation nom/date/espèce. |
| 6 | Reconnaissance plutôt que mémorisation | 3,5/4 | Autocomplétion espèce, puces visibles ; pénalisé par 21 puces espèces du spot et filtres saison sans état coloré. |
| 7 | Flexibilité et efficacité | 3/4 | FAB contextuel, GPS 1 clic, « Générer les manquantes » ; pas de raccourcis, retour de fiche détail pénible, pas de recherche spots/cueillettes. |
| 8 | Esthétique minimaliste | 3,5/4 | Memphis riche mais dense : fiche détail et feuille variété chargées ; pas de bruit parasite hors design. |
| 9 | Aide à la reconnaissance des erreurs | 3,5/4 | messageErreurIA français avec guidance ; le catch photo affiche le message brut de l'API. |
| 10 | Aide et documentation | 3/4 | Placeholders explicites, notes, bandeau clé, crédits photos ; pas d'onboarding ni d'aide intégrée à la checklist. |

**Total : 35/40** (progression vs 34/40 à la 6e passe — les fixes tiennent, mais de nouveaux trous de cohérence sont apparus : checklist non vidée, focus boutons, olive oublié, erreurs photo brutes, puces saison).
**Profil :** très fort sur la prévention des erreurs et le contrôle (sécurité + réassurance), plus faible sur la cohérence des détails (focus, titres, erreurs) et l'efficacité de navigation en fiche détail.

---

## 6. Forces spécifiques (2-3)

1. **Le système de verdicts ⚠️/✅ de la checklist terrain** (index.html:1281-1292, 1318-1332) : verdict ⚠️ visible dès 0 critère avec « Rien n'est encore vérifié », bascule en ✅ seulement quand les 5 critères sont cochés, persistance IndexedDB, réindexation des coches au retrait d'une spécificité, inclusion dans l'export/import v5. C'est un mécanisme de sécurité réel, pas un gadget — et il est exécuté sans faille.
2. **La tenue du design system Memphis dans les micro-états** : appui translate 3 px + ombre réduite (boutons, items, FAB), rebond élastique des feuilles (cubic-bezier(.2,1.3,.4,1)) avec sortie ease-out sans rebond, coin cassé systématique (18/5 px, 12/4 px, 24/18 px), vignettes à rayures ambre/blanc, zigzag d'onglet actif. Un langage visuel rarement tenu avec cette discipline dans une PWA mono-fichier.
3. **Le copy de réassurance terrain** : « En cas de doute : on ne mange pas » répété aux trois moments de vérité (guide, verdict, identification photo), alerte MORTEL avec centre antipoison 1-800-463-5060 systématique, « Jamais exporté : vos données vivent uniquement sur ce téléphone », double confirmation avec « Exportez d'abord si nécessaire ». Le produit parle comme un carnet de chasse, pas comme un logiciel.

---

## 7. Problèmes prioritaires (3-5)

### P1-1 — « Tout effacer » ne vide pas la checklist terrain
- **Sévérité : P1** (promesse de destruction non tenue, données résiduelles).
- **Preuve :** index.html:2218-2219 (`vider('spots'); vider('cueillettes'); vider('especes'); vider('illustrations'); vider('caches'); vider('supprimees')`) — `checklist` absent, alors que l'import vide bien les 7 stores (index.html:2200) et que le toast annonce « Toutes les données ont été effacées » (index.html:2220).
- **Pourquoi c'est grave :** l'utilisateur qui efface tout pour repartir à zéro (ou avant de revendre/prêter le téléphone) retrouvera ses anciennes coches et verdicts sur les 21 fiches — données personnelles résiduelles + verdicts périmés qui peuvent induire en erreur.
- **Correctif concret :** ajouter `await Stockage.vider('checklist');` à la ligne 2219.

### P1-2 — Retour depuis la fiche détail : aucun onglet actif, retour en bas de page
- **Sévérité : P1** (blocage récurrent du parcours cœur en contexte terrain).
- **Preuve :** `naviguer('detail')` ne marque aucun onglet actif (index.html:924) ; le header sticky n'offre aucun retour ; le seul « ← Retour » est dans la grille de boutons en bas de la fiche (index.html:1297-1299), après ~3000 px de scroll pour une fiche à 5 spécificités avec photos.
- **Pourquoi c'est grave :** le parcours d'identification réel est « fiche A → retour → fiche B » (comparer une amanite douteuse avec la phalloïde). En forêt, une main, gants, ce retour coûte un scroll entier à chaque comparaison.
- **Correctif concret :** ajouter un bouton « ← » sticky dans le header quand `Etat.vue === 'detail'` (ou rendre l'onglet Identifier actif et le retour par l'onglet), et/ou un bouton retour flottant en haut de la fiche.

### P2-1 — Focus clavier non-Memphis sur boutons, puces, items, FAB, onglets
- **Sévérité : P2** (cohérence design system + accessibilité).
- **Preuve :** le focus ambre `box-shadow:0 0 0 3px var(--jaune)` n'est défini que sur `.champ input/select/textarea` et `.saisie` (index.html:180). Tous les autres éléments interactifs (`.btn`, `.puce`, `.item`, `.fab`, `nav.tabs button`) retombent sur l'outline navigateur par défaut — invisible sur fond crème, hors design system.
- **Correctif concret :** `button:focus-visible, .puce:focus-visible, .item:focus-visible, .fab:focus-visible { outline:3px solid var(--noir); outline-offset:2px; box-shadow:0 0 0 3px var(--jaune); }` (ou l'équivalent ambre documenté).

### P2-2 — Contraste : libellé « Espèces » sur olive (3,56:1) et sous-titre header (4,22:1)
- **Sévérité : P2** (échec AA sur texte 12-12,5 px).
- **Preuve :** `.stat-carte .libelle{opacity:.8}` (index.html:295) sur `.stat-carte:nth-child(3){background:var(--vert)}` (index.html:293) → noir 80 % sur #6F8F3E = **3,56:1** (calcul de luminance explicite). La passe 6 a corrigé cuir/terracotta (blanc pur, opacity 1) mais pas olive. Sous-titre header : noir 90 % sur #C87224 = **4,22:1** en 12,5 px (index.html:49).
- **Correctif concret :** passer le libellé de la carte olive en blanc pur (opacity 1) comme les cartes 2 et 4 ; pour le sous-titre, passer l'opacité à 1 (noir pur sur #C87224 = 4,79:1, toujours sous AA strict — envisager #241A0F à 100 % + graisse 700, ou assombrir le coin du dégradé).

### P2-3 — Erreurs IA brutes dans l'identification photo
- **Sévérité : P2** (incohérence avec le fix de la passe 6).
- **Preuve :** le catch d'`analyserPhoto` affiche `esc(err.message)` brut (index.html:2095) — « Failed to fetch », « API 429 »… — alors que tous les autres chemins IA passent par `messageErreurIA` (index.html:1445-1455).
- **Correctif concret :** remplacer par `messageErreurIA(err)` dans le catch (index.html:2093-2096).

### P2-4 — Filtres de saison actifs sans indicateur de couleur
- **Sévérité : P2** (feedback d'état faible).
- **Preuve :** les règles `.puce.actif[data-f=…]` (index.html:166-171) ne couvrent que les statuts ; les puces saison (`data-fs`) actives ne reçoivent que `transform:rotate(-2deg)` (index.html:165) — aucun changement de fond ni de bordure.
- **Pourquoi c'est grave :** en plein soleil (usage forêt), une rotation de 2° ne se lit pas ; l'utilisateur ne sait pas quel filtre saison est appliqué.
- **Correctif concret :** ajouter `.puce.actif[data-fs]{background:var(--noir);color:var(--creme);}` (ou un fond ambre) pour les puces saison actives.

---

## 8. Red flags par persona

### Jonathan en forêt (mobile, une main, gants, sans réseau)
- **Ce qui marche :** tout est hors-ligne, cibles ≥ 44 px, FAB contextuel, GPS 1 clic, verdicts lisibles sans réseau.
- **Red flags :** retour de fiche détail en bas de page (P1-2) ; puces saison sans état coloré en plein soleil (P2-4) ; feuille variété longue à scroller une main.
- **Pire moment :** champignon douteux en main → fiche de l'amanite rougissante → vouloir comparer avec la panthère → 3000 px de scroll pour retrouver « ← Retour ».

### Utilisateur à accessibilité réduite (clavier, lecteur d'écran)
- **Ce qui marche :** role=button + tabindex partout, Enter/Espace global, aria-live toast, reduced-motion, focus initial sur « Annuler » dans les confirmations.
- **Red flags :** focus clavier non-ambre sur boutons/puces/items (P2-1) ; lightbox sans role=dialog ni Escape ; imbrication role=button contenant un vrai `<button>` (index.html:1246-1253) ; input recherche sans aria-label.
- **Pire moment :** tabuler dans la checklist terrain — le focus sur les spec-cartes est invisible sur fond blanc.

### Utilisateur pressé / distrait (notification, appel, prêt du téléphone)
- **Ce qui marche :** double confirmation avant destruction, toasts clairs, « Jamais exporté ».
- **Red flags :** « Tout effacer » qui laisse la checklist (P1-1) — fausse croyance de repartir à zéro ; coches fantômes qui réapparaissent sur les fiches.
- **Pire moment :** effacer tout avant de prêter le téléphone, puis découvrir d'anciens verdicts « ✅ confirmé » sur une fiche mortelle.

---

## 9. Observations mineures

- Coche ✓ blanche sur olive (`.spec-carre.fait`) à 3,44:1 — glyphe, P3.
- Lightbox : pas de gestion Escape, pas de role=dialog, pas de gestion du focus (index.html:2006-2013).
- `g-recherche` sans aria-label (placeholder seul, index.html:385).
- Imbrication interactive invalide : `.item` role=button + `<button>` enfant (index.html:1246-1253).
- Styles inline massifs (margin-top, display) dans le HTML — dette de code, pas un défaut de design.
- `h3` des cartes stats non stylés (taille navigateur par défaut) — deux grammaires de titres de section.
- `.deco-tri` à opacity .12 — quasi invisible, décoration fantôme.
- Le verdict ✅ vert apparaît aussi sur les fiches mortelles (« restez prudent ») — sémantique discutable (voir questions).
- `spec-zoom` « 🔍 Agrandir » : bonne affordance, mais le badge est un `<span>` non cliquable (le clic passe par l'image) — le libellé promet un clic que le span ne porte pas.
- `restaurer-ok` désactivé à 0 sélection ✓ ; `accent-color:var(--orange)` sur les checkboxes ✓.
- `loading="lazy"` sur les vignettes du guide ✓ ; `rel="noopener"` sur les liens externes ✓.
- `compresser` (900 px, JPEG 0.72) : bon équilibre taille/qualité pour les photos embarquées.
- `aujourdhui()` en heure locale ✓ — pas de bug de date UTC.
- `seqRecharger` guard + nettoyage des orphelins de `caches` ✓ (index.html:2299-2313).
- SW bump cqm-v28 cohérent avec le refactor d707531 ✓.

---

## 10. Questions provocatrices

1. « Tout effacer » promet tout effacer — pourquoi la checklist survit-elle à la destruction totale alors que l'import, lui, vide bien les 7 stores ?
2. Le retour de fiche est en bas de page après 5 photos et ~3000 px — le header sticky ne devrait-il pas porter un « ← » dès qu'on est en détail ?
3. Une puce saison active n'est marquée que par une rotation de 2° — en plein soleil, comment Jonathan sait-il quel filtre est appliqué ?
4. Le focus ambre documenté dans DESIGN.md ne s'applique qu'aux champs de saisie — pourquoi boutons, puces et items échappent-ils au design system ?
5. L'identification photo affiche les erreurs brutes de l'API alors que tout le reste de l'app les traduit en français avec guidance — pourquoi ce chemin échappe-t-il à `messageErreurIA` ?
6. La passe 6 a corrigé les libellés stats sur cuir et terracotta — pourquoi la carte olive (3,56:1) a-t-elle été oubliée ?
7. Le verdict ✅ vert s'affiche aussi sur les fiches mortelles (« restez prudent ») — un ✅ vert sur une fiche MORTEL ne risque-t-il pas d'être lu comme « bon à manger » par un œil pressé ? Ne faudrait-il pas un verdict neutre/rouge pour les espèces non comestibles ?
8. La feuille variété cumule 10 champs + 4 boutons photo — faut-il la découper (étapes ou sections repliables) ou assumer la densité pour un usage rare ?
9. Le sélecteur d'espèces d'un spot affiche 21 puces d'un coup — un champ de recherche ou un tri par saison allégerait-il la sélection en forêt ?
10. Le badge rouge du header compte les cueillettes — le rouge est réservé au danger dans DESIGN.md ; la pastille est documentée, mais un utilisateur ne le sait pas. Faut-il la passer en ambre pour préserver la Règle du Rouge Mortel ?
11. Les h3 des cartes stats ne portent aucun style Memphis — pourquoi les titres de section du guide ont-ils droit à la pastille cuir et pas eux ?
12. La lightbox n'a ni Escape ni role=dialog — pour un zoom photo en forêt, un appui n'importe où ferme, mais au clavier, comment sort-on ?

---

## Vérification des fixes des passes 4-6 (exigence de relecture)

| Fix annoncé | Verdict |
|---|---|
| P0-1 verdict ⚠️ visible à 0 critère | ✅ Confirmé (index.html:1291, `ouv` si nbFaits < length) |
| P1-1 variables CSS --ambre/--olive/--cuir | ✅ Confirmé (index.html:20-24) |
| P1-2 a11y clavier (role=button, Enter/Espace, aria-live, reduced-motion) | ✅ Confirmé (index.html:951-956, 680, 336-338) |
| P2-1 contrastes (verdict ✅ noir/olive, meta .85) | ✅ Confirmé (4,61:1 et 10,16:1) — **résiduel : libellé stats olive 3,56:1** |
| P2-2 autocomplétion espèce (input + suggestions, valeur libre) | ✅ Confirmé (index.html:1360-1379) |
| P1-1 checklist dans l'export/import v5 | ✅ Confirmé (index.html:2175, 2200, 2207) |
| P1-2 réindexation des coches au retrait d'une spécificité | ✅ Confirmé (index.html:1963-1971) |
| P2-1 contrastes libellés stats AA | ⚠️ Partiel — cuir/terracotta ✓ (blanc pur), **olive oublié (3,56:1)** |
| P2-2 filtres sécurité complets | ✅ Confirmé (index.html:1231-1234) |
| P2-3 erreurs IA en français avec guidance | ⚠️ Partiel — toasts ✓, **catch identification photo brut (index.html:2095)** |
| Refactor helpers (appelGemini, lierPhoto, topRangs, fermerFeuilleVariete, saisonsDe, recharger Promise.all) | ✅ Tous confirmés (index.html:1457, 1050, 2125, 1502, 1223, 2302) |
| saisonsDe : chanterelle automne, pleurote hiver | ✅ Confirmé (index.html:1222-1226) |

---

*Rapport produit par lecture statique uniquement (Assessment A) — aucun fichier du projet modifié, aucun outil de détection ni navigateur utilisé.*
