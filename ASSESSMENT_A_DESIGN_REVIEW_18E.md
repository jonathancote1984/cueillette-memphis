# Assessment A — Critique design (18e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2642 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v42) · **Base :** `img/mycoquebec.json` (3938 entrées)
**Méthode :** lecture statique seule (Assessment A), vérification des 6 findings de la passe 17E et des 5 claims du commit `b0a20f2` (v42) dans le code ET sur les données (base JSON interrogée avec le prédicat et le comparateur réels de l'app, l.1581-1602, répliqués en Python).
**Note :** les 6 findings de 17E sont **tous corrigés ou partiellement corrigés** (aucune régression) ; sur les 5 claims v42, **4 sont entièrement tenus**, 1 est **partiel** (« migration ordre stocké » : la migration écrase aussi les choix EXPLICITES, et son commentaire décrit mal ce qu'elle fait). Un résidu de 17E survit partiellement : « pied-de-mouton » sert toujours Hydnum repandum en premier (le taxon du guide est dans la base, mais le tri le classe 2e).

---

## 1. Verdict de spécificité design : **9/10**

Inchangé : palette de septembre, zigzag, pois, vignettes rayées, inclinaisons, Règle du Trait Noir, Règle du Rouge Mortel, Règle du Décalage Net tenues du header au toast. Les correctifs v42 (transfert de caractéristiques, prompts structurés, migration) ne touchent pas à la grammaire visuelle. Le seul point où la spécificité vacille reste le même : le langage ludique s'applique uniformément, y compris aux moments mortels (rebond élastique des alertes rouges).

## 2. Scores heuristiques Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 4 | Boutons restaurés sur tous les chemins, `btn:disabled` stylé, toasts dans les boucles — inchangé, rien ne régresse |
| 2 | Correspondance monde réel | 3.5 | « amanite vireuse » → **Amanita virosa en premier** ✅, « chanterelle commune » → **cibarius** ✅, « gyromitre » → **esculenta MORTEL 1er** ✅, « morille » → Morchella spp. ✅ — mais « pied-de-mouton » (nom court, celui affiché en tête de fiche) sert **toujours Hydnum repandum** premier, latin auto-rempli différent de la fiche du guide (P2-2), et le paramètre « 🍄 MycoQuébec → Wikimedia → IA » promis dans la liste déroulante est silencieusement réinitialisé à chaque lancement (P2-1) |
| 3 | Contrôle et liberté | 4 | Annuler partout, ← sticky, voile/poignée/Annuler/Escape → garde-fou, analyse annulable, ordre des images configurable (6 combinaisons) |
| 4 | Cohérence et standards | 4 | Double alerte orange supprimée (l.599 : une seule reste), aria-labels 🗑️ ajoutés (l.1194, l.1475), toast par source wiki/myco/IA cohérent — les deux résidus de 17E sont refermés |
| 5 | Prévention des erreurs | 4 | **Régression Escape de 17E corrigée** : `boiteVisible()` gagne maintenant en premier (l.1051-1056) — Escape ferme la confirmation au lieu de la re-empiler ; la branche feuille ne court qu'après (l.1057-1062) |
| 6 | Reconnaissance vs mémorisation | 4 | Autocomplétion (2 systèmes) avec miniatures 26 px dans les suggestions Myco, recherche, tout à l'écran |
| 7 | Flexibilité / efficacité | 3.5 | FAB contextuel, « Réessayer » dernière source, « Générer les manquantes », ordre des images persistant — **mais la migration v42 (l.923) écrase silencieusement une combinaison choisie explicitement** : l'option reste offerte dans le select (l.447) et ne tient jamais au redémarrage |
| 8 | Esthétique minimaliste | 3 | Feuille variété toujours dense : 8 champs + 4 boutons photo + 1 alerte (allégée d'une alerte cette passe) |
| 9 | Aide à la récupération d'erreurs | 4 | messageErreurIA en français, « série interrompue », repli copie du partage, fail-safe statut IA, prompt IA restructuré en 5 objets {spec,desc} EXACTS (l.1780, l.2400) avec placeholder e-carac guidé (l.632) |
| 10 | Aide et documentation | 4 | Carte « Comment identifier », notes partout, crédits Commons, libellé explicite du paramètre Ordre des images |

**Total : 38/40** — progression honnête par rapport à 17E (37,5/40) : les fixes vérifiés (Escape H5 3,5→4, cohérence H4 3,5→4) sont compensés par le nouveau P2-1 (migration, H7 4→3,5) et le résidu pied-de-mouton qui plafonne H2. Profil : sécurité, contrôle et état du système excellents ; le talon d'Achille reste la fidélité des suggestions (1 nom du guide sur 21 sert le mauvais taxon) et la cohérence du paramétrage d'images.

## 3. Charge cognitive : modérée, améliorée

- **Bonne nouvelle** : les miniatures 26 px dans les suggestions Myco (l.1605-1607) donnent enfin l'outil de désambiguïsation visuelle pour les 9 entrées du guide qui en portent — mais 12/21 n'en ont toujours pas (voir P3-1).
- **Friction 1 — Feuille variété** : 8 champs + 4 boutons photo + 1 alerte orange (l.599). La double alerte est réduite à une seule — le bruit baisse, la densité reste.
- **Friction 2 — Suggestions Myco** : puces lourdes (bordure 3 px + ombre) pour un menu de suggestions, toujours sans navigation clavier flèches ↑/↓ (résidu 16E).

**Checklist 8 items :** 1 Focus unique ✅ · 2 Chunking ≤ 4 ✅ · 3 Regroupement visuel ✅ · 4 Hiérarchie ✅ · 5 Une chose à la fois ✅ · 6 Choix minimaux ≤ 4 ❌ (feuille variété : 8 champs + 4 boutons photo + 1 alerte) · 7 Mémoire de travail ✅ (miniatures 26 px aident la désambiguïsation) · 8 Divulgation progressive ✅. **1 échec sur 8.**

## 4. Voyage émotionnel

Ouverture chaleureuse (header dégradé, formes flottantes, zigzag) → le guide accueille avec l'alerte rouge « Règle d'or » → la fiche hybride reste le sommet : cocher une spécificité est une récompense tactile, la coche rouge sans barré arrête la satisfaction là où le danger commence → **le creux de la passe 17 est refermé** : Escape ne boucle plus sur la confirmation (la branche modale gagne, l.1051), taper « amanite vireuse » auto-remplit enfin le latin de l'espèce MORTELLE du guide (Amanita virosa), « chanterelle commune » sert cibarius, « gyromitre » met l'espèce MORTELLE en première position. **Nouveau creux** : le paramètre Ordre des images ment — choisir « 🍄 MycoQuébec → Wikimedia → IA » dans les Paramètres, puis relancer l'app : le select affiche silencieusement « 🌐 Wikimedia → MycoQuébec → IA ». Le choix de l'utilisateur est annulé sans message, à chaque lancement. Le point faible émotionnel reste le même : le rebond élastique s'applique aussi aux alertes mortelles.

## 5. Forces

1. **Un design system tenu de bout en bout** — les quatre règles nommées (Trait Noir, Rouge Mortel, Décalage Net, Inclinaison) sont appliquées sans exception, du header au toast, y compris dans les correctifs v42.
2. **La fiche hybride est une idée de design remarquable** — checklist terrain + verdicts dynamiques ⚠️/✅/☠️. La nouveauté v42 la renforce : les caractéristiques IA structurées en 5 objets {spec,desc} EXACTS (l.1780, l.2400) sont transférées sous les photos à la sauvegarde (`transfererCaracVersItems`, l.1688-1719, appelé l.1739), avec garde-fou `estGenerique` (l.1698) qui préserve les descriptions personnalisées. Le pipeline prompt → parsing → transfert → rendu est cohérent de bout en bout.
3. **Le garde-fou de fermeture couvre les 4 gestes, et Escape a retrouvé son rôle** — poignée (l.1007-1010), voile (l.1003-1006), Annuler (l.1676) et Escape (l.1049-1064) passent par `fermerFeuilleVariete`, et la branche modale gagne (l.1051-1056) : fini la confirmation empilée. Le pattern « vérifier chaque geste séparément » du rapport 14E est complet et sans régression.
4. **Le pattern anti-double-clic est uniforme et complet** — `genererIllu` (l.2187-2205) et `illu-toutes` (l.2224-2251) restaurent leur bouton sur tous les chemins de sortie, avec `btn:disabled` stylé (l.148). Le double-clic payant et le bouton figé restent refermés.
5. **La sécurité reste redondante sans être hystérique** — alerte en tête + verdict dynamique + antipoison répété + matche flou des synonymes + fail-safe IA + focus initial sur « Annuler ». Le rouge est exactement là où il doit être.

## 6. Problèmes prioritaires

**P2-1 (NOUVEAU) — la « migration ordre stocké » écrase un choix EXPLICITE de l'utilisateur, et son commentaire décrit mal ce qu'elle fait.** l.923 : `if (localStorage.getItem('cqm_ordre_images') === 'myco,wikimedia,ia') localStorage.setItem('cqm_ordre_images', 'wikimedia,myco,ia');` avec le commentaire « l'ancien ordre par défaut mettait MycoQuébec en tête ». Or l'ancien défaut n'a **jamais été persisté** : `ordreImages: localStorage.getItem('cqm_ordre_images') || 'myco,wikimedia,ia'` (ancien code) n'écrivait rien — la seule écriture de la clé est le handler du select (l.2542), donc **toute valeur stockée = choix explicite du menu**. La migration convertit donc 100 % de choix délibérés, pas des défauts. Pire : l'option « 🍄 MycoQuébec → Wikimedia → IA » est toujours proposée dans la liste déroulante (l.447), l'utilisateur peut la choisir, et elle sera silencieusement réinitialisée au prochain lancement — le paramètre ment (l'UI promet une combinaison que l'app refuse de tenir). *Pourquoi c'est grave :* une préférence persistante annoncée (« persistant » dans le libellé 15E) qui ne persiste pas, sans aucun message. *Fix :* soit retirer l'option « myco,wikimedia,ia » du select (si MycoQuébec en tête n'est plus un ordre supporté), soit supprimer la migration et laisser le tri faire le travail (avec l'ordre par défaut `wikimedia,myco,ia`, le comportement souhaité est déjà atteint sans toucher aux choix).

**P2-2 (passe 17, claim partiel) — « pied-de-mouton » sert toujours Hydnum repandum en premier.** Le fix bc3cef1 a bien ajouté l'entrée du guide dans la base (« Pied-de-mouton (hydne ombiliqué) », Hydnum umbilicatum, guide:true — vérifié par identité). Mais le tri (l.1583-1601) départage par score d'abord : taper « pied-de-mouton » (le nom court, celui affiché en tête de fiche du guide) est une **égalité exacte** sur « Pied-de-mouton » → Hydnum repandum (score 0, avec img), tandis que « Pied-de-mouton (hydne ombiliqué) » n'est qu'un **préfixe** (score 1). `guide:true` ne départage que les scores égaux (l.1598-1599). Résultat vérifié sur la base avec le comparateur réel : repandum premier, umbilicatum 2e — le latin auto-rempli reste différent de la fiche du guide. (Les deux sont comestibles : c'est un problème de cohérence, plus de sécurité.) *Fix :* donner à l'entrée Hydnum umbilicatum le nomFr exact « Pied-de-mouton » (en gardant « (hydne ombiliqué) » en complément), ou retirer « Pied-de-mouton » du nomFr de l'entrée repandum.

**P3-1 (passe 17, résidu) — 12 des 21 espèces du guide n'ont toujours aucune miniature dans les suggestions.** Le rendu 26 px est en place (l.1605-1607, claim tenu), mais les données manquent : 9/21 entrées du guide portent une `img`, 12 non — dont **Amanite phalloïde, Amanite vireuse et Lépiote brunâtre, les trois MORTELLES**, plus Cèpe de Bordeaux, Chanterelle commune, Chanterelle en tube, Morille, Lépiote élevée, Amanite rougissante, Amanite tue-mouches, Amanite panthère, Entolome livide (vérifié par identité sur la base). L'outil de désambiguïsation visuelle n°1 sert donc le mauvais moitié : les espèces du guide — précisément celles que le guide documente — apparaissent en texte seul, souvent à côté d'un doublon taxonomique avec miniature (vireuse : virosa sans img 1er, amerivirosa avec img 2e). *Fix :* associer les photos `img/especes/<id>.jpg` (déjà embarquées et cachées par le SW) aux 12 entrées.

**P3-2 (NOUVEAU) — repli d'ordre périmé dans `illustrerSpec`.** l.1864 : `const ordre = (Etat.ordreImages || 'myco,wikimedia,ia').split(',')` — le défaut de repli est l'ancien ordre MycoQuébec-en-tête que la migration v42 vient d'abandonner (nouveau défaut : `wikimedia,myco,ia`, l.928). Code mort en pratique (`Etat.ordreImages` est toujours défini), mais le défaut contradictoire trompe le prochain lecteur et contredit le commentaire de migration. *Fix :* aligner sur `'wikimedia,myco,ia'` ou supprimer le repli.

## 7. Red flags par persona

- **Jonathan en forêt, une main, gants, fatigue** : les pires moments de la passe 17 sont refermés — « amanite vireuse » (l'espèce MORTELLE) auto-remplit enfin Amanita virosa, « chanterelle commune » sert cibarius, « gyromitre » place l'espèce MORTELLE en premier, Escape ne boucle plus sur la confirmation d'une feuille sale. **Piège restant :** en doute sur un « pied-de-mouton », la première suggestion auto-remplit Hydnum repandum, un taxon différent de la fiche du guide (P2-2) — et les suggestions des 3 espèces MORTELLES du guide restent sans miniature (P3-1) alors que le doute est le moment où l'image déciderait.
- **Proche débutant (via export/import)** : le garde-fou couvre les 4 gestes ✅, les verdicts sont conditionnés au statut ✅, le marquage guide:true est enfin 21/21 par identité (dont les deux MORTELLES) ✅. Le risque restant : choisir une suggestion Myco laisse le statut « ✅ Comestible » par défaut dans la feuille variété (résidu 16E).
- **Utilisateur pressé / en doute** : le double-clic payant est protégé sur les 3 boutons de génération ✅. Le piège : le paramètre Ordre des images réinitialise silencieusement le choix « MycoQuébec → Wikimedia → IA » à chaque lancement (P2-1) — une préférence qui disparaît sans explication.

## 8. Observations mineures

- 12/21 entrées du guide sans `img` dans la base (dont 3 MORTELLES) — le rendu 26 px est fait, les données ne suivent pas (résidu 17E).
- `choisirNomMyco` (l.1612-1618) : le latin n'est auto-rempli que si le champ est vide — un latin partiel saisi reste (résidu 15E).
- `chargerBaseMyco` (l.1567-1574) : échec de fetch silencieux (`baseMyco = []`) — les suggestions disparaissent sans message (résidu 15E).
- Champ recherche sans label visible (l.387, placeholder seul) — résidu 16E.
- Focus perdu sur les selects de filtre (re-rendu du DOM à chaque changement, l.1318-1319) — résidu 16E.
- `COULEURS_MOIS` (l.2407) : les 12 couleurs se répètent par blocs de 6 sans logique saisonnière lisible — résidu 16E.
- Barres de stats (`topRangs`, l.2410-2413) sans `role="progressbar"` ni valeur numérique sur la barre — résidu 16E.
- Lightbox (l.2257-2277) : Escape + focus restore ✅, pas de focus trap — résidu 16E.
- `alt="photo"` générique sur les photos des zones (l.1142) — résidu 16E.
- `imageEnBase64` (l.1824-1832) sans limite de taille — résidu 16E.
- « Dernière sortie » à 24 px dans une carte 2 colonnes (l.2423) : « 15 août 2026 » peut déborder sur écran étroit — résidu 13E.
- `ouvrirMyco` (l.2254-2256) : lien externe — hors-ligne, le navigateur affiche sa page d'erreur sans message de l'app — résidu 16E.
- `mois-col .lab` à 10,5 px (l.315) : contraste OK (noir sur crème) mais très petit — résidu 16E.
- Dans la boucle `illu-toutes` (l.2241-2242), une image générée par IA ne déclenche aucun toast par item (seuls wiki/myco en ont) — la couverture « Génération terminée ✨ » compense, mais la valence par source est inégale entre le bouton simple (l.2200) et la boucle.
- Le toast « Aucune spécificité — ajoutez-en une ci-dessous » (l.2172) est honnête mais toujours pratiquement inatteignable : `ouvrirSheetIllu` injecte les 5 défauts à l'ouverture (l.2136-2139).

## 9. Questions provocatrices

1. La migration (l.923) réécrit « myco,wikimedia,ia » → « wikimedia,myco,ia » à chaque lancement, alors que cette valeur ne peut exister que par un choix explicite dans le select (l.2542). Pourquoi l'option « 🍄 MycoQuébec → Wikimedia → IA » est-elle encore proposée si l'app refuse de la tenir ?
2. « Pied-de-mouton » sert Hydnum repandum en premier alors que la fiche du guide est Hydnum umbilicatum. Le nom court du guide doit-il être un nomFr exact de l'entrée du guide, ou le tri doit-il départager par `guide:true` AVANT le score d'exactitude ?
3. 12/21 espèces du guide (dont 3 MORTELLES) n'ont pas de miniature dans les suggestions, alors que `img/especes/<id>.jpg` est embarqué et caché par le SW. Pourquoi la désambiguïsation visuelle n°1 dessert-elle précisément le mauvais moitié ?
4. `transfererCaracVersItems` ne transfère que vers les descriptions « génériques » (l.1698) : pour une variété dont les items ont déjà été illustrés avec des descs riches, les détails IA générés restent-ils volontairement ignorés à la sauvegarde — ou l'utilisateur doit-il re-générer la fiche pour les voir ?
5. Le prompt IA exige 5 valeurs de `spec` EXACTES (l.1780) : si le modèle renvoie « Chapeau et cuticule » au lieu de « Chapeau », la ligne est-elle silencieusement perdue par le regex de transfert (l.1692), ou affichée dans e-carac et simplement non transférée ?
6. Le défaut de repli d'`illustrerSpec` (l.1864) dit encore « myco,wikimedia,ia » alors que le nouveau défaut est « wikimedia,myco,ia » (l.928). Lequel est la vérité du produit ?
7. Escape ferme maintenant la confirmation au-dessus d'une feuille sale (l.1051) — et la feuille reste ouverte, formulaire intact. Est-ce le bon comportement, ou Escape #2 devrait-il re-proposer la fermeture ?
8. La coche rouge sans barré sur les fiches mortelles (13E) tient toujours, mais le rebond élastique des alertes rouges aussi : le plaisir doit-il s'arrêter exactement là où le danger commence ?

---

**Correctifs de la passe 17 vérifiés :** P2-1 Escape ✅ **entièrement corrigé** (branche `boiteVisible()` en premier, l.1051-1056 — la confirmation se ferme, plus d'empilement ; branche feuille reléguée après, l.1057-1062) · P2-2 tie-break `guide:true` avant longueur ✅ (l.1598-1599 ; vérifié sur la base : « amanite vireuse » → Amanita virosa 1er, « chanterelle commune » → cibarius 1er, « gyromitre » → esculenta MORTEL 1er, « morille » → Morchella spp. 1er) · P2-3 pied-de-mouton ⚠️ **partiel** (entrée Hydnum umbilicatum ajoutée + guide:true ✅, mais « pied-de-mouton » sert toujours repandum 1er — P2-2) · P3-1 marquage guide ✅ **21/21 par identité** (0 faux positifs, 0 manquants, dont Galérine marginée et Lépiote brunâtre MORTELLES) · P3-3 miniatures 26 px ✅ (rendu l.1605-1607 — **mais 12/21 entrées sans img**, P3-1) · P3-4 libellé état vide ✅ (l.2172, plus de « générez les 5 classiques ») · résidus : double alerte orange supprimée ✅ (une seule alerte l.599), aria-labels 🗑️ ✅ (l.1194, l.1475) · SW cqm-v41 ✅ (remplacé par cqm-v42).
**Claims v42 vérifiés :** 5 claims — 4 entièrement tenus (Wikimedia par terme d'abord avec défaut `wikimedia,myco,ia` + MOTS_SPEC_WIKI par partie l.1834-1847 ; prompts fiche + idphoto structurés en 5 objets {spec,desc} EXACTS l.1780/l.2400 ; `transfererCaracVersItems` à la sauvegarde l.1739 avec garde estGenerique ; placeholder e-carac guidé l.632 ; SW cqm-v42 ✅), 1 **partiel** (« migration ordre stocké » : mécanisme présent l.923 mais il écrase les choix explicites — P2-1, et le commentaire est factuellement inexact).
**Non corrigés (passe 17) :** P2-2 résiduel (pied-de-mouton → repandum 1er) · P3-1 (12/21 sans miniature) · navigation clavier des suggestions Myco · résidus micro-textes et accessibilité listés en section 8.
