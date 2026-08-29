# Journal des versions

> **Wiki Cueillette Québec — édition Memphis** · [Accueil du dépôt](../README.md) ·
> [Index du wiki](README.md)

Le projet n'a pas de numéro de version applicatif : le repère de livraison est le **numéro de
cache du service worker** (`cqm-vN`, déclaré dans `sw.js`) et l'historique Git. Ce journal
résume les grandes itérations ; `git log` reste la référence exacte.

## Sommaire

- [Comment lire ce journal](#comment-lire-ce-journal)
- [Août 2026 — fondations (cqm-v1 à v10)](#août-2026--fondations-cqm-v1-à-v10)
- [Août 2026 — le guide devient un outil de terrain (v11 à v23)](#août-2026--le-guide-devient-un-outil-de-terrain-v11-à-v23)
- [Août 2026 — passes de critique 4e à 21e (v23 à v49)](#août-2026--passes-de-critique-4e-à-21e-v23-à-v49)
- [Août 2026 — filet de sécurité et parité des fiches (v50 à v61)](#août-2026--filet-de-sécurité-et-parité-des-fiches-v50-à-v61)
- [Août 2026 — audit webapp complet et robustesse de l'IA (v58 à v62)](#août-2026--audit-webapp-complet-et-robustesse-de-lia-v58-à-v62)
- [Ménage de la documentation](#ménage-de-la-documentation)

## Comment lire ce journal

- **Passe de critique** : cycle interne de revue où l'app est notée sur 40 ; les constats sont
  classés P0 (bloquant) à P3 (finition) puis corrigés. Les rapports sont archivés dans
  [archive/](archive/).
- **`— SW bump cqm-vN`** en fin de message de commit : la livraison a changé un fichier servi,
  donc le cache a été incrémenté.

## Août 2026 — QA navigateur complète (v62 à v66)

Audit fonctionnel/visuel/qualité/sécurité exécuté dans un vrai navigateur, au-delà de l'audit
statique. Correctifs appliqués :

- **CSP `worker-src 'self'`** : le service worker ne se ré-enregistrait plus sur les nouvelles
  installations (le hors-ligne de la PWA était cassé).
- **Import JSON** : `ecrireTout` enveloppait `cachees`/`supprimees` en objet de clé IDB → tout
  import contenant des espèces masquées/supprimées échouait. Corrigé.
- **XSS stocké (S1)** : `imgSaine` n'ancrait que le début d'URL → une photo importée
  `https://…" onerror="…` exécutait du code et lisait la clé Gemini. `imgSaine` durci (ancré
  des 2 côtés, rejet de `" ' < >` et espaces).
- **CSP `connect-src`** : `upload.wikimedia.org` ajouté (les photos Wikimedia étaient stockées
  en URL distante, hors-ligne cassé + fuite IP) ; `img-src` restreint aux hôtes réels.
- **Fail-safe alimentaire** : `badgeStatut` — `prudence` n'écrase plus un statut
  `mortel`/`toxique`/`immangeable` (une variété MORTELLE ne s'affiche plus « comestible — prudence »).
- **Filet de noms (C-1)** : le Levenshtein compare désormais aussi le nom **sans parenthèse** —
  une faute de frappe (« gyromitte ») ne fait plus perdre le badge MORTEL à `gyromitre (fausse morille)`.
- **Saisie du poids** : champ en `inputmode="decimal"` — `1,5` vaut bien `1,5` kg (et non 15 kg).
- **Robustesse** : media query ≤380px (nav 5 onglets), `flex-wrap` des étapes, timeout sur les
  fetch Wikimedia, `aria-label` (recherche, clé, navigation), alias sémantiques de palette
  (`--rouille`, `--terracotta`).
- **Photos** : les 5 `specs/chanterelle-1..5.jpg` (crédits Wikimedia absents) ont été **retirées**
  pour rester conforme aux licences ; les 100 photos restantes recompressées/réduites à 720 px
  (≈ 14 Mo, −35 %).

## Août 2026 — fondations (cqm-v1 à v10)

- Première version : PWA de cueillette refaite de zéro, spots avec GPS, guide de 21 espèces
  avec photos, journal des récoltes, statistiques.
- Variétés personnelles : ajout, modification, suppression, avec génération de fiche par
  Gemini et photo Wikimedia Commons ou illustration par IA.
- Remplacement des boîtes système par des **modales Memphis** (confirmations stylées).
- Bascule du style vers la **palette automne/terre** (ambre, rouille, terracotta, olive,
  cuir) et restauration sélective des espèces masquées.
- `theme_color` ambre pour la barre de statut mobile.
- Masquage ou suppression définitive d'une espèce (modale de choix), illustrations par
  spécificité (chapeau, lames, pied, section, habitat), identification par photo (Gemini
  vision), export version 2.
- Robustesse : poids à virgule (`1,5`), statut `inconnu` pour les entrées douteuses, ménage
  des orphelins.
- Capture de la vérité produit et du système de design : `PRODUCT.md` et `DESIGN.md`.
- Accessibilité : contrastes WCAG AA (terracotta `#B94527`, vert de mesure `#0B7A55`).

## Août 2026 — le guide devient un outil de terrain (v11 à v23)

- Partage d'un spot (Web Share API, repli presse-papiers, lien Google Maps).
- Onglet **Paramètres** : unités kg/lb avec conversion à la saisie, à l'affichage et dans les
  stats ; clé API Gemini déplacée des feuilles vers les paramètres ; suppression définitive
  des espèces d'origine (store `supprimees`, double confirmation, export version 4).
- Signaux de sécurité conservés sur les cueillettes liées à une espèce supprimée (archivage de
  l'identifiant d'espèce).
- **Fiche hybride** : checklist terrain interactive à 5 critères par espèce, avec photos
  réelles et descriptions, persistance en IndexedDB (store `checklist`, base version 5),
  verdicts ✅ / ⚠️.
- **105 photos** Wikimedia embarquées pour les 5 spécificités des 21 espèces (hors-ligne).
- Sélection multi-espèces sur les spots ; menu déroulant natif pour l'espèce d'une cueillette.
- Recherche d'illustration : Wikimedia par partie du champignon d'abord, IA en repli.
- Filtres du guide par saison en plus des filtres de statut.
- Écran **Crédits photos** dans les paramètres (auteur, licence, lien Commons).

## Août 2026 — passes de critique 4e à 21e (v23 à v49)

Cycle de revues successives, principalement axées sur la sécurité d'affichage et
l'ergonomie de terrain :

- verdict ⚠️ visible **dès 0 critère coché** (« rien n'est encore vérifié ») ;
- verdict rouge « espèce mortelle » sur toute fiche non comestible, même à 5/5 ;
- checklist incluse dans l'export/import (version 5) et vidée par « Tout effacer » ;
- correspondance floue des noms et des synonymes vernaculaires (« fausse morille » →
  gyromitre, « ange destructeur » → amanite vireuse) ;
- cibles tactiles ≥ 44 px, bouton retour collant, focus visible, `aria` sur les onglets, les
  compteurs et les barres de stats ;
- masquage déplacé dans la fiche individuelle (le 🙈 remplace le 🗑️ dans la liste) ;
- filtres du guide convertis en listes déroulantes ;
- **autocomplétion MycoQuébec** sur le nom français (base embarquée, nom latin auto-rempli) ;
- 21/21 miniatures locales, dont les espèces mortelles (plus de dépendance à un site distant) ;
- feuille de variété en **2 étapes progressives** (Identité, puis Détails et photo) ;
- refactorisations : `appelGemini`, `lierPhoto`, purge du CSS mort ;
- finitions d'interface : transitions d'ombre et de transformation, `tabular-nums`,
  `text-wrap: pretty`, sortie de feuille sans rebond.

## Août 2026 — filet de sécurité et parité des fiches (v50 à v61)

- **Le guide a le dernier mot** : croisement du résultat d'IA avec le guide, échelle de
  gravité, jamais de badge vert sur une espèce que le guide juge plus grave.
- Filet étendu aux espèces **masquées et supprimées** (`infoEspeceArchive`, `BASE_COMPLETE`
  avec correspondance exacte, floue et par inclusion) ; conservation des « tombes » à
  l'export/import, donc le filet survit sur le téléphone d'un proche.
- Garde-fou de formulaire sur toutes les feuilles (voile, poignée, `Échap`, Annuler).
- Contrôle de collision à l'enregistrement d'une variété homonyme d'une espèce du guide.
- Confirmation avant la suppression d'une variété perso ; nettoyage réel de la checklist.
- **Parité des fiches** : les 21 fiches du guide portent les mêmes champs que les variétés
  perso (ajout du champ prudence aux 19 qui en manquaient — seules la morille et l'amanite
  rougissante restent en prudence).
- À l'ajout d'une variété avec photo : proposition de générer les illustrations manquantes.

## Août 2026 — audit webapp complet et robustesse de l'IA (v58 à v62)

Audit en trois axes (sécurité, qualité, performance) consolidé dans
[AUDIT_RAPPORT.md](AUDIT_RAPPORT.md), puis corrigé en trois phases :

- **Import sécurisé** : identifiants validés (`^[A-Za-z0-9_-]{1,64}$`) et régénérés au besoin,
  URL d'images en liste blanche, gestionnaires migrés vers `data-*`, liste blanche des
  statuts, import **transactionnel** avec restauration intégrale en cas d'échec.
- **Anti-injection** : le prompt d'identification par photo ordonne d'ignorer les consignes
  écrites dans l'image ; une espèce absente du guide ne reçoit plus de badge vert seul.
- **Robustesse** : gestionnaire global de rejets de promesses, chargement en `allSettled` (un
  store corrompu ne donne plus une app blanche), installation du service worker tolérante,
  repli HTML réservé aux navigations, purge des caches préfixés `cqm-`.
- **Confidentialité et réseau** : clé Gemini transmise en en-tête `x-goog-api-key` (plus dans
  l'URL), CSP en balise meta avec liste blanche des connexions, police Fredoka auto-hébergée
  (fin de la dépendance à Google Fonts), exclusion de `mycoquebec.org` du cache.
- **Performance** : 105 photos de spécificités recompressées (22,9 Mo → 18,6 Mo).
- **Fiabilité de l'IA** : validation de la clé, parsing JSON tolérant (`parserJSONIA`), repli
  sur un modèle plus léger, temporisation exponentielle sur 429/500/503, délai d'attente et
  repli sur 404, réordonnancement des modèles d'image.

## Ménage de la documentation

- 25 rapports de revue devenus obsolètes ont été déplacés dans [archive/](archive/).
- La présente documentation « style wiki » a été introduite dans `docs/`, avec correction
  d'une contradiction du README : la palette décrite (« crème + rouge/jaune/bleu/rose/vert
  vifs ») ne correspondait pas à la palette réelle de l'app, qui est **automne/terre**.

Voir aussi : [Déploiement](deploiement.md) · [Contribution](contribution.md) ·
[AUDIT_RAPPORT.md](AUDIT_RAPPORT.md)
