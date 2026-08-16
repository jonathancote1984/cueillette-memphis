# Assessment A — Critique design (22e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2724 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v49) · **Base :** `img/mycoquebec.json` (3938 entrées, 3396 avec `nomFr`, 0 doublon de latin)
**Méthode :** lecture statique seule (Assessment A, aucun navigateur, aucun détecteur). Vérification des 8 findings de la passe 21E (P2-1, P3-2 à P3-8) et des claims du commit `bf134a6` dans le code ET sur les données : base JSON interrogée en Python par identité (latin), comparateur de suggestions (l.1612-1638) répliqué avec la normalisation de requête réelle (`normNom` appliqué AVANT le filtre, l.1615), 21 noms exacts de fiches + variantes espacées/trait d'union, existence des fichiers sur disque + liste `FICHIERS` du SW, contrastes WCAG exacts, grep batterie Python (io.open) sur le fichier entier.
**Note globale :** les 8 findings de 21E sont **corrigés en code** — 7 entièrement, 1 partiellement (P3-2 : tabpanel/aria-labelledby présents, navigation fléchée absente). La normalisation `normNom` tient ses promesses vérifiées par réplication : « pied de mouton » **et** « pied-de-mouton » servent `Hydnum umbilicatum` en position 1 (vignette locale), 21/21 noms de fiches → bon taxon en position 1. Les 21 espèces du guide restent 21/21 en `guide:true` exact (0 faux positif/négatif), `nomFr` = nom de fiche, img locale sur disque et dans le SW. Score **39,5/40 — plateau honnête** : les pénalités 21E sont levées sur preuve, la seule restante (H8, densité de l'étape 1) n'a pas bougé (5 champs, la barre ≤4 reste dépassée), et le nouveau passif est du niveau P3.

---

## 1. Verdict de spécificité design : 9/10 (inchangé)

La grammaire Memphis tient sur les nouveaux éléments : 0 couleur hors palette (les 5 couleurs d'onglets actifs, le dégradé header, les fonds d'alertes et la barre vide sont tous documentés dans le frontmatter DESIGN.md), 0 box-shadow flouté (grep 4 longueurs : 0), 0 uppercase, 0 boîte système (`window.confirm` n'apparaît que dans un commentaire). L'encart d'aide (`.encart-aide`, l.221-227) remplace l'alerte-orange pour l'onboarding : rayures ambre 45° sur blanc, sans le losange « Prudence » — la correction P3-4 21E est aussi un gain de grammaire (le signal orange redevient réservé au danger de consommation).

**Axes :** conceptuel ~90 % (carnet de chasse, vocabulaire mycologique québécois, antipoison, étapes « Identité » / « Détails & photo ») · visuel ~90 % (une capture sans texte révèle Memphis-automne-champignon). Verdict : spécifique sur les deux axes.

## 2. Évaluation holistique

- **Hiérarchie visuelle** — tenue. Barre d'étapes en fil d'Ariane 2 niveaux ; h2 en pastille inclinée ; fiche détail : `<h2>` pour le nom d'espèce (l.1453), sections en h3 — hiérarchie sémantique correcte sur l'écran le plus dense.
- **Architecture de l'information** — le découpage en 2 étapes est sain, et le bouton Enregistrer vit sur l'étape 2 uniquement : tout enregistrement impose de traverser l'étape 2 — le garde-fou structurel contre le « contenu IA jamais relu » est en place, indépendamment des toasts.
- **Adéquation émotionnelle** — la vallée 21E (IA remplit l'étape 2 invisible) est refermée : bascule automatique après `e-generer` (l.1885) + toast « vérifiez les détails ci-dessous » ; chemin idphoto : toast guidé « vérifiez l'identité, puis Suivant » (l.2477) + porte structurelle (Enregistrer n'existe que sur l'étape 2). Nouvelle petite vallée : les miniatures de suggestions non-guide cassent hors-ligne (voir P3-1).
- **Découvrabilité** — rien au hover ; la barre d'étapes annonce l'étendue du formulaire ; l'encart d'aide IA est visible dès l'étape 1.
- **Composition** — colonne 640 px, feuille 84 vh conservées. Nouveau point faible : les suggestions `e-nom-suggestions` vivent dans la demi-colonne du `grille2` (l.631-638) — à 360 px de large, chaque cellule fait ~150 px pour des puces avec vignette 26 px + nom long (P3-2).
- **Typographie** — Fredoka 400-700 (le lien charge exactement ces 4 graisses ; grep 900/300 : 0) ; `.etape` 13 px/700, numéros 11,5 px. Aucune graisse synthétisée.
- **Couleur** — 0 dérive. Contrastes exacts vérifiés : onglet Identifier actif `#B3540B` sur blanc = **4,66:1** (AA à 11,5 px, le plus faible des 5) ; toxique blanc sur `#B45309` = **5,02:1** ; comestible noir sur `#6F8F3E` = **4,61:1** (AA juste) ; MORTEL blanc sur rouge = **6,54:1** ; header (extrémité gauche du dégradé) = **4,79:1** ; sous-titre 12,5 px OK. Textes à opacité .85 (latin, meta, spec-desc, note) = **4,91:1** composé — AA à 12-13 px. La Règle du Rouge Mortel tient : les numéros rouges des pilules actives sont une pastille de numéro, pas un signal de danger.
- **Accessibilité** — aria-labels, focus-trap modales, Escape hiérarchisé (modale avant feuille, l.1088-1113), `prefers-reduced-motion` (l.361-363). Tablist : `role="tablist"/tab/tabpanel"` + `aria-labelledby` + `aria-selected` synchronisé (l.623-629, 660, 1717-1731) — mais pas de navigation fléchée ni de tabindex roving (P3-2 21E : partiel). Focus au premier champ à chaque bascule (l.1729-1730) — sauf à l'OUVERTURE (P3-5 : `etapeEspece(1)` appelé avant `ouvrirFeuille`, la feuille en `visibility:hidden` rend le `focus()` inopérant).
- **États** — bouton ✨ désactivé pendant l'appel (l.1872-1890), `illu-toutes` désactivé + restauré sur tous les chemins (l.2309-2334), validation nom avant étape 2, états vides partout. Échec IA → `messageErreurIA` par cause. Grep `aria-invalid` : 0 — la validation reste toast-only (résidu).
- **Copy** — toasts à valence alignée sur leur branche (vérifié branche par branche : « Analyse terminée ✨ » ne part que sur résultat réussi l.2455 ; l'inconnu reste neutre « — à vérifier » l.2399). Incohérence mineure : l'autocomplétion Myco reste muette à 0 résultat alors que celle des cueillettes affiche « Aucune correspondance — vous pouvez saisir un nom libre » (l.1529) — P3-4.
- **Cas limites** — dates locales (`aujourdhui()`), `toISOString` uniquement pour la métadonnée technique d'export (usage correct), import versionné (l.2562-2568), orphelins `caches` nettoyés (l.2687-2691), checklist réindexée au retrait d'item (l.2289-2306).

## 3. Évaluation de charge cognitive : 1 échec / 8 (inchangé)

1. Focus unique ✅ · 2. Chunking ≤ 4 ✅ · 3. Regroupement visuel ✅ · 4. Hiérarchie ✅ · 5. Une chose à la fois ✅ · 6. Choix minimaux ≤ 4 ❌ — **étape 1 = 5 champs** (nom, latin, comestibilité, saison, prudence) + 2 boutons + 1 encart ; étape 2 = 4 champs + zone photo + 8 boutons. `bf134a6` n'a pas touché au nombre de champs : le point reste en échec, exactement comme jugé en 21E. · 7. Mémoire de travail ✅ · 8. Divulgation progressive ✅.

**1 échec franc sur 8.** Le claim du commit `326f57c` (« lève l'échec ≤ 4 ») était déjà jugé partiel en 21E ; il le reste.

## 4. Voyage émotionnel

Ouverture chaleureuse (dégradé, formes flottantes, zigzag) → guide → fiche hybride inchangés. **Le creux 21E est refermé au pire moment du parcours :** le doute sur « fausse morille » ou « ange destructeur » tape le nom que la fiche enseigne et reçoit la bonne espèce en position 1 avec vignette locale — et désormais aussi en saisie « clavier mobile » (espaces/traits d'union équivalents, réplication : 0/21 échec + variantes OK). **Le pic de création de variété** (recette en 2 temps) est renforcé : après génération IA, l'utilisateur est transporté sur les détails qu'on lui demande de vérifier — le toast ne promet plus l'invisible. **Nouvelle vallée, plus petite :** en forêt, hors-ligne, les suggestions Myco affichent des miniatures cassées pour la plupart des requêtes non-guide (« lactaire », « russule », « cortinaire » : 6/6 distantes ; « bolet » : 3/6) — l'aide visuelle de la recherche est à moitié aveugle hors-ligne (P3-1). Fin de journée : rappel d'export (alerte-orange « Jamais exporté ») — pic de réassurance honnête, pas de faux pic.

## 5. Scores heuristiques Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 4 | Bascule auto vers l'étape 2 après IA (l.1885), toasts guidés, boutons désactivés pendant les appels, focus au premier champ |
| 2 | Correspondance monde réel | 4 | Réplication : 21/21 noms de fiches + variantes espacées/trait d'union → bon taxon du guide en position 1, vignette locale — 0/27 échec |
| 3 | Contrôle et liberté | 4 | Retour entre étapes, garde-fou couvrant voile/poignée/Escape (l.1042-1049, 1096-1101), annulable partout |
| 4 | Cohérence et standards | 4 | Grammaire tenue sur l'encart-aide et les pilules ; seule fausse note : état vide incohérent entre les 2 autocomplétions (P3-4, sans dock) |
| 5 | Prévention des erreurs | 4 | Validation nom avant étape 2, double confirmation de destruction, statut hors vocabulaire → inconnu (fail-safe, l.2411-2412), confirmation « synonyme dangereux » à l'enregistrement (l.1576-1578) |
| 6 | Reconnaissance vs mémorisation | 4 | Les noms que la fiche enseigne sont requêtables dans toutes leurs formes de saisie ; « amanite vireuse » → virosa (l'égalité exacte d'amerivirosa, non-guide, ne bat plus l'espèce MORTELLE) |
| 7 | Flexibilité / efficacité | 4 | ✨ Détails IA (remplit les 2 étapes), retry + repli modèle, ordre des images persistant, FAB contextuel |
| 8 | Esthétique minimaliste | 3,5 | Le split a réduit la densité (8→5 visibles) mais l'étape 1 dépasse toujours la barre ≤4 et l'étape 2 garde ~13 éléments d'attention |
| 9 | Aide à la récupération d'erreurs | 4 | messageErreurIA par cause, parserJSONIA tolérant, séries interrompues avec état restauré, import versionné avec confirmations |
| 10 | Aide et documentation | 4 | Encart d'onboarding (l.630), carte « Comment identifier », crédits Commons, DESIGN.md documente désormais le composant étapes |

**Total : 39,5/40 — plateau honnête, égal au record 21E.** Les deux pénalités 21E (H6, H8) : la première était déjà levée et le reste (vérifié par réplication), la seconde n'a pas bougé. Le passif nouveau est P3 et ne justifie aucun dock. Profil : sécurité, état du système et prévention excellents ; le seul frottement structurel restant est la densité du formulaire variété.

## 6. Forces spécifiques

1. **La correction P3-5 21E est tenue par réplication sur les deux formes de saisie.** `normNom` (l.976) réduit espaces/traits d'union/points au même séparateur, appliqué à la requête ET aux données. Résultats vérifiés : « pied de mouton » → `Hydnum umbilicatum` pos 1, « pied-de-mouton » → idem, « tue mouches » / « tue-mouches » → `Amanita muscaria` pos 1, et les 21 noms exacts de fiches → bon taxon pos 1 (0/21 échec). La chaîne « ce qu'on apprend → ce qu'on peut taper au clavier mobile » est cohérente, vérifiée au niveau du comparateur réel (score exact/préfixe/guide, tie-break guide puis longueur).
2. **Le P2-1 21E est corrigé sur les DEUX chemins, avec un garde-fou structurel.** `e-generer` bascule à l'étape 2 (l.1885) et le toast désigne les détails visibles ; `preparerVarieteDepuisResultat` guide vers l'étape 2 (l.2477) — et surtout, le bouton Enregistrer n'existe QUE sur l'étape 2 (l.692), donc aucun enregistrement ne peut contourner la relecture. La correction ne repose pas sur la bonne volonté de l'utilisateur.
3. **La discipline des données tient toujours, par identité.** 21/21 entrées `guide:true` = exactement les 21 latins du guide (0 faux positif/négatif), 21/21 `nomFr` = nom de fiche, 21/21 img locales présentes sur disque ET dans `FICHIERS` du SW (cqm-v49). Le vocabulaire de sécurité (alertes MORTEL/toxique + antipoison, verdicts conditionnés au statut) reste cohérent de la fiche à l'identification photo jusqu'à l'enregistrement de cueillette (badge synonyme + confirmation).

## 7. Problèmes prioritaires

**P3-1 (NOUVEAU) — les miniatures de suggestions non-guide pointent vers mycoquebec.org : cassées hors-ligne.** `remplirSuggestionsMyco` rend `x.img` directement (l.1643) ; seules les 21 espèces du guide ont des vignettes locales. Mesuré sur des requêtes courantes : « lactaire » 6/6 distantes, « russule » 6/6, « cortinaire » 6/6, « chanterelle » 4/6, « bolet » 3/6, « lepiote » 4/6. Hors-ligne — le mode d'emploi promis du produit — la liste de suggestions affiche des images cassées pour la majorité des requêtes. Pas d'impact sécurité (les espèces du guide sont locales et gagnent le tri), mais dégradation visible d'un flux central. *Fix :* `onerror` sur l'`<img>` de suggestion (remplacer par une vignette neutre à rayures ou masquer), ou ne rendre l'image que si elle commence par `img/`.*

**P3-2 (NOUVEAU) — les suggestions vivent dans la demi-colonne du `grille2`.** l.631-638 : le `<label>` « Nom français » (avec `#e-nom-suggestions`) partage la grille 2 colonnes avec « Nom latin ». Sur un écran de 360 px, la cellule fait ~150 px pour des puces contenant une vignette 26 px + des noms comme « Amanite vireuse américaine » — débordement ou retour à la ligne illisible. *Fix :* déplacer `#e-nom-suggestions` hors du `grille2`, pleine largeur sous les deux champs.*

**P3-3 (NOUVEAU, DOC) — PRODUCT.md est déjà périmé d'un cran dans le commit même qui le corrigeait.** l.38 dit « (actuellement v48) » alors que le SW du même commit `bf134a6` est à cqm-v49. Le P3-6 21E proposait deux remèdes ; celui choisi (« mettre à jour à chaque bump ») a raté son premier rendez-vous. *Fix :* retirer « actuellement vN » du texte (il sera toujours faux), ou écrire v49.*

**P3-4 (NOUVEAU) — état vide incohérent entre les deux autocomplétions.** Cueillettes : « Aucune correspondance — vous pouvez saisir un nom libre » (l.1529). Myco : `zone.innerHTML = ''` silencieux (l.1640-1646) — l'utilisateur qui tape un nom absent de la base ne reçoit rien. *Fix :* même message dans `remplirSuggestionsMyco`.*

**P3-5 (NOUVEAU) — le focus ne tombe pas dans la feuille à l'ouverture.** `ouvrirSheetEspece`/`editerEspece` appellent `etapeEspece(1)` avant `ouvrirFeuille` (l.1741, 1756) : la feuille est encore en `visibility:hidden`, le `premier.focus()` (l.1729-1730) est un no-op. Le focus reste sur le FAB. La correction P3-3 21E (focus aux bascules) est intacte ; c'est le geste d'ouverture qui est orphelin. *Fix :* appeler `etapeEspece(1)` après `ouvrirFeuille`, ou focus dans un `requestAnimationFrame`.*

**P3-6 (RÉSIDU, re-vérifié) — barres de stats sans sémantique ARIA et avec minimum visuel.** 0 `role="progressbar"` dans le fichier (grep confirmé) ; `Math.max(4, …)` (l.2494) et `Math.max(6, …)` (l.2525) donnent aux valeurs minuscules une hauteur minimale trompeuse. *Fix :* `role="progressbar"` + `aria-valuenow/aria-valuemax` + afficher la valeur numérique sur/à côté de la barre ; hauteur réelle proportionnelle (pas de plancher déguisé).*

**P3-7 (NOUVEAU, EFFICACITÉ) — `illustrerSpec` rappelle l'IA à l'identique après un échec.** Le repli l.1982-1984 rejoue `genererImageIA` avec les mêmes arguments alors que la boucle l.1974-1980 vient d'essayer cette source (si `ia` est dans l'ordre). En cas d'échec IA, l'appel payant est doublé immédiatement, sans délai ni changement de paramètres. Le conditionnement sur l'ordre est correct (échec honnête si `ia` absent) ; la redondance ne l'est pas. *Fix :* retirer le repli et laisser l'erreur de la boucle remonter, ou garder le repli mais uniquement pour les sources hors-ligne (myco/wikimedia) qui échouent par réseau.*

## 8. Red flags par persona

- **Jonathan en forêt, une main, sans réseau** : le pire moment 21E est refermé — taper « fausse morille », « ange destructeur », « pied de mouton » (espacé ou non) sert la bonne espèce du guide en position 1, vignette locale, hors-ligne. Restant : les suggestions de genres non-guide (lactaires, russules — précisément ce qu'on croise en forêt) affichent des miniatures cassées hors-ligne (P3-1) ; l'étape 2 dense (13 éléments) à la fin d'une journée. Pire moment : en forêt, chercher un lactaire hors-ligne et voir 6 vignettes cassées avant de lire les noms.
- **Proche débutant (via export/import)** : la chaîne nom → taxon → fiche est cohérente 21/21 dans toutes les formes de saisie ; l'encart d'aide (désormais neutre, sans le losange de prudence) guide la génération IA ; un enregistrement passe obligatoirement par l'étape 2 (le contenu IA ne peut plus être validé sans relecture).
- **Utilisateur pressé / au clavier** : le tablist ARIA est fonctionnel (les deux onglets restent Tab-focusables, `aria-selected` synchronisé, focus au premier champ aux bascules) mais n'implémente pas le patron complet (pas de flèches ←/→, pas de `aria-controls`) ; à l'ouverture de la feuille, le focus reste sur le FAB (P3-5). Les suggestions Myco restent sans navigation ↑/↓ (résidu 16E).

## 9. Observations mineures

**Nouveaux :**
- `p-cle` (l.460) : champ password sans `<label>` associé (le h3 de carte n'est pas un label) — petit passif 3.3.2.
- `rendreBandeauCle` insère un `<button>` dans un `<p class="note">` (l.2376-2379) — HTML invalide mais rendu conforme ; à sortir du paragraphe.
- Le claim « tabpanel ARIA complet » (`bf134a6`) est partiel : tabpanel + `aria-labelledby` + `aria-selected` oui ; `aria-controls`, tabindex roving et flèches ←/→ non (voir section 2 Accessibilité).
- `connue` (l.2418) compare les noms sans `normNom` : une réponse IA sans accent (« Amanite phalloide ») ne trouve pas la fiche ; le filet de sécurité (prudence IA) reste actif, mais le bouton « Voir la fiche du guide » manque alors qu'il serait utile.

**Résidus inchangés depuis les passes précédentes (non re-scorés, listés pour mémoire, tous re-confirmés présents en 22E) :** navigation clavier des suggestions Myco (16E) · `choisirNomMyco` ne remplit le latin que si vide (15E) · échec silencieux de `chargerBaseMyco` (15E) · champ recherche du guide sans label visible (16E) · focus perdu sur les selects de filtre (16E) · `COULEURS_MOIS` cycle de 6 répété 2×/an (16E) · lightbox sans focus-trap (16E) · `alt="photo"` générique (16E) · « Dernière sortie » 24 px en carte 2 colonnes (13E) · `ouvrirMyco` sans message hors-ligne (16E) · `.mois-col .lab` 10,5 px (16E) · toast par item absent pour la source IA dans `illu-toutes` (18E) · cache SW non borné pour les GET réussis (20E) · `aria-invalid` : 0 partout, validation toast-only (nouveau au catalogue).

## 10. Questions provocatrices

1. Les miniatures de suggestions non-guide pointent vers mycoquebec.org et cassent hors-ligne : l'app assume-t-elle que hors-ligne on ne cherche que les 21 espèces du guide, ou la recherche de genres (lactaires, russules) est-elle un flux de première classe qui mérite des vignettes locales ou aucune vignette ?
2. PRODUCT.md dit « actuellement v48 » alors que le SW du même commit est v49 : une version en prose dans la doc est-elle tenable, ou faut-il la supprimer — et si le bump est la règle, qui la vérifie ?
3. L'étape 1 garde 5 champs après deux passes : la barre « choix minimaux ≤ 4 » est-elle encore une barre, ou est-elle devenue une cible molle assumée ?
4. Le patron tabs s'arrête à tabpanel + aria-selected : à quel moment les flèches ←/→, le tabindex roving et `aria-controls` arrivent-ils — ou le projet assume-t-il officiellement « tabs simplifiés, Tab suffit » ?
5. `illustrerSpec` rejoue l'appel IA à l'identique après un échec : pourquoi un repli qui n'ajoute ni délai ni variation de paramètres — est-ce un confort perçu ou un coût réel doublé ?
6. Deux autocomplétions, deux états vides : unifier le message « Aucune correspondance — saisie libre possible », ou la base Myco mérite-t-elle un état distinct (« introuvable dans les 3 938 espèces ») ?
7. Les suggestions Myco vivent dans une demi-colonne de grille : le formulaire variété a-t-il été regardé à 360 px de large, ou seulement à 640 ?
8. Le focus n'entre pas dans la feuille à l'ouverture (le `focus()` meurt sur `visibility:hidden`) : le parcours clavier de la variété est-il conçu jusqu'à l'ouverture, ou seulement à l'intérieur de la feuille ?

---

**Correctifs de la passe 21E vérifiés :**
- **P2-1 ✅ corrigé sur les deux chemins.** `e-generer` : bascule `etapeEspece(2)` (l.1885) + toast « vérifiez les détails ci-dessous » (l.1886) — l'utilisateur est sur l'étape où vivent les champs remplis. `preparerVarieteDepuisResultat` : reste sur l'étape 1 mais toast guidé « vérifiez l'identité, puis Suivant » (l.2477) + porte structurelle : Enregistrer n'existe que sur l'étape 2 (l.692), l'enregistrement sans relecture est impossible.
- **P3-2 ✅ partiel.** `role="tablist"` + `aria-label` (l.623), `role="tab"` + `aria-selected` (l.624/626, synchronisé l.1727-1728), `role="tabpanel"` + `aria-labelledby` sur `#etape-1`/`#etape-2` (l.629, 660). Absent : navigation fléchée, tabindex roving, `aria-controls`. Fonctionnel au clavier (les deux onglets sont Tab-focusables) mais le claim « complet » surestime.
- **P3-3 ✅ corrigé.** `etapeEspece` focus `e-nom` (étape 1) / `e-habitat` (étape 2) à chaque bascule (l.1729-1730). Réserve : inopérant à l'ouverture (feuille encore `visibility:hidden`) — voir P3-5 nouveau.
- **P3-4 ✅ corrigé.** `.encart-aide` neutre (rayures ambre sur blanc, l.221-227), utilisé l.630 ; l'alerte-orange est redevenue exclusivement « Prudence ».
- **P3-5 ✅ corrigé, par réplication.** `normNom` réduit `[\s\u00A0\-–—_.]+` à l'espace (l.976) : « pied de mouton » ET « pied-de-mouton » → `Hydnum umbilicatum` pos 1 (guide, vignette locale) ; « tue mouches » / « tue-mouches » → `Amanita muscaria` pos 1. L'hydne blanc/élancé ne gagne plus l'égalité (tie-break guide, l.1635-1636). 21/21 noms exacts de fiches → bon taxon pos 1.
- **P3-6 ✅ partiel.** PRODUCT.md passé à « v48 / version 5 » (l.26, l.38) — mais le SW du même commit est cqm-v49 : la doc est déjà périmée d'un cran (P3-3 nouveau). Le pattern « actuellement vN » subsiste.
- **P3-7 ✅ corrigé.** DESIGN.md documente « Étapes progressives (feuille variété) » (l.222-227) : pilules, sémantique ARIA, focus, encart d'aide.
- **P3-8 ✅ corrigé.** `.etape:focus-visible` ajouté à la règle l.180 (outline noir + anneau ambre).

**Claims `bf134a6` vérifiés** (`git show --stat` : DESIGN.md +7, PRODUCT.md ±2, index.html +24/−7, sw.js bump — conforme) : tous les items du message existent dans le code, avec les deux réserves notées (P3-2 « complet » surestimé ; PRODUCT.md v48 vs SW v49).

**Non corrigés (nouveaux de cette passe) :** P3-1 à P3-7 ci-dessus, et les résidus de la section 9.
