# Audit qualité code & architecture — Cueillette Québec (édition Memphis)

**Date :** 16 août 2026 — **Portée :** analyse statique du JS inline d'`index.html` (~2 090 lignes, script unique démarrant ligne 748) + `sw.js` (166 lignes). **Méthode :** lecture intégrale du code, extraction du JS (`sed` + `node --check` : syntaxe OK), greps ciblés (duplication, rejets, races, XSS), vérifications des données réelles (`img/mycoquebec.json` : 3 938 entrées, 103 noms avec apostrophe).

**Convention de lignes :** le JS inline d'`index.html` commence à la ligne 748 (`<script>`), ligne 749 = 1re ligne de code. Les références `index.html:NNN` désignent les lignes du fichier réel. Les références `sw.js:NNN` sont directes.

**Aucun fichier modifié** — rapport seul.

---

## 1. Constats

### 1.1 Robustesse des données & gestion d'erreurs

**[SÉVÉRITÉ: critique] Import destructif : données actuelles effacées AVANT que l'import ne soit garanti, sans transaction ni restauration**
- **Fichier:ligne :** `index.html:2680-2694` (handler `st-import-fichier`)
- **Impact :** le flux est `vider()` les 7 stores **puis** écritures séquentielles `await` par item. Un échec en cours d'import (quota dépassé — plausible avec des fichiers contenant des photos, l'erreur la plus fréquente en IDB) laisse l'app avec **toutes les données actuelles détruites + un import partiel**. Le `catch` affiche « ⚠️ Fichier invalide — import annulé », un message faux (le fichier était valide ; c'est l'écriture qui a échoué). L'utilisateur ne s'en rend compte qu'au prochain rechargement. C'est le pire scénario possible pour une app dont le produit EST la donnée.
- **Recommandation :** écrire l'import dans **une seule transaction IDB** (`readwrite` sur les 7 stores, `Promise` résolue sur `tx.oncomplete`), ou à défaut : valider + simuler (taille estimée) avant le `vider`, écrire vers des stores temporaires puis basculer, et sur échec **restaurer l'état précédent** (sauvegarde mémoire des données actuelles + réécriture). Message d'erreur honnête et distinct de « fichier invalide ».

**[SÉVÉRITÉ: majeur] Rejets silencieux : aucune gestion d'erreur sur les écritures IndexedDB/localStorage**
- **Fichier:ligne :** `index.html:1367-1384` (sauvegarde spot), `1651-1676` (cueillette), `1895-1922` (variété), `1361-1366`, `1645-1650` (suppressions), `1535-1562` (checklist) ; couche `txn` : `index.html:804-834` (rejet sur `request.onerror`, ligne 828)
- **Impact :** aucun handler de sauvegarde ne fait de `try/catch` autour de `await Stockage.ecrire(...)`. Un échec (quota dépassé par une photo, transaction avortée, JSON corrompu en repli localStorage) produit une **promesse rejetée non gérée** : pas de toast, pas de rollback, l'UI affiche un état qui n'est pas persisté. `basculerSpec` (checklist terrain) et `choix-masquer`/`choix-supprimer` sont aussi concernés. Le message « enregistré ✅ » n'apparaît pas, mais rien n'indique l'échec non plus.
- **Recommandation :** wrapper `sauvegarder(fn)` avec `try/catch` + `toast('⚠️ Enregistrement impossible (stockage plein ?)')` ; tester explicitement le chemin quota (photo ~300 Ko × 100 = risque réel) ; ajouter un handler global `unhandledrejection` qui toast l'erreur en développement.

**[SÉVÉRITÉ: majeur] `recharger()`/`init` sans filet : un seul store corrompu = app blanche, sans message**
- **Fichier:ligne :** `index.html:2793-2822` (`recharger`), `2825-2838` (`init`)
- **Impact :** `Promise.all` des 7 lectures sans `try/catch` ; en repli localStorage, `JSON.parse(localStorage.getItem(...) || '[]')` (ligne 808) jette sur JSON tronqué. Une seule erreur → `init` échoue → **page vide, aucun diagnostic**. Le repli localStorage est censé être la bouée de sauvetage d'IDB, mais il est aussi fragile que la donnée qu'il porte.
- **Recommandation :** `try/catch` dans `recharger()` avec toast d'erreur + rendu dégradé (stores réussis, store fautif ignoré) ; en repli, `JSON.parse` dans un try avec réparation (sauvegarde `.corrompu` + reset du store) ; `window.onerror` de diagnostic.

**[SÉVÉRITÉ: majeur] Validation d'import superficielle : un fichier JSON valide mais mal formé fait crasher les rendus**
- **Fichier:ligne :** `index.html:2664-2669` (seuls `Array.isArray` sont vérifiés), crash au rendu : `b.date.localeCompare(a.date)` `index.html:1571`, `c.espece.toLowerCase()` `index.html:2608`
- **Impact :** une cueillette sans `date` ou sans `espece` (fichier modifié à la main, export d'une future version, copie partielle) → `TypeError` dans `rendreCueillettes` ou `rendreStats` → liste/stats mortes sans message. `fmtDate` (l.757-761) fait du rollover silencieux sur les dates invalides (« 2024-02-30 » → 1er mars).
- **Recommandation :** schéma de validation minimal à l'import (types des champs critiques : `date`/`espece`/`id` string, `poids` number) avec rejet des items invalides + rapport « N items ignorés » ; rendre les rendus défensifs (`String(c.date||'')`).

### 1.2 Sécurité (injection)

**[SÉVÉRITÉ: majeur] Injection HTML/JS via `onclick` inline : `esc()` est insuffisant en contexte « JS dans attribut », et les IDs ne sont jamais échappés**
- **Fichier:ligne :** `esc` : `index.html:751` ; boutons autocomplétion : `index.html:1604` (`choisirEspeceCueillette('…')`), `1723` (`choisirNomMyco('…')`), `1510` (`ouvrirMyco('…')`) ; IDs bruts interpolés : `index.html:1288-1290` (spots), `1588-1589` (cueillettes), `1503-1510` (détail), `2362-2426` (illu) ; `src` de photo non échappé : `index.html:1279`
- **Impact :** double problème. **(a) Bug fonctionnel réel :** `esc()` convertit `'` en `&#39;`, mais le parseur HTML décode l'entité AVANT compilation du handler → une apostrophe dans un nom casse la chaîne JS → `SyntaxError` au clic. **103 noms de `img/mycoquebec.json` contiennent une apostrophe** (« Amanite d'Atkinson », « Bolet d'Amérique »…) : les suggestions d'autocomplétion de ces espèces sont mortes. Idem pour toute variété perso nommée avec une apostrophe (courant en français). **(b) XSS :** un ID ou un nom forgé (`');alert(1);//`) injecté via un fichier d'import (les IDs des spots/cueillettes/variétés importés ne sont jamais validés ni échappés, `rendreSpots`/`rendreCueillettes`/`ouvrirDetail` les collent tels quels dans les attributs) exécute du code arbitraire — y compris la lecture de la clé Gemini stockée en localStorage.
- **Recommandation :** ne plus interpoler de données dans les handlers inline : `data-*` + délégation d'événements (`addEventListener` sur conteneur), ou encodage JSON (`JSON.stringify` + `decodeURIComponent` inverse n'existe pas — utiliser `encodeURIComponent` + décodage, ou attributs `data-`). Échapper systématiquement `id` et `src` (au minimum `esc`, mais cela ne suffit pas en contexte JS-dans-attribut : bannir ce pattern). Valider `id` à l'import (`/^[a-zA-Z0-9_-]+$/`).

### 1.3 Service worker

**[SÉVÉRITÉ: majeur] `install` tout-ou-rien : une seule ressource manquante = aucun service worker**
- **Fichier:ligne :** `sw.js:143-145`
- **Impact :** `c.addAll(FICHIERS)` échoue en bloc si UNE des ~140 ressources (105 photos `img/specs/`…) manque ou renvoie 404 (fichier renommé, déploiement partiel). L'installation échoue silencieusement → l'app reste en ligne uniquement, l'utilisateur en forêt perd l'offline sans aucun signe. Le commentaire « bump cqm-vN » documente la procédure, pas la panne.
- **Recommandation :** `Promise.allSettled`/`addAll` avec `catch` par ressource (log + poursuite), ou vérification `FICHIERS` vs fichiers présents en CI ; au minimum un `install` qui réussit même avec des images manquantes (elles retomberont sur le fallback réseau).

**[SÉVÉRITÉ: majeur] Le fallback réseau sert `index.html` pour TOUTE requête en échec, y compris les images**
- **Fichier:ligne :** `sw.js:159-164`
- **Impact :** une requête d'image distante (miniatures MycoQuébec référencées par `illustrerSpec`, `index.html:2045-2049` — hôte non exclu par la règle wikimedia/googleapis) échoue hors-ligne → le SW répond `index.html` avec un 200 → `<img>` affiche une icône cassée, et tout consommateur non-navigateur reçoit du HTML. C'est aussi un piège de debug : les erreurs réseau réelles sont masquées par un faux 200 HTML.
- **Recommandation :** ne servir le fallback que pour les navigations : `if (e.request.mode === 'navigate') … caches.match('./index.html')`, sinon `Response.error()`/404 ; exclure aussi `mycoquebec.org` du cache réseau (comme wikimedia).

**[SÉVÉRITÉ: majeur] `activate` purge TOUS les caches de l'origine, pas seulement `cqm-*`**
- **Fichier:ligne :** `sw.js:147-151`
- **Impact :** `caches.keys().filter(c => c !== CACHE)` supprime tous les caches de l'origine. Sur GitHub Pages, l'origine `jonathancote1984.github.io` est partagée par toutes les apps/repos du compte : un autre projet PWA déployé sur la même origine perd son cache offline au prochain `activate`. Même mono-app, le filtre devrait être préfixé.
- **Recommandation :** `c.startsWith('cqm-')` dans le filtre (et supprimer en priorité les anciennes versions `cqm-vN`).

### 1.4 Monolithes & duplication

**[SÉVÉRITÉ: majeur] Monolithes de rendu + duplication des blocs d'alerte sécurité**
- **Fichier:ligne :** `ouvrirDetail` : `index.html:1464-1529` (~66 lignes de gabarit HTML en concaténation, logique sécurité + migration illustrations + écriture IDB mélangées) ; `analyserPhoto` : `index.html:2478-2566` (~89 lignes, 6 gabarits de sortie)
- **Impact :** les blocs d'alerte MORTEL / toxique / prudence (avec le numéro du centre antipoison **1-800-463-5060**) sont dupliqués mot pour mot 2× (détail guide + résultat IA), et les verdicts de checklist 4× dans `ouvrirDetail` seul. C'est du contenu de **sécurité critique** : toute divergence future (numéro, formulation) ou erreur de branche est indétectable par compilation et double le risque d'un mauvais affichage (ex. badge comestible sur une espèce mortelle). `analyserPhoto` mélange en plus parsing, croisement guide/IA, calculs de confiance et 6 gabarits HTML.
- **Recommandation :** extraire `alerteStatut(statut, prudence)` (une seule source pour MORTEL/toxique/prudence + antipoison) et `gabaritVerdict(…)` ; découper `analyserPhoto` en `calculerVerdictIA(r, connue)` (pur, testable) puis `rendreResultatIA(r, verdict)` ; `ouvrirDetail` en `ouvrirDetail` (état) + `rendreDetail(e, perso)` (gabarit). Les gabarits en `String.raw`/fonctions dédiées remplacent la concaténation géante.

**[SÉVÉRITÉ: mineur] Duplication quasi totale de `infoEspece` et `infoEspeceArchive`**
- **Fichier:ligne :** `index.html:987-1009` et `1013-1034` (~48 lignes, mêmes 3 passes exacte/floue/inclusion sur deux bases)
- **Impact :** toute correction du matching (seuils Levenshtein, synonymes) doit être faite deux fois ; risque de divergence silencieuse — or c'est du code de **sécurité** (badge de statut sur les cueillettes). `toutesEspeces()`/`BASE_COMPLETE()` sont reconstruites 3× par appel (`index.html:974-977`).
- **Recommandation :** factoriser `matcherEspece(nom, base)` et appeler `infoEspece` = `matcherEspece(nom, toutesEspeces())` ; ajouter un test de parité (les deux fonctions doivent retourner le même statut pour un même nom).

**[SÉVÉRITÉ: mineur] Duplication `chercherPhotoCommons` / `chercherPhotoSpec`**
- **Fichier:ligne :** `index.html:1990-2002` et `2027-2039` (URLs d'API et filtres ~85 % identiques)
- **Impact :** modifications divergentes probables (filtres de filtrage, limite) ; ~25 lignes dupliquées.
- **Recommandation :** `chercherCommons(terme, { limit, largeur, filtreMime, motsExclus })` unique.

**[SÉVÉRITÉ: mineur] Duplications courtes répétées (conventions d'édition)**
- **Fichier:ligne :** labels d'unités ×3 : `index.html:2717-2720`, `2726-2729`, `2831-2834` ; purge des 7 stores ×2 : `index.html:2680` et `2705-2706` ; initialisation des champs de feuille (spot/cueillette/variété) ~15 lignes quasi identiques `index.html:1322-1329`, `1617-1625`, `1829-1849`
- **Impact :** chaque correctif (ex. oubli d'un store dans la purge) doit être répliqué ; un store ajouté à la v7 devra être ajouté à 4 endroits (création, lecture, purge, export).
- **Recommandation :** `NOMS_STORES` constant + `viderTout()` / `sauvegarderTout(data)` ; helper `remplirFeuille(mapChamps)` ; helper `appliquerLabelsUnite()`.

### 1.5 Async / races

**[SÉVÉRITÉ: mineur] Race `analyseAbort` partagé : l'échec d'une ancienne analyse peut écraser l'UI d'une analyse en cours**
- **Fichier:ligne :** `index.html:2478-2489`, `2560-2565` (le `catch` teste `analyseAbort.signal.aborted` sur le contrôleur COURANT, pas celui de la requête qui a échoué)
- **Impact :** scénario : analyse A → Annuler → nouvelle analyse B démarre (nouveau contrôleur) → le rejet de A arrive → `analyseAbort.signal.aborted` est celui de B (non avorté) → le `catch` rend l'UI d'erreur par-dessus « Analyse en cours… » de B. Transitoire (B re-rend à la fin) mais déroutant, et l'erreur de A peut aussi déclencher un toast parasite.
- **Recommandation :** capturer le signal localement (`const signal = analyseAbort.signal` en début de fonction) et tester `signal.aborted` ; ou vérifier l'identité `analyseAbort === monControleur`.

**[SÉVÉRITÉ: mineur] `analyseAbort` jamais remis à `null` : fermer la feuille après une analyse terminée affiche « Analyse annulée »**
- **Fichier:ligne :** `index.html:2456-2464` (`annulerAnalyse`), garde-fou de fermeture : `index.html:1093`
- **Impact :** `analyseAbort` reste non-null après succès ; `fermerFeuilleAvecGardeFou` (feuille idphoto ouverte + `analyseAbort` truthy) appelle `annulerAnalyse()` qui remplace le résultat affiché par « ✋ Analyse annulée » (avant fermeture). Si l'utilisateur rouvre la feuille, il voit « annulée » pour une analyse réussie.
- **Recommandation :** `try/finally { analyseAbort = null; }` autour de l'analyse ; `annulerAnalyse` ne devrait remplacer le contenu que si une analyse est réellement en cours.

**[SÉVÉRITÉ: mineur] `imageEnBase64` : `FileReader` sans `onerror` → promesse qui ne rejette jamais**
- **Fichier:ligne :** `index.html:2003-2011`
- **Impact :** si la lecture du blob échoue (rare, mais possible sur fichier distant), la promesse reste pendante → `illustrerSpec`/`genererIllu`/`illu-toutes` restent bloqués sur « ⏳ En cours… » indéfiniment (bouton désactivé, pas d'annulation possible). Les `try/catch` des appelants sont impuissants.
- **Recommandation :** ajouter `rd.onerror = () => ko(new Error('lecture'))` + timeout ; idem pour `FileReader` dans `ouvrirChoixPhoto` (`index.html:1262-1266`).

**[SÉVÉRITÉ: mineur] `Stockage.ouvrir` : `onblocked` non géré, promesse sans chemin d'échec**
- **Fichier:ligne :** `index.html:785-803`
- **Impact :** si un autre onglet tient une ancienne version de la base, l'upgrade (v5) est bloqué → `onblocked` (jamais `onerror`) → `ok()` jamais appelé → `init` **fige l'app pour toujours**, sans message. La promesse ne rejette jamais (pattern « jamais de ko ») ce qui interdit tout diagnostic.
- **Recommandation :** gérer `rq.onblocked` (message « fermez l'autre onglet »), `rq.onupgradeneeded` avec versionning explicite, et permettre à `ouvrir()` de rejeter ; re-tenter l'ouverture après un délai.

**[SÉVÉRITÉ: mineur] Écritures « fire-and-forget » sur `illustrations`**
- **Fichier:ligne :** `index.html:1481` (`ouvrirDetail`), `1892` (`transfererCaracVersItems`), `2314` et `2329` (`ouvrirSheetIllu`) — `Stockage.ecrire` sans `await` ni `catch`
- **Impact :** un échec (quota) est totalement invisible : la fiche semble enrichie mais la donnée est perdue au rechargement suivant.
- **Recommandation :** `await` + `catch` (ou `void …catch(() => {})` au minimum), et regrouper dans la sauvegarde de fiche existante.

### 1.6 Fuites mémoire & DOM

**[SÉVÉRITÉ: mineur] `ouvrirChoixPhoto` : input caché fantôme si le sélecteur est annulé**
- **Fichier:ligne :** `index.html:1252-1269`
- **Impact :** `onchange` ne se déclenche pas si l'utilisateur annule la boîte de dialogue → `nettoyer()` jamais appelé → un `<input type=file>` invisible s'accumule dans le DOM à chaque annulation. Mineur (quelques nœuds), symptomatique d'un nettoyage non garanti.
- **Recommandation :** nettoyer dans `inp.oncancel` (API récente) ou via `setTimeout` après `click()` ; ou réutiliser un input unique caché permanent.

**[SÉVÉRITÉ: mineur] Lightbox : pas de focus trap, scroll non verrouillé, listener global non nettoyé en cas de double fermeture**
- **Fichier:ligne :** `index.html:2432-2452`
- **Impact :** Tab peut sortir de la lightbox (a11y) ; le fond défile sous l'overlay ; si deux lightboxes s'empilent (possible par clavier), les listeners `keydown` de la première ne sont retirés qu'à sa fermeture (ok) mais l'ordre de fermeture n'est pas garanti. Le reste des listeners de la page (2 × `keydown` globaux) n'est pas retiré — pas de fuite réelle, mais la gestion est fragile.
- **Recommandation :** verrouiller le scroll (`body.style.overflow='hidden'` au `finally`), piéger le focus dans la lightbox, et n'ajouter qu'UN listener global unique (délégation) plutôt qu'un par ouverture.

**[SÉVÉRITÉ: mineur] Aucun garde de fermeture d'onglet : données saisies perdues sans avertissement**
- **Fichier:ligne :** `index.html:1075-1099` (garde-fous des feuilles, mais rien au niveau page)
- **Impact :** une feuille sale + fermeture d'onglet/du navigateur = perte silencieuse (mobile : swipe pour fermer, retour système). Les garde-fous existants ne couvrent que voile/Échap.
- **Recommandation :** `beforeunload` (et `visibilitychange` pour Android) quand `feuilleSaisieSale() || formulaireEspeceSale()`.

### 1.7 Edge cases & conventions

**[SÉVÉRITÉ: mineur] `reinitialiserFiltres` ne re-rend pas les `<select>` de filtre → état affiché ≠ contenu**
- **Fichier:ligne :** `index.html:1425-1431`
- **Impact :** après un clic sur « ↩️ Réinitialiser les filtres », la liste montre tout mais les selects affichent encore « Mortels » / « Automne » (ils ne sont re-rendus que par `rendreFiltres`, jamais appelé ici). Incohérence visuelle déroutante.
- **Recommandation :** appeler `rendreFiltres()` (ou mettre à jour les deux selects) dans `reinitialiserFiltres`.

**[SÉVÉRITÉ: mineur] Edge cases numériques : poids et dates**
- **Fichier:ligne :** `kgDepuisSaisie` `index.html:768-772` ; `fmtDate` `index.html:757-761` ; `c-poids` `index.html:581` (`type=number step=0.1`)
- **Impact :** (a) « 1 500 » (séparateur de milliers français) → `parseFloat` = `1` ; « abc » → 0 silencieux (pas d'avertissement) ; (b) `type=number` + `step=0.1` : la virgule française est acceptée sur la plupart des mobiles mais le step invalide `0.25` (état `:invalid` incohérent selon les navigateurs) ; (c) dates importées non paddées (« 2024-1-5 ») → `<input type=date>` vide, `fmtDate` rollover silencieux.
- **Recommandation :** parser explicitement (regex nombre), toaster sur saisie non numérique, `step="0.01"` + `inputmode="decimal"` en `type=text`, normaliser `YYYY-MM-DD` à l'import et valider avec `Date.parse` + comparaison ronde.

**[SÉVÉRITÉ: mineur] `compresser` : pas de `onerror`, orientation EXIF ignorée**
- **Fichier:ligne :** `index.html:1222-1233`
- **Impact :** (a) image illisible → `onload` ne se déclenche jamais → le callback `cb` n'est jamais appelé → l'utilisateur touche « Appareil photo », rien ne se passe, aucun retour ; (b) les photos iPhone (EXIF orientation) sont souvent **tournées de 90°** après passage au canvas (drawImage ignore EXIF).
- **Recommandation :** `img.onerror = () => cb(dataUrl)` (repli sans compression) ; utiliser `createImageBitmap(file, { imageOrientation: 'from-image' })` (ou corriger via EXIF) ; `cv.getContext('2d')` peut renvoyer `null` — tester.

**[SÉVÉRITÉ: mineur] Repli localStorage : quota 5 Mo atteint très vite avec photos, aucune stratégie**
- **Fichier:ligne :** `index.html:804-819`
- **Impact :** en mode repli (IDB indisponible), chaque photo (~200-400 Ko base64) consomme le quota localStorage ; quelques dizaines de photos → `QuotaExceededError` → les `put` suivants (même sans photo) échouent en chaîne, y compris de simples spots. La bouée de sauvetage devient une source de perte.
- **Recommandation :** en repli, limiter/compresser plus fort les photos (ex. 600 px, qualité 0.5), afficher un compteur de taille et un avertissement, et tenter de ré-ouvrir IDB périodiquement.

**[SÉVÉRITÉ: mineur] `confirmer()` : `resolveConfirm` global unique — deux confirmations simultanées = première promesse pendante**
- **Fichier:ligne :** `index.html:1115-1125`
- **Impact :** si deux `confirmer()` s'enchaînent avant réponse (double-tap sur « Supprimer » → `supprimerSpot` + `choix-supprimer`…), le second écrase `resolveConfirm` : le premier appelant reste bloqué sur un `await` qui ne résoudra jamais (perte de la réponse, comportement indéfini à la reprise). Les doubles confirmations de suppression (l.1211-1212) sont exactement ce scénario si l'utilisateur double-clique.
- **Recommandation :** file d'attente de confirmations (promise chaînée) ou résolution de l'ancienne avec `false` à l'ouverture d'une nouvelle.

**[SÉVÉRITÉ: mineur] Perf : `recharger()` relit 7 stores et re-rend tout après CHAQUE mutation**
- **Fichier:ligne :** `index.html:2793-2822` (appelé après chaque save/delete/import), `974-977` (`toutesEspeces()` reconstruit les tableaux 3× par `infoEspece`)
- **Impact :** avec ~100 cueillettes + photos (~30-50 Mo en mémoire), chaque « enregistré ✅ » re-parse tout : à-coups UI et pics mémoire sur mobile. C'est un choix délibéré de simplicité (correct pour le volume actuel), mais le coût est déjà ressenti à la génération IA (écritures + re-rend).
- **Recommandation :** à volume constant, au minimum ne re-rendre que la vue active et ne relire que les stores touchés ; à plus long terme, cache en mémoire des photos (`new Image()` + `createImageBitmap`).

**[SÉVÉRITÉ: mineur] Conventions hétérogènes**
- **Fichier:ligne :** `index.html:1683` (`photoEspece` globale pour l'édition variété vs `Etat.spot.photo`/`Etat.cueillette.photo`), store `caches` vs `Etat.cachees` (`index.html:794`, `962`), `Etat.detailId` jamais remis à `null` dans `fermerDetail` (`index.html:1531-1533`), commentaires « P1-1 (24e)… » nombreux et précieux mais datés (sans référence croisée)
- **Impact :** l'état d'édition vit à trois endroits différents (globales `photoEspece`/`editEspeceId`/`illuEspeceId` + `Etat.spot`/`Etat.cueillette`) ; `detailId` fantôme après fermeture (inoffensif aujourd'hui, piège pour `basculerSpec`). Le monolithe a déjà un « journal de bord » interne : c'est le signe que les invariants métier devraient être documentés au même endroit (une section « invariants » en tête de fichier).
- **Recommandation :** uniformiser l'état d'édition (`Etat.edition = { type, id, photo }`), remettre `detailId` à null, et consolider les commentaires P1/P2/P3 dans un CHANGELOG en tête de script (ils sont historiquement riches).

**[SÉVÉRITÉ: mineur] `uid()` non validé, collision théorique**
- **Fichier:ligne :** `index.html:752`
- **Impact :** `Date.now().toString(36) + 5 caractères aléatoires` : collision possible (2 créations même milliseconde, ~1/60 M) ; surtout, les IDs importés ne passent par aucun filtre (voir 1.2) alors qu'ils alimentent les attributs `onclick` et les clés IDB.
- **Recommandation :** ajouter un compteur (ex. `Date.now().toString(36) + compteur++`) et valider `id` à l'import.

---

## 2. Résumé chiffré

| Métrique | Valeur |
|---|---|
| **Constats totaux** | **27** (1 critique · 8 majeurs · 18 mineurs) |
| JS analysé | 2 090 lignes inline (`index.html:748-2837`) + `sw.js` 166 lignes |
| Syntaxe (`node --check`) | OK (JS inline et sw.js) |
| Code mort détecté | Aucune fonction inutilisée ; 1 état fantôme (`Etat.detailId`) ; quasiment pas de branches inatteignables |
| Écritures sans gestion d'erreur | ~20 appels `Stockage.*` sans try/catch (dont 4 fire-and-forget) |
| Rejets silencieux possibles | Toutes les sauvegardes (spot, cueillette, variété, checklist, masquage, suppression) |
| Duplication identifiée | ~150-200 lignes : `infoEspece`/`infoEspeceArchive` (~48), `chercherPhoto*` (~25), labels unités (~12), purge stores (~10), blocs d'alerte sécurité (4×), gabarits verdict (4×) |
| Monolithes | `analyserPhoto` (~89 lignes), `ouvrirDetail` (~66 lignes) |
| Points d'injection HTML | 34 `onclick=` interpolés, dont ~10 avec données non échappables par `esc()` (IDs, noms) |
| Nombre d'apostrophes réelles cassant l'autocomplétion | **103/3 938** noms dans `img/mycoquebec.json` |

**Points positifs notables :** fail-safe sécurité métier excellent (le guide a le dernier mot sur l'IA — `GRAV`, `index.html:2509-2512` ; vocabulaire coercé ; badge « À vérifier » par défaut) ; pas de code mort ; syntaxe propre ; gestion des fenêtres modales/voile cohérente (z-index vérifiés) ; garde-fous de saisie bien pensés (feuilles, double confirmation) ; `seqRecharger` règle la race de rechargement ; retry+fallback de modèle Gemini robuste (`index.html:1775-1787`).

---

## 3. Top 5 des actions recommandées

1. **Sécuriser l'import JSON** (critique) : écriture transactionnelle ou avec restauration, validation de schéma des items, message d'erreur honnête. C'est le seul chemin de perte de données totale de l'app. *(C1 + M4)*
2. **Gestion d'erreurs des écritures** (majeur) : wrapper try/catch + toast sur tous les `Stockage.ecrire/effacer`, handler global `unhandledrejection`, filet dans `recharger()`/`init` (app jamais blanche). *(M1 + M3)*
3. **Bannir l'interpolation de données dans les `onclick`** (majeur) : `data-*` + délégation d'événements, échappement systématique des IDs, validation des IDs à l'import. Corrige à la fois le bug des 103 noms à apostrophe et le vecteur XSS. *(M2)*
4. **Durcir le service worker** (majeur) : install résiliente (une ressource manquante ne doit pas tuer l'offline), fallback réservé aux navigations, purge préfixée `cqm-`. *(M5 + M6 + M7)*
5. **Refactorer les monolithes de rendu** (majeur) : extraire `alerteStatut()` (source unique MORTEL/toxique/prudence + antipoison), `gabaritVerdict()`, et découper `analyserPhoto` en calcul pur + rendu. Premier pas vers la sortie du monolithe sans changer l'architecture mono-fichier (le découpage peut rester dans le même `<script>`). *(M8 + m1/m2)*
