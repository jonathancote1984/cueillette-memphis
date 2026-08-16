# Assessment B — Détecteur impeccable + preuves navigateur (26e passe)

**Date** : 2026-08-16 · **Cible** : `index.html` (PWA mono-fichier, commit `2751ec4`, SW `cqm-v53`)
**Serveur** : `python -m http.server 8142` (port libéré et vérifié après les sondes)
**Verdict global** : runtime 100 % vert sur tous les points de sécurité · **fix P2-2 (25e) vérifié au runtime** · **B-2 (P3 cosmétique, 25e) toujours présent** · 0 défaut bloquant au détecteur (101 findings, tous des faux positifs documentés ou advisories connus)

---

## 1. Findings CLI (detect.mjs --json)

**101 findings** — exit code 2 (findings, pas une erreur), stderr vide.

| Compte | Antipattern | Sévérité | Détail |
|---|---|---|---|
| 1 | side-tab | warning | l.135 `border-right:3px solid var(--noir)` |
| 4 | bounce-easing | warning | l.111 `cubic-bezier(.2,1.6,.4,1)` · l.241/244 `(.2,1.5,.4,1)` · l.281 `(.2,1.3,.4,1)` |
| 1 | broken-image | warning | l.1992 — commentaire JS `// … CORS OK en <img>` (décalé de 22 lignes vs 25e, même commentaire) |
| 1 | em-dash-overuse | warning (advisory) | l.0 — 8 tirets cadratins / 5 336 car. corps = **0,75 / 500** (sous le seuil de 1/500) |
| 55 | design-system-radius | advisory | tokens : `999px`×12 · `5px`×9 · `4px`×9 · `16px`×8 · `14px`×7 · `3px`×3 · `6px`×2 · `9px`×2 · `10px`×2 · `20px`×1 |
| 34 | design-system-font-size | advisory | `14px`×9 · `14.5px`×5 · `11.5px`×4 · `12px`×4 · `22px`×2 · `15px`×2 · `30/32/36/48/24/18/17/10.5px`×1 chaque |
| 5 | design-system-color | advisory | 4× `rgba(0,0,0,.1)` l.137/189/255/347 (contours photos) + 1× `rgba(20,14,8,.92)` l.2387 (overlay lightbox) |

**Totaux par sévérité** : 7 warning · 94 advisory. **Par catégorie** : 6 slop · 95 quality.

Composition identique à la 25e passe (mêmes règles, mêmes totaux). Les décalages de lignes et les nouveaux numéros (l.554, l.1477/1481/1484, l.1677, l.2431–2483, l.2497, l.2719/2722) correspondent au code ajouté par `2751ec4` (garde-fou P3-1, carte idphoto) — aucun nouvel antipattern introduit.

---

## 2. Triage — faux positifs identifiés (101/101 expliqués)

| Finding | Verdict | Raisonnement |
|---|---|---|
| side-tab l.135 | **FP en contexte** | Bordure noire 3 px = engagement de marque documenté : DESIGN.md « bordures noires épaisses (3 px) », « Règle du Trait Noir ». Le trait EST l'accent. |
| bounce-easing ×4 | **FP en contexte** | DESIGN.md « Élasticité délibérée : cubic-bezier(.2, 1.3-1.6, .4, 1) » — les 4 courbes sont dans la plage 1.3–1.6. |
| broken-image l.1992 | **FP** | Le `<img>` flaggé est dans le commentaire `// … CORS OK en <img>`. Aucun vrai `<img>` sans `src` (vérifié sur le source). |
| em-dash-overuse | **Partiel (advisory)** | 8 tirets / 5 336 car. de corps = 0,75/500, sous le seuil — typographie française standard. |
| design-system-radius ×55 | **FP en contexte** | Échelle frontmatter 8/12/18/24 px vs signature « coin cassé » (3–6 px sur un coin) et pilules 999 px documentées dans DESIGN.md (l.180) et les composants frontmatter. Paires dominantes : `14px 4px`×7, `16px 5px`×8, `18px 5px`, pilules ×12, mini-coins cassés `9px 3px`/`10px`/`6px` sur vignettes et suggestions (même patron à petite échelle). |
| design-system-font-size ×34 | **Partiel (cohérent)** | Ramp frontmatter 21/20/16/13. Dominantes documentées/cohérentes : `14.5px` ×5 (le composant `.ds-btn` du design.json l'utilise lui-même), `14px` ×9, micro-textes `10.5–12px`. Nouveaux numéros de ligne : l.554 (note 12 px « Touchez une espèce… », feuille spot), l.1477/1481/1484 (carte idphoto : 17/14/14.5 px inline) — même familles déjà triées en 25e. Aucun hors-plage aberrant. |
| design-system-color ×5 | **FP en contexte** | 4× `rgba(0,0,0,.1)` = contours de photos (pas des couleurs de marque) ; `rgba(20,14,8,.92)` = overlay lightbox dérivé du noir de marque. Les ignoreValues config (`rgba(31,26,23,.08)`/`.5`) produisent **zéro résiduel**. |

**Aucune dérive réelle** : couleurs, courbes et coins flaggés sont tous des patterns documentés.

---

## 3. Findings console navigateur

- **Erreurs JS : 0** (`window.__errs` via CDP `Page.addScriptToEvaluateOnNewDocument` + reloads complets → `[]` à chaque lecture, y compris après toutes les sondes).
- **Ressources ≥ 400 : 0** (performance entries — aucun 404, y compris `img/especes/*`).
- Service worker : reset des caches (ancien `cqm-v52` supprimé) → re-registré **`cqm-v53`**, `controller: true`, cache `cqm-v53` recréé — runtime vérifié sur code frais, pas un cache périmé.
- Audit final après reload complet : 0 erreur, 0 ressource ≥ 400, titre « 🐴 Cueillette Québec — édition Memphis ».

---

## 4. Défauts — suivi 25e → 26e

### B-1 (P2, 25e) — ☠️ forcé sur les fiches comestibles → **CORRIGÉ (fix P2-2 de `2751ec4`), vérifié au runtime**
`basculerSpec` (l.1516) calcule désormais `glypheAtt` selon le statut de l'espèce (`☠️` réservé aux non-comestibles, `⚠️` sinon). Preuves :
- Chanterelle (comestible), cycle 0/5 → 5/5 → 0/5 : titre de la carte att **toujours ⚠️** (codepoint `26a0`), y compris après bascule — plus de crâne sur la carte ambre `rgb(217,164,65)`.
- Gyromitre (mortel) : titre att `☠️` (codepoint `2620`) — correct.

### B-2 (P3 cosmétique, 25e) — le corps de la carte ⚠️ ne suit toujours pas le compteur → **TOUJOURS PRÉSENT**
Reproduit au runtime : fiche chanterelle à 1/5 (re-ouverte → corps « Ne consommez pas tant que tout n'est pas vérifié… »), puis décochage → 0/5 : le titre redevient « ⚠️ Rien n'est encore vérifié » mais le **corps reste** « Ne consommez pas… » au lieu de « Cochez chaque critère… ». Les deux textes interdisent la consommation → erre côté prudence, cosmétique. Le fix `2751ec4` n'a traité que le glyphe (P2-2), pas le corps. Fix suggéré (non appliqué, périmètre Assessment B) : re-rendre titre + corps ensemble dans `basculerSpec`.

### Nouveaux fixes `2751ec4` vérifiés au runtime (tous verts)
- **P2-1** — phalloïde **masquée** (`Etat.cachees`) + IA simulée « comestible 95 % » → carte toujours « 🍄 amanite phalloïde MORTEL ☠️ » + alerte rouge + antipoison 1-800-463-5060, **jamais de badge vert** ; bouton « 📖 Voir la fiche du guide » absent (espèce archivée) — le filet couvre les masquées/supprimées.
- **P2-3** — statut IA en majuscules (`COMESTIBLE`) accepté sans toast ; statut hors vocabulaire (`DELICIEUX`) → toast « ⚠️ Statut IA hors vocabulaire — confirmez la comestibilité » + badge « ⚠️ Inconnu » + alerte « Vérifiez avec le guide ».
- **P3-1** — garde-fou des feuilles : feuille cueillette sale (espèce remplie) → **voile**, **Escape** et **poignée** déclenchent tous la modale réelle « ⚠️ Feuille non enregistrée / Quitter sans enregistrer ? Les champs remplis seront perdus. » ; Annuler préserve les champs et la feuille ; Oui ferme. Contrôle négatif : feuille propre → fermeture directe sans modale. Variante spot (s-nom rempli) : même garde-fou.

---

## 5. Étapes navigateur réussies (toutes ✅)

| # | Étape | Résultat observé |
|---|---|---|
| 1 | Chargement + état | SW `cqm-v53` contrôlant après reset caches, globals app OK, titre correct |
| 2 | Filtres (selects) | tous=**21** · mortels=**5** (phalloïde, vireuse, galerine, gyromitre, lépiote brunâtre) · hiver=**1** (pleurote) · prudence=**2** (morille, amanite rougissante) · comestibles=**8** — ancres exactes |
| 3 | Verdict dynamique comestible (chanterelle) | 0/5 → `verdict-att` ⚠️ ambre · 5/5 → `verdict-ok` ✅ olive `rgb(111,143,62)` · retour 0/5 → ⚠️ — **glyphe ⚠️ confirmé après bascule (B-1 corrigé)** |
| 4 | Verdict dynamique mortel (gyromitre) | 0/5 → `verdict-danger-att` rouge `rgb(179,38,30)` · 5/5 → `verdict-danger` « **☠️ 5/5 critères vérifiés** » (texte dynamique) · retour 0/5 → danger-att. Valence jamais verte sur mortel |
| 5 | ARIA checklist | `aria-pressed` true/false suit les bascules (5/5 → true×5, 0/5 → false×5) · compteur `#spec-compteur` `aria-live="polite"` (source l.1452) mis à jour à chaque bascule · état persistant (re-ouverture de fiche à 1/5) |
| 6 | Synonymes mortels (`infoEspece`) | « fausse morille » → gyromitre **mortel** (synonyme:true) · « amanite phaloide » → phalloïde **mortel** (Levenshtein) · « ange destructeur » → vireuse **mortel** (inclusion) · « pied-de-mouton » → comestible · inconnu → null |
| 7 | Croisement IA × guide (P1-1) | IA simulée « comestible 95 % » sur phalloïde → « 🍄 amanite phalloïde MORTEL ☠️ » + alerte rouge + antipoison — **jamais de badge vert**, le guide a le dernier mot |
| 8 | P2-1 espèce masquée | phalloïde masquée + IA comestible → **toujours MORTEL**, pas de bouton fiche (archivée) |
| 9 | P2-3 vocabulaire | `COMESTIBLE` majuscule → badge Comestible sans toast ; `DELICIEUX` → toast hors-vocabulaire + « ⚠️ Inconnu » + « Vérifiez avec le guide » |
| 10 | Fail-safe IA sans clé | « 🔑 Clé Gemini manquante — ajoutez-la dans ⚙️ Paramètres. » (jamais silencieux) |
| 11 | Analyse annulable | « 🔍 Analyse en cours… » + **✋ Annuler** observable (stub pendante) → `annulerAnalyse()` → « ✋ Analyse annulée. » + [🖼️ Choisir une photo, Fermer] |
| 12 | Import versionné | v4 → « version ANTÉRIEURE (v4) : la checklist terrain sera perdue » · v6 → « version PLUS RÉCENTE (v6)… import risqué » — les deux capturées via `confirmer` |
| 13 | Lightbox a11y | `role="dialog"` + `aria-modal="true"` + `aria-label="Photo agrandie"` · focus déplacé dans la lightbox à l'ouverture · **Escape ferme** (nœud retiré du DOM) · **focus restauré** au déclencheur |
| 14 | Garde-fou P3-1 | voile + Escape + poignée → modale de confirmation sur feuille sale ; Annuler préserve ; Oui ferme ; feuille propre → fermeture directe (contrôle négatif) |
| 15 | Console | **0 erreur JS**, **0 ressource ≥ 400** après reloads complets (avant, pendant et après les sondes) |

**Étape échouée** : aucune (2 échecs de sonde corrigés côté sonde, voir §6 — jamais l'app).

---

## 6. Notes de méthode

- **Timeout IPC du harness sur IIFE async à nombreux `await`** (documenté) : les bascules de checklist ont été menées à coups de clics unitaires + pauses Python (état relu à chaque pas). Une IIFE async (5 clics × 200 ms) a timeouté mais a fini de s'exécuter en arrière-plan (checklist 5/5 lue ensuite) — limitation du harness, pas de l'app.
- **Piège de sonde — `js()` attend la promesse retournée** : `js("eval(\"analyserPhoto(...)\")")` retourne la promesse de l'app ; avec un stub never-resolving, le harness timeout. Correctif : suffixer `; 'started'` pour ne pas renvoyer la promesse. Échec de sonde, pas de l'app.
- **Piège de citation** : `eval("Etat.cachees.push('phalloide'); 'masque')")` contenait une parenthèse parasite (SyntaxError) — reformulé sans chaîne finale. Échec de sonde.
- Détecteur lancé depuis la racine projet (config `.impeccable/config.json` + DESIGN.md résolus) ; JSON temporaire dans `C:/Users/Jo/AppData/Local/Temp/` (nettoyé).
- État de la checklist remis à 0/5 sur les deux fiches sondées ; clé IA de test supprimée ; `identifierPhotoIA`/`confirmer` restaurés ; aucune modification de code ni du répertoire de la skill impeccable.
- Serveur 8142 arrêté et port vérifié libre (`curl` → 000, `netstat` → aucun LISTEN).
