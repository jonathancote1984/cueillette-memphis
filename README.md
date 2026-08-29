# Cueillette Québec — édition Memphis

[![App en ligne sur GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-en%20ligne-D9A441?style=flat-square&labelColor=241A0F)](https://jonathancote1984.github.io/cueillette-memphis/)
[![PWA hors-ligne](https://img.shields.io/badge/PWA-100%20%25%20hors--ligne-6F8F3E?style=flat-square&labelColor=241A0F)](docs/installation.md)
[![Sans build](https://img.shields.io/badge/build-aucun%20%C2%B7%20statique-8A5A2B?style=flat-square&labelColor=241A0F)](docs/deploiement.md)

**App en ligne : <https://jonathancote1984.github.io/cueillette-memphis/>**

Carnet de cueillette de champignons du Québec et guide d'identification, livré comme
application web installable (PWA) qui fonctionne à 100 % hors-ligne, en forêt, sans réseau.
Pas de compte, pas de serveur applicatif : les données restent sur l'appareil.

## Sommaire

- [Présentation](#présentation)
- [Fonctionnalités](#fonctionnalités)
- [Design](#design)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Sécurité](#sécurité)
- [Licence et droits des photos](#licence-et-droits-des-photos)
- [Structure du dépôt](#structure-du-dépôt)
- [Documentation (wiki)](#documentation-wiki)

## Présentation

L'app est un carnet de chasse personnel : elle sert à retrouver ses coins secrets (GPS),
journaliser ses récoltes (poids, météo, photo), consulter un guide de 21 espèces du Québec
et vérifier une identification sur le terrain à l'aide d'une liste de critères à cocher.

Caractéristiques techniques principales :

- PWA statique **mono-fichier** : toute l'app tient dans `index.html` (≈ 185 Ko), sans
  framework et sans étape de compilation.
- Service worker `sw.js` en stratégie *cache-first* : l'app, les icônes, la police et les
  121 photos embarquées sont disponibles hors-ligne dès la première visite.
- Données locales seulement : IndexedDB `cqm_bd` (version 5) avec repli `localStorage`.
- Fonctions d'IA **facultatives** (Google Gemini), activées uniquement si l'utilisateur
  colle sa propre clé API dans les paramètres.

## Fonctionnalités

| Onglet | Ce qu'il fait |
|---|---|
| **Spots** | Coins de cueillette : nom, description, GPS avec précision affichée, photo, espèces attendues, lien Google Maps, partage (Web Share API avec repli presse-papiers). |
| **Identifier** | Guide de 21 espèces du Québec (saison, habitat, description, caractéristiques, confusions dangereuses), recherche, filtres comestibilité et saison, fiches à checklist terrain, identification par photo (IA), variétés personnelles. |
| **Cueillettes** | Journal : date, espèce (suggestions ou saisie libre), poids en kg ou lb, spot lié, météo, note, photo. |
| **Stats** | Total récolté, nombre de sorties, espèces distinctes, dernière sortie, tops espèces et spots, barres mensuelles. Contient aussi l'export/import et l'effacement complet. |
| **Paramètres** | Unités kg/lb, clé API Gemini, ordre de priorité des sources d'images, crédits photos, rappel de la méthode d'identification. |

Détail complet : [docs/fonctionnalites.md](docs/fonctionnalites.md).

## Design

Style Memphis assumé, sur une **palette automne/terre** — la forêt québécoise en septembre.

| Rôle | Nom | Code |
|---|---|---|
| Accent principal | Ambre | `#D9A441` |
| Signal | Rouille | `#B45309` |
| Énergie (FAB, accents) | Terracotta | `#B94527` |
| Confiance (comestible) | Olive | `#6F8F3E` |
| Action secondaire | Cuir | `#8A5A2B` |
| Fond | Crème | `#F3E8D5` |
| Surfaces | Blanc chaud | `#FDF6E7` |
| Trait et texte | Noir | `#241A0F` |
| Danger absolu | Rouge | `#B3261E` |

Règles structurantes : bordure noire de 3 px sur toute surface colorée, ombres dures sans
flou (décalage 3 à 6 px), un coin cassé par carte, titres inclinés de -1 à -2°, typographie
Fredoka auto-hébergée (`fonts/fredoka.woff2`), rouge réservé au danger et à la destruction.

Le système de design complet (tokens, composants, do/don't) est dans
[DESIGN.md](DESIGN.md) ; la synthèse orientée wiki est dans [docs/design.md](docs/design.md).

## Installation

### Héberger sur GitHub Pages

1. Pousser le dépôt sur GitHub (branche `main`).
2. *Settings → Pages → Build and deployment* : source **Deploy from a branch**, branche
   `main`, dossier `/ (root)`.
3. L'app est servie à `https://<utilisateur>.github.io/<dépôt>/` — ici
   <https://jonathancote1984.github.io/cueillette-memphis/>.

Aucun réglage supplémentaire : tous les chemins de l'app sont relatifs (`./index.html`,
`./img/...`), donc le sous-dossier de Pages fonctionne tel quel.

### Ajouter à l'écran d'accueil

Ouvrir l'adresse dans Chrome (Android) ou Safari (iOS), puis
**menu → « Ajouter à l'écran d'accueil »**. L'app s'ouvre ensuite en plein écran
(`display: standalone`), en orientation portrait, et fonctionne sans réseau.

### Servir en local

```bash
python3 -m http.server 8091     # puis http://localhost:8091
# ou
npx serve -l 8091
```

Le service worker exige `https://` ou `localhost` : `file://` ne fonctionne pas.

Procédure détaillée, mise à jour du cache `cqm-vN` et dépannage :
[docs/installation.md](docs/installation.md).

## Utilisation

1. **Noter un spot** : onglet Spots → bouton flottant 📍 → nom, GPS (bouton de
   localisation), photo, espèces attendues.
2. **Identifier** : onglet Identifier → chercher ou filtrer une espèce → ouvrir la fiche →
   cocher les 5 critères (chapeau, hyménium, pied, chair et odeur, habitat) devant le
   champignon réel. Le verdict n'est jamais vert avant que tous les critères concordent, et
   jamais vert sur une espèce non comestible.
3. **Identifier par photo** (facultatif, requiert une clé Gemini) : bouton d'identification
   photo → appareil ou galerie → l'IA propose une espèce avec un niveau de confiance. Le
   guide a toujours le dernier mot sur le statut de comestibilité.
4. **Journaliser** : onglet Cueillettes → date, espèce, poids, spot, météo, note, photo.
5. **Sauvegarder** : onglet Stats → *Exporter* (fichier JSON complet) ; *Importer* remplace
   toutes les données après confirmation chiffrée.

Guide d'utilisation de l'identification : [docs/guide-identification.md](docs/guide-identification.md).

## Sécurité

L'app est un outil d'aide à la décision, **pas** un avis mycologique. Elle ne remplace ni un
expert ni un cours d'identification.

- **En cas de doute, on ne mange pas.**
- **Centre antipoison du Québec : 1-800-463-5060** (affiché dans l'app avec chaque alerte
  mortelle et à chaque verdict incertain).
- Statuts possibles : comestible, prudence, immangeable, toxique, **MORTEL**, et `inconnu`
  quand l'information est incertaine — le doute penche toujours du côté prudent.
- Cinq espèces mortelles sont documentées dans le guide, dont deux sosies de comestibles
  recherchés (gyromitre/morille, galerine/pleurote).

Voir [docs/securite-alimentaire.md](docs/securite-alimentaire.md) pour les règles complètes
et [docs/donnees-confidentialite.md](docs/donnees-confidentialite.md) pour la sécurité des
données (clé API, photos, import/export).

## Licence et droits des photos

- **Code** : projet personnel, aucune licence explicite n'est déclarée dans le dépôt. Sans
  fichier `LICENSE`, tous droits réservés par défaut — ajouter une licence si le code doit
  être réutilisé.
- **Photos** : les 21 photos d'espèces (`img/especes/`) et les 100 photos de spécificités
  (`img/specs/`) proviennent de **Wikimedia Commons**, sous licences libres (CC0, CC BY,
  CC BY-SA). Auteur, licence et page source sont conservés dans
  `img/especes/credits.json` et `img/specs/credits.json`, et affichés dans l'app
  (Paramètres → Crédits photos).
- **Miniatures MycoQuébec** : `img/mycoquebec.json` référence des vignettes distantes de
  mycoquebec.org utilisées pour l'autocomplétion ; elles ne sont pas redistribuées dans le
  dépôt et ne sont jamais mises en cache.

Détail et état des crédits : [docs/licences-credits.md](docs/licences-credits.md).

## Structure du dépôt

| Chemin | Rôle |
|---|---|
| `index.html` | L'application complète (HTML, CSS, JS — aucune dépendance externe). |
| `sw.js` | Service worker hors-ligne ; **incrémenter `cqm-vN` à chaque mise à jour**. |
| `manifest.json` | Manifeste PWA (nom, icônes, `theme_color` ambre, portrait, standalone). |
| `fonts/fredoka.woff2` | Police auto-hébergée (aucun appel à Google Fonts). |
| `icons/` | Icônes PWA 192/512 et maskable. |
| `generer_icones.py` | Régénère les icônes (Pillow). |
| `img/especes/` | 21 photos d'espèces + `credits.json`. |
| `img/specs/` | 100 photos de spécificités (21 espèces × 5 critères) + `credits.json`. |
| `img/mycoquebec.json` | Base d'autocomplétion (3 938 entrées latin / nom français / miniature). |
| `scripts/telecharger_photos.py` | Re-télécharge les photos depuis Wikimedia Commons. |
| `DESIGN.md` | Système de design complet (source de vérité visuelle). |
| `PRODUCT.md` | Vérité produit : usagers, contexte, contraintes, principes. |
| `docs/` | Wiki de documentation + rapports d'audit et archives. |

## Documentation (wiki)

Point d'entrée : **[docs/README.md](docs/README.md)**

- [Installation](docs/installation.md) — GitHub Pages, écran d'accueil, serveur local, cache `cqm-vN`
- [Fonctionnalités](docs/fonctionnalites.md) — spots, identification, cueillettes, stats, sauvegarde
- [Guide d'identification](docs/guide-identification.md) — les 21 espèces, checklist terrain, IA
- [Sécurité alimentaire](docs/securite-alimentaire.md) — badges, verdicts, antipoison, anti-injection
- [Données et confidentialité](docs/donnees-confidentialite.md) — IndexedDB, clé Gemini, photos, export/import
- [Design](docs/design.md) — style Memphis, palette automne/terre, tokens
- [Déploiement](docs/deploiement.md) — publication, bump du cache, vérifications
- [Licences et crédits](docs/licences-credits.md) — photos Wikimedia, attribution
- [Contribution](docs/contribution.md) — conventions, checklist avant commit
- [Journal des versions](docs/changelog.md) — grandes itérations du projet
