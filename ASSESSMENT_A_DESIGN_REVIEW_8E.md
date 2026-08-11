# Assessment A — Critique design (8e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2357 lignes, HTML+CSS+JS mono-fichier)
**Docs de référence :** `PRODUCT.md`, `DESIGN.md` (North Star « La Récolte », palette AUTOMNE/TERRE)
**Méthode :** lecture statique du source (Assessment A), vérification des fixes des passes 4-7 (commits d00b6d8 → 8efa18f), calculs de contrastes WCAG explicites (luminance relative).
**Date :** 11 août 2026

---

## 1. Verdict de spécificité design

**Axe conceptuel : ~90 %.** Vocabulaire du carnet de chasse mycologique québécois : « coin secret », « Règle d'or : en cas de doute, on ne mange pas », « centre antipoison 1-800-463-5060 », « spécificités à repérer », verdicts ⚠️/✅, confusions dangereuses (gyromitre vs morille, lépiote brunâtre vs élevée, amanite rougissante vs panthère). Une capture sans texte révélerait le domaine : champignons, panier, forêt, saisons.

**Axe visuel : ~85 %.** Toujours pas un template : bordures noires 3 px, coins cassés 18/5 px, ombres dures sans flou, zigzag d'en-tête, pois crème, titres inclinés -1/-2°, vignettes à rayures ambre/blanc, FAB rose, pastilles inclinées, focus ambre désormais étendu aux boutons/puces/items/FAB/onglets (index.html:190). Seule réserve inchangée : les 4 cartes stats et les barres de rang restent proches d'une grammaire de dashboard générique — rattrapées par le trait noir et les coins cassés.

**Verdict :** interface spécifique à ce produit sur les deux axes. Le test « screenshot sans texte » passe.

---

## 2. Évaluation holistique

### Hiérarchie visuelle
- Échelle typographique documentée et tenue : display 21 px (h1, -1,5°, text-shadow rose) → titre-vue 20 px pastille blanche → titre de feuille 18 px pastille ambre → corps 16 px → label 13 px → meta 12,5 px. `text-wrap:balance`, `tabular-nums` (index.html:45-47, 54, 304).
- **Dérive persistante :** les `h3` des cartes Stats (« 🏆 Top espèces », « 🗺️ Top spots », « 📅 Récolte par mois », « 💾 Sauvegarde », index.html:411-415) restent en style navigateur par défaut, sans la pastille cuir `.guide-sujet` (index.html:328-329). Deux grammaires de titres de section cohabitent toujours.
- **Nouveau :** `font-weight:900` sur `.spec-num` (index.html:259) et `.spec-carre` (index.html:262) — graisse hors échelle : Fredoka n'est chargée qu'en 400-700 (index.html:17) et DESIGN.md limite la graisse à 400-700. Le navigateur synthétise ou arrondit : rendu incohérent selon les plateformes.
- `.deco-tri` (opacity .12, index.html:337) toujours quasi invisible — décoration fantôme.

### Architecture de l'information
- 5 onglets complets, FAB contextuel (📍 Spots, ＋ ailleurs, masqué Stats/détail/Paramètres — index.html:936-938).
- **Fix P1-2 de la passe 7 confirmé :** bouton « ← » sticky dans le header en vue détail (index.html:56-63, 373, 939) + onglet Identifier actif en détail (index.html:935). Le retour ne coûte plus 3000 px de scroll.
- **Nouveau trou :** le retour ramène en HAUT de la liste du guide — `naviguer()` fait `window.scrollTo(0,0)` à chaque navigation (index.html:943), y compris `fermerDetail()`. Le parcours de comparaison (fiche A → ← → fiche B) perd la position dans la liste filtrée à chaque aller-retour.
- **Nouveau trou :** la vue détail n'a ni titre-vue ni nom d'espèce dans le header sticky (index.html:428-430) : en scroll profond dans une fiche de ~3000 px, on ne sait plus quelle espèce on consulte. Le header affiche « Cueillette Québec » + badge compteur (index.html:369-372).
- Terminologie stable, pas de résidus de renommage.

### Adéquation émotionnelle
- North Star tenu : header chaleureux, états vides guidés (« Appuyez sur le bouton rose pour ajouter votre premier coin secret ! », index.html:1095), toasts noirs bordés d'ambre.
- Valence correcte : rouge strictement réservé au danger/destruction/compteur documenté ; hors-ligne jamais montré en rouge.
- **Nouvelle fausse note (la plus grave de cette passe) :** le verdict « ✅ Tous les critères correspondent — [nom] confirmé » est rendu en VERT olive (`.verdict-ok`, index.html:271, 1302) même sur les fiches MORTELLES. Cocher les 5 critères d'une amanite phalloïde produit le même bandeau vert « confirmé » que sur une chanterelle — le texte « — restez prudent » ne compense pas la valence visuelle positive (voir P1-1).

### Découvrabilité
- Bandeau clé Gemini persistant avec « Configurer la clé → » qui navigue et focusse le champ (index.html:2032-2035) — excellent.
- « ✨ Générer les manquantes » découvrable (index.html:667).
- **Nouveau piège d'affordance :** le badge « 🔍 Agrandir » (`.spec-zoom`, index.html:260, 1298) est un `<span>` sans handler ni stopPropagation : seul l'`<img>` porte `onclick="event.stopPropagation();ouvrirLightbox(...)"`. Un clic sur le libellé remonte à `.spec-carte` (role=button, `basculerSpec`) → **coche/décoche le critère au lieu d'agrandir** (voir P2-1).

### Composition
- Colonne unique max 640 px, rythme 4/8/12/16/24 px, cartes 16 px — conforme. Feuilles 84 vh avec poignée étendue (index.html:291).
- **Nouveau risque :** en vue détail, le header cumule logo 52 px + titre + badge rouge 34 px + bouton ← 44 px + paddings ≈ 344 px — débordement probable sous 340 px de large (iPhone SE 1re génération), d'autant que le badge compteur n'a aucun sens contextuel pendant l'identification.

### Typographie
- Fredoka 400-700, pas d'uppercase forcé, pas de graisse < 400 — **sauf** les deux `font-weight:900` (voir Hiérarchie).
- Sous-titre header : noir pur, opacity 1, 700 (index.html:49) — **4,79:1** sur #C87224 (calcul explicite) : fix P2-2 de la passe 7 confirmé, AA atteint.

### Couleur
- Palette tenue : 8 couleurs AUTOMNE/TERRE + extensions documentées. Aucune dérive hors palette.
- **Contrastes recalculés (luminance relative explicite) :**
  - ✅ noir/olive 4,61:1 (btn-vert, verdict-ok, st-comestible, libellé carte olive désormais opacity 1 — index.html:306) — fix P2-2 confirmé.
  - ✅ noir/ambre 7,59:1 ; blanc/rouge 6,07:1 ; blanc/terracotta 4,95:1 ; blanc/cuir 5,45:1 ; noir/gris 6,08:1 ; noir/crème (puce saison active) 14,08:1 ; noir sur fonds d'alertes 13,3-13,5:1 ; orange #B45309 sur blanc 4,67:1 ; rouille onglet #B3540B sur blanc 4,66:1 ; cuir lien Commons sur blanc 5,45:1.
  - ⚠️ Coche ✓ blanche sur olive (`.spec-carre.fait`) : 3,44:1 — glyphe 16 px bold, P3 (inchangé).
- **Règle du Rouge Mortel respectée** : rouge = MORTEL, suppression, compteur documenté uniquement.

### Accessibilité
- role=button + tabindex, clavier Enter/Espace (index.html:963-968), aria-live toast (index.html:691), prefers-reduced-motion (index.html:346-348) — confirmés.
- **Fix P2-1 de la passe 7 confirmé :** focus-visible ambre sur `.btn, .puce, .item, .fab, nav.tabs button, .btn-retour` (index.html:190).
- Résidus connus (P3) : `g-recherche` sans aria-label (index.html:396) ; lightbox sans role=dialog ni Escape (index.html:2018-2025) ; imbrication `.item` role=button contenant un vrai `<button>` (index.html:1258-1265) ; `boite-choix` sans focus initial (contrairement à `boite-confirm` qui focus « Annuler », index.html:984) ; pas d'aria-current sur l'onglet actif ; badge header sans aria-label (title seul, index.html:372) ; input `c-espece` sans rôle combobox/aria-expanded pour ses suggestions.

### États
- Chargement : « Analyse en cours… » avec sous-texte (index.html:2045) ; « Génération en cours… » (index.html:1589) ; progression « Génération i/n » (index.html:2001).
- Erreur : `messageErreurIA` en français avec guidance partout, **y compris le catch d'identification photo** (index.html:2107) — fix P2-3 de la passe 7 confirmé.
- Vide : états vides guidés partout.
- **Nouveau trou d'état :** l'écran Crédits photos affiche « Aucun crédit disponible » hors-ligne (voir P1-2).

### Copy
- Français du Québec soigné, ton carnet de chasse tenu. « En cas de doute : on ne mange pas » aux bons endroits.
- **Nouveau point de copy :** « ✅ Tous les critères correspondent — [nom] confirmé — restez prudent » sur les fiches mortelles : le mot « confirmé » accolé à un ✅ vert est ambigu (confirme l'identification, pas la comestibilité) — voir P1-1.

### Cas limites
- `aujourdhui()` en heure locale (index.html:698-701) — pas de bug UTC. `saisonsDe` multi-saisons confirmé (index.html:1235-1238).
- Suppression de spot : cueillettes conservées, affichées « Sans spot » (index.html:1178, 1363) — documenté.
- **Nouvelle incohérence :** dans le Top spots (index.html:2160), les cueillettes dont le spot a été supprimé apparaissent sous « Sans spot » (`nomSpot(c.spotId) || 'Sans spot'`), mais les cueillettes JAMAIS liées à un spot (`!c.spotId`) sont exclues du classement — deux catégories de « sans spot » traitées différemment.
- Réindexation des coches au retrait d'une spécificité : confirmée (index.html:1979-1983).
- « Tout effacer » vide bien les 7 stores dont `checklist` (index.html:2231) — fix P1-1 de la passe 7 confirmé.

---

## 3. Évaluation de charge cognitive (8 items)

| # | Item | Verdict | Preuve |
|---|------|---------|--------|
| 1 | Focus unique (un job par écran) | ✅ | Chaque vue a un job principal ; le guide est un hub mais reste lisible. |
| 2 | Chunking ≤ 4 | ❌ | 10 puces de filtre en 2 rangées (index.html:1222-1230) ; 5 spécificités par fiche ; 21 puces espèces du spot (index.html:1154-1156). |
| 3 | Regroupement visuel | ✅ | Rangées de puces séparées, cartes groupées, grille2, sections guide-sujet. |
| 4 | Hiérarchie | ❌ | h3 des cartes stats hors échelle (style navigateur) ; font-weight:900 hors graisse chargée. |
| 5 | Une chose à la fois | ✅ | Une feuille = un formulaire ; verdicts et compteur n/5 allègent la fiche. |
| 6 | Choix minimaux ≤ 4 | ❌ | Feuille variété : 10 champs + 4 boutons photo ; sélecteur d'espèces du spot : 21 puces d'un coup. |
| 7 | Mémoire de travail | ❌ | **Régression :** le header détail n'affiche pas le nom de l'espèce (il faut se souvenir de laquelle on consulte en scrollant) et le retour de fiche perd la position dans la liste (il faut se souvenir où on était). |
| 8 | Divulgation progressive | ❌ | Fiche détail déverse tout d'un bloc (description, caractéristiques, confusions, 5 photos, verdicts, 4 boutons) — pas de sections repliables. |

**Échecs : 5/8** (régression d'un point vs passe 7 : l'item 7 passe de ✅ à ❌ à cause du header détail sans contexte et de la perte de position au retour).

---

## 4. Voyage émotionnel (peak-end rule)

- **Entrée :** header chaleureux (dégradé, formes flottantes, zigzag), pop élastique des vues — pic d'entrée réussi.
- **Milieu :** zéro boîte système navigateur ; garde-fou « Quitter sans enregistrer ? » (index.html:1514-1518) ; toasts avec guidance. Vallée principale inchangée : la feuille variété longue à remplir une main en forêt. **Nouvelle micro-frustration :** cliquer sur « 🔍 Agrandir » coche le critère — le geste contredit le libellé, et en terrain ça peut modifier un verdict sans que l'utilisateur le veuille.
- **Pic de fin :** « Cueillette enregistrée ✅ » + badge qui s'incrémente + stats colorées — pic authentique.
- **Faux pic (nouveau, le plus sérieux) :** sur une fiche MORTELLE, cocher les 5 critères produit le bandeau VERT « ✅ … confirmé » — le même signal de réussite que sur une chanterelle. C'est un faux pic de sécurité : la satisfaction de la checklist est encodée positivement là où le message devrait être « espèce mortelle, ne pas consommer ».
- **Réassurance à haut risque :** double confirmation destruction, alerte MORTEL + antipoison systématique, verdict ⚠️ par défaut, fail-safe IA (statut hors vocabulaire → inconnu, prudence forcée morille/amanite rougissante, confiance < 60 → inconnue — index.html:2061-2071) — exemplaire.

---

## 5. Les 10 heuristiques de Nielsen

| # | Heuristique | Score | Problème clé |
|---|-------------|-------|--------------|
| 1 | Visibilité de l'état du système | 3,5/4 | Toasts, compteurs, verdicts, puces saison actives noir/crème (fix P2-4 tient) excellents ; pénalisé par le header détail sans nom d'espèce. |
| 2 | Correspondance système-monde réel | 4/4 | Vocabulaire mycologique québécois exact, saisons réelles, emojis météo. |
| 3 | Contrôle et liberté | 4/4 | Bouton ← sticky (fix P1-2 tient), annuler partout, restauration sélective, double confirmation. |
| 4 | Cohérence et standards | 3/4 | Focus ambre partout (fix P2-1 tient) ; pénalisé par font-weight:900 hors échelle, h3 stats non stylés, double espacement des puces, deux traitements « sans spot ». |
| 5 | Prévention des erreurs | 3,5/4 | Verdict ⚠️ par défaut, réindexation, double confirmation, fail-safe IA ; pénalisé par le piège « Agrandir » (modification d'état involontaire) et le verdict ✅ vert sur fiches mortelles (erreur de lecture). |
| 6 | Reconnaissance plutôt que mémorisation | 3/4 | Autocomplétion, puces visibles ; pénalisé par la perte de position au retour de fiche et le header détail sans contexte. |
| 7 | Flexibilité et efficacité | 3/4 | FAB contextuel, GPS 1 clic, « Générer les manquantes » ; pas de raccourcis, pas de recherche spots/cueillettes, comparaison de fiches coûteuse. |
| 8 | Esthétique minimaliste | 3,5/4 | Memphis riche mais dense : fiche détail et feuille variété chargées ; pas de bruit parasite hors design. |
| 9 | Aide à la reconnaissance des erreurs | 4/4 | messageErreurIA français avec guidance partout, y compris catch photo (fix P2-3 tient). |
| 10 | Aide et documentation | 3/4 | Placeholders explicites, bandeau clé, crédits photos ; pas d'onboarding ; crédits indisponibles hors-ligne. |

**Total : 34,5/40** (35/40 à la 7e passe — les 6 fixes tiennent tous, mais 4 nouveaux trous sont apparus : verdict ✅ vert sur mortel, crédits hors-ligne, piège « Agrandir », perte de position/header détail).
**Profil :** très fort sur la prévention des erreurs, le contrôle et la réassurance ; plus faible sur la cohérence des détails et l'efficacité du parcours de comparaison.

---

## 6. Forces spécifiques (2-3)

1. **Le système de verdicts ⚠️/✅ de la checklist terrain** (index.html:1291-1304, 1330-1344) : verdict ⚠️ visible dès 0 critère (« Rien n'est encore vérifié »), bascule ✅ seulement à 5/5, persistance IndexedDB, réindexation des coches au retrait d'une spécificité, inclusion dans l'export/import v5 ET dans « Tout effacer » (fix P1-1 passe 7 confirmé, index.html:2231). Un mécanisme de sécurité réel, exécuté sans faille.
2. **Le fail-safe de l'identification photo** (index.html:2061-2071, 2129) : statut hors vocabulaire → « inconnu » (jamais comestible par défaut), prudence forcée pour les espèces à cuisson obligatoire, confiance < 60 % → « Impossible d'identifier avec certitude » + alerte rouge « En cas de doute, on ne mange pas ». Le prompt lui-même interdit de répondre « comestible » sans prudence. C'est du design de sécurité exemplaire, rare dans une PWA mono-fichier.
3. **La tenue du design system Memphis dans les micro-états** : appui translate 3 px + ombre réduite, rebond élastique des feuilles avec sortie ease-out, coin cassé systématique, vignettes à rayures, zigzag d'onglet actif, et désormais le focus ambre étendu à tous les éléments interactifs (index.html:190). Un langage visuel tenu avec une discipline rare.

---

## 7. Problèmes prioritaires (3-5)

### P1-1 — Verdict ✅ vert « confirmé » sur les fiches mortelles : collision de valence
- **Sévérité : P1** (message de sécurité ambigu au moment de la décision).
- **Preuve :** index.html:1302 — `'<div class="verdict-carte verdict-ok' + (nbFaits === illu.items.length ? ' ouv' : '') + '">…✅ Tous les critères correspondent…' + esc(e.nom) + ' confirmé' + (e.statut === 'comestible' ? ' — récolte possible.' : ' — restez prudent.')` avec `.verdict-ok{background:var(--olive);color:var(--noir)}` (index.html:271). L'olive est définie dans DESIGN.md comme « la confiance » et le ✅ comme la satisfaction du critère vérifié — le même bandeau vert « confirmé » apparaît donc sur l'amanite phalloïde, la galerine et le gyromitre.
- **Pourquoi c'est grave :** le verdict est le dernier élément visuel avant les boutons d'action — le point d'ancrage de la décision. Un cueilleur qui a coché les 5 critères d'une phalloïde voit « ✅ … confirmé » en vert : la valence positive du signal contredit le contenu (« restez prudent »). C'est exactement le type d'ambiguïté qu'un produit à parti pris sécurité (PRODUCT.md, principe 1) ne peut pas se permettre.
- **Correctif concret :** pour les statuts non comestibles (mortel/toxique/immangeable), remplacer le bandeau vert par un verdict neutre (noir/crème) ou rouge, avec un libellé explicite : « 5/5 critères vérifiés — espèce MORTELLE : ne pas consommer » (et « espèce toxique : ne pas consommer »). Réserver le ✅ vert + « récolte possible » aux comestibles/prudence.

### P1-2 — Crédits photos indisponibles hors-ligne : trou dans la promesse 100 % hors-ligne
- **Sévérité : P1** (fonctionnalité livrée inaccessible dans le mode d'usage normal du produit).
- **Preuve :** `chargerCredits()` fetch `img/specs/credits.json` et `img/especes/credits.json` (index.html:2277-2280) avec catch silencieux → hors-ligne, l'écran affiche « Aucun crédit disponible » (index.html:2297). Or `sw.js` FICHIERS (sw.js:5-138) ne contient AUCUN des deux credits.json — le service worker ne les met jamais en cache.
- **Pourquoi c'est grave :** PRODUCT.md promet « 100 % hors-ligne dès la première visite » (PRODUCT.md:23). L'écran Crédits (livré en passe 6) est une obligation des licences CC : les crédits doivent rester accessibles. En forêt ou en avion, l'utilisateur qui consulte les crédits voit un écran vide — et le fetch échoue silencieusement, sans message.
- **Correctif concret :** ajouter `./img/specs/credits.json` et `./img/especes/credits.json` à FICHIERS dans sw.js (bump cqm-v30), et afficher un état d'erreur explicite si le fetch échoue malgré tout.

### P2-1 — « 🔍 Agrandir » ne fonctionne pas : le clic coche le critère
- **Sévérité : P2** (affordance mensongère + modification d'état involontaire de la checklist de sécurité).
- **Preuve :** index.html:1298 — le badge `.spec-zoom` « 🔍 Agrandir » est un `<span>` sans handler ni stopPropagation ; seul l'`<img>` porte `onclick="event.stopPropagation();ouvrirLightbox(this.src)"`. Un clic sur le libellé remonte à `.spec-carte` (role=button, `onclick="basculerSpec(i)"`) → coche/décoche le critère. Au clavier, le span n'est pas focusable : le focus saute à la carte, Entrée coche.
- **Pourquoi c'est grave :** le libellé promet un zoom, le geste modifie l'état de la checklist — donc potentiellement le verdict de sécurité. En forêt, doigt épais, on vise le badge et on change le verdict sans le vouloir.
- **Correctif concret :** donner au span un `onclick="event.stopPropagation();ouvrirLightbox(this.src)"` (ou en faire un vrai `<button>` avec aria-label « Agrandir la photo »).

### P2-2 — Retour de fiche : perte de position dans la liste du guide
- **Sévérité : P2** (parcours de comparaison — le plus critique en identification — toujours coûteux).
- **Preuve :** `naviguer()` exécute `window.scrollTo(0,0)` à chaque navigation (index.html:943), y compris `fermerDetail() → naviguer('guide')` (index.html:1329). Le fix P1-2 de la passe 7 a réglé le scroll de 3000 px dans la fiche, mais le retour ramène en haut de la liste, même si on était à la 18e espèce d'une liste filtrée.
- **Pourquoi c'est grave :** le parcours réel est « fiche A → ← → fiche B » (comparer une amanite douteuse avec la panthère). Chaque comparaison coûte un re-scroll + un re-filtrage mental.
- **Correctif concret :** mémoriser `window.scrollY` (ou l'index de l'item) avant `ouvrirDetail()` et le restaurer dans `fermerDetail()` avant/après le rendu du guide.

### P2-3 — Le header en vue détail n'identifie pas l'espèce consultée
- **Sévérité : P2** (orientation perdue au moment où elle compte le plus).
- **Preuve :** `vue-detail` n'a pas de `h2.titre-vue` (index.html:428-430) ; le header sticky affiche toujours « Cueillette Québec » + badge rouge compteur (index.html:369-372). En scroll profond dans une fiche de ~3000 px (5 photos 16:9 + checklist), rien ne rappelle quelle espèce on consulte.
- **Pourquoi c'est grave :** l'utilisateur doit mémoriser l'espèce (charge cognitive, item 7) pendant qu'il compare des critères — exactement le moment où la mémoire est déjà sollicitée par les 5 spécificités.
- **Correctif concret :** en vue détail, remplacer le sous-titre (ou le h1) par le nom de l'espèce consultée, et masquer le badge compteur (bruit sans contexte).

---

## 8. Red flags par persona

### Jonathan en forêt (mobile, une main, gants, sans réseau)
- **Ce qui marche :** tout est hors-ligne, cibles ≥ 44 px, FAB contextuel, GPS 1 clic, bouton ← sticky, verdicts lisibles sans réseau.
- **Red flags :** verdict ✅ vert « confirmé » sur les fiches mortelles (P1-1) ; « 🔍 Agrandir » qui coche le critère (P2-1) ; retour de fiche qui perd la position dans la liste (P2-2) ; header détail sans nom d'espèce (P2-3).
- **Pire moment :** il a coché les 5 critères d'une amanite phalloïde, le bandeau vert « ✅ … confirmé » s'affiche, et il hésite — le doute ne devrait jamais être installé par l'interface sur une espèce mortelle.

### Utilisateur à accessibilité réduite (clavier, lecteur d'écran)
- **Ce qui marche :** role=button + tabindex partout, Enter/Espace global, aria-live toast, reduced-motion, focus ambre partout (fix P2-1 tient), focus initial sur « Annuler » dans les confirmations.
- **Red flags :** « 🔍 Agrandir » non focusable (le focus saute à la carte, Entrée coche au lieu d'agrandir) ; lightbox sans role=dialog ni Escape ; `g-recherche` sans aria-label ; imbrication `.item` role=button + `<button>` enfant ; `boite-choix` sans focus initial ; pas d'aria-current sur l'onglet actif.
- **Pire moment :** tabuler jusqu'au badge « Agrandir », appuyer Entrée, et découvrir que le verdict de la checklist a changé.

### Utilisateur pressé / distrait (notification, appel, prêt du téléphone)
- **Ce qui marche :** double confirmation avant destruction, toasts clairs, « Jamais exporté », « Tout effacer » vide vraiment tout (fix P1-1 tient).
- **Red flags :** crédits photos « Aucun crédit disponible » hors-ligne (P1-2) — l'écran promis est vide sans explication ; badge rouge compteur affiché en détail (bruit).
- **Pire moment :** consulter les crédits en avion pour vérifier une licence CC et tomber sur un écran vide sans message d'erreur.

---

## 9. Observations mineures

- `g-recherche` sans aria-label (placeholder seul, index.html:396).
- Lightbox sans role=dialog, sans Escape, sans gestion du focus (index.html:2018-2025).
- Imbrication interactive invalide : `.item` role=button contenant un vrai `<button class="btn-suppr-item">` (index.html:1258-1265).
- `boite-choix` (Masquer/Supprimer) sans focus initial, contrairement à `boite-confirm` (index.html:984).
- `nav.tabs` sans aria-current sur l'onglet actif ; badge header sans aria-label (title seul, index.html:372).
- Input `c-espece` sans rôle combobox/aria-expanded pour ses suggestions (index.html:1372-1391).
- `p-cle` en type=password sans toggle « voir la clé » (index.html:445).
- h3 des cartes stats non stylés (style navigateur par défaut) — deux grammaires de titres de section.
- `.deco-tri` à opacity .12 — décoration fantôme quasi invisible (index.html:337).
- Double espacement des puces du guide (gap 6px + margin 7px, index.html:1225/1228 + 169) vs puces du spot (gap seul, index.html:516).
- Deux traitements « sans spot » dans le Top spots : jamais-liées exclues, spots supprimés agrégés sous « Sans spot » (index.html:2160).
- Emojis ☠️ (« Ne pas manger ») vs 💀 (« Mortels ») : deux crânes dont le plus « poison » est sur le niveau le moins grave — la hiérarchie est portée par les couleurs, pas par les emojis.
- Coche ✓ blanche sur olive 3,44:1 — glyphe, P3 (inchangé).
- Pas de `<noscript>` : sans JS, page blanche.
- `manifest.json` : `orientation: "portrait"` forcée — discutable sur tablette/desktop.
- Risque de débordement du header en vue détail sous ~340 px (logo + titre + badge + ←).
- Styles inline massifs (margin-top, display) dans le HTML — dette de code, pas un défaut de design.

---

## 10. Questions provocatrices

1. Le verdict « ✅ Tous les critères correspondent — confirmé » est vert olive sur l'amanite phalloïde comme sur la chanterelle — pourquoi la couleur de la confiance valide-t-elle une espèce mortelle ? Ne faut-il pas un verdict rouge/neutre « 5/5 vérifiés — MORTEL : ne pas consommer » ?
2. Les crédits photos sont une obligation des licences CC et le produit promet « 100 % hors-ligne » — pourquoi credits.json n'est-il pas dans le cache du service worker, et pourquoi l'échec est-il silencieux ?
3. « 🔍 Agrandir » est un span décoratif : pourquoi le libellé qui promet un zoom déclenche-t-il une coche de checklist — et qui assume la modification de verdict qui en résulte ?
4. Le retour de fiche ramène en haut de la liste filtrée — pourquoi ne pas mémoriser la position de scroll pour le parcours de comparaison, qui est le parcours de sécurité n° 1 ?
5. En scrollant dans une fiche de 3000 px, le header affiche « Cueillette Québec » et le compteur de cueillettes — pourquoi pas le nom de l'espèce consultée, et le compteur a-t-il un sens pendant l'identification ?
6. `font-weight:900` sur `.spec-num` et `.spec-carre` alors que Fredoka n'est chargée qu'en 400-700 — la graisse est-elle un oubli ou un choix assumé de synthèse navigateur ?
7. Les cueillettes jamais liées à un spot sont invisibles dans le Top spots, mais celles de spots supprimés apparaissent sous « Sans spot » — y a-t-il une seule catégorie « sans spot » ou deux ?
8. Les puces du guide cumulent gap 6 px + margin 7 px quand celles du spot n'ont que le gap — quel est l'espacement de référence du design system ?
9. La modale de choix d'espèce (Masquer/Supprimer) n'a pas de focus initial alors que la confirmation en a un — pourquoi deux traitements clavier pour deux modales jumelles ?
10. ☠️ pour « Ne pas manger » et 💀 pour « Mortels » : si un utilisateur daltonien ne lit que les emojis, quelle hiérarchie perçoit-il ?
11. Le h3 des cartes stats reste en style navigateur par défaut — quand les titres de section auront-ils droit à la pastille cuir comme ceux du guide ?
12. Le badge rouge compteur reste affiché en vue détail à côté du bouton ← — sur un écran de 320 px, que sacrifie-t-on : le titre, le badge ou le bouton retour ?

---

## Vérification des fixes des passes 4-7 (exigence de relecture)

| Fix annoncé | Verdict |
|---|---|
| P0-1 verdict ⚠️ visible à 0 critère ET après décoche totale | ✅ Confirmé (index.html:1303, `nbFaits < illu.items.length` couvre 0) |
| P1-1 variables CSS --ambre/--olive/--cuir | ✅ Confirmé (index.html:20-24) |
| P1-2 a11y clavier (role=button, Enter/Espace, aria-live, reduced-motion) | ✅ Confirmé (index.html:963-968, 691, 346-348) |
| P2-1 contrastes (verdict ✅ noir/olive, meta .85) | ✅ Confirmé (4,61:1 et 10,16:1) |
| P2-2 autocomplétion espèce (input + suggestions, valeur libre) | ✅ Confirmé (index.html:1372-1391) |
| P1-1 checklist dans l'export/import v5 | ✅ Confirmé (index.html:2187, 2212, 2219) |
| P1-2 réindexation des coches au retrait d'une spécificité | ✅ Confirmé (index.html:1979-1983) |
| P2-1 contrastes libellés stats AA (dont olive) | ✅ Confirmé (index.html:306, opacity 1 → 4,61:1) |
| P2-2 filtres sécurité complets | ✅ Confirmé (index.html:1242-1246) |
| P2-3 erreurs IA en français avec guidance (dont catch photo) | ✅ Confirmé (index.html:2107) |
| P1-1 « Tout effacer » vide aussi la checklist | ✅ Confirmé (index.html:2231) |
| P1-2 bouton ← sticky header + onglet Identifier actif en détail | ✅ Confirmé (index.html:56-63, 373, 935, 939) |
| P2-1 focus-visible ambre boutons/puces/items/FAB/onglets | ✅ Confirmé (index.html:190) |
| P2-2 contraste olive + sous-titre header noir pur 700 | ✅ Confirmé (4,61:1 et 4,79:1 — calculs explicites) |
| P2-3 catch identification photo via messageErreurIA | ✅ Confirmé (index.html:2107) |
| P2-4 puces saison actives fond noir/crème | ✅ Confirmé (index.html:174, 14,08:1) |
| Refactor helpers (appelGemini, lierPhoto, topRangs, fermerFeuilleVariete, saisonsDe, recharger Promise.all) | ✅ Tous confirmés (index.html:1469, 1062, 2137, 1514, 1235, 2314) |
| SW bump cqm-v29 cohérent avec le commit 8efa18f | ✅ Confirmé (sw.js:4) |

**Tous les fixes des passes 4-7 tiennent.** Le score baisse légèrement (35 → 34,5/40) non par régression des fixes, mais par l'apparition de 4 nouveaux trous (verdict vert sur mortel, crédits hors-ligne, piège « Agrandir », perte de position/header détail).

---

*Rapport produit par lecture statique uniquement (Assessment A) — aucun fichier du projet modifié, aucun outil de détection ni navigateur utilisé.*
