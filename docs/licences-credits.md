# Licences et crédits

> **Wiki Cueillette Québec — édition Memphis** · [Accueil du dépôt](../README.md) ·
> [Index du wiki](README.md)

## Sommaire

- [Code de l'application](#code-de-lapplication)
- [Photos des espèces](#photos-des-espèces)
- [Photos des spécificités](#photos-des-spécificités)
- [Miniatures MycoQuébec](#miniatures-mycoquébec)
- [Police de caractères](#police-de-caractères)
- [Comment l'attribution est affichée](#comment-lattribution-est-affichée)
- [Ajouter une photo en respectant la licence](#ajouter-une-photo-en-respectant-la-licence)
- [État des crédits](#état-des-crédits)

## Code de l'application

Aucun fichier `LICENSE` n'est présent dans le dépôt. En l'absence de licence explicite, le
code reste **sous droit d'auteur, tous droits réservés** : personne ne peut légalement le
réutiliser, le modifier ou le redistribuer sans autorisation.

Si le projet doit être réutilisable, ajouter un fichier `LICENSE` à la racine (MIT ou
Apache-2.0 pour du permissif) et le mentionner dans le [README](../README.md).

## Photos des espèces

- Emplacement : `img/especes/` — **21 photos**, une par espèce du guide.
- Source : **Wikimedia Commons**.
- Licences rencontrées : CC0, CC BY 2.0/4.0, CC BY-SA 2.0/3.0/4.0.
- Attribution : `img/especes/credits.json` — pour chaque identifiant d'espèce, le fichier
  local, l'espèce photographiée, l'auteur, la licence et l'URL de la page Commons.

Exemple d'entrée :

```json
"chanterelle": {
  "fichier": "img/especes/chanterelle.jpg",
  "espece": "Cantharellus cibarius",
  "auteur": "Jebulon",
  "licence": "CC0",
  "page": "https://commons.wikimedia.org/wiki/File:Girolles_Viktualienmarkt_Munich.jpg"
}
```

## Photos des spécificités

- Emplacement : `img/specs/` — **100 photos** (21 espèces × 5 critères : chapeau, hyménium,
  pied, chair et odeur, habitat).
- Source : Wikimedia Commons, récupérées par terme de recherche selon la partie visée.
- Attribution : `img/specs/credits.json`, même structure que ci-dessus, avec l'identifiant
  `<espece>-<1..5>`.
- Ces images ont été recompressées (qualité 80) pour ramener le poids embarqué de 22,9 Mo à
  18,6 Mo.

## Miniatures MycoQuébec

`img/mycoquebec.json` contient **3 938 entrées** (nom latin, nom français quand il existe,
URL de miniature sur `mycoquebec.org`, indicateur de présence dans le guide). Il sert à
l'autocomplétion du nom d'une variété personnelle.

Ces miniatures ne sont **pas redistribuées** dans le dépôt : seules les URL sont stockées, et
le service worker exclut explicitement `mycoquebec.org` de son cache. Les vignettes distantes
ne sont pas affichées comme des images locales dans les suggestions.

## Police de caractères

`fonts/fredoka.woff2` — **Fredoka**, police libre distribuée sous SIL Open Font License 1.1,
auto-hébergée pour éviter tout appel à Google Fonts (confidentialité et fonctionnement
hors-ligne). Conserver le fichier de licence de la fonte si la police est mise à jour.

## Comment l'attribution est affichée

Dans l'app : **Paramètres → Crédits photos**. L'écran liste, pour chaque photo embarquée,
l'espèce, l'auteur, la licence et un lien vers la page Commons d'origine. Les deux fichiers
`credits.json` sont mis en cache par le service worker, donc l'attribution reste consultable
hors-ligne — c'est une exigence des licences CC BY et CC BY-SA.

## Ajouter une photo en respectant la licence

1. Choisir une image sur Wikimedia Commons dont la licence permet la réutilisation (CC0,
   CC BY, CC BY-SA).
2. Télécharger, recompresser (côté long ≈ 1 200 px, qualité 80) et déposer le fichier dans
   `img/especes/` ou `img/specs/`.
3. Ajouter l'entrée d'attribution complète (fichier, espèce, auteur, licence, page) dans le
   `credits.json` du dossier.
4. Ajouter le chemin au tableau `FICHIERS` de `sw.js`.
5. Incrémenter `cqm-vN` (voir [Déploiement](deploiement.md)).

Ne jamais embarquer une image sans entrée de crédit : sans attribution, la redistribution
d'une image CC BY ou CC BY-SA n'est pas conforme.

## État des crédits

Vérification faite sur l'état actuel du dépôt :

| Dossier | Fichiers | Entrées de crédit | État |
|---|---|---|---|
| `img/especes/` | 21 photos | 21 | complet |
| `img/specs/` | 100 photos | 100 | **0 manquante** (photos `chanterelle-1..5` retirées, crédits absents) |

À faire : retrouver la provenance des cinq photos de spécificités de la chanterelle commune et
compléter `img/specs/credits.json`, ou remplacer ces images par des fichiers dont
l'attribution est connue.

Voir aussi : [Design](design.md) · [Contribution](contribution.md) ·
[Guide d'identification](guide-identification.md)
