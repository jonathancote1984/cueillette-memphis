# Design

> **Wiki Cueillette Québec — édition Memphis** · [Accueil du dépôt](../README.md) ·
> [Index du wiki](README.md)

Cette page est la synthèse du système de design. La **source de vérité** complète (tokens,
composants, do/don't) est [../DESIGN.md](../DESIGN.md) : en cas de divergence, c'est ce
fichier qui a raison.

## Sommaire

- [Intention](#intention)
- [Palette automne/terre](#palette-automneterre)
- [Typographie](#typographie)
- [Tokens de forme et d'espacement](#tokens-de-forme-et-despacement)
- [Règles nommées](#règles-nommées)
- [Composants clés](#composants-clés)
- [Mise en page](#mise-en-page)
- [Do et don't](#do-et-dont)

## Intention

**Étoile du Nord créative : « La Récolte » — l'énergie d'une belle journée de cueillette,
panier plein.**

L'interface est un carnet de chasse chaleureux et tactile, exécuté en style Memphis :
bordures noires épaisses, coins cassés, ombres dures sans flou, formes géométriques
flottantes, zigzag d'en-tête, pois au fond, titres légèrement inclinés. Le ludisme est
assumé, y compris dans les rebonds élastiques des feuilles.

La palette n'est pas celle du Memphis des années 1980 (rose/cyan/jaune primaire) : c'est
celle de **l'automne québécois** — ambre, rouille, terracotta, olive, cuir sur crème.

## Palette automne/terre

| Rôle | Nom | Code | Usage |
|---|---|---|---|
| Accent principal | Ambre | `#D9A441` | boutons jaunes, puces actives, titres de feuille, zigzag |
| Signal | Rouille | `#B45309` | alertes de prudence, onglet Identifier actif |
| Énergie | Terracotta | `#B94527` | FAB, carte « Dernière sortie », onglet Stats actif |
| Confiance | Olive | `#6F8F3E` | badges Comestible, boutons d'identification photo |
| Action secondaire | Cuir | `#8A5A2B` | boutons Modifier, titres de section du guide |
| Fond | Crème | `#F3E8D5` | fond général et pois |
| Surfaces | Blanc chaud | `#FDF6E7` | cartes, feuilles, champs |
| Trait et texte | Noir | `#241A0F` | bordures, texte principal, toasts |
| Danger | Rouge | `#B3261E` | badges MORTEL, suppression, pastille compteur |
| Neutre | Gris | `#A89882` | boutons Retour, filtre « Tous », badge Immangeable |

Couleurs de service documentées (ne pas en ajouter sans les inscrire dans
[../DESIGN.md](../DESIGN.md)) : bleu canard `#0B6E96` et rose `#C2185B` (onglets actifs),
rouille d'onglet `#B3540B`, vert de mesure `#0B7A55`, brun tabac `#7A5C2E`, brun d'en-tête
`#C87224`, fonds d'alerte `#F6DFD2` (rouge) et `#F4E3C3` (orange), barre vide `#D8C9AC`.

Le manifeste PWA est aligné sur la palette : `theme_color` ambre `#D9A441`,
`background_color` crème `#F3E8D5`.

## Typographie

**Fredoka**, auto-hébergée (`fonts/fredoka.woff2` — aucun appel à Google Fonts), avec repli
`'Segoe UI', system-ui, sans-serif`. Une seule famille du titre au corps ; la hiérarchie
passe par le poids (400 à 700) et la taille.

| Niveau | Taille | Poids | Interlignage | Note |
|---|---|---|---|---|
| Display (H1 d'en-tête) | 21 px | 700 | 1.1 | incliné de -1,5° |
| Titre de vue | 20 px | 700 | 1.2 | pastille blanche cerclée de noir, -1° |
| Titre de feuille | 18 px | 700 | 1.2 | pastille ambre, -1° |
| Corps | 16 px | 400 | 1.65 | descriptions, fiches |
| Label de champ | 13 px | 700 | 1.4 | libellés de formulaire |
| Meta | 12,5 px | 400 | 1.5 | opacité 0,85 — ne pas descendre sous 0,8 (contraste AA) |

Pas d'uppercase forcé, pas de césure, `tabular-nums` sur les mesures et les compteurs pour
garder les colonnes stables.

## Tokens de forme et d'espacement

| Token | Valeurs |
|---|---|
| Arrondis | `sm` 8 px · `md` 12 px · `lg` 18 px · `xl` 24 px · pilules 999 px |
| Espacements | `xs` 4 · `sm` 8 · `md` 12 · `lg` 16 · `xl` 24 (px) |
| Bordures | 3 px noir (2,5 px sur les pastilles) |
| Ombres | décalage 2 à 6 px, noir pur, **sans flou** |
| Élasticité | `cubic-bezier(.2, 1.3–1.6, .4, 1)` à l'apparition ; sortie en `ease-out` |

## Règles nommées

- **La Règle du Trait Noir** — toute surface colorée porte une bordure noire de 3 px. Sans le
  trait, la couleur n'est pas un élément de l'interface.
- **La Règle du Rouge Mortel** — le rouge n'apparaît que pour le danger (MORTEL, suppression,
  compteur), jamais pour la décoration.
- **La Règle du Décalage Net** — jamais de `box-shadow` avec flou ; une ombre est un décalage
  net de 2 à 6 px.
- **La Règle de l'Inclinaison** — un titre n'est jamais parfaitement droit : -1 à -2°,
  jamais plus.

## Composants clés

- **Boutons** — pilules, bordure 3 px, ombre dure 3 px ; couleur selon l'action (ambre par
  défaut, olive pour l'identification photo, rouge pour la destruction, cuir pour la
  modification, terracotta pour le FAB). À l'appui : `translate(3px, 3px)` et ombre réduite,
  effet « bouton qu'on enfonce ». Cibles tactiles ≥ 44 px.
- **Pastilles de statut** — pilules inclinées de -1,5° : olive Comestible, ambre Prudence,
  gris Immangeable, orange Toxique, rouge MORTEL ☠️, gris Inconnu ⚠️.
- **Cartes** — coins 18 px avec **un coin cassé** à 5 px, fond blanc chaud, ombre dure 5 px.
  Variante « item » avec vignette de 88 px à rayures ambre et blanc.
- **Champs de saisie** — bordure 3 px, coins 12 px avec coin cassé 4 px, anneau ambre 3 px au
  focus. Zone photo en pointillé sur fond crème.
- **Feuilles glissantes** — max 84 vh, coins hauts 24 px, poignée de fermeture, entrée
  élastique, garde-fou sur les champs modifiés.
- **Navigation** — barre fixe basse, 5 onglets, onglet actif relevé de 4 px avec zigzag
  ambre et couleur propre.
- **Alertes de sécurité** — coin décoratif (cercle rayé rouge pour MORTEL, losange rouille
  pour la prudence) ; fond saumon `#F6DFD2` ou crème doré `#F4E3C3` ; la mention du centre
  antipoison est **obligatoire** sur une alerte mortelle.
- **Fiche hybride (checklist terrain)** — photo 16:9, case ✓, titre, description, compteur
  « n/5 » en pastille noire (`aria-live="polite"`), verdict pleine largeur ✅ / ⚠️ / ☠️.
- **Étapes progressives** — deux pilules numérotées (Identité → Détails et photo), sémantique
  `tablist`/`tab`/`tabpanel`, focus déplacé sur le premier champ à chaque bascule ; jamais
  plus de 5 à 6 champs à l'écran.

## Mise en page

Colonne unique centrée, largeur maximale 640 px. En-tête collant avec zigzag et formes SVG
flottantes ; barre de navigation fixe en bas ; FAB circulaire au-dessus de la barre, masqué
en Stats, en Paramètres et en vue détaillée. Rythme d'espacement 4/8/12/16/24 px, 16 px entre
les cartes. Grille de 2 colonnes pour les paires de boutons et les cartes de stats.

## Do et don't

**Do**

- bordure noire de 3 px sur toute surface colorée ;
- casser un coin (inférieur droit, 4 à 6 px) sur cartes, champs et feuilles ;
- incliner titres et pastilles de -1 à -2° ;
- enfoncer les éléments au clic ;
- réserver le rouge au danger et à la destruction ;
- garder l'élasticité des feuilles et des confirmations.

**Don't**

- pas d'ombre douce ou floutée ;
- pas de boîte système du navigateur (`confirm`, `alert`) — modales Memphis seulement ;
- pas d'uppercase forcé ni de graisse sous 400 ;
- pas d'alerte MORTEL sans le centre antipoison **1-800-463-5060** ;
- pas de couleur hors palette sans la documenter dans [../DESIGN.md](../DESIGN.md).

Voir aussi : [../DESIGN.md](../DESIGN.md) · [../PRODUCT.md](../PRODUCT.md) ·
[archive/](archive/) pour l'historique des revues de design
