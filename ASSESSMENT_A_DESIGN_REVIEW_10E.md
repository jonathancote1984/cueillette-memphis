# Assessment A — Critique design : Cueillette Québec — édition Memphis (10e passe)

**Fichier audité :** `index.html` (2415 lignes, HTML+CSS+JS mono-fichier) · `sw.js` (v31, cache `cqm-v31`) · `manifest.json`
**Docs de référence :** `PRODUCT.md` (North Star « La Récolte », principes sécurité/terrain/privé/plaisir/zéro friction) · `DESIGN.md` (palette AUTOMNE/TERRE, Règle du Trait Noir, Règle du Rouge Mortel, Règle de l'Inclinaison, Règle du Décalage Net)
**Méthode :** lecture statique complète du source, vérification des 5 fixes de la 9e passe (commit `fc1021d`), calculs WCAG exacts (script Python), zéro modification de fichier. Aucun outil navigateur utilisé (Assessment A).

---

## 1. Verdict de spécificité design

| Axe | Score | Preuve |
|---|---|---|
| **Conceptuel** | **~90 %** | Vocabulaire mycologique québécois exclusif : « volve en sac », « sporée rose », « anneau coulissant », « hyménium », « deliquescence », centre antipoison **1-800-463-5060** (index.html:1318, 2147), statuts Comestible/Prudence/Immangeable/Toxique/MORTEL ☠️, saisons de cueillette (morilles au printemps, chanterelles été-automne), métaphores de récolte (« coin secret », « panier », « carnet de chasse »). Les fiches parlent d'aiguillons, de réseau blanc, de bleuissement à la coupe — aucun autre domaine ne dirait « toute amanite entièrement blanche doit être évitée ». |
| **Visuel** | **~85 %** | Le Memphis est tenu avec une discipline rare : bordures noires 3 px sur toute surface colorée, coin cassé systématique (18 px/5 px cartes, 12 px/4 px champs, 24 px/6 px feuilles), ombres dures sans flou (3-6 px), inclinaisons -1 à -2° (h1 -1,5°, pastilles -1,5°, puces actives -2°), zigzag sous le header et au-dessus de l'onglet actif, pois crème au fond (radial-gradient 28 px), vignettes à rayures ambre/blanc 45°, formes SVG flottantes (cercle pointillé, demi-lune, triangle). Un screenshot sans texte révélerait immédiatement un carnet ludique automnal, pas un dashboard. |

**Verdict :** interface hautement spécifique sur les deux axes — le Memphis n'est pas un habillage, c'est la grammaire du produit ; le vocabulaire est celui d'un mycologue québécois. Test du screenshot sans texte : réussi.

---

## 2. Évaluation holistique

### Hiérarchie visuelle
- Échelle typographique disciplinée : display 21 px/700 (h1, l.45), titre-vue 20 px/700 en pastille blanche cerclée (l.110-115), titre de feuille 18 px/700 en pastille ambre (l.293-295), corps 16 px/1.65, label 13 px/700, meta 12.5 px/600. Aucune taille arbitraire hors gabarit.
- Les 4 cartes stats volontairement inégales (jaune/bleu/vert/rose, l.298-304) : choix Memphis assumé, libellés 12 px/700 avec opacité gérée (l.306-307).
- Compteurs vivants en `font-variant-numeric:tabular-nums` (badge header l.54, spec-compteur l.274) — les chiffres ne dansent pas pendant la coche.
- **Le point faible historique est corrigé :** le verdict danger est maintenant **dynamique** (`'☠️ ' + nbFaits + '/' + illu.items.length + ' critères vérifiés'`, l.1344) — plus de « 5/5 » en dur face à un compteur « 4/4 ». La vérité est unique. Fix P1-1 de la 9e passe **confirmé**.

### Architecture de l'information
- 5 onglets complets et stables (Spots/Identifier/Cueillettes/Stats/Paramètres, l.463-469) ; le détail guide est une 6e vue sans onglet, onglet Identifier maintenu actif (l.952) — bonne gestion d'état.
- FAB contextuel : 📍 en Spots, ＋ ailleurs, masqué en Stats/détail/Paramètres (l.953-955) — cohérent.
- **Trou :** le FAB a un `aria-label` statique « Ajouter » (l.461) alors que son contenu et son action changent selon la vue — un lecteur d'écran annonce « Ajouter » pour une action de géolocalisation.
- **Trou :** l'import (l.2257-2284) ne vérifie **jamais** `data.version` (l'export écrit `version: 5`, l.2245). Un export v4 (sans checklist) s'importe sans avertissement, vide la checklist et affiche « Import réussi ✅ » — la perte est silencieuse.

### Adéquation émotionnelle
- Le North Star « La Récolte » est présent partout : header dégradé ambre/rouille avec formes flottantes, zigzag, rebonds élastiques des feuilles (cubic-bezier(.2,1.3,.4,1), l.281), appui enfoncé des boutons (translate 3 px + ombre réduite, l.154), toasts noirs cerclés d'ambre avec ombre rose (l.339-345).
- **Valence exemplaire :** verdict ✅ vert réservé comestibles/prudence avec nuance (« restez prudent (cuisson obligatoire) », l.1343) ; verdict ☠️ rouge dynamique « MORTELLE : ne pas consommer » (l.1344). La satisfaction de cocher n'écrase jamais le danger.
- **Valence défaillante :** le bouton « 🗑️ » de la liste guide (l.1304) ouvre « Masquer ou supprimer » (l.1036-1045) — la corbeille promet la destruction, l'action par défaut est réversible. L'icône ment sur la gravité.
- Le « 📷 Réessayer » (l.2136) appelle `identifierParPhoto(false)` — la galerie — même si la photo venait de l'appareil. Promesse de continuité, livraison d'un détour.

### Découvrabilité
- Excellente : bandeau clé Gemini avec bouton qui navigue ET focus le champ (l.2090-2093), alerte « Jamais exporté » (l.2235-2242), règle d'or en tête du guide (l.391), note « Touchez une espèce pour l'ajouter ou la retirer » (l.518), états vides qui pointent le FAB (l.1134, 1400).
- **Trou :** l'état vide du guide filtré « Aucun champignon trouvé » (l.1291) ne suggère pas de réinitialiser les filtres — un utilisateur qui a combiné « Mortels » + « Hiver » sans résultat ne sait pas quoi défaire.

### Composition
- Colonne unique max 640 px, rythme 4/8/12/16/24 px respecté, cartes espacées 16 px, grille2 pour les paires. Feuilles bottom-sheet bien proportionnées (max 84 vh, coins hauts 24 px, poignée avec hit-area étendue via `::after` inset -14 px, l.292).
- **Amélioration majeure :** la galerie + les verdicts sont maintenant placés **juste sous l'alerte de sécurité** (l.1360-1361 : `avis` puis `galerie`), avant la description — la décision est visible sans scroller. Fix P2-2 de la 9e passe **confirmé**. Le mur persiste toutefois : la même carte enchaîne ensuite KV saison/habitat, description, caractéristiques, confusions et 4 boutons.

### Typographie
- Fredoka 400-700 chargée (l.17), une seule famille, pas d'uppercase forcé, pas de césure. Hiérarchie par poids/taille conforme au DESIGN.md.
- **Trou :** `.spec-num` utilise `font-weight:900` (l.259) — hors des graisses chargées (400-700). Le navigateur synthétise : rendu variable selon la plateforme.

### Couleur
- Palette tenue : les 8 couleurs du DESIGN.md + extensions documentées (rouge, gris, bleu-canard, vert-mesure, rose-onglet, brun-tabac, fonds d'alertes, barre-vide). La Règle du Rouge Mortel est respectée (rouge = MORTEL/suppression/compteur ; « Masquer » est en gris, l.1352).
- **Trou mineur :** `COULEURS_MOIS` (l.2194) est un tableau de hex en dur au lieu des variables CSS — dérive de tokenisation amorcée.
- **Contrastes recalculés (script exact) :** noir/olive **4.61:1** ✅, noir/ambre 7.59:1 ✅, blanc/rouge 6.07:1 ✅, blanc/orange 4.67:1 ✅, noir/creme 14.08:1 ✅ (puces saison actives, fix 7e passe), blanc/cuir 5.45:1 ✅, blanc/terracotta 4.95:1 ✅, noir/#C87224 4.79:1 ✅ (sous-titre header), noir/fond-alerte-rouge 13.34:1 ✅, blanc/bleu-canard 5.30:1 ✅, noir/gris 6.08:1 ✅. **Seul point sous AA :** le ✓ blanc sur olive à **3.44:1** (l.263) — acceptable comme icône graphique (seuil 3:1), à trancher si on le considère comme du texte.

### Accessibilité
- Fixes 5e-9e passes **confirmés** : clavier Enter/Espace sur role=button (l.980-985), focus-visible ambre (l.190), aria-live toast (l.692), prefers-reduced-motion (l.347-349), cibles ≥44 px (l.162, 166), span « 🔍 Agrandir » role=button + stopPropagation (l.1338), **lightbox** role=dialog + aria-modal + aria-label + tabIndex=-1 + Escape + focus initial (l.2068-2083), **focus trap + Escape sur modales confirm/choix** (l.1011-1032).
- **Trous restants :**
  - Lightbox : le focus n'est **pas restauré** à l'élément déclencheur à la fermeture (`fermer()` fait `anc.remove()` sans mémoriser `document.activeElement`, l.2077-2082) — le focus retombe sur `<body>`.
  - Boîte de choix (masquer/supprimer, l.485-491) : `role="dialog" aria-modal` mais **pas de focus initial** — le focus reste sur le bouton 🗑️ de la liste, derrière le voile.
  - Badge compteur header : `title` seulement, pas d'aria-label (l.373) — un lecteur d'écran annonce « 0 » sans contexte.
  - `alt="photo"` générique sur les photos utilisateur (l.1097).
  - Bouton 🗑️ imbriqué dans un item `role="button"` (l.1304) : imbrication interactive invalide, compensée par stopPropagation.

### États
- Chargement : « Analyse en cours… (10-20 s) » avec sous-texte explicatif (l.2103).
- **Trou nouveau (P2) :** pendant l'analyse IA, **aucun bouton d'annulation** (pas d'AbortController sur le fetch, l.1525) et, si l'utilisateur ferme la feuille via la poignée ou le voile pendant les 10-20 s, le résultat est réécrit dans une feuille **fermée** (l.2140-2162 : `innerHTML` seul, sans réouverture) — l'analyse aboutit mais devient invisible, sans toast.
- Erreurs : `messageErreurIA` français avec guidance par cause (l.1507-1517), catch identification photo inclus (l.2163-2167) — fix 7e passe confirmé.
- Vides : tous les états vides sont rédigés et orientent vers l'action (l.1134, 1291, 1400, 1993, 2355).
- **Trou :** le champ date de cueillette (l.541) accepte les dates futures — « Dernière sortie » (l.2210) peut afficher une sortie qui n'a pas encore eu lieu.

### Copy
- Français du Québec assumé, ton chaleureux et précis (« coin secret », « on ne mange pas », « goûter et cracher »). Messages de sécurité non négociables et complets (centre antipoison systématique sur MORTEL).
- **Trous :** « 📷 Réessayer » rouvre la galerie (l.2136) ; le `title="Cliquez pour retirer la photo"` des photo-zones (l.521, 569, 626) est faux quand la zone est vide (cliquer ouvre la galerie) ; le bouton « 🗑️ » de la liste guide promet la suppression et livre un choix.

### Cas limites
- Réindexation des coches au retrait d'une spécificité : `splice` sur `faits` (l.2029-2033) — fix 6e passe confirmé.
- Checklist dans l'export v5 (l.2245) et vidée par « Tout effacer » (l.2289) — fixes confirmés.
- Saisons multi-mois : `saisonsDe` (l.1274-1277) couvre chanterelle (été+automne) et pleurote (hiver) — fix 7e passe confirmé.
- **Trou nouveau (P1) :** le matche flou Levenshtein ≤ 2 (l.936-942) couvre les **fautes de frappe** mais pas les **synonymes vernaculaires** : une cueillette notée « fausse morille » ou « ange destructeur » (noms vernaculaires québécois réels, littéralement présents dans les noms du guide : « Gyromitre (fausse morille) » l.887, « Amanite vireuse (ange destructeur) » l.877) ne matche ni exactement ni par distance (différence de longueur ≥ 13) → `statutEff = null` → **aucun badge rouge** dans le journal pour des espèces MORTELLES. Le fix de la 9e passe tient pour l'orthographe, mais le vocabulaire de terrain reste un angle mort.

---

## 3. Évaluation de charge cognitive (8 items)

| # | Item | Verdict | Preuve |
|---|---|---|---|
| 1 | Focus unique (une tâche par écran) | ❌ | La fiche détail mélange identifier (checklist), décider (verdicts) et gérer (boutons IA/modifier/masquer) — l.1354-1368. |
| 2 | Chunking ≤ 4 | ❌ | 5 spécificités par fiche (justifié métier), 10 puces de filtres (5 statuts + 5 saisons, l.1260-1269), 4 cartes stats + 3 tops + 1 graphique. |
| 3 | Regroupement visuel | ✅ | Cartes, sections balisées par `guide-sujet` (l.329), grille2, séparation des rangées de puces. |
| 4 | Hiérarchie | ✅ | 6 niveaux cohérents (21/20/18/16/13/12.5 px), poids 400-700, tabular-nums sur les compteurs. |
| 5 | Une chose à la fois | ❌ | La fiche détail déverse tout d'un coup ; améliorée (verdicts montés sous l'alerte) mais le bloc reste : alerte + 5 cartes + KV + description + caractéristiques + confusions + 4 boutons dans une carte. |
| 6 | Choix minimaux ≤ 4 | ❌ | 10 puces de filtres, 5 options météo, 4 options statut + checkbox prudence. |
| 7 | Mémoire de travail | ❌ | Le verdict est maintenant cohérent (dynamique), mais le badge du journal dépend de la reconnaissance lexicale : « fausse morille » s'affiche sans rouge et l'utilisateur doit se souvenir du statut réel. |
| 8 | Divulgation progressive | ⚠️ | Excellente aux portes (liste compacte, feuilles bottom-sheet, checklist sur demande) ; la décision est montée en haut de fiche (progrès), mais le contenu encyclopédique reste déversé d'un bloc. |

**Total : 3 ✅ / 5 ❌** (dont 1 ⚠️ compté ❌) — même compte que la 9e passe, mais le point 7 a changé de nature : la cohérence interne du verdict est réparée, c'est la couverture lexicale qui charge la mémoire.

---

## 4. Voyage émotionnel (peak-end)

- **Entrée (pic) :** header dégradé ambre/rouille, zigzag noir, formes flottantes, h1 incliné avec text-shadow rose, animation `pop` élastique (l.108-109). L'app salue comme un carnet de chasse qu'on ouvre.
- **Milieu :** cocher une spécificité est gratifiant (carte qui bascule olive + barré + compteur tabular qui avance, l.1380-1394). Les feuilles rebondissent. **Vallées :** l'analyse IA 10-20 s sans annulation et sans récupération si la feuille est fermée (l.2103, 2140-2162) ; le « Réessayer » qui rouvre la galerie (l.2136) ; le toast à 2,2 s (l.725) court pour les messages d'erreur IA longs.
- **Fin de journée (pic) :** le badge rouge du header qui monte, les stats colorées (4 cartes + tops + barres mensuelles), « Dernière sortie » — le panier se remplit visuellement.
- **Faux pics :** aucun — le verdict ✅ vert est nuancé pour les prudence, le rouge MORTEL est sans ambiguïté, l'alerte « Jamais exporté » est honnête.
- **Rassurance :** double confirmation sur destruction (l.1072-1073, 2286-2287), garde-fou de saisie variété (l.1560-1568), centre antipoison sur chaque alerte MORTEL. Le moment le plus anxiogène du produit (identifier un champignon douteux) est le mieux accompagné.

---

## 5. Heuristiques de Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 4 | Toasts, compteur n/n dynamique, verdicts sous l'alerte, bandeau clé, alerte export — tout est vivant. Pénalisé par l'analyse IA sans état d'annulation. |
| 2 | Correspondance système-monde réel | 3 | Vocabulaire mycologique exact et centre antipoison — mais le monde réel parle « fausse morille » et « ange destructeur », que le journal ne reconnaît pas (aucun badge rouge). |
| 3 | Contrôle et liberté | 4 | Annuler partout, garde-fou variété, restauration sélective, double confirmation. |
| 4 | Cohérence et standards | 3 | Système très tenu (helpers unifiés, tokens), mais « Réessayer » ≠ appareil, title photo-zone faux quand vide, 🗑️ = masquer. |
| 5 | Prévention des erreurs | 3 | Double confirmation, fail-safe IA (statut hors vocabulaire → inconnu, l.2118-2120), validation nom — mais date future acceptée, import sans version, synonymes mortels sans alerte. |
| 6 | Reconnaissance plutôt que mémorisation | 3 | Filtres visibles, autocomplétion, matche flou — mais FAB sans libellé dynamique, état vide filtré sans reset suggéré. |
| 7 | Flexibilité et efficacité | 3 | FAB contextuel, partage Web Share, GPS, matche flou — pas de tri/recherche dans le journal, pas de raccourcis. |
| 8 | Esthétique minimaliste | 3 | Memphis dense et assumé ; la fiche détail s'est allégée au bon endroit (verdict tôt) mais 10 puces et le mur encyclopédique restent. |
| 9 | Aide à la reconnaissance des erreurs | 4 | messageErreurIA français avec guidance par cause (clé/réseau/quota/500/404), toasts, états vides orientés. |
| 10 | Documentation et aide | 3 | Bandeau clé, note export, règle d'or — pas d'aide in situ sur la signification du verdict, pas d'onboarding. |

**Total : 33/40** — profil : très fort sur la sécurité émotionnelle, le langage de domaine et la cohérence interne ; pénalisé par deux angles morts de vérité (synonymes mortels sans badge, analyse IA livrée dans une feuille fermée) et la densité de la fiche.

---

## 6. Forces spécifiques (2-3)

1. **Le système de verdicts de la checklist est devenu un modèle de vérité unique.** ⚠️ ambre par défaut avec « Rien n'est encore vérifié » à 0 critère ET après décoche totale (l.1345, `nbFaits < illu.items.length` couvre 0) ; ✅ vert réservé comestibles/prudence avec nuance (« restez prudent (cuisson obligatoire) », l.1343) ; ☠️ rouge **dynamique** « n/n critères vérifiés — MORTELLE : ne pas consommer » (l.1344). Le compteur et le verdict ne peuvent plus se contredire, et le tout est monté juste sous l'alerte de sécurité (l.1360-1361). C'est exactement l'inverse du pattern « positive-valence verdict on danger items ».
2. **La boucle de comparaison est pensée comme un parcours, pas une navigation.** Scroll mémorisé (`positionGuide`, l.1312, restauré en rAF l.1378), nom d'espèce dans le sous-titre du header + badge masqué (l.1370-1371), bouton ← sticky 44 px (l.56-63, 374), onglet Identifier maintenu actif (l.952). Comparer une récolte douteuse avec l'amanite phalloïde puis la galerine se fait sans perdre sa place — le geste le plus important du produit est le plus fluide.
3. **La discipline Memphis est totale, jusque dans les micro-détails.** Poignée de feuille avec hit-area étendu (l.292), tabular-nums sur tous les compteurs dynamiques, appui scale(.96) des cartes spécificités (l.256), sortie de feuille sans rebond (l.286), outlines 1 px noir 10 % sur les images, text-wrap:balance sur les titres, focus ambre + focus trap + Escape sur toutes les modales. Chaque règle nommée du DESIGN.md (Trait Noir, Rouge Mortel, Inclinaison, Décalage Net) est exécutée dans le code.

---

## 7. Problèmes prioritaires (3-5)

### P1-1 — Les synonymes vernaculaires mortels ne déclenchent aucun badge de sécurité dans le journal
- **Preuve :** `infoEspece` (l.932-944) matche par nom normalisé exact, puis Levenshtein ≤ 2. « Fausse morille » vs « Gyromitre (fausse morille) » : différence de longueur 13 → rejeté. « Ange destructeur » vs « Amanite vireuse (ange destructeur) » : ≥ 19 → rejeté. Or ces deux synonymes sont **littéralement dans les noms du guide** (l.887, l.877) et la recherche guide les trouve par inclusion (l.1287). Le journal, lui, affiche « Fausse morille » sans aucun badge (l.1412, `statutEff = null`).
- **Pourquoi c'est grave :** « fausse morille » est LE nom vernaculaire québécois de la gyromitre, l'espèce la plus meurtrière du printemps. Le produit connaît le synonyme (il est dans la fiche) mais le journal n'affiche aucun rouge — la promesse « badge de sécurité conservé » (l.1405-1408) est trahie par la couverture lexicale, pas par l'orthographe. Le fix Levenshtein de la 9e passe tient pour les fautes de frappe ; il ne couvre pas le vocabulaire de terrain.
- **Fix :** dans `infoEspece`, après l'exact et le flou, ajouter un matche par **inclusion** (le nom saisi est contenu dans le nom complet d'une espèce) avec priorité au plus long, ou une table de synonymes par espèce ; à la saisie, alerter « ⚠️ « fausse morille » = Gyromitre (fausse morille) — MORTELLE » avant d'enregistrer.

### P2-1 — L'analyse photo IA n'est ni annulable ni récupérable
- **Preuve :** `analyserPhoto` (l.2099-2104) ouvre la feuille puis attend 10-20 s (fetch sans AbortController, l.1525). `fermerFeuilles()` (l.970-973) retire simplement la classe `ouverte` ; quand la réponse arrive, l'`innerHTML` est réécrit (l.2108-2111, 2140-2162) **sans rouvrir la feuille** et sans toast.
- **Pourquoi :** l'utilisateur en forêt qui referme la feuille (poignée ou voile) croit avoir annulé ; l'analyse aboutit en arrière-plan et le résultat (potentiellement « MORTEL — centre antipoison ») disparaît silencieusement. Le seul moyen de le revoir : re-photographier.
- **Fix :** AbortController pour annuler réellement (avec bouton « ✋ Annuler » dans l'état d'analyse), ou à défaut ré-ouvrir la feuille si elle est fermée quand la réponse arrive (`if (!sheet-idphoto.classList.contains('ouverte')) ouvrirFeuille('sheet-idphoto')`) + toast « Analyse terminée ».

### P2-2 — L'import écrase les données v5 sans vérifier la version du fichier
- **Preuve :** l'export écrit `version: 5` (l.2245) ; l'import (l.2257-2284) ne lit jamais `data.version`, ne valide que les tableaux et affiche « Import réussi ✅ » (l.2278). Un export v4 (sans checklist) s'importe, `data.checklist` est forcé à `[]` (l.2266), les stores sont vidés (l.2270) — la checklist terrain disparaît sans avertissement.
- **Pourquoi :** c'est la seule vraie porte de perte de données du carnet, et le toast en fait une victoire. Le power user qui restaure un vieux fichier découvre des semaines plus tard que ses vérifications terrain ont été avalées.
- **Fix :** si `data.version` manque ou est < 5, afficher un avertissement explicite dans la boîte de confirmation (« fichier d'une version antérieure — la checklist sera perdue ») ; si version > 5, refuser ou prévenir d'un format inconnu.

### P3-1 — « 📷 Réessayer » rouvre la galerie au lieu de répéter la source
- **Preuve :** l.2136 : `onclick="identifierParPhoto(false)"` — toujours la galerie, même si la photo venait de l'appareil (l.2095-2097).
- **Fix :** mémoriser `derniereSource` et la répéter, ou libeller « 🖼️ Choisir une autre photo ».

### P3-2 — La lightbox ne restaure pas le focus à la fermeture
- **Preuve :** l.2077-2082 : `fermer()` retire l'écouteur et supprime le nœud sans mémoriser `document.activeElement` — le focus retombe sur `<body>` après Escape/clic.
- **Fix :** capturer l'élément déclencheur à l'ouverture (`const declencheur = document.activeElement`) et `declencheur.focus()` dans `fermer()`.

---

## 8. Red flags par persona

### Power user — Jonathan à la maison (stats, export/import, variétés perso)
- **Ce qui marche :** stats complètes, export v5 avec checklist, restauration sélective, feuille variété avec garde-fou, double confirmation sur tout effacement.
- **Red flags :** l'import écrase sans vérifier la version (l.2257-2284) — un vieux fichier avale la checklist et le toast dit « réussi » ; l'alerte « Jamais exporté » (l.2235-2242) est un one-shot à vie (`cqm_exporte` posé au premier export, l.2252) — la promesse « Exportez-le régulièrement » n'est plus soutenue après le premier clic.
- **Pire moment :** restaurer un fichier de l'an dernier et découvrir des semaines plus tard que toutes ses vérifications terrain ont été avalées.

### Utilisateur à accessibilité réduite (clavier, lecteur d'écran)
- **Ce qui marche :** clavier Enter/Espace sur tous les role=button, focus-visible ambre, aria-live toast, contrastes AA vérifiés, lightbox dialog + Escape, focus trap sur les modales.
- **Red flags :** focus non restauré après fermeture de la lightbox (l.2077-2082) ; boîte de choix sans focus initial (l.1036-1045) ; badge compteur annoncé « 0 » sans contexte (l.373) ; FAB annoncé « Ajouter » pour une action 📍 (l.461).
- **Pire moment :** agrandir la photo d'une amanite phalloïde pour vérifier la volve, fermer au clavier, et se retrouver le focus perdu dans la page sans savoir où on est.

### Mobile distrait — en forêt, une main, sans réseau
- **Ce qui marche :** 100 % hors-ligne (SW v31, credits.json inclus l.138-139), cibles ≥44 px, autocomplétion, matche flou (fautes de frappe couvertes), puces à bascule, verdicts lisibles au soleil (noir/crème 14.08:1).
- **Red flags :** « fausse morille » noté d'une main mouillée = aucun badge rouge (l.932-944) ; l'analyse IA 10-20 s sans annulation dont le résultat se perd si la feuille est fermée (l.2099-2162) ; toast 2,2 s court pour les erreurs IA longues (l.725).
- **Pire moment :** photographier un petit champignon brun sur une souche, fermer la feuille pendant l'analyse, et ne jamais voir le verdict « Galerine marginée — MORTEL » qui est pourtant arrivé.

---

## 9. Observations mineures

- `.spec-num` `font-weight:900` hors des graisses chargées (l.259 vs l.17) — rendu synthétisé variable.
- `COULEURS_MOIS` en dur (l.2194) au lieu des variables CSS — dérive de tokens amorcée.
- `title="Cliquez pour retirer la photo"` trompeur quand la zone est vide (l.521, 569, 626).
- FAB aria-label statique « Ajouter » alors que l'icône devient 📍 (l.461).
- Badge header : `title` seulement, pas d'aria-label (l.373).
- `alt="photo"` générique sur les photos utilisateur (l.1097).
- Bouton 🗑️ de la liste guide : la corbeille promet la suppression, le clic ouvre « Masquer ou supprimer » (l.1304 vs l.1036-1045).
- ✓ blanc sur olive à 3.44:1 : sous AA pour du texte, OK comme icône graphique (3:1) — à trancher.
- Graphique mensuel sans valeurs en kg (l.2228-2231).
- Champ date de cueillette accepte le futur (l.541) — « Dernière sortie » peut être future.
- État vide du guide filtré sans suggestion de réinitialisation des filtres (l.1291).
- Sous-titre header en détail = nom d'espèce : « Amanite vireuse (ange destructeur) » peut pousser le bouton retour sur petit écran (l.1370) — pas d'ellipsis sur `.sous`.
- Le select météo natif est le seul contrôle « système » visible — acceptable (documenté), mais casse légèrement l'illusion native.
- Alerte « Jamais exporté » one-shot à vie (l.2252) — plus de rappel de sauvegarde après le premier export.
- Boîte de choix sans focus initial (l.1036-1045) alors que la boîte de confirmation focus « Annuler » (l.1001) — incohérence de pattern entre les deux modales.

---

## 10. Questions provocatrices

1. Le matche flou Levenshtein ≤ 2 couvre « amanite phaloide » mais pas « fausse morille » ni « ange destructeur » — deux noms vernaculaires québécois qui figurent littéralement dans les noms du guide : la couverture de sécurité du journal doit-elle être lexicale (fautes de frappe) ou sémantique (tout nom que le guide reconnaît) ?
2. L'analyse photo IA dure 10-20 s sans annulation, et son résultat est réécrit dans une feuille fermée si l'utilisateur est parti : doit-on annuler réellement (AbortController + bouton), ou livrer le résultat en ré-ouvrant la feuille avec un toast — sachant que le verdict peut être « MORTEL » ?
3. L'import ne vérifie pas `data.version` : faut-il un avertissement « fichier d'une version antérieure — la checklist sera perdue » quand version < 5, refuser les versions futures, ou les deux ?
4. Le bouton « 🗑️ » de la liste guide ouvre « Masquer ou supprimer » : la corbeille promet la destruction, l'action par défaut est réversible — faut-il une icône neutre (⋯) pour le masquage et réserver la corbeille à la vraie suppression, ou assumer la corbeille comme « gestion d'espèce » ?
5. Le « 📷 Réessayer » rouvre la galerie : l'utilisateur qui vient de photographier un champignon douteux en forêt doit-il repasser par l'appareil, ou « Réessayer » devrait-il répéter la dernière source ?
6. Les 10 puces de filtres (5 statuts + 5 saisons) : est-ce le bon équilibre pour une main en forêt, ou faut-il un menu dépliable « Filtres » qui ne montre que la combinaison active ?
7. Le graphique mensuel montre des barres sans valeurs : un carnet de récolte a-t-il besoin de lire « 2,4 kg en septembre », ou la hauteur relative suffit-elle pour un usage personnel ?
8. L'alerte « Jamais exporté » ne réapparaît jamais après le premier export : faut-il un rappel périodique (tous les X exports, ou après N nouvelles cueillettes), ou l'utilisateur est-il supposé prendre l'habitude tout seul ?
9. La boîte de confirmation focus « Annuler » mais la boîte de choix ne focus rien : les deux modales doivent-elles partager le même protocole de focus initial, et lequel est le bon (le plus sûr = Annuler, ou le plus probable = l'action principale) ?
10. La lightbox restaure-t-elle le focus au déclencheur, et si oui, l'utilisateur clavier qui a zoomé 5 photos de spécificités à la suite doit-il repasser par 5 retours de focus, ou la navigation devrait-elle sauter de photo en photo dans la lightbox elle-même ?

---

## Vérification des fixes de la 9e passe (commit fc1021d) — tous confirmés

| Fix annoncé | Preuve | Statut |
|---|---|---|
| Verdict danger dynamique ☠️ n/n (fini le « 5/5 » en dur) | l.1344 : `'☠️ ' + nbFaits + '/' + illu.items.length + ' critères vérifiés'` | ✅ |
| Matche flou infoEspece (Levenshtein ≤ 2, badge survit aux fautes de frappe) | l.924-944 (`distLevenshtein`, filtre `c.d <= 2`, garde `n.length >= 4`) | ✅ |
| Lightbox accessible (role=dialog, aria-label, Escape, focus) | l.2068-2083 | ✅ |
| Galerie + verdicts placés juste sous l'alerte de sécurité | l.1360-1361 (`avis` puis `galerie` avant tout le reste) | ✅ |
| Focus trap + Escape sur modales confirm/choix | l.1011-1032 | ✅ |

**Score : 33/40** (vs 34/40 à la 9e passe). Les 5 fixes tiennent tous, sans régression visible. La baisse d'un point vient de deux trous nouvellement caractérisés : **P1-1** — le matche flou couvre l'orthographe mais pas les synonymes vernaculaires mortels (« fausse morille »/« ange destructeur » sans badge rouge dans le journal, résidu du même domaine que le fix P1-2 de la 9e) — et **P2-1** — l'analyse photo IA sans annulation dont le résultat est livré dans une feuille fermée. L'échelle reste honnête : les corrections confirment, le vocabulaire de terrain et les états d'analyse restent les deux fronts de vérité du produit.
