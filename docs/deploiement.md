# Déploiement

> **Wiki Cueillette Québec — édition Memphis** · [Accueil du dépôt](../README.md) ·
> [Index du wiki](README.md)

## Sommaire

- [Comment le site est publié](#comment-le-site-est-publié)
- [Procédure de mise à jour](#procédure-de-mise-à-jour)
- [Le bump du cache `cqm-vN`](#le-bump-du-cache-cqm-vn)
- [Ajouter des fichiers au cache hors-ligne](#ajouter-des-fichiers-au-cache-hors-ligne)
- [Vérifications après déploiement](#vérifications-après-déploiement)
- [Option : publier avec GitHub Actions](#option--publier-avec-github-actions)
- [Retour arrière](#retour-arrière)

## Comment le site est publié

- Dépôt : `jonathancote1984/cueillette-memphis`, branche `main`.
- Publication : **GitHub Pages en mode « Deploy from a branch »**, branche `main`, dossier
  `/ (root)`. Le dépôt ne contient **aucun** workflow dans `.github/` : il n'y a rien à
  compiler.
- Adresse publique : <https://jonathancote1984.github.io/cueillette-memphis/>
- Déployer = **pousser sur `main`**. Pages republie en une à deux minutes.

Rien d'autre n'est requis : pas de variable d'environnement, pas de secret, pas d'étape de
compilation. Les chemins sont relatifs, donc le sous-dossier de Pages fonctionne tel quel.

## Procédure de mise à jour

```bash
cd cueillette-memphis

# 1. modifier l'app (index.html, styles, images, etc.)

# 2. bumper le cache du service worker (OBLIGATOIRE)
#    sw.js ligne 4 : const CACHE = 'cqm-vN';  ->  'cqm-v(N+1)'

# 3. vérifier localement
python3 -m http.server 8091   # http://localhost:8091

# 4. livrer
git add -A
git commit -m "fix(guide): ..."
git push origin main

# 5. attendre la republication de Pages, puis rouvrir l'app sur le téléphone
```

Étape 2 non facultative : sans bump, les appareils déjà installés continuent de servir
l'ancienne version depuis leur cache.

## Le bump du cache `cqm-vN`

Le numéro de cache est déclaré à un seul endroit :

```js
// sw.js
const CACHE = 'cqm-vN';
```

**Quand bumper** : dès qu'un fichier servi change — `index.html`, `sw.js`,
`manifest.json`, une icône, la police, une photo. Une modification de documentation
(`README.md`, `docs/`, `DESIGN.md`, `PRODUCT.md`) n'a pas besoin de bump, puisque ces
fichiers ne sont pas mis en cache par le service worker.

**Ce que le bump déclenche**

1. `install` : le socle critique (page, manifeste, icônes, 21 photos d'espèces, JSON de
   crédits, `img/mycoquebec.json`, police) est mis en cache avec `addAll` ; les 100 photos de
   spécificités sont ajoutées une à une, les échecs étant tolérés — une image manquante ne
   casse plus l'installation.
2. `activate` : tous les caches nommés `cqm-*` autres que le courant sont supprimés, puis
   `clients.claim()`.
3. `fetch` : cache d'abord, réseau ensuite ; une réponse non `ok` n'est jamais mise en cache ;
   le repli `index.html` est réservé aux navigations (jamais aux images ou aux JSON).

**Jamais mis en cache** : `*.wikimedia.org`, `*.googleapis.com`, `*.mycoquebec.org`, et toute
URL contenant `key=`.

Convention de journal de bord : le message de commit mentionne le bump
(`— SW bump cqm-v62`), ce qui permet de retracer la version servie à chaque changement.

## Ajouter des fichiers au cache hors-ligne

Pour qu'une nouvelle ressource soit disponible hors-ligne :

1. l'ajouter au tableau `FICHIERS` dans `sw.js`, avec un chemin **relatif** commençant par
   `./` ;
2. si c'est une photo de spécificité, la placer dans `img/specs/` (le service worker traite
   ce préfixe en mode tolérant) ;
3. ajouter l'entrée d'attribution correspondante dans le `credits.json` du dossier ;
4. bumper `cqm-vN`.

## Vérifications après déploiement

À faire au moins une fois par livraison :

- [ ] la page répond en 200 à l'adresse Pages, en navigation privée ;
- [ ] DevTools → *Application → Service Workers* : le service worker actif porte le
      **nouveau** numéro de cache ;
- [ ] DevTools → *Application → Cache Storage* : un seul cache `cqm-*` subsiste ;
- [ ] mode avion (ou *Network → Offline*) : le guide, les fiches et les 5 photos de
      spécificités s'affichent ;
- [ ] `manifest.json` répond en 200 et l'invite « Ajouter à l'écran d'accueil » apparaît ;
- [ ] aucune erreur en console, en particulier aucune violation de CSP ;
- [ ] un export JSON se télécharge et se réimporte sans perte.

## Option : publier avec GitHub Actions

Le mode « branche » suffit et reste le plus simple. Si un jour la publication doit passer par
Actions (par exemple pour ajouter une étape de vérification), l'équivalent minimal est un
workflow qui téléverse la racine du dépôt comme artéfact Pages :

```yaml
# .github/workflows/pages.yml
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
  workflow_dispatch:
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: true
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: .
      - id: deployment
        uses: actions/deploy-pages@v4
```

Avant d'activer ce workflow, basculer *Settings → Pages → Source* sur **GitHub Actions** ;
sinon les deux mécanismes se marchent sur les pieds. Ce fichier n'existe pas dans le dépôt
aujourd'hui : c'est un modèle, à créer seulement si le besoin apparaît.

## Retour arrière

L'app étant statique, revenir en arrière consiste à republier l'état antérieur :

```bash
git revert <commit fautif>       # ou git reset --hard <commit sain> puis push forcé
# bumper de nouveau cqm-vN (un retour arrière est aussi un changement)
git push origin main
```

Le bump au retour arrière est nécessaire : sans nouveau numéro, les appareils garderaient la
version fautive en cache.

Voir aussi : [Installation](installation.md) · [Contribution](contribution.md) ·
[Journal des versions](changelog.md)
