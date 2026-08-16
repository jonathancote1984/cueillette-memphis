# ASSESSMENT B — Détecteur impeccable + preuves navigateur (16 août 2026)

Cible : `C:/Users/Jo/projets/cueillette-memphis/index.html` (PWA mono-fichier, édition Memphis).
Méthode : `detect.mjs --json` sur le fichier, triage contre DESIGN.md / PRODUCT.md / `.impeccable/config.json`, puis sondes runtime sur serveur statique local (port 8642, éteint en fin de session).

---

## 1. Findings CLI (detect.mjs)

**Résultat : EXIT=2 (findings présents — pas une erreur, stderr vide). 101 findings.**

| Règle | Count | Sévérité | Catégorie |
|---|---|---|---|
| design-system-radius | 55 | advisory | quality |
| design-system-font-size | 34 | advisory | quality |
| design-system-color | 5 | advisory | quality |
| bounce-easing | 4 | warning | slop |
| side-tab | 1 | warning | slop |
| broken-image | 1 | warning | slop |
| em-dash-overuse | 1 | advisory | quality |

**Totaux : 7 warnings + 94 advisory ; 6 slop + 95 quality.**

### Liste complète (règle | ligne | extrait)

```
side-tab                L 135 | border-right:3px solid var(--noir)
bounce-easing           L 111 | cubic-bezier(.2, 1.6, .4, 1)
bounce-easing           L 241 | cubic-bezier(.2, 1.5, .4, 1)
bounce-easing           L 244 | cubic-bezier(.2, 1.5, .4, 1)
bounce-easing           L 281 | cubic-bezier(.2, 1.3, .4, 1)
broken-image            L1959 | <img>  (commentaire source uniquement)
em-dash-overuse         L   0 | 8 em-dashes in body text
design-system-color     L 137,189,255,347 | rgba(0,0,0,.1)  (outline photos)
design-system-color     L2354 | rgba(20,14,8,.92)  (voile lightbox)
design-system-radius    55 findings (voir triage ci-dessous)
design-system-font-size 34 findings (voir triage ci-dessous)
```

Détail radius (55) : pilules `999px` ×12 (L53,99,145,164,195,257,274,289,300,305,334,357) · coins cassés `4/5/6 px` ×18 (L58,116,122,126,175,185,206,223,239,247,252,267,294,313,347,1843,2253,2672) · rayons principaux `14/16/20 px` ×16 (L58,116,185,206,223,239,267,347,1843,2253,2355,2398,2408,2431,2440,2672) · micro-valeurs `3/6/9/10 px` + `5 px` seul ×10 (L256,259,325,342,344,1644,1645,1845,256,259).
Détail font-size (34) : `11.5px` ×4, `22px` ×2, `32px` ×1, `18px` ×1 (documentés) ; `14px` ×9, `14.5px` ×4, `15px` ×2, `12px` ×4, `17px`, `24px`, `30px`, `36px`, `48px`, `10.5px` (micro-variantes).

---

## 2. Triage / faux positifs (verdicts)

**Faux positifs documentés (le détecteur a techniquement raison, le contexte le disculpe) :**

- **side-tab (L135)** — `border-right:3px solid var(--noir)` : c'est La Règle du Trait Noir (DESIGN.md Key Characteristics : « Bordures noires 3 px partout » ; PRODUCT.md Brand Commitments « bordures noires épaisses (3 px) »). Le token de marque EST l'accent. → **faux positif**.
- **bounce-easing ×4** — DESIGN.md L124 : « Élasticité délibérée : cubic-bezier(.2, 1.3-1.6, .4, 1) pour les apparitions » ; Elevation : « les rebonds élastiques des feuilles et des confirmations font partie du plaisir, pas un défaut ». → **faux positif** (trait identitaire documenté).
- **broken-image (L1959)** — le seul `<img>` sans src est dans le commentaire `// CORS OK en <img>`. `grep '<img[^>]*>' | grep -v 'src='` ne retourne que ce commentaire. → **faux positif**.
- **design-system-color ×5** — `rgba(0,0,0,.1)` ×4 : `outline:1px solid` filet fonctionnel autour des vignettes/zone photo/spec-photo/detail-img (pas une couleur de surface). `rgba(20,14,8,.92)` : voile du lightbox zoom. Ombre/filet/voile ≠ couleur de marque. → **faux positif** (à ajouter aux ignoreValues du config si on veut zéro bruit).
- **radius ≈45/55** — pilules 999px (composants documentés), coins cassés 4-6px (signature « coin cassé », DESIGN.md Shapes : « coin inférieur droit presque droit (4-6 px) »), rayons principaux 14/16/20px conformes à la prose Shapes « coins arrondis généreux (12-24 px) », 18/5 cartes, 16/5 alertes, 12/4 champs — tous documentés. → **faux positif**.
- **font-size ≈8/34** — 11.5px (libellés nav, DESIGN.md L207), 22px (icônes nav), 32px (icône zone photo), 18px (titre de feuille) : documentés. → **faux positif**.

**Partials (cohérents mais non documentés) :**

- **radius ≈10/55** — `9px 9px 9px 3px` (badge spec-num ×2), `10px` (×2), `6px` (×2), `5px` seul (L342), `3px` coin d'un 8px (L344) : micro-variantes de petits éléments (badges, barre d'étapes) hors échelle 8/12/18/24 mais fidèles à la signature coin cassé. → **partial**.
- **font-size ≈26/34** — 14/14.5/15/17/12/10.5/24/30/36/48px : hiérarchie cohérente (Fredoka, poids 400-700), tailles d'emoji/titres/meta non répertoriées dans la rampe 21/20/18/16/13/12.5. → **partial**.
- **em-dash-overuse** — densité mesurée 8 tirets / 3 062 caractères de corps = 1,31 par 500 (seuil 8). Typographie française standard, advisory. → **partial**.

**Drift réel : 0.** Aucune couleur hors palette, aucun motif AI résiduel, aucun radius/font aberrant.

---

## 3. Findings console navigateur

- **Erreurs JS : 0** (`window.__errs` vide via injection `Page.addScriptToEvaluateOnNewDocument`, relevé en début ET fin de session).
- **Ressources 4xx : 0** (`performance.getEntriesByType('resource')` filtré ≥400, vide). Toutes les photos/JSON servis 200 (log serveur).
- SW : 1 registration, cache `cqm-v50` ; reset complet (unregister + caches.delete) → re-enregistrement et re-création du cache vérifiés (runtime testé sur code frais).

---

## 4. Sondes runtime (verdicts dynamiques, synonymes, analyse IA, import/export)

**Verdicts dynamiques (checklist terrain) — TOUT PASSÉ :**
- 0/5 → carte `#spec-verdict-att` visible ⚠️ « Rien n'est encore vérifié » ; 5/5 → `#spec-verdict-ok` ✅ « Tous les critères correspondent — Bolet bai confirmé — récolte possible » (fond olive) ; décochage → retour ⚠️, compteur 0/5.
- Persistance IndexedDB : 5/5 survit à un reload complet (compteur, classes, verdicts restaurés).
- Espèce mortelle (Amanite phalloïde) : à 5/5 la carte visible est la variante danger — fond `rgb(179,38,30)` = `--rouge #B3261E` calculé, texte « est MORTELLE — ne pas consommer », jamais de ✅ vert ; alerte MORTEL avec centre antipoison **1-800-463-5060** présent.
- **Défaut mineur réel (drift cosmétique) :** `basculerSpec` ne met à jour que les classes + compteur, jamais le texte des cartes de verdict. À 1/5 la carte ⚠️ affiche encore « Rien n'est encore vérifié » ; à 5/5 sur espèce mortelle la carte ☠️ affiche « ☠️ 0/5 critères vérifiés » alors que le compteur indique 5/5. Direction toujours prudente (jamais dangereux), mais contradictoire à l'écran.

**Synonymes — TOUT PASSÉ :**
- `infoEspece('fausse morille')` → synonyme:true, mortel, « Gyromitre (fausse morille) ».
- `infoEspece('ange destructeur')` → synonyme:true, mortel, « Amanite vireuse (ange destructeur) ».
- `infoEspece('fausse chanterelle')` → synonyme:false (nom exact d'espèce). Typo `'morile'` → « Morille » (Levenshtein ≤2).
- Flux sécurité : saisir « fausse morille » dans une cueillette → modale « ☠️ Sécurité — correspond à Gyromitre (fausse morille) — MORTELLE : ne pas consommer. Enregistrer quand même ? » ; Annuler → modale fermée, **0 écriture** (Etat.cueillettes inchangé).

**Analyse IA (photo) — TOUT PASSÉ (stub `identifierPhotoIA`, aucune clé Gemini consommée) :**
- `analyserPhoto(dataUrl)` transmet bien la photo (data:image/png;base64,…) ET le `AbortSignal` au stub (capture vérifiée).
- États vérifiés : chargement 🔍 « Analyse en cours… (10-20 s) » + bouton ✋ Annuler ; succès (Bolet bai 92 %) avec badge, confiance, description, confusions, boutons « Voir la fiche du guide » / « Ajouter comme variété » / Fermer ; confiance 45 % → 😕 + alerte rouge « En cas de doute, on ne mange pas… » + 📷 Réessayer ; `espece:'inconnu'` → 😕 + Fermer ; annulation → « ✋ Analyse annulée. » + 🖼️ Choisir une photo. Fonction d'origine restaurée ensuite.

**Import/export JSON — TOUT PASSÉ :**
- v5 valide (1 spot, 1 cueillette) → modale résumé « Le fichier contient 1 cueillette, 1 spot » (comptes exacts) ; Annuler → **0 écriture**.
- v6 → garde « version PLUS RÉCENTE (v6)… import risqué » ; v4 → garde « version ANTÉRIEURE (v4) : la checklist terrain sera perdue ».
- JSON invalide → toast « ⚠️ Fichier invalide — import annulé » (auto-dismiss ~2,6 s), **0 écriture**.
- Export → toast « Export téléchargé 📤 » + alerte export rendue dans Stats.

---

## 5. Étapes navigateur réussies / échouées

| Étape | Résultat |
|---|---|
| Serveur statique local (8642) + chargement | ✅ 200, titre correct |
| Reset SW + caches → re-registration | ✅ 1 SW, cache cqm-v50 recréé |
| Capture erreurs console (injection new-document) | ✅ 0 erreur, 0 404 |
| Verdicts dynamiques (complet + mortel + persistance) | ✅ (1 défaut mineur noté §4) |
| Synonymes + garde sécurité cueillette | ✅ |
| Analyse IA (4 branches + annulation) | ✅ |
| Import (v5/v6/v4/invalide) + export | ✅ |
| Arrêt serveur + port vérifié libre | ✅ (curl 000) |
| Échecs | Aucun côté application |

**Limitations d'automatisation (pas des défauts de l'app) :** les évaluations `js()` > ~3 s dépassent le budget IPC du harnais (TimeoutError) — la boucle de toggles a été découpée en petites étapes ; après un timeout la boucle page-side continue de tourner (état intermédiaire observé puis réinitialisé proprement via écriture directe du store). Une sonde stub « faible/annulation » a dû être relancée après correction du stub (bug de sonde, pas de l'app).

---

## 6. Synthèse

- **Détecteur : 101 findings, 0 drift réel.** ~63 faux positifs documentés (signature Memphis : bordures 3px, coins cassés 4-6px/12-24px, pilules 999px, rebonds élastiques, filets/voiles photos), ~38 partials cohérents (micro-tailles de police et micro-rayons non répertoriés), 1 advisory (em-dash). Suggestion : ajouter `rgba(0,0,0,.1)` et `rgba(20,14,8,.92)` aux ignoreValues pour un scan 100 % silencieux.
- **Runtime : 0 erreur JS, 0 ressource 404, toutes les sondes dynamiques passent** (verdicts ✅/⚠️/☠️ + persistance, synonymes + garde mortel, pipeline IA complet, import/export avec gardes de version).
- **1 défaut mineur réel** : texte des cartes de verdict figé au rendu (`basculerSpec` met à jour classes + compteur, pas le libellé — « 0/5 » affiché à 5/5 sur carte ☠️). Cosmétique, direction sûre.
