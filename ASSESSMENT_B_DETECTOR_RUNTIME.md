# Assessment B — Détecteur impeccable + preuves navigateur (27e passe)

**Date** : 2026-08-16 · **Cible** : `index.html` (PWA mono-fichier, HEAD `238fc14`, code `bd04b49` = fix critique 26e, SW `cqm-v54`)
**Serveur** : `python -m http.server 8142` (port libéré et vérifié après les sondes)
**Verdict global** : runtime **vert sur tous les points de sécurité** · **B-2 (25e) CORRIGÉ et vérifié au runtime (P3-3)** · tous les fixes `bd04b49` (P2-1/P2-2/P2-3/P3-1/P3-2/P3-3) vérifiés au runtime · **1 nouveau défaut P3 UX découvert (B-3, régression du fix P2-2)** · 0 défaut bloquant au détecteur (101 findings, composition identique à la 26e, tous faux positifs documentés ou advisories connus)

---

## 1. Findings CLI (detect.mjs --json)

**101 findings** — exit code 2 (findings, pas une erreur), stderr vide.

| Compte | Antipattern | Sévérité | Détail |
|---|---|---|---|
| 1 | side-tab | warning | l.135 `border-right:3px solid var(--noir)` |
| 4 | bounce-easing | warning | l.111 `cubic-bezier(.2,1.6,.4,1)` · l.241/244 `(.2,1.5,.4,1)` · l.281 `(.2,1.3,.4,1)` |
| 1 | broken-image | warning | l.2017 — commentaire JS `// … CORS OK en <img>` (décalé +25 lignes vs 26e, même commentaire) |
| 1 | em-dash-overuse | warning (advisory) | l.0 — 8 tirets cadratins / 5 958 car. corps = **0,67 / 500** (sous le seuil de 1/500) |
| 55 | design-system-radius | advisory | tokens : `999px`×12 · `5px`×9 · `4px`×9 · `16px`×8 · `14px`×7 · `3px`×3 · `6px`×2 · `9px`×2 · `10px`×2 · `20px`×1 |
| 34 | design-system-font-size | advisory | `14px`×9 · `14.5px`×5 · `11.5px`×4 · `12px`×4 · `22px`×2 · `15px`×2 · `30/32/36/48/24/18/17/10.5px`×1 chaque |
| 5 | design-system-color | advisory | 4× `rgba(0,0,0,.1)` l.137/189/255/347 (contours photos) + 1× `rgba(20,14,8,.92)` l.2412 (overlay lightbox) |

**Totaux par sévérité** : 7 warning · 94 advisory. **Par catégorie** : 6 slop · 95 quality.

Composition **identique à la 26e passe** (mêmes règles, mêmes totaux, mêmes distributions de tokens radius/font-size). Seuls décalages : broken-image 1992→2017 et color lightbox 2387→2412 (+25 lignes), correspondant au code ajouté par `bd04b49` (BASE_COMPLETE, garde-fou élargi, P3-3). **Aucun nouvel antipattern introduit** — le JS ajouté ne contient aucune CSS.

---

## 2. Triage — faux positifs identifiés (101/101 expliqués)

| Finding | Verdict | Raisonnement |
|---|---|---|
| side-tab l.135 | **FP en contexte** | Bordure noire 3 px = engagement de marque documenté : DESIGN.md « bordures noires épaisses (3 px) », « Règle du Trait Noir ». Le trait EST l'accent. |
| bounce-easing ×4 | **FP en contexte** | DESIGN.md « Élasticité délibérée : cubic-bezier(.2, 1.3-1.6, .4, 1) » — les 4 courbes sont dans la plage 1.3–1.6. |
| broken-image l.2017 | **FP** | Le `<img>` flaggé est dans le commentaire `// … CORS OK en <img>`. Aucun vrai `<img>` sans `src` (vérifié sur le source : seul le commentaire matche). |
| em-dash-overuse | **Partiel (advisory)** | 8 tirets / 5 958 car. de corps = 0,67/500, sous le seuil — typographie française standard. |
| design-system-radius ×55 | **FP en contexte** | Échelle frontmatter 8/12/18/24 px vs signature « coin cassé » (3–6 px sur un coin) et pilules 999 px documentées dans DESIGN.md (l.180) et les composants frontmatter. Paires dominantes : `14px 4px`×7, `16px 5px`×8, `18px 5px`, pilules ×12, mini-coins cassés `9px 3px`/`10px`/`6px` sur vignettes et suggestions (même patron à petite échelle). |
| design-system-font-size ×34 | **Partiel (cohérent)** | Ramp frontmatter 21/20/16/13. Dominantes documentées/cohérentes : `14.5px` ×5 (le composant `.ds-btn` du design.json l'utilise lui-même), `14px` ×9, micro-textes `10.5–12px`. Lignes décalées : l.1498/1502/1505 (fiche détail 17/14/14.5 px) — mêmes familles déjà triées en 25e/26e. Aucun hors-plage aberrant. |
| design-system-color ×5 | **FP en contexte** | 4× `rgba(0,0,0,.1)` = contours de photos (pas des couleurs de marque) ; `rgba(20,14,8,.92)` = overlay lightbox dérivé du noir de marque. Les ignoreValues config (`rgba(31,26,23,.08)`/`.5`) produisent **zéro résiduel** (aucun finding sur ces valeurs). |

**Aucune dérive réelle** : couleurs, courbes et coins flaggés sont tous des patterns documentés.

---

## 3. Findings console navigateur

- **Erreurs JS : 0** (`window.__errs` via CDP `Page.addScriptToEvaluateOnNewDocument` + reloads complets → `[]` à chaque lecture, avant, pendant et après toutes les sondes).
- **Ressources ≥ 400 : 0** (performance entries — aucun 404, y compris `img/especes/*`).
- Service worker : reset des caches (ancien `cqm-v54` supprimé) → re-registré **`cqm-v54`**, `controller: true`, cache `cqm-v54` recréé (4 entrées) — runtime vérifié sur code frais, pas un cache périmé.
- Injection overlay `/detect.js` : **échouée pour raison précise** — fichier absent du projet (`detect*` : 0 hit), 404 réel du serveur statique (pas de fallback SPA), `onerror` confirmé dans la console. Étape rapportée telle quelle (pas de succès silencieux).
- Audit final après reload complet : 0 erreur, 0 ressource ≥ 400, titre « 🐴 Cueillette Québec — édition Memphis », état des données intact.

---

## 4. Défauts — suivi 26e → 27e

### B-1 (P2, 25e) — ☠️ forcé sur les fiches comestibles → **toujours corrigé, ré-verifié au runtime**
Chanterelle (comestible), cycle 0/5 → 5/5 → 0/5 : titre de la carte att **toujours ⚠️** (codepoint `26a0`), y compris après bascule. Gyromitre (mortel) : titre att `☠️` (codepoint `2620`). Correct.

### B-2 (P3 cosmétique, 25e) — corps de la carte ⚠️ figé à « Ne consommez pas… » à 0/5 → **CORRIGÉ (P3-3 de `bd04b49`), vérifié au runtime**
`basculerSpec` (l.1519) met désormais à jour le corps via `.corps-att`, et `ouvrirDetail` le rend via template. Preuves (chanterelle) :
- 0/5 : « ⚠️ Rien n'est encore vérifié » + corps « **Cochez chaque critère** sur le champignon avant de consommer… »
- 5/5 : carte ✅ olive `rgb(111,143,62)` visible, att masquée
- retour 0/5 : titre **et corps** redeviennent « Rien n'est encore vérifié » / « Cochez chaque critère… » — plus de corps résiduel « Ne consommez pas… ». Le cycle complet est cohérent.

### B-3 (NOUVEAU, P3 UX) — régression du fix P2-2 : la feuille cueillette VIERGE déclenche le garde-fou
`bd04b49` a ajouté `c-meteo` au test de saleté de la feuille cueillette, mais `#c-meteo` est un `<select>` **sans option vide** et `ouvrirSheetCueillette()` l'initialise à `'🌞 Ensoleillé'` → `feuilleSaisieSale()` est **toujours vrai** pour la feuille cueillette, même vierge. Reproduit au runtime : feuille cueillette fraîche (aucun champ touché) + Escape → modale « ⚠️ Feuille non enregistrée / Quitter sans enregistrer ? » (le contrôle négatif qui passait en 26e échoue désormais pour la cueillette ; la feuille spot reste correcte : puces vides, champs vides → fermeture directe sans modale). Erre côté prudence, aucun risque de perte de données, mais confirmation parasite à **chaque** fermeture d'une nouvelle cueillette.
**Fix suggéré (non appliqué, périmètre Assessment B)** : comparer `c-meteo` à la valeur d'ouverture (`'🌞 Ensoleillé'`) au lieu de la chaîne vide, ou exclure `c-meteo` du test, ou ajouter une option vide « — Météo — » comme `c-spot` en a une.

### Nouveaux fixes `bd04b49` vérifiés au runtime (tous verts)
- **P2-1** — filet archive complet : gyromitre masquée → `infoEspece` visible = null mais `infoEspeceArchive('fausse morille')` = gyromitre **MORTEL** (archivee:true, synonyme:true) ; « amanite phaloide » (frappe sans tréma) masquée → phalloïde **MORTELLE** ; « ange destructeur » supprimée → vireuse **MORTELLE** ; variété perso (`especesCustom` + `supprimees`, état type import) → **mortel, perso:true** (exact + Levenshtein `testette mortel`). Limite structurelle assumée : une variété perso réellement effacée de l'IndexedDB (`Stockage.effacer`) n'a plus d'enregistrement consultable — le filet couvre les états masqué/supprimé-logique, pas l'effacement physique des données.
- **P2-2** — garde-fou élargi : puces d'espèces seules (champs texte vides) → modale ✅ ; `c-spot` sélectionné seul → modale ✅ ; contrôle négatif feuille spot propre → fermeture directe ✅ (cf. B-3 pour le cas `c-meteo`).
- **P2-3** — `s-cancel`/`c-cancel` passent par `fermerFeuilleAvecGardeFou` : feuille sale + Annuler → modale ; « Annuler » préserve les champs (« Spot Y » conservé) et laisse la feuille ouverte ✅.
- **P3-1** — toast hors-vocabulaire tiré après le croisement seulement : IA `DELICIEUX` sur espèce connue du guide → le guide résout (badge « Comestible »), **zéro toast** ; IA `DELICIEUX` sur espèce inconnue → toast « ⚠️ Statut IA hors vocabulaire — confirmez la comestibilité » + badge « ⚠️ Inconnu » + « vérifiez avec le guide » ✅.
- **P3-2** — glyphe via BASE_COMPLETE : gyromitre masquée depuis sa propre fiche + bascule d'un critère → titre att **☠️ conservé** (codepoint `2620`) ✅.
- **P3-3** — corps du verdict-att dynamique : voir B-2 ✅.

---

## 5. Étapes navigateur réussies (toutes ✅ sauf une, hors périmètre)

| # | Étape | Résultat observé |
|---|---|---|
| 1 | Chargement + état | SW `cqm-v54` contrôlant après reset caches (4 entrées), globals app OK, titre correct, état des données intact |
| 2 | Filtres (selects) | tous=**21** · mortels=**5** · prudence=**2** · comestibles=**8** · hiver=**1** — ancres exactes (identiques à la 26e) |
| 3 | Verdict dynamique comestible (chanterelle) | 0/5 → `verdict-att` ⚠️ ambre `rgb(217,164,65)` · 5/5 → `verdict-ok` ✅ olive `rgb(111,143,62)` · retour 0/5 → ⚠️ — **corps suit le compteur (B-2 corrigé)** |
| 4 | Verdict dynamique mortel (gyromitre) | 0/5 → `verdict-danger-att` rouge `rgb(179,38,30)` · 5/5 → « **☠️ 5/5 critères vérifiés** » (texte dynamique) · retour 0/5 → danger-att. Valence jamais verte sur mortel |
| 5 | P3-2 glyphe espèce masquée | gyromitre masquée depuis sa fiche + bascule → glyphe ☠️ conservé (codepoint `2620`) |
| 6 | Synonymes (`infoEspece`) | « fausse morille » → gyromitre **mortel** (synonyme) · « amanite phaloide » → phalloïde **mortel** (normalisation d'accents) · « ange destructeur » → vireuse **mortel** · « pied-de-mouton » → comestible · inconnu → null |
| 7 | Filet archive P2-1 | masquées (gyromitre, phalloïde) et supprimée (vireuse) toutes résolues **MORTELLES** par `infoEspeceArchive` (archivee:true) ; variété perso (exact + frappe) → mortel, perso:true |
| 8 | Fail-safe IA sans clé | « 🔑 Clé Gemini manquante — ajoutez-la dans ⚙️ Paramètres. » + « Vérifiez votre clé et votre connexion. » (jamais silencieux) |
| 9 | Croisement IA × guide (P1-1) | IA simulée « comestible 95 % » sur phalloïde → « 🍄 Amanite phalloïde MORTEL ☠️ » + alerte rouge + antipoison 1-800-463-5060 — **jamais de badge vert**, le guide a le dernier mot |
| 10 | P2-1 espèce masquée | phalloïde masquée + IA comestible → **toujours MORTEL**, pas de bouton « 📖 Voir la fiche » (archivee) |
| 11 | P3-1 vocabulaire | `DELICIEUX` + espèce connue → badge « Comestible » (guide résout), **zéro toast** · `DELICIEUX` + inconnue → toast hors-vocabulaire + « ⚠️ Inconnu » + « vérifiez avec le guide » |
| 12 | Analyse annulable | « 🔍 Analyse en cours… » + **✋ Annuler** observable (stub pendante) → `annulerAnalyse()` → « ✋ Analyse annulée. » + [🖼️ Choisir une photo, Fermer] |
| 13 | Import versionné | v4 → « version ANTÉRIEURE (v4) : la checklist terrain sera perdue » · v6 → « version PLUS RÉCENTE (v6)… import risqué » — les deux capturées via `confirmer` stubé |
| 14 | Garde-fou P2-2/P2-3 | puces seules → modale · `c-spot` seul → modale · s-cancel/c-cancel sales → modale · Annuler préserve les champs · feuille spot propre → fermeture directe (contrôle négatif ✅) · **feuille cueillette vierge → modale (B-3, régression)** |
| 15 | Lightbox a11y | `role="dialog"` + `aria-modal="true"` + `aria-label="Photo agrandie"` · focus déplacé dans la lightbox à l'ouverture · **Escape retire le nœud du DOM** · **focus restauré** au déclencheur |
| 16 | Console | **0 erreur JS**, **0 ressource ≥ 400** après reloads complets (avant, pendant et après les sondes) |

**Étape échouée** : injection overlay `/detect.js` (fichier absent — 404 réel + `onerror` confirmé) — seule étape non exécutée, raison précise documentée. Aucun échec imputable à l'app.

---

## 6. Notes de méthode

- Détecteur lancé depuis la racine projet (config `.impeccable/config.json` + DESIGN.md résolus) ; JSON temporaire dans `C:/Users/Jo/AppData/Local/Temp/` (nettoyé).
- 2 échecs de sonde corrigés côté sonde, jamais l'app : parenthèse parasite dans une expression `js()` (SyntaxError) ; ordre restore/snapshot inversé dans un probe d'état.
- Environnement : popup Chrome « Allow remote debugging? » (connu) puis dérive de tab du daemon partagé (page étrangère) — récupérés par retry + re-navigation ; toutes les sondes vérifient `location.href` + un global app avant de conclure.
- État restauré en fin de session : checklists chanterelle/gyromitre 0/5 (état d'origine), `Etat.cachees`/`supprimees`/`especesCustom` vides, spots vides, stubs `confirmer`/`identifierPhotoIA` restaurés, aucune clé IA écrite, aucune modification de code ni du répertoire de la skill impeccable.
- Serveur 8142 arrêté et port vérifié libre (`curl` → 000, `netstat` → aucun LISTEN).

**Synthèse** : 101 findings = 101 faux positifs documentés/advisories connus (composition identique à la 26e, zéro dérive) · runtime 16/17 sondes vertes + 1 étape hors périmètre documentée (overlay absent) · B-1 et B-2 corrigés et vérifiés · 6/6 fixes `bd04b49` vérifiés au runtime · **1 nouveau défaut P3 UX (B-3, régression du garde-fou cueillette)** à corriger au prochain chantier.
