# Assessment A — 3e Revue Design : Cueillette Québec — édition Memphis

**Fichier :** `index.html` (1906 lignes, tout HTML/CSS/JS), `sw.js` (cqm-v15), `PRODUCT.md`, `DESIGN.md`, `.impeccable/design.json`
**Commit évalué :** `98411d0` (onglet Paramètres ⚙️ + suppression définitive des espèces, BD IndexedDB v4, export v4)
**Méthode :** lecture statique seule (Assessment A) — aucune modification, aucun détecteur, aucun navigateur. Chaque affirmation vérifiée par lecture de fichier ou calcul Python (contrastes = calculs sRGB réels, pas des estimations).
**Historique :** 1re critique 29/40 → fixes P1+P2 · 2e critique 31/40 → fixes P1-3..P1-5, P2-5..P2-13, P3 → **3e critique : 34/40** (progression +3).

---

## 1. Verdict de spécificité design

**Conceptuelle : ~90 %** (était ~80 %). Le vocabulaire est 100 % domaine : « Mes spots », « Identifier », « Mon journal », « Récolte par mois », « Cueillettes », « Règle d'or », « MORTEL ☠️ », « variété », badges comestible/prudence/immangeable/toxique, « Fausse morille », confusions par espèce. Le 5e onglet « Paramètres ⚙️ » introduit la première zone générique de l'app (unités, clé API) — mais son contenu reste spécifique au produit (unités kg/lb de cueillette, clé Gemini) et son titre de vue respecte la grammaire Memphis (pastille blanche inclinée, `index.html:399`). L'intégration est propre : la clé Gemini n'est plus un intrus dans les feuilles ; elle a un foyer dédié, et le bandeau Identifier (l.1617-1620) pointe vers elle avec un bouton « Configurer la clé → » qui navigue ET focus le champ (`naviguer('parametres');document.getElementById('p-cle').focus()`).

**Visuelle : ~80 %** (était ~70 %). La grammaire Memphis est appliquée partout, y compris sur les nouveaux ajouts : boutons d'unités avec `.actif` = outline noir + rotation -1° (l.154), cartes blanc/crème avec coins cassés et ombres dures, trait noir 3 px sur toute surface colorée, aucun `text-transform`, aucune ombre floutée, aucune boîte système (zéro `window.confirm`/`alert(` — seul un commentaire l.224 en parle). Palette 100 % documentée : **zéro hex hors palette** (vérifié par extraction regex de tous les `#RRGGBB`).

**Test « capture d'écran sans texte » :** le zigzag, les pois, les coins cassés, la vignette à rayures diagonales ambre/blanc, les cartes stat jaune/bleu/vert/rose et le champignon à pois du header suffisent à reconnaître l'univers. **Verdict : toujours profondément ancré Memphis, et les ajouts Paramètres/5e onglet s'intègrent sans rupture.**

---

## 2. Vérification des fixes rounds 1-2

| Fix annoncé | Vérifié ? | Preuve |
|---|---|---|
| Seuils de confiance IA (≥90 fiable, 60-89 à vérifier, <60 inconnu) | ✅ | l.1649-1651 exactement : `fiable = confiance >= 90`, `aVerifier = >=60 && <90`, `inconnue = confiance < 60` ; + fail-safe statut hors vocabulaire → « inconnu » (l.1646-1647) ; prudence morille respectée (l.1653-1656) |
| Bandeau clé sur Identifier + accès en 1 clic | ✅ | l.1614-1621 ; bouton navigue vers Paramètres et focus `p-cle` |
| Contrastes WCAG AA (btn bleu/rose, terracotta, vert kg, header) | ✅ | Calculs : cuir/blanc **5,45:1** · terracotta/blanc **4,95:1** · rouge/blanc **6,07:1** · orange/blanc **4,67:1** · vert kg/blanc **4,97:1** · header brun/noir **4,79:1** · tous les onglets actifs > 4,6:1. Un seul sous-sujet : `.sous` du header, texte noir à opacité .75 sur dégradé brun #C87224 → **≈3,4:1** (AA 4,5 non atteint, détail) |
| Import avec résumé chiffré + confirmation | ✅ | l.1802-1804 : résumé complet (cueillettes/spots/variétés) + `confirmer()` Memphis |
| Zones photo cliquables à vide | ✅ | l.1124, l.1296, l.1515 : clic à vide = ouvre la galerie ; clic avec photo = confirmation de retrait |
| Alerte « Jamais exporté » | ✅ | l.1771-1779 : visible tant que `cqm_exporte` absent, disparaît après export |
| Espèces supprimées (store `supprimees`, double confirmation, export v4) | ✅ | l.686 (store v4), l.965-973 (double confirmation + écriture `supprimees` + purge caches/especes/illustrations), l.1781 (export v4 avec `supprimees`), l.1801-1811 (import v4), l.863 (`toutesEspeces` filtre `!Etat.supprimees.includes` — diff confirmé sur 98411d0), l.1882 (chargement) |
| Clé Gemini déplacée des feuilles vers Paramètres | ✅ | `p-cle` l.410 ; alerte feuille espece l.594 « La clé Gemini se configure dans Paramètres » |

**Résidus de communication (nouveaux, liés au déplacement de la clé) :**
- l.1499 et l.1553 : toasts « 🔑 Ajoutez votre clé Gemini (section Clé IA) » — **la section « Clé IA » n'existe plus** (elle est dans Paramètres). Copy morte → P2.
- l.1623 : toast « bouton “Configurer la clé” ci-dessus » — correct sur l'onglet Identifier (bandeau), mais si l'utilisateur a déjà fermé le bandeau (clé enregistrée puis effacée ailleurs), le bouton n'est « pas ci-dessus ». Mineur.
- La double occurrence `rendreParametres()` l.1834-1837 + l.1843-1846 refait les mêmes mises à jour de labels — duplication sans bug (P3).

---

## 3. Les 10 heuristiques de Nielsen (0-4)

| # | Heuristique | Score | Note clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 4 | Badge compteur header, toasts systématiques, états « Analyse en cours… (10-20 s) », « Génération 1/5 : chapeau… », GPS « Localisation en cours… », séries interrompues annoncées |
| 2 | Correspondance système ↔ monde réel | 4 | Vocabulaire cueillette québécoise, emojis météo, « Sans spot », « coins secrets » |
| 3 | Contrôle et liberté | 4 | Annuler partout, poignée/voile pour fermer les feuilles, double confirmation sur tout acte irréversible, restauration sélective ↩️ |
| 4 | Cohérence et standards | 4 | 5/5 onglets, une seule grammaire visuelle, zéro boîte système, une seule modale de confirmation |
| 5 | Prévention des erreurs | 4 | Double confirmation suppression définitive, résumé d'import chiffré, alerte « Jamais exporté », validation nom/date/espèce avant save, fail-safe IA |
| 6 | Reconnaissance plutôt que mémorisation | 3 | Datalist espèces, pastilles statut persistantes, filtres ; mais : poids saisi en lb converti en kg stocké sans rappel visible de la conversion dans la feuille (l'utilisateur doit retenir que 2,2 lb = 1 kg) |
| 7 | Flexibilité et efficacité | 3 | FAB contextuel, navigation 1 clic, recherche sans accents, pré-remplissage fiche variété depuis résultat IA ; mais pas de tri ni recherche côté Spots/Cueillettes, pas de modification rapide (tout passe par la feuille) |
| 8 | Esthétique et minimalisme | 3 | Memphis assumé et discipliné, mais la feuille Espèce = 10 champs + 4 boutons photo + 2 alertes → la plus chargée de l'app |
| 9 | Aide à la reconnaissance, diagnostic et récupération | 3 | Toasts d'erreur utiles, repli presse-papiers partagé, « Réessayer » photo ; mais toasts sans action (pas de bouton dans le toast), messages d'erreur IA génériques (« IA indisponible (erreur) ») |
| 10 | Aide et documentation | 2 | Aucune aide intégrée (pas de section « ? », pas d'aide contextuelle), les notes `.note` sont présentes mais la découverte passe par l'essai ; le bandeau clé est le seul onboarding réel |

**Total : 34/40** (était 31/40). **Progressions :** H3 et H5 (+1 chacun, double confirmation + fail-safe + import résumé) ; H4 consolidé (le 5e onglet respecte la grammaire). **Aucune régression identifiée.**

---

## 4. Checklist charge cognitive (8 items)

1. **Focus unique (un seul job par écran)** — ✅ Une vue = une tâche ; la feuille Espèce est le seul écran qui déborde (10 champs + 4 boutons photo) → ✅ avec réserve.
2. **Chunking ≤ 4** — ❌ Filtres = 4 puces ✅, mais la feuille Espèce aligne 10 champs ; les cartes stats = 4 ✅ ; les actions d'un item = jusqu'à 4 boutons (spot : Partager/Modifier/🗑️/Carte, l.1029-1031).
3. **Regroupement visuel** — ✅ Cartes, grille2, sections « Description / Caractéristiques / Confusions » avec pastilles de sujet ; la feuille Espèce regroupe bien photo + 4 boutons.
4. **Hiérarchie** — ✅ Titres inclinés pastille (vue → feuille), poids 700/400, échelle 21/20/18/16/13 px cohérente.
5. **Une chose à la fois** — ✅ Feuilles bottom-sheet + voile, modales, navigation 5 onglets.
6. **Choix minimaux ≤ 4** — ❌ Feuille Espèce : 2 boutons d'unités + 2 boutons photo + 2 boutons recherche/IA + 2 boutons save/cancel = 8 choix simultanés ; la modale « Que faire de cette espèce ? » = 3 choix ✅.
7. **Mémoire de travail** — ❌ Conversion kg/lb invisible dans la feuille Cueillette : le label change (« Poids (lb) ») mais aucune indication « stocké en kg » ni calcul affiché — l'utilisateur doit retenir le facteur 2,2. Aussi : l'onglet Paramètres n'est pas accessible pendant la saisie.
8. **Divulgation progressive** — ✅ Détail d'espèce sur demande, illustrations par spécificité en galerie, restauration sur demande.

**Échecs : 2/8** (chunking, mémoire de travail). Le 8e item (divulgation progressive) est la grande force du carnet.

---

## 5. Parcours émotionnel (règle pic-fin)

**Entrée :** pop élastique de la vue, header chaleureux avec champignon à pois, zigzag, pastille rouge du compteur → pic immédiat. **Milieu :** vallées rares et bien traitées — confirmations rebondissantes Memphis (jamais système), états de chargement IA explicites et rassurants (« 10-20 s », « série interrompue »), alertes MORTEL avec antipoison = réassurance à haut risque, pas de peur. **Pic de fin de journée :** la stat « Dernière sortie » en date longue, les tops espèces/spots, les barres mensuelles colorées = vrai pic de récolte. **Faux pic :** aucun « Tout terminé 🎉 » ici — bonne discipline. **Valence :** le rouge reste réservé au danger/suppression (Règle du Rouge Mortel respectée) ; l'offline n'est jamais montré en rouge — correct pour une PWA hors-ligne. **Seul accroc émotionnel :** la feuille Espèce qui s'ouvre avec une alerte « ✨ Entrez le nom, puis “Détails par IA”… (clé Gemini, section 🔑 ci-dessous) » alors que la clé n'est plus ci-dessous mais dans Paramètres — message périmé qui crée une micro-frustration (voir P2-3).

---

## 6. Nouveaux problèmes prioritaires

### P1-1 — Datalist « espèces » contamine le champ avec des statuts hors norme (guide → saisie)
**Sévérité : P1** (données erronées + faux positifs de sécurité).
**Preuve :** `remplirDatalist()` l.1236-1237 = `toutesEspeces().map(e => '<option value="' + esc(e.nom) + '">')`. Or `toutesEspeces()` l.862-865 inclut les **21 espèces d'origine** avec leurs statuts, et `infoEspece` l.867-871 ne renvoie `statut` que si le nom correspond à une espèce **non supprimée** (filtre `!Etat.supprimees.includes`). Donc : Jonathan supprime définitivement la phalloïde → elle disparaît du guide ✅, mais son nom reste dans la liste de suggestions de la feuille Cueillette (le datalist n'est pas filtré) → il la saisit → `infoEspece` ne trouve rien → **aucun badge MORTEL** dans le journal (l.1225 : badge seulement `si info.statut`), aucune alerte de sécurité. Le champ libre permet de toute façon de saisir n'importe quel nom (l.1273-1274 ne valide que la non-vacuité), mais le datalist **propose activement** le nom d'une espèce mortelle sans aucun garde-fou : c'est un piège de suggestion.
**Pourquoi c'est grave :** la promesse du produit (« la sécurité prime », « toute ambiguïté penche vers la prudence ») est contournée par la propre liste de suggestions de l'app.
**Correctif concret :** (a) filtrer `remplirDatalist` sur `!Etat.supprimees` (une ligne, aligne datalist sur le guide) ; (b) si `infoEspece` ne trouve pas l'espèce, afficher le badge `⚠️ Inconnu` (`st-inconnu`) au lieu de rien dans le journal — le fail-safe statut inconnu existe déjà côté IA (l.1646-1647), l'étendre aux saisies libres est cohérent.

### P1-2 — Suppression d'une espèce d'origine : les cueillettes liées perdent leur badge de sécurité
**Sévérité : P1** (sécurité régressive — découverte, non régression de code).
**Preuve :** dans le journal, `infoEspece(c.espece)` (l.1221) cherche dans `toutesEspeces()`, filtrée par `Etat.supprimees` (l.863). Après suppression définitive de la phalloïde : les anciennes cueillettes « Amanite phalloïde » restent listées (le champ `espece` est une chaîne, l.1280), mais **sans badge** et **sans alerte** — alors que le journal affiche les poids (l.1227) et les notes. Or les données de cueillette sont précisément les données que l'utilisateur relit. La suppression d'espèces d'origine (nouvelle feature) crée des « orphelins de sécurité » : c'est le même trou que P1-1, par l'autre bout.
**Correctif concret :** stocker une copie du statut au moment de la saisie (déjà fait : `especeId` est sauvegardé, l.1281 — mais jamais utilisé pour l'affichage) → afficher `badgeStatut` depuis le statut historique archivé (ex. table `statuts_archives` ou champ `statut` sur la cueillette) quand `infoEspece` ne trouve plus rien. À défaut : badge « ⚠️ Inconnu » systématique (même correctif que P1-1b).

### P1-3 — La clé Gemini s'affiche en clair dans Paramètres et dans localStorage
**Sévérité : P1** (données sensibles exposées).
**Preuve :** `p-cle` est un `<input class="saisie">` sans `type="password"` ni `autocomplete` (l.410) ; `rendreParametres()` y réinjecte la clé à chaque visite (`$('p-cle').value = cleIA()` l.1833) ; stockage `localStorage['cqm_cle_ia']` en clair (l.1300, l.1855). L'app est une PWA installable, souvent prêtée (partage à des proches, PRODUCT.md l.11) et l'écran est public en forêt/à la maison. La clé Gemini est un secret facturé à son propriétaire.
**Correctif concret :** `type="password"` + `autocomplete="off"` + bouton œil 👁️ pour révéler ; ne pas réinjecter la clé dans le champ à chaque `rendreParametres()` (afficher « •••• •••• » masqué à la place) ; documenter dans la note (l.411) qu'elle est stockée en clair sur l'appareil et qu'il faut la régénérer si le téléphone est partagé.

### P2-1 — Le datalist Cueillette inclut les variétés perso masquées et les espèces supprimées (cohérence)
**Sévérité : P2.** Même cause que P1-1 : `remplirDatalist` = `toutesEspeces()` sans filtre `cachees` ni `supprimees`. Un nom masqué reste suggéré. Correctif : `[...ESPECES, ...Etat.especesCustom].filter(e => !Etat.cachees.includes(e.id) && !Etat.supprimees.includes(e.id))` — exactement le filtre du guide.

### P2-2 — Le badge « ⭐ perso » réutilise `st-immangeable` avec style inline noir
**Sévérité : P2** (dérive de composant + accessibilité). `badgeStatut` est le seul chemin de rendu des pastilles ; or le badge perso est un `<span class="pastille-statut st-immangeable" style="background:var(--noir);color:var(--creme)">⭐ perso</span>` (l.1151 et l.1193) — il **hérite de la classe sémantique « Immangeable »** (gris) tout en la surchargeant par inline. C'est un « faux badge » : il ment au CSS (un lecteur d'écran/outil d'analyse qui lit `st-immangeable` croit que l'espèce est immangeable) et il crée un nouveau badge non documenté dans DESIGN.md. Correctif : classe dédiée `.st-perso` (fond noir, texte crème) documentée au design system, sans réutiliser `st-immangeable`.

### P2-3 — Alerte de la feuille Espèce périmée : « clé Gemini, section 🔑 ci-dessous »
**Sévérité : P2** (copy trompeuse, conséquence directe du déplacement de la clé). l.542 : « …générez la fiche automatiquement (clé Gemini, section 🔑 ci-dessous) » — la section n'est plus ci-dessous (l.594 dit correctement « dans Paramètres »). Deux messages contradictoires dans la même feuille. Correctif : réécrire l'alerte l.542 comme l.594 (« …la clé Gemini se configure dans Paramètres ⚙️ ») ou la fusionner avec elle.

### P2-4 — Toasts « (section Clé IA) » obsolètes
**Sévérité : P2.** l.1499 et l.1553 référencent « section Clé IA » qui n'existe plus. Correctif : « Paramètres ⚙️ ».

### P2-5 — Conversion lb invisible dans la feuille Cueillette (mémoire de travail, H6/H7)
**Sévérité : P2.** Le label change (« Poids (lb) », l.498/1834), mais l'utilisateur ne voit ni la conversion ni le fait que le stockage reste en kg (la note existe seulement dans Paramètres, l.406, invisible au moment de la saisie). Correctif : sous le champ, une micro-ligne dynamique (« ≈ 1,0 kg » pendant la frappe) ou un rappel dans la note de la feuille.

### P3-1 — `setUnite` n'est pas rappelé à l'init : unité relue mais labels non resynchronisés
**Sévérité : P3.** `Etat.unite` est initialisé depuis `localStorage` (l.853), mais le premier `rendreParametres()` n'a lieu qu'à la navigation (l.885). Si l'unité était « lb » à la fermeture, le label « Poids (kg) » de la feuille (l.498) reste « kg » au premier rendu jusqu'à ce qu'on visite Paramètres. Correctif : appeler `setUnite(Etat.unite)` (ou une `majLabelsUnite()`) dans `init()` l.1895-1903.

### P3-2 — Duplication dans `rendreParametres`/`setUnite`
**Sévérité : P3.** Les mises à jour de `c-poids-label` et `st-label-kg1/2` sont répétées aux l.1834-1837 et l.1843-1846. Correctif : factoriser en une fonction `majLabelsUnite()` appelée par les deux.

### P3-3 — Détail d'espèce : bouton « 🗑️ Supprimer » pour une variété perso dans le détail, mais « 🗑️ Masquer » pour une espèce d'origine
**Sévérité : P3.** l.1185-1187 : dans le détail, une variété perso affiche « Supprimer » (ouvre la modale choix), une espèce d'origine affiche « Masquer » (ouvre aussi la modale choix, qui permet de supprimer). Deux libellés pour un même point d'entrée — la modale est la même. Correctif : libellé unique « Masquer ou supprimer » dans les deux cas, ou bouton « 🗑️ Masquer » partout.

### P3-4 — Documentation dérivée (PRODUCT.md, DESIGN.md, design.json)
**Sévérité : P3.** PRODUCT.md : « IndexedDB (`cqm_bd` v3) » → v4 (l.38), « export/import JSON (version 3…) » → v4 (l.26), « SW … (actuellement v10) » → v15 (l.37). DESIGN.md l.169 et l.208 + design.json « 4 onglets » → 5 (l.388-389 du JSON). Aucun de ces écarts ne casse l'app, mais la documentation est devenue une source de vérité périmée.

---

## 7. Red flags par persona, observations mineures, questions provocatrices

### Red flags par persona

**Jonathan, en forêt, une main, sans réseau (persona principal, mobile)**
- ✅ Tout le parcours terrain (spot → cueillette → identification) est hors-ligne, rapide, une main.
- 🚩 Le champ « Poids (lb) » sans conversion visible force un calcul mental en forêt (P2-5).
- 🚩 Feuille Espèce : 10 champs + 4 boutons photo — à remplir une main, debout, c'est le moment le plus fragile.
- 🚩 Si la clé Gemini expire en forêt (sans réseau, impossible de la régénérer), l'identification photo échoue avec un message générique — pas de repli hors-ligne explicite (H9).

**Utilisateur réduit en accessibilité (lecture d'écran, gros doigts)**
- ✅ Cibles ≥ 34 px, contraste AA généralisé, focus ring noir 3 px, modales `role="alertdialog"` + aria-labelledby/describedby.
- 🚩 Boutons emoji seuls sans `aria-label` explicite : « 🗑️ » des items (l.1031, l.1231), « ✖️ » (l.1532). Le FAB « ＋ » a bien `aria-label="Ajouter"` (l.420 ✅) ; les boutons « 📤 Partager »/« 🗺️ Carte » ont du texte. Pour les boutons emoji seuls, le nom accessible dépend du lecteur d'écran (annonce « poubelle » ou « corbeille », incohérent) — ajouter des `aria-label` stables (« Supprimer », « Retirer ») garantirait un nom cohérent.
- 🚩 Badge « ⭐ perso » ment à la sémantique (P2-2).

**Utilisateur distrait, multi-tâche (partage du téléphone, notifications)**
- 🚩 La clé Gemini en clair (P1-3) : écran partagé avec un proche = secret exposé.
- 🚩 Double confirmation bienvenue, mais aucune indication du nombre d'étapes restantes (« Étape 1 sur 2 ») — on peut croire que c'est fini après la 1re confirmation.
- 🚩 La modale de choix d'espèce (l.444-450) n'a pas de poignée ni de voile dédié : elle se ferme via `voile-confirm` (l.946) mais le contraste entre les deux modales empilées peut prêter à confusion.

### Observations mineures

- **Méta `opacity:.75`** sur `.item .meta` (l.135) : texte noir 7,23:1 sur blanc ✅ mais en dessous du 7:1 AAA — acceptable.
- **Poignée des feuilles** `.poignee` opacity .35 sur blanc : 2,16:1 — décoratif assumé, mais sous le seuil des éléments d'interface.
- **Labels des cartes stats** `.stat-carte .libelle` opacity .8 : ~11:1 sur ambre (calculé), correct.
- **`st-label-kg1`/`st-label-kg2`** : l'ID garde « kg » même en lb (l.376-378) — cosmétique.
- **Barre de mois vide** `#D8C9AC` vs fond crème : 1,35:1 — c'est un fond de graphique, acceptable (la barre active est cerclée de noir).
- **`c-poids` en `type="number" step="0.1"`** : la virgule « 1,5 » est acceptée par `kgDepuisSaisie` (l.658-662) mais certains claviers iOS `type=number` n'affichent pas la virgule — le parseur est là, le clavier peut manquer.
- **`img src` non échappées** (l.1021, l.1149, l.1180, l.1191) : les URLs de photos Wikimedia/Ia sont injectées telles quelles ; un `"` dans une URL casserait l'attribut (faible risque, mais le `esc()` est utilisé partout ailleurs).
- **`e-photo-info`** peut afficher « 🌐 Photo distante — visible après une 1re visite avec réseau » (l.1461) : le SW exclut Wikimedia du cache (sw.js l.50) → la photo distante **ne sera jamais** disponible hors-ligne malgré le message — copy trompeuse mineure (P3, à corriger par un vrai embarquement ou un message honnête).
- **`g-recherche` placeholder « 🔎 Chercher un champignon… »** : pas de libellé associé (accessibilité), mais le placeholder est informatif.
- **`manifest.json`** : non relu (hors périmètre), mais le `theme-color` ambre (l.6) est cohérent avec la palette.

### Questions provocatrices

1. **Que doit-on montrer dans le journal quand une espèce mortelle a été supprimée du guide ?** Un badge « ⚠️ Inconnu », le statut archivé, ou rien — et qui décide ?
2. **La suppression définitive d'une espèce d'origine devrait-elle être bloquée si des cueillettes y sont liées ?** La double confirmation suffit-elle, ou faut-il un compteur « 3 cueillettes référencent cette espèce » dans la modale ?
3. **Le datalist propose-t-il délibérément des espèces que le guide a bannies ?** Si non, pourquoi le filtre `supprimees` n'est-il pas appliqué à `remplirDatalist` ?
4. **La clé Gemini est-elle un secret ou une simple commodité ?** Si c'est un secret, pourquoi n'est-elle pas en `type="password"` avec un œil ?
5. **Qui utilise vraiment « Détails par IA » en forêt ?** La feuille Espèce assume une connexion et 10-20 s d'attente — est-ce compatible avec « Le terrain d'abord » ou est-ce une fonction de bureau à re-tasser ?
6. **Le 5e onglet annonce-t-il la fin de la barre à 5 items ?** Les Paramètres vont grossir (langue, thème, export, à propos) — que se passe-t-il au 6e onglet ?
7. **Si l'export est le seul filet de sécurité, pourquoi n'est-il pas proposé au premier lancement, quand le carnet est vide, plutôt que seulement dans Stats ?**
8. **« Photo distante » pour Wikimedia : est-ce un vrai hors-ligne ou une promesse ?** Le SW exclut Wikimedia du cache — le message « visible après une 1re visite » est-il honnête ?
9. **Le badge « ⭐ perso » doit-il exister ?** Il ajoute une information (« c'est ma variété ») mais emprunte la sémantique « Immangeable » — vaut-il une vraie classe documentée ou doit-il disparaître ?
10. **Combien de champs une « nouvelle variété » mérite-t-elle en forêt ?** La feuille actuelle en a 10 — est-ce la fiche idéale ou le formulaire d'un autre produit ?

---

*Rapport généré par lecture statique (Assessment A). Aucun fichier modifié. Contrastes calculés (sRGB → luminance relative → ratio), aucune estimation.*
