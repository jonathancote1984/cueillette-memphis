# Assessment A — Critique design (15e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2562 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v38) · **Base :** `img/mycoquebec.json` (3924 entrées)
**Méthode :** lecture statique seule (Assessment A), vérification des correctifs de la passe 14 (rapport `ASSESSMENT_A_DESIGN_REVIEW_14E.md`) et des claims du commit `ee85f7b` (v38) dans le code.
**Note :** les deux correctifs de la passe 14 sont **confirmés dans le code** (P1-1 base enrichie, P2-1 latin .85) ; le claim v38 est **tenu** (86 % de nomFr, tri français, .85 AA). Mais la passe 14 sous-estimait le trou du garde-fou de fermeture : la poignée de feuille **contourne entièrement** le garde-fou (nouveau constat, H5 en baisse), et les noms français des espèces les plus dangereuses restent muets dans l'autocomplétion (H2 plafonné).

---

## 1. Verdict de spécificité design : **9/10**

Design **indissociable de son sujet** — inchangé depuis la passe 14 : palette de septembre, zigzag, pois, vignettes rayées, inclinaisons, Règle du Trait Noir, Règle du Rouge Mortel, Règle du Décalage Net tenues du header au toast. La base MycoQuébec enrichie (3924 entrées) ne change rien à la grammaire visuelle : les suggestions réutilisent les puces existantes, le tri français est invisible à l'œil. Le seul endroit où la spécificité vacille reste le même : le langage ludique s'applique uniformément, y compris aux moments mortels (rebond élastique des alertes rouges, coche rouge qui reste une « récompense » visuelle sur les fiches dangereuses — atténuée par le fix 13E sans barré).

## 2. Scores heuristiques Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 3 | « Générer » et « Générer les manquantes » ne désactivent toujours pas leur bouton pendant 10-20 s par image (P2-2 non corrigé) ; le toast meurt à 2,2 s |
| 2 | Correspondance monde réel | 3 | Base passée de 21 à 3379 nomFr (86 %) ✅ — mais les noms français des espèces les plus dangereuses restent muets : « amanite phalloïde », « amanite panthère », « paxille enroulé » → zéro suggestion (P2-1 nouveau) |
| 3 | Contrôle et liberté | 4 | Annuler partout, ← sticky, voile/poignée/Escape, garde-fou (partiel), analyse annulable, restauration sélective, ordre des images configurable |
| 4 | Cohérence et standards | 3 | Toast « Illustration générée ✅ » pour une miniature MycoQuébec *trouvée* ; FAB aria-label fixe « Ajouter » ; double alerte orange dans la feuille variété ; « 🍄 Fiche MycoQuébec » seul dans une `grille2` |
| 5 | Prévention des erreurs | 2.5 | Double confirmation, import versionné, matche flou+synonymes — **mais la poignée de feuille contourne entièrement le garde-fou** (ligne 1011 : `fermerFeuilles` direct, pas `fermerFeuilleVariete`) : fermer la feuille variété par la poignée perd TOUS les champs sans confirmation, et le statut n'est protégé sur aucun chemin (P2-3 aggravé) |
| 6 | Reconnaissance vs mémorisation | 4 | Autocomplétion (2 systèmes), recherche, tout est à l'écran |
| 7 | Flexibilité / efficacité | 4 | FAB contextuel, « Réessayer » dernière source, « Générer les manquantes », ordre des images (6 combinaisons, persistant) |
| 8 | Esthétique minimaliste | 3 | Vue Identifier allégée (2 selects) ✅ ; la feuille variété reste dense : 8 champs + 4 boutons photo + 2 alertes orange empilées |
| 9 | Aide à la récupération d'erreurs | 4 | messageErreurIA en français, « série interrompue », repli copie du partage, fail-safe statut IA |
| 10 | Aide et documentation | 4 | Carte « Comment identifier », notes partout, crédits Commons, libellé explicite du paramètre Ordre des images |

**Total : 34,5/40** — baisse honnête de 1,5 par rapport à la passe 14 (36/40) : les deux correctifs de la 14e passe sont vérifiés dans le code (P1-1 base 86 %, P2-1 latin .85 = 4,91:1), mais la passe 14 affirmait que le garde-fou couvrait « poignée, voile, Escape » — c'était faux : la poignée (geste de fermeture principal) appelle `fermerFeuilles` directement et contourne tout le garde-fou (H5 3 → 2,5), et l'autocomplétion reste muette sur les noms des mortelles (H2 plafonné à 3). Profil : très solide sur la sécurité et le contrôle, faible sur la cohérence des micro-messages, le feedback des opérations longues et la protection des chemins de fermeture.

## 3. Charge cognitive : modérée, inchangée

- **Bonne nouvelle** : les 2 selects de filtres tiennent (la vue Identifier reste allégée), et l'autocomplétion MycoQuébec couvre maintenant 86 % des noms français — le système s'apprend toujours en 2 minutes.
- **Friction 1 — Feuille variété** : 8 champs + 4 boutons photo + 2 alertes orange empilées (lignes 605 et 661) avant les boutons d'action. La deuxième alerte (« 🔑 La clé Gemini se configure dans Paramètres ») reste redondante avec le toast PAS_DE_CLE et le bandeau de la vue guide.
- **Friction 2 — Suggestions Myco** : puces lourdes (bordure 3 px + ombre) pour un menu de suggestions, sans navigation clavier flèches — même constat que les passes 13-14, maintenant doublé.

**Checklist 8 items :** 1 Focus unique ✅ · 2 Chunking ≤ 4 ✅ · 3 Regroupement visuel ✅ · 4 Hiérarchie ✅ · 5 Une chose à la fois ✅ · 6 Choix minimaux ≤ 4 ❌ (feuille variété : 8 champs + 4 boutons photo + 2 alertes) · 7 Mémoire de travail ✅ · 8 Divulgation progressive ✅. **1 échec sur 8.**

## 4. Voyage émotionnel

Ouverture chaleureuse (header dégradé, formes flottantes, zigzag) → le guide accueille avec l'alerte rouge « Règle d'or » : la sécurité prime, le plaisir retombe d'un coup → la fiche hybride reste le sommet : cocher une spécificité est une récompense tactile, et sur les fiches mortelles la coche rouge sans barré arrête la satisfaction là où le danger commence → **le sommet de la passe 15** : l'autocomplétion répond enfin aux noms français courants (86 % de la base) — le plaisir de la découverte est réel → **le creux, inchangé et aggravé** : taper « amanite phalloïde » — le nom du champignon le plus dangereux du guide — dans la feuille variété ne donne **aucune suggestion** (P2-1 nouveau) ; et fermer la feuille par la poignée après avoir rempli 8 champs perd tout sans confirmation (P2-3 aggravé). Le point faible émotionnel reste le même : le rebond élastique s'applique aussi aux alertes mortelles.

## 5. Forces

1. **Un design system tenu de bout en bout** — les quatre règles nommées (Trait Noir, Rouge Mortel, Décalage Net, Inclinaison) sont appliquées sans exception, du header au toast, y compris dans les trois dernières features. C'est un système, pas un habillage.
2. **La fiche hybride est une idée de design remarquable** — checklist terrain + verdicts dynamiques ⚠️/✅/☠️ qui transforment un guide passif en protocole actif. Le fix 13E (coche rouge sans barré, verdict-att rouge conditionné) tient toujours.
3. **La sécurité est redondante sans être hystérique** — alerte en tête + verdict dynamique + antipoison répété + matche flou des synonymes + fail-safe IA + focus initial sur « Annuler ». Le rouge est exactement là où il doit être.
4. **La base MycoQuébec enrichie (v38)** — 3924 entrées, 3379 nomFr (86 %), tri priorisant les matches français, latin des suggestions à .85 (4,91:1 AA). Le claim du commit est tenu, y compris sur les données (vérifié : 3924 entrées, 3379 nomFr, tous uniques, 21/21 espèces du guide présentes dans la base).

## 6. Problèmes prioritaires

**P1-1 (passe 14) — ✅ CORRIGÉ ET VÉRIFIÉ.** Base enrichie : 3924 entrées, 3379 avec nomFr (86 %), tri priorisant les matches français (lignes 1566-1571), latin des suggestions à `opacity:.85` (ligne 1575). Vérifié sur les données : 3924 entrées, 3379 nomFr uniques, 21/21 espèces du guide présentes. Le claim v38 est tenu.

**P2-1 (passe 14) — ✅ CORRIGÉ ET VÉRIFIÉ.** Latin des suggestions passé de `.7` à `.85` (ligne 1575) : noir #241A0F à 85 % sur blanc #FDF6E7 = **4,91:1** (AA à 13 px). La réintroduction du défaut de la passe 11 est refermée.

**P2-2 (passe 14) — ❌ NON CORRIGÉ — Les boutons de génération restent sans état désactivé.** `genererIllu` (ligne 2115) et `illu-toutes` (ligne 2150) ne désactivent toujours pas leur bouton pendant la génération (10-20 s par image, 50-100 s pour les 5 manquantes) ; le toast meurt à 2,2 s (ligne 747), donc plus aucun feedback visible, et un second clic relance un appel payant. `e-generer` (ligne 1723) fait exactement le contraire (`btn.disabled = true` + libellé « Génération en cours… ») — le pattern existe dans le fichier. *Fix :* aligner les trois boutons sur le pattern de `e-generer`, avec un état visuel et un garde anti-double-clic.

**P2-3 (passe 14) — ❌ NON CORRIGÉ ET AGGRAVÉ — Le garde-fou de fermeture est contournable par la poignée, et le statut n'est protégé sur aucun chemin.** `formulaireEspeceSale()` (lignes 1644-1646) teste 7 champs texte + la photo, mais **ignore `e-statut` et `e-prudence`** — changer « ✅ Comestible » → « ☠️ MORTEL » puis fermer perd le choix sans confirmation. **Nouveau constat :** la poignée de feuille (ligne 1011) appelle `fermerFeuilles` **directement**, pas `fermerFeuilleVariete` — le geste de fermeture le plus naturel (tirer la poignée) contourne **entièrement** le garde-fou, même pour les champs texte. Seuls le voile (ligne 1008) et le bouton Annuler (ligne 1643) passent par le garde-fou. La passe 14 affirmait « poignée, voile, Escape » — c'était faux (Escape ne ferme d'ailleurs aucune feuille, seulement les modales, lignes 1050-1065). *Fix :* `document.querySelectorAll('.feuille .poignee').forEach(p => p.addEventListener('click', fermerFeuilleVariete))` (ou un handler générique qui route vers le garde-fou de la feuille ouverte), et ajouter `$('e-statut').value !== 'comestible' || $('e-prudence').checked` au test.

**P2-4 (passe 14) — ❌ NON CORRIGÉ — Le repli IA contourne l'ordre des images choisi (ligne 1830).** Si l'utilisateur choisit « myco,wikimedia » (sans IA) et que les deux sources échouent, `illustrerSpec` appelle **quand même** `genererImageIA` hors ordre — et sans clé, l'utilisateur reçoit un toast « 🔑 Ajoutez votre clé Gemini » pour une source qu'il n'a pas demandée. *Fix :* soit respecter strictement l'ordre (retourner l'échec avec un message honnête), soit documenter « l'IA en dernier recours » dans le libellé du paramètre.

**P2-5 (NOUVEAU) — Les noms français des espèces les plus dangereuses sont muets dans l'autocomplétion MycoQuébec.** Vérifié sur la base : « amanite phalloïde » → **zéro suggestion** (aucune entrée phalloides/pantherina avec nomFr) ; « amanite panthère » → zéro ; « paxille enroulé » → zéro. « amanite vireuse » suggère « Amanite amerivirosa » (nomFr « Amanite vireuse ») — un taxon différent du « Amanita virosa » du guide, avec auto-remplissage du latin erroné (ligne 1585). Le cueilleur en doute sur LE champignon le plus mortel du guide tape son nom et n'obtient rien — le pire moment pour un silence. *Fix :* injecter les 21 espèces du guide (dont les 5 mortelles) dans la base avec leur nomFr, ou ajouter un repli : si zéro suggestion Myco, proposer les espèces du guide dont le nom français matche.

**P3-1 (passe 14) — ❌ NON CORRIGÉ — CSS mort non purgé malgré le claim du commit `4929c4d` (v36).** Les 7 règles orphelines `puce.actif[data-f=…]` et `puce.actif[data-fs]` (lignes 167-173) sont **toujours dans le CSS** alors que plus aucun élément `data-f` n'existe dans le HTML/JS. *Fix :* supprimer les lignes 167-173.

**P3-2 (passe 14) — ❌ NON CORRIGÉ — Toast « Illustration générée ✅ » pour une miniature trouvée (ligne 2127).** Le ternaire ne distingue que `wikimedia` ; une miniature MycoQuébec *trouvée* affiche « Illustration générée ✅ » — même mécanisme de valence mensongère que le ✨ corrigé en passe 12. *Fix :* distinguer `myco` (« Photo MycoQuébec 🍄 »).

**P3-3 (passe 14) — ❌ NON CORRIGÉ — Résidus :** FAB `aria-label="Ajouter"` fixe alors que l'icône change (ligne 479) ; 🗑️ icon-only sans aria-label sur les items spots (ligne 1185) et cueillettes (ligne 1459) ; toast à 2,2 s trop court pour les messages d'erreur IA longs (ligne 747) ; double alerte orange dans la feuille variété (lignes 605, 661) ; « 🍄 Fiche MycoQuébec » noyé dans le bloc Photo (lignes 656-658) et **seul dans une `grille2`** → bouton à demi-largeur avec un vide à côté ; champ recherche sans label visible ni bouton d'effacement (ligne 393) ; « Aucun champignon trouvé » sans proposition de réinitialiser (ligne 1329) ; suggestions (cueillette + variété) sans navigation clavier flèches (lignes 1474, 1575) ; focus perdu sur les selects de filtre (re-rendu du DOM à chaque changement, lignes 1296-1308).

**P3-4 (passe 14) — ❌ NON CORRIGÉ — Miniatures MycoQuébec « hors-ligne » seulement après une 1re charge en ligne.** Le JSON est embarqué ✅, mais les `img` sont des URLs distantes `mycoquebec.org` (3807/3924 entrées). Le SW les met en cache best-effort après une 1re visite en ligne (fetch handler, lignes 160-163), mais hors-ligne dès la première utilisation, l'image ne charge pas. *Fix :* documenter la limite, ou télécharger les miniatures dans `img/` comme les photos Wikimedia.

**P3-5 (NOUVEAU) — La carte « Comment identifier » hardcode « 5/5 vérifiés » (ligne 472).** La checklist est dynamique (l'utilisateur ajoute/retire des spécificités via la feuille Illustrations IA) — le verdict affiche « n/n » dynamiquement, mais la carte d'aide promet un compte fixe de 5. Le fix de la passe 9 (« verdict danger dynamique, plus de 5/5 en dur vs compteur ») a corrigé le verdict mais pas la carte d'aide. *Fix :* « Tous les critères vérifiés sur une espèce mortelle » sans chiffre.

## 7. Red flags par persona

- **Jonathan en forêt, une main, gants, fatigue** : le pire moment reste la génération d'illustrations sans feedback — bouton muet pendant 10-20 s, double-clic possible, toast mort à 2,2 s. **Nouveau pire moment potentiel** : en doute sur une amanite, il tape « amanite phalloïde » dans la feuille variété → silence (P2-5), puis ferme la feuille par la poignée → tout est perdu sans confirmation (P2-3).
- **Proche débutant (via export/import)** : le filtre « ☠️ Ne pas manger » inclut les mortelles ✅, les verdicts sont conditionnés au statut ✅. Le risque restant : la feuille variété où « MORTEL » peut être perdu silencieusement à la fermeture (P2-3), et la carte d'aide qui promet « 5/5 » alors que le compte est dynamique (P3-5).
- **Utilisateur pressé / en doute** : le parcours photo IA est bien sécurisé (fail-safe, « à vérifier », Annuler). Le piège : re-cliquer « Générer » pendant une génération en cours = double coût API et double attente (P2-2).

## 8. Observations mineures

- `choisirNomMyco` (ligne 1585) : le latin n'est auto-rempli que si le champ est **vide** — un latin partiel saisi reste, créant une incohérence nomFr/latin possible.
- `chargerBaseMyco` (ligne 1556) : échec de fetch silencieux (`baseMyco = []`) — les suggestions disparaissent sans message.
- `mois-col .lab` à 10,5 px (ligne 321) : contraste OK (noir sur crème, 14:1) mais très petit.
- `COULEURS_MOIS` (ligne 2327) : les 12 couleurs se répètent par blocs de 6 sans logique saisonnière lisible (juillet-août = rouille, comme janvier-février).
- Barres de stats (`topRangs`, lignes 2328-2333) sans `role="progressbar"` — l'info est dans le texte adjacent, perte limitée mais barres muettes pour les lecteurs d'écran.
- Lightbox (lignes 2178-2198) : Escape + focus restore ✅, mais pas de focus trap (Tab peut sortir du dialogue).
- `alt="photo"` générique sur les photos des zones (ligne 1133).
- `imageEnBase64` (ligne 1756) sans limite de taille — une grosse image Wikimedia peut saturer IndexedDB.
- « Dernière sortie » à 24 px dans une carte 2 colonnes (ligne 2343) : « 15 août 2026 » risque de déborder sur écran étroit (résidu 13E).
- `ouvrirMyco` (ligne 2176) : lien externe vers mycoquebec.org — hors-ligne, le navigateur affiche sa page d'erreur, sans message de l'app.

## 9. Questions provocatrices

1. La base couvre 86 % des noms français — mais « amanite phalloïde », le nom du champignon le plus mortel du guide, ne donne aucune suggestion. La couverture est-elle mesurée sur les espèces que les gens cherchent, ou sur celles que la base contient ?
2. La poignée de feuille contourne entièrement le garde-fou de fermeture. Pourquoi le geste de fermeture le plus naturel est-il le seul qui ne demande jamais confirmation ?
3. « Amanite vireuse » suggère « Amanita amerivirosa » et auto-remplit un latin différent de celui du guide. Est-ce une erreur taxonomique ou une mise à jour silencieuse de la nomenclature ?
4. « Générer les manquantes » lance 5 appels Gemini sans désactiver le bouton. Combien de double-clics avant que le quota 429 ne devienne le vrai feedback ?
5. L'ordre des images exclut l'IA… sauf quand tout échoue. Un paramètre contourné en silence est-il encore un paramètre ?
6. Le toast dit « Illustration générée ✅ » pour une photo trouvée sur MycoQuébec. Le mensonge est petit — mais c'est le même mécanisme que le ✨ de l'échec corrigé en passe 12.
7. Les 7 règles CSS orphelines des puces `data-f` : le commit v36 dit « CSS mort purgé ». Qui vérifie les claims des commits avant de les archiver ?
8. La carte « Comment identifier » promet « 5/5 » alors que l'utilisateur peut ajouter ou retirer des spécificités. Un compte en dur à côté d'un compteur dynamique : lequel ment ?
9. Deux systèmes de suggestions (cueillette + variété) avec des puces lourdes et zéro navigation clavier. Quand le menu de suggestions deviendra-t-il un vrai composant ?
10. La miniature MycoQuébec est « hors-ligne » seulement après une 1re charge en ligne. Le JSON est embarqué, les images non — où s'arrête la promesse 100 % hors-ligne du PRODUCT.md ?

---

**Correctifs de la passe 14 vérifiés :** P1-1 base enrichie 3924 espèces / 3379 nomFr (86 %) + tri français + latin .85 ✅ (vérifié sur les données : 3924 entrées, 3379 nomFr uniques, 21/21 espèces du guide présentes) · P2-1 latin des suggestions à .85 = 4,91:1 AA ✅.
**Claims v38 vérifiés :** base 3924 espèces (3379 nomFr, 86 % vs 21 avant) ✅ · tri priorisant les matches français ✅ · latin des suggestions à opacity .85 (AA) ✅ — **claim entièrement tenu**.
**Non corrigés (passe 14) :** P2-2 (boutons de génération sans disabled) · P2-3 (garde-fou incomplet — aggravé : poignée contourne tout) · P2-4 (repli IA hors ordre) · P3-1 (CSS mort) · P3-2 (toast myco) · P3-3 (résidus) · P3-4 (miniatures distantes).
