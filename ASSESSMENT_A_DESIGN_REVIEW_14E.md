# Assessment A — Critique design (14e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2557 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v37) · **Base :** `img/mycoquebec.json` (212 entrées)
**Méthode :** lecture statique seule (Assessment A), vérification des correctifs de la passe 13 (commit `32cebce`) et des claims des commits `4929c4d` (v36) et `7d11cd4` (v37) dans le code.
**Note :** tous les correctifs de la passe 13 sont **confirmés dans le code** ; deux claims de commits récents sont **partiellement non tenus** (voir P1-1 et P3-1).

---

## 1. Verdict de spécificité design : **9/10**

Design **indissociable de son sujet** — inchangé depuis la passe 13 : palette de septembre, zigzag, pois, vignettes rayées, inclinaisons, Règle du Trait Noir, Règle du Rouge Mortel, Règle du Décalage Net tenues du header au toast. Les deux nouveautés de la passe 14 s'intègrent sans casser la grammaire : les filtres du guide sont passés de 10 puces à 2 selects (la double grammaire d'état « actif » a disparu avec elles — amélioration réelle), et l'autocomplétion MycoQuébec réutilise les puces existantes. Le seul endroit où la spécificité vacille reste le même : le langage ludique s'applique uniformément, y compris aux moments mortels (le rebond élastique des alertes rouges, la coche rouge qui reste une « récompense » visuelle).

## 2. Scores heuristiques Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 3 | « Générer les manquantes » et « 🎨 Générer » ne désactivent pas leur bouton pendant 10-20 s par image ; le toast meurt à 2,2 s — l'utilisateur ne voit plus rien, et peut relancer un double appel Gemini |
| 2 | Correspondance monde réel | 3 | L'autocomplétion MycoQuébec ne couvre que **21/212** espèces en nom français (P1-1) — taper un nom français courant hors de ces 21 ne donne aucune suggestion |
| 3 | Contrôle et liberté | 4 | Annuler partout, ← sticky, voile/poignée/Escape, garde-fou de saisie, analyse annulable, restauration sélective, ordre des images configurable |
| 4 | Cohérence et standards | 3 | Toast « Illustration générée ✅ » pour une miniature *trouvée* ; FAB aria-label fixe « Ajouter » ; double alerte orange dans la feuille variété ; « 🍄 Fiche MycoQuébec » noyé dans le bloc Photo |
| 5 | Prévention des erreurs | 3 | Double confirmation, import versionné, matche flou+synonymes — mais le garde-fou de fermeture de la feuille variété **ignore le statut** : changer « comestible » → « MORTEL » puis fermer perd le choix sans confirmation (P2-3) |
| 6 | Reconnaissance vs mémorisation | 4 | Autocomplétion (2 systèmes), recherche, tout est à l'écran |
| 7 | Flexibilité / efficacité | 4 | FAB contextuel, « Réessayer » dernière source, « Générer les manquantes », ordre des images (6 combinaisons, persistant) — bon ajout |
| 8 | Esthétique minimaliste | 3 | Vue Identifier allégée (2 selects au lieu de 10 puces) ✅ ; la feuille variété reste dense : 8 champs + 4 boutons photo + 2 alertes orange empilées |
| 9 | Aide à la récupération d'erreurs | 4 | messageErreurIA en français, « série interrompue », repli copie du partage, fail-safe statut IA |
| 10 | Aide et documentation | 4 | Carte « Comment identifier », notes partout, crédits Commons, libellé explicite du paramètre Ordre des images |

**Total : 36/40** — plateau honnête par rapport à la passe 13 (36/40) : les six correctifs de la 13e passe sont vérifiés dans le code, mais les deux nouvelles features (v36/v37) apportent leur propre dette (couverture Myco 21/212, feedback de génération absent, garde-fou incomplet). Profil : très solide sur la sécurité et le contrôle, faible sur la cohérence des micro-messages et le feedback des opérations longues.

## 3. Charge cognitive : modérée, un point de friction en moins, un en plus

- **Bonne nouvelle** : les 10 puces de filtres sont devenues 2 selects — la vue Identifier a perdu sa double grammaire d'état (couleur sémantique vs noir/crème) et 8 éléments de décision. Le système s'apprend toujours en 2 minutes.
- **Friction 1 — Feuille variété** : 8 champs + 4 boutons photo + 2 alertes orange empilées (lignes 605 et 661) avant les boutons d'action. La deuxième alerte (« 🔑 La clé Gemini se configure dans Paramètres ») est redondante avec le toast PAS_DE_CLE et le bandeau de la vue guide.
- **Friction 2 — Suggestions Myco** : puces lourdes (bordure 3 px + ombre) pour un menu de suggestions, sans navigation clavier flèches — même constat que la passe 13 sur l'autocomplétion cueillette, maintenant doublé.

**Checklist 8 items :** 1 Focus unique ✅ · 2 Chunking ≤ 4 ✅ · 3 Regroupement visuel ✅ · 4 Hiérarchie ✅ · 5 Une chose à la fois ✅ · 6 Choix minimaux ≤ 4 ❌ (feuille variété : 8 champs + 4 boutons photo + 2 alertes) · 7 Mémoire de travail ✅ · 8 Divulgation progressive ✅ (suggestions au fil de la frappe, ordre des images documenté dans Paramètres). **1 échec sur 8.**

## 4. Voyage émotionnel

Ouverture chaleureuse (header dégradé, formes flottantes, zigzag) → le guide accueille avec l'alerte rouge « Règle d'or » : la sécurité prime, le plaisir retombe d'un coup → la fiche hybride reste le sommet : cocher une spécificité est une récompense tactile, et sur les fiches mortelles la coche rouge sans barré (fix 13E vérifié) arrête la satisfaction là où le danger commence → **nouveau sommet de la passe 14** : générer les illustrations dans l'ordre choisi (MycoQuébec → Wikimedia → IA) donne un sentiment de contrôle rare dans une PWA mono-fichier → le creux : taper un nom français dans la feuille variété et ne recevoir aucune suggestion pour 191 espèces sur 212 (P1-1) — le plaisir de la découverte s'arrête net. Le point faible émotionnel reste le même : le rebond élastique s'applique aussi aux alertes mortelles.

## 5. Forces

1. **Un design system tenu de bout en bout** — les quatre règles nommées (Trait Noir, Rouge Mortel, Décalage Net, Inclinaison) sont appliquées sans exception, du header au toast, y compris dans les deux nouvelles features. C'est un système, pas un habillage.
2. **La fiche hybride est une idée de design remarquable** — checklist terrain + verdicts dynamiques ⚠️/✅/☠️ qui transforment un guide passif en protocole actif. Le fix 13E (coche rouge sans barré sur fiches dangereuses, verdict-att rouge conditionné) a fermé la dernière collision de valence.
3. **La sécurité est redondante sans être hystérique** — alerte en tête + verdict dynamique + antipoison répété + matche flou des synonymes + fail-safe IA + focus initial sur « Annuler ». Le rouge est exactement là où il doit être.
4. **Le paramètre « 🖼️ Ordre des images »** (lignes 450-459, 1791, 1818-1825) : 6 combinaisons, persistant, appliqué par `illustrerSpec` — une vraie flexibilité utilisateur, documentée dans son libellé, dans une app mono-fichier. Rareté.

## 6. Problèmes prioritaires

**P1-1 — L'autocomplétion MycoQuébec ne couvre que 21/212 espèces en nom français.** Le commit `7d11cd4` promet « base embarquée 212 espèces latin+miniature+nomFr, suggestions au fil de la frappe ». La base `img/mycoquebec.json` contient bien 212 entrées, mais **seules 21 ont un `nomFr`** (vérifié : 191 entrées n'ont que `latin` + `img`). `remplirSuggestionsMyco` (ligne 1566) filtre sur `x.nomFr && normNom(x.nomFr).includes(q)` — pour 191 espèces, seule la frappe du **latin** donne une suggestion. Un cueilleur qui tape « Tricholome », « Cortinaire » ou « Russule » n'obtient rien et peut croire que l'espèce n'est pas documentée. *Pourquoi c'est grave :* la promesse de la fonction (nom français au fil de la frappe) est livrée à 10 %. *Fix :* enrichir la base avec les nomFr manquants (le site MycoQuébec les expose), ou reformuler le libellé (« suggestions pour les espèces les plus courantes ») et le placeholder.

**P2-1 — Latin des suggestions Myco à `opacity:.7` = 2.91:1 (ligne 1570).** `<i style="opacity:.7">` sur le nom latin dans chaque puce de suggestion : noir #241A0F à 70 % sur blanc #FDF6E7 → **2.91:1** (AA exige 4.5:1 à 13 px). C'est la **réintroduction exacte du défaut corrigé en passe 11** (`.ligne-latin` passé de .7 à .85 = 4.91:1). *Fix :* `opacity:.85` (4.91:1) ou suppression de l'italique atténué.

**P2-2 — Boutons de génération sans état désactivé : double-clic = double appel Gemini.** `genererIllu` (ligne 2110) et `illu-toutes` (ligne 2145) ne désactivent pas leur bouton pendant la génération (10-20 s par image, 50-100 s pour les 5 manquantes) ; le toast meurt à 2,2 s, donc plus aucun feedback visible, et un second clic relance un appel payant. `e-generer` (ligne 1718) fait exactement le contraire (`btn.disabled = true` + libellé « Génération en cours… ») — le pattern existe déjà dans le fichier. *Fix :* aligner les trois boutons sur le pattern de `e-generer`, avec un état visuel (libellé changeant) et un garde anti-double-clic.

**P2-3 — Garde-fou de fermeture incomplet : le statut n'est pas protégé.** `formulaireEspeceSale()` (lignes 1639-1642) teste 7 champs texte + la photo, mais **ignore `e-statut` et `e-prudence`**. Changer « ✅ Comestible » → « ☠️ MORTEL » puis fermer la feuille (poignée, voile, Escape) ferme **sans confirmation** et perd le choix — une perte de sécurité, pas seulement de texte. *Fix :* ajouter `$('e-statut').value !== 'comestible' || $('e-prudence').checked` au test.

**P2-4 — Le repli IA contourne l'ordre des images choisi (ligne 1825).** Si l'utilisateur choisit « myco,wikimedia » (sans IA) et que les deux sources échouent, `illustrerSpec` appelle **quand même** `genererImageIA` hors ordre — et sans clé, l'utilisateur reçoit un toast « 🔑 Ajoutez votre clé Gemini » pour une source qu'il n'a pas demandée. Le paramètre promet un ordre de priorité ; le code ajoute un repli inconditionnel. *Fix :* soit respecter strictement l'ordre (retourner l'échec avec un message honnête), soit documenter « l'IA en dernier recours » dans le libellé du paramètre.

**P3-1 — CSS mort non purgé malgré le claim du commit `4929c4d`.** Le commit v36 dit « CSS mort purgé » ; les 8 règles orphelines `puce.actif[data-f=…]` et `puce.actif[data-fs]` (lignes 167-173) sont **toujours dans le CSS** alors que plus aucun élément `data-f` n'existe dans le HTML/JS (les puces ont été remplacées par les selects). Claim non tenu. *Fix :* supprimer les lignes 167-173.

**P3-2 — Toast « Illustration générée ✅ » pour une miniature trouvée (ligne 2122).** Le ternaire ne distingue que `wikimedia` (« Photo Wikimedia trouvée 📷 ») ; une miniature MycoQuébec *trouvée* affiche « Illustration générée ✅ » — même mécanisme de valence mensongère que le ✨ corrigé en passe 12. *Fix :* distinguer `myco` (« Photo MycoQuébec 🍄 »).

**P3-3 — Résidus de la passe 13 non adressés :** FAB `aria-label="Ajouter"` fixe alors que l'icône change (ligne 479) ; 🗑️ icon-only sans aria-label sur les items spots (ligne 1185) et cueillettes (ligne 1459) ; toast à 2,2 s trop court pour les messages d'erreur IA longs ; double alerte orange dans la feuille variété (lignes 605, 661) ; « 🍄 Fiche MycoQuébec » noyé dans le bloc Photo (lignes 656-658) et **seul dans une `grille2`** → bouton à demi-largeur avec un vide à côté ; champ recherche sans label visible ni bouton d'effacement ; « Aucun champignon trouvé » sans proposition de réinitialiser ; suggestions (cueillette + variété) sans navigation clavier flèches.

**P3-4 — Miniatures MycoQuébec « hors-ligne » seulement après une 1re charge en ligne.** Le JSON est embarqué ✅, mais les `img` sont des URLs distantes `mycoquebec.org` (197/212 entrées). Le SW les met en cache best-effort après une 1re visite en ligne (fetch handler, ligne 160-163), mais hors-ligne dès la première utilisation, l'image ne charge pas. Le commentaire du commit (« hors-ligne, CORS OK en <img> ») est optimiste. *Fix :* documenter la limite, ou télécharger les miniatures dans `img/` comme les photos Wikimedia.

## 7. Red flags par persona

- **Jonathan en forêt, une main, gants, fatigue** : le pire moment est désormais la génération d'illustrations sans feedback — bouton muet pendant 10-20 s, double-clic possible, toast mort à 2,2 s. Et l'autocomplétion qui ne répond pas aux noms français courants (191/212 muettes) le fait douter de sa propre saisie en pleine forêt.
- **Proche débutant (via export/import)** : le filtre « ☠️ Ne pas manger » inclut désormais les mortelles ✅ (fix 13E vérifié). Le risque restant : la feuille variété où « MORTEL » peut être perdu silencieusement à la fermeture (P2-3).
- **Utilisateur pressé / en doute** : le parcours photo IA est bien sécurisé (fail-safe, « à vérifier », Annuler). Le piège : re-cliquer « Générer » pendant une génération en cours = double coût API et double attente.

## 8. Observations mineures

- `choisirNomMyco` (ligne 1580) : le latin n'est auto-rempli que si le champ est **vide** — un latin partiel saisi reste, créant une incohérence nomFr/latin possible.
- `chargerBaseMyco` (ligne 1556) : échec de fetch silencieux (`baseMyco = []`) — les suggestions disparaissent sans message.
- `mois-col .lab` à 10,5 px (ligne 321) : contraste OK (noir sur crème, 14:1) mais très petit.
- `COULEURS_MOIS` (ligne 2322) : les 12 couleurs se répètent par blocs de 6 sans logique saisonnière lisible (juillet-août = rouille, comme janvier-février).
- Barres de stats (`topRangs`, lignes 2326-2328) sans `role="progressbar"` — l'info est dans le texte adjacent, perte limitée mais barres muettes pour les lecteurs d'écran.
- Lightbox (lignes 2173-2193) : Escape + focus restore ✅, mais pas de focus trap (Tab peut sortir du dialogue).
- `alt="photo"` générique sur les photos des zones (ligne 1133).
- `imageEnBase64` (ligne 1751) sans limite de taille — une grosse image Wikimedia peut saturer IndexedDB.
- « Dernière sortie » à 24 px dans une carte 2 colonnes (ligne 2338) : risque de débordement sur écran étroit (résidu 13E).
- Focus perdu sur les selects de filtre : `rendreFiltres()` re-rend le DOM à chaque changement (lignes 1296-1308) — le select est détruit pendant l'interaction.

## 9. Questions provocatrices

1. La base MycoQuébec promet « 212 espèces latin+miniature+nomFr » et n'en livre que 21 en français. Vaut-il mieux une base honnête de 21 espèces complètes, ou une promesse de 212 ?
2. Le latin des suggestions à 2.91:1 réintroduit le défaut corrigé en passe 11. Qui surveille les nouveaux textes ajoutés après une passe de correctifs ?
3. « Générer les manquantes » lance 5 appels Gemini sans désactiver le bouton. Combien de double-clics avant que le quota 429 ne devienne le vrai feedback ?
4. Le garde-fou protège les champs texte mais pas le statut. Perdre « MORTEL » en fermant une feuille, est-ce une perte de texte ou une perte de sécurité ?
5. L'ordre des images exclut l'IA… sauf quand tout échoue. Un paramètre contourné en silence est-il encore un paramètre ?
6. Le toast dit « Illustration générée ✅ » pour une photo trouvée sur MycoQuébec. Le mensonge est petit — mais c'est le même mécanisme que le ✨ de l'échec corrigé en passe 12.
7. Les 8 règles CSS orphelines des puces `data-f` : le commit v36 dit « CSS mort purgé ». Qui vérifie les claims des commits avant de les archiver ?
8. Deux systèmes de suggestions (cueillette + variété) avec des puces lourdes et zéro navigation clavier. Quand le menu de suggestions deviendra-t-il un vrai composant ?
9. La miniature MycoQuébec est « hors-ligne » seulement après une 1re charge en ligne. Le JSON est embarqué, les images non — où s'arrête la promesse 100 % hors-ligne du PRODUCT.md ?

---

**Correctifs de la passe 13 vérifiés et tenus** (commit `32cebce`, cqm-v35) : P0 verdict-att conditionné au statut (rouge « Espèce MORTELLE — ne jamais consommer, même si tous les critères semblent correspondre », plus de passage rouge→jaune à la décoche) ✅ · P1 filtre « ☠️ Ne pas manger » inclut les mortelles ✅ · P1 « Confusions possibles » remontées sous l'alerte (index < index de la galerie) ✅ · P2 coche rouge sans barré sur fiches non comestibles ✅ · P2 bandeau clé passé en note discrète (`class="note"`) ✅ · P3 h2 « Cueillettes » + badge masqué à 0 ✅.
**Claims v36 vérifiés :** 🙈 retiré de la liste du guide ✅ · 2 selects avec aria-label ✅ · **CSS mort purgé ❌ (P3-1)**.
**Claims v37 vérifiés :** détails des spécificités sous les photos ✅ · paramètre Ordre des images (6 combinaisons, persistant, appliqué) ✅ · **base 212 espèces latin+miniature+nomFr ❌ partiel (21/212 nomFr — P1-1)**.
