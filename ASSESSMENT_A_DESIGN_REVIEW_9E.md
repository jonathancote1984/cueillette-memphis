# Assessment A — Critique design : Cueillette Québec — édition Memphis (9e passe)

**Fichier audité :** `index.html` (2369 lignes, HTML+CSS+JS mono-fichier) · `sw.js` (v30) · `manifest.json`
**Docs de référence :** `PRODUCT.md` (North Star « La Récolte », principes sécurité/terrain/privé/plaisir/zéro friction) · `DESIGN.md` (palette AUTOMNE/TERRE, Règle du Trait Noir, Règle du Rouge Mortel, Règle de l'Inclinaison, Règle du Décalage Net)
**Méthode :** lecture statique complète du source, vérification des 6 fixes de la 8e passe (commit `7143d28`), calculs WCAG exacts (script contrast-check.py), zéro modification de fichier.

---

## 1. Verdict de spécificité design

| Axe | Score | Preuve |
|---|---|---|
| **Conceptuel** | **~90 %** | Vocabulaire mycologique québécois exclusif : « volve en sac », « sporée rose », « anneau coulissant », « hyménium », « deliquescence », centre antipoison **1-800-463-5060** (index.html:1280, 2101), statuts Comestible/Prudence/Immangeable/Toxique/MORTEL ☠️, saisons de cueillette (morilles au printemps, chanterelles été-automne), métaphores de récolte (« coin secret », « panier », « carnet de chasse »). Aucun autre domaine ne parlerait de fausse morille ou de lépiote brunâtre. |
| **Visuel** | **~85 %** | Le Memphis est tenu avec une discipline rare : bordures noires 3 px sur toute surface colorée, coin cassé systématique (18 px/5 px, 12 px/4 px, 24 px/6 px), ombres dures sans flou (3-6 px), inclinaisons -1 à -2° (h1 -1,5°, pastilles -1,5°, puces actives -2°), zigzag sous le header et au-dessus de l'onglet actif, pois crème au fond (radial-gradient 28 px), vignettes à rayures ambre/blanc 45°, formes SVG flottantes (cercle pointillé, demi-lune, triangle). Un screenshot sans texte révélerait immédiatement un carnet ludique automnal. |

**Verdict :** interface hautement spécifique sur les deux axes — le langage Memphis n'est pas un habillage, c'est la grammaire du produit, et le vocabulaire de terrain est celui d'un mycologue québécois. Test du screenshot sans texte : réussi.

---

## 2. Évaluation holistique

### Hiérarchie visuelle
- Échelle typographique disciplinée : display 21 px/700 (h1, index.html:45), titre-vue 20 px/700 en pastille blanche cerclée (l.110-115), titre de feuille 18 px/700 en pastille ambre (l.293-295), corps 16 px/1.65, label 13 px/700, meta 12.5 px/600. Aucune taille arbitraire hors gabarit (les 15.5/14.5/13.5 px des boutons/cartes sont des variantes documentées).
- Les 4 cartes stats (l.2160-2165) sont volontairement inégales (jaune/bleu/vert/rose) — c'est un choix Memphis assumé, pas une erreur d'égalité de poids ; les libellés sont en 12 px/700 avec opacité gérée (l.306-307).
- Le compteur « n/5 » (l.1297) et la pastille badge header (l.54) utilisent `font-variant-numeric:tabular-nums` — les chiffres ne dansent pas pendant la coche. Détail de qualité.
- **Trou :** le verdict danger « ☠️ 5/5 critères vérifiés » est **codé en dur** (l.1306) alors que le compteur au-dessus est dynamique (`nbFaits + '/' + illu.items.length`, l.1297). Dès qu'un utilisateur retire une spécificité (feuille « 🎨 Illustrations IA », accessible pour toutes les espèces, l.1309), le verdict peut dire « 5/5 » pendant que le compteur dit « 4/4 » — deux vérités contradictoires sur le même écran, au pire endroit possible (verdict de sécurité).

### Architecture de l'information
- 5 onglets complets et stables (Spots/Identifier/Cueillettes/Stats/Paramètres, l.463-469) ; le détail guide est une 6e vue sans onglet, avec l'onglet Identifier maintenu actif (l.936) — bonne gestion de l'état de navigation.
- FAB contextuel : 📍 en Spots, ＋ ailleurs, masqué en Stats/détail/Paramètres (l.938-939) — cohérent.
- **Trou :** le FAB a un `aria-label` statique « Ajouter » (l.461) alors que son contenu et son action changent selon la vue (📍 ouvre la feuille spot, ＋ ouvre variété/cueillette). Un lecteur d'écran annonce « Ajouter » pour une action de géolocalisation.
- **Trou :** l'import (l.2211-2238) ne vérifie **jamais** `data.version` (l.2199 exporte `version: 5`). Un export v4 (sans checklist) ou un fichier d'une version future inconnue s'importe sans avertissement et écrase les données v5 — la checklist terrain (le cœur du produit) peut disparaître silencieusement.

### Adéquation émotionnelle
- Le North Star « La Récolte » est présent partout : header dégradé ambre/rouille avec formes flottantes, zigzag, rebonds élastiques des feuilles (cubic-bezier(.2,1.3,.4,1), l.281), appui enfoncé des boutons (translate 3 px + ombre réduite, l.154), toasts noirs cerclés d'ambre avec ombre rose (l.339-345).
- **Valence exemplaire :** le verdict ✅ vert est réservé aux comestibles/prudence avec texte nuancé (« restez prudent (cuisson obligatoire) », l.1304-1305) ; le verdict rouge « ☠️ 5/5 critères vérifiés — MORTELLE : ne pas consommer » (l.1306) encode le danger, pas la satisfaction de cocher. Le fix P1-1 de la 8e passe tient.
- **Valence défaillante :** le bouton « 🗑️ » de la liste guide (l.1266) est une corbeille qui promet la destruction, mais le clic ouvre « Masquer ou supprimer » (l.998-1007) — l'action par défaut est réversible. L'icône ment sur la gravité.
- Le « 📷 Réessayer » de l'écran d'identification (l.2090) appelle `identifierParPhoto(false)` — la galerie — même si la photo venait de l'appareil photo. Promesse de continuité, livraison d'un détour.

### Découvrabilité
- Excellente : bandeau clé Gemini avec bouton « Configurer la clé → » qui navigue ET focus le champ (l.2044-2047), alerte « Jamais exporté » (l.2194-2196), règle d'or en tête du guide (l.391), note « Touchez une espèce pour l'ajouter ou la retirer » (l.518), états vides qui pointent le FAB (« Appuyez sur le bouton rose… », l.1096, 1362).
- **Trou :** l'état vide du guide filtré (« Aucun champignon trouvé », l.1253) ne suggère pas de réinitialiser les filtres — l'utilisateur qui a combiné « Mortels » + « Hiver » sans résultat ne sait pas quoi défaire.

### Composition
- Colonne unique max 640 px, rythme 4/8/12/16/24 px respecté, cartes espacées de 16 px, grille2 pour les paires de boutons. Les feuilles bottom-sheet (max 84 vh, coins hauts 24 px, poignée avec hit-area étendue via `::after` inset -14 px, l.292) sont bien proportionnées.
- **Trou :** la fiche détail est un mur vertical : alerte + KV + description + caractéristiques + confusions + 5 cartes spécificités + 2 verdicts + 4 boutons (l.1316-1330). Sur un écran de 640 px de haut, le verdict (l'information la plus importante) est sous 3-4 écrans de scroll. La divulgation progressive s'arrête à la porte de la fiche.

### Typographie
- Fredoka 400-700 chargée (l.17), une seule famille, pas d'uppercase forcé, pas de césure. Hiérarchie par poids/taille conforme au DESIGN.md.
- **Trou :** `.spec-num` utilise `font-weight:900` (l.259) — hors des graisses chargées. Le navigateur synthétise ou arrondit : rendu variable selon la plateforme, exactement le pattern « font weight outside the loaded weights ».

### Couleur
- Palette tenue : les 8 couleurs du DESIGN.md + extensions documentées (rouge #B3261E, gris, bleu-canard, vert-mesure, rose-onglet, brun-tabac, fonds d'alertes, barre-vide). La Règle du Rouge Mortel est respectée (le rouge n'apparaît que MORTEL/suppression/compteur — le « Masquer » est en gris, l.1314).
- **Trou mineur :** `COULEURS_MOIS` (l.2148) est un tableau de hex en dur au lieu des variables CSS — les couleurs sont dans la palette, mais la dérive de tokenisation est amorcée.
- **Contrastes vérifiés (script WCAG exact) :** noir/olive **4.61:1** ✅ (verdict ✅), noir/ambre 7.59:1 ✅, blanc/rouge 6.07:1 ✅ (MORTEL), noir/C87224 4.79:1 ✅ (sous-titre header), blanc/terracotta 4.95:1 ✅, blanc/cuir 5.45:1 ✅, orange/blanc 4.67:1 ✅, rouille-onglet/blanc 4.66:1 ✅, noir/gris 6.08:1 ✅, noir/creme 14.08:1 ✅, noir/fond-alerte-rouge 13.34:1 ✅, noir/fond-alerte-orange 13.52:1 ✅, vert-mesure/blanc 4.97:1 ✅, bleu-canard/blanc 5.30:1 ✅, rose-onglet/blanc 5.46:1 ✅, brun-tabac/blanc 5.74:1 ✅. **Seul point sous AA :** le ✓ blanc sur olive à **3.44:1** (l.263) — acceptable comme icône graphique (seuil 3:1), à surveiller si on le considère comme du texte.

### Accessibilité
- Fixes 5e-8e passes confirmés : clavier Enter/Espace sur role=button (l.964-969), focus-visible ambre sur boutons/puces/items/FAB/onglets (l.190), aria-live toast (l.692), prefers-reduced-motion global (l.347-349), span « 🔍 Agrandir » avec role=button + stopPropagation (l.1300), cibles ≥44 px (btn-petit min-height:44, l.162).
- **Trous :**
  - Lightbox (l.2030-2037) : div dynamique sans `role="dialog"`, sans fermeture **Escape**, sans focus trap, sans aria-label. L'image agrandie est inaccessible au clavier.
  - Image de la fiche détail (l.1318) : `cursor:zoom-in` + onclick, mais pas de role/tabindex — le zoom promis par le curseur est inaccessible au clavier.
  - Boîte de confirmation (l.475-482) : `role="alertdialog" aria-modal="true"` mais **pas de focus trap** ni de fermeture Escape ; le focus initial sur « Annuler » (l.985) est bien vu, mais le focus peut s'échapper dans la page derrière.
  - Badge compteur header (l.373) : `title` seulement, pas d'aria-label — un lecteur d'écran annonce « 0 » sans contexte.
  - `alt="photo"` générique sur les photos de spot/cueillette (l.1059).
  - Bouton 🗑️ imbriqué dans un item `role="button"` (l.1259-1266) : imbrication interactive invalide (bouton dans un bouton-like), compensée par stopPropagation mais sémantiquement bancale.

### États
- Chargement : « Analyse en cours… (10-20 s) » avec sous-texte explicatif (l.2057) — mais **aucun bouton d'annulation** pendant l'analyse ; le seul échappatoire est le voile (non évident).
- Erreurs : `messageErreurIA` en français avec guidance par cause (clé/ réseau/ quota/ 500/ 404, l.1469-1479), catch identification photo inclus (l.2117-2121) — fix 7e passe confirmé.
- Vides : tous les états vides sont rédigés et orientent vers l'action (l.1096, 1253, 1362, 1955, 2150).
- **Trou :** le champ date de cueillette (l.541) accepte les dates futures — « Dernière sortie » (l.2164) peut afficher une sortie qui n'a pas encore eu lieu.

### Copy
- Français du Québec assumé, ton chaleureux et précis (« coin secret », « on ne mange pas », « goûter et cracher »). Les messages de sécurité sont non négociables et complets (centre antipoison systématique sur MORTEL).
- **Trous :** « 📷 Réessayer » (l.2090) rouvre la galerie ; le `title="Cliquez pour retirer la photo"` des photo-zones (l.521, 569, 626) est faux quand la zone est vide (cliquer ouvre la galerie) ; le bouton « 🗑️ » de la liste guide promet la suppression et livre un choix masquer/supprimer.

### Cas limites
- Réindexation des coches au retrait d'une spécificité (l.1987-2004) : `splice` sur `faits` — fix 6e passe confirmé.
- Checklist dans l'export v5 (l.2199) et vidée par « Tout effacer » (l.2243) — fixes confirmés.
- Saisons multi-mois : `saisonsDe` (l.1236-1239) couvre chanterelle (juillet-octobre → été+automne) et pleurote (décembre → hiver) — fix 7e passe confirmé.
- **Trou :** le verdict « 5/5 » en dur (l.1306) casse précisément dans le cas limite « retirer une spécificité d'une espèce mortelle » — le pire moment pour une incohérence.
- **Trou :** badge de sécurité des cueillettes dépendant de l'orthographe exacte (`infoEspece` matche par nom normalisé exact, l.924-928 ; fallback `especeId` seulement si l'espèce a été choisie via l'autocomplétion, l.1368). Une cueillette « amanite phaloide » (faute) n'a **aucun badge rouge** dans le journal.

---

## 3. Évaluation de charge cognitive (8 items)

| # | Item | Verdict | Preuve |
|---|---|---|---|
| 1 | Focus unique (une tâche par écran) | ❌ | La fiche détail mélange 3 tâches : identifier (checklist), décider (verdicts), gérer (boutons IA/modifier/masquer) — l.1316-1330. |
| 2 | Chunking ≤ 4 | ❌ | 5 spécificités par fiche (chunking métier justifié mais > 4), 10 puces de filtres (5 statuts + 5 saisons, l.1223-1224), 4 cartes stats + 3 tops + 1 graphique. |
| 3 | Regroupement visuel | ✅ | Cartes, sections balisées par `guide-sujet` (l.329), grille2, séparation des rangées de puces. |
| 4 | Hiérarchie | ✅ | 6 niveaux cohérents (21/20/18/16/13/12.5 px), poids 400-700, tabular-nums sur les compteurs. |
| 5 | Une chose à la fois | ❌ | La fiche détail déverse tout d'un coup ; le verdict (décision critique) est sous 3-4 écrans de scroll. |
| 6 | Choix minimaux ≤ 4 | ❌ | 10 puces de filtres, 5 options météo, 4 options statut + checkbox prudence. |
| 7 | Mémoire de travail | ❌ | Le verdict « 5/5 » en dur vs compteur dynamique force l'utilisateur à recalculer ; le badge de sécurité absent sur les noms mal orthographiés exige de se souvenir du statut réel. |
| 8 | Divulgation progressive | ⚠️ | Excellente aux portes (liste compacte, feuilles bottom-sheet, checklist sur demande) mais la fiche détail est un mur. |

**Total : 3 ✅ / 5 ❌** (dont 1 ⚠️ compté ❌) — la charge est maîtrisée à la navigation, mais la fiche détail et les filtres dépassent les seuils.

---

## 4. Voyage émotionnel (peak-end)

- **Entrée (pic) :** header dégradé ambre/rouille, zigzag noir, formes flottantes, h1 incliné avec text-shadow rose, animation `pop` élastique (l.108-109). L'app salue comme un carnet de chasse qu'on ouvre.
- **Milieu :** cocher une spécificité est gratifiant (carte qui bascule olive + barré + compteur tabular qui avance, l.1342-1356). Les feuilles rebondissent. **Vallées :** l'analyse IA 10-20 s sans annulation (l.2057) ; le « Réessayer » qui rouvre la galerie (l.2090) ; le toast à 2,2 s (l.725) un peu court pour les messages d'erreur IA longs.
- **Fin de journée (pic) :** le badge rouge du header qui monte, les stats colorées (4 cartes + tops + barres mensuelles), « Dernière sortie » — le panier se remplit visuellement.
- **Faux pics :** aucun — le verdict ✅ vert est nuancé pour les prudence, le rouge MORTEL est sans ambiguïté, l'alerte « Jamais exporté » est honnête.
- **Rassurance :** double confirmation sur destruction (l.1034-1035, 2240-2241), garde-fou de saisie variété (l.1526-1530), centre antipoison sur chaque alerte MORTEL. Le moment le plus anxiogène du produit (identifier un champignon douteux) est le mieux accompagné.

---

## 5. Heuristiques de Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 4 | Toasts, compteur n/5, verdicts, bandeau clé, alerte export — tout est vivant. Toast 2,2 s un peu court. |
| 2 | Correspondance système-monde réel | 4 | Vocabulaire mycologique québécois exact, emojis météo, « coin secret », centre antipoison. |
| 3 | Contrôle et liberté | 4 | Annuler partout, garde-fou variété, restauration sélective, double confirmation. |
| 4 | Cohérence et standards | 3 | Système très tenu (helpers unifiés, tokens), mais verdict « 5/5 » en dur vs compteur dynamique, et « Réessayer » ≠ appareil. |
| 5 | Prévention des erreurs | 3 | Double confirmation, fail-safe IA, validation nom — mais badge de sécurité orthographe-dépendant et date future acceptée. |
| 6 | Reconnaissance plutôt que mémorisation | 3 | Filtres visibles, autocomplétion, mais 10 puces + FAB contextuel sans libellé dynamique. |
| 7 | Flexibilité et efficacité | 3 | FAB contextuel, partage Web Share, GPS — mais pas de tri/recherche dans le journal, pas de raccourcis. |
| 8 | Esthétique minimaliste | 3 | Memphis dense et assumé, mais fiche détail en mur et 10 puces de filtres. |
| 9 | Aide à la reconnaissance des erreurs | 4 | messageErreurIA français avec guidance par cause, toasts, états vides orientés. |
| 10 | Documentation et aide | 3 | Bandeau clé, note export, règle d'or — mais pas d'aide dans la fiche (que signifie le verdict ?) ni d'onboarding. |

**Total : 34/40** — profil : très fort sur la sécurité émotionnelle et le langage de domaine ; pénalisé par deux incohérences de vérité (verdict 5/5 en dur, badge orthographe-dépendant) et la densité de la fiche détail.

---

## 6. Forces spécifiques (2-3)

1. **Le système de verdict de la checklist terrain est un modèle de valence de sécurité.** ⚠️ ambre par défaut avec « Rien n'est encore vérifié » à 0 critère ET après décoche totale (l.1307, `nbFaits < illu.items.length` couvre 0) ; ✅ vert réservé comestibles/prudence avec nuance « restez prudent » (l.1304-1305) ; ☠️ rouge « MORTELLE : ne pas consommer » pour les non-comestibles (l.1306). La satisfaction de cocher n'écrase jamais le danger réel — c'est exactement l'inverse du pattern « positive-valence verdict on danger items ».
2. **La boucle de comparaison est pensée comme un parcours, pas comme une navigation.** Scroll mémorisé (`positionGuide`, l.1274, restauré en rAF l.1340), nom d'espèce dans le sous-titre du header + badge masqué (l.1332-1333), bouton ← sticky 44 px (l.56-63, 374, 940), onglet Identifier maintenu actif (l.936). Comparer une récolte douteuse avec l'amanite phalloïde puis la galerine se fait sans perdre sa place — le geste le plus important du produit est le plus fluide.
3. **La discipline du système Memphis est totale, jusque dans les micro-détails.** Poignée de feuille avec hit-area étendu (l.292), tabular-nums sur tous les compteurs dynamiques, appui scale(.96) des cartes spécificités (l.256), sortie de feuille sans rebond (ease-out, l.286), outlines 1 px noir 10 % sur les images (l.141, 258, 333), text-wrap:balance sur les titres. Le DESIGN.md n'est pas un vœu pieux : chaque règle nommée (Trait Noir, Rouge Mortel, Inclinaison, Décalage Net) est exécutée dans le code.

---

## 7. Problèmes prioritaires (3-5)

### P1-1 — Verdict danger « ☠️ 5/5 critères vérifiés » codé en dur
- **Preuve :** index.html:1306 (`'<div class="t">☠️ 5/5 critères vérifiés</div>'`) vs compteur dynamique l.1297 (`nbFaits + '/' + illu.items.length`).
- **Pourquoi c'est grave :** la feuille « 🎨 Illustrations IA » (l.1309) est accessible pour **toutes** les espèces, y compris les mortelles, et `retirerIllu` (l.1987-2004) supprime des critères. Une amanite phalloïde réduite à 4 critères affichera « ☠️ 5/5 critères vérifiés » à 4/4 — le verdict de sécurité ment, en contradiction avec le compteur à 20 px au-dessus. C'est le pire endroit possible pour une incohérence de vérité.
- **Fix :** interpoler `'☠️ ' + illu.items.length + '/' + illu.items.length + ' critères vérifiés'` (et idem pour le libellé ✅ si le nombre change).

### P1-2 — Le badge de sécurité du journal dépend de l'orthographe exacte
- **Preuve :** `infoEspece` matche par nom normalisé **exact** (l.924-928) ; le fallback `especeId` (l.1368) ne couvre que les cueillettes saisies via l'autocomplétion. Une saisie libre « amanite phaloide » ou « amanite phalloid » → `statutEff = null` → **aucun badge rouge** sur la ligne de journal la plus dangereuse du carnet.
- **Pourquoi c'est grave :** en forêt, une main, doigts mouillés, l'utilisateur tape vite. La promesse produit (« badge de sécurité conservé même si l'espèce est supprimée », l.1367) est trahie par une faute de frappe — et le journal est relu à la maison, loin du champignon.
- **Fix :** à la saisie, si le nom libre ressemble (distance de Levenshtein / inclusion) à une espèce toxique/mortelle du guide, afficher une alerte « ⚠️ Voulez-vous dire « Amanite phalloïde » (MORTEL) ? » ; à défaut, matcher flou dans `infoEspece` pour l'affichage du badge.

### P2-1 — Lightbox sans accessibilité ni clavier
- **Preuve :** l.2030-2037 : div dynamique, `cursor:zoom-out`, fermeture au clic uniquement. Pas de `role="dialog"`, pas d'Escape, pas de focus trap, pas d'aria-label.
- **Pourquoi :** la PWA prétend « se comporter comme une app native » (DESIGN.md) et l'image agrandie est un outil d'identification critique (comparer des lames fines). Un utilisateur clavier ne peut ni l'ouvrir (image détail, l.1318, sans role/tabindex) ni la fermer.
- **Fix :** `role="dialog" aria-modal="true" aria-label="Photo agrandie"`, fermeture sur Escape, focus initial dans la lightbox, retour de focus à l'élément déclencheur.

### P2-2 — La fiche détail est un mur : le verdict est sous 3-4 écrans de scroll
- **Preuve :** l.1316-1330 : alerte + KV + description + caractéristiques + confusions + 5 cartes spécificités + 2 verdicts + 4 boutons, dans une seule carte.
- **Pourquoi :** l'information de décision (verdict ⚠️/✅/☠️) arrive après tout le reste. En forêt, l'utilisateur coche les 5 critères en bas de page et doit remonter pour voir le verdict changer — ou ne le voit jamais.
- **Fix :** verdict collant en bas de la fiche (sticky au-dessus de la barre d'onglets) ou sommaire ancré ; à défaut, déplacer le verdict juste sous l'alerte de sécurité, avant la description.

### P2-3 — Boîte de confirmation `aria-modal` sans focus trap ni Escape
- **Preuve :** l.475-482 (`role="alertdialog" aria-modal="true"`) ; le focus initial sur « Annuler » (l.985) est bon, mais Tab peut sortir dans la page derrière le voile.
- **Fix :** focus trap minimal (boucler Tab entre les deux boutons) + Escape = Annuler.

### P3 — Pile de polissage
- `.spec-num` `font-weight:900` (l.259) hors des graisses chargées (400-700, l.17) — rendu synthétisé variable.
- `COULEURS_MOIS` en dur (l.2148) au lieu des variables CSS.
- FAB `aria-label` statique « Ajouter » (l.461) alors que l'icône devient 📍.
- Badge header : `title` seulement, pas d'aria-label (l.373).
- `title="Cliquez pour retirer la photo"` faux quand la zone est vide (l.521, 569, 626).
- « 📷 Réessayer » rouvre la galerie, pas l'appareil (l.2090).
- Import sans vérification de `data.version` (l.2215).
- Champ date acceptant le futur (l.541).
- `alt="photo"` générique (l.1059).
- Bouton 🗑️ dans un item `role="button"` (l.1259-1266).
- Graphique mensuel sans valeurs affichées (l.2182-2185).
- État vide du guide filtré sans suggestion de réinitialisation (l.1253).

---

## 8. Red flags par persona

### Power user — Jonathan à la maison (stats, export/import, variétés perso)
- **Ce qui marche :** stats complètes, export v5 avec checklist, restauration sélective, feuille variété avec garde-fou.
- **Red flag :** l'import écrase tout sans vérifier la version (l.2215) — importer un vieux export v4 fait disparaître la checklist silencieusement, et le toast dit « Import réussi ✅ ».
- **Pire moment :** restaurer un fichier de l'an dernier et découvrir des semaines plus tard que toutes ses vérifications terrain ont été avalées.

### Utilisateur à accessibilité réduite (clavier, lecteur d'écran)
- **Ce qui marche :** clavier Enter/Espace sur tous les role=button, focus-visible ambre, aria-live toast, contrastes AA vérifiés.
- **Red flags :** lightbox et image zoom inaccessibles au clavier (l.2030-2037, l.1318) ; boîte de confirmation sans focus trap (l.475-482) ; badge compteur annoncé « 0 » sans contexte (l.373) ; FAB annoncé « Ajouter » pour une action 📍 (l.461).
- **Pire moment :** agrandir la photo d'une amanite phalloïde pour vérifier la volve, et ne pouvoir ni l'ouvrir ni la fermer au clavier.

### Mobile distrait — en forêt, une main, sans réseau
- **Ce qui marche :** 100 % hors-ligne (SW v30, credits.json inclus), cibles ≥44 px, autocomplétion, puces à bascule, verdicts lisibles au soleil (puces saison noir/crème, l.174).
- **Red flags :** badge de sécurité orthographe-dépendant (l.924-928) — une faute de frappe sur une espèce mortelle = journal sans alerte ; l'analyse IA 10-20 s sans annulation (l.2057) ; le verdict sous 3-4 écrans de scroll dans la fiche (l.1316-1330).
- **Pire moment :** noter « amanite phaloide » d'une main mouillée, voir la cueillette s'enregistrer sans aucun rouge, et relire ce journal à la maison.

---

## 9. Observations mineures

- `.spec-num` font-weight:900 hors graisses chargées (l.259 vs l.17).
- `COULEURS_MOIS` en dur (l.2148) — dérive de tokens amorcée.
- `title="Cliquez pour retirer la photo"` trompeur quand la zone est vide (l.521, 569, 626).
- FAB aria-label statique « Ajouter » alors que l'icône devient 📍 (l.461).
- Badge header : title seulement, pas d'aria-label (l.373).
- `alt="photo"` générique sur les photos utilisateur (l.1059).
- Bouton 🗑️ de la liste guide : la corbeille promet la suppression, le clic ouvre « Masquer ou supprimer » (l.1266 vs l.998-1007).
- ✓ blanc sur olive à 3.44:1 : sous AA pour du texte, OK comme icône graphique (3:1) — à trancher.
- Graphique mensuel sans valeurs en kg (l.2182-2185).
- Import sans vérification de `data.version` (l.2215).
- Champ date de cueillette accepte le futur (l.541).
- « 📷 Réessayer » rouvre la galerie, pas l'appareil (l.2090).
- État vide du guide filtré sans suggestion de réinitialisation (l.1253).
- Sous-titre header en détail = nom d'espèce : peut être long et pousser le bouton retour sur petit écran (l.1332).
- Le select météo natif est le seul contrôle « système » visible — acceptable (documenté), mais casse légèrement l'illusion native.
- Le toast à 2,2 s (l.725) est court pour les messages d'erreur IA longs.

---

## 10. Questions provocatrices

1. Le verdict « ☠️ 5/5 critères vérifiés » est codé en dur (l.1306) : quand un utilisateur retire une spécificité d'une amanite phalloïde, le compteur dira 4/4 et le verdict 5/5 — lequel doit-on croire, et pourquoi le produit autorise-t-il deux vérités sur un verdict de sécurité ?
2. Une cueillette « amanite phaloide » (faute de frappe) s'enregistre sans aucun badge rouge : le carnet doit-il **exiger** la sélection d'une espèce connue pour les statuts dangereux, ou accepter le nom libre sans alerte — et qui assume la responsabilité ?
3. La fiche détail est un mur de 4 sections + 5 cartes + 2 verdicts + 4 boutons : faut-il un verdict sticky au-dessus de la barre d'onglets, un sommaire ancré, ou des sections repliables — sachant que le verdict est la seule information qui décide de manger ou pas ?
4. Le FAB change d'icône (📍/＋) mais son aria-label reste « Ajouter » : l'action contextuelle est-elle assez claire pour un utilisateur d'écran, ou faut-il un libellé dynamique (« Ajouter un spot » / « Nouvelle variété ») ?
5. L'import écrase tout sans vérifier `data.version` : faut-il un avertissement « fichier d'une version antérieure — la checklist sera perdue » quand version < 5, ou refuser l'import ?
6. La lightbox n'a ni Escape ni role=dialog : une PWA qui prétend « zéro boîte système, comportement natif » peut-elle se permettre un composant d'identification critique inaccessible au clavier ?
7. Le graphique mensuel montre des barres sans valeurs : un carnet de récolte a-t-il besoin de lire « 2,4 kg en septembre », ou la hauteur relative suffit-elle pour un usage personnel ?
8. Le « 📷 Réessayer » rouvre la galerie : l'utilisateur qui vient de photographier un champignon douteux en forêt doit-il repasser par l'appareil photo, ou « Réessayer » devrait-il répéter la dernière source ?
9. Les 10 puces de filtres (5 statuts + 5 saisons) : est-ce le bon équilibre pour une main en forêt, ou faut-il un menu dépliable « Filtres » qui ne montre que la combinaison active ?
10. Le badge compteur rouge du header n'a pas d'aria-label : un lecteur d'écran annonce « 0 » sans contexte — faut-il « 0 cueillettes », ou le badge est-il purement décoratif et devrait être `aria-hidden` ?
11. Le ✓ blanc sur olive à 3.44:1 : la coche de satisfaction est-elle un composant graphique (3:1 suffit) ou du texte (4.5:1 requis) — et la réponse change-t-elle le design de la case cochée ?
12. Le bouton 🗑️ de la liste guide ouvre « Masquer ou supprimer » : la corbeille promet la destruction, l'action par défaut est réversible — faut-il une icône neutre (⋯) pour le masquage, et réserver la corbeille à la vraie suppression ?

---

## Vérification des fixes des passes 4-8 (tous confirmés)

| Fix annoncé | Preuve | Statut |
|---|---|---|
| Verdict ⚠️ à 0 critère ET après décoche totale | l.1307 `nbFaits < illu.items.length` couvre 0 | ✅ |
| Verdict ✅ vert réservé comestibles/prudence, ☠️ rouge mortelles | l.1304-1306 | ✅ |
| Variables CSS --ambre/--olive/--cuir | l.19-24 | ✅ |
| a11y clavier Enter/Espace role=button | l.964-969 | ✅ |
| focus-visible ambre | l.190 | ✅ |
| Contrastes (olive 4.61:1, sous-titre 4.79:1, coche 3.44:1 graphique) | script WCAG | ✅ |
| Autocomplétion espèce (input + suggestions, valeur libre) | l.1384-1403 | ✅ |
| Checklist dans export/import v5 | l.2199, 2220, 2224, 2231 | ✅ |
| « Tout effacer » vide la checklist | l.2243 | ✅ |
| Réindexation des coches au retrait d'une spécificité | l.1991-1995 | ✅ |
| Filtres sécurité (Prudence + Ne pas manger = toxiques+immangeables) | l.1243-1247 | ✅ |
| Erreurs IA françaises avec guidance + catch idphoto | l.1469-1479, 2117-2121 | ✅ |
| Bouton ← sticky + nom espèce header + badge masqué | l.56-63, 374, 940, 1332-1333 | ✅ |
| Puces saison actives fond noir/crème | l.174 | ✅ |
| credits.json dans le cache SW | sw.js:138-139 | ✅ |
| Span « 🔍 Agrandir » cliquable (role=button, stopPropagation) | l.1300 | ✅ |
| Position de scroll mémorisée au retour de fiche | l.1274, 1340 | ✅ |
| Helpers unifiés (appelGemini/lierPhoto/topRangs/fermerFeuilleVariete/saisonsDe/recharger Promise.all) | l.1481, 1063, 2149, 1526, 1236, 2326 | ✅ |

**Score : 34/40** (stable vs 34,5/40 à la 8e passe — les 6 fixes tiennent tous ; la légère baisse vient de deux trous de vérité nouvellement caractérisés : verdict « 5/5 » en dur P1-1 et badge de sécurité orthographe-dépendant P1-2, qui étaient présents mais non signalés).
