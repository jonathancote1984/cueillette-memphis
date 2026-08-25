# Assessment A — Critique design (12e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2471 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v33)
**Méthode :** lecture statique seule (Assessment A), vérification des correctifs de la 11e passe (commit `2c6c5e3`) dans le code, contrastes recalculés par script WCAG exact (ratios composites pour les opacités).
**Date :** 13 août 2026

---

## 1. Verdict de spécificité design

**Conceptuelle : ~90 %.** Inchangé et tenu : le vocabulaire est entièrement du domaine — « spots », « cueillettes », « Règle d'or », « spécificités à repérer », « centre antipoison 1-800-463-5060 », « volve en sac », « anneau coulissant », « sporée rose » (l.821, 835, 875, 1328, 1388). La métaphore du carnet de chasse est partout : pastille-compteur de récoltes (l.373), FAB « panier » rose (l.94-104), zigzag d'en-tête (l.376-377), pois au fond (l.32-33), formes SVG flottantes (l.355-358). Aucune interface générique ne dirait « vérifiez la sporée rose » ni « toute amanite à volve est à proscrire » (l.886).

**Visuelle : ~85 %.** Le test « une capture sans texte révèle-t-elle le domaine ? » : oui — vignettes à rayures ambre/blanc (l.138), photos de champignons 16:9, badges MORTEL rouges cerclés de noir, palette automne/terre. La discipline Memphis est intacte : bordures noires 3 px sur toute surface colorée, coins cassés 18/5 px systématiques (l.119, 123, 255), ombres dures sans flou (aucun `box-shadow` flouté trouvé), inclinaisons -1/-2° (l.46, 114, 173), zéro boîte système navigateur (aucun `window.confirm/alert`), zéro uppercase forcé, Fredoka 400-700 seule (l.17).

**Verdict :** interface fortement spécifique, les deux axes tenus — le style n'est pas un habillage mais le produit lui-même (le plaisir de la récolte est un principe produit, PRODUCT.md l.64). La carte « 🍄 Comment identifier » (l.458-467) renforce encore le caractère « carnet de chasse » : elle parle au cueilleur dans sa langue.

---

## 2. Évaluation holistique

### Hiérarchie visuelle
- Échelle typographique disciplinée : display 21 px/700 (h1, l.45), titre-vue 20 px/700 en pastille blanche cerclée (l.110-115), titre de feuille 18 px/700 en pastille ambre (l.293-295), corps 16 px, label 13 px/700, meta 12.5 px. Poids 400-700 uniquement — le `font-weight:900` de `.spec-num`/`.spec-carre` (P3-1 de la passe 11) est corrigé à 700 (l.259, 262) ✅.
- **Résidu :** `.rang:nth-child(4n+2/3/4)` (l.315-317) — la couleur des pastilles de rang dépend toujours de la position dans la liste, pas de la valeur. Un top-3 spots (l.2268) colorera 1-2-3 en jaune/bleu/vert alors que le top-5 espèces (l.2263) colorera 1-2-3-4-5 en jaune/bleu/vert/rose/jaune. Même composant, deux grammaires de couleur.
- Les 4 cartes stats volontairement inégales (jaune/bleu/vert/rose, l.298-304) : choix Memphis assumé et documenté.

### Architecture de l'information
- 5 onglets complets (l.473-479), FAB contextuel (📍 en Spots, ＋ ailleurs, masqué en Stats/détail/Paramètres, l.974), bouton ← sticky en détail (l.56-63, 374). Rien d'atteignable n'est innavigable.
- **Résidu terminologique :** « Identifier » (onglet, l.390) vs « guide » (toasts « Espèce masquée du guide » l.1077, « Restaurer des espèces » l.1329, bouton « Voir la fiche du guide » l.2204). Deux termes pour un même objet.
- **Résidu de valence (P1-1, voir section 7) :** la liste du guide a été corrigée (🙈, l.1326) mais la fiche détail garde « 🗑️ Masquer » (l.1374) — deux surfaces, deux icônes pour la même action réversible.

### Adéquation émotionnelle
- Le concept « La Récolte » est exécuté avec une cohérence rare : rebonds élastiques (cubic-bezier(.2,1.3,.4,1), l.281), appui « bouton qu'on enfonce » (l.154), poignée de feuille avec hit-area étendu (l.292), tabular-nums sur les compteurs (l.54, 305), sortie de feuille sans rebond (l.286).
- **Valence parfaite sur le danger :** rouge strictement réservé au mortel/destruction (Règle du Rouge Mortel tenue — vérifié : « Masquer » est gris l.1374, le bouton 🙈 de la liste est blanc/noir l.1326), verdicts ☠️ dynamiques « n/n critères vérifiés — MORTELLE : ne pas consommer » (l.1366), ✅ vert réservé comestibles/prudence (l.1365).
- **Nouvelle fausse célébration (P2-1) :** le toast « Analyse terminée ✨ » est émis même quand l'identification échoue (« Impossible d'identifier ce champignon avec certitude », l.2153) — le ✨ célèbre un échec.
- États vides chaleureux et orientés action : « Appuyez sur le bouton rose pour ajouter votre premier coin secret ! » (l.1156), « Aucun champignon trouvé » (l.1313).

### Découvrabilité
- Le bandeau « Configurer la clé → » (l.2130-2133) est bien placé et focus la clé (l.2132) — correctif efficace confirmé.
- La checklist terrain est découverte par l'ouverture d'une fiche, mais la nouvelle carte « 🍄 Comment identifier » (l.458-467) documente désormais les verdicts ⚠️/✅/☠️ et le centre antipoison — l'heuristique 10 progresse (voir section 5).
- Le bouton « ↩️ Restaurer des espèces » n'apparaît que s'il y a des espèces masquées (l.1328-1330) : bonne divulgation progressive.

### Composition
- Colonne unique max 640 px (l.106), grille 2 colonnes pour paires de boutons (l.192), cartes espacées 16 px, feuilles bottom-sheet max 84 vh (l.282). La grille2 casse proprement à 320 px.
- **Risque de chevauchement :** le bouton 🙈 (44 px, position absolue top:8 right:8, l.1326) flotte au-dessus du `.corps` de l'item ; le nom + badge statut (flex-wrap, l.143) peuvent passer dessous sur petit écran — le badge « MORTEL ☠️ » est long. Non confirmé sans rendu, mais le pattern est là.

### Typographie
- Fredoka 400-700 uniquement (l.17), pas d'uppercase forcé, pas de césure, `text-wrap:balance` sur titres (l.47, 114). Meta à opacité .85 (l.144) — conforme et lisible.
- **Correctifs 11e confirmés (ratios exacts, script WCAG) :**
  - `.ligne-latin` opacity .85 (l.332) : **4.91:1** ✅ AA (était 2.56:1)
  - `.info-gps` opacity 1 (l.202) : **15.87:1** ✅ (était 3.36:1)
  - `.mois-col .lab` opacity 1 (l.325) : **15.87:1** ✅ (était 2.86:1)
  - `.stat-carte .libelle` carte 1 opacity 1 (l.306) : **7.59:1** ✅ (était 3.27:1)
- **Résidus de la même famille (P2-4) :** `.vide-etat` opacity .8 (l.335) : **3.99:1** à 15 px — échec AA (texte normal) ; note « Touchez une espèce… » opacity .75 inline (l.528) : **3.36:1** à 12 px — échec AA.
- Passent : noir/olive 4.61 ✅, noir/ambre 7.59 ✅, blanc/rouge 6.07 ✅, blanc/orange 4.67 ✅, noir/creme 14.08 ✅, noir/C87224 4.79 ✅, blanc/terracotta 4.95 ✅, blanc/cuir 5.45 ✅, noir/gris 6.08 ✅, vert-mesure 4.97 ✅, cuir/blanc 5.45 ✅, spec-zoom noir sur blanc .92 → 7.25 ✅, spec-desc .85 → 4.91 ✅, illu-desc .85 → 4.91 ✅, credits-desc .85 → 4.91 ✅.

### Couleur
- Palette AUTOMNE/TERRE respectée à 100 % : les seules couleurs hors palette sont documentées dans DESIGN.md (onglets actifs l.89-93, dégradé header l.38, fonds d'alertes l.220/226, barre vide l.2279, COULEURS_MOIS l.2243). Aucune dérive non documentée.
- **Règle du Rouge Mortel tenue** : le rouge n'apparaît que pour MORTEL, suppression, compteur. Le bouton 🙈 de la liste est blanc/noir (l.1326), « Masquer » de la fiche est gris (l.1374) — mais l'icône 🗑️ de ce dernier reste une dérive sémantique (voir P1-1).

### Accessibilité
- Correctifs 5e-11e passes **confirmés dans le code** : clavier Enter/Espace sur role=button (l.1000-1005), focus-visible ambre (l.190), aria-live toast (l.702), prefers-reduced-motion (l.347-349), lightbox role=dialog + aria-label + Escape + restauration du focus (l.2094-2114), focus trap + Escape sur modales (l.1031-1052), cibles ≥44 px, span « 🔍 Agrandir » avec role=button + stopPropagation (l.1360), **image de fiche focusable** `role="button" tabindex="0" aria-label="Agrandir la photo"` (l.1378) ✅, **title photo-zone dynamique** (l.1117) ✅.
- **Trous restants :**
  - **La fiche détail n'a aucun heading** (P2-2) : `vue-detail` est une section vide (l.429-431), le contenu injecté (l.1376-1390) n'a ni h2 ni h3 — le nom de l'espèce est un `<p class="sous">` dans le header (l.1392) et les sections (Spécificités, Description, Caractéristiques, Confusions) sont des `<span class="guide-sujet">`. Un lecteur d'écran ne peut pas naviguer par titres dans la fiche.
  - **La modale de choix n'a pas de focus initial** (P2-3) : `ouvrirChoixEspece` (l.1056-1065) n'appelle aucun `.focus()`, contrairement à `confirmer` qui focus « Annuler » (l.1021). Le focus reste sur le bouton déclencheur derrière la modale.
  - **role=button imbriqués** : `.spec-carte` (role=button, l.1359) contient un span role=button (Agrandir, l.1360) ; `.item` du guide (role=button, l.1319) contient un vrai `<button>` (🙈, l.1326). L'ARIA interdit les interactifs imbriqués — annonce ambiguë possible.
  - L'img de spécificité cliquable (l.1360) n'a ni role ni tabindex (l'action reste accessible via le span Agrandir — résidu partiel du P2-2 de la passe 11).
  - Puces filtres sans `aria-pressed` (l.1287-1290) ; suggestions d'autocomplétion sans rôle listbox/aria-expanded (l.1444-1458) — résidus déjà notés en 11e.

### États
- Chargement : pas d'écran initial (IndexedDB local, quasi instantané) — acceptable.
- Erreurs IA : `messageErreurIA` français avec guidance par cause (l.1532-1542), catch identification photo inclus (l.2210-2216) — confirmé.
- Analyse annulable (AbortController + ✋ Annuler, l.2120-2126, 2142) et récupérable (réouverture + toast, l.2153, 2209) — confirmé.
- Import versionné (alerte si < 5 ou > 5, l.2317-2322) — confirmé. **Cas limite :** un fichier sans champ `version` (l.2317 : `data.version ? 0 : null`) passe sans aucune alerte — perte de checklist silencieuse possible pour un format indatable.
- « Réessayer » répète la dernière source (l.2182, `derniereSourcePhoto` l.2119) — confirmé.
- **Aucun faux « all clear »** : pas de « Tout terminé 🎉 », stats calculées (l.2251-2281).

### Copy
- Français du Québec authentique (« boisé du rang 4 », « coin secret », « en forêt »). Toasts chaleureux (« Spot enregistré ✅ », « Espèce masquée 🙈 »).
- **Résidus :** « guide » vs « Identifier » (voir AI) ; « 🗑️ Masquer » de la fiche détail (l.1374) mélange l'icône de destruction et le verbe réversible ; le toast « Analyse terminée ✨ » (l.2153) célèbre un échec d'identification.
- La carte « Comment identifier » (l.458-467) est un modèle de copy pédagogique : chaque verdict est expliqué avec sa conséquence (« ne consommez pas », « récolte possible en respectant la prudence », « ne pas consommer, jamais ») + antipoison.

### Cas limites
- Dates : `aujourdhui()` local (l.709-712), `fmtDate` local (l.713-717) — pas de piège UTC. Graphique mensuel parse le mois localement (l.2273) — cohérent.
- Poids : virgule acceptée (l.724-728), conversion kg/lb cohérente, labels d'unité mis à jour partout (l.2356-2359, 2461-2464).
- Checklist : réindexation des coches au retrait d'une spécificité (l.2054-2059) — confirmé. Export v5 inclut checklist (l.2294), « Tout effacer » vide la checklist (l.2345) — confirmés.
- Matche flou Levenshtein ≤2 (l.946-951) + inclusion des synonymes (l.954-961) + alerte ☠️ à la saisie (l.1504-1506) — confirmés. Le cas « chanterelle du Québec » (inclusion → alerte synonyme à tort pour une variété locale) reste un comportement défensif acceptable.
- **Nouveau cas limite :** la carte « Comment identifier » dit « ☠️ 5/5 vérifiés sur une espèce mortelle » (l.464) en dur, alors que le nombre de critères est variable (ajout/retrait de spécificités, l.2022-2032, 2051-2068) — une fiche mortelle à 6 critères dira 6/6 dans le verdict mais la carte d'aide promet 5/5.

---

## 3. Évaluation de charge cognitive

1. **Focus unique** ✅ — chaque vue sert une tâche ; le FAB contextuel renforce le focus.
2. **Chunking ≤ 4** ❌ — la fiche détail empile : alerte + galerie (5 spécificités) + verdicts + saison/habitat + description + caractéristiques (4-5 puces) + confusions + 2-4 boutons = ~8 blocs. Le chunking par carte est bon, le nombre de blocs dépasse 4.
3. **Regroupement visuel** ✅ — cartes cerclées de noir, sections avec pastilles de sujet (l.329-330), verdicts sous l'alerte (l.1364-1367), espacement 16 px.
4. **Hiérarchie** ✅ — 4 niveaux de titre distincts (21/20/18/16 px), poids 400-700, inclinaison comme marqueur de titre. (Mais voir P2-2 : cette hiérarchie n'existe pas en HTML sémantique dans la fiche détail.)
5. **Une chose à la fois** ✅ — feuilles bottom-sheet, modales, lightbox. Rien ne se chevauche.
6. **Choix minimaux ≤ 4** ❌ — feuille cueillette : 7 champs ; feuille variété : 11 champs + 2 alertes. Groupés logiquement, pré-remplissage IA (l.1659-1682) réduit l'effort réel.
7. **Mémoire de travail** ❌ — retenir statut, critères non cochés, saison, confusions pendant qu'on manipule le champignon. Atténué par le compteur n/5 persistant et les verdicts visibles ; la carte « Comment identifier » (l.458-467) aide désormais à décoder les verdicts.
8. **Divulgation progressive** ✅ — le guide montre nom + badge + saison + habitat ; la fiche révèle le reste. Filtres en puces, restauration conditionnelle.

**Échecs : 3/8** (chunking fiche, choix formulaires, mémoire de travail) — inchangé, structurel à la tâche.

---

## 4. Voyage émotionnel (peak-end rule)

- **Entrée :** animation `pop` des vues (l.108-109) avec rebond élastique ; header dégradé ambre + zigzag + formes flottantes — le ton « carnet de chasse » dès la première seconde.
- **Milieu de session (forêt) :** le pic est la fiche hybride — photo réelle, checklist tactile, verdict qui bascule en direct (l.1402-1416). Le compteur n/5 en tabular-nums ne saute pas. La carte « Comment identifier » (Paramètres) documente ce moment — l'aide arrive là où on la cherche.
- **Vallées :** les erreurs IA sont adoucies par des messages français avec guidance (l.1532-1542). **Nouvelle vallée :** le toast « Analyse terminée ✨ » (l.2153) quand l'IA répond « Impossible d'identifier » — une fausse célébration qui transforme un moment de doute en moment de joie, avant que le contenu de la feuille ne ramène à la réalité.
- **Pic de danger :** l'alerte MORTEL avec centre antipoison (l.1340, 2193) est non négociable et bien placée (juste sous le nom, avant la galerie). Le verdict ☠️ dynamique « n/n critères vérifiés » transforme la peur en action vérifiable.
- **Fin de journée :** pas de faux pic « Tout terminé 🎉 ». Le pic de fin est le toast « Cueillette enregistrée ✅ » + le badge du header qui monte (l.2445). Le graphique mensuel (l.2277-2280) donne la récompense visuelle de la saison.
- **Valence :** aucune erreur de valence rouge — le hors-ligne n'est jamais montré en rouge, le rouge est strictement danger/destruction.

---

## 5. Les 10 heuristiques de Nielsen

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 4 | Compteur n/5, verdicts dynamiques, toast aria-live, badge récoltes, position scroll mémorisée — tout est visible et à jour |
| 2 | Correspondance système ↔ monde réel | 4 | Vocabulaire du cueilleur québécois, métaphores carnet/panier, zéro jargon technique |
| 3 | Contrôle et liberté | 4 | Annuler partout, garde-fou perte de saisie (l.1586-1594), analyse annulable, restauration d'espèces, double confirmation destruction |
| 4 | Cohérence et standards | 3 | Correctif 🙈 appliqué à la liste (l.1326) mais la fiche détail garde « 🗑️ Masquer » (l.1374) ; « guide » vs « Identifier » ; role=button imbriqués |
| 5 | Prévention des erreurs | 4 | Matche flou + synonymes + alerte ☠️ à la saisie, import versionné, double confirmation, fail-safe statut IA inconnu (l.2164-2166) |
| 6 | Reconnaissance plutôt que mémorisation | 3 | Filtres en puces visibles, suggestions d'espèces ; la fiche exige de retenir les critères non cochés (structurel) |
| 7 | Flexibilité et efficacité | 3 | FAB contextuel, « Réessayer » répète la source, génération IA en 1 clic ; pas de raccourcis avancés (acceptable pour 1 utilisateur) |
| 8 | Esthétique minimaliste | 3 | Memphis dense assumé ; la fiche détail empile ~8 blocs, les formulaires ont 7-11 champs |
| 9 | Aide à la reconnaissance des erreurs | 3 | Erreurs IA françaises avec guidance par cause, messages GPS clairs ; mais le toast « Analyse terminée ✨ » célèbre un échec d'identification (l.2153) |
| 10 | Aide et documentation | 3 | Carte « 🍄 Comment identifier » ajoutée (l.458-467) : verdicts ⚠️/✅/☠️ expliqués + centre antipoison — l'heuristique 10 progresse (était 2) ; reste : pas d'aide contextuelle dans la fiche elle-même |

**Total : 34/40** — plateau honnête : les correctifs de la 11e passe tiennent tous (H10 2→3), mais la dette résiduelle (🗑️ Masquer fiche, toast ✨ sur échec) compense le gain (H9 4→3). Profil : exceptionnelle sur la sécurité et la prévention des erreurs (4-5), faible sur la densité (8) et l'aide contextuelle (10).

---

## 6. Forces spécifiques

1. **La fiche hybride est un chef-d'œuvre de design de sécurité — désormais documentée.** Photo réelle + description de ce qu'il faut vérifier + checklist tactile + verdict dynamique (⚠️ à 0 critère ET après décoche, ✅ vert réservé comestibles/prudence, ☠️ rouge « n/n critères vérifiés — MORTELLE : ne pas consommer »), le tout juste sous l'alerte de sécurité (l.1340-1367). La peur est convertie en protocole vérifiable, et la carte « Comment identifier » (l.458-467) explique enfin ce que signifient les verdicts — l'aide est au niveau du moment où l'utilisateur en a besoin.
2. **La discipline Memphis est totale, jusque dans les micro-détails.** Poignée de feuille avec hit-area étendu (l.292), appui « bouton qu'on enfonce » (l.154), tabular-nums sur tous les compteurs dynamiques (l.54, 305), text-wrap:balance sur titres (l.47), outlines 1 px sur images (l.141, 258), sortie de feuille sans rebond (l.286). Aucune boîte système, aucune ombre floutée, aucun uppercase — la doc est respectée à la lettre, ce qui est rarissime.
3. **La prévention des erreurs est pensée comme un système, pas comme des alertes.** Matche flou Levenshtein ≤2 (l.946-951) + inclusion des synonymes vernaculaires (l.954-961) + alerte ☠️ à la saisie (l.1504-1506) + badge de sécurité archivé pour les espèces supprimées (l.1428-1430) + fail-safe statut IA inconnu (l.2164-2166) + import versionné (l.2317-2322) + double confirmation destruction (l.1092-1093, 2342-2343). Chaque couche attrape une classe d'erreur différente, et le principe « toute ambiguïté penche vers la prudence » (PRODUCT.md l.61) est implémenté, pas seulement proclamé.

---

## 7. Problèmes prioritaires

### P1-1 — « 🗑️ Masquer » dans la fiche détail : le correctif de la 11e passe est partiel
- **Preuve :** la liste du guide a bien été corrigée — `<button class="btn-suppr-item" title="Masquer ou supprimer" ...>🙈</button>` (l.1326). Mais la fiche détail des espèces d'origine garde `<button class="btn btn-gris" onclick="ouvrirChoixEspece(...)">🗑️ Masquer</button>` (l.1374) — la corbeille + le verbe réversible cohabitent toujours.
- **Pourquoi c'est grave :** c'est exactement le problème que la 11e passe prétendait corriger (P1-2 : « l'icône corbeille promet la destruction, le geste par défaut est le masquage réversible »). Deux surfaces, deux icônes pour la même action : l'utilisateur qui a appris « 🙈 = masquer » dans la liste rencontre « 🗑️ = masquer » dans la fiche. La corbeille dévalue aussi le vrai bouton de suppression définitive (qui, lui, est dans la modale, l.499).
- **Fix :** remplacer par « 🙈 Masquer » (ou « 🙈 » seul) dans la fiche détail, comme dans la liste. Un changement d'une ligne, même classe que le correctif déjà appliqué.

### P2-1 — Le toast « Analyse terminée ✨ » célèbre un échec d'identification
- **Preuve :** dans la branche `!r || !r.espece || r.espece === 'inconnu'` (l.2152-2153) : `if (!$('sheet-idphoto').classList.contains('ouverte')) { ouvrirFeuille('sheet-idphoto'); toast('Analyse terminée ✨'); }` — le ✨ est émis juste avant d'afficher « Impossible d'identifier ce champignon avec certitude » (l.2156). Le même toast est émis sur succès (l.2209).
- **Pourquoi c'est grave :** en forêt, un toast « ✨ » après une analyse peut faire croire à une identification réussie — c'est le pire moment pour une ambiguïté. La 11e passe l'avait noté en observation mineure pour le cas « À vérifier » ; le cas « inconnu » est pire : le ✨ accompagne un échec franc.
- **Fix :** toast conditionnel — « Analyse terminée ✨ » seulement si une espèce a été identifiée ; « Analyse terminée — à vérifier » (ou pas de toast) pour le cas inconnu/incertain.

### P2-2 — La fiche détail n'a aucun heading : navigation par titres impossible
- **Preuve :** `vue-detail` est une section vide (l.429-431) ; le contenu injecté (l.1376-1390) n'a ni h2 ni h3. Le nom de l'espèce est un `<p class="sous">` dans le header (l.1392), les sections (Spécificités, Description, Caractéristiques, Confusions) sont des `<span class="guide-sujet">` (l.1356, 1385-1388).
- **Pourquoi c'est grave :** la fiche est l'écran le plus dense de l'app (~8 blocs). Un utilisateur de lecteur d'écran ne peut ni sauter à « Confusions possibles » ni comprendre la structure — il doit tout écouter linéairement. C'est aussi un manque de hiérarchie sémantique pour tous (le nom de l'espèce, information la plus importante, n'est pas un titre).
- **Fix :** rendre le nom de l'espèce un `<h2>` (ou h1 de la vue) et les `.guide-sujet` des `<h3>` — la hiérarchie visuelle existe déjà, il suffit de la baliser.

### P2-3 — La modale de choix n'a pas de focus initial
- **Preuve :** `ouvrirChoixEspece` (l.1056-1065) ajoute les classes `visible` mais n'appelle aucun `.focus()`. `confirmer`, lui, focus « Annuler » (l.1021). Le focus trap (l.1037-1052) ne s'active qu'à la première touche Tab.
- **Pourquoi c'est grave :** un utilisateur clavier qui ouvre « Masquer ou supprimer » garde le focus sur le bouton déclencheur derrière la modale — le lecteur d'écran annonce la page derrière, pas la modale. L'incohérence avec `confirmer` (qui focus) est flagrante.
- **Fix :** `$('choix-masquer').focus()` dans `ouvrirChoixEspece` (l'action par défaut, réversible — cohérent avec le choix défensif de `confirmer`).

### P2-4 — Micro-textes résiduels sous AA : la famille « opacity » n'est pas finie
- **Preuves (ratios exacts) :** `.vide-etat` opacity .8 (l.335) : **3.99:1** à 15 px — échec AA texte normal (passe seulement en large text 3:1) ; note « Touchez une espèce pour l'ajouter ou la retirer » opacity .75 inline (l.528) : **3.36:1** à 12 px — échec AA.
- **Pourquoi :** la 11e passe a corrigé trois micro-textes (info-gps, mois-col, stat-carte1) mais pas ceux-ci. Ce sont exactement les textes lus en conditions difficiles : l'état vide (premier contact avec une vue) et l'instruction de la feuille spot en forêt.
- **Fix :** opacity 1 sur `.vide-etat` (noir pur = 15.87:1) et sur la note l.528 (ou ≥ .85 → 4.91:1). Deux unilignes. Et énoncer la règle une fois pour toutes : « tout texte ≤ 13 px à opacité < .85 est interdit ».

---

## 8. Red flags par persona

### Jonathan, power user (propriétaire, à la maison, gestion des données)
- **Ce qui marche :** export/import versionné avec résumé (l.2323-2325), double confirmation destruction, restauration sélective, stats calculées en direct, carte Comment identifier.
- **Red flags :** le « 🗑️ Masquer » de la fiche détail (P1-1) — un power user qui réorganise son guide peut masquer par erreur en croyant supprimer, exactement le piège que la 11e passe a corrigé ailleurs. L'import d'un fichier sans champ `version` (l.2317) passe sans alerte — perte de checklist silencieuse.
- **Pire moment :** réorganiser le guide depuis une fiche (bouton 🗑️) après avoir appris que 🙈 = masquer dans la liste — deux langages pour une action.

### Utilisateur à accessibilité réduite (clavier, lecteur d'écran)
- **Ce qui marche :** focus trap + Escape sur modales (l.1031-1052), lightbox dialog avec restauration du focus (l.2094-2114), clavier Enter/Espace global (l.1000-1005), aria-live toast (l.702), focus-visible ambre (l.190), image de fiche focusable (l.1378).
- **Red flags :** la fiche détail sans headings (P2-2) — l'écran le plus dense est le moins navigable ; la modale de choix sans focus initial (P2-3) ; les role=button imbriqués (spec-carte > span Agrandir, item > button 🙈) ; puces sans aria-pressed ; suggestions sans listbox.
- **Pire moment :** ouvrir une fiche mortelle et devoir écouter 8 blocs linéairement pour atteindre « Confusions possibles » — l'information de sécurité la plus critique est la moins accessible.

### Utilisateur mobile distrait (en forêt, une main, hors-ligne)
- **Ce qui marche :** tout est hors-ligne (SW cache-first cqm-v33, 105 photos specs + 21 espèces + credits.json dans le cache, l.5-140), cibles ≥44 px, FAB contextuel, verdicts sous l'alerte (zéro scroll pour la décision), analyse annulable, « Réessayer » répète la source.
- **Red flags :** le toast « Analyse terminée ✨ » sur échec (P2-1) — en forêt, un ✨ peut faire croire à un succès ; les micro-textes résiduels (P2-4) lus au soleil ; le risque de chevauchement nom+badge+bouton 🙈 sur petit écran (l.1326).
- **Pire moment :** photographier un champignon suspect, voir « ✨ » dans le coin de l'œil, et devoir relire la feuille pour comprendre que l'identification a échoué.

---

## 9. Observations mineures

- `.rang:nth-child(4n+2/3/4)` (l.315-317) : couleur des pastilles de rang par position, pas par valeur — deux tops (5 vs 3 entrées) produisent des grammaires de couleur différentes. Résidu non corrigé depuis la 11e.
- `COULEURS_MOIS` (l.2243) : cycle fixe [rouille, rouille, ambre, olive, cuir, terracotta] ×2 — janvier/février en rouille, mars en ambre ; le mapping ne suit pas les saisons (printemps = olive, automne = ambre). Détail, mais le mapping saisonnier serait plus « récolte ».
- Le graphique mensuel n'a toujours pas de valeurs au survol/au clic (l.2277-2280) — impossible de savoir le poids exact d'un mois sans calcul mental.
- La carte « Comment identifier » dit « ☠️ 5/5 vérifiés » en dur (l.464) alors que le nombre de critères est variable (ajout/retrait, l.2022-2068) — micro-incohérence pédagogique (P3).
- L'img de spécificité cliquable (l.1360) n'a ni role ni tabindex — l'action zoom reste accessible via le span « 🔍 Agrandir », mais l'img promet le clic sans être focusable (résidu partiel du P2-2 de la 11e).
- Import sans champ `version` (l.2317) : `data.version ? 0 : null` — un fichier sans version passe sans alerte (P3, perte checklist silencieuse possible).
- Suggestions d'autocomplétion (l.1444-1458) : boutons `<button>` corrects, mais pas de rôle listbox/aria-expanded sur l'input.
- Puces filtres (l.1287-1290) : role=button corrects, mais sans aria-pressed — l'état actif n'est annoncé que visuellement.
- Le select météo (l.566-572) utilise des emojis dans les options — rendu variable selon plateforme (❄️ vs ☃️).
- La recherche du guide (l.1332) re-rend la liste à chaque frappe sans debounce — 21 espèces, imperceptible.
- `manifest.json` : `orientation: "portrait"` (l.10) — verrouille l'orientation ; acceptable pour une app une-main, mais à documenter.
- La lightbox (l.2094-2114) n'a pas de focus trap — un seul élément focusable (l'anc lui-même, tabIndex=-1), Tab sort dans la page derrière. Acceptable, mais à connaître.
- Le matche par inclusion (l.954-961) : « chanterelle du Québec » saisi en cueillette déclenchera l'alerte synonyme alors que c'est peut-être une variété locale — comportement défensif, acceptable.
- Terminologie « guide » vs « Identifier » (l.390 vs 1077, 1329, 2204) — résidu de renommage.
- Le rappel « Jamais exporté » (l.2289-2291) reste le seul élément qui « gronde » — nécessaire, disparaît après le premier export (l.2301).

---

## 10. Questions provocatrices

1. **Le « 🗑️ Masquer » de la fiche (l.1374) :** la 11e passe a remplacé la corbeille de la liste par 🙈 — pourquoi la fiche détail, qui ouvre la même modale, garde-t-elle la corbeille ? Quelle icône représente honnêtement « ranger dans un tiroir », et pourquoi deux surfaces n'ont-elles pas la même ?
2. **Le toast « Analyse terminée ✨ » (l.2153) :** faut-il célébrer quand l'IA répond « Impossible d'identifier » ? Le ✨ ne devrait-il pas être réservé aux identifications fiables, et l'échec annoncé sobrement — surtout en forêt, où un toast est lu en diagonale ?
3. **La fiche détail sans headings (P2-2) :** si le nom de l'espèce est l'information la plus importante de l'écran, pourquoi n'est-il pas un titre ? Un lecteur d'écran peut-il raisonnablement parcourir 8 blocs sans structure de titres — et la « Règle d'or » de sécurité est-elle servie par une fiche non navigable ?
4. **La modale de choix sans focus initial (P2-3) :** `confirmer` focus « Annuler » (défensif, l.1021) — pourquoi `ouvrirChoixEspece` ne focus-t-il pas « Masquer » (l'action par défaut, réversible) ? L'incohérence est-elle un oubli ou un choix ?
5. **Les micro-textes (P2-4) :** la 11e passe a corrigé trois opacités, il en reste deux sous AA (l.335, 528). Faut-il énoncer une règle unique « tout texte ≤ 13 px à opacité < .85 est interdit » pour que la famille soit finie une fois pour toutes ?
6. **Le « 5/5 » en dur de la carte Comment identifier (l.464) :** si l'utilisateur peut ajouter ou retirer des spécificités, le « 5/5 » pédagogique ne ment-il pas dès la première personnalisation ? Ne devrait-il pas dire « tous les critères » ?
7. **L'import sans version (l.2317) :** un fichier sans champ `version` passe sans alerte — la perte silencieuse de la checklist est-elle acceptable pour un format qu'on ne peut pas dater ? Ne faudrait-il pas traiter « version absente » comme « antérieure » ?
8. **Les role=button imbriqués (l.1359-1360, 1319-1326) :** l'ARIA interdit les interactifs dans un role=button. Faut-il faire de la spec-carte un `<article>` cliquable (avec le span Agrandir en vrai `<button>`) pour que les lecteurs d'écran annoncent correctement les deux actions ?
9. **Le graphique mensuel sans valeurs (l.2277-2280) :** un cueilleur qui veut savoir « combien j'ai récolté en septembre » doit-il toujours faire le calcul mental ? Un libellé au clic changerait-il la valeur du graphique ?
10. **Le verrouillage portrait (manifest l.10) :** en forêt, photographier un champignon au sol — le paysage ne serait-il pas plus naturel ? Le portrait est-il un choix de conception ou un héritage ?

---

*Rapport généré par lecture statique (Assessment A) — aucun fichier modifié. Correctifs de la 11e passe vérifiés dans le code et confirmés (nom latin 4.91:1, 🙈 liste, 3 micro-textes AA, image fiche focusable, title photo-zone dynamique, font-weight 700, carte Comment identifier) ; les problèmes ci-dessus sont des résidus de correctifs partiels ou des trous nouveaux.*
