# ASSESSMENT B — Détecteur impeccable + preuves navigateur (16 août 2026, run 12:33)

Cible : `C:/Users/Jo/projets/cueillette-memphis/index.html` (PWA mono-fichier, édition Memphis).
Méthode : `detect.mjs --json` sur le fichier, triage contre DESIGN.md / PRODUCT.md / `.impeccable/config.json`, puis sondes runtime sur serveur statique local (port 8642, éteint en fin de session). **Code re-scanné après l'édition de 12:01 (cache bump v50→v51, correction du texte de verdict).**

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
| em-dash-overuse | 1 | warning (flag advisory) | quality |

**Totaux : 7 warnings + 94 advisory ; 6 slop + 95 quality.**

### Liste complète (règle | ligne | extrait)

```
side-tab                L  135 | border-right:3px solid var(--noir)
bounce-easing           L  111 | cubic-bezier(.2, 1.6, .4, 1)
bounce-easing           L  241 | cubic-bezier(.2, 1.5, .4, 1)
bounce-easing           L  244 | cubic-bezier(.2, 1.5, .4, 1)
bounce-easing           L  281 | cubic-bezier(.2, 1.3, .4, 1)
broken-image            L 1967 | <img>  (commentaire source uniquement)
em-dash-overuse         L    0 | 8 em-dashes in body text (densité 1,09 / 500 chars)
design-system-color     L 137,189,255,347 | rgba(0,0,0,.1)  (outline photos, 4×)
design-system-color     L 2362 | rgba(20,14,8,.92)  (voile lightbox)
design-system-radius    55 findings (voir triage ci-dessous)
design-system-font-size 34 findings (voir triage ci-dessous)
```

Détail radius (55) : pilules `999px` ×12 (L53,99,145,164,195,257,274,289,300,305,334,357) · coins cassés `4/5/6 px` ×20 (L58,116,122,126,175,185,206,223,239,247,252,267,294,313,342,344,347,1652,1851,2261,2684) · rayons principaux `14/16/20 px` ×16 (L58,116,185,206,223,239,267,347,1851,2261,2363,2406,2416,2439,2448,2684) · micro-valeurs `3/9/10 px` ×7 (L256,259,325,344,1853).
Détail font-size (34) : `11.5px` ×4, `22px` ×2, `32px` ×1, `18px` ×1 (documentés) ; `14px` ×9, `14.5px` ×5, `15px` ×2, `12px` ×4, `17px`, `24px`, `30px`, `36px`, `48px`, `10.5px` (micro-variantes).

---

## 2. Triage / faux positifs (verdicts)

**Faux positifs documentés (le détecteur a techniquement raison, le contexte le disculpe) :**

- **side-tab (L135)** — `border-right:3px solid var(--noir)` : c'est La Règle du Trait Noir (DESIGN.md L147 : « Toute surface colorée porte une bordure noire de 3 px » ; PRODUCT.md Brand Commitments « bordures noires épaisses (3 px) »). Le token de marque EST l'accent. → **faux positif**.
- **bounce-easing ×4** — DESIGN.md L124 : « Élasticité délibérée : cubic-bezier(.2, 1.3-1.6, .4, 1) pour les apparitions » ; L116/L237 : « les rebonds élastiques des feuilles et des confirmations font partie du plaisir, pas un défaut ». → **faux positif** (trait identitaire documenté).
- **broken-image (L1967)** — le seul `<img>` sans src est dans le commentaire `// …(hors-ligne, CORS OK en <img>)`. `grep '<img[^>]*>' | grep -v 'src='` ne retourne que ce commentaire. → **faux positif**.
- **design-system-color ×5** — `rgba(0,0,0,.1)` ×4 : `outline:1px solid` filet fonctionnel autour des vignettes/zone photo/spec-photo/detail-img (pas une couleur de surface). `rgba(20,14,8,.92)` : voile du lightbox zoom. Ombre/filet/voile ≠ couleur de marque. → **faux positif** (à ajouter aux ignoreValues du config si on veut zéro bruit).
- **radius ≈48/55** — pilules 999px (composants documentés), coins cassés 4-6px (signature « coin cassé », DESIGN.md L180 : « coin inférieur droit presque droit (4-6 px) »), rayons principaux 14/16/20px conformes à la prose Shapes « coins arrondis généreux (12-24 px) », 18/5 cartes, 16/5 alertes, 12/4 champs — tous documentés. → **faux positif**.
- **font-size ≈8/34** — 11.5px (libellés nav, DESIGN.md L207), 22px (icônes nav), 32px (icône zone photo, L204), 18px (titre de feuille) : documentés. → **faux positif**.

**Partials (cohérents mais non documentés) :**

- **radius ≈7/55** — `9px 9px 9px 3px` (badge spec-num ×2), `10px` (×2), `3px` (×1) : micro-variantes de petits éléments hors échelle 8/12/18/24 mais fidèles à la signature coin cassé. → **partial**.
- **font-size ≈26/34** — 14/14.5/15/17/12/10.5/24/30/36/48px : hiérarchie cohérente (Fredoka, poids 400-700), tailles d'emoji/titres/meta non répertoriées dans la rampe 21/20/16/13 ; la `.ds-btn` du design.json embarque elle-même 14.5px. → **partial**.
- **em-dash-overuse** — densité mesurée 8 tirets / 3 682 caractères de corps = 1,09 par 500 (seuil 8). Typographie française standard. → **partial**.

**Drift réel : 0.** Aucune couleur hors palette, aucun motif AI résiduel, aucun radius/font aberrant.

---

## 3. Findings console navigateur

- **Erreurs JS : 0** (`window.__errs` vide via injection `Page.addScriptToEvaluateOnNewDocument`, relevé au chargement, après chaque bloc de sondes, et en fin de session).
- **Ressources 4xx : 0** (`performance.getEntriesByType('resource')` filtré ≥400, vide en fin de session).
- SW : reset complet (unregister 1 registration + `caches.delete` de `cqm-v50`) → rechargement → **re-enregistrement vérifié (1 registration, cache `cqm-v51` recréé, controller actif)** : le runtime est testé sur code frais, pas sur cache périmé.

---

## 4. Sondes runtime (verdicts dynamiques, synonymes, analyse IA, import/export)

**Verdicts dynamiques (checklist terrain) — TOUT PASSÉ :**
- Bolet bai (comestible) : 0/5 → `#spec-verdict-att` visible ⚠️ « Rien n'est encore vérifié » (fond ambre `rgb(217,164,65)`), `#spec-verdict-ok` caché ; 5/5 → carte ✅ visible (fond olive `rgb(111,143,62)`) « Tous les critères correspondent », compteur 5/5, 5 cartes `.fait` ; décochage → retour ⚠️ + compteur 0/5.
- **Persistance IndexedDB : 5/5 survit à un reload complet** (compteur, classes, verdicts restaurés après réouverture de la fiche).
- Espèce mortelle (Gyromitre) : à 5/5 la carte visible est la variante danger — fond `rgb(179,38,30)` = `--rouge` calculé, texte « est MORTELLE — ne pas consommer », **aucune carte verte jamais rendue** ; centre antipoison **1-800-463-5060** présent dans la fiche.
- **Correction vérifiée (le défaut mineur du run 11:59 est FIXÉ)** : `basculerSpec` (L1490-1492) met désormais à jour le texte de la carte danger — à 5/5 la carte affiche « ☠️ **5/5 critères vérifiés** », à 0/5 « ☠️ 0/5 critères vérifiés ». Le compteur et le libellé ne se contredisent plus. Note cosmétique résiduelle : le libellé de la carte ⚠️ reste figé au rendu (affiche « Critères manquants » même à 0/5 après décoche) — sémantiquement correct, direction sûre, non un défaut.

**Synonymes — TOUT PASSÉ :**
- `infoEspece('fausse morille')` → `{id:'gyromitre', statut:'mortel', synonyme:true, nomComplet:'Gyromitre (fausse morille)'}`.
- `infoEspece('ange destructeur')` → `{id:'vireuse', statut:'mortel', synonyme:true}`.
- `infoEspece('fausse chanterelle')` → synonyme:false (nom exact d'espèce). Typo `'morile'` → « Morille » (Levenshtein ≤2). Inconnu → `{id:null}`.
- Flux sécurité : « fausse morille » dans une cueillette → `confirmer` capturé : « ⚠️ « fausse morille » correspond à « Gyromitre (fausse morille) » — MORTELLE : ne pas consommer. Enregistrer quand même ? », titre « ☠️ Sécurité » ; Annuler → **0 écriture** (Etat.cueillettes 0 avant ET après). Boîte de suggestions : exactement « Gyromitre (fausse morille) ».

**Analyse IA (photo) — TOUT PASSÉ (stub `identifierPhotoIA` à payload programmable, aucune clé Gemini consommée) :**
- `analyserPhoto(dataUrl)` transmet bien la photo (`data:image/png;base64,…`) ET le `AbortSignal` au stub (4/4 captures, `hasSignal:true`).
- États vérifiés : chargement 🔍 « Analyse en cours… (10-20 s) » + bouton ✋ Annuler + image affichée + feuille ouverte (observé sur stub à résolution différée ET sur stub jamais résolu) ; succès (Bolet bai 92 %) → badge Comestible, Confiance 92 %, description, confusions, boutons « 📖 Voir la fiche du guide » / « ➕ Ajouter comme variété » / Fermer ; confiance 45 % → 😕 + alerte rouge « En cas de doute, on ne mange pas… » + 📷 Réessayer / Fermer ; `espece:'inconnu'` → 😕 + Fermer seul ; annulation → « ✋ Analyse annulée. » + 🖼️ Choisir une photo / Fermer. Fonctions d'origine restaurées après chaque bloc.

**Import/export JSON — TOUT PASSÉ :**
- v5 valide (1 spot, 1 cueillette) → modale résumé « Le fichier contient 1 cueillette, 1 spot » (comptes exacts) ; Annuler → **0 écriture** (spots/cueillettes 0/0 avant ET après).
- v6 → « version PLUS RÉCENTE (v6)… import risqué » ; v4 → « version ANTÉRIEURE (v4) : la checklist terrain (vos vérifications ⚠️/✅) sera perdue ».
- JSON invalide → toast « ⚠️ Fichier invalide — import annulé », **0 écriture**, aucun confirmer supplémentaire.
- Export → toast « Export téléchargé 📤 ». (L'alerte « Jamais exporté » était déjà masquée — `cqm_exporte` posé par une session antérieure ; le toast prouve l'exécution du handler.)

---

## 5. Étapes navigateur réussies / échouées

| Étape | Résultat |
|---|---|
| Serveur statique local (8642) + chargement | ✅ 200, titre « 🐴 Cueillette Québec — édition Memphis » |
| Reset SW + caches → re-registration | ✅ 1 SW, cache cqm-v51 recréé, controller actif |
| Capture erreurs console (injection new-document) | ✅ 0 erreur en début, milieu et fin ; 0 404 |
| Verdicts dynamiques (comestible + mortel + persistance) | ✅ (correction du texte ☠️ vérifiée, voir §4) |
| Synonymes + garde sécurité cueillette | ✅ |
| Analyse IA (4 branches + en-vol + annulation + args) | ✅ |
| Import (v5/v6/v4/invalide) + export | ✅ |
| Arrêt serveur + port vérifié libre | ✅ (curl 000, aucun listener sur 8642) |
| Échecs | Aucun côté application |

**Limitations d'automatisation (pas des défauts de l'app) :** la résolution immédiate des stubs IA rendait l'état « Analyse en cours… » inobservable sur les branches résolues — contourné par un stub à résolution différée (2 s) et un stub jamais résolu ; l'alerte d'export « jamais exporté » était déjà consommée par une session antérieure (localStorage persistant du daemon), donc non re-démontrée ce run.

---

## 6. Synthèse

- **Détecteur : 101 findings, 0 drift réel.** ~63 faux positifs documentés (signature Memphis : bordures 3px, coins cassés 4-6px/12-24px, pilules 999px, rebonds élastiques, filets/voiles photos), ~38 partials cohérents (micro-tailles de police et micro-rayons non répertoriés, em-dash typographique). Suggestion : ajouter `rgba(0,0,0,.1)` et `rgba(20,14,8,.92)` aux ignoreValues pour un scan 100 % silencieux.
- **Runtime : 0 erreur JS, 0 ressource 404, toutes les sondes dynamiques passent** (verdicts ✅/⚠️/☠️ + persistance IndexedDB, synonymes + garde mortel avec 0 écriture, pipeline IA complet sans clé consommée, import/export avec gardes de version et 0 écriture sur annulation).
- **1 défaut mineur du run précédent CORRIGÉ et vérifié** : le texte de la carte ☠️ suit désormais le compteur (plus de « 0/5 » figé à 5/5). Seule rémanence cosmétique : le libellé de la carte ⚠️ est figé au rendu — direction sûre, sans risque.
