# Assessment B — Détecteur impeccable + preuves navigateur (28e passe)

**Date** : 2026-08-16 · **Cible** : `index.html` (PWA mono-fichier, HEAD `33351cc` = archive docs 27e, code = `b87d1dd` fix critique 27e, SW `cqm-v55`)
**Serveur** : `python -m http.server 8146` (tué après les sondes, port vérifié libre, aucun orphelin)
**Verdict global** : runtime **100 % vert** (18/18 sondes) · **B-3 (27e) CORRIGÉ et vérifié au runtime** · 6/6 fixes `b87d1dd` vérifiés · **0 nouveau défaut** · 101 findings au détecteur = 101 faux positifs documentés/advisories connus, composition identique à la 27e.

---

## 1. Findings CLI (detect.mjs --json)

**101 findings** — exit code 2 (findings, pas une erreur), stderr vide.

| Compte | Antipattern | Sévérité | Détail |
|---|---|---|---|
| 1 | side-tab | warning | l.135 `border-right:3px solid var(--noir)` |
| 4 | bounce-easing | warning | l.111 `cubic-bezier(.2, 1.6, .4, 1)` · l.241/244 `(.2, 1.5, .4, 1)` · l.281 `(.2, 1.3, .4, 1)` |
| 1 | broken-image | warning | l.2022 — commentaire JS `// … CORS OK en <img>` (même commentaire, +5 lignes vs 27e) |
| 1 | em-dash-overuse | warning (advisory) | l.0 — 8 tirets cadratins (advisory, jamais bloquant) |
| 55 | design-system-radius | advisory | tokens : `999px`×12 · `4px`×9 · `5px`×9 · `16px`×8 · `14px`×7 · `3px`×3 · `6px`×2 · `9px`×2 · `10px`×2 · `20px`×1 |
| 34 | design-system-font-size | advisory | `14px`×9 · `14.5px`×5 · `11.5px`×4 · `12px`×4 · `22px`×2 · `15px`×2 · `30/32/36/24/18/17/10.5px`×1 chaque |
| 5 | design-system-color | advisory | 4× `rgba(0,0,0,.1)` l.137/189/255/347 (contours photos) + 1× `rgba(20,14,8,.92)` l.2417 (overlay lightbox) |

**Totaux par sévérité** : 7 warning · 94 advisory. **Par catégorie** : 6 slop · 95 quality.

**Composition identique à la 27e passe** (mêmes règles, mêmes totaux, mêmes distributions de tokens). Seuls décalages : broken-image 2017→2022 et color lightbox 2412→2417 (+5 lignes), correspondant au code ajouté par `b87d1dd`. **Aucun nouvel antipattern introduit.** Les ignoreValues config (`rgba(31,26,23,.08)`/`.5`) produisent zéro résiduel — la config reste à jour ; les 5 couleurs flaggées sont des FP documentés laissés volontairement hors ignoreValues (contours photos + overlay lightbox, pas des couleurs de marque).

---

## 2. Triage — faux positifs identifiés (101/101 expliqués)

| Finding | Verdict | Raisonnement |
|---|---|---|
| side-tab l.135 | **FP en contexte** | Bordure noire 3 px = engagement de marque documenté : DESIGN.md « bordures noires épaisses (3 px) », « Règle du Trait Noir ». Le trait EST l'accent. |
| bounce-easing ×4 | **FP en contexte** | DESIGN.md « Élasticité délibérée : cubic-bezier(.2, 1.3-1.6, .4, 1) » — les 4 courbes sont dans la plage 1.3–1.6. |
| broken-image l.2022 | **FP** | Le `<img>` flaggé est dans le commentaire `// 1. MycoQuébec : miniature depuis la base embarquée (hors-ligne, CORS OK en <img>)`. Aucun vrai `<img>` sans `src`. |
| em-dash-overuse | **Advisory** | 8 tirets cadratins — typographie française standard, sous le seuil. |
| design-system-radius ×55 | **FP en contexte** | Signature « coin cassé » (3–6 px) + pilules 999 px documentées dans DESIGN.md et les composants frontmatter ; paires dominantes `14px 4px`×7, `16px 5px`×8, pilules ×12. |
| design-system-font-size ×34 | **Partiel (cohérent)** | Ramp frontmatter 21/20/16/13 ; dominantes documentées/cohérentes (`14.5px` = le composant `.ds-btn` du design.json lui-même, `14px`×9, micro-textes 10.5–12 px). Aucun hors-plage aberrant. |
| design-system-color ×5 | **FP en contexte** | 4× `rgba(0,0,0,.1)` = contours de photos ; `rgba(20,14,8,.92)` = overlay lightbox dérivé du noir de marque. |

**Aucune dérive réelle.**

---

## 3. Findings console navigateur

- **Erreurs JS : 0** (`window.__errs` via CDP `Page.addScriptToEvaluateOnNewDocument` + reloads complets → `[]` avant, pendant et après toutes les sondes).
- **Ressources ≥ 400 : 0** (performance entries — aucun 404, `img/especes/*` et `img/specs/*` tous servis 200).
- Service worker : unregister → ré-enregistrement propre → install `addAll` complet (135 fichiers, **tous 200** dans le log serveur) → cache `cqm-v55` recréé (**136 entrées**), `controller: true`. Runtime vérifié sur code frais, pas un cache périmé.
- Injection overlay `/detect.js` : **échouée pour raison précise** — fichier absent du projet (404 réel, pas de fallback SPA). Étape hors périmètre, rapportée telle quelle (pas de succès silencieux).

---

## 4. Défauts — suivi 27e → 28e

### B-3 (P3 UX, 27e) — garde-fou déclenché sur feuille cueillette VIERGE → **CORRIGÉ (P2-1 de `b87d1dd`), vérifié au runtime**

- Feuille cueillette fraîche (aucun champ touché) : `feuilleSaisieSale()` = **false** (comparaison `c-meteo` vs `meteoInitial` = `'🌞 Ensoleillé'`), fermeture **directe sans modale** — le contrôle négatif qui échouait en 27e passe désormais.
- Feuille cueillette sale (`c-note` rempli) : modale « ⚠️ Feuille non enregistrée » → Annuler **préserve le champ** et laisse la feuille ouverte ; Quitter ferme.
- Feuille spot : vierge → fermeture directe ; sale (`s-nom`) → modale + Annuler préserve.
- **Aucun nouveau défaut découvert** sur l'ensemble des sondes.

### Nouveaux fixes `b87d1dd` vérifiés au runtime (tous verts)

- **P1-1** — masquage réel des variétés perso : variété `Testette mortel` créée → carte « ⭐ perso » rendue dans le guide → masquée → carte disparue, `toutesEspeces()` exclut l'id, toast « Espèce masquée 🙈 » (aucun toast mensonger).
- **P2-2** — tombes : suppression définitive de la variété perso → `Etat.tombes.testette` = `{statut:'mortel', perso:true}` ; `infoEspeceArchive('testette mortel')` → **mortel, archivee:true** (exact) ; `infoEspeceArchive('testette mortell')` → **mortel, archivee:true** (Levenshtein sur les tombes — le filet couvre les frappes même sur espèces effacées).
- **P3-1** — glyphe ☠️ conservé sur fiche perso supprimée : après suppression depuis sa propre fiche, la carte verdict reste `☠️` (rouge `rgb(179,38,30)`). Note : les cartes spec de la fiche deviennent inertes après suppression (les illustrations de l'espèce sont effacées par le flux → `basculerSpec` sort tôt) — fenêtre transitoire jusqu'au « ← Retour », aucun risque de sécurité, la valence ☠️ est préservée dans le DOM.
- **P3-2** — badges des cueillettes via `infoEspeceArchive` : cueillette « Testette mortel » (variété supprimée) → carte rendue « 🍄 Testette mortel **MORTEL ☠️** ».
- **P2-1 (régression c-meteo)** — voir B-3 ci-dessus.

---

## 5. Étapes navigateur réussies (18/18 ✅)

| # | Étape | Résultat observé |
|---|---|---|
| 1 | Chargement + état | SW `cqm-v55` contrôlant après ré-enregistrement propre, cache 136 entrées, titre « 🐴 Cueillette Québec — édition Memphis », globals OK. Vue initiale = `spots` (défaut de l'app, confirmé dans `Etat`). |
| 2 | Filtres (selects) | tous=**21** · mortels=**5** · prudence=**2** · comestibles=**8** · npas=**11** · hiver=**1** (pleurote « Septembre à décembre ») · mortels+printemps=**1** — ancres exactes (hiver re-mesuré avec statut=tous ; un probe préalable enchaînait npas+hiver=0, combinaison légitime). |
| 3 | Verdict dynamique comestible (chanterelle) | 0/5 → att ⚠️ ambre `rgb(217,164,65)` « Rien n'est encore vérifié » + corps « Cochez chaque critère… » · 5/5 → ok ✅ olive `rgb(111,143,62)` visible · retour 0/5 → att ⚠️, corps redevient « Cochez chaque critère… » (B-2 tient : le corps suit le compteur). |
| 4 | Verdict dynamique mortel (gyromitre) | 0/5 → danger-att rouge `rgb(179,38,30)` « ☠️ Rien n'est encore vérifié » · 5/5 → danger « **☠️ 5/5 critères vérifiés** » (texte dynamique) · retour 0/5 → danger-att. Valence jamais verte sur mortel. |
| 5 | Persistance checklist | Après cycle propre : IndexedDB `chanterelle=[F,F,F,F,F]`, compteur 0/5 — **la vérité stockée = la vérité affichée** (probe de persistance direct sur `Stockage.lire('checklist')`). |
| 6 | Synonymes (`infoEspece`) | « fausse morille » → gyromitre **mortel** (synonyme:true) · « amanite phaloide » → phalloïde **mortel** (Levenshtein) · « ange destructeur » → vireuse **mortel** · « pied-de-mouton » → **comestible** · inconnu → null. |
| 7 | Filet tombes P2-2 | Variété perso supprimée → `infoEspeceArchive` exact + flou → **mortel** (archivee:true, perso:true). |
| 8 | Fail-safe IA sans clé | Bandeau « 🔑 Identification par photo : ajoutez votre clé Gemini… » visible ; `identifierParPhoto` → toast ; `analyserPhoto` → « 🔑 Clé Gemini manquante — ajoutez-la dans ⚙️ Paramètres. » + « Vérifiez votre clé et votre connexion. » (jamais silencieux). |
| 9 | Croisement IA × guide (P1-1 24e) | IA simulée « comestible 95 % » sur phalloïde → « 🍄 Amanite phalloïde **MORTEL ☠️** » + alerte rouge + antipoison **1-800-463-5060** — **jamais de badge vert**, bouton « 📖 Voir la fiche du guide » présent. |
| 10 | P2-1 25e espèce masquée | Phalloïde masquée + IA comestible → **toujours MORTEL**, bouton « Voir la fiche » absent (archivee). |
| 11 | Analyse annulable | « 🔍 Analyse en cours… (10-20 s) » + **✋ Annuler** → « ✋ Analyse annulée. » + [🖼️ Choisir une photo, Fermer]. |
| 12 | Import versionné | v4 → « version ANTÉRIEURE (v4) : la checklist terrain (vos vérifications ⚠️/✅) sera perdue » · v6 → « version PLUS RÉCENTE (v6)… import risqué » · v5 → résumé chiffré (« 0 cueillette, 0 spot ») — Annuler partout, **données intactes** (0 écriture). |
| 13 | Import — fichier invalide (bonus) | Fichier malformé → toast « ⚠️ Fichier invalide — import annulé », **aucune écriture, aucune modale** — rejet honnête (comportement découvert en déboguant un probe, vérifié délibérément). |
| 14 | Garde-fou B-3 | Cueillette vierge → fermeture directe · sale → modale · Annuler préserve · Quitter ferme · spot vierge → direct · spot sale → modale. |
| 15 | Lightbox a11y | `role="dialog"` + `aria-modal="true"` + `aria-label="Photo agrandie"` · focus déplacé dans la lightbox à l'ouverture · **Escape retire le nœud du DOM** · **focus restauré** au déclencheur (`.detail-img`). |
| 16 | Console | **0 erreur JS**, **0 ressource ≥ 400** après reloads complets (avant, pendant et après les sondes). |
| 17 | SW après reset | Unregister → reload → install `addAll` 135 fichiers (tous 200 au log serveur) → cache recréé 136 entrées, controller:true. |
| 18 | État final restauré | Stores vides (spots/cueillettes/custom/cachees/supprimees/tombes = 0), checklists chanterelle/gyromitre 0/5, aucune clé IA écrite, aucun code modifié. |

---

## 6. Notes de méthode (sondes et pièges rencontrés)

- Détecteur lancé depuis la racine projet (config `.impeccable/config.json` + DESIGN.md résolus) ; JSON temporaire écrit en local projet puis supprimé.
- **Probe async trop long** : un IIFE de ~13 s (2 cycles de verdict dans un seul `js()`) a dépassé le timeout `Runtime.evaluate` ; l'exécution page-side a **continué en arrière-plan** et interfolié ses écritures checklist avec les probes suivants → compteur transitoire « 3/5 » puis état stocké brouillé. Résolu par reset explicite + cycle propre avec **preuve de persistance IndexedDB** (étapes 3–5). Aucun bug app — mais tout probe async de plus de ~8 s doit être découpé en appels courts (1 toggle par `js()` + sleep), comme documenté dans la skill.
- **Piège payload JSON** : construire un `File` pour l'import avec `new File([<json.dumps>], …)` insère un **objet JS littéral** (→ contenu « [object Object] ») ; l'app a correctement rejeté avec le toast invalide (étape 13, bonus). Rejoué avec payload doublement échappé → alertes versionnées capturées (étape 12).
- **Modale partagée (singleton `resolveConfirm`)** : lire `confirm-titre`/`confirm-message` sans vérifier la classe `visible` renvoie du **texte périmé** (un ancien message de garde-fou a faussé une première lecture d'import). Toujours coupler lecture texte + classe visible.
- **Filtres enchaînés** : mesurer chaque ancre de filtre après avoir remis les autres filtres au défaut (hiver=0 initial = npas+hiver, combinaison légitime).
- Environnement : popup Chrome « Allow remote debugging? » (connu, sans impact) ; toutes les sondes vérifient `location.href` + globals avant de conclure.
- Serveur 8146 arrêté, port vérifié libre (`curl` → 000, `netstat` → aucun LISTEN sur 8110-8159), **aucun http.server orphelin**.

**Synthèse** : 101 findings = 101 faux positifs documentés/advisories connus (zéro dérive vs 27e, seul décalage +5 lignes = code `b87d1dd`) · runtime 18/18 sondes vertes · B-3 corrigé et vérifié · 6/6 fixes `b87d1dd` vérifiés · **0 nouveau défaut** · console 0 erreur, 0 ressource ≥ 400 · SW `cqm-v55` prouvé sur cache frais.
