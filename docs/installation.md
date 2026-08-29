# Installation

> **Wiki Cueillette Québec — édition Memphis** · [Accueil du dépôt](../README.md) ·
> [Index du wiki](README.md)

## Sommaire

- [Prérequis](#prérequis)
- [Héberger sur GitHub Pages](#héberger-sur-github-pages)
- [Ajouter l'app à l'écran d'accueil](#ajouter-lapp-à-lécran-daccueil)
- [Servir l'app en local](#servir-lapp-en-local)
- [Mise à jour et cache du service worker](#mise-à-jour-et-cache-du-service-worker)
- [Première utilisation](#première-utilisation)
- [Dépannage](#dépannage)

## Prérequis

Rien à compiler, rien à installer côté serveur : l'app est un ensemble de fichiers
statiques. Il faut seulement :

- un hébergement statique en **HTTPS** (GitHub Pages fait la job) ou `localhost` pour les
  tests — le service worker refuse de s'enregistrer sur `file://` et en HTTP non local ;
- un navigateur moderne : Chrome/Edge (Android, bureau) ou Safari 16+ (iOS) ;
- environ **25 Mo** d'espace de cache sur l'appareil : l'app embarque 121 photos.

Facultatif :

- **Python 3 + Pillow** pour régénérer les icônes (`generer_icones.py`) ;
- **Python 3 + requests** pour re-télécharger les photos (`scripts/telecharger_photos.py`) ;
- une **clé API Google Gemini** (gratuite) pour les fonctions d'IA — voir
  [Données et confidentialité](donnees-confidentialite.md).

## Héberger sur GitHub Pages

1. Pousser le dépôt sur GitHub, branche `main`.
2. Dans le dépôt : *Settings → Pages → Build and deployment*.
3. **Source** : `Deploy from a branch`. **Branch** : `main`, dossier `/ (root)`.
4. Enregistrer. GitHub publie le site en une à deux minutes à l'adresse
   `https://<utilisateur>.github.io/<dépôt>/`.

Pour ce dépôt : <https://jonathancote1984.github.io/cueillette-memphis/>

Points à savoir :

- Tous les chemins de l'app et du service worker sont **relatifs** (`./index.html`,
  `./img/especes/...`), donc la publication dans un sous-dossier de Pages fonctionne sans
  réécriture.
- Le dépôt n'a **aucun workflow GitHub Actions** : la publication est faite par Pages
  directement depuis la branche. Un simple `git push` sur `main` suffit à déployer. Voir
  [Déploiement](deploiement.md) si vous préférez passer par un workflow.
- Aucun secret n'est requis au déploiement : la clé Gemini est saisie par l'utilisateur dans
  l'app, jamais stockée dans le dépôt.

## Ajouter l'app à l'écran d'accueil

**Android (Chrome)**

1. Ouvrir l'adresse de l'app.
2. Menu ⋮ → **Ajouter à l'écran d'accueil** (ou la bannière d'installation proposée).
3. Confirmer. L'icône « Cueillette » apparaît sur l'écran d'accueil.

**iOS (Safari)**

1. Ouvrir l'adresse de l'app.
2. Bouton Partager → **Sur l'écran d'accueil**.
3. Confirmer.

L'app s'ouvre alors en plein écran (`display: standalone`, orientation portrait, barre de
statut ambre `#D9A441`), comme une app native.

> **Important** : laisser la page ouverte quelques secondes à la première visite. Le service
> worker télécharge et met en cache l'app, la police, les icônes et les 121 photos. Une fois
> l'installation du cache terminée, tout fonctionne sans réseau.

## Servir l'app en local

```bash
cd cueillette-memphis
python3 -m http.server 8091
# puis ouvrir http://localhost:8091
```

Autres options équivalentes :

```bash
npx serve -l 8091
php -S localhost:8091
```

Pour tester depuis un téléphone sur le même réseau Wi-Fi, servir l'app puis visiter
`http://<ip-du-poste>:8091`. Attention : sur une adresse IP (non `localhost`, non HTTPS), le
navigateur **n'enregistrera pas** le service worker — l'app fonctionne, mais pas le mode
hors-ligne. Pour valider le hors-ligne, tester sur GitHub Pages ou via un tunnel HTTPS.

Pendant le développement, garder les DevTools ouverts avec *Application → Service Workers →
Update on reload* pour éviter de servir une vieille version.

## Mise à jour et cache du service worker

Le mécanisme de mise à jour de l'app **est** le numéro de cache. Il vit à une seule place :

```js
// sw.js, ligne 4
const CACHE = 'cqm-vN';
```

Règle : **toute** modification de `index.html`, `sw.js`, `manifest.json`, des icônes, des
polices ou des images exige d'incrémenter `N` (`cqm-v62` → `cqm-v63`, etc.). Sans bump, les
appareils déjà installés continuent de servir l'ancienne version depuis le cache, parfois
pendant des semaines.

Ce qui se passe au bump :

1. `install` — le nouveau service worker met en cache le socle critique (`./`,
   `index.html`, `manifest.json`, icônes, photos d'espèces, JSON de crédits,
   `img/mycoquebec.json`, `fonts/fredoka.woff2`) avec `addAll`, puis les 100 photos de
   spécificités une par une en tolérant les échecs. Une image manquante ne casse plus
   l'installation.
2. `activate` — tous les caches dont le nom commence par `cqm-` et qui ne sont pas le cache
   courant sont supprimés, puis `clients.claim()` prend la main.
3. `fetch` — réponse depuis le cache d'abord, sinon réseau ; une réponse en erreur n'est
   jamais mise en cache ; le repli HTML est réservé aux navigations.

Jamais mis en cache : `*.wikimedia.org`, `*.googleapis.com`, `*.mycoquebec.org` et toute
requête dont l'URL contient `key=`.

Côté utilisateur, la mise à jour s'applique à la fermeture/réouverture de l'app (ou après un
rechargement forcé). En cas de doute : désinstaller l'app de l'écran d'accueil, vider les
données du site, réinstaller — **après avoir exporté** ses données (onglet Stats →
Exporter).

## Première utilisation

1. Ouvrir l'app, laisser le cache se remplir (compter une minute sur une bonne connexion).
2. Passer en mode avion et vérifier que le guide, les photos et les fiches s'affichent.
3. Onglet **Paramètres** : choisir l'unité de poids (kg ou lb).
4. Facultatif : coller une clé API Gemini pour activer l'identification par photo et la
   génération de fiches. Voir [Données et confidentialité](donnees-confidentialite.md).
5. Prendre l'habitude d'exporter (onglet Stats → Exporter) : c'est la seule sauvegarde.

## Dépannage

| Symptôme | Cause probable | Correctif |
|---|---|---|
| L'app ne fonctionne pas hors-ligne | service worker non enregistré (HTTP sur IP, `file://`) | servir en HTTPS ou sur `localhost` |
| Une vieille version s'affiche après un déploiement | `cqm-vN` non incrémenté dans `sw.js` | bumper le cache, redéployer, rouvrir l'app |
| Photos manquantes hors-ligne | installation du cache interrompue | rouvrir l'app en ligne et laisser terminer, puis revérifier |
| « Ajouter à l'écran d'accueil » absent | `manifest.json` non servi ou page non HTTPS | vérifier l'adresse et le code de réponse du manifeste |
| Les fonctions IA échouent | clé absente, invalide, ou quota Google atteint | revalider la clé dans Paramètres ; l'app réessaie et bascule sur un modèle de repli |
| Données disparues après réinstallation | IndexedDB effacée avec les données du site | restaurer le dernier export JSON (onglet Stats → Importer) |

Voir aussi : [Déploiement](deploiement.md) · [Fonctionnalités](fonctionnalites.md) ·
[Contribution](contribution.md)
