# Assessment B — Détecteur impeccable + preuves navigateur (25e passe)

**Date** : 2026-08-16 · **Cible** : `index.html` (PWA mono-fichier, commit `ff0cfb2`, SW `cqm-v52`)
**Serveur** : `python -m http.server 8142` (port libéré et vérifié après les sondes)
**Verdict global** : runtime 100 % vert sur tous les points de sécurité · **1 nouveau défaut réel P2 + 1 cosmétique P3 trouvés** (voir §4) · 0 défaut bloquant au détecteur (101 findings, tous des faux positifs documentés ou advisories connus)

---

## 1. Findings CLI (detect.mjs --json)

**101 findings** — exit code 2 (findings, pas une erreur), stderr vide.

| Compte | Antipattern | Sévérité | Détail |
|---|---|---|---|
| 4 | bounce-easing | warning | l.111 `cubic-bezier(.2,1.6,.4,1)` · l.241 `(.2,1.5,.4,1)` · l.244 `(.2,1.5,.4,1)` · l.281 `(.2,1.3,.4,1)` |
| 1 | side-tab | warning | l.135 `border-right:3px solid var(--noir)` |
| 1 | broken-image | warning | l.1970 — commentaire JS `// CORS OK en <img>` |
| 1 | em-dash-overuse | warning (advisory) | l.0 — 8 tirets cadratins / 5 336 car. corps = **0,75 / 500** |
| 55 | design-system-radius | advisory | tokens : `999px`×12 · `4px`×9 · `5px`×9 · `16px`×8 · `14px`×7 · `3px`×3 · `6px`×2 · `9px`×2 · `10px`×2 |
| 34 | design-system-font-size | advisory | `14px`×9 · `14.5px`×5 · `11.5px`×4 · `12px`×4 · `22px`×2 · `15px`×2 · `30/32/36px`×3 |
| 5 | design-system-color | advisory | 4× `rgba(0,0,0,.1)` l.137/189/255/347 (contours photos du polish) + 1× `rgba(20,14,8,.92)` l.2365 (overlay lightbox) |

**Totaux par sévérité** : 7 warning · 94 advisory. **Par catégorie** : 6 slop · 95 quality.

---

## 2. Triage — faux positifs identifiés (101/101 expliqués)

| Finding | Verdict | Raisonnement |
|---|---|---|
| side-tab l.135 | **FP en contexte** | Bordure noire 3 px = engagement de marque documenté : DESIGN.md l.116 « bordures noires épaisses (3 px) », l.119 « Bordures noires 3 px partout », l.147 « Règle du Trait Noir ». Le trait EST l'accent, pas un reliquat IA. |
| bounce-easing ×4 | **FP en contexte** | Élasticité délibérée documentée : DESIGN.md l.124 « Élasticité délibérée : cubic-bezier(.2, 1.3-1.6, .4, 1) » + l.173 (feuilles 0,3 s). Les 4 courbes sont dans la plage 1.3–1.6. |
| broken-image l.1970 | **FP** | Le moteur regex scanne le source brut : le `<img>` flaggé est dans le commentaire `// … CORS OK en <img>` (l.1970). `grep -o '<img[^>]*>' | grep -v 'src='` → seule occurrence = ce commentaire. Aucun vrai `<img>` sans `src`. |
| em-dash-overuse | **Partiel (advisory)** | 8 tirets / 5 336 car. de corps (script/style/tags retirés) = 0,75/500, sous le seuil de 1/500 — typographie française standard. Advisory, non compté dans le exit code. |
| design-system-radius ×55 | **FP en contexte** | Le détecteur applique l'échelle frontmatter (`rounded: 8/12/18/24 px`), mais la signature « coin cassé » (4–6 px sur un coin) et les pilules 999 px sont documentées dans DESIGN.md l.180 (« le coin inférieur droit est presque droit (4-6 px)… Boutons et pastilles : pilules (999 px) ») ET dans les composants frontmatter (rounded 999px, l.61-91). Valeurs dominantes : paires coin-cassé + pilules. |
| design-system-font-size ×34 | **Partiel (cohérent)** | Ramp frontmatter 21/20/16/13. Les écarts dominants sont documentés/cohérents : `14.5px` ×5 (le composant `.ds-btn` du design.json l'utilise lui-même), `14px` ×9 (labels/tailles de composants compactes), `11.5/12px` micro-textes (opacité corrigée en passe 11e). Aucun hors-plage aberrant. |
| design-system-color ×5 | **FP en contexte** | 4× `rgba(0,0,0,.1)` = contours de photos (ombres/outlines, pas des couleurs de marque — même famille que les ombres déjà ignorées) ; `rgba(20,14,8,.92)` = overlay lightbox, dérivé du noir de marque, fonctionnel. Les ignoreValues config (`rgba(31,26,23,.08)` / `.5`) produisent **zéro résiduel** cette passe. |

**Aucune dérive réelle de couleur** : les 5 couleurs flaggées sont des overlays/ombres ; la palette marque n'est jamais hors design system.

---

## 3. Findings console navigateur

- **Erreurs JS : 0** (`window.__errs` via CDP `Page.addScriptToEvaluateOnNewDocument` + reload complet → `[]`).
- **Ressources ≥ 400 : 0** (performance entries — 0× 404).
- Service worker : reset caches → re-registré `cqm-v52`, contrôle la page, cache recréé (runtime vérifié sur code frais, pas un cache périmé).

---

## 4. Défauts réels découverts (nouveaux, cette passe)

### B-1 (P2) — Le titre dynamique du verdict « att » force le crâne ☠️ sur les fiches COMESTIBLES
`basculerSpec` (l.1497, fix P3-2 de la 24e) met à jour le titre du verdict « att » avec un emoji **codé en dur** :
```js
if (txtAtt) txtAtt.textContent = '☠️ ' + (nb === 0 ? 'Rien n\'est encore vérifié' : 'Critères manquants');
```
Les deux paires de verdicts partagent l'id `spec-verdict-att` : sur une fiche **mortelle** la carte `verdict-danger-att` doit avoir ☠️ (correct), mais sur une fiche **comestible** la carte ambre `verdict-att` porte ⚠️ au rendu initial… puis ☠️ dès la première bascule.

**Preuve runtime (chanterelle, comestible)** :
- Rendu initial (0 bascule) : `verdict-att` titre « ⚠️ Critères manquants », codepoint **26a0** (⚠️) — correct.
- Après décochage → 0/5 : `verdict-att ouv`, titre « **☠️** Rien n'est encore vérifié », codepoint **2620** (crâne), fond ambre `rgb(217,164,65)` — **crâne sur carte d'avertissement ambre d'une espèce comestible**.
- Les octets du template l.1444 sont bien `e2 9a a0` (⚠️) — le défaut est exclusivement dans la mise à jour dynamique l.1497.
- Contrôle gyromitre (mortel) : danger-att « ☠️ Rien n'est encore vérifié » — correct.

**Pourquoi P2** : le couple ⚠️/☠️ est un canal de sécurité chargé de sens (avertissement vs danger mortel). Un crâne sur la carte de vérification d'une chanterelle dégrade la crédibilité du signal rouge (effet « loup qui crie »), même si l'erreur penche vers la prudence (pas un faux signal de sécurité). **Fix suggéré** (non appliqué, périmètre Assessment B) : `const nonComestible = …` dans `basculerSpec` et `txtAtt.textContent = (nonComestible ? '☠️ ' : '⚠️ ') + (nb === 0 ? 'Rien n\'est encore vérifié' : 'Critères manquants');` + bump SW.

### B-2 (P3, cosmétique) — Le corps de la carte ⚠️ ne suit pas le compteur
Le rendu initial du corps dépend de `nbFaits === 0` (« Cochez chaque critère… » vs « Ne consommez pas tant que tout n'est pas vérifié… »), mais `basculerSpec` ne re-rend que le **titre** — après un cycle cocher/décocher, le corps reste la variante du premier rendu (observé : corps « Ne consommez pas… » à 0/5). Les deux textes interdisent la consommation → **erre côté prudence**, cosmétique. À corriger avec B-1 (re-rendre titre + corps ensemble).

---

## 5. Étapes navigateur réussies (toutes ✅)

| # | Étape | Résultat observé |
|---|---|---|
| 1 | Chargement + état | `index.html` servi, globals app OK, SW `cqm-v52` contrôlant après reset caches |
| 2 | Filtres (selects) | tous=**21** · mortels=**5** (phalloïde, vireuse, galerine, gyromitre, lépiote brunâtre) · hiver=**1** (pleurote) · prudence=**2** (morille, amanite rougissante) · comestibles=**8** — ancres exactes |
| 3 | Verdict dynamique comestible (chanterelle) | 0/5 → `verdict-att` ⚠️ ambre · 5/5 → `verdict-ok` ✅ olive `rgb(111,143,62)` · retour 0/5 → ⚠️ (fix 5e passe tient) — **sauf emoji ☠️ du défaut B-1 après bascule** |
| 4 | Verdict dynamique mortel (gyromitre) | 0/5 → `verdict-danger-att` rouge `rgb(179,38,30)` · 5/5 → `verdict-danger` « **☠️ 5/5 critères vérifiés** » (**texte dynamique — fix 23e vérifié**, plus de « 0/5 » figé) · retour 0/5 → danger-att. Valence jamais verte sur mortel |
| 5 | ARIA checklist | `aria-pressed` true/false suit les bascules · compteur `aria-live="polite"` |
| 6 | Synonymes mortels (`infoEspece`) | « fausse morille » → gyromitre **mortel** (synonyme:true) · « amanite phaloide » → phalloïde **mortel** (Levenshtein) · « ange destructeur » → vireuse **mortel** (inclusion) · « pied-de-mouton » → comestible (fix 17e) · inconnu → null |
| 7 | Croisement IA × guide (P1-1 24e) | IA simulée « comestible 95 % » sur phalloïde → carte rendue « **🍄 amanite phalloïde MORTEL ☠️** » + « ☠️ MORTEL — ne jamais consommer » + antipoison 1-800-463-5060 — **jamais de badge vert**, le guide a le dernier mot |
| 8 | Fail-safe IA sans clé | « 🔑 Clé Gemini manquante — ajoutez-la dans ⚙️ Paramètres » (jamais silencieux) |
| 9 | Analyse annulable | « Analyse en cours… » + bouton **✋ Annuler** observable (stub never-resolving) → `annulerAnalyse()` → « ✋ Analyse annulée. » + [🖼️ Choisir une photo, Fermer] |
| 10 | Import versionné | v4 → modale « version ANTÉRIEURE (v4) : la checklist terrain sera perdue » · v6 → « version PLUS RÉCENTE (v6)… import risqué » — les deux capturées via `confirmer` |
| 11 | Lightbox a11y | `role="dialog"` + `aria-modal="true"` + `aria-label="Photo agrandie"` · focus à l'intérieur · **Escape ferme** (nœud retiré du DOM) · **focus restauré** au déclencheur |
| 12 | Console | **0 erreur JS**, **0 ressource ≥ 400** après reload complet |

**Étape échouée** : aucune.

## 6. Notes de méthode

- Sondes navigateur menées par lots courts (< 3 s d'attente par appel `js()`) : le harness `browser_exec` de cet hôte **timeout l'IPC** sur les IIFE async à nombreux `await` (~15 timers) — les sondes trop longues ont continué de s'exécuter en arrière-plan (état checklist pollué puis remis à 0/5 en fin de passe). Limitation du harness, pas de l'app.
- Détecteur lancé depuis la racine projet (config `.impeccable/config.json` + DESIGN.md résolus) ; JSON dans `C:/Users/Jo/AppData/Local/Temp/detect_b25.json` (nettoyé après rapport).
- Aucune modification de code ni du répertoire de la skill impeccable ; serveur 8142 arrêté et port vérifié libre (`curl` → 000, `netstat` → aucun LISTEN).
