# Assessment A — Critique design (17e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2602 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v40) · **Base :** `img/mycoquebec.json` (3938 entrées)
**Méthode :** lecture statique seule (Assessment A), vérification des 9 claims du commit `36e11a9` (v40) dans le code ET sur les données (base JSON interrogée avec le prédicat réel de l'app, l.1580-1599).
**Note :** 7 claims sur 9 sont **entièrement tenus**, 1 est **partiellement tenu** (P2-5 : 21 entrées marquées `guide:true` mais seulement 11 sont des espèces du guide — le marquage est à moitié faux), 1 est **tenu avec réserve** (P2-4 : « morille » et « gyromitre » sont enfin visibles, mais « amanite vireuse » et « chanterelle commune » affichent toujours le mauvais taxon en premier, et « pied-de-mouton » sert un taxon différent de celui du guide). Le fix Escape (P3) a introduit une **régression** : Escape ne peut plus fermer une modale de confirmation ouverte au-dessus d'une feuille variété sale — il re-déclenche le garde-fou et empile la confirmation.

---

## 1. Verdict de spécificité design : **9/10**

Inchangé depuis la passe 16 : palette de septembre, zigzag, pois, vignettes rayées, inclinaisons, Règle du Trait Noir, Règle du Rouge Mortel, Règle du Décalage Net tenues du header au toast. Les correctifs v40 (tri des suggestions, Escape, boutons restaurés) ne touchent pas à la grammaire visuelle. Le seul endroit où la spécificité vacille reste le même : le langage ludique s'applique uniformément, y compris aux moments mortels (rebond élastique des alertes rouges).

## 2. Scores heuristiques Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 4 | Boutons restaurés sur TOUS les chemins de sortie (l.2150-2153, l.2189-2210) ✅ ; `btn:disabled` enfin stylé (l.148 : opacity .55 + not-allowed) ✅ ; toast myco dans la boucle (l.2203) ✅ |
| 2 | Correspondance monde réel | 3.5 | « morille » → Morchella spp. en premier ✅, « fausse chanterelle » → Hygrophoropsis aurantiaca (le bon taxon toxique) ✅, « corne d'abondance »/« lactaire délicieux » ✅ — mais « amanite vireuse » → amerivirosa premier (latin erroné auto-rempli pour l'espèce MORTELLE), « chanterelle commune » → enelensis premier, « pied-de-mouton » → Hydnum repandum (≠ Hydnum umbilicatum du guide), « gyromitre » → Gyromitra esculenta MORTELLE 3e |
| 3 | Contrôle et liberté | 4 | Annuler partout, ← sticky, voile/poignée/Annuler/Escape → garde-fou, analyse annulable, ordre des images configurable |
| 4 | Cohérence et standards | 3.5 | Toast myco dans la boucle ✅, libellé échec de sources distinct ✅ (l.1626) — résidus : double alerte orange (l.599, l.655), 🗑️ sans aria-label (l.1193, l.1474) |
| 5 | Prévention des erreurs | 3.5 | Escape couvre enfin les feuilles (l.1049-1058) ✅ — **mais régression** : Escape ne peut pas fermer une confirmation ouverte au-dessus d'une feuille sale (l.1049-1058 court avant la branche modale l.1060-1064 → re-déclenche le garde-fou, confirmation empilée) |
| 6 | Reconnaissance vs mémorisation | 4 | Autocomplétion (2 systèmes), recherche, tout est à l'écran |
| 7 | Flexibilité / efficacité | 4 | FAB contextuel, « Réessayer » dernière source, « Générer les manquantes », ordre des images (6 combinaisons, persistant) |
| 8 | Esthétique minimaliste | 3 | Feuille variété toujours dense : 8 champs + 4 boutons photo + 2 alertes orange empilées |
| 9 | Aide à la récupération d'erreurs | 4 | messageErreurIA en français, « série interrompue », repli copie du partage, fail-safe statut IA |
| 10 | Aide et documentation | 4 | Carte « Comment identifier », notes partout, crédits Commons, libellé explicite du paramètre Ordre des images |

**Total : 37,5/40** — plateau honnête par rapport à 16E (37/40) : la régression du bouton figé est **vérifiée corrigée** (+0,5 sur H1), mais le fix Escape a introduit le piège de la confirmation empilée (−0,5 sur H5), et H2 reste plafonné par le mauvais taxon premier sur les deux requêtes les plus dangereuses. Profil : très solide sur la sécurité, le contrôle et l'état du système ; encore faible sur la qualité des suggestions (égalité exacte non départagée par `guide:true`) et les micro-messages.

## 3. Charge cognitive : modérée, inchangée

- **Bonne nouvelle** : les 3 cas nommés en passe 16 répondent, « morille » exacte est première, « fausse chanterelle » sert le bon taxon toxique.
- **Friction 1 — Feuille variété** : 8 champs + 4 boutons photo + 2 alertes orange empilées (l.599 et l.655) avant les boutons d'action. La deuxième alerte (« 🔑 La clé Gemini se configure dans Paramètres ») reste redondante avec le toast PAS_DE_CLE et le bandeau de la vue guide.
- **Friction 2 — Suggestions Myco** : puces lourdes (bordure 3 px + ombre) pour un menu de suggestions, sans navigation clavier flèches, et **sans miniatures** alors que la base en porte (l.1600-1604 ne rend que du texte) — même constat que les passes 13-16.

**Checklist 8 items :** 1 Focus unique ✅ · 2 Chunking ≤ 4 ✅ · 3 Regroupement visuel ✅ · 4 Hiérarchie ✅ · 5 Une chose à la fois ✅ · 6 Choix minimaux ≤ 4 ❌ (feuille variété : 8 champs + 4 boutons photo + 2 alertes) · 7 Mémoire de travail ✅ · 8 Divulgation progressive ✅. **1 échec sur 8.**

## 4. Voyage émotionnel

Ouverture chaleureuse (header dégradé, formes flottantes, zigzag) → le guide accueille avec l'alerte rouge « Règle d'or » : la sécurité prime → la fiche hybride reste le sommet : cocher une spécificité est une récompense tactile, et sur les fiches mortelles la coche rouge sans barré arrête la satisfaction là où le danger commence → **les creux de la passe 16 sont partiellement refermés** : « morille » répond en premier, « fausse chanterelle » sert enfin le bon taxon toxique, « corne d'abondance » et « lactaire délicieux » répondent — mais **le pire moment reste mal servi** : taper « amanite vireuse » (doute sur l'espèce MORTELLE) propose toujours « Amanita amerivirosa » en premier, latin erroné auto-rempli ; taper « pied-de-mouton » (nom du guide) sert Hydnum repandum, un taxon différent de la fiche du guide ; et « gyromitre » place Gyromitra esculenta MORTELLE en 3e position. **Nouveau creux** : sur une feuille variété sale, Escape ouvre la confirmation… et Escape ne peut plus la fermer — chaque appui re-déclenche le garde-fou. Le point faible émotionnel reste le même : le rebond élastique s'applique aussi aux alertes mortelles.

## 5. Forces

1. **Un design system tenu de bout en bout** — les quatre règles nommées (Trait Noir, Rouge Mortel, Décalage Net, Inclinaison) sont appliquées sans exception, du header au toast, y compris dans les correctifs v40. C'est un système, pas un habillage.
2. **La fiche hybride est une idée de design remarquable** — checklist terrain + verdicts dynamiques ⚠️/✅/☠️ qui transforment un guide passif en protocole actif. Le fix 13E (coche rouge sans barré, verdict-att rouge conditionné) tient toujours.
3. **Le garde-fou de fermeture couvre maintenant les 4 gestes** — poignée (l.1006-1009), voile (l.1002-1005), Annuler (l.1671) et **Escape (l.1049-1058)** passent tous par `fermerFeuilleVariete`, et `formulaireEspeceSale` teste les 7 champs texte + la photo + le statut et la prudence (l.1672-1676). Le pattern « vérifier chaque geste séparément » du rapport 14E est enfin complet — avec le piège de l'empilement (voir P2-1).
4. **Le pattern anti-double-clic est uniforme et complet** — `genererIllu` (l.2148-2166) et `illu-toutes` (l.2185-2212) restaurent leur bouton sur **tous** les chemins de sortie (clé manquante, espèce introuvable, item introuvable, tout-généré, erreur, succès), et `btn:disabled` a maintenant un style visuel (l.148). Le double-clic payant et le bouton figé sont refermés.
5. **La sécurité reste redondante sans être hystérique** — alerte en tête + verdict dynamique + antipoison répété + matche flou des synonymes + fail-safe IA + focus initial sur « Annuler ». Le rouge est exactement là où il doit être.

## 6. Problèmes prioritaires

**P2-1 (NOUVEAU — régression du fix Escape v40) — Escape ne peut pas fermer une confirmation ouverte au-dessus d'une feuille sale.** Le nouveau bloc Escape (l.1049-1058) court **avant** la branche modale (l.1060-1064). Scénario : feuille variété sale ouverte → Escape #1 → `fermerFeuilleVariete()` → `formulaireEspeceSale()` vrai → `confirmer()` (l.1677-1681). La modale est ouverte, la feuille reste `.ouverte`. Escape #2 → le premier bloc attrape l'événement (la feuille est toujours ouverte) → `fermerFeuilleVariete()` → le formulaire est toujours sale → `confirmer()` **à nouveau** : `resolveConfirm` est écrasé (l.1031), la confirmation se ré-affiche au lieu de se fermer. La branche modale d'Escape (l.1060-1064) est **inatteignable** tant qu'une feuille est ouverte. Le geste clavier le plus standard pour « non, annule » boucle. *Fix :* tester `boiteVisible()` en premier dans le handler (si une modale est visible, la branche modale gagne), ou dans la branche feuille, ignorer si `boiteVisible()`.

**P2-2 (passe 16, résidu) — le mauvais taxon gagne toujours sur les égalités exactes.** Le nouveau tri (l.1582-1598) départage par score (exact 0 / préfixe 1 / guide 2 / inclusion 3) puis par **longueur du nom** (l.1597). Mais sur une égalité exacte (même nomFr, même longueur), le tri stable laisse l'ordre de la base gagner : « amanite vireuse » → **Amanita amerivirosa** (avec img) premier, « Amanita virosa » (guide:true, img:'') second — le latin erroné s'auto-remplit toujours pour l'espèce MORTELLE (vérifié sur la base avec le prédicat réel). Même mécanisme pour « chanterelle commune » → **Cantharellus enelensis** premier, « Cantharellus cibarius » (guide:true) 6e. Le flag `guide:true` n'intervient qu'au score 2, jamais pour départager une égalité exacte. *Fix :* dans le tie-break, `guide:true` avant la longueur (ou fusionner les entrées : garder le nomFr du guide + la miniature existante).

**P2-3 (passe 16, résidu) — « pied-de-mouton » sert un taxon différent de la fiche du guide.** Le guide a « Pied-de-mouton (hydne ombiliqué) » = Hydnum umbilicatum ; la base a « Hydne ombiliqué » (Hydnum umbilicatum) **sans** « pied-de-mouton » dans son nomFr, et l'entrée marquée `guide:true` « Pied-de-mouton » = **Hydnum repandum** (un autre champignon). Taper « pied-de-mouton » → 1 suggestion : Hydnum repandum, latin auto-rempli différent de la fiche du guide. Le nom d'affichage du guide est absent de la base. *Fix :* ajouter « Pied-de-mouton » comme nomFr de l'entrée Hydnum umbilicatum (ou renommer l'entrée), et corriger le marquage `guide:true` (voir P3-1).

**P3-1 (passe 16, claim partiel) — le marquage `guide:true` est à moitié faux.** 21 entrées marquées, mais seulement **11 sont des espèces du guide** ; 10 marquées ne le sont pas (Chanterelle jaune, Helvelle crépue, Hydnum repandum, Lactaire indigo, Pied bleu, Morille commune, Russule émétique, Bolet jaune, Corne d'abondance, Lactaire délicieux) et **10 espèces du guide ne sont pas marquées** (Cèpe de Bordeaux, Bolet bai, Pied-de-mouton/hydne ombiliqué, Morille, Coprin chevelu, Lépiote élevée, Bolet amer, Entolome livide, **Galerine marginée MORTELLE**, **Lépiote brunâtre MORTELLE**). Le claim « 21 espèces du guide marquées guide:true » est exact sur le compte, trompeur sur l'identité. Impact pratique faible (les 21 répondent par nom exact via la base), mais le boost de tri promis par le flag ne s'applique qu'à 11 espèces. *Fix :* aligner le marquage sur les 21 latins du guide (vérifiable par script).

**P3-2 (passe 16, résidu) — « gyromitre » : l'espèce MORTELLE est 3e, pas première.** « Gyromitre brun » (Discina brunnea) et « Gyromitre ambigu » (Paragyromitra ambigua) passent devant « Gyromitre commun » (Gyromitra esculenta, guide:true) : tous préfixes (score 1), tie-break par longueur → « gyromitrebrun » (13) < « gyromitrecommun » (15). Visible dans les 6 ✅, mais le premier choix n'est pas l'espèce du guide. *Fix :* le tie-break `guide:true` avant la longueur règle aussi ce cas.

**P3-3 (passe 16, résidu) — suggestions sans miniatures ni navigation clavier.** Les puces (l.1600-1604) ne rendent que du texte alors que la base porte des `img` (les 10 entrées nouvellement marquées en ont toutes). Pour une app de champignons, la miniature est l'outil de désambiguïsation visuel n°1 — et les 10 entrées du guide injectées ont toujours `img:''` (aucune miniature pour les espèces du guide). Pas de navigation flèches non plus. *Fix :* `<img>` 24-28 px dans chaque puce (avec repli texte), flèches ↑/↓ + Entrée.

**P3-4 (passe 16, résidu) — l'état vide « générez les 5 classiques » est un mensonge doux.** l.2133 : « Aucune spécificité — ajoutez-en une ci-dessous ou générez les 5 classiques. » Or `ouvrirSheetIllu` injecte automatiquement les 5 spécificités par défaut à l'ouverture (l.2097-2100) — l'état vide est **inatteignable** et il n'existe aucun bouton « générer les 5 classiques ». *Fix :* supprimer la mention ou la remplacer par le vrai comportement.

## 7. Red flags par persona

- **Jonathan en forêt, une main, gants, fatigue** : les pires moments de la passe 16 sont partiellement refermés — « morille » répond en premier, « fausse chanterelle » sert le bon taxon toxique, « corne d'abondance »/« lactaire délicieux » répondent. **Pièges restants :** en doute sur une amanite vireuse (l'espèce MORTELLE), la première suggestion auto-remplit le latin d'un taxon différent (P2-2) ; en doute sur un pied-de-mouton, la suggestion sert un autre champignon que la fiche du guide (P2-3) ; et sur une feuille sale, Escape boucle sur la confirmation (P2-1).
- **Proche débutant (via export/import)** : le garde-fou couvre maintenant les 4 gestes ✅, les verdicts sont conditionnés au statut ✅. Le risque restant : choisir une suggestion Myco laisse le statut « ✅ Comestible » par défaut dans la feuille variété — l'autocomplétion encourage à badger comestible des espèces dont le statut est inconnu de la base (résidu 16E).
- **Utilisateur pressé / en doute** : le double-clic payant est protégé sur les 3 boutons de génération, avec état visuel désactivé ✅. Le piège : Escape qui boucle sur la confirmation d'une feuille sale (P2-1) — le geste « non, annule » le plus naturel devient une boucle.

## 8. Observations mineures

- `guide:true` : 11/21 corrects, 10 marqués à tort, 10 espèces du guide non marquées (dont 2 MORTELLES) — le claim du commit surestime le travail de données.
- Les 10 entrées du guide injectées ont toujours `img:''` — aucune miniature pour les suggestions des espèces du guide (résidu 16E).
- Double alerte orange dans la feuille variété (l.599, l.655) — résidu 16E.
- 🗑️ icon-only sans aria-label (l.1193 spots, l.1474 cueillettes) — résidu 16E.
- Champ recherche sans label visible (l.387, placeholder seul) — résidu 16E.
- Focus perdu sur les selects de filtre (re-rendu du DOM à chaque changement, l.1307-1315) — résidu 16E.
- `COULEURS_MOIS` (l.2367) : les 12 couleurs se répètent par blocs de 6 sans logique saisonnière lisible — résidu 16E.
- Barres de stats (`topRangs`) sans `role="progressbar"` — résidu 16E.
- Lightbox (l.2218-2238) : Escape + focus restore ✅, mais pas de focus trap — résidu 16E.
- `alt="photo"` générique sur les photos des zones (l.1141) — résidu 16E.
- `imageEnBase64` (l.1785) sans limite de taille — résidu 16E.
- « Dernière sortie » à 24 px dans une carte 2 colonnes (l.2383) : « 15 août 2026 » risque de déborder sur écran étroit — résidu 13E.
- `ouvrirMyco` (l.2215) : lien externe — hors-ligne, le navigateur affiche sa page d'erreur sans message de l'app — résidu 16E.
- `mois-col .lab` à 10,5 px (l.315) : contraste OK (noir sur crème) mais très petit — résidu 16E.
- `choisirNomMyco` (l.1607-1613) : le latin n'est auto-rempli que si le champ est vide — un latin partiel saisi reste, créant une incohérence nomFr/latin possible (résidu 15E).
- `chargerBaseMyco` (l.1566-1573) : échec de fetch silencieux (`baseMyco = []`) — les suggestions disparaissent sans message (résidu 15E).

## 9. Questions provocatrices

1. « Amanite vireuse » → amerivirosa premier, « chanterelle commune » → enelensis premier : le tie-break par longueur ignore `guide:true` sur les égalités exactes. À quoi sert le flag s'il ne peut pas départager le cas le plus dangereux ?
2. Escape sur une feuille sale ouvre la confirmation… et Escape ne peut plus la fermer (l.1049-1058 court avant la branche modale l.1060-1064). Le geste « non, annule » doit-il boucler ?
3. « Pied-de-mouton » sert Hydnum repandum alors que la fiche du guide est Hydnum umbilicatum. Quelle est la vérité de l'app : le nom d'affichage du guide ou le taxon de la base ?
4. 10 entrées marquées `guide:true` ne sont pas des espèces du guide, et 10 espèces du guide (dont 2 MORTELLES) ne sont pas marquées. Le marquage a-t-il été fait par script ou à la main ?
5. Les suggestions sont des puces texte alors que la base porte des miniatures. Pour une app de champignons, pourquoi la désambiguïsation visuelle n°1 n'est-elle toujours pas rendue ?
6. « générez les 5 classiques » (l.2133) : les 5 spécificités sont injectées automatiquement à l'ouverture (l.2097-2100). Cet état vide est-il jamais atteignable ?
7. « Gyromitre » place Gyromitra esculenta MORTELLE en 3e position derrière deux gyromitres non dangereux. « Visible » suffit-il pour l'espèce la plus mortelle du guide ?
8. La double alerte orange de la feuille variété (l.599, l.655) : laquelle est la gardienne, laquelle est le bruit ?

---

**Correctifs de la passe 16 vérifiés :** P2-2 bouton figé restauré sur tous les chemins de sortie ✅ (l.2150-2153, l.2189-2210) · P2-4 tri par exactitude/préfixe/guide/longueur ✅ **avec réserves** (morille exacte première ✅, gyromitre MORTEL 3e ⚠️, amerivirosa/enelensis toujours premiers sur égalité exacte ⚠️) · P2-5 21 entrées marquées `guide:true` ⚠️ (11/21 correctes) ; pied-de-mouton/fausse chanterelle/corne d'abondance/lactaire délicieux servis ✅ (pied-de-mouton = mauvais taxon ⚠️) · P3-1 CSS data-fs/data-f purgé ✅ (0 occurrence) · P3-2 toast myco dans la boucle ✅ (l.2203) · P3 Escape ferme les feuilles via le garde-fou ✅ **avec régression** (confirmation empilée, P2-1) · P3 libellé échec de sources distinct ✅ (l.1626, matche le message minusculisé de l.1863) · P3 style btn:disabled ✅ (l.148) · SW bump cqm-v40 ✅ (sw.js l.4).
**Claims v40 vérifiés :** 9 claims — 7 entièrement tenus, 1 partiel (P2-5 : marquage 11/21), 1 tenu avec réserve (P2-4 : 2 mauvais taxons premiers sur égalité exacte). Le libellé « 21 espèces du guide marquées guide:true » est inexact sur l'identité : 11 correctes, 10 marquées à tort, 10 non marquées.
**Non corrigés (passe 16) :** P3-4 (miniatures distantes — aggravé : les suggestions ne rendent aucune miniature, même locale) · P2-2/P2-3 (mauvais taxon premier / pied-de-mouton) · P3-3 (navigation clavier suggestions) · résidus micro-textes et accessibilité listés en section 8.
