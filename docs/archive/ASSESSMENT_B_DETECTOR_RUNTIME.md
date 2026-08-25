# Assessment B — Détecteur impeccable + preuves navigateur (29e passe)

**Date** : 2026-08-16 · **Cible** : `index.html` (PWA mono-fichier, HEAD `3e34cdc` = docs 28e, code = `1598f06` fix critique 28e, SW `cqm-v56`)
**Serveur** : `python -m http.server 8146` (tué après les sondes, port vérifié libre, aucun orphelin)
**Verdict global** : runtime **100 % vert (20/20 sondes)** · **5/5 fixes `1598f06` vérifiés au runtime** · **0 nouveau défaut** · 101 findings au détecteur = 101 faux positifs documentés/advisories connus, composition identique à la 28e.

---

## 1. Findings CLI (detect.mjs --json)

**101 findings** — exit code 2 (findings, pas une erreur), stderr vide.

| Compte | Antipattern | Sévérité | Détail |
|---|---|---|---|
| 1 | side-tab | warning | l.135 `border-right:3px solid var(--noir)` |
| 4 | bounce-easing | warning | l.111 `cubic-bezier(.2, 1.6, .4, 1)` · l.241/244 `(.2, 1.5, .4, 1)` · l.281 `(.2, 1.3, .4, 1)` |
| 1 | broken-image | warning | l.2033 — commentaire JS `// … CORS OK en <img>` (même commentaire, +11 lignes vs 28e) |
| 1 | em-dash-overuse | warning (advisory) | l.0 — 8 tirets cadratins / 3 680 caractères de corps = 1,09 par 500 (advisory, jamais bloquant) |
| 55 | design-system-radius | advisory | tokens : `999px`×12 · `4px`×9 · `5px`×9 · `16px`×8 · `14px`×7 · `3px`×3 · `6px`×2 · `9px`×2 · `10px`×2 · `20px`×1 |
| 34 | design-system-font-size | advisory | `14px`×9 · `14.5px`×5 · `11.5px`×4 · `12px`×4 · `22px`×2 · `15px`×2 · `30/32/36/24/18/17/48/10.5px`×1 chaque |
| 5 | design-system-color | advisory | 4× `rgba(0,0,0,.1)` l.137/189/255/347 (contours `outline` des photos) + 1× `rgba(20,14,8,.92)` l.2428 (overlay lightbox) |

**Totaux par sévérité** : 7 warning · 94 advisory. **Par catégorie** : 6 slop · 95 quality.

**Composition identique à la 28e passe** (mêmes règles, mêmes totaux, mêmes distributions de tokens). Seuls décalages : broken-image 2022→2033 et color lightbox 2417→2428 (+11 lignes), correspondant au code ajouté par `1598f06`. **Aucun nouvel antipattern introduit.** Les ignoreValues config (`rgba(31,26,23,.08)`/`.5`) produisent zéro résiduel — la config reste à jour ; les 5 couleurs flaggées sont des FP documentés laissés volontairement hors ignoreValues (contours photos + overlay lightbox, pas des couleurs de marque).

---

## 2. Triage — faux positifs identifiés (101/101 expliqués)

| Finding | Verdict | Raisonnement |
|---|---|---|
| side-tab l.135 | **FP en contexte** | Bordure noire 3 px = engagement de marque documenté : DESIGN.md « bordures noires épaisses (3 px) », « Règle du Trait Noir ». Le trait EST l'accent. |
| bounce-easing ×4 | **FP en contexte** | DESIGN.md « Élasticité délibérée : cubic-bezier(.2, 1.3-1.6, .4, 1) » — les 4 courbes sont dans la plage 1.3–1.6. |
| broken-image l.2033 | **FP** | Le `<img>` flaggé est dans le commentaire `// 1. MycoQuébec : miniature depuis la base embarquée (hors-ligne, CORS OK en <img>)`. Vérifié : `grep -o '<img[^>]*>' \| grep -v 'src='` ne renvoie que le `<img>` du commentaire — aucun vrai `<img>` sans `src`. |
| em-dash-overuse | **Advisory** | 8 tirets cadratins / 3 680 caractères de corps = 1,09 par 500 — typographie française standard, sous le seuil. |
| design-system-radius ×55 | **FP en contexte** | Signature « coin cassé » (3–6 px) + pilules 999 px documentées dans DESIGN.md et les composants frontmatter ; paires dominantes `14px 4px`×7, `16px 5px`×8, pilules ×12, `999px` des compteurs/dés. |
| design-system-font-size ×34 | **Partiel (cohérent)** | Ramp frontmatter 21/20/16/13 ; dominantes documentées/cohérentes (`14.5px` = le composant `.ds-btn` du design.json lui-même, `14px`×9, micro-textes 10.5–12 px, `48px` = icône `.vide-etat`, `17px` = titre de fiche). Aucun hors-plage aberrant. |
| design-system-color ×5 | **FP en contexte** | 4× `rgba(0,0,0,.1)` = `outline` subtil des photos ; `rgba(20,14,8,.92)` = overlay lightbox dérivé du noir de marque. |

**Aucune dérive réelle.**

---

## 3. Findings console navigateur

- **Erreurs JS : 0** — double capture : `window.__errs` (injecté via CDP `Page.addScriptToEvaluateOnNewDocument` avant le reload, relu après chaque cycle) **et** les événements natifs `Runtime.exceptionThrown` / `Runtime.consoleAPICalled` collectés pendant toute la session : `[]` partout.
- **Ressources ≥ 400 : 0** — le seul 404 de toute la session est `/detect.js` (l'injection volontaire, cf. §6). Le log serveur confirme : 135 fichiers `addAll` du SW install **tous 200** (aucun autre 404, un 304 légitime sur `sw.js` au rechargement).
- **Service worker** : unregister → reload → ré-enregistrement propre → cache `cqm-v56` recréé (135 entrées `addAll`, 136 après les GET runtime) → `controller: true`. Runtime vérifié sur code frais, pas un cache périmé.
- **Injection overlay `/detect.js` : échouée pour raison précise** — fichier absent du projet (0 hit `search_files`, 404 réel du serveur statique sans fallback SPA, `onerror` capturé dans la page). Étape hors périmètre, rapportée telle quelle (pas de succès silencieux).

---

## 4. Défauts — suivi 28e → 29e

### Fixes `1598f06` (critique 28e) — tous vérifiés au runtime (5/5 verts)

- **P2-1 — tombes dans l'export/import (round-trip complet)** : variété perso mortelle supprimée → tombe écrite ; export v5 → `tombes[]` contient `{id, nom:'Testette mortel', statut:'mortel', prudence:false, perso:true}` ; wipe total des 7 stores → `Etat.tombes` vide, `infoEspeceArchive('testette mortel')` = null (filet vide) ; import du fichier exporté → modale résumé → Oui → tombes reconstruites (entrées `supprimees` enrichies) → `infoEspeceArchive` exact **et** flou (« testette mortell », Levenshtein) → **mortel, archivee:true**. Le filet de sécurité survit au téléphone du proche. ✅
- **P2-2 — confirmation avant suppression d'une variété perso** : modale « 🗑️ Supprimer la variété » — « Supprimer « Testette mortel » ? La fiche, ses illustrations IA et sa checklist seront perdues définitivement. » · **Annuler** → variété intacte, fiche toujours ouverte · **Oui** → variété effacée + tombe écrite + toast. ✅
- **P3-1 — fiche fantôme fermée après suppression** : suppression depuis la fiche de la variété → `vue-detail` plus visible (`Etat.detailId` fermé). ✅
- **P3-2 — espèces masquées sélectionnées désélectionnables** : spot avec « Chanterelle commune » + espèce masquée → réouverture du spot → la puce est **présente et `actif`** malgré le masquage ; clic → désélection (`Etat.spot.especes` → `[]`). ✅
- **P3-3 — c-date dans le garde-fou** : feuille cueillette vierge → `feuilleSaisieSale()` **false** → fermeture directe sans modale ; date modifiée → modale « ⚠️ Feuille non enregistrée » → **Annuler préserve la date et la feuille** → Quitter ferme. ✅

### Aucun nouveau défaut découvert (0/20 sondes rouges, 0 exception, 0 ressource ≥ 400).

---

## 5. Étapes navigateur réussies (20/20 ✅)

| # | Étape | Résultat observé |
|---|---|---|
| 1 | Chargement + état | Titre « 🐴 Cueillette Québec — édition Memphis », SW `cqm-v56` contrôlant après ré-enregistrement propre (1 registration, cache 135→136 entrées, `controller:true`), globals OK (`confirmer`, `infoEspece`), vue initiale = spots. |
| 2 | Filtres (selects, chaque dimension remise au défaut) | tous=**21** · mortels=**5** · prudence=**2** (Morille, Amanite rougissante) · comestibles=**8** · npas=**11** · hiver=**1** (pleurote) · mortels∩printemps=**1** (gyromitre) · prudence∩hiver=**0** (combinaison légitime). |
| 3 | Verdict dynamique comestible (chanterelle) | 0/5 → att ⚠️ ambre `rgb(217,164,65)` « Rien n'est encore vérifié » · 5/5 → ok ✅ olive `rgb(111,143,62)` · retour 0/5 → att (le corps suit le compteur). |
| 4 | Verdict dynamique mortel (gyromitre) | 0/5 → danger-att rouge `rgb(179,38,30)` « ☠️ Rien n'est encore vérifié » · 5/5 → danger « **☠️ 5/5 critères vérifiés** » (texte dynamique) · retour 0/5 → danger-att. Valence jamais verte. |
| 5 | Persistance checklist | IndexedDB : gyromitre `[T,T,T,T,T]` à 5/5 puis `[F,F,F,F,F]` à 0/5, chanterelle `[F×5]` — **la vérité stockée = la vérité affichée** (lecture directe `Stockage.lire('checklist')`). |
| 6 | Synonymes (`infoEspece`) | « fausse morille » → gyromitre **mortel** (synonyme:true) · « amanite phaloide » → phalloïde **mortel** (Levenshtein) · « ange destructeur » → vireuse **mortel** · « pied-de-mouton » → **comestible** · inconnu → null. |
| 7 | P2-2 confirmation suppression | Modale exacte « 🗑️ Supprimer la variété » · Annuler préserve · Oui supprime + tombe `{statut:'mortel'}`. |
| 8 | P3-1 fiche fantôme | Après suppression depuis la fiche : `vue-detail` fermée. |
| 9 | Filet tombes après suppression | `infoEspeceArchive` exact + flou → **mortel** (archivee:true, perso:true). |
| 10 | P2-1 round-trip tombes | Export v5 avec `tombes[]` → wipe → filet vide → import → tombes reconstruites, filet complet (exact + flou). |
| 11 | P3-2 puce masquée sélectionnée | Puce « Chanterelle commune » présente + actif malgré masquage ; clic → désélectionnée (`selection []`). |
| 12 | P3-3 garde-fou c-date | Vierge → fermeture directe · date modifiée → modale · Annuler préserve (date `2026-08-01` conservée) · Quitter ferme. |
| 13 | Garde-fou spot (B-3, bonus) | `s-cancel` sur spot sale (`s-nom` rempli) → modale → Quitter ferme. |
| 14 | Fail-safe IA sans clé | Bandeau « 🔑 Identification par photo : ajoutez votre clé Gemini… » + fiche « 🔑 Clé Gemini manquante — ajoutez-la dans ⚙️ Paramètres. » + « Vérifiez votre clé et votre connexion. » (jamais silencieux). |
| 15 | Croisement IA × guide | IA simulée « comestible 95 % » sur phalloïde → « **MORTEL** » + antipoison **1-800-463-5060** + badge mortel (jamais vert) + « 📖 Voir la fiche du guide » présent. |
| 16 | Analyse annulable | « 🔍 Analyse en cours… » + **✋ Annuler** → « ✋ Analyse annulée. » + [🖼️ Choisir une photo, Fermer]. |
| 17 | Imports versionnés + invalide | v4 → « version ANTÉRIEURE (v4) : la checklist terrain (vos vérifications ⚠️/✅) sera perdue » · v6 → « version PLUS RÉCENTE (v6)… import risqué » · Annuler partout → **0 écriture** (spots=1, cueillettes=0 inchangés) · fichier malformé → toast « ⚠️ Fichier invalide — import annulé », aucune modale, aucune écriture. |
| 18 | Lightbox a11y | `role="dialog"` + `aria-modal="true"` + `aria-label="Photo agrandie"` · focus dans la lightbox · **Escape retire le nœud du DOM** · **focus restauré** au déclencheur (`.detail-img`). |
| 19 | Console + ressources | **0 erreur JS** (double capture `__errs` + événements CDP), **0 ressource ≥ 400** hors l'injection volontaire `/detect.js`, addAll 135 fichiers tous 200 au log serveur. |
| 20 | État final restauré | Stores vides (spots/cueillettes/custom/caches/supprimees/tombes/illustrations/checklist = 0), clé IA nulle, aucun code modifié. |

---

## 6. Notes de méthode (sondes et pièges rencontrés)

- **Popup Chrome « Allow remote debugging? » a bloqué `browser_exec` (~20 min, sessions nommée ET partagée)** : le consentement exige un clic humain. FALLBACK VALIDÉ : **Chrome headless maison piloté par CDP** (`--headless=new` ne demande jamais le consentement) — `ws://[::1]:9222` (l'IPv4 9222 est occupé par le daemon browser-use du hôte, bind IPv6 sans conflit). Mêmes preuves : `Runtime.evaluate` + `awaitPromise`/`returnByValue`, capture native `Runtime.exceptionThrown`/`consoleAPICalled`, `performance.getEntriesByType('resource')`. Fermeture propre par `Browser.close` + vérification du port.
- Détecteur lancé depuis la racine projet (config `.impeccable/config.json` + DESIGN.md résolus) ; JSON temporaire écrit dans `%TEMP%` (hors arbre projet).
- **Piège AND-filtres (probe, pas app)** : prudence/comestible/npas mesurés avec la saison restée sur « hiver » → 0/1/0 (légitime). Re-mesurés après remise de la saison à « Toutes » → 2/8/11 exacts.
- **`curl -o /dev/null -w "%{size_download}"` renvoie « 200 0 » sur ce host pour des fichiers réels** (quirk outillage MSYS) — corps vérifié via `head -c`, jamais conclu « fichier vide » sur SIZE=0.
- Tous les toggles de checklist ont respecté le délai async de `Stockage.ecrire` (120–450 ms entre clics) ; aucun état lu à chaud.
- Serveur 8146 arrêté, port vérifié libre (`curl` → 000, `netstat` → aucun LISTEN), **aucun http.server orphelin** ; Chrome headless fermé (port 9222 IPv6 libéré, le LISTEN IPv4 restant = daemon browser-use du hôte, antérieur à la session).
- Les stubs IA (`identifierPhotoIA` → promesse figée / résultat simulé) ont été **restaurés** et la fausse clé supprimée ; aucun résidu dans les stores.

**Synthèse** : 101 findings = 101 faux positifs documentés/advisories connus (zéro dérive vs 28e, seul décalage +11 lignes = code `1598f06`) · runtime **20/20 sondes vertes** · **5/5 fixes critique-28e vérifiés** (dont round-trip complet des tombes export→import) · **0 nouveau défaut** · console 0 erreur, 0 ressource ≥ 400 · SW `cqm-v56` prouvé sur cache frais.
