# Fonctionnalités

> **Wiki Cueillette Québec — édition Memphis** · [Accueil du dépôt](../README.md) ·
> [Index du wiki](README.md)

## Sommaire

- [Navigation générale](#navigation-générale)
- [Spots](#spots)
- [Identifier](#identifier)
- [Cueillettes](#cueillettes)
- [Stats](#stats)
- [Sauvegarde : export et import](#sauvegarde--export-et-import)
- [Paramètres](#paramètres)
- [Ce que l'app ne fait pas](#ce-que-lapp-ne-fait-pas)

## Navigation générale

Cinq onglets dans une barre fixe au bas de l'écran : **Spots**, **Identifier**,
**Cueillettes**, **Stats**, **Paramètres**. L'onglet actif est relevé, souligné d'un zigzag
ambre et porte `aria-current="page"`.

Un bouton flottant (FAB) en bas à droite déclenche l'action principale de l'écran courant :
📍 en Spots, ＋ ailleurs. Il est masqué en Stats, en Paramètres et dans une fiche détaillée.

Les formulaires s'ouvrent en **feuilles glissantes** (bottom sheets) avec poignée. Un
garde-fou détecte les champs modifiés : fermer par le voile, la poignée ou `Échap` demande une
confirmation au lieu de jeter la saisie. Aucune boîte système du navigateur n'est utilisée :
confirmations et choix passent par des modales Memphis.

## Spots

Enregistrement des coins de cueillette.

- Nom, description libre.
- **GPS** : bouton de localisation qui affiche la précision obtenue (« ± 12 m ») ; saisie
  manuelle des coordonnées possible si le GPS n'est pas disponible.
- Photo du lieu (appareil ou galerie).
- **Espèces attendues** : sélection multiple, affichée en puces sur la carte du spot.
- Lien **Google Maps** généré à partir des coordonnées.
- **Partage** : Web Share API quand elle existe, sinon copie du texte dans le
  presse-papiers.
- Modification et suppression avec confirmation.

## Identifier

L'onglet le plus riche. Il combine un guide de référence, une méthode de vérification
terrain et deux fonctions d'IA facultatives.

### Guide des 21 espèces

- Recherche par nom (français ou latin), avec anti-rebond.
- Deux filtres en listes déroulantes : **comestibilité** et **saison**.
- Chaque espèce affiche une vignette locale (les 21 photos sont embarquées, donc
  disponibles hors-ligne) et une pastille de statut : comestible, prudence, immangeable,
  toxique, **MORTEL**, ou inconnu.

Répartition du guide : 10 comestibles (dont 2 à cuisson obligatoire), 1 immangeable,
5 toxiques, 5 mortelles. Liste complète dans
[Guide d'identification](guide-identification.md).

### Fiche d'espèce

- Photo, nom français, nom latin, statut, saison, habitat, description.
- **Confusions dangereuses** explicitement nommées.
- **Checklist terrain** : 5 spécificités (chapeau ; hyménium — lames, tubes ou aiguillons ;
  pied ; chair et odeur ; habitat), chacune avec une photo réelle et la description de ce
  qu'il faut observer. Les cases cochées sont persistées localement (store `checklist`),
  avec compteur « n/5 » et verdict.
- Alerte rouge non négociable sur les espèces mortelles, avec le numéro du centre
  antipoison.
- Bouton pour masquer l'espèce (elle peut être restaurée) ou la supprimer définitivement
  (double confirmation).

### Identification par photo (IA, facultatif)

- Photo prise sur place ou choisie dans la galerie, envoyée à Gemini avec un prompt
  d'identification structuré.
- Retour : espèce probable, nom latin, statut, **niveau de confiance**, description,
  5 caractéristiques observables, confusions à éviter.
- Seuils : ≥ 90 % « fiable », 60 à 89 % « à vérifier », en dessous ou espèce inconnue
  → aucune confiance accordée.
- **Le guide a le dernier mot** : si l'espèce proposée correspond à une espèce du guide (ou
  à un de ses synonymes), le statut le plus grave gagne toujours. Une espèce absente du
  guide ne reçoit jamais un badge vert seul : une alerte « Espèce absente du guide »
  l'accompagne.
- L'analyse peut être annulée en fermant la feuille.

### Variétés personnelles

- Ajout, modification, suppression de vos propres espèces, marquées « perso » dans le guide.
- Feuille en **2 étapes** : (1) Identité — nom français, latin, comestibilité, saison,
  prudence ; (2) Détails et photo — habitat, description, caractéristiques, confusions,
  photos des 5 spécificités.
- **Autocomplétion MycoQuébec** sur le nom français (base embarquée `img/mycoquebec.json`,
  3 938 entrées) : le nom latin se remplit automatiquement.
- **Détails par IA** : génération de la fiche complète à partir du nom (latin de
  préférence).
- **Illustrations** : recherche d'une photo libre par spécificité, selon l'ordre de sources
  choisi dans les paramètres (MycoQuébec, Wikimedia, IA — 6 combinaisons).
- Les espèces d'origine masquées ou supprimées laissent une « tombe » : leurs signaux de
  sécurité continuent de s'appliquer aux cueillettes déjà journalisées.

## Cueillettes

Journal des sorties.

- Date, espèce (suggestions du guide et des variétés perso, ou saisie libre), poids, spot
  lié, météo, note, photo.
- Poids saisi en kg ou en lb selon les paramètres ; la virgule décimale est acceptée
  (`1,5`). Le stockage se fait **toujours en kg**, la conversion est faite à l'affichage et
  à la saisie.
- Les badges de sécurité de l'espèce sont affichés sur l'entrée du journal, y compris si
  l'espèce a été masquée ou supprimée depuis.

## Stats

- Quatre cartes : **Total récolté**, **Sorties**, **Espèces** distinctes, **Dernière
  sortie**.
- Tops espèces et tops spots.
- Barres mensuelles de récolte, avec chiffres à chasse fixe (colonnes stables).
- Toutes les mesures respectent l'unité choisie.

## Sauvegarde : export et import

Dans l'onglet **Stats**, carte de sauvegarde.

- **Exporter** : télécharge un fichier JSON complet (version 5) contenant spots,
  cueillettes, variétés perso, illustrations, espèces masquées, espèces supprimées, tombes
  et checklist. Un rappel s'affiche quand l'export devient vieux.
- **Importer** : remplace **toutes** les données, après un résumé chiffré (nombre de
  cueillettes, spots, variétés) et confirmation. L'import est validé et transactionnel : en
  cas d'échec, l'état antérieur est restauré intégralement.
- **Tout effacer** : double confirmation, vide tous les stores.

Détail du format et des validations : [Données et confidentialité](donnees-confidentialite.md).

## Paramètres

| Réglage | Effet |
|---|---|
| **Unités de poids** | kg (métrique) ou lb (impérial) — affichage et saisie ; stockage toujours en kg. |
| **Clé API Gemini** | Champ masqué, stockage local seulement. Nécessaire à l'identification par photo et aux fiches par IA. |
| **Ordre des images** | Priorité des sources d'illustration : MycoQuébec, Wikimedia, IA (6 combinaisons possibles). |
| **Crédits photos** | Écran listant auteur, licence et lien Commons pour chaque photo embarquée. |
| **Comment identifier** | Rappel de la méthode (checklist, verdicts) et du numéro du centre antipoison. |

## Ce que l'app ne fait pas

- Pas de compte, pas de synchronisation entre appareils : le transfert se fait par export
  et import JSON.
- Pas de carte interactive intégrée : le lien Google Maps ouvre l'app de cartes du système.
- Pas de partage public de spots ou de récoltes.
- **Pas de validation mycologique** : l'app aide à décider, elle ne décide pas. Voir
  [Sécurité alimentaire](securite-alimentaire.md).

Voir aussi : [Guide d'identification](guide-identification.md) ·
[Données et confidentialité](donnees-confidentialite.md) · [../PRODUCT.md](../PRODUCT.md)
