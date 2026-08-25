# Assessment A — Critique design (21e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2714 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v48) · **Base :** `img/mycoquebec.json` (3938 entrées, 3396 avec `nomFr`, 0 doublon de latin)
**Méthode :** lecture statique seule (Assessment A, aucun navigateur, aucun détecteur). Vérification des 2 findings de la passe 20E (P2-1, P3-1) et des claims des 3 commits de la passe (`b1aa81d`, `f076f6c`, `326f57c`) dans le code ET sur les données : base JSON interrogée en Python par identité (latin), comparateur de suggestions (l.1611-1631) répliqué pour les 21 noms exacts de fiches + 36 requêtes à haut risque, existence des fichiers vérifiée sur disque, liste `FICHIERS` du SW lue ligne à ligne, `git diff` pour le garde-fou « inchangé », contrastes WCAG exacts pour les nouveaux éléments.
**Note globale :** les 2 findings de 20E sont **entièrement corrigés** — le P2-1 est tenu par identité sur les deux axes : libellés (21/21 `nomFr` = nom exact de la fiche) et hors-ligne (21/21 vignettes locales, disque + SW). La nouvelle feuille variété en 2 étapes est une vraie amélioration de densité, mais le commit surestime : l'échec de charge cognitive « choix minimaux ≤ 4 » est **réduit, pas levé** (5 champs sur l'étape 1). Score 39,5/40 : H6 retrouve son 4 (pénalité synonymes levée, vérifiée par réplication), H8 monte à 3,5 — nouveau record, honnête.

---

## 1. Verdict de spécificité design : 9/10 (inchangé)

La grammaire Memphis tient du header aux nouvelles pilules d'étapes, pour la 21e passe consécutive : 0 couleur hors palette documentée, 0 box-shadow flouté (grep `blur(` : 0 résultat), 0 uppercase, 0 boîte système (confirm/alert natifs absents). Le nouveau composant `.etape` (l.290-302) respecte les quatre règles nommées : trait noir 2,5-3 px, ombre dure sans flou, inclinaison -1,5° de la pilule active, coins cassés hérités de la grammaire. Les pilules numérotées (pastille numéro noir sur crème, active = jaune + numéro rouge) sont du Memphis pur — le « 1 → 2 » aurait pu être un stepper générique, il est un élément du carnet.

**Axes :** conceptuel ~90 % (carnet de chasse, vocabulaire mycologique québécois, antipoison, cueillettes/spots, étapes « Identité » / « Détails & photo ») · visuel ~90 % (une capture sans texte révèle Memphis-automne-champignon). Verdict : spécifique sur les deux axes, toujours rare.

## 2. Évaluation holistique

- **Hiérarchie visuelle** — tenue : h2 en pastille inclinée, header sticky avec badge, sous-titre suit l'entité ouverte (l.1459-1460). Les pilules d'étapes créent un fil d'Ariane de 2 niveaux, discret et utile.
- **Architecture de l'information** — le découpage en 2 étapes organise la feuille variété en deux blocs sémantiques propres (identité vs détails/photo). Résidu : l'encart d'aide IA en tête d'étape 1 (l.623) porte le vocabulaire visuel d'une alerte de prudence (P3-4).
- **Adéquation émotionnelle** — le creux de 20E (synonyme appris ininterrogeable) est refermé : « fausse morille » et « ange destructeur » servent la bonne espèce, vignette locale, position 1. Nouvelle vallée : l'IA remplit l'étape 2 pendant que l'utilisateur regarde l'étape 1 (P2-1).
- **Découvrabilité** — tout est visible, rien au hover. La barre d'étapes rend l'étendue du formulaire visible dès l'ouverture (2 étapes annoncées, pas de surprise).
- **Composition** — colonne unique 640 px, feuille 84 vh conservées. Étape 1 compacte (≈ 1 écran), étape 2 plus longue mais scrollable.
- **Typographie** — Fredoka 400-700, hiérarchie tenue ; `.etape` en 13 px / 700, numéros en 11,5 px sur pastille noire — contrastes vérifiés (voir Couleur).
- **Couleur** — 0 dérive. Nouveaux contrastes exacts : numéro rouge `#B3261E` sur blanc `#FDF6E7` = **6,07:1** (AA à 11,5 px) ; texte noir `#241A0F` sur pilule active jaune `#D9A441` = **7,59:1** ; texte de l'encart d'étape 1 sur `#F4E3C3` = **13,52:1**. La Règle du Rouge Mortel tient : le rouge des numéros actifs n'est pas un rouge de danger (c'est la pastille numéro), mais voir P3-4 pour l'orange.
- **Accessibilité** — aria-labels, focus-trap modales, Escape hiérarchisé (modale avant feuille, l.1081-1106), `prefers-reduced-motion` (l.354-356). Nouveau : la barre d'étapes est un tablist ARIA partiel (P3-2), et le focus tombe au body aux changements d'étape (P3-3).
- **États** — bouton ✨ Détails IA désactivé pendant l'appel (l.1864, l.1880), validation du nom avant l'étape 2 (l.1711-1714), états vides partout. Le garde-fou `formulaireEspeceSale` couvre les 10 champs des deux étapes (l.1751-1755) — vérifié byte-identique au pré-commit par `git diff`.
- **Copy** — toasts à valence alignée sur leur branche. Nouveau point de friction : « Fiche générée ✨ — vérifiez puis enregistrez » (l.1876) invite à vérifier un contenu qui est sur l'étape invisible (P2-1).
- **Cas limites** — dates locales (`aujourdhui()`), version d'import vérifiée, checklist réindexée, orphelins de `caches` nettoyés (l.2677-2681). La génération IA ne relance pas une requête image interrompue (l.1689) — choix défendable.

## 3. Évaluation de charge cognitive : 1 échec / 8 (réduit, pas levé)

1. Focus unique ✅ · 2. Chunking ≤ 4 ✅ · 3. Regroupement visuel ✅ (identité / détails-photo) · 4. Hiérarchie ✅ · 5. Une chose à la fois ✅ (le découpage SERT cet item) · 6. Choix minimaux ≤ 4 ❌ — **étape 1 = 5 champs** (nom, latin, comestibilité, saison, prudence) + 2 boutons + 1 encart ; étape 2 = 4 champs + 1 zone photo + 8 boutons (l.622-688). La barre ≤4 est toujours dépassée sur l'étape 1. · 7. Mémoire de travail ✅ · 8. Divulgation progressive ✅ (amélioré par le split).

**1 échec franc sur 8 — mais le claim du commit `326f57c` (« lève l'échec de charge cognitive ») est partiellement tenu.** Ce qui est vrai : les 8 champs d'un seul écran sont devenus 5 + 4, un vrai gain. Ce qui ne l'est pas : l'item 6 échoue encore sur l'étape 1 (5 > 4), et l'étape 2 concentre 13 éléments d'attention (4 champs + zone photo + 8 boutons) — autant que l'ancien formulaire unique (8 champs + 4 boutons + 1 alerte = 13). Le problème a été redistribué, pas résolu.

## 4. Voyage émotionnel

Ouverture chaleureuse inchangée (header dégradé, formes flottantes, zigzag) → guide → fiche hybride. **Le creux 20E est refermé au pire moment du parcours :** en forêt, sans réseau, le doute sur Gyromitre ou Amanite vireuse tape « fausse morille » / « ange destructeur » et reçoit la bonne espèce en position 1 avec une vignette locale — la décision visuelle fonctionne dans le mode d'emploi promis, vérifié par réplication du comparateur. **Nouveau pic de cette passe :** la création d'une variété est devenue un vrai parcours en 2 temps — pilules numérotées, « Suivant : détails & photo → » — le formulaire se lit comme une recette plutôt qu'une corvée. **Nouvelle vallée :** l'utilisateur clique ✨ Détails par IA (10-20 s d'attente), le toast dit « vérifiez puis enregistrez », mais habitat/description/caractéristiques/confusions ont été remplis sur l'étape 2, invisible depuis l'étape 1 — le toast invite à vérifier ce qu'on ne voit pas (P2-1). Même mécanique après « ➕ Ajouter comme variété » depuis l'identification photo : la photo pré-remplie vit sur l'étape 2 (l.2466).

## 5. Scores heuristiques Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 4 | Indicateur d'étapes actif, toasts, bouton IA désactivé pendant l'appel, validation nom avec focus retour |
| 2 | Correspondance monde réel | 4 | Réplication : les 21 noms exacts des fiches servent le bon taxon du guide en position 1, vignette locale — 0/21 échec |
| 3 | Contrôle et liberté | 4 | Retour entre étapes, garde-fou intact sur 4 gestes, annulable partout, ordre des images tenu |
| 4 | Cohérence et standards | 4 | Grammaire Memphis tenue sur les pilules ; P3-4 (encart IA en alerte-orange) noté sans dock |
| 5 | Prévention des erreurs | 4 | **Nouveau :** validation du nom AVANT l'étape 2 (l.1711-1714) — l'erreur « formulaire incomplet à l'étape finale » est impossible |
| 6 | Reconnaissance vs mémorisation | 4 | **Pénalité 20E levée, par identité :** les synonymes appris par les fiches (« fausse morille », « ange destructeur ») sont requêtables ; amerivirosa renommée, l'égalité exacte ne bat plus l'espèce MORTELLE du guide |
| 7 | Flexibilité / efficacité | 4 | ✨ Détails IA en tête d'étape 1 (remplit les deux étapes), retry IA + repli modèle, ordre des images persistant |
| 8 | Esthétique minimaliste | 3,5 | Le split réduit la densité de champs (8→5 visibles), mais l'étape 2 garde 13 éléments d'attention et l'étape 1 dépasse la barre ≤4 |
| 9 | Aide à la récupération d'erreurs | 4 | messageErreurIA par cause, parserJSONIA tolérant (fences, extraction {…}), série interrompue avec état restauré |
| 10 | Aide et documentation | 4 | Encart d'onboarding en tête d'étape 1 (l.623), carte « Comment identifier », crédits Commons |

**Total : 39,5/40 — nouveau record, honnête.** Les deux pénalités 20E (H6 synonymes, H8 densité) sont levées ou réduites sur des preuves d'identité, pas sur des déclarations. Profil : sécurité, état du système, prévention des erreurs excellents ; le seul frottement restant est le formulaire variété — mieux découpé, mais l'étape 2 reste un plateau dense.

## 6. Forces spécifiques

1. **Le P2-1 20E est tenu sur les DEUX axes, vérifié par identité.** Les 21 entrées `guide:true` portent exactement le `nomFr` de leur fiche (0 divergence sur 21, comparé par latin), 0 faux positif/négatif sur le flag, 0 img distante, 21/21 fichiers sur disque, 21/21 dans `FICHIERS` du SW. Réplication du comparateur réel (l.1611-1631, score exact/préfixe/guide, tie-break guide puis longueur) : « fausse morille » → `Gyromitra esculenta` pos 1, « ange destructeur » → `Amanita virosa` pos 1, « amanite vireuse » → virosa (l'égalité exacte d'amerivirosa, renommée « Amanite vireuse américaine », ne bat plus l'espèce MORTELLE), et **les 21 noms exacts des fiches servent le bon taxon en position 1 (0/21 échec)**. La chaîne « ce qu'on apprend → ce qu'on peut taper » est enfin cohérente.
2. **Le découpage en 2 étapes est fait dans la grammaire du projet.** Les pilules numérotées (`.etape`, l.290-302) portent l'inclinaison, le trait noir et l'ombre dure — un stepper qui aurait pu être générique est un élément Memphis. Et le garde-fou `formulaireEspeceSale` (l.1751-1755) couvre les 10 champs des deux étapes sans modification (byte-identique, vérifié par `git diff`) : le refactor n'a pas ouvert de trou dans la protection anti-perte.
3. **La résilience IA protège la promesse émotionnelle.** « Détails IA » était en échec systématique (503 backend saturé) ; la passe retire `responseMimeType` (seul le commentaire l.1665 le mentionne — grep confirmé), parse par `parserJSONIA` (fences + extraction du premier `{…}`, l.1700-1707) et retente 1,5 s sur 429/500/503 avec repli `gemini-flash-lite-latest` (l.1685-1697). Le bouton ✨ tient sa promesse en conditions réelles, testé par le commit — c'est de l'ingénierie au service du voyage, pas un pansement d'UI.

## 7. Problèmes prioritaires

**P2-1 (NOUVEAU) — l'IA remplit l'étape 2 pendant que l'utilisateur regarde l'étape 1, et le toast invite à vérifier l'invisible.** `e-generer` (l.1858-1881) remplit `e-habitat`, `e-desc`, `e-carac`, `e-confusions` (l.1872-1875) — tous sur l'étape 2, masquée (`display:none`, l.653) — puis toaste « Fiche générée ✨ — vérifiez puis enregistrez » (l.1876) sans avancer à l'étape 2 ni la mentionner. Idem `preparerVarieteDepuisResultat` (l.2454-2468) : photo + description + caractéristiques pré-remplies sur l'étape 2, utilisateur laissé sur l'étape 1. L'utilisateur en confiance (le toast dit que c'est prêt) ne peut pas voir ce qu'on lui demande de vérifier ; s'il enregistre directement, il valide un contenu IA jamais relu. Pour une fiche de champignon, c'est un angle mort de sécurité. *Fix (une ligne) :* `etapeEspece(2)` après `e-generer` réussi et à la fin de `preparerVarieteDepuisResultat` — ou, à défaut, toast « Détails remplis — étape 2 → » avec le bouton Suivant mis en évidence.*

**P3-2 (NOUVEAU) — barre d'étapes : tablist ARIA partiel.** Les pilules sont `role="tab"` avec `aria-selected` synchronisé (l.616-620, l.1718-1721), mais sans `role="tabpanel"` ni `aria-controls` sur les panneaux (l.622, l.653), sans navigation fléchée ←/→ (patron ARIA tabs), sans gestion de `tabindex=-1`. Un lecteur d'écran entend « onglet 1, onglet 2 » sans savoir que le panneau a changé. *Fix :* `role="tabpanel"` + `aria-labelledby` sur `#etape-1`/`#etape-2`, `tabindex` roving sur les deux onglets, flèches gauche/droite dans le keydown.*

**P3-3 (NOUVEAU) — le focus tombe au body à chaque changement d'étape.** `etapeEspece()` masque le conteneur courant (`display:none`, l.1716-1717) : le bouton qui vient d'être cliqué disparaît du DOM visible et le focus est perdu. Au clavier, après « Suivant », l'utilisateur doit re-Tab depuis le début de la page (le bouton suivant de l'ordre de tabulation est la barre de navigation). *Fix :* après le basculement, `$('e-habitat').focus()` (étape 2) / `$('e-nom').focus()` (étape 1), ou `requestAnimationFrame` pour laisser le rendu s'installer.*

**P3-4 (NOUVEAU) — l'encart d'aide IA réutilise l'alerte-orange documentée « Prudence ».** l.623 utilise `.alerte.alerte-orange` — que DESIGN.md définit comme le signal de prudence (« Prudence : fond crème doré #F4E3C3 », utilisée pour « Ne pas consommer » et « Prudence requise » sur les fiches et l'identification photo). L'encart « ✨ Entrez le nom, puis Détails par IA… » est un onboarding, pas un avertissement : le vocabulaire visuel de la prudence sert un contenu promotionnel. Dilution sémantique douce mais réelle, dans une app où l'orange signale le danger de consommation. *Fix :* un style d'aide dédié (fond blanc + icône ✨, sans le losange décoratif d'alerte) ou documenter explicitement l'usage dans DESIGN.md.*

**P3-5 (DONNÉES, NOUVEAU) — les variantes espacées des noms composés échappent encore.** Réplication : « pied de mouton » (espaces) → `Hydnum subtilior` (« Hydne élancé (Pied de mouton) », non-guide, **img distante** → vignette cassée hors-ligne) ; « tue mouches » → **0 suggestion**. Les noms appris par la fiche (« Pied-de-mouton (hydne ombiliqué) », « Amanite tue-mouches ») fonctionnent 21/21 — c'est la saisie naturelle au clavier mobile (espaces au lieu de traits d'union) qui rate. Espèces non mortelles (hydne, amanite tue-mouches = toxique), donc P3 — mais c'est la même classe de défaut que le P2-1 de 20E, plus petit. *Fix (données ou normalisation) :* `normNom` pourrait ignorer traits d'union et espaces multiples (l.969), ou ajouter les variantes espacées aux `nomFr` concernés.*

**P3-6 (DOC, NOUVEAU) — PRODUCT.md est périmé.** l.38 : « service worker cache-first avec bump `cqm-vN` (actuellement v20) » — le SW est à cqm-v48 (sw.js l.4). Un lecteur de la doc croit à une PWA figée depuis 28 bumps. *Fix :* retirer « actuellement vN » (il sera toujours faux) ou le mettre à jour à chaque bump comme le SW lui-même.*

**P3-7 (DOC, NOUVEAU) — DESIGN.md n'inclut pas le composant étapes progressives.** Le nouveau composant (`.etape`, `.etape-fleche`, l.290-302) respecte la palette mais n'existe pas dans la section Components du design system. Le Do's/Don'ts exige de documenter toute nouveauté. *Fix :* une entrée « Barre d'étapes » dans DESIGN.md (pilule crème → active jaune, numéro noir → rouge, flèche 60 %).*

**P3-8 (A11Y, NOUVEAU) — `.etape` absente de la liste `:focus-visible`.** l.180 couvre `.btn`, `.puce`, `.item`, `.fab`, `nav.tabs`, `.btn-retour` — pas `.etape` : les pilules n'ont que l'outline navigateur par défaut, sans l'anneau ambre du système. *Fix :* ajouter `.etape:focus-visible` à la règle l.180.*

## 8. Red flags par persona

- **Jonathan en forêt, une main, sans réseau** : le pire moment de 20E est refermé — en doute sur un Gyromitre ou une Amanite vireuse, taper le nom que la fiche enseigne (« fausse morille », « ange destructeur ») sert la bonne espèce en position 1 avec une vraie vignette locale. Restant : « pied de mouton » espacé sert un autre hydne avec vignette distante (P3-5), et la création de variété en forêt impose l'étape 2 dense (13 éléments) à la fin d'une journée de cueillette. Pire moment : cliquer ✨ Détails IA sur le terrain, voir le toast « vérifiez », et ne pas trouver quoi — c'est sur l'étape 2 (P2-1).
- **Proche débutant (via export/import)** : la chaîne nom → taxon → fiche est cohérente 21/21 — la confusion morille/gyromitre se résout par « fausse morille » qui répond enfin. L'encart d'étape 1 (l.623) guide la génération IA. Risque restant : un débutant qui génère par IA et enregistre sans visiter l'étape 2 valide un contenu jamais lu (P2-1).
- **Utilisateur pressé / en doute** : le lecteur d'écran entend un tablist incomplet (P3-2) et le clavier perd le focus aux changements d'étape (P3-3) — le flux variété est moins fluide au clavier qu'au doigt. Les suggestions Myco restent sans navigation ↑/↓ (résidu 16E).

## 9. Observations mineures

**Nouveaux :**
- `toast('Entrez d\u2019abord le nom de la variété')` (l.1712) : échappement unicode inutile mais correct — lisibilité du code source seulement.
- Les suggestions `e-nom-suggestions` vivent dans un `<label>` de grille (l.627) : boutons imbriqués dans un label, pattern préexistant mais fragile au clic (le clic sur un bouton de suggestion peut re-déclencher l'activation du label selon le navigateur).
- `.etape-fleche` (l.302) : flèche décorative à opacité 0,6 — cohérent avec le ton, pas un problème de contraste (non informative, `aria-hidden` ✓).

**Résidus inchangés depuis les passes précédentes (non re-scorés, listés pour mémoire) :** navigation clavier des suggestions Myco (16E) · `choisirNomMyco` ne remplit le latin que si vide (15E) · échec silencieux de `chargerBaseMyco` (15E) · champ recherche du guide sans label visible (16E) · focus perdu sur les selects de filtre (16E) · `COULEURS_MOIS` cycle de 6 répété 2×/an (16E) · barres de stats sans `role="progressbar"` + `Math.max(4, …)` pour 0 kg (16E/19E) · lightbox sans focus-trap (16E) · `alt="photo"` générique (16E) · `imageEnBase64` sans limite de taille (16E) · « Dernière sortie » 24 px en carte 2 colonnes (13E) · `ouvrirMyco` sans message hors-ligne (16E) · `.mois-col .lab` 10,5 px (16E) · toast par item absent pour la source IA dans `illu-toutes` (18E) · toast « Aucune spécificité » inatteignable (18E) · `spec-zoom` role=button imbriqué (19E) · cache SW non borné pour les GET réussis (20E).

## 10. Questions provocatrices

1. L'IA remplit l'étape 2 pendant que l'utilisateur regarde l'étape 1, et le toast dit « vérifiez » : pourquoi ne pas avancer automatiquement à l'étape 2 après une génération réussie — un contenu de fiche champignon jamais relu vaut-il le confort de rester sur place ?
2. L'étape 1 garde 5 champs alors que la barre du projet est ≤4 : le découpage est-il fini (prudence/saison → étape 1b, ou statut seul à l'étape 2), ou la barre ≤4 est-elle devenue une cible molle ?
3. « Pied de mouton » espacé sert `Hydnum subtilior` (non-guide, vignette distante) alors que « pied-de-mouton » sert l'espèce du guide : `normNom` ne devrait-il pas ignorer les traits d'union, puisque c'est exactement la faute que fait un clavier mobile ?
4. L'alerte-orange est documentée « Prudence » et sert maintenant d'encart d'aide IA : combien d'usages non-avertissement une couleur de signal peut-elle porter avant que l'utilisateur cesse de la lire comme un danger ?
5. Les pilules d'étapes sont des tabs ARIA sans tabpanel ni flèches : à quel moment ce projet traite-t-il ses composants ARIA jusqu'au bout (tablist complet, combobox des suggestions) au lieu de l'arrêt à mi-chemin ?
6. PRODUCT.md dit « actuellement v20 » alors que le SW est v48 : la doc produit doit-elle suivre la même discipline de bump que le cache, ou est-elle un instantané assumé ?
7. L'étape 2 concentre 8 boutons : « Enregistrer » mérite-t-il d'être le seul bouton plein-vert du bas, les 5 boutons photo pouvant-ils se replier derrière une seule zone photo à 2 actions (caméra/galerie) avec les sources génératives en menu ?
8. Le focus tombe au body à chaque bascule d'étape : le clavier doit-il suivre l'utilisateur dans le parcours (focus sur le premier champ), ou est-ce que le flux variété est conçu doigt-d'abord et assume le clavier comme citoyen de seconde zone ?

---

**Correctifs de la passe 20E vérifiés :**
- **P2-1 ✅ entièrement corrigé, par identité sur les deux axes.** Données : 21/21 entrées `guide:true`, l'ensemble flaggé = exactement les 21 latins du guide (0 faux positif/négatif), 21/21 `nomFr` identiques au nom de la fiche (comparé par latin), `amerivirosa` renommée « Amanite vireuse américaine » (guide:false), 0 img distante, 21/21 fichiers sur disque, 21/21 dans `FICHIERS` du SW (cqm-v48). Comportement (réplication du comparateur l.1611-1631) : « fausse morille » → `Gyromitra esculenta` pos 1, « ange destructeur » → `Amanita virosa` pos 1, « amanite vireuse » → virosa (tie-break guide l.1628), **21/21 noms exacts de fiches → bon taxon en position 1**.
- **P3-1 ✅ corrigé.** `fermerDetail()` (l.1463-1466) = `naviguer('guide')` + restauration du scroll, plus aucun doublon de réinitialisation ; le reset du header vit uniquement dans `naviguer()` (l.1014-1017).
- **Claims `b1aa81d` vérifiés ✅** (`git show --stat` : mycoquebec.json + index.html −2 lignes + sw.js bump, conforme au message).
- **Claims `f076f6c` vérifiés ✅** : `responseMimeType` absent de la requête (seul le commentaire l.1665 le cite), `parserJSONIA` robuste (l.1700-1707), retry 1,5 s sur 429/500/503 + repli `gemini-flash-lite-latest` (l.1685-1697).
- **Claims `326f57c` vérifiés ✅ sauf un** : 2 étapes (l.616-688) ✅ · validation nom avant étape 2 (l.1711-1714) ✅ · pilules tablist + `aria-selected` synchronisé (l.616-620, l.1718-1721) ✅ · garde-fou `formulaireEspeceSale` inchangé (l.1751-1755, byte-identique par `git diff`) ✅ · SW cqm-v48 ✅ · **« lève l'échec de charge cognitive ≤ 4 » : PARTIEL** — 5 champs sur l'étape 1 (barre ≤4 dépassée), étape 2 à 13 éléments d'attention ; l'amélioration est réelle (8→5 champs visibles) mais l'item 6 échoue toujours (voir section 3).

**Non corrigés (nouveaux de cette passe) :** P2-1 (étape 2 remplie invisible), P3-2 à P3-8, et les résidus listés en section 9.
