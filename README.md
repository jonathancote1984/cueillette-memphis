# 🍄 Cueillette Québec — édition Memphis

**App en ligne : https://jonathancote1984.github.io/cueillette-memphis/**

Version **refaite de zéro** (design + code) de l'app de cueillette de champignons, dans un
style **Memphis ludique** : couleurs vives, formes géométriques, zigzags, pois, bordures
épaisses noires et ombres dures. 100 % hors-ligne (PWA), aucune dépendance au code du
Carnet de Pêche ni à Android natif.

## Fonctionnalités (identiques à l'édition classique)

- **📍 Spots** — vos coins secrets : nom, description, GPS (précision affichée), photo,
  lien Google Maps.
- **🍄 Identifier** — guide de 21 champignons du Québec : saison, habitat, caractéristiques,
  confusions dangereuses, badges comestible / prudence / immangeable / toxique / **MORTEL**.
- **🧺 Cueillettes** — date, espèce (suggestions + libre), poids kg, spot lié, météo, notes, photo.
- **📊 Stats** — total récolté, sorties, espèces, tops, barres mensuelles multicolores.
- **💾 Sauvegarde** — export/import JSON complet.

## Design Memphis

- Palette : crème + rouge / jaune / bleu / rose / vert vifs, contours noirs épais.
- Bordures 3 px, ombres dures (sans flou), coins cassés, titres légèrement inclinés.
- Motifs : pois, rayures, zigzag d'en-tête, formes géométriques flottantes (SVG).
- Typographie arrondie (Fredoka) avec repli système.
- Formulaires en **feuilles glissantes** (bottom sheets), bouton flottant (FAB) coloré.

## Installation (téléphone)

Identique à l'édition classique : hébergez sur GitHub Pages (ou `npx serve -l 8091`),
ouvrez dans Chrome → « Ajouter à l'écran d'accueil ».

## Fichiers

| Fichier | Rôle |
|---|---|
| `index.html` | L'application complète (design Memphis + logique réécrite) |
| `manifest.json` | Configuration PWA |
| `sw.js` | Service worker hors-ligne (bump `cqm-vN` à chaque mise à jour) |
| `icons/` | Icônes Memphis (jaune à pois + champignon rouge) |
| `generer_icones.py` | Régénère les icônes (Pillow) |
| `img/especes/` | Photos des 21 espèces (pré-cachées par le SW, offline) |
| `scripts/telecharger_photos.py` | Re-télécharge les photos depuis Wikimedia Commons |

## 🧪 Gérer vos variétés + IA

**Onglet Identifier** → bouton rose `＋` :
- **Ajouter / modifier / supprimer** vos variétés (badge « ⭐ perso » dans le guide). Les
  21 espèces d'origine peuvent être masquées (bouton ↩️ pour les restaurer).
- **✨ Détails par IA** : entrez le nom (latin de préférence) → l'IA (Gemini) génère la
  fiche complète : description, caractéristiques, confusions, saison, habitat,
  comestibilité. **Clé gratuite** : aistudio.google.com/apikey → section « 🔑 Clé Gemini »
  dans la feuille d'ajout. La clé reste sur votre téléphone.
- **🔎 Chercher une photo** : trouve automatiquement une photo libre sur Wikimedia
  Commons et l'embarque (hors-ligne). **🎨 Illustration IA** : tente une génération
  d'image (selon les capacités de votre clé).

Vos variétés sont stockées localement (IndexedDB) et incluses dans l'export JSON.

## 📷 Photos des champignons

Chaque espèce du guide affiche une photo réelle (vignette + grande image dans le détail),
téléchargée depuis **Wikimedia Commons** et embarquée localement (`img/especes/`) — l'app
fonctionne donc à 100 % hors-ligne, photos comprises, dès la première installation.

Les **crédits d'attribution** (auteur, licence, page source) de chaque photo sont dans
`img/especes/credits.json`, conformément aux licences libres (CC BY-SA, CC0…).

## Sécurité

Guide informatif — ne remplace pas un expert. En cas de doute, on ne mange pas.
Centre antipoison Québec : **1-800-463-5060**.
