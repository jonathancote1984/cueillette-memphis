# Audit Performance / PWA / UX — cueillette-memphis

**Date :** 16 août 2026 — **Méthode :** analyse statique complète (index.html, sw.js, manifest.json) + inspection réelle des images (PIL : formats, dimensions, poids) + croisement automatique des références (FICHIERS ↔ disque ↔ code). PWA statique sans build : pas de Lighthouse fiable ici ; les temps de parse sont des estimations documentées comme telles.

**Verdict global :** aucune sévérité **critique**. La PWA est **offline-first complète et propre** (135/135 ressources locales couvertes, exclusions API correctes, re-rendus ciblés sur les interactions à enjeu). Les 3 constats **majeurs** portent sur le poids d'installation (images non optimisées, 25,7 Mo), la typo signature absente hors-ligne (Google Fonts jamais précachée), et une fragilité du cache runtime (404 empoisonnables). Rien ne bloque l'usage terrain.

---

## 1. Poids du monolithe

### [SÉVÉRITÉ: majeur] Google Fonts : render-blocking en ligne + police signature absente hors-ligne
**fichier:ligne :** `index.html:15-17` (preconnect ×2 + `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka...&display=swap">`) ; exclusion corrélée `sw.js:158` (`googleapis.com` jamais mis en cache).
**Impact :** (a) en ligne, la feuille de style Google est **bloquante pour le premier rendu** (un RTT supplémentaire avant le premier paint, même avec preconnect) ; (b) hors-ligne — le cœur de la promesse « 100 % hors-ligne » — la requête échoue et `font-display:swap` fait retomber **toute l'interface en police système** : l'identité visuelle Fredoka (assumée dans DESIGN.md) disparaît à chaque usage en forêt. Le SW exclut volontairement googleapis.com (bonne pratique anti-clé-API), mais la police en fait les frais.
**Recommandation :** self-hoster les 4 graisses woff2 de Fredoka dans `fonts/` (ou `img/fonts/`), les ajouter à `FICHIERS` (bump SW), garder `font-display:swap`, supprimer les 3 `<link>` Google. Alternative minimale : retirer la link et assumer une stack système — mais le design Memphis repose sur Fredoka.

### [SÉVÉRITÉ: mineur] Monolithe 182,5 Ko re-parsé à chaque chargement
**fichier:ligne :** `index.html:748-2838` (JS inline 133,2 Ko / 2 092 lignes ; CSS inline 20,85 Ko / 347 lignes ; total fichier 182 530 octets, 2 842 lignes).
**Impact :** ~133 Ko de JS parsés/exécutés à chaque chargement (estimation 15-40 ms sur mobile milieu de gamme, hors exécution `init`). Tout correctif = re-téléchargement intégral via bump de cache. C'est le **choix d'architecture assumé** (zéro framework, zéro build, déploiement mono-fichier) et le coût est faible pour une app privée.
**Recommandation :** ne rien changer tant que le JS reste < ~250 Ko. Si le code grossit, découper en 2 blocs `<script>` (cœur au chargement, vues secondaires différées) sans introduire de build.

---

## 2. Cache du service worker

### [SÉVÉRITÉ: majeur] Le cache runtime peut être empoisonné par des réponses non-OK (404)
**fichier:ligne :** `sw.js:160-163` — `fetch(e.request).then(r => { const copie = r.clone(); caches.open(CACHE).then(c => c.put(e.request, copie)) … })` sans vérification du statut.
**Impact :** en stratégie **cache-first**, toute réponse d'erreur (404 d'un déploiement partiel sur GitHub Pages, 500 transitoire) est mise en cache comme si elle était valide → l'app servira cette erreur **indéfiniment** (jusqu'au prochain bump). Une seule ressource manquante casse durablement une partie de l'app hors-ligne.
**Recommandation :** `if (r.ok || r.type === 'opaque') { caches.open(CACHE).then(c => c.put(e.request, copie)).catch(() => {}); } return r;`

### [SÉVÉRITÉ: mineur] Install atomique `addAll` sur 135 fichiers / 25,7 Mo : un seul échec = zéro offline
**fichier:ligne :** `sw.js:143-145` — `caches.open(CACHE).then(c => c.addAll(FICHIERS))`.
**Impact :** `addAll` est tout-ou-rien : si UNE des 135 ressources échoue (réseau coupé en plein install, fichier renommé), `e.waitUntil` rejette, le SW ne s'installe pas et **aucun fichier n'est précaché** — la promesse offline tombe entièrement. Aujourd'hui les 135 fichiers existent sur disque (vérifié), le risque est faible mais la conséquence est totale.
**Recommandation :** installer le socle critique (index.html, manifest, icônes, JSON) en `addAll`, puis ajouter les 126 images en `add()` individuel avec `catch` (une image qui échoue ne doit pas bloquer l'installation).

### [SÉVÉRITÉ: mineur] `'./'` et `'./index.html'` précachés en double
**fichier:ligne :** `sw.js:6-7` — les deux entrées résolvent vers le même document.
**Impact :** un fetch/put redondant à l'install (quelques Ko, négligeable) ; confusion possible sur quelle entrée sert le fallback navigation.
**Recommandation :** ne garder que `'./index.html'` (déjà utilisé comme fallback en `sw.js:164`).

### [POSITIF — à préserver] Exclusions API correctes et clé jamais cachée
**fichier:ligne :** `sw.js:158` — `wikimedia.org`, `googleapis.com` et toute URL avec `key=` exclues du cache.
**Impact positif :** les résultats d'identification Gemini et de recherche Wikimedia restent toujours frais, et la clé API (présente dans l'URL) n'est jamais stockée dans Cache Storage. Runtime cache-first propre pour tout le reste (GET uniquement, `sw.js:155`).

---

## 3. Offline-first complet

### [POSITIF — prouvé] 100 % des ressources locales sont précachées, zéro trou
**fichier:ligne :** `sw.js:5-141` (FICHIERS, 135 entrées) ; références croisées `index.html` (JS).
**Preuve :** 135 entrées FICHIERS → 0 fichier manquant sur disque, 0 doublon ; 129 références `img/…` littérales du JS → 0 absente ; les 21 `img/especes/*.jpg` de ESPECES → toutes couvertes ; les 105 `img/specs/*.jpg` de SPECS_DEFAUT → toutes couvertes ; `img/mycoquebec.json` (3 938 entrées) et les 2 `credits.json` → couverts. Guide, fiches hybrides, checklist, spots, cueillettes, crédits CC : **tout fonctionne hors-ligne**. Les seules dépendances réseau restantes sont assumées et documentées : Gemini (identification/illustrations IA), Wikimedia (recherche de photos à la génération), lien MyCoQuébec (ouverture externe) — avec messages d'erreur français explicites (`messageErreurIA`).

### [SÉVÉRITÉ: mineur] Registration du SW en fin d'init
**fichier:ligne :** `index.html:790` (JS : `navigator.serviceWorker.register('sw.js')` en dernière ligne d'`init`, après `Stockage.ouvrir()` + `recharger()` + rendus initiaux).
**Impact :** au premier chargement, l'installation du SW (et le préchargement des 25,7 Mo) ne démarre qu'après l'ouverture IndexedDB, les 7 lectures et les rendus initiaux — quelques dizaines à centaines de ms de retard, sans conséquence fonctionnelle.
**Recommandation :** déplacer la registration en tête d'`init` (elle est asynchrone et non bloquante).

---

## 4. Images (mesures réelles)

### [SÉVÉRITÉ: majeur] 105 photos de spécificités non optimisées : 22,9 Mo, jusqu'à 474 Ko, croppées à l'affichage
**fichier:ligne :** `img/specs/*.jpg` (105 fichiers) ; affichage `index.html:257` (`.spec-photo img` : `aspect-ratio:16/9; object-fit:cover`).
**Mesures réelles (PIL) :** toutes JPEG RGB, **960 px de large**, hauteurs de 540 à **1 594 px** ; poids moyen **218 Ko**, min 42,6 Ko, max **474 Ko** (`phalloide-5.jpg`), top 5 : phalloide-5 474 Ko, cepe-5 448 Ko, galerine-5 420 Ko (960×1594), galerine-3 403 Ko, lepiote-3 394 Ko. Total : **22 942 Ko = 89 % du poids de précache (25,7 Mo)**.
**Impact :** (a) installation initiale lente et volumineuse pour une app privée ; (b) les photos verticales (jusqu'à 1 594 px de haut) sont affichées croppées en 16/9 (~960×540) : **~50-60 % de leurs pixels ne sont jamais vus** dans la carte ; (c) décodage mémoire de 218 Ko en moyenne à chaque ouverture de fiche. Nuance : la lightbox « 🔍 Agrandir » affiche bien la pleine résolution, donc le 960 px se justifie pour elle.
**Recommandation :** recompression JPEG **q78-82 sans métadonnées** des 105 fichiers (le 960 px reste pertinent pour la lightbox retina) → 80-150 Ko/photo attendus, **~10-12 Mo économisés**. Optionnel : générer une version carte 640 px (16/9 recadré) + conserver l'originale pour la lightbox.

### [SÉVÉRITÉ: mineur] Vignettes du guide : les 800 px décodées en 88×92 px
**fichier:ligne :** `index.html:132` (`.item .vig` 88×92 px, `img` 100 %) ; données `index.html` (ESPECES : 21 `img/especes/*.jpg`, 800 px de large, 2 552 Ko, moy. 122 Ko, max 190 Ko `coprin.jpg`).
**Impact :** le même fichier 800 px sert la vignette 88 px de la liste **et** la photo pleine largeur de la fiche — surcoût de décodage à chaque rendu de liste (21 images), sans srcset. Modeste (21 fichiers seulement).
**Recommandation :** acceptable en l'état. Si optimisation un jour : `srcset` 240w/800w sur la vignette, ou versions 240 px pour la liste.

### [POSITIF — à préserver] Pas de CLS : dimensions réservées partout
**fichier:ligne :** `index.html:132` (`.item .vig` min-height 92 px), `index.html:257` (aspect-ratio 16/9 sur les cartes specs), `index.html:349` (`.detail-img` max-height 280 px) + `loading="lazy"` sur les vignettes du guide (`index.html:1433`).
**Impact positif :** aucune image ne provoque de saut de mise en page au chargement ; le lazy évite le décodage des vignettes hors écran (servies instantanément par le SW de toute façon).

---

## 5. Démarrage / parse cost

### [SÉVÉRITÉ: mineur] Filtrage des 3 938 entrées MyCoQuébec à chaque frappe, sans debounce
**fichier:ligne :** `index.html:1689` (`chargerBaseMyco()` : fetch lazy de `img/mycoquebec.json`, 573 Ko / 97 Ko gz, 3 938 entrées — **bon point** : jamais au démarrage, mémorisé dans `baseMyco`) ; `index.html:1699` (`remplirSuggestionsMyco()` : `.filter()` + `.sort()` avec score sur les 3 938 entrées à chaque `input`).
**Impact :** ~4 appels `normNom` (`index.html:979` : `toLowerCase` + `normalize('NFD')` + 2 regex) × 3 938 entrées ≈ 16 000 normalisations synchrones par frappe → micro-blocages du thread principal (estimé 10-50 ms/frappe) sur mobile, re-rendu des 6 suggestions à chaque fois.
**Recommandation :** debounce 150-250 ms + pré-normalisation de `nomFr`/`latin` en une passe au premier chargement de `baseMyco`.

### [SÉVÉRITÉ: mineur] Recherche du guide : rebuild complet de la liste à chaque frappe
**fichier:ligne :** `index.html:1464` (`input` sur `g-recherche` → `rendreGuide()` direct) ; `rendreGuide()` `index.html:1433` (innerHTML de ≤ 22 cartes + vignettes re-créées).
**Impact :** chaque caractère saisi reconstruit toute la liste (DOM + éléments `<img>` re-créés — décodage réutilisé via le cache navigateur, coût réel faible mais inutile).
**Recommandation :** debounce 150 ms, ou ne re-rendre que si la requête normalisée a changé.

---

## 6. Re-rendus DOM

### [POSITIF — à préserver] Interactions terrain à mise à jour ciblée
**fichier:ligne :** `index.html:1536` (`basculerSpec()` : toggle de classe + `textContent` du compteur/verdicts, **pas** de rebuild de la fiche) ; `index.html:1343` (`basculerEspeceSpot()` : `classList.toggle` uniquement).
**Impact positif :** cocher les 5 critères d'une fiche (usage répété en forêt) ne re-rend jamais les 5 photos ni le reste de la fiche — fluide et économe. C'est le bon pattern, à ne pas casser.

### [SÉVÉRITÉ: mineur] `recharger()` re-rend toutes les vues à chaque écriture
**fichier:ligne :** `index.html:2794` (`recharger()` : 7 lectures IDB en `Promise.all` + `rendreSpots()` + `rendreCueillettes()` + `remplirDatalist()` + `remplirSelectSpot()` + vue courante) ; 12 appels `await recharger()` après chaque sauvegarde/suppression.
**Impact :** chaque opération d'écriture re-rend des vues qui n'ont pas changé. Imperceptible à l'échelle actuelle (< 100 spots/cueillettes) ; le garde-fou anti-course `seqRecharger` (`index.html:2796`) est déjà en place.
**Recommandation :** ne re-rendre que la vue courante ; conserver le `Promise.all` (déjà optimisé).

### [SÉVÉRITÉ: mineur] `rendreFiltres()` reconstruit les 2 `<select>` à chaque changement de filtre
**fichier:ligne :** `index.html:1406` (`rendreFiltres()`) appelé par `filtrerGuide`/`filtrerSaison` (`index.html:1419-1420`).
**Impact :** le `<select>` déclencheur est détruit/re-créé pendant son `onchange` (le menu natif peut se fermer brutalement sur mobile) et l'autre `<select>` est re-rendu sans raison.
**Recommandation :** ne re-rendre que `liste-guide` ; construire les `<select>` une seule fois à l'init.

---

## 7. UX mobile / iOS

### [SÉVÉRITÉ: mineur] Header sans `env(safe-area-inset-top)` en mode standalone iOS
**fichier:ligne :** `index.html:5` (`viewport-fit=cover`), `index.html:37` (header sticky `top:0`), safe-areas utilisées uniquement en bas (`index.html:32, 78, 99, 285, 356` : nav, fab, feuilles, toast).
**Impact :** avec `viewport-fit=cover` sur iPhone à encoche en mode « Ajouter à l'écran d'accueil », le header ambre peut passer **sous la barre de statut** (le contenu est étendu sous la zone de la barre). À confirmer sur device (le comportement varie selon la version iOS et `status-bar-style`).
**Recommandation :** ajouter `padding-top: env(safe-area-inset-top)` au header (et au body si besoin), ou passer `apple-mobile-web-app-status-bar-style` à `black-translucent` avec gestion complète des insets.

### [SÉVÉRITÉ: mineur] `apple-touch-icon` non dédié (192 px au lieu de 180 px)
**fichier:ligne :** `index.html:14` — `icons/icon-192.png` réutilisé pour iOS.
**Impact :** iOS redimensionne l'icône 192 → rendu parfois légèrement flou sur l'écran d'accueil.
**Recommandation :** générer `apple-touch-icon.png` en 180×180 (le script `generer_icones.py` existe) et le référencer.

### [SÉVÉRITÉ: mineur] Lightbox sans transition ni verrouillage du scroll
**fichier:ligne :** `index.html:2433` (`ouvrirLightbox()` : overlay créé en dur, `cursor:zoom-out`, fermeture au clic/Escape, **focus restauré** ✓, `aria-modal` ✓).
**Impact :** apparition/disparition instantanée (aucun fondu/zoom) ; le body reste scrollable derrière l'overlay sur iOS (un swipe peut faire défiler la page en arrière-plan).
**Recommandation :** fondu/zoom 120-150 ms (respectant `prefers-reduced-motion`, déjà présent `index.html:356`) + `document.body.style.overflow='hidden'` à l'ouverture, restauration à la fermeture.

### [POSITIF — conforme] Viewport, meta iOS et manifest
**fichier:ligne :** `index.html:5` (viewport `width=device-width, initial-scale=1, viewport-fit=cover`) ; `index.html:9-11` (`apple-mobile-web-app-capable=yes`, `status-bar-style=default`, titre) ; `manifest.json` (display `standalone`, `orientation: portrait`, `lang: fr`, `id`/`start_url`/`scope` cohérents, `theme_color #D9A441` / `background_color #F3E8D5`, icônes 192/512/maskable — **vérifiées PIL** : PNG RGBA aux bonnes dimensions, 2-7 Ko). `prefers-reduced-motion` présent (`index.html:356`).

### [POSITIF — conforme] Cibles tactiles ≥ 44 px partout
**fichier:ligne :** `.puce` min-height 44 px (`index.html:163`), `.fab` 60×60 px (`index.html:99`), `.btn` ~46 px de haut (`index.html:144`), `nav.tabs button` ~55 px de haut (`index.html:80`), `.item` = carte entière cliquable (`index.html:126`). Aucune cible < 44 px détectée. Seule réserve : libellés des onglets en 11,5 px (`index.html:80`) — petit mais standard pour une tab bar.

---

## Résumé chiffré (mesures réelles)

| Métrique | Valeur |
|---|---|
| `index.html` | **182 530 o (182,5 Ko)** — 2 842 lignes — gzip **47,9 Ko** |
| CSS inline | 20,85 Ko (1 bloc, 347 lignes) |
| JS inline | **133,2 Ko** (2 092 lignes, 84 fonctions, 36 `innerHTML`, 55 listeners, 6 `fetch`, 13 `recharger()` dont 12 `await`, 0 `setInterval`) |
| `sw.js` | 5,6 Ko — CACHE `cqm-v57` — **FICHIERS 135 entrées** (0 manquante, 0 doublon) |
| **Précache total** | **~25,7 Mo** (dont 25,5 Mo d'images) |
| `img/especes` | 21 JPEG 800 px — 2 552 Ko (moy. 122 Ko, max 190 Ko) |
| `img/specs` | 105 JPEG 960 px — **22 942 Ko** (moy. 218 Ko, max **474 Ko**, hauteur max 1 594 px) |
| `img/mycoquebec.json` | 573 Ko (97 Ko gz) — 3 938 entrées — chargement lazy ✓ |
| Icônes | 2,1 + 6,5 + 7,1 Ko — PNG RGBA aux bonnes dimensions ✓ |
| Offline-first | 129/129 références `img/` du JS couvertes ; 135/135 fichiers présents |
| CSS mobile | 5 usages safe-area (bottom), 1 `prefers-reduced-motion`, 0 cible < 44 px, 0 font-size < 12 px (hors tabs 11,5 px) |

**Comptage des constats :** 0 critique · 3 majeur · 10 mineur · 7 points positifs documentés.

## Top 5 des optimisations à fort impact

1. **Recompresser les 105 photos `img/specs` (JPEG q78-82, sans métadonnées)** — 22,9 Mo → ~10-12 Mo attendus ; install 25,7 → ~14 Mo ; décodage plus rapide à chaque fiche. *(majeur)*
2. **Self-hoster Fredoka (woff2 dans FICHIERS)** — la typo signature survit hors-ligne + premier rendu en ligne plus rapide (suppression du render-blocking Google). *(majeur)*
3. **Vérifier `r.ok` avant `c.put` dans le fetch handler** — un 404 transitoire ne doit jamais empoisonner le cache-first. *(majeur)*
4. **Debounce 150-250 ms sur la recherche guide et les suggestions MyCoQuébec** — fluidité de saisie (3 938 entrées filtrées par frappe aujourd'hui). *(mineur)*
5. **`padding-top: env(safe-area-inset-top)` sur le header + `apple-touch-icon` 180×180** — finitions iOS standalone. *(mineur)*

---

*Méthode : analyse statique — aucun navigateur/Lighthouse (PWA statique sans build) ; dimensions/format des images vérifiés par PIL (126 JPEG RGB, aucune extension mensongère) ; croisements FICHIERS ↔ disque ↔ code par script. Les estimations de parse sont indicatives.*
**Aucun fichier du projet n'a été modifié.**
