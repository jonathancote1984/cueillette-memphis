---
name: Cueillette Québec — édition Memphis
description: Carnet de cueillette de champignons du Québec, 100 % hors-ligne, style Memphis automne/terre chaleureux et assumé.
colors:
  ambre: "#D9A441"
  rouille: "#B45309"
  terracotta: "#B94527"
  olive: "#6F8F3E"
  cuir: "#8A5A2B"
  creme: "#F3E8D5"
  blanc: "#FDF6E7"
  noir: "#241A0F"
  rouge: "#B3261E"
  gris: "#A89882"
  bleu-canard: "#0B6E96"
  rouille-onglet: "#B3540B"
  vert-mesure: "#0B7A55"
  rose-onglet: "#C2185B"
  brun-tabac: "#7A5C2E"
  brun-header: "#C87224"
  fond-alerte-rouge: "#F6DFD2"
  fond-alerte-orange: "#F4E3C3"
  barre-vide: "#D8C9AC"
typography:
  display:
    fontFamily: "Fredoka, 'Segoe UI', system-ui, sans-serif"
    fontSize: "21px"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "0.2px"
  titre:
    fontFamily: "Fredoka, 'Segoe UI', system-ui, sans-serif"
    fontSize: "20px"
    fontWeight: 700
    lineHeight: 1.2
  corps:
    fontFamily: "Fredoka, 'Segoe UI', system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.65
  label:
    fontFamily: "Fredoka, 'Segoe UI', system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 700
    lineHeight: 1.4
rounded:
  sm: "8px"
  md: "12px"
  lg: "18px"
  xl: "24px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "24px"
components:
  btn-jaune:
    backgroundColor: "{colors.ambre}"
    textColor: "{colors.noir}"
    rounded: "999px"
    padding: "10px 16px"
  btn-rouge:
    backgroundColor: "{colors.rouge}"
    textColor: "{colors.blanc}"
    rounded: "999px"
    padding: "10px 16px"
  btn-vert:
    backgroundColor: "{colors.olive}"
    textColor: "{colors.noir}"
    rounded: "999px"
    padding: "10px 16px"
  btn-bleu:
    backgroundColor: "{colors.cuir}"
    textColor: "{colors.blanc}"
    rounded: "999px"
    padding: "10px 16px"
  btn-rose:
    backgroundColor: "{colors.terracotta}"
    textColor: "{colors.blanc}"
    rounded: "999px"
    padding: "10px 16px"
  pastille-comestible:
    backgroundColor: "{colors.olive}"
    textColor: "{colors.noir}"
    rounded: "999px"
    padding: "3px 11px"
  pastille-mortel:
    backgroundColor: "{colors.rouge}"
    textColor: "{colors.blanc}"
    rounded: "999px"
    padding: "3px 11px"
  carte:
    backgroundColor: "{colors.blanc}"
    textColor: "{colors.noir}"
    rounded: "{rounded.lg}"
    padding: "14px"
  saisie:
    backgroundColor: "{colors.blanc}"
    textColor: "{colors.noir}"
    rounded: "{rounded.md}"
    padding: "12px"
  titre-vue:
    backgroundColor: "{colors.blanc}"
    textColor: "{colors.noir}"
    rounded: "{rounded.lg}"
    padding: "6px 14px"
---

# Design System : Cueillette Québec — édition Memphis

## Overview

**Creative North Star : « La Récolte » — l'énergie d'une belle journée de cueillette, panier plein.**

L'interface est un carnet de chasse chaleureux et tactile, exécuté dans le style Memphis : bordures noires épaisses (3 px), coins cassés, ombres dures sans flou, formes géométriques flottantes, zigzag d'en-tête, pois au fond, titres légèrement inclinés. Le ludisme est assumé jusque dans les micro-interactions — les rebonds élastiques des feuilles et des confirmations font partie du plaisir, pas un défaut. La palette est celle de l'automne québécois : ambre, rouille, terracotta, olive, cuir sur crème. L'app se comporte comme une app native : feuilles bottom-sheet avec poignée, FAB contextuel, toasts, zéro boîte système navigateur. Les moments à haut risque (espèces mortelles, identification incertaine) sont marqués par des alertes rouges non négociables avec centre antipoison.

**Key Characteristics :**
- Bordures noires 3 px partout, ombres dures sans flou (décalage 3-6 px)
- Coins cassés : un coin différent des trois autres (18 px vs 5 px)
- Titres légèrement inclinés (-1 à -2°), badges et pastilles aussi
- Zigzag noir sous l'en-tête, pois crème sur le fond, formes SVG flottantes
- Fredoka, arrondie et chaleureuse, sans uppercase forcé
- Élasticité délibérée : cubic-bezier(.2, 1.3-1.6, .4, 1) pour les apparitions

## Colors

Palette AUTOMNE/TERRE — la forêt québécoise en septembre. Cinq accents vifs sur fond crème, cerclés de noir.

### Primary
- **Ambre** (#D9A441) : l'accent principal — boutons jaunes, puces actives, titres de feuille, zigzag. La chaleur du soleil d'automne.
- **Rouille** (#B45309) : signal — alertes orange, onglet Identifier actif, illustration active. L'écorce et les feuilles mortes.

### Secondary
- **Terracotta** (#B94527) : l'énergie — FAB, bouton rose, carte « Dernière sortie », onglet Stats actif. Le panier rempli.
- **Olive** (#6F8F3E) : la confiance — badges Comestible, boutons d'identification photo, carte « Espèces ». La mousse.
- **Cuir** (#8A5A2B) : l'action secondaire — boutons Modifier, titres de section guide, carte « Sorties ». Le cuir du carnet.

### Neutral
- **Crème** (#F3E8D5) : fond général + pois.
- **Blanc** (#FDF6E7) : surfaces (cartes, feuilles, champs).
- **Noir** (#241A0F) : bordures, texte principal, toasts. Le trait du crayon.
- **Rouge** (#B3261E) : danger absolu — badges MORTEL, boutons de suppression, pastille compteur.
- **Gris** (#A89882) : neutre — boutons Retour, filtre « Tous » actif, badge « Immangeable ».

### Named Rules
**La Règle du Trait Noir.** Toute surface colorée porte une bordure noire de 3 px. Sans le trait, la couleur n'est pas un élément de l'interface.
**La Règle du Rouge Mortel.** Le rouge n'apparaît que pour le danger (MORTEL, suppression, compteur) — jamais pour la décoration.

## Typography

**Display Font :** Fredoka (avec repli 'Segoe UI', system-ui, sans-serif) — arrondie, dodue, chaleureuse.

**Caractère :** une seule famille, ronde et amicale, du titre au corps. Pas d'uppercase forcé, pas de césure. La hiérarchie passe par le poids (400-700) et la taille.

### Hierarchy
- **Display** (700, 21 px, 1.1) : le H1 du header, incliné de -1,5°, avec text-shadow rose.
- **Titre de vue** (700, 20 px, 1.2) : en pastille blanche cerclée de noir, inclinée de -1°.
- **Titre de feuille** (700, 18 px, 1.2) : en pastille ambre, inclinée de -1°.
- **Corps** (400, 16 px, 1.65) : texte courant, descriptions, fiches.
- **Label de champ** (700, 13 px, 1.4) : libellés de formulaires.
- **Meta** (400, 12.5 px, 1.5) : secondaires (dates, habitats) avec opacité 0.85 (correction AA — ne pas redescendre sous 0.8).

### Named Rules
**La Règle de l'Inclinaison.** Un titre n'est jamais parfaitement droit : -1 à -2°, jamais plus. L'inclinaison est le sourire du carnet.

## Layout

Colonne unique centrée, max-width 640 px. Header sticky avec zigzag ; navigation en barre fixe en bas (5 onglets : Spots, Identifier, Cueillettes, Stats, Paramètres), avec indicateur d'onglet actif en zigzag ambre et icône relevée de 4 px. FAB circulaire en bas à droite (au-dessus de la barre), icône contextuelle (📍 en Spots, ＋ ailleurs), masqué en Stats/détail/Paramètres. Espacement : rythme 4/8/12/16/24 px, cartes espacées de 16 px. Formulaires en feuilles bottom-sheet (max 84 vh, coins hauts arrondis 24 px), poignée de fermeture en haut. Grille 2 colonnes pour les paires de boutons et les cartes stats.

## Elevation & Depth

**Pas d'ombres douces : des ombres dures.** La profondeur est exprimée par décalage net : 3-6 px de noir pur sous chaque surface, sans flou. L'appui (état actif) translate l'élément de 2-3 px et réduit l'ombre à 0-2 px — l'effet « bouton qu'on enfonce ». Les feuilles glissent depuis le bas avec rebond élastique (cubic-bezier(.2, 1.3, .4, 1), 0.3 s).

### Named Rules
**La Règle du Décalage Net.** Jamais de box-shadow avec blur. Une ombre = un décalage de 2-6 px, noir pur, sans flou.

## Shapes

Forme de base : coins arrondis généreux (12-24 px) avec **un coin cassé** — le coin inférieur droit est presque droit (4-6 px) quand les autres sont ronds. C'est la signature Memphis du projet, déclinée sur les cartes, champs, feuilles et alertes. Boutons et pastilles : pilules (999 px). Vignettes : fond en rayures diagonales ambre/blanc (répétition 45°, 8-16 px). Zigzag : triangle répété sous l'en-tête et dans l'indicateur d'onglet actif. Motifs : pois crème sur fond (radial-gradient, 28 px), formes SVG flottantes (cercle pointillé, demi-lune, triangle) dans le header. Icône : SVG inline, pas de bibliothèque.

## Components

### Boutons
- **Forme :** pilule (999 px), bordure noire 3 px, ombre dure 3 px.
- **Primaire :** fond coloré selon l'action — jaune (défaut), vert (identification photo), rouge (destruction), bleu (modification), rose (FAB).
- **Appui :** translate(3px, 3px), ombre réduite à 0 — effet enfoncé.
- **Variantes :** btn-plein (largeur 100 %, padding 13 px, 15.5 px), btn-petit (padding 10 px 14 px, 13 px, ombre 2 px, min-height 44 px).

### Pastilles de statut (chips)
- **Style :** pilule (999 px), bordure 2.5 px noire, inclinée de -1,5°.
- **Couleurs sémantiques :** vert Comestible · jaune Prudence · gris Immangeable · orange Toxique · rouge MORTEL ☠️ (texte blanc) · gris Inconnu ⚠️ (statut fail-safe : toute ambiguïté penche vers la prudence).
- **Filtres du guide :** deux `<select>` (Comestibilité + Saison) pleine largeur, style champ Memphis — remplacés les puces filtres (depuis v22).

### Cartes / Conteneurs
- **Coins :** 18 px avec coin cassé 5 px.
- **Fond :** blanc ; ombre dure 5 px ; bordure 3 px noire.
- **Padding interne :** 14 px. **Marges :** 16 px entre cartes.
- Variante item : disposition horizontale avec vignette (88 px) à rayures ambre/blanc séparée par une bordure noire.

### Champs de saisie
- **Style :** bordure noire 3 px, coins 12 px avec coin cassé 4 px, fond blanc, ombre interne subtile.
- **Focus :** anneau ambre 3 px (box-shadow externe).
- **Zone photo :** bordure pointillée noire 3 px, fond crème, icône 32 px.

### Navigation
- **Style :** barre fixe basse, fond blanc, bordure haute noire 3 px, icônes emoji 22 px + libellés 11.5 px en colonne.
- **Actif :** onglet relevé de 4 px, zigzag ambre au-dessus, couleur propre à chaque onglet (bleu canard / rouille / vert / rose).

### Alertes de sécurité
- **Style :** coins 16 px avec coin cassé 5 px, ombre 4 px, coin décoratif (cercle rayé rouge pour MORTEL, losange rouille pour prudence).
- **MORTEL :** fond saumon #F6DFD2, texte noir, mention du centre antipoison 1-800-463-5060 obligatoire.
- **Prudence :** fond crème doré #F4E3C3.

### Fiche hybride (checklist terrain)
- **Structure :** photo réelle (16:9, bordure basse noire 3 px) + corps (case ✓, titre, description) + verdict.
- **Carte de spécificité :** coins 18 px avec coin cassé 5 px, bordure noire 3 px, ombre dure 3 px, curseur pointer, appui scale(.96).
- **Case cochée :** fond olive, texte barré (line-through 2 px, opacité .75) — la satisfaction du critère vérifié.
- **Compteur :** pastille noire « n/5 » sur crème, à droite de l'en-tête de section (aria-live="polite").
- **Verdicts :** carte pleine largeur, bordure noire 3 px, coin cassé — ✅ vert (tous les critères) / ⚠️ ambre (critères manquants, « En cas de doute : on ne mange pas »).

### Étapes progressives (feuille variété)
- **But :** divulgation progressive — jamais plus de 5-6 champs à l'écran (règle « choix minimaux ≤ 4 »).
- **Barre :** deux pilules numérotées (1 Identité → 2 Détails & photo), bordure noire 2,5 px, ombre dure 2 px, transition transform/box-shadow .1 s.
- **Étape active :** fond ambre, inclinaison -1,5°, pastille numérotée rouge sur blanc ; étape inactive fond crème.
- **Sémantique :** `role="tablist"`/`tab`/`tabpanel"` + `aria-selected`/`aria-labelledby` ; focus déplacé sur le premier champ à chaque bascule ; validation du nom avant l'étape 2.
- **Encart d'aide :** fond blanc à rayures ambre 45° (zigzag d'aide), bordure noire 3 px, coins cassés — distinct de l'alerte de prudence (losange rouille réservé aux alertes de sécurité).

## Do's and Don'ts

### Do :
- **Do** utiliser la bordure noire 3 px sur toute surface colorée (La Règle du Trait Noir).
- **Do** casser un coin sur les cartes, champs et feuilles (inférieur droit, 4-6 px).
- **Do** incliner les titres et pastilles de -1 à -2°.
- **Do** enfoncer les éléments au clic (translate + ombre réduite).
- **Do** réserver le rouge au danger et à la destruction.
- **Do** garder l'élasticité des feuilles et confirmations (le rebond fait partie du plaisir).

### Don't :
- **Don't** utiliser d'ombre douce ou floutée (La Règle du Décalage Net).
- **Don't** utiliser de boîte système navigateur (confirm/alert) — toujours les modales Memphis.
- **Don't** utiliser d'uppercase forcé ni de graisse inférieure à 400.
- **Don't** afficher une alerte MORTEL sans le centre antipoison 1-800-463-5060.
- **Don't** introduire de couleur hors palette sans la documenter (les onglets actifs, le dégradé header, les fonds d'alertes et la barre vide sont déjà documentés — toute nouvelle dérive doit l'être aussi).
