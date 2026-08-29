# Données et confidentialité

> **Wiki Cueillette Québec — édition Memphis** · [Accueil du dépôt](../README.md) ·
> [Index du wiki](README.md)

## Sommaire

- [Principe](#principe)
- [Où vivent les données](#où-vivent-les-données)
- [Photos : ré-encodage local](#photos--ré-encodage-local)
- [Clé API Gemini](#clé-api-gemini)
- [Ce qui sort de l'appareil](#ce-qui-sort-de-lappareil)
- [Export et import JSON (version 5)](#export-et-import-json-version-5)
- [Validations à l'import](#validations-à-limport)
- [Effacer ses données](#effacer-ses-données)
- [Sauvegarde : ce qu'il faut savoir](#sauvegarde--ce-quil-faut-savoir)

## Principe

L'app n'a **pas de serveur applicatif ni de compte utilisateur**. Tout ce que vous notez
(spots, coordonnées GPS, photos, récoltes, notes) reste dans le navigateur de l'appareil.
Aucune donnée n'est transmise sans une action explicite de votre part.

## Où vivent les données

**IndexedDB — base `cqm_bd`, version 5** (repli automatique sur `localStorage` si IndexedDB
n'est pas disponible) :

| Store | Contenu |
|---|---|
| `spots` | coins de cueillette : nom, description, GPS, photo, espèces attendues |
| `cueillettes` | journal : date, espèce, poids (toujours en kg), spot, météo, note, photo |
| `especes` | variétés personnelles |
| `caches` | identifiants des espèces masquées |
| `supprimees` | identifiants des espèces d'origine supprimées définitivement |
| `illustrations` | images des 5 spécificités par espèce (générées ou trouvées) |
| `checklist` | cases cochées des vérifications terrain |

**`localStorage`** — préférences seulement :

| Clé | Contenu |
|---|---|
| `cqm_unite` | `kg` ou `lb` |
| `cqm_cle_ia` | clé API Gemini (texte, en clair, sur l'appareil) |
| `cqm_ordre_images` | ordre de priorité des sources d'images |
| `cqm_exporte` | date du dernier export, pour le rappel de sauvegarde |

**Caches du service worker** — nommés `cqm-vN` : l'app, le manifeste, les icônes, la police
et les 121 photos embarquées. Aucune donnée personnelle ne s'y trouve.

## Photos : ré-encodage local

Toute photo ajoutée (spot, cueillette, variété) passe par la fonction `compresser()` :

1. lecture du fichier en `data:` URL ;
2. redessin dans un `<canvas>` avec un côté maximal de **900 px** ;
3. ré-encodage en **JPEG qualité 0,72** ;
4. stockage du résultat dans IndexedDB.

Conséquence utile pour la confidentialité : le ré-encodage par canvas **ne recopie pas les
métadonnées EXIF** de l'original (dont les coordonnées GPS de l'appareil et le modèle du
téléphone). La photo conservée est une image nue.

Les coordonnées GPS d'un spot, elles, sont enregistrées volontairement — c'est le but de la
fonction — et se retrouvent dans l'export JSON. Un export partagé partage donc vos coins.

## Clé API Gemini

- Saisie dans **Paramètres → Clé API Gemini** (champ masqué), obtenue gratuitement sur
  `aistudio.google.com/apikey`.
- Stockée **uniquement** dans `localStorage`, sur l'appareil. Elle n'est jamais poussée vers
  un serveur du projet — il n'y en a pas.
- Transmise à Google **en en-tête HTTP** `x-goog-api-key`, jamais dans l'URL (elle ne finit
  donc pas dans des journaux d'accès ou l'historique).
- Le service worker n'entre **jamais en cache** les requêtes vers `googleapis.com`,
  `wikimedia.org`, `mycoquebec.org`, ni aucune URL contenant `key=`.
- La clé **n'est pas incluse dans l'export JSON**.
- Elle peut être effacée en un bouton (Paramètres → Effacer).

Sans clé, l'app fonctionne au complet sauf l'identification par photo et la génération de
fiches ou d'illustrations par IA.

## Ce qui sort de l'appareil

L'app n'établit que trois types de connexions sortantes, toutes déclenchées par une action de
l'utilisateur, et toutes déclarées dans la politique de sécurité du contenu (CSP) de la page :

| Destination | Quand | Ce qui est envoyé |
|---|---|---|
| `generativelanguage.googleapis.com` | identification par photo, génération de fiche ou d'illustration | la photo choisie ou le nom de l'espèce, plus la clé API en en-tête |
| `commons.wikimedia.org` | recherche d'une photo libre pour une variété perso | le terme de recherche (nom de l'espèce, partie visée) |
| `mycoquebec.org` | miniatures d'autocomplétion (images distantes) | une requête d'image |

La CSP restreint également les sources de scripts, de styles, de polices (`self`) et interdit
les objets embarqués (`object-src 'none'`). Les images sont limitées à `self`, `data:` et
`https:`.

Aucune analytique, aucun traceur, aucun cookie applicatif.

## Export et import JSON (version 5)

L'export produit un fichier JSON téléchargé localement :

```json
{
  "app": "cueillette-quebec-memphis",
  "version": 5,
  "exporteLe": "2026-08-28T14:03:00.000Z",
  "spots": [],
  "cueillettes": [],
  "especes": [],
  "illustrations": [],
  "cachees": [],
  "supprimees": [],
  "tombes": [],
  "checklist": []
}
```

- `tombes` conserve le nom, le latin, le statut et la prudence des espèces supprimées : c'est
  ce qui permet au filet de sécurité de survivre sur le téléphone d'un proche.
- Les photos sont incluses en `data:` URL — un export avec beaucoup de photos peut peser
  plusieurs mégaoctets.
- La clé API et les préférences d'affichage ne sont pas exportées.

L'import affiche un résumé chiffré (cueillettes, spots, variétés) et demande une
confirmation, car il **remplace toutes les données**. Un avertissement supplémentaire
apparaît si le fichier vient d'une version plus récente (format inconnu) ou plus ancienne
(la checklist terrain sera perdue).

## Validations à l'import

L'import est traité comme une entrée non fiable :

| Contrôle | Comportement |
|---|---|
| Forme du fichier | `spots` et `cueillettes` doivent être des tableaux, sinon rejet |
| Identifiants | doivent respecter `^[A-Za-z0-9_-]{1,64}$` ; sinon régénérés et les références re-pointées |
| Statuts | liste blanche `comestible`, `immangeable`, `toxique`, `mortel`, `inconnu` ; toute autre valeur devient `inconnu` — **jamais** `comestible` |
| URL d'images | acceptées seulement en `data:image/(jpeg\|png\|webp);base64,`, chemin local `img/...` ou `https://` ; le reste est écarté |
| Types | poids numérique fini, dates et textes forcés en chaînes |
| Transaction | l'état antérieur est sauvegardé puis **restauré intégralement** si l'import échoue |

## Effacer ses données

- **Paramètres → Effacer** pour la seule clé API.
- **Stats → Tout effacer** (double confirmation) vide tous les stores : spots, cueillettes,
  variétés, illustrations, masquages, suppressions, checklist.
- Effacer les données du site dans le navigateur, ou désinstaller la PWA, supprime aussi
  IndexedDB et `localStorage`.

## Sauvegarde : ce qu'il faut savoir

Il n'y a **aucune copie ailleurs**. Si l'appareil est perdu, réinitialisé, ou si les données
du site sont effacées, tout est perdu sauf ce qui a été exporté.

Bonnes pratiques :

1. Exporter après chaque bonne sortie (l'app rappelle quand l'export vieillit).
2. Conserver le fichier ailleurs que sur le téléphone (ordinateur, disque, nuage personnel).
3. Vérifier une fois par saison qu'un import du dernier fichier fonctionne, sur un appareil
   de test ou après un export frais.
4. Se rappeler qu'un export **contient les coordonnées GPS des spots** : à ne pas partager à
   la légère.

Voir aussi : [Sécurité alimentaire](securite-alimentaire.md) · [AUDIT_SECU.md](AUDIT_SECU.md)
· [Installation](installation.md)
