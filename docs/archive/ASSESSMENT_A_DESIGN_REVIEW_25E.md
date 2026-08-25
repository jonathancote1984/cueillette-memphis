# Assessment A — Critique design (25e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2752 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v52) · **Méthode :** lecture statique seule (Assessment A, aucun navigateur, aucun détecteur). Vérification des 8 claims de `3360ade` (fix critique-24e) ligne par ligne dans le code — chaque ligne citée provient de `read_file` (aucune de search_files) ; contrastes calculés par `contrast-check.py` ; arbre git propre (HEAD = état évalué).

**Note globale :** les 8 claims de `3360ade` sont **tenus en code** — P1-1 (cœur), P2-1, P2-2, P3-1, P3-3, P3-4, P3-5 : 7/8 vérifiés sans réserve ; P3-2 vérifié mais introduit une régression de valence (☠️ sur la carte « attente » des comestibles). Nouveau passif : **3 P2** (le filet du P1-1 saute les espèces masquées/supprimées ; ☠️ sur l'ambre des comestibles ; carte « ✅ Comestible » + « confiance insuffisante » contradictoire) et 1 P3. Score **38,5/40 — plateau honnête** : +0,5 H5 (le guide a le dernier mot, vérifié) compensé par −0,5 H4 (deux incohérences de valence nouvelles sur l'écran de décision).

---

## 1. Verdict de spécificité design : 9/10 (inchangé)

Rien ne sort de la grammaire Memphis cette passe : la logique du croisement guide/IA est invisible pour l'œil, 0 couleur hors palette, 0 ombre floutée, 0 uppercase, 0 boîte système, contrastes tous AA (4,61–13,5:1). **Axes :** conceptuel ~90 % (carnet de chasse, vocabulaire mycologique, antipoison, verdicts ⚠️/☠️/✅) · visuel ~90 % (une capture sans texte révèle Memphis-automne-champignon). Verdict : spécifique sur les deux axes — et la passe le prouve en creux : c'est un correctif de SÉCURITÉ, et il se fond dans le design sans le dégrader.

## 2. Évaluation holistique

- **Hiérarchie visuelle** — tenue. h1 unique, h2 par vue, h2 nom d'espèce en détail. La carte de résultat idphoto (l.2456-2478) gagne en cohérence : badge, alerte et bouton fiche dérivent tous du même `r.statut` muté par le croisement.
- **Architecture de l'information** — le statut « inconnu » est désormais intégré au filtre « ☠️ Ne pas manger » (l.1382 ✓). Mais le filet de sécurité du flux photo ne consulte pas les espèces masquées/supprimées (P2-1) alors que le flux cueillette, lui, archive (`especeId`, l.1510-1513) — deux flux, deux mémoires.
- **Adéquation émotionnelle** — la vallée 24E (« ✅ Comestible » sur une espèce MORTELLE du guide) est refermée pour les espèces visibles : IA « comestible » 95 % sur phalloïde → badge MORTEL + antipoison (traçage l.2431-2435 → l.2459, 2462-2463). Deux nouvelles petites vallées : un ☠️ apparaît sur la carte ambre d'une espèce comestible dès le premier critère coché (P2-2), et une carte peut afficher « ✅ Comestible » et « confiance insuffisante » en même temps (P2-3).
- **Découvrabilité** — rien au hover ; bandeau clé, FAB contextuel, étapes progressives inchangés.
- **Composition** — colonne 640 px, feuille 84 vh, grilles 2 colonnes conservées ; la carte idphoto conserve sa structure carte unique pleine largeur.
- **Typographie** — Fredoka 400-700 exactement (aucun 900), aucune taille arbitraire nouvelle ; Meta 400/12,5 px/0,85 conforme à DESIGN.md l.162.
- **Couleur** — 0 dérive. Contrastes recalculés : pastilles gris #A89882 6,08:1 · olive 4,61:1 · ambre 7,59:1 · toxique 4,67:1 · mortel 6,07:1 · blanc/rose 4,95:1 · blanc/cuir 5,45:1 · vert-mesure 4,97:1 · header 4,79:1 · alertes 13,3-13,5:1 — tous AA. La Règle du Rouge Mortel tient (rouge uniquement : badge MORTEL, suppression, compteur d'étape, compteur n/n — jamais décoratif).
- **Accessibilité** — la passe 24E confirme ses gains : `aria-current="page"` dans le HTML initial (l.500 ✓ P3-1), `aria-valuetext` en unité d'affichage sur les barres (l.2522 ✓ P3-4 — l'oreille et l'œil partagent enfin la même unité), compteur `aria-live` (l.1433). Reste : `aria-invalid` = 0 partout (résidu), lightbox sans piège à focus (nouveau, mineur).
- **États** — boutons IA désactivés pendant les appels (l.1895, 2328), états vides honnêtes, toast de coercition déplacé au point où l'information existe (l.2428 ✓ P3-3). Nouveau : état contradictoire possible sur la carte idphoto (P2-3).
- **Copy** — le toast « Statut IA hors vocabulaire — confirmez la comestibilité » (l.2428) tire désormais au bon endroit. Le toast de pré-remplissage (l.2505) ne mentionne toujours pas le statut transféré (résidu 24E).
- **Cas limites** — dates locales, import versionné (v5, garde v>5/v<5), checklist réindexée au retrait. Nouveau : l'inclusion floue d'`infoEspece` peut apparier un nom générique (« Amanite ») à l'espèce la plus courte (panthère) — sur-verdict systématique (sûr, mais le bouton « Voir la fiche du guide » peut lier une espèce que l'IA n'a pas nommée, cf. questions).

## 3. Évaluation de charge cognitive : 1 échec / 8 (inchangé)

1. Focus unique ✅ · 2. Chunking ≤ 4 ✅ · 3. Regroupement visuel ✅ · 4. Hiérarchie ✅ · 5. Une chose à la fois ✅ · 6. Choix minimaux ≤ 4 ❌ — **étape 1 = 5 champs** (nom, latin, comestibilité, saison, prudence) + 2 boutons + 1 encart ; inchangé depuis 21E · 7. Mémoire de travail ✅ — le croisement guide/IA *réduit* la charge au moment critique : l'utilisateur n'a plus à se souvenir du statut du guide pendant qu'il lit la carte IA, la carte le fait pour lui · 8. Divulgation progressive ✅.

**1 échec franc sur 8.**

## 4. Voyage émotionnel

Ouverture chaleureuse → guide → fiche hybride inchangés. **La vallée majeure de 24E est fermée dans son cas nominal :** le flux photo consulte désormais le guide via `infoEspece` (normNom + synonymes + tolérance de frappe), classe les gravités et ne laisse JAMAIS un badge vert s'afficher quand le guide dit plus grave (l.2429-2435) — et la prudence dérivée du guide voyage jusqu'à la fiche variété (l.2437 → l.2499). **Mais trois vallées subsistent, plus petites :** (a) masquer ou supprimer une espèce MORTELLE du guide fait disparaître son filet de sécurité du flux photo (P2-1) — le pire moment (décision de consommer) dépend d'une action de rangement ; (b) le premier critère coché sur une chanterelle fait apparaître « ☠️ Critères manquants » sur la carte ambre (P2-2) — un faux pic d'alerte qui, répété sur les comestibles, désensibilise le glyphe au moment où il compte (phalloïde) ; (c) une carte peut juxtaposer « ✅ Comestible » et « la confiance est insuffisante pour une identification formelle » (P2-3) — la pire des incohérences : l'utilisateur ne sait plus si la carte le rassure ou l'avertit. Fin de journée : rappel d'export honnête, pas de faux pic.

## 5. Scores heuristiques Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 4 | Toast de coercition au bon endroit, boutons désactivés, compteur live, aria-valuetext |
| 2 | Correspondance monde réel | 4 | Vocabulaire du carnet de chasse ; le guide « a le dernier mot » comme un aîné mycologue — métaphore juste |
| 3 | Contrôle et liberté | 4 | Garde-fou (voile/poignée/Escape), retours, annulable partout, Escape-modale gagne (ordre vérifié l.1093-1108) |
| 4 | Cohérence et standards | **3,5** (−0,5) | ARIA complétés, mais ☠️ sur la carte ambre des comestibles (P2-2) et carte « ✅ + confiance insuffisante » (P2-3) — deux langages pour un même état |
| 5 | Prévention des erreurs | **3,5** (+0,5) | P1-1 vérifié : le guide prime sur la gravité, la prudence voyage, « inconnu » dans npas. Plafonné par le trou des espèces masquées (P2-1) |
| 6 | Reconnaissance vs mémorisation | 4 | Noms requêtables sous toutes leurs formes ; croisement par normNom + synonymes + Levenshtein |
| 7 | Flexibilité / efficacité | 4 | IA remplit les 2 étapes, retry + repli modèle, ordre des images persistant, 21 guide:true dans la base |
| 8 | Esthétique minimaliste | 3,5 | Étape 1 à 5 champs, étape 2 ~13 éléments (inchangé) |
| 9 | Aide à la récupération d'erreurs | 4 | messageErreurIA par cause, parserJSONIA tolérant, import versionné ; le toast de coercition tire réellement désormais |
| 10 | Aide et documentation | 4 | P3-5 vérifié : DESIGN.md documente le statut « inconnu » (l.192) et le compteur noir (l.219) |

**Total : 38,5/40 — plateau honnête.** Les correctifs 24E sont vérifiés (7/8 sans réserve) ; le dock est H4 (4 → 3,5) pour les deux incohérences de valence nouvelles, compensé par H5 (3 → 3,5) : le filet du guide est réel et vérifié dans le cas nominal.

## 6. Forces spécifiques

1. **La mutation à la source est le bon patron, au bon endroit.** Le croisement guide/IA (l.2431-2437) mute `r.statut` et `r.prudence` AVANT tout rendu : badge (l.2459), alertes (l.2462-2470), bouton fiche (l.2473-2474) et transfert variété (l.2497-2499) consomment tous la même valeur corrigée. Chaque futur consommateur est protégé sans éditer un seul rendu — le contraire du patch par écran. La preuve : le transfert, qui était le trou de 23E, est réparé sans ligne dédiée (il hérite de la mutation).
2. **Le repo contient déjà le patron manquant pour P2-1.** Le flux cueillette archive l'espèce masquée/supprimée (`especeId` + `ESPECES.find`, l.1510-1513, commentaire « P1-2 ») — le correctif du trou des espèces masquées dans le flux photo est littéralement un copier-coller de ce patron vers `analyserPhoto`, pas une invention.
3. **La discipline Memphis survit à une passe de sécurité.** 0 nouvelle couleur, 0 ombre floutée, 0 uppercase, 0 boîte système, 21/21 `guide:true` dans la base MycoQuébec, SW cqm-v52 — le correctif le plus chargé en enjeux de l'histoire de l'app ne coûte rien au langage visuel.

## 7. Problèmes prioritaires

**P2-1 (NOUVEAU, SÉCURITÉ — trou dans le fix P1-1) — le filet du guide saute les espèces masquées ou supprimées.** `analyserPhoto` croise via `infoEspece` (l.2431), qui cherche dans `toutesEspeces()` (l.973-976) — laquelle FILTRE `Etat.cachees` et `Etat.supprimees`. Si Jonathan a masqué « Amanite phalloïde » du guide (fonction 🙈 de premier plan, l.1452), une photo identifiée « comestible, 95 % » par l'IA ne croise plus rien : `connue.id = null` → pas de surclassement GRAV → badge vert « ✅ Comestible ». Le filet de sécurité dépend d'un choix de rangement. Pire : le flux cueillette gère déjà ce cas (l.1510-1513, « badge de sécurité même si l'espèce a été supprimée ou masquée ») — deux flux, deux mémoires, et le flux NON protégé est celui de la décision de consommer. *Fix :* dans `analyserPhoto`, doubler le croisement — `infoEspece(r.espece)` puis, si `id` nul, une recherche directe dans `ESPECES` + `Etat.especesCustom` SANS filtre de visibilité (patron P1-2) ; conserver le surclassement GRAV dans les deux cas.*

**P2-2 (NOUVEAU, RÉGRESSION introduite par le fix P3-2) — ☠️ sur la carte « attente » des espèces comestibles.** Le rendu initial distingue les deux variantes du verdict-att : `⚠️` pour comestible/prudence (l.1444), `☠️` pour non-comestible (l.1445). `basculerSpec` écrase le titre sans distinction : `txtAtt.textContent = '☠️ ' + (nb === 0 ? … : 'Critères manquants')` (l.1496). Sur une chanterelle, dès le premier critère coché, la carte ambre affiche « ☠️ Critères manquants » — le glyphe réservé au danger (DESIGN.md l.192) sur l'état « en attente » d'une espèce comestible ; répété sur les 13 comestibles du guide, il désensibilise le ☠️ au moment où il compte (phalloïde). De plus le corps de la carte n'est pas mis à jour (à 1/5, le titre dit « Critères manquants » pendant que le texte dit « Cochez chaque critère… », la version nb=0). *Fix :* brancher le préfixe comme le rendu initial — `(nonComestible ? '☠️ ' : '⚠️ ')` — et mettre à jour aussi le texte du corps, ou re-rendre la zone verdict complète à chaque `basculerSpec`.*

**P2-3 (NOUVEAU, VALENCE) — carte « ✅ Comestible » + « confiance insuffisante » simultanés.** Le vocabulaire de statut est vérifié sans normalisation de casse (l.2427, sensible à « Comestible » majuscule ou à « prudence » comme statut — plausible venant du modèle). Si le statut est hors vocabulaire ET que le guide surclasse en comestible ET que confiance ≥ 90 : `afficheComestible = fiable && !prudente` = vrai → badge vert (l.2459), pendant que `aVerifier` (calculé sur le `statutValide` D'ORIGINE, l.2442) force la méta « — vérifiez avec le guide » (l.2461) et l'alerte orange « la confiance est insuffisante pour une identification formelle » (l.2468-2469) sous un « Confiance : 95 % » affiché juste au-dessus. La carte se contredit au moment de la décision. *Fix :* normaliser `(r.statut || '').toLowerCase()` dans le test du vocabulaire, et dériver `aVerifier` de la seule bande de confiance (60–89) — le cas « statut invalide » est déjà traité par la coercition + le toast + le surclassement du guide.*

**P3-1 (NOUVEAU, COHÉRENCE) — les feuilles spot et cueillette se ferment sans garde-fou.** Le voile (l.1047-1050), la poignée (l.1051-1054) et Escape (l.1107-1108) ferment `sheet-spot`/`sheet-cueillette` instantanément : une description tapée + une photo choisie disparaissent sans confirmation, alors que la feuille variété (même interaction, même famille) est protégée par `formulaireEspeceSale` (l.1782-1791). L'utilisateur apprend que le voile est sûr sur une feuille et destructeur sur l'autre. *Fix :* généraliser le garde-fou — un `formulaireSale(id)` générique (champs non vides ou photo) branché sur les trois feuilles dans les trois gestes (voile, poignée, Escape).*

## 8. Red flags par persona

- **Jonathan en forêt, une main, sans réseau** : le moment de vérité (photo ID) est désormais protégé dans le cas nominal — phalloïde mal lue « comestible 95 % » → MORTEL + antipoison (vérifié par traçage). **Pire moment :** identifier une espèce qu'il a masquée ou supprimée du guide — le filet se tait (P2-1). Et s'il est en train de cocher sa checklist de chanterelle, le ☠️ du verdict-att peut le faire sursauter pour rien (P2-2).
- **Proche débutant (via export/import)** : le transfert porte enfin la prudence du guide (l.2437 → 2499 ✓) — la morille pré-remplit « ⚠️ Prudence » cochée. Mais la carte contradictoire (✅ + « confiance insuffisante », P2-3) lui apprend à ne pas faire confiance aux badges, et le ☠️ sur les comestibles (P2-2) brouille la seule règle simple qu'il avait : « ☠️ = ne jamais manger ».
- **Utilisateur au clavier / lecteur d'écran** : `aria-current` existe à froid (l.500 ✓), les barres annoncent l'unité d'affichage (l.2522 ✓). Le titre du verdict-att annoncé à voix haute devient « ☠️ Critères manquants » sur une espèce comestible (P2-2 — même incohérence, en audio), et la lightbox n'a pas de piège à focus (Tab sort derrière le dialogue). Pire moment : ouvrir une fiche comestible, cocher un critère, entendre ☠️.

## 9. Observations mineures

**Nouveaux :**
- `ouvrirLightbox` (l.2358-2378) : dialogue `aria-modal` sans piège à focus — Tab et Shift+Tab sortent derrière la photo agrandie ; l'overlay n'est pas `aria-hidden` pour le reste de la page.
- Les suggestions d'espèce de la feuille cueillette (l.1533-1539) n'affichent que le nom, sans badge de statut — le signal de sécurité n'apparaît qu'après l'enregistrement (contrairement aux suggestions Myco de la feuille variété, qui ont vignette + latin).
- Commentaire l.2426 « P1-5 » : numérotation d'une ancienne passe, le référent actuel est 23E-P2-1 — le prochain développeur ne retrouvera pas le finding.

**Résidus inchangés (non re-scorés, tous re-confirmés présents en 25E) :** `rendreBandeauCle` insère un `<button>` dans un `<p class="note">` (l.2394-2397, HTML invalide) · `p-cle` sans label (l.460) · toast de pré-remplissage sans mention du statut transféré (l.2505) · `retirerIllu` ne re-rend pas la vue détail sous-jacente (l.2307-2324) · PRODUCT.md l.39 (`especesCustom`/`cachees`) vs code (`especes`/`caches`, l.792-793) · champ recherche du guide sans label visible (l.411) · échec silencieux de `chargerBaseMyco` (l.1620) · focus perdu sur les selects de filtre (re-rendu `rendreFiltres`, l.1362-1363) · `alt="photo"` générique (l.1186) · `ouvrirMyco` sans message hors-ligne (l.2355-2357) · `.mois-col .lab` 10,5 px (l.339) · cache SW non borné pour les GET réussis (sw.js) · `aria-invalid` : 0 partout, validation toast-only · `COULEURS_MOIS` cycle 6×2 sans sémantique de saison (l.2517) · `aria-valuenow`/`aria-valuemax` restent en kg bruts (l.2522 — couvert par `aria-valuetext`, moindre).

## 10. Questions provocatrices

1. Masquer une espèce MORTELLE retire-t-elle son filet de sécurité du flux photo ? Pourquoi le flux cueillette archive l'espèce masquée (P1-2) et le flux idphoto l'oublie — les deux flux ne devraient-ils pas partager une seule fonction de croisement, visibilité comprise ?
2. Le ☠️ du verdict-att est-il un état de vérification ou un état de danger ? Un seul glyphe peut-il signifier « ne jamais manger » ET « critères manquants » sur la même page, à deux cartes d'écart ?
3. Quand l'IA sort un statut hors vocabulaire et que le guide le corrige en comestible, la carte peut afficher ✅ et « confiance insuffisante » ensemble : les textes de la carte doivent-ils dériver du statut d'origine ou du statut effectif — et qui teste ce cas ?
4. Cas inverse du P1-1 : l'IA dit « MORTEL, 95 % » d'une espèce que le guide marque comestible. Faut-il afficher MORTEL sans nuance, ou « le guide la dit comestible — vérifiez » ? Jusqu'où va la primauté du guide ?
5. L'inclusion floue d'`infoEspece` peut lier « Amanite » à l'espèce la plus courte (panthère) : le bouton « Voir la fiche du guide » doit-il être réservé aux correspondances exactes/synonymes, et le surclassement GRAV aux appariements sûrs ?
6. Les feuilles spot et cueillette se ferment sans garde-fou sur un tap au voile : pourquoi la feuille variété mérite-t-elle une protection et pas les deux autres — la longueur du formulaire est-elle le bon critère ?
7. Le toast de coercition (2,2 s) tire avant le rendu de la carte : l'avertissement « statut IA hors vocabulaire » est-il réellement lu, ou faut-il l'inscrire dans la carte corrigée (ex. méta « statut IA corrigé par le guide ») ?
8. La lightbox n'a pas de piège à focus : la photo agrandie est-elle un dialogue, ou un état de la page qui devrait être annoncé autrement ?

---

**Correctifs de la passe 24E vérifiés (8/8, dont 7 sans réserve) :**
- **P1-1 ✅ corrigé (cœur), avec réserve.** `connue = infoEspece(r.espece)` (l.2431) — normNom + synonymes + Levenshtein ≤ 2 ; `GRAV = { inconnu:0, comestible:1, immangeable:2, toxique:3, mortel:4 }` (l.2432) ; surclassement `si GRAV[guide] > GRAV[IA]` (l.2433-2435). Traçage IA « comestible » 95 % sur phalloïde : statut → mortel → badge MORTEL (l.2459), alerte rouge + antipoison (l.2462-2463), statut muté propagé au transfert (l.2497). **Réserve :** le croisement ne voit pas les espèces masquées/supprimées (P2-1).
- **P2-1 ✅ corrigé.** `if (connue.id && connue.prudence) r.prudence = true` (l.2437) → `$('e-prudence').checked = !!r.prudence` (l.2499). La prudence affichée = la prudence transférée ; `formulaireEspeceSale` la couvre (l.1785).
- **P2-2 ✅ corrigé.** `Etat.filtre === 'npas'` inclut `e.statut === 'inconnu'` (l.1382).
- **P3-1 ✅ corrigé.** `aria-current="page"` sur l'onglet Spots dans le HTML initial (l.500), avant tout appel à `naviguer`.
- **P3-2 ✅ corrigé, avec réserve.** `basculerSpec` met à jour le titre du verdict-att (l.1494-1496) — plus de « Rien n'est encore vérifié » figé à 1/5. **Réserve :** préfixe ☠️ inconditionnel → régression de valence sur les comestibles (P2-2).
- **P3-3 ✅ corrigé.** Toast déplacé au point de coercition (l.2428) ; le `else` du transfert est un filet silencieux documenté (l.2498).
- **P3-4 ✅ corrigé.** `aria-valuetext="' + esc(fmtKg(e[1])) + '"` sur les barres top (l.2522) — l'annonce parle l'unité d'affichage.
- **P3-5 ✅ corrigé.** DESIGN.md l.192 liste « gris Inconnu ⚠️ (statut fail-safe…) » (6 pastilles) ; DESIGN.md l.219 décrit la pastille noire « n/5 » sur crème — conforme au code (l.274).

**Claims `3360ade` vérifiés** (`git show --stat` : DESIGN.md ±4, index.html +26/−17, sw.js ±1 — conforme) : cqm-v52 en sw.js l.4 ; 21 `"guide":true` dans `img/mycoquebec.json` ; arbre git propre (aucun changement non commité) ; 0 régression CSS dans le diff (aucun nouveau `opacity:`, aucun hex hors palette, aucun flou).

**Non corrigés (nouveaux de cette passe) :** P2-1, P2-2, P2-3, P3-1 ci-dessus, et les résidus de la section 9.
