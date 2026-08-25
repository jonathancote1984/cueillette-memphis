# Assessment A — Critique design (24e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2743 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v51) · **Méthode :** lecture statique seule (Assessment A, aucun navigateur, aucun détecteur). Vérification des 6 findings de la passe 23E (P2-1, P3-1 à P3-5, verdict dynamique) ligne par ligne dans le code : diff complet de `5d34539` relu, chaque ligne citée provient de `read_file` (aucune de search_files).

**Note globale :** les 6 claims de `5d34539` sont **tenus en code** — P2-1 (cœur), P3-1, P3-2, P3-4, P3-5, verdict n/n : 6/6 vérifiés, dont 2 avec réserves (P2-1 laisse échapper un signal de sécurité voisin ; P3-3 n'a converti que les labels). Nouveau passif : **1 P1 de sécurité** (le verdict de l'IA écrase celui du guide sur la carte de résultat), 2 P2 (prudence du guide perdue au transfert ; « inconnu » absent du filtre « Ne pas manger »), 5 P3. Score **38,5/40 — baisse honnête de 0,5** : les correctifs sont confirmés, mais la passe révèle une dette de sécurité pré-existante plus lourde que celle corrigée (H5 : 3,5 → 3).

---

## 1. Verdict de spécificité design : 9/10 (inchangé)

Rien de nouveau ne sort de la grammaire : la nouvelle option « ⚠️ Inconnu » (l.647) réutilise la pastille grise `st-inconnu` existante, les ARIA ajoutés sont invisibles pour l'œil, 0 couleur hors palette, 0 ombre floutée, 0 uppercase, 0 boîte système. **Axes :** conceptuel ~90 % (carnet de chasse, vocabulaire mycologique, antipoison, verdicts ⚠️/☠️) · visuel ~90 % (une capture sans texte révèle Memphis-automne-champignon). Verdict : spécifique sur les deux axes.

## 2. Évaluation holistique

- **Hiérarchie visuelle** — tenue. h1 unique, h2 par vue, h2 nom d'espèce + h3 en détail. Le compteur (pastille noire, l.274) reste lisible contre l'œil.
- **Architecture de l'information** — la nouvelle valeur de statut « inconnu » (créée par le fix P2-1) n'est pas intégrée à l'IA du guide : invisible dans le filtre « ☠️ Ne pas manger » (P2-2, l.1382).
- **Adéquation émotionnelle** — la vallée 23E (« ✅ Comestible » silencieux après un verdict « À vérifier ») est refermée : le select s'ouvre désormais sur « ⚠️ Inconnu » (l.647, 2487-2489). Mais deux vallées de confiance subsistent au pire moment : une espèce MORTELLE du guide peut recevoir un badge « ✅ Comestible » si l'IA se trompe avec confiance ≥ 90 (P1-1), et la prudence du guide s'affiche sur la carte puis disparaît au transfert (P2-1).
- **Découvrabilité** — rien au hover ; bandeau clé inchangé ; FAB contextuel inchangé.
- **Composition** — colonne 640 px, feuille 84 vh, grilles 2 colonnes conservées.
- **Typographie** — Fredoka 400-700 exactement ; Meta 400/12,5 px/0,85 désormais documenté (DESIGN.md l.162, P3-5 23E ✓).
- **Couleur** — 0 dérive. Contrastes stables depuis 23E (Identifier `#B3540B` ≈ 4,64:1 ; toxique ≈ 4,65:1 ; textes .85 = 4,91:1 composé). La Règle du Rouge Mortel tient.
- **Accessibilité** — la passe a été productive : `aria-pressed` sur les cartes checklist (l.1435, 1487), `aria-live` sur le compteur (l.1433), `aria-current` dans `naviguer` (l.1017-1019), labels ARIA des barres/tiges en `fmtKg` (l.2513, 2544). Reste : `aria-current` absent au chargement initial (P3-1), `aria-valuenow/max` toujours en kg bruts (P3-4), `aria-invalid` toujours 0 (résidu).
- **États** — boutons désactivés pendant les appels IA (inchangé), états vides cohérents, message Myco désormais interpolé (`base.length`, l.1656 — P3-4 23E ✓).
- **Copy** — toasts à valence alignée. Le toast « Statut IA hors vocabulaire » (l.2489) est du code mort : la coercition en amont garantit que `r.statut` est toujours dans le vocabulaire (P3-3).
- **Cas limites** — dates locales, import versionné (v5, garde v>5/v<5), checklist réindexée au retrait, séquence de rechargement gardée. Nouveau : la nouvelle option « inconnu » n'exige aucun changement de version d'export (chaîne libre) — correct.

## 3. Évaluation de charge cognitive : 1 échec / 8 (inchangé)

1. Focus unique ✅ · 2. Chunking ≤ 4 ✅ · 3. Regroupement visuel ✅ · 4. Hiérarchie ✅ · 5. Une chose à la fois ✅ · 6. Choix minimaux ≤ 4 ❌ — **étape 1 = 5 champs** (nom, latin, comestibilité, saison, prudence) + 2 boutons + 1 encart ; l'ajout de l'option « inconnu » ne change pas le compte (5 options dans un select = 1 champ). Inchangé depuis 21E. · 7. Mémoire de travail ✅ · 8. Divulgation progressive ✅.

**1 échec franc sur 8.**

## 4. Voyage émotionnel

Ouverture chaleureuse → guide → fiche hybride inchangés. **La vallée 23E est fermée dans son cas nominal :** le flux photo → « Ajouter comme variété » ne peut plus présenter « ✅ Comestible » silencieusement quand le verdict était « À vérifier » — le select porte « ⚠️ Inconnu ». **Mais le faux pic de confiance persiste ailleurs, en plus grave :** si l'IA identifie une espèce MORTELLE du guide comme comestible avec confiance ≥ 90, la carte de résultat affiche le badge vert de l'IA, sans aucune confrontation avec le verdict du guide — l'app possède la vérité (nom = espèce du guide) et choisit de ne pas l'utiliser (P1-1). C'est le moment où l'utilisateur décide de manger. **Vallée plus petite, même mécanique que le fix :** la morille (guide, `prudence:true`) identifiée avec `r.prudence` absent s'affiche « Comestible — prudence » sur la carte, puis « Ajouter comme variété » ouvre la fiche avec la case prudence décochée (P2-1) — le signal visible est réécrit vers la valeur la plus permissive. Fin de journée : rappel d'export honnête, pas de faux pic.

## 5. Scores heuristiques Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 4 | Bascule auto étape 2, toasts guidés, boutons désactivés, focus d'ouverture, compteur live |
| 2 | Correspondance monde réel | 4 | Comparateur de suggestions 13/13 (vérifié 23E, non retouché), vocabulaire du carnet de chasse |
| 3 | Contrôle et liberté | 4 | Garde-fou (voile/poignée/Escape), retours, annulable partout |
| 4 | Cohérence et standards | 4 | ARIA complétés cette passe ; drifts doc résiduels en P3 |
| 5 | Prévention des erreurs | 3 | P2-1 23E vérifié, mais le verdict IA écrase le verdict du guide sur la carte de résultat (P1-1) et la prudence du guide se perd au transfert (P2-1) — deux trous au moment où l'erreur coûte le plus cher |
| 6 | Reconnaissance vs mémorisation | 4 | Noms requêtables sous toutes leurs formes ; normNom requête + données |
| 7 | Flexibilité / efficacité | 4 | IA remplit les 2 étapes, retry + repli modèle, ordre des images persistant |
| 8 | Esthétique minimaliste | 3,5 | Étape 1 à 5 champs, étape 2 ~13 éléments (inchangé) |
| 9 | Aide à la récupération d'erreurs | 4 | messageErreurIA par cause, parserJSONIA tolérant, import versionné ; le toast mort (P3-3) ne retire rien : le repli « ⚠️ Inconnu » est visible dans le select |
| 10 | Aide et documentation | 4 | Les 3 corrections de doc 23E sont vérifiées (filtres selects, Meta 400/.85, ~170 Ko) ; manque la doc du statut « inconnu » (P3-5) |

**Total : 38,5/40 — baisse honnête de 0,5.** Les 6 correctifs de `5d34539` sont vérifiés (2 avec réserve) ; le dock est H5 (3,5 → 3), pour la dette de sécurité révélée cette passe : le guide sait, la carte de résultat ne l'écoute pas.

## 6. Forces spécifiques

1. **Le cœur du fix P2-1 est bien fait : le statut invalide meurt deux fois, pas une.** La coercition `r.statut = 'inconnu'` en amont (l.2426-2427) ET le vocabulaire élargi au transfert (l.2487-2489) doublonnent la protection : aucune valeur exotique de l'IA ne peut atteindre le select, et le select possède désormais la seule option honnête pour l'incertitude (« ⚠️ Inconnu », l.647). Le défaut permissif silencieux de 23E est structurellement impossible.
2. **La checklist est enfin un composant à bascule complet.** `aria-pressed` initial (l.1435) + mise à jour au toggle (l.1487) + compteur `aria-live="polite"` (l.1433) + titre du verdict danger synchronisé sur le compteur (l.1491-1492) : le lecteur d'écran reçoit la même vérité que l'œil sur l'écran le plus critique pour la sécurité.
3. **La discipline des données et du vocabulaire tient dans la durée.** Aucun claim de données cette passe, mais la base, les 21 `guide:true`, les img locales et le SW cqm-v51 sont cohérents avec la passe 23E (aucun changement sur ces axes — rien à re-vérifier, rien n'a bougé).

## 7. Problèmes prioritaires

**P1-1 (NOUVEAU, SÉCURITÉ — pré-existant, révélé par la relecture du flux idphoto) — le verdict de l'IA écrase celui du guide sur la carte de résultat.** `connue` est calculé (l.2433) et utilisé pour la prudence (l.2435) et le bouton « Voir la fiche » (l.2464) — jamais pour confronter le statut. `afficheComestible = fiable && !prudente` (l.2436) et le badge suit `r.statut` (l.2450) : si l'IA identifie une espèce MORTELLE du guide (ex. Amanite phalloïde) comme « comestible » avec confiance ≥ 90 et `prudence:false`, la carte affiche le badge vert « ✅ Comestible » — l'app sait (nom = espèce du guide, statut mortel) et n'oppose rien. C'est l'inverse du principe produit n° 1 au moment où l'utilisateur décide de manger. Le flux cueillette, lui, croise `infoEspece` (l.1583-1586) ; le flux photo ne le fait pas. *Fix :* quand `connue` existe, classer les statuts par gravité (mortel > toxique > immangeable > comestible) et afficher TOUJOURS le verdict du guide en cas de conflit (badge MORTEL + alerte rouge + antipoison) ; utiliser `infoEspece(r.espece)` (normNom + synonymes + tolérance) au lieu du match exact sans normNom (l.2433), et reporter le statut du guide dans `preparerVarieteDepuisResultat`.*

**P2-1 (NOUVEAU, résidu du fix 23E) — la prudence dérivée du guide s'affiche puis disparaît au transfert.** La carte affiche `prudente = connue.prudence || (r.prudence && !connue)` (l.2435) : une morille (guide, `prudence:true`) identifiée avec `r.prudence` absent/`false` porte le badge « Comestible — prudence » + l'alerte orange (l.2457-2458). Le transfert, lui, exécute `$('e-prudence').checked = !!r.prudence` (l.2490) — la case reste décochée, statut « comestible ». Le signal de sécurité visible sur la carte est réécrit vers sa valeur la plus permissive : c'est exactement la mécanique condamnée en 23E, un cran plus loin. *Fix :* transférer la même valeur que l'affichage — `$('e-prudence').checked = !!prudente` (recalculer `connue` dans `preparerVarieteDepuisResultat` via `infoEspece`, ou stocker le booléen affiché sur `r` au moment du rendu).*

**P2-2 (NOUVEAU, intégration filtre) — le statut « inconnu » est invisible dans le filtre de danger.** Le prédicat « ☠️ Ne pas manger » couvre `toxique || immangeable || mortel` (l.1382) mais pas `inconnu`. La variété créée par le fix P2-1 (statut « ⚠️ Inconnu », le plus prudent de tous) n'apparaît sous aucun filtre sauf « Tous les statuts » (et « Prudence » si cochée) — précisément le filtre qu'un utilisateur utilise pour croiser un doute avant de consommer. *Fix :* ajouter `|| e.statut === 'inconnu'` au prédicat `npas` (l.1382).*

**P3-1 (NOUVEAU, A11Y) — `aria-current` n'existe pas au chargement initial.** L'attribut n'est posé que dans `naviguer` (l.1017-1019) ; l'onglet Spots porte `class="actif"` dans le HTML (l.500) sans attribut, et `init()` (l.2727-2740) n'appelle jamais `naviguer`. Au premier rendu, aucun onglet n'est signalé actif au lecteur d'écran. *Fix :* un `naviguer('spots')` à l'init (ou poser l'attribut sur l'onglet par défaut dans le HTML).*

**P3-2 (NOUVEAU, ÉTAT) — le titre du verdict « att » reste figé au premier coche.** `basculerSpec` met à jour le compteur, `aria-pressed` et le titre n/n du verdict danger (l.1491-1492), mais pas le titre du verdict « att » : à 1/5 coché, la carte affiche toujours « Rien n'est encore vérifié » (rendu initial l.1444-1445) pendant que le compteur annonce 1/5 — contradiction visible sur l'écran de sécurité. *Fix :* dans `basculerSpec`, basculer aussi le titre et le sous-texte du verdict-att (« Critères manquants » / « Ne consommez pas tant que tout n'est pas vérifié ») selon `nb === 0`.*

**P3-3 (NOUVEAU, CODE MORT) — le toast « Statut IA hors vocabulaire » ne peut jamais tirer.** La coercition de `analyserPhoto` (l.2426-2427) s'exécute avant tout affichage et garantit que `r.statut` ∈ vocabulaire au moment du transfert ; le `else` de l.2489 est inatteignable (dernierResultatId n'est assigné qu'en l.2421). La protection réelle (select sur « ⚠️ Inconnu ») fonctionne, mais le message d'avertissement promis par le commit n'existe pas en exécution. *Fix :* déplacer le toast vers le point de coercition (l.2427, où l'information existe encore) ou retirer le else et documenter que le select « ⚠️ Inconnu » EST l'avertissement.*

**P3-4 (P3-3 23E — CORRIGÉ PARTIELLEMENT) — les labels ARIA parlent lb, les valeurs numériques restent en kg.** `aria-label` des barres et tiges passe par `fmtKg` (l.2513, 2544 ✓), mais `aria-valuenow`/`aria-valuemax` contiennent toujours les kg bruts (l.2513, inchangés par le diff). En mode lb, un lecteur d'écran peut annoncer « 2,2 sur 5 » puis « Chanterelle : 4,8 lb » — deux nombres pour la même barre. *Fix :* convertir valuenow/max dans l'unité d'affichage (même facteur 2,20462 que `fmtKg` — le pourcentage est invariant) ou poser un `aria-valuetext` = `fmtKg(e[1])`.*

**P3-5 (NOUVEAU, DOC) — DESIGN.md ne documente pas le statut « Inconnu », et décrit un compteur qui n'existe plus.** (a) La nouvelle option « ⚠️ Inconnu » (l.647) et sa pastille `st-inconnu` (l.203, 970) n'apparaissent pas dans la liste des pastilles de statut (DESIGN.md l.192) — le doc liste 5 statuts, le code en gère 6. (b) DESIGN.md l.219 : « Compteur : pastille ambre « n/5 » » — le code exécute une pastille noire sur crème (l.274) ; drift pré-existant jamais signalé. *Fix :* ajouter « gris Inconnu ⚠️ » à la liste des pastilles et corriger la description du compteur.*

## 8. Red flags par persona

- **Jonathan en forêt, une main, sans réseau** : l'identification photo est le moment de vérité — et c'est là que vit le P1-1 : une photo d'amanite phalloïde mal lue par l'IA lui montre un badge vert « ✅ Comestible » (confiance ≥ 90), sans que l'app oppose le verdict de son propre guide. C'est le pire moment de toute l'app : la décision de consommer, hors-ligne, seul. Les pastilles rayures 🍄 hors-ligne et les 21 vignettes locales tiennent toujours.
- **Proche débutant (via export/import)** : la chaîne nom → taxon → fiche tient (13/13 vérifié 23E, non retouché) ; le flux « À vérifier » → « Ajouter comme variété » ouvre désormais sur « ⚠️ Inconnu » — vrai progrès. Mais si l'IA dit « Morille, comestible, 95 % », la carte montre « Comestible — prudence » et la fiche variété s'ouvre avec la prudence décochée (P2-1) : le débutant recopie l'app, et l'app a réécrit son propre avertissement.
- **Utilisateur au clavier / lecteur d'écran** : la checklist expose enfin son état (`aria-pressed` + compteur live), la nav signale l'onglet actif après la première navigation — mais pas au chargement (P3-1), et les barres de stats peuvent annoncer kg et lb pour la même barre (P3-4). Pire moment : ouvrir l'app à froid et n'entendre aucun onglet actif, puis cocher un critère sur une fiche mortelle et voir (entendre) le verdict « att » figé sur « Rien n'est encore vérifié » (P3-2).

## 9. Observations mineures

**Nouveaux :**
- `retirerIllu` (l.2304-2321) réindexe la checklist en données mais ne re-rend jamais la vue détail sous-jacente : au retour de la feuille, compteur et verdict affichent l'ancien décompte jusqu'au prochain rechargement (pré-existant, non signalé).
- PRODUCT.md l.39 décrit les stores IndexedDB comme `especesCustom` et `cachees` ; le code crée `especes` et `caches` (l.792-793) — drift de nommage pré-existant, doc jamais alignée.
- Le toast de pré-remplissage (l.2496) ne mentionne pas le statut transféré : « vérifiez l'identité » sans dire « statut : Inconnu » — le select le montre, le toast pourrait le rappeler (un cran plus explicite pour un statut de sécurité).

**Résidus inchangés (non re-scorés, tous re-confirmés présents en 24E) :** `rendreBandeauCle` insère un `<button>` dans un `<p class="note">` (l.2391-2394, HTML invalide) · `p-cle` sans label (l.460) · `connue` compare sans `normNom` (l.2433 — absorbé par le fix P1-1 proposé) · `choisirNomMyco` ne remplit le latin que si vide (l.1664) · échec silencieux de `chargerBaseMyco` (l.1617 — « 0 espèces » honnête si le fetch échoue) · champ recherche du guide sans label visible (l.411) · focus perdu sur les selects de filtre (re-rendu `rendreFiltres`, l.1362-1363) · `alt="photo"` générique (l.1186) · `ouvrirMyco` sans message hors-ligne (l.2352-2354) · `.mois-col .lab` 10,5 px (l.339) · cache SW non borné pour les GET réussis (sw.js l.162) · `aria-invalid` : 0 partout, validation toast-only · `COULEURS_MOIS` cycle 6×2 sans sémantique de saison (l.2508).

## 10. Questions provocatrices

1. Le guide possède le statut de l'espèce et la carte de résultat le jette : quand l'IA dit « comestible » d'une espèce que le guide marque MORTELLE, qui a le dernier mot — et à quel seuil de confiance l'IA a-t-elle le droit de contredire le guide ?
2. La prudence affichée sur la carte (`connue.prudence || r.prudence`) n'est pas celle transférée (`r.prudence`) : quelle valeur le pré-remplissage doit-il recopier — celle qu'on a montrée à l'utilisateur, ou celle que l'IA a écrite ?
3. Le statut « ⚠️ Inconnu » existe dans le select mais pas dans les filtres : « Ne pas manger » doit-il inclure « pas encore su » — et est-ce qu'une espèce inconnue est plus dangereuse qu'une toxique connue ?
4. Le toast « Statut IA hors vocabulaire » est mort-né : la coercition en amont rend le else inatteignable — faut-il avertir au moment de la coercition (là où l'info existe) ou le select « ⚠️ Inconnu » suffit-il comme avertissement ?
5. `aria-current` n'existe qu'après la première navigation : l'accessibilité de l'état initial doit-elle être posée dans le HTML ou par un `naviguer()` à l'init — et qui teste le rendu à froid ?
6. Le verdict « att » dit « Rien n'est encore vérifié » à 1/5 : le texte du verdict doit-il être un état dérivé recalculé à chaque toggle (comme le n/n), ou un rendu complet de la zone verdict à chaque `basculerSpec` ?
7. Les ARIA des barres annoncent « 2,2 sur 5 » en kg et le label dit « 4,8 lb » : l'accessibilité doit-elle parler une seule unité par barre, ou `aria-valuetext` est-il le bon endroit pour l'unité d'affichage ?
8. DESIGN.md liste 5 pastilles de statut ; le code en gère 6 et décrit un compteur ambre qui est noir depuis des passes : à quelle fréquence la doc doit-elle être ré-auditée contre le code, plutôt que corrigée au fil des critiques ?
9. Le flux photo croise le guide pour la prudence mais pas pour le statut, le flux cueillette croise pour le statut mais seulement sur synonyme : les deux flux doivent-ils partager une seule fonction de croisement guide-vs-IA (ex. `infoEspece`), et pourquoi n'est-ce pas déjà le cas ?

---

**Correctifs de la passe 23E vérifiés (6/6, dont 2 avec réserve) :**
- **P2-1 ✅ corrigé (cœur).** Option « ⚠️ Inconnu » dans le select (l.647) ; transfert limité au vocabulaire élargi avec repli « inconnu » (l.2487-2489) ; `$('e-prudence').checked = !!r.prudence` (l.2490) ; `formulaireEspeceSale` couvre le nouveau statut (l.1782 : toute valeur ≠ comestible rend le formulaire sale). Le défaut permissif silencieux de 23E est structurellement impossible. **Réserve :** la prudence dérivée du guide (affichée l.2435) n'est pas transférée (P2-1 nouveau) ; le toast du else est inatteignable (P3-3).
- **P3-1 ✅ corrigé.** `aria-pressed` au rendu (l.1435) + mise à jour au toggle (l.1487) ; `aria-live="polite"` sur `#spec-compteur` (l.1433), mis à jour l.1489.
- **P3-2 ✅ corrigé.** `aria-current="page"` posé/retiré dans `naviguer` (l.1017-1019), y compris le cas `detail → guide` (l.1017). **Réserve :** absent au chargement initial (P3-1 nouveau).
- **P3-3 ⚠️ corrigé partiellement.** Labels des barres (l.2513) et des tiges (l.2544) passent par `fmtKg` — l'œil et l'oreille partagent l'unité dans le libellé. `aria-valuenow`/`aria-valuemax` restent en kg bruts (P3-4 nouveau).
- **P3-4 ✅ corrigé.** « dans les ' + base.length + ' espèces de la base » (l.1656) — plus de compte en dur.
- **P3-5 ✅ corrigé.** DESIGN.md l.193 (deux `<select>` pleine largeur, « depuis v22 »), DESIGN.md l.162 (Meta 400, 12,5 px, opacité 0,85 + garde « ne pas redescendre sous 0.8 »), PRODUCT.md l.38 (« ~170 Ko » — le fichier pèse 174 063 octets ≈ 170 Ko, cohérent).
- **Verdict ☠️ n/n dynamique ✅ corrigé.** Rendu initial dynamique (l.1442) + mise à jour au toggle (l.1491-1492). **Réserve :** seul le titre du verdict danger se met à jour ; le verdict « att » reste figé (P3-2 nouveau).

**Claims `5d34539` vérifiés** (`git show --stat` : DESIGN.md ±4, PRODUCT.md ±2, index.html +25/−11, sw.js bump — conforme) : cqm-v51 dans sw.js l.4, `FICHIERS` inclut `img/mycoquebec.json` et les deux `credits.json` (l.138-140), aucune régression CSS dans le diff (aucun nouveau `opacity:`, aucun hex hors palette).

**Non corrigés (nouveaux de cette passe) :** P1-1, P2-1, P2-2, P3-1 à P3-5 ci-dessus, et les résidus de la section 9.
