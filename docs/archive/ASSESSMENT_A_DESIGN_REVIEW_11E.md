# Assessment A — Critique design (11e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2459 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v32)
**Méthode :** lecture statique seule (Assessment A), vérification des correctifs des passes 4-10 dans le code, contrastes recalculés par script WCAG exact.
**Date :** 12 août 2026

---

## 1. Verdict de spécificité design

**Conceptuelle : ~90 %.** Le vocabulaire est entièrement du domaine — « spots », « cueillettes », « Règle d'or », « spécificités à repérer », « centre antipoison 1-800-463-5060 », « fausse morille », « volve en sac », « anneau coulissant » (l.821, 835, 875, 1328). La métaphore du carnet de chasse est tenue partout : pastille-compteur de récoltes dans le header (l.373), FAB « panier » rose, zigzag d'en-tête, pois au fond (l.32-33). Aucune interface générique ne parlerait de « vérifiez la sporée rose » (l.861).

**Visuelle : ~85 %.** Le test « une capture sans texte révèle-t-elle le domaine ? » : oui — vignettes à rayures ambre/blanc (l.138), photos de champignons 16:9, badges MORTEL rouges cerclés de noir, palette automne/terre. Le style Memphis est appliqué avec une discipline rare : bordures noires 3 px sur toute surface colorée (Règle du Trait Noir), coins cassés 18/5 px systématiques (l.119, 123, 255), ombres dures sans flou (aucun `box-shadow` à 3 valeurs trouvé), inclinaisons -1/-2° (l.46, 114, 173), zéro boîte système navigateur (aucun `window.confirm/alert`), zéro uppercase forcé. Les formes SVG flottantes du header (l.355-358) et le zigzag (l.376-377) complètent le tableau.

**Verdict :** interface fortement spécifique, les deux axes tenus — un des rares cas où le style n'est pas un habillage mais le produit lui-même (le plaisir de la récolte est un principe produit, PRODUCT.md l.64).

---

## 2. Évaluation holistique

### Hiérarchie visuelle
- Échelle typographique disciplinée : display 21 px/700 (h1, l.45), titre-vue 20 px/700 en pastille blanche cerclée (l.110-115), titre de feuille 18 px/700 en pastille ambre (l.293-295), corps 16 px, label 13 px/700, meta 12.5 px. La hiérarchie passe par le poids et la taille, comme documenté.
- **Dérive :** `font-weight:900` sur `.spec-num` (l.259) et `.spec-carre` (l.262) alors que la police Fredoka n'est chargée qu'en 400-700 (l.17) — le navigateur synthétise ou arrondit, rendu variable selon plateforme. Violation directe de DESIGN.md (« graisse inférieure à 400 » interdite ; le 900 n'est pas documenté non plus).
- **Dérive :** `.rang:nth-child(4n+2/3/4)` (l.315-317) — la couleur des pastilles de rang dépend de la position dans la liste, pas de la valeur. Un top-3 spots (l.2256) colorera ses rangs 1-2-3 en jaune/bleu/vert alors que le top-5 espèces (l.2251) colorera 1-2-3-4-5 en jaune/bleu/vert/rose/jaune. Même composant, deux grammaires de couleur : la couleur n'est pas un signal fiable.
- Les 4 cartes stats volontairement inégales (jaune/bleu/vert/rose, l.298-304) : choix Memphis assumé et documenté, pas une erreur d'égalité de poids.

### Architecture de l'information
- 5 onglets complets et cohérents (l.463-469), FAB contextuel (📍 en Spots, ＋ ailleurs, masqué en Stats/détail/Paramètres, l.964), bouton ← sticky en détail (l.56-63, 374). Navigation complète : rien d'atteignable n'est innavigable.
- **Terminologie :** « Identifier » (onglet) vs « Guide » (dans le code et les toasts « Espèce masquée du guide ») — l'onglet s'appelle Identifier mais le contenu parle de « guide » partout (l.391, 1317, 1362). Deux termes pour un même objet, résidu de renommage.
- **Dérive sémantique :** le bouton 🗑️ sur les items du guide (l.1314) ouvre « Masquer ou supprimer » — l'icône corbeille promet la destruction, le geste par défaut est le masquage réversible. La 4e passe avait corrigé « Masquer en gris (rouge = destruction seule) » pour les variétés perso, mais le bouton du guide est resté une corbeille noire sur blanc.

### Adéquation émotionnelle
- Le concept « La Récolte » est exécuté avec une cohérence rare : rebonds élastiques (cubic-bezier(.2,1.3,.4,1), l.281), appui « bouton qu'on enfonce » (translate + ombre réduite, l.154), poignée de feuille avec hit-area étendu (l.292), tabular-nums sur les compteurs (l.54, 305).
- **Valence parfaite sur le danger :** rouge réservé au mortel/destruction (Règle du Rouge Mortel respectée), verdicts ☠️ dynamiques « n/n critères vérifiés — MORTELLE : ne pas consommer » (l.1354), ✅ vert réservé comestibles/prudence (l.1353). La collision de valence historique est corrigée.
- **Valence à surveiller :** le mode hors-ligne n'est jamais montré en rouge (bien) ; mais l'alerte « Jamais exporté » (l.2277-2279) en orange est un rappel anxiogène permanent sur l'onglet Stats — nécessaire, mais c'est le seul endroit où l'app « gronde » l'utilisateur.
- États vides chaleureux et orientés action : « Appuyez sur le bouton rose pour ajouter votre premier coin secret ! » (l.1144), « Aucun champignon trouvé » (l.1301).

### Découvrabilité
- **Point faible historique non résolu :** l'identification par photo (fonctionnalité phare, PRODUCT.md l.33) est annoncée par deux boutons verts en haut du guide (l.393-394) — mais si la clé Gemini manque, l'utilisateur ne voit qu'un bandeau orange « Configurer la clé → » (l.2118-2121). Le bandeau est bien placé et le bouton focus la clé (l.2120) : correctif efficace.
- La checklist terrain (cœur de la fiche hybride) est découverte par l'ouverture d'une fiche — pas d'onboarding, mais le pré-remplissage automatique des 5 spécificités (l.1336-1339) rend la découverte naturelle.
- Le bouton « ↩️ Restaurer des espèces » n'apparaît que s'il y a des espèces masquées (l.1316-1318) : bonne divulgation progressive.

### Composition
- Colonne unique max 640 px (l.106), grille 2 colonnes pour paires de boutons (l.192), cartes espacées 16 px. Les feuilles bottom-sheet max 84 vh (l.282) avec poignée. La grille2 casse proprement sur mobile (1fr 1fr reste lisible à 320 px).
- **Détail :** la feuille variété (sheet-espece) est très longue (nom, latin, statut, saison, prudence, habitat, description, caractéristiques, confusions, IA, photo, 2 alertes) — un scroll de ~2 écrans dans la feuille, mais le formulaire est groupé logiquement.

### Typographie
- Fredoka 400-700 uniquement (l.17), pas d'uppercase forcé, pas de césure. `text-wrap:balance` sur titres (l.47, 114). Meta à opacité .85 (l.144) — conforme à la doc (0.75) mais plus lisible.
- **Dérives contrastes (calculs exacts, script WCAG) :**
  - `.ligne-latin` opacité .65 (l.332) : **2.56:1** sur blanc, 13 px italique — échec AA (4.5:1). C'est le nom latin, présent sur chaque item du guide et chaque fiche.
  - `.info-gps` opacité .75 (l.202) : **3.36:1**, 12.5 px — échec AA. C'est le retour GPS (« Position obtenue ± 5 m ») et les messages d'erreur GPS.
  - `.mois-col .lab` opacité .7 (l.325) : **2.86:1**, 10.5 px — échec AA. Les étiquettes J F M A M J J A S O N D du graphique mensuel.
  - `.stat-carte .libelle` carte 1 (jaune) opacité .8 (l.306) : **3.27:1**, 12 px — échec AA (les cartes 2-4 ont été corrigées à opacité 1, l.307, mais la carte 1 est restée à .8).
  - `.vide-etat` opacité .8 (l.335) : **3.99:1**, 15 px — sous 4.5:1 (échec AA texte normal ; passe seulement en « large text » 3:1).
  - `.spec-carre` coche ✓ blanc sur olive : **3.44:1** (glyphe 16 px décoratif, acceptable).
  - Passent : noir/olive 4.61:1 ✅, noir/ambre 7.59:1 ✅, blanc/rouge 6.07:1 ✅, blanc/orange 4.67:1 ✅, noir/creme 14.08:1 ✅, noir/C87224 4.79:1 ✅, blanc/terracotta 4.95:1 ✅, blanc/cuir 5.45:1 ✅.

### Couleur
- Palette AUTOMNE/TERRE respectée à 100 % : les seules couleurs hors palette sont documentées dans DESIGN.md (onglets actifs l.89-93, dégradé header l.38, fonds d'alertes l.220/226, barre vide l.2267, COULEURS_MOIS l.2231). Aucune dérive non documentée trouvée.
- **Règle du Rouge Mortel tenue :** le rouge n'apparaît que pour MORTEL, suppression, compteur. Vérifié : « Masquer » est gris (l.1362), le bouton 🗑️ du guide est noir/blanc (l.1314) — mais voir la dérive sémantique ci-dessus.

### Accessibilité
- Correctifs 5e-10e passes **confirmés dans le code** : clavier Enter/Espace sur role=button (l.990-995), focus-visible ambre (l.190), aria-live toast (l.692), prefers-reduced-motion (l.347-349), lightbox role=dialog + aria-label + Escape + restauration du focus (l.2082-2101), focus trap + Escape sur modales (l.1027-1042), cibles ≥44 px (btn-petit l.162, puces l.166, btn-suppr-item l.130), span « 🔍 Agrandir » avec role=button + stopPropagation (l.1348).
- **Trous restants :**
  - L'image de la fiche détail promet le zoom (`cursor:zoom-in`, l.1366) mais n'a ni role ni tabindex — inaccessible au clavier (le span Agrandir des spécificités, lui, est correct).
  - Les `title="Cliquez pour retirer la photo"` des photo-zones (l.521, 569, 626) sont faux quand la zone est vide : le clic ouvre alors la galerie, pas un retrait.
  - Les suggestions d'autocomplétion (l.1443) sont des `<button>` — bien ; mais la liste n'a pas de rôle listbox/aria-expanded sur l'input.
  - Le focus initial des modales va sur « Annuler » (l.1011) — choix défensif correct pour les confirmations destructrices.

### États
- Chargement : pas d'écran de chargement initial (IndexedDB local, quasi instantané) — acceptable.
- Erreurs IA : `messageErreurIA` français avec guidance par cause (clé/réseau/quota/500/404, l.1520-1529), catch identification photo inclus (l.2198-2204) — correctif 7e passe confirmé.
- Analyse photo annulable (AbortController + ✋ Annuler, l.2106-2113) et récupérable (réouverture + toast, l.2141, 2197) — correctif 10e passe confirmé.
- Import versionné (alerte si < 5 ou > 5, l.2305-2310) — correctif 10e passe confirmé.
- « Réessayer » répète la dernière source (l.2170, `derniereSourcePhoto` l.2107) — correctif 10e passe confirmé.
- **Aucun faux « all clear »** : pas de « Tout terminé 🎉 », pas de compteurs en dur. Les stats sont calculées (l.2240-2268).

### Copy
- Français du Québec authentique (« boisé du rang 4 », « coin secret », « en forêt »). Toasts chaleureux (« Spot enregistré ✅ », « Espèce masquée 🙈 »).
- **Résidus de renommage :** « guide » vs « Identifier » (voir AI). Le bouton « 🗑️ Masquer » (l.1362) mélange l'icône de destruction et le verbe réversible.
- Le toast « Analyse terminée ✨ » (l.2141, 2197) avec un ✨ pour une identification potentiellement mortelle : la célébration est mal placée quand le résultat est « À vérifier » — mais le verdict rouge suit immédiatement dans la feuille, donc l'ambiguïté est brève.

### Cas limites
- Dates : `aujourdhui()` local (l.699-701), `fmtDate` local (l.703-707) — pas de piège UTC. Le graphique mensuel parse le mois localement (l.2261) — cohérent.
- Poids : virgule acceptée (l.715), conversion kg/lb cohérente (l.711, 717), labels d'unité mis à jour partout (l.2344-2347, 2449-2452).
- Checklist : réindexation des coches au retrait d'une spécificité (l.2042-2047) — correctif 6e passe confirmé. Export v5 inclut checklist (l.2282), « Tout effacer » vide la checklist (l.2333) — correctifs confirmés.
- Matche flou Levenshtein ≤2 (l.936-941) + inclusion des synonymes (l.944-952) + alerte ☠️ à la saisie d'un synonyme mortel (l.1492-1494) — correctifs 9e/10e passes confirmés.
- **Cas limite non couvert :** le matche par inclusion (l.946-949) ne vérifie pas que le terme saisi est un *vrai* synonyme — « morille » saisi dans une cueillette matchera « Morille » (exact) mais aussi, si l'exact échoue, n'importe quel nom contenant le terme. Le garde-fou `estSynonyme` (l.952) ne s'applique qu'à l'inclusion, pas au flou : une faute de frappe sur « chanterelle » (distance 1) donnera le badge comestible sans alerte — c'est le comportement voulu (le badge survit aux fautes), mais un nom libre comme « chanterelle du Québec » (inclusion) déclenchera l'alerte synonyme alors que c'est peut-être une variété locale. Comportement défensif, acceptable.

---

## 3. Évaluation de charge cognitive

1. **Focus unique** ✅ — chaque vue sert une tâche (Spots = gérer les coins, Identifier = identifier, Cueillettes = journaliser, Stats = lire, Paramètres = configurer). Le FAB contextuel renforce le focus.
2. **Chunking ≤ 4** ❌ — la fiche détail empile : alerte + galerie (5 spécificités) + verdicts + saison/habitat + description + caractéristiques (4-5 puces) + confusions + 2-4 boutons = ~8 blocs d'information distincts. Le chunking par carte est bon, mais le nombre de blocs dépasse 4. Le guide affiche 21 items (liste, acceptable — c'est une liste, pas un formulaire).
3. **Regroupement visuel** ✅ — cartes cerclées de noir, sections avec pastilles de sujet (l.329-330), verdicts sous l'alerte (l.1370-1371), espacement 16 px. La galerie + verdicts juste sous l'alerte (correctif 9e passe) regroupe la décision au bon endroit.
4. **Hiérarchie** ✅ — 4 niveaux de titre distincts (21/20/18/16 px), poids 400-700, inclinaison comme marqueur de titre. Cohérent partout.
5. **Une chose à la fois** ✅ — feuilles bottom-sheet pour les formulaires, modales pour les confirmations, lightbox pour le zoom. Rien ne se chevauche.
6. **Choix minimaux ≤ 4** ❌ — la feuille cueillette a 7 champs (date, poids, espèce, spot, météo, notes, photo) ; la feuille variété en a 11 + 2 alertes. Les formulaires sont longs mais groupés logiquement ; le pré-remplissage IA (l.1655-1664) réduit l'effort réel.
7. **Mémoire de travail** ❌ — l'utilisateur doit retenir : le statut de l'espèce (badge), le nombre de critères cochés (compteur n/5), le verdict (⚠️/✅/☠️), la saison, les confusions. Le compteur et les verdicts sont persistants et visibles, ce qui aide ; mais la fiche exige de retenir les critères non cochés pendant qu'on manipule le champignon. C'est inhérent à la tâche, bien atténué par l'UI.
8. **Divulgation progressive** ✅ — le guide montre nom + badge + saison + habitat ; la fiche révèle le reste. Les filtres (5 statuts × 5 saisons) sont des puces, pas des menus. La restauration n'apparaît que si nécessaire.

**Échecs : 3/8** (chunking fiche, choix formulaires, mémoire de travail) — score correct pour une app de terrain, les échecs sont structurels à la tâche, pas des défauts d'UI.

---

## 4. Voyage émotionnel (peak-end rule)

- **Entrée :** animation `pop` des vues (l.108-109) avec rebond élastique — accueil chaleureux immédiat. Le header dégradé ambre + zigzag + formes flottantes donne le ton « carnet de chasse » dès la première seconde.
- **Milieu de session (forêt) :** le pic est la fiche hybride — photo réelle, checklist tactile, verdict qui bascule en direct (l.1390-1403). C'est le moment « je vérifie mon champignon » et l'UI répond instantanément (coche olive + barré, l.263-264). Le compteur n/5 en tabular-nums ne saute pas.
- **Vallées :** les erreurs IA sont adoucies par des messages français avec guidance (l.1520-1529) — pas de « 429 Too Many Requests » brut. Le rappel « Jamais exporté » (l.2277) est une petite gifle sur l'onglet Stats, mais c'est une protection légitime.
- **Pic de danger :** l'alerte MORTEL avec centre antipoison (l.1328, 2181) est non négociable et bien placée (juste sous le nom, avant la galerie). Le verdict ☠️ dynamique « n/n critères vérifiés » transforme la peur en action vérifiable — excellent design émotionnel de la sécurité.
- **Fin de journée :** pas de faux pic « Tout terminé 🎉 » (aucun trouvé). Le pic de fin est le toast « Cueillette enregistrée ✅ » + le badge du header qui monte (l.2433) — la satisfaction du carnet qui se remplit. Le graphique mensuel (l.2265-2268) donne la récompense visuelle de la saison.
- **Valence :** aucune erreur détectée — le hors-ligne n'est jamais montré en rouge, le rouge est strictement danger/destruction.

---

## 5. Les 10 heuristiques de Nielsen

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 4 | Compteur n/5, verdicts dynamiques, toast aria-live, badge récoltes, position scroll mémorisée — tout est visible et à jour |
| 2 | Correspondance système ↔ monde réel | 4 | Vocabulaire du cueilleur québécois, métaphores carnet/panier, zéro jargon technique |
| 3 | Contrôle et liberté | 4 | Annuler partout, garde-fou perte de saisie (l.1578-1582), analyse annulable, restauration d'espèces, double confirmation destruction |
| 4 | Cohérence et standards | 3 | Système très tenu (helpers unifiés, tokens), mais : 🗑️ = masquer (l.1314), « guide » vs « Identifier », title photo-zone faux quand vide |
| 5 | Prévention des erreurs | 4 | Matche flou + synonymes + alerte ☠️ à la saisie, import versionné, double confirmation, fail-safe statut IA inconnu (l.2153-2154) |
| 6 | Reconnaissance plutôt que mémorisation | 3 | Filtres en puces visibles, suggestions d'espèces ; mais la fiche exige de retenir les critères non cochés (structurel) |
| 7 | Flexibilité et efficacité | 3 | FAB contextuel, « Réessayer » répète la source, génération IA en 1 clic ; pas de raccourcis avancés (acceptable pour 1 utilisateur) |
| 8 | Esthétique minimaliste | 3 | Memphis dense assumé ; la fiche détail empile ~8 blocs, les formulaires ont 7-11 champs |
| 9 | Aide à la reconnaissance des erreurs | 4 | Erreurs IA françaises avec guidance par cause, toasts explicites, messages d'erreur GPS clairs |
| 10 | Aide et documentation | 2 | Aucune aide intégrée : pas de page « Comment identifier », pas d'explication du verdict ⚠️/✅/☠️, la Règle d'or est le seul texte d'aide (l.391). Le centre antipoison est présent mais l'app n'explique jamais comment utiliser la checklist |

**Total : 34/40** — profil : exceptionnelle sur la sécurité et la prévention des erreurs (4-5-9), faible sur l'aide intégrée (10) et la densité (8).

---

## 6. Forces spécifiques

1. **La fiche hybride est un chef-d'œuvre de design de sécurité.** Photo réelle + description de ce qu'il faut vérifier + checklist tactile + verdict dynamique (⚠️ à 0 critère ET après décoche, ✅ vert réservé comestibles/prudence, ☠️ rouge « n/n critères vérifiés — MORTELLE : ne pas consommer ») — le tout placé juste sous l'alerte de sécurité (l.1343-1356). La peur est convertie en protocole vérifiable, et le compteur n/5 en tabular-nums ne bouge pas pendant la coche. C'est le meilleur moment de l'app, et c'est le moment qui compte.
2. **La discipline Memphis est totale, jusque dans les micro-détails.** Poignée de feuille avec hit-area étendu (l.292), appui « bouton qu'on enfonce » (l.154), tabular-nums sur tous les compteurs dynamiques (l.54, 305), text-wrap:balance sur titres (l.47), outlines 1 px sur images (l.141, 258). Aucune boîte système, aucune ombre floutée, aucun uppercase — la doc est respectée à la lettre, ce qui est rarissime.
3. **La prévention des erreurs est pensée comme un système, pas comme des alertes.** Matche flou Levenshtein ≤2 (l.936-941) + inclusion des synonymes vernaculaires (l.944-952) + alerte ☠️ à la saisie (l.1492-1494) + badge de sécurité archivé pour les espèces supprimées (l.1416-1418) + fail-safe statut IA inconnu (l.2153-2154) + import versionné (l.2305-2310). Chaque couche attrape une classe d'erreur différente, et le principe « toute ambiguïté penche vers la prudence » (PRODUCT.md l.61) est implémenté, pas seulement proclamé.

---

## 7. Problèmes prioritaires

### P1-1 — Le nom latin est illisible (2.56:1) sur chaque item du guide et chaque fiche
- **Preuve :** `.ligne-latin{font-style:italic; opacity:.65; font-size:13px}` (l.332), utilisé l.1311 (liste guide) et l.1369 (fiche). Ratio calculé : 2.56:1 sur blanc — échec AA (4.5:1).
- **Pourquoi c'est grave :** le nom latin est l'outil de désambiguïsation n°1 du mycologue (c'est lui qui distingue la chanterelle de la fausse chanterelle). Le rendre quasi invisible à l'œil fatigué de la forêt, c'est affaiblir l'outil de sécurité.
- **Fix :** passer l'opacité à .85 (comme `.meta`, l.144) → ~4.9:1, ou utiliser `var(--cuir)` à opacité 1 (5.45:1). Un changement d'une ligne.

### P1-2 — Le bouton 🗑️ du guide promet la destruction, exécute le masquage
- **Preuve :** `<button class="btn-suppr-item" title="Masquer ou supprimer" onclick="...ouvrirChoixEspece(...)">🗑️</button>` (l.1314) — l'icône corbeille + le style rouge de suppression (l.127-132) annoncent « supprimer », le clic ouvre une modale dont l'action par défaut est « 🙈 Masquer du guide » (l.488), réversible.
- **Pourquoi c'est grave :** un utilisateur pressé (en forêt, une main) qui veut *masquer* une espèce peut croire qu'il la supprime ; inversement, l'icône corbeille dévalue le vrai bouton de suppression définitive. La 4e passe avait corrigé « Masquer en gris » pour les variétés perso (l.1362) mais pas ce bouton.
- **Fix :** remplacer l'icône par « 🙈 » (ou « ⋯ ») et le title par « Masquer ou supprimer » sans corbeille ; garder la corbeille uniquement dans la modale de choix, sur le bouton rouge « Supprimer définitivement » (l.489).

### P2-1 — Trois micro-textes sous le seuil AA (12.5 px et moins)
- **Preuves :** `.info-gps` opacité .75 → 3.36:1 (l.202, messages GPS et erreurs) ; `.mois-col .lab` opacité .7 → 2.86:1 (l.325, étiquettes du graphique mensuel) ; `.stat-carte .libelle` carte 1 opacité .8 → 3.27:1 (l.306, « Total récolté » sur fond jaune — les cartes 2-4 ont été corrigées à opacité 1, l.307, la carte 1 est restée en arrière).
- **Pourquoi :** ce sont exactement les textes lus en conditions difficiles (soleil, écran sale, gants) : le retour GPS en forêt, les mois du graphique, le libellé de la KPI principale.
- **Fix :** opacité 1 sur `.info-gps` et `.mois-col .lab` (noir pur = 15.87:1), opacité 1 sur le libellé de la carte 1 (noir sur jaune = 7.59:1). Trois unilignes.

### P2-2 — Le zoom de l'image de fiche est promis au curseur mais inaccessible au clavier
- **Preuve :** `<img class="detail-img" ... onclick="ouvrirLightbox(this.src)" style="cursor:zoom-in">` (l.1366) — pas de role, pas de tabindex, pas d'aria-label. Le span « 🔍 Agrandir » des spécificités a été corrigé (l.1348) mais pas l'image principale de la fiche.
- **Pourquoi :** l'utilisateur clavier/lecteur d'écran ne peut pas agrandir la photo d'identification principale — c'est la photo la plus importante de la fiche.
- **Fix :** ajouter `role="button" tabindex="0" aria-label="Agrandir la photo"` sur l'img (le handler clavier global Enter/Espace l.990-995 le rendra actif automatiquement).

### P2-3 — Le `title` des zones photo ment quand la zone est vide
- **Preuve :** `title="Cliquez pour retirer la photo"` sur les trois photo-zones (l.521, 569, 626) ; le clic sur une zone vide ouvre la galerie (l.1115-1119).
- **Pourquoi :** au survol (ou à l'audition par lecteur d'écran), l'app promet « retirer la photo » alors qu'il n'y en a pas — le geste réel est « ajouter ». Micro-menterie qui s'accumule.
- **Fix :** mettre à jour le title selon l'état (vide → « Ajouter une photo », pleine → « Retirer la photo ») dans `afficherPhoto` (l.1105-1109).

### P3-1 — `font-weight:900` hors de la plage chargée
- **Preuve :** `.spec-num` (l.259) et `.spec-carre` (l.262) en 900 ; la feuille de style ne charge que 400-700 (l.17). Le navigateur synthétise ou arrondit — rendu variable selon plateforme, et DESIGN.md interdit les graisses hors 400-700.
- **Fix :** passer à 700 (le gras Fredoka est déjà très rond).

---

## 8. Red flags par persona

### Jonathan, power user (propriétaire, à la maison, gestion des données)
- **Ce qui marche :** export/import versionné avec résumé du contenu (l.2311-2313), double confirmation destruction, restauration sélective, stats calculées en direct.
- **Red flags :** le rappel « Jamais exporté » (l.2277) est le seul élément qui « gronde » — mais il disparaît après le premier export (l.2289), bien vu. Le bouton 🗑️ du guide (P1-2) est le piège principal : un power user qui réorganise son guide peut masquer par erreur en croyant supprimer.
- **Pire moment :** l'import d'un fichier v4 (alerte « checklist perdue ») — bien géré, mais l'utilisateur doit comprendre que ses vérifications terrain disparaîtront.

### Utilisateur à accessibilité réduite (clavier, lecteur d'écran)
- **Ce qui marche :** focus trap + Escape sur modales (l.1027-1042), lightbox dialog avec restauration du focus (l.2082-2101), clavier Enter/Espace global (l.990-995), aria-live toast (l.692), focus-visible ambre (l.190).
- **Red flags :** l'image de fiche non focusable (P2-2) ; les suggestions d'autocomplétion sans rôle listbox ; les puces filtres sont des spans role=button (correct) mais sans aria-pressed — l'état actif n'est annoncé que visuellement (fond coloré + inclinaison).
- **Pire moment :** ouvrir une fiche et ne pas pouvoir agrandir la photo principale — l'outil d'identification est amputé.

### Utilisateur mobile distrait (en forêt, une main, hors-ligne)
- **Ce qui marche :** tout est hors-ligne (SW cache-first, 105 photos specs + 21 espèces + credits.json dans le cache, l.6-140), cibles ≥44 px, FAB contextuel, verdicts sous l'alerte (zéro scroll pour la décision), analyse annulable.
- **Red flags :** la feuille variété (11 champs) est longue à remplir en forêt — mais c'est une tâche de maison, pas de terrain. Le vrai risque terrain : le nom latin illisible (P1-1) au moment de comparer deux espèces.
- **Pire moment :** identifier un champignon à confiance 85 % (« À vérifier ») et devoir comparer avec le guide — le nom latin de la fiche est à 2.56:1, illisible au soleil.

---

## 9. Observations mineures

- `.spec-num` et `.spec-carre` en font-weight:900 (l.259, 262) — voir P3-1.
- `.rang:nth-child(4n+2/3/4)` (l.315-317) : la couleur des pastilles de rang dépend de la position, pas de la valeur — deux tops (5 vs 3 entrées) produisent des grammaires de couleur différentes.
- Le toast « Analyse terminée ✨ » (l.2141, 2197) célèbre avec un ✨ même quand le résultat est « À vérifier » — l'emoji devrait dépendre du verdict.
- `title="Cliquez pour retirer la photo"` faux quand vide (l.521, 569, 626) — voir P2-3.
- Le bandeau « Configurer la clé → » (l.2118-2121) navigue vers Paramètres et focus la clé : excellent, mais le bouton est dans une alerte orange — le contraste du texte noir sur #F4E3C3 est bon (13.52:1).
- `COULEURS_MOIS` (l.2231) : janvier/février en rouille, mars en ambre — la couleur des barres mensuelles ne suit pas les saisons (printemps = olive en mai, automne = ambre en septembre) mais un cycle fixe. Détail, mais le mapping saisonnier serait plus « récolte ».
- Le graphique mensuel n'a pas de valeurs au survol/au clic — impossible de savoir le poids exact d'un mois sans calcul mental.
- `manifest.json` : `orientation: "portrait"` (l.11) — verrouille l'orientation ; acceptable pour une app une-main, mais à documenter.
- La recherche du guide (l.1320) re-rend la liste à chaque frappe sans debounce — 21 espèces, imperceptible, mais le pattern est là.
- Le `select` météo (l.556-561) utilise des emojis dans les options — rendu variable selon plateforme (❄️ vs ☃️).
- `sw.js` : le fetch handler exclut `wikimedia.org` et `googleapis.com` du cache (l.157) — les photos distantes des variétés perso ne sont donc jamais mises en cache, cohérent avec le message « visible après une 1re visite avec réseau » (l.1757).

---

## 10. Questions provocatrices

1. **Le nom latin à 2.56:1 (P1-1) :** si le nom latin est l'outil de désambiguïsation n°1, pourquoi est-il le texte le plus pâle de l'interface ? Quelle information mérite moins de contraste que lui ?
2. **Le bouton 🗑️ du guide (P1-2) :** si « masquer » est réversible et « supprimer » est irréversible, pourquoi partagent-ils la même icône corbeille ? Quelle icône représenterait honnêtement « ranger dans un tiroir » ?
3. **L'aide (heuristique 10, score 2) :** l'app dit « En cas de doute, on ne mange pas » — mais où explique-t-elle *comment* utiliser la checklist, ce que signifie ⚠️ vs ✅ vs ☠️, et pourquoi 5 critères ? Une page « Comment identifier » d'une carte suffirait-elle, ou est-ce que l'absence d'aide est un choix assumé de simplicité ?
4. **Le toast « Analyse terminée ✨ » (l.2141) :** faut-il vraiment célébrer quand l'IA répond « À vérifier » ? Le ✨ ne devrait-il pas être réservé aux identifications fiables, et le verdict incertain annoncé sobrement ?
5. **Les couleurs des rangs (l.315-317) :** si la couleur des pastilles de rang change selon le nombre d'entrées (top 3 vs top 5), que signifie-t-elle ? Ne serait-il pas plus honnête de colorer par valeur (1er = ambre, 2e = olive, 3e = cuir) ?
6. **Le graphique mensuel sans valeurs (l.2265-2268) :** un cueilleur qui veut savoir « combien j'ai récolté en septembre » doit-il vraiment faire le calcul mental ? Un libellé au clic (ou une valeur au-dessus de la barre) changerait-il la valeur du graphique ?
7. **La feuille variété (11 champs) :** le pré-remplissage IA réduit l'effort, mais la feuille reste intimidante. Faut-il la diviser en étapes (identité → détails → photo) ou est-ce que la longueur est acceptable pour une tâche rare ?
8. **Le verrouillage portrait (manifest l.11) :** en forêt, un utilisateur qui photographie un champignon au sol ne préférerait-il pas le paysage ? Le portrait est-il un choix de conception ou un héritage ?
9. **Le rappel « Jamais exporté » (l.2277) :** si les données ne quittent jamais l'appareil, l'export est la seule sauvegarde. Faut-il un rappel périodique (toast mensuel) plutôt qu'un bandeau permanent sur Stats ?
10. **Les suggestions d'espèces (l.1443) :** sans rôle listbox ni aria-expanded, un lecteur d'écran annonce-t-il les suggestions ? Et si l'utilisateur tape « chanterelle du Québec » (inclusion), l'alerte synonyme se déclenche-t-elle à tort pour une variété locale légitime ?

---

*Rapport généré par lecture statique (Assessment A) — aucun fichier modifié. Correctifs des passes 4-10 vérifiés dans le code et confirmés ; les problèmes ci-dessus sont nouveaux ou résiduels.*
