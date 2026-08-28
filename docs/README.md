# Wiki — Cueillette Québec, édition Memphis

> Documentation du dépôt [cueillette-memphis](../README.md) · app en ligne :
> <https://jonathancote1984.github.io/cueillette-memphis/>

Ce dossier est le wiki du projet : une page par sujet, en français du Québec, avec des liens
relatifs qui fonctionnent aussi bien sur GitHub que dans un éditeur local.

## Par où commencer

| Si vous voulez… | Lisez |
|---|---|
| installer l'app sur un téléphone | [Installation](installation.md) |
| savoir ce que l'app fait, écran par écran | [Fonctionnalités](fonctionnalites.md) |
| identifier un champignon correctement | [Guide d'identification](guide-identification.md) |
| comprendre les règles de sécurité | [Sécurité alimentaire](securite-alimentaire.md) |
| savoir où vont vos données | [Données et confidentialité](donnees-confidentialite.md) |
| respecter l'identité visuelle | [Design](design.md) puis [DESIGN.md](../DESIGN.md) |
| publier une mise à jour | [Déploiement](deploiement.md) |
| modifier le code | [Contribution](contribution.md) |
| retracer l'évolution du projet | [Journal des versions](changelog.md) |
| citer les photos correctement | [Licences et crédits](licences-credits.md) |

## Pages du wiki

- **[Installation](installation.md)** — hébergement GitHub Pages, ajout à l'écran d'accueil,
  serveur local, mise à jour du cache `cqm-vN`, dépannage.
- **[Fonctionnalités](fonctionnalites.md)** — spots, identification, cueillettes, stats,
  sauvegarde, paramètres.
- **[Guide d'identification](guide-identification.md)** — les 21 espèces documentées, la
  checklist terrain à 5 critères, l'identification par photo et ses limites.
- **[Sécurité alimentaire](securite-alimentaire.md)** — badges de statut, verdicts, centre
  antipoison, primauté du guide sur l'IA, protection contre l'injection de consignes.
- **[Données et confidentialité](donnees-confidentialite.md)** — IndexedDB `cqm_bd` v5, clé
  Gemini locale, ré-encodage des photos, export/import JSON version 5.
- **[Design](design.md)** — style Memphis, palette automne/terre, tokens, composants clés.
- **[Déploiement](deploiement.md)** — publication par branche, option GitHub Actions, bump du
  cache du service worker, vérifications après déploiement.
- **[Licences et crédits](licences-credits.md)** — origine et attribution des photos.
- **[Contribution](contribution.md)** — conventions de code et de commit, checklist avant
  livraison, documents à tenir à jour.
- **[Journal des versions](changelog.md)** — grandes itérations, du premier commit à
  aujourd'hui.

## Documents de référence hors wiki

Ces fichiers restent la source de vérité de leur domaine ; le wiki les résume et y renvoie.

| Document | Contenu |
|---|---|
| [../DESIGN.md](../DESIGN.md) | Système de design complet : tokens, couleurs nommées, composants, règles do/don't. |
| [../PRODUCT.md](../PRODUCT.md) | Vérité produit : usagers, contexte d'usage, capacités, contraintes, principes. |
| [AUDIT_RAPPORT.md](AUDIT_RAPPORT.md) | Audit webapp consolidé (sécurité, qualité, performance) avec plan de correction. |
| [AUDIT_SECU.md](AUDIT_SECU.md) | Constats de sécurité détaillés. |
| [AUDIT_QUALITE.md](AUDIT_QUALITE.md) | Constats de qualité de code. |
| [AUDIT_PERF.md](AUDIT_PERF.md) | Constats performance, PWA et UX. |
| [archive/](archive/) | Rapports de revue de design et d'exécution des passes de critique (historique). |

## Conventions du wiki

- Une page = un sujet ; en-tête identique (titre, fil d'Ariane, sommaire si la page est
  longue).
- Liens **relatifs** seulement (`installation.md`, `../DESIGN.md`) — jamais d'URL absolue
  vers GitHub pour un fichier du dépôt.
- Le numéro de cache du service worker n'est **jamais** recopié dans la documentation : il
  vit dans `sw.js` (`const CACHE = 'cqm-vN'`) et nulle part ailleurs.
- Ton factuel, français du Québec, pas de promesse commerciale.
- Les messages de sécurité (« en cas de doute, on ne mange pas », centre antipoison
  1-800-463-5060) sont repris mot pour mot, sans reformulation atténuante.
