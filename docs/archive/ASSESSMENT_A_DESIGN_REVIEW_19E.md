# Assessment A — Critique design (19e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2643 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v44) · **Base :** `img/mycoquebec.json` (3938 entrées)
**Méthode :** lecture statique seule (Assessment A), vérification des 4 findings de la passe 18E, des 4 claims du commit `c900076` (v43) et des 7 claims du commit `699ae19` (v44, polish make-interfaces-feel-better) dans le code ET sur les données (base JSON interrogée avec le comparateur réel de l'app, l.1589-1601, répliqué en Python ; existence des fichiers vérifiée sur disque et dans la liste FICHIERS du SW).
**Note globale :** les 4 findings de 18E sont **corrigés ou partiellement corrigés** (aucune régression) ; sur les claims v43, 3 sont entièrement tenus et 1 est **partiel** (P3-1 : 21/21 avec img vrai au comptage, mais 9/21 pointent encore vers des URLs distantes mycoquebec.org — voir P2-1) ; les 7 claims v44 sont **tous tenus**.

---

## 1. Verdict de spécificité design : **9/10**

Inchangé, et même renforcé par le polish v44. La grammaire Memphis (trait noir 3 px, coins cassés, ombres dures sans flou, inclinaisons, zigzag, pois, vignettes rayées) tient du header au toast, sans une seule dérive mesurable : 0 couleur hors palette documentée, 0 box-shadow flouté, 0 uppercase, graisses strictement 400-700 (battery grep confirmée). Le gain v44 est réel : les transitions `transform + box-shadow` synchronisées sur `.fab/.item/.puce/.btn-retour` font de la Règle du Décalage Net une règle *animée* — l'appui translate et l'ombre se résorbe ensemble, l'effet « bouton qu'on enfonce » est désormais physique, pas téléporté. Le seul point où la spécificité vacille reste identique : le langage ludique s'applique uniformément, y compris aux moments mortels (rebond élastique des alertes rouges).

## 2. Scores heuristiques Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 4 | Toasts, états vides, analyse annulable, `btn:disabled` — mais le header reste en « mode détail » après une navigation par onglet (P3-1) |
| 2 | Correspondance monde réel | 4 | **Pied-de-mouton → Hydnum umbilicatum en premier** ✅ (repandum renommé « Hydne sinué »), vireuse → virosa, chanterelle commune → cibarius, gyromitre → esculenta MORTEL 1er, morille → Morchella spp. — les 21 noms du guide servent le bon taxon, vérifié par réplication du comparateur |
| 3 | Contrôle et liberté | 4 | Annuler partout, ← sticky avec restauration du scroll, garde-fou 4 gestes, analyse annulable, 6 combinaisons d'ordre d'images **enfin honorées** (migration supprimée) |
| 4 | Cohérence et standards | 4 | Une seule alerte orange dans la feuille variété, aria-labels 🗑️, toasts par source wiki/myco/IA — seul accroc : l'aria-label du FAB ment sur l'onglet Identifier (P3-2) |
| 5 | Prévention des erreurs | 4 | Branche modale avant branche feuille dans Escape (l.1050-1064), matche flou des synonymes, double confirmation, focus initial sur Annuler |
| 6 | Reconnaissance vs mémorisation | 3.5 | Miniatures 26 px dans les suggestions Myco : **21/21 espèces du guide en portent une** — mais 9 pointent vers des URLs distantes et cassent hors-ligne, dont 2 MORTELLES (P2-1) |
| 7 | Flexibilité / efficacité | 4 | FAB contextuel, « Réessayer » dernière source, « Générer les manquantes », ordre des images persistant et **tenu au redémarrage** (le mensonge 18E est refermé) |
| 8 | Esthétique minimaliste | 3 | Feuille variété toujours dense : 8 champs + 4 boutons photo + 1 alerte |
| 9 | Aide à la récupération d'erreurs | 4 | messageErreurIA en français par cause, « série interrompue », repli copie du partage, fail-safe statut IA, prompts JSON stricts |
| 10 | Aide et documentation | 4 | Carte « Comment identifier », crédits Commons, libellés explicites, note du paramètre Ordre des images honnête |

**Total : 38,5/40** — progression honnête par rapport à 18E (38/40) : H2 3,5→4 (pied-de-mouton) et H7 3,5→4 (migration supprimée, l'option « myco,wikimedia,ia » est enfin tenue) sont partiellement compensés par H6 4→3,5 (9 miniatures distantes hors-ligne). Profil : sécurité, contrôle, état du système excellents ; le talon d'Achille reste la fidélité du support visuel de désambiguïsation dans le mode de fonctionnement promis (hors-ligne).

## 3. Charge cognitive : modérée, améliorée

- **Bonne nouvelle** : les 12 miniatures locales ajoutées couvrent enfin les 3 MORTELLES phalloïde/vireuse/lépiote-brunâtre + cèpe, chanterelle commune/tube, morille, lépiote élevée, rougissante, tue-mouches, panthère, entolome (vérifié par identité). 9 espèces restent sur des vignettes distantes (P2-1).
- **Friction 1 — Feuille variété** : 8 champs + 4 boutons photo + 1 alerte orange (l.602). Densité inchangée.
- **Friction 2 — Suggestions Myco** : puces lourdes (bordure 3 px + ombre) pour un menu de suggestions, toujours sans navigation clavier ↑/↓ (résidu 16E).

**Checklist 8 items :** 1 Focus unique ✅ · 2 Chunking ≤ 4 ✅ · 3 Regroupement visuel ✅ · 4 Hiérarchie ✅ · 5 Une chose à la fois ✅ · 6 Choix minimaux ≤ 4 ❌ (feuille variété) · 7 Mémoire de travail ⚠️ (9 vignettes distantes = l'outil visuel n°1 disparaît hors-ligne, précisément au moment du doute — P2-1) · 8 Divulgation progressive ✅. **1 échec franc + 1 avertissement sur 8.**

## 4. Voyage émotionnel

Ouverture chaleureuse inchangée (header dégradé, formes flottantes, zigzag) → guide avec la Règle d'or → fiche hybride toujours au sommet (cocher une spécificité reste une récompense tactile, la coche rouge sans barré arrête la satisfaction où le danger commence). **Le creux de la passe 18 est refermé** : le paramètre Ordre des images tient enfin — choisir « 🍄 MycoQuébec → Wikimedia → IA » survit au redémarrage, la migration abusive a disparu (0 occurrence grep), et le select (l.449-456) ne ment plus. Le polish v44 ajoute une vraie caresse : l'appui des cartes/boutons est désormais physique (ombre + translation animées ensemble), et les colonnes de chiffres (mesures, rangs, compteurs) ne dansent plus grâce à `tabular-nums` — deux micro-joies pour une main fatiguée en forêt. **Nouveau creux** : en forêt, sans réseau, les suggestions de 9 espèces du guide (dont la Galérine marginée et le Gyromitre, MORTELLES) affichent une vignette cassée — l'outil de désambiguïsation visuelle tombe en panne au pire moment, dans le mode d'emploi promis. Le point faible émotionnel historique reste : le rebond élastique s'applique aussi aux alertes mortelles.

## 5. Forces

1. **Le polish tactile v44 est un vrai gain, pas du vernis** — les 7 claims sont tenus : transitions `transform + box-shadow` synchronisées sur `.fab` (l.104), `.item` (l.128), `.puce` (l.167), `.btn-retour` (l.62) ; onglets animés 0,15 s interruptibles (l.83) ; hit area 44 px du zoom de spécificité (l.250) ; outline 1 px noir 10 % sur toutes les photos de zones (l.137, 189, 248, 326) ; `tabular-nums` sur mesures/rangs/compteurs (l.55, 141, 267, 298, 312) ; `text-wrap:pretty` sur le corps (l.140, 259, 320, 330) ; `-webkit-font-smoothing:antialiased` (l.29). La Règle du Décalage Net devient une règle animée — cohérente avec l'identité « carnet tactile ».
2. **La chaîne nom → taxon → fiche est enfin cohérente pour les 21 espèces** — la paire nomFr exact + `guide:true` + tri score→guide→longueur (l.1589-1601) sert le bon taxon pour chaque nom du guide, vérifié par réplication du comparateur sur la base : « pied-de-mouton » → Hydnum umbilicatum ★🖼 premier (repandum a été renommé « Hydne sinué » — plus aucun doublon exact), « amanite vireuse » → virosa devant amerivirosa, « gyromitre » → esculenta MORTEL premier. Le latin auto-rempli dans la feuille variété correspond désormais à la fiche du guide.
3. **Un design system tenu sans exception, même dans les correctifs** — battery grep : 0 migration résiduelle, 0 couleur hors palette, 0 ombre floutée, 0 uppercase, 0 graisse hors 400-700, aucune valence de toast mensongère sur un chemin d'échec (les ✨/✅ ne vivent que dans les branches de succès). Les quatre règles nommées (Trait Noir, Rouge Mortel, Décalage Net, Inclinaison) tiennent du header au toast, pour la 19e passe consécutive.

## 6. Problèmes prioritaires

**P2-1 (claim v43 partiel) — 9 des 21 miniatures du guide restent des URLs distantes mycoquebec.org dans la base : l'outil de désambiguïsation visuelle casse hors-ligne, dont pour 2 espèces MORTELLES.** Vérifié par identité sur `img/mycoquebec.json` : 12 entrées `guide:true` portent une `img` locale (`img/especes/<id>.jpg`, dont phalloïde, vireuse, lépiote-brunâtre), mais 9 portent `https://mycoquebec.org/images/espece-mini/...` : **Coprin chevelu, Galérine marginée (MORTEL), Gyromitre commun (MORTEL), Pied-de-mouton, Fausse chanterelle, Bolet bai, Paxille enroulé, Pleurote en huître, Bolet amer**. Ces URLs ne figurent pas dans la liste FICHIERS du SW (l.12-32) : hors-ligne, la miniature de suggestion (rendu l.1606-1608) et la source « myco » d'`illustrerSpec` (l.1867-1872) affichent une image cassée tant que l'URL n'a jamais été mise en cache par une visite en ligne — pour un produit promis « 100 % hors-ligne dès la première visite » (PRODUCT.md). Le claim « 21/21 avec img » est vrai au comptage, faux sur l'axe que l'utilisateur vit (le hors-ligne). Le fix est trivial : `img/especes/<id>.jpg` existe sur disque pour les 21 espèces et est déjà caché par le SW — remplacer les 9 valeurs `img` par les fichiers locaux.

**P3-1 (NOUVEAU) — le header reste en « mode détail » après une navigation par onglet.** `naviguer()` (l.977-991) bascule les vues et le bouton ←, mais ne réinitialise ni `#sous-titre` ni `#badge` : seul `fermerDetail()` (l.1434-1435) restaure « Carnet de champignons · édition Memphis » et le badge compteur. Si Jonathan ouvre la fiche « Amanite phalloïde » puis tape l'onglet Cueillettes, le header affiche « 🍄 Amanite phalloïde » et le badge reste masqué pour le reste de la session (jusqu'au prochain aller-retour détail) — l'état affiché contredit la vue courante. *Fix :* centraliser la réinitialisation du header dans `naviguer()` (sous-titre + badge + btn-retour), `fermerDetail()` ne faisant que rappeler `naviguer('guide')`.

**P3-2 (NOUVEAU) — l'aria-label du FAB ment sur l'onglet Identifier.** l.985 : `fab.setAttribute('aria-label', vue === 'spots' ? 'Ajouter un spot' : 'Ajouter une cueillette')` — mais sur l'onglet Identifier, le clic ouvre la feuille « Nouvelle variété » (l.996). Un lecteur d'écran annonce « Ajouter une cueillette » et l'action crée une variété d'espèce. *Fix :* trois valeurs de label alignées sur l'action réelle par onglet (spots → spot, guide → variété, cueillettes → cueillette), ou un libellé neutre « Ajouter ».

## 7. Red flags par persona

- **Jonathan en forêt, une main, sans réseau** : les pires pièges des passes précédentes sont refermés — « pied-de-mouton » auto-remplit enfin le taxon de la fiche du guide (P2-2 18E ✅), l'ordre des images survit au redémarrage (P2-1 18E ✅), Escape ne boucle plus (17E ✅). **Piège restant :** en doute sur un Gyromitre ou une Galérine — deux MORTELLES —, la suggestion affiche une vignette cassée hors-ligne (P2-1) : l'image qui déciderait est exactement celle qui manque, dans le mode promis.
- **Proche débutant (via export/import)** : les verdicts sont conditionnés au statut, le marquage guide est 21/21 par identité, l'import vérifie la version ✅. Risque restant : choisir une suggestion Myco laisse le statut « ✅ Comestible » par défaut dans la feuille variété (résidu 16E), et 9 vignettes distantes (P2-1) alimentent la confusion visuelle hors-ligne.
- **Utilisateur pressé / en doute** : le double-clic payant est protégé sur les 3 boutons de génération ✅, l'ordre des images est enfin honnête ✅. Nouveau petit piège : un lecteur d'écran pressé entend « Ajouter une cueillette » sur l'onglet Identifier et se retrouve dans « Nouvelle variété » (P3-2).

## 8. Observations mineures

- 12/21 miniatures du guide sont locales, 9/21 distantes (P2-1) — le rendu 26 px est complet, les données à moitié.
- `choisirNomMyco` (l.1618) : le latin n'est auto-rempli que si le champ est vide — résidu 15E.
- `chargerBaseMyco` (l.1573) : échec de fetch silencieux (`baseMyco = []`) — les suggestions disparaissent sans message — résidu 15E.
- Champ recherche sans label visible (l.390, placeholder seul) — résidu 16E.
- Focus perdu sur les selects de filtre (re-rendu du DOM, l.1319) — résidu 16E.
- `COULEURS_MOIS` (l.2408) : le même cycle de 6 couleurs se répète deux fois par an (janv-fév rouille, mars ambre, avr olive, mai cuir, juin terracotta, puis à l'identique) — résidu 16E.
- Barres de stats (`topRangs`, l.2410-2413) sans `role="progressbar"` ni valeur sur la barre ; un poids de 0 kg dessine quand même un stub de 4 % (`Math.max(4, …)`) — résidus 16E/19E.
- Lightbox (l.2258-2278) : Escape + focus restore ✅, pas de focus trap — résidu 16E.
- `alt="photo"` générique (l.1143) — résidu 16E.
- `imageEnBase64` (l.1825-1833) sans limite de taille — résidu 16E.
- « Dernière sortie » à 24 px dans une carte 2 colonnes (l.2424) : « 15 août 2026 » peut déborder sur écran étroit — résidu 13E.
- `ouvrirMyco` (l.2256) : lien externe — hors-ligne, page d'erreur du navigateur sans message de l'app — résidu 16E.
- `.mois-col .lab` à 10,5 px (l.318) : contraste OK (noir sur crème) mais très petit — résidu 16E.
- Boucle `illu-toutes` : une image générée par IA ne déclenche aucun toast par item (seuls wiki/myco en ont, l.2242-2243) — valence par source inégale — résidu 18E.
- Toast « Aucune spécificité — ajoutez-en une ci-dessous » (l.2173) toujours inatteignable : `ouvrirSheetIllu` injecte les 5 défauts à l'ouverture (l.2136-2140) — résidu 18E.
- `spec-zoom` : span `role="button"` imbriqué dans une carte `role="button"` (l.1393) — imbrication interactive, fonctionnelle grâce au stopPropagation.

## 9. Questions provocatrices

1. `img/especes/<id>.jpg` existe pour les 21 espèces du guide et est caché par le SW — pourquoi 9 entrées de la base gardent-elles des URLs mycoquebec.org dans `img`, alors que le fix de la passe 18 a touché les 12 autres ? La promesse « 100 % hors-ligne dès la première visite » s'applique-t-elle aux suggestions ou seulement aux fiches ?
2. « pied-de-mouton » sert enfin Hydnum umbilicatum, mais le gyromitre s'affiche « Gyromitre commun » dans les suggestions alors que la fiche du guide dit « Gyromitre (fausse morille) » : deux libellés pour une même espèce MORTELLE — lequel est la vérité du produit ?
3. Le header n'est réinitialisé que par `fermerDetail()` : l'état du header (sous-titre, badge, ←) doit-il vivre dans `naviguer()` comme les vues, plutôt que d'être restauré par un chemin de sortie unique ?
4. Le FAB annonce « Ajouter une cueillette » sur l'onglet Identifier et ouvre « Nouvelle variété » : le label doit-il suivre l'action par onglet (3 valeurs), ou le FAB devrait-il carrément changer d'icône sur l'onglet guide (＋ → 🍄) pour dire ce qu'il fait ?
5. `COULEURS_MOIS` répète le même cycle de 6 deux fois par an : est-ce un cycle saisonnier délibéré (les couleurs de l'automne québécois en double) ou une copie de tableau ?
6. Les suggestions Myco sont sans navigation clavier depuis 16E, et le latin ne s'auto-remplit que si le champ est vide (15E) : à quel moment un champ d'autocomplétion devient-il un vrai combobox ARIA dans ce projet ?
7. Le verdict ☠️ « n/n critères vérifiés » d'une espèce toxique (non mortelle) utilise le même rouge que MORTEL : la coche rouge sans barré (13E) doit-elle distinguer « toxique » de « mortel » dans le verdict final ?
8. `Math.max(4, …)` dessine une barre de 4 % pour une récolte de 0 kg : un zéro honnête doit-il être un zéro invisible ?
9. Les 9 miniatures distantes se mettent en cache au premier GET réussi (fetch handler du SW) : est-ce un mécanisme de remplissage acceptable, ou la base doit-elle être la seule source de vérité visuelle hors-ligne ?

---

**Correctifs de la passe 18 vérifiés :** P2-1 migration ✅ **entièrement corrigée** (0 occurrence de code de migration ; l.929 `ordreImages: localStorage.getItem('cqm_ordre_images') || 'wikimedia,myco,ia'` ; l'option « myco,wikimedia,ia » du select l.450 est maintenant tenue — handler l.2541-2545 → lecture l.929, aucun écrasement) · P2-2 pied-de-mouton ✅ **entièrement corrigé** (base : Hydnum umbilicatum `nomFr` « Pied-de-mouton (hydne ombiliqué) » + `guide:true` + img ; Hydnum repandum renommé « Hydne sinué » ; comparateur répliqué : « pied-de-mouton » → umbilicatum 1er, aucun autre doublon exact) · P3-1 miniatures ⚠️ **partiel** (12/21 locales ajoutées dont les 3 MORTELLES phalloïde/vireuse/lépiote-brunâtre ✅ — mais 9/21 restent distantes, P2-1) · P3-2 repli illustrerSpec ✅ (l.1865 `'wikimedia,myco,ia'` aligné sur le défaut l.929) · SW cqm-v43 ✅ (remplacé par cqm-v44).
**Claims v44 vérifiés (7/7 tenus) :** transitions ombre+transform `.fab` l.104 / `.item` l.128 / `.puce` l.167 / `.btn-retour` l.62 ✅ · onglets actifs 0,15 s interruptibles l.83 ✅ · hit area spec-zoom 44 px l.250 ✅ · outline 1 px noir pur 10 % sur photos de zones l.137/189/248/326 ✅ · `tabular-nums` mesures l.141 + rangs l.312 (+ compteurs l.55/267/298) ✅ · `text-wrap:pretty` corps l.140/259/320/330 ✅ · `-webkit-font-smoothing:antialiased` l.29 ✅ · SW cqm-v44 ✅ (FICHIERS complet : 21 jpg especes + 105 specs + 2 credits.json + mycoquebec.json).
**Non corrigés (passe 18) :** P3-1 partiel (9/21 distantes — P2-1) · navigation clavier des suggestions Myco · résidus micro-textes et accessibilité listés en section 8.
