# Assessment A — Critique design (16e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2579 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v39) · **Base :** `img/mycoquebec.json` (3936 entrées, 3392 nomFr)
**Méthode :** lecture statique seule (Assessment A), vérification des 8 claims du commit `3e4ed78` (v39) dans le code ET sur les données (base JSON interrogée avec le prédicat réel de l'app).
**Note :** 6 claims sur 8 sont **entièrement tenus**, 2 sont **partiellement tenus** (P2-5 autocomplétion : les 3 cas nommés répondent, mais 4 espèces du guide restent muettes ou mal servies et le mauvais taxon « amerivirosa » gagne toujours ; P3-1 : 2 règles CSS orphelines sur 7 restent). Le fix P2-2 a introduit une **régression** : le bouton « Générer les manquantes » se fige définitivement quand toutes les images existent déjà (return sans restauration du disabled).

---

## 1. Verdict de spécificité design : **9/10**

Inchangé depuis la passe 15 : palette de septembre, zigzag, pois, vignettes rayées, inclinaisons, Règle du Trait Noir, Règle du Rouge Mortel, Règle du Décalage Net tenues du header au toast. Les correctifs v39 (boutons désactivés, garde-fou complet, toast myco) ne touchent pas à la grammaire visuelle. Le seul endroit où la spécificité vacille reste le même : le langage ludique s'applique uniformément, y compris aux moments mortels (rebond élastique des alertes rouges).

## 2. Scores heuristiques Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 3.5 | Boutons de génération désactivés + « ⏳ En cours… » sur les 3 chemins (pattern e-generer étendu) ✅ ; toast long 4,5 s ✅ — **mais régression** : « Générer les manquantes » reste désactivé pour toujours si toutes les images existent déjà (l.2170, return sans restauration) |
| 2 | Correspondance monde réel | 3.5 | « amanite phalloïde », « amanite panthère », « paxille enroulé » répondent enfin ✅ — mais « pied-de-mouton » → zéro suggestion, « fausse chanterelle » → un taxon différent, « morille »/« gyromitre » → l'espèce du guide coupée par slice(0,6), et « amanite vireuse » suggère toujours « Amanita amerivirosa » en premier (latin erroné auto-rempli) |
| 3 | Contrôle et liberté | 4 | Annuler partout, ← sticky, voile/poignée/Annuler → garde-fou, analyse annulable, restauration sélective, ordre des images configurable |
| 4 | Cohérence et standards | 3.5 | Toast « Photo MycoQuébec 🍄 » ✅, FAB aria-label dynamique ✅, MycoQuébec pleine largeur ✅ — résidus : double alerte orange, 🗑️ sans aria-label, « ⚠️ Erreur IA : Aucune image trouvée… » pour un échec de sources |
| 5 | Prévention des erreurs | 3.5 | Poignée → garde-fou ✅, statut/prudence dans le test ✅ — le garde-fou couvre enfin les 3 gestes (poignée, voile, Annuler) ; Escape ne ferme toujours aucune feuille (résidu) |
| 6 | Reconnaissance vs mémorisation | 4 | Autocomplétion (2 systèmes), recherche, tout est à l'écran |
| 7 | Flexibilité / efficacité | 4 | FAB contextuel, « Réessayer » dernière source, « Générer les manquantes », ordre des images (6 combinaisons, persistant) |
| 8 | Esthétique minimaliste | 3 | Feuille variété toujours dense : 8 champs + 4 boutons photo + 2 alertes orange empilées |
| 9 | Aide à la récupération d'erreurs | 4 | messageErreurIA en français, « série interrompue », repli copie du partage, fail-safe statut IA |
| 10 | Aide et documentation | 4 | Carte « Comment identifier » (sans « 5/5 » en dur ✅), notes partout, crédits Commons, libellé explicite du paramètre Ordre des images |

**Total : 37/40** — record (13E : 36/40), hausse honnête de 2,5 : les deux gros problèmes de la passe 15 (garde-fou contourné par la poignée, boutons de génération sans feedback) sont **vérifiés corrigés dans le code**, et les 3 cas nommés de l'autocomplétion répondent. La hausse est partiellement plafonnée par le fix P2-5 incomplet (4 espèces du guide muettes, mauvais taxon premier) et par la régression du bouton figé (P2-2). Profil : très solide sur la sécurité et le contrôle, encore faible sur la qualité des suggestions (tri binaire, slice(0,6)) et les micro-messages.

## 3. Charge cognitive : modérée, inchangée

- **Bonne nouvelle** : les 2 selects de filtres tiennent, l'autocomplétion couvre les 3 cas les plus dangereux nommés en passe 15.
- **Friction 1 — Feuille variété** : 8 champs + 4 boutons photo + 2 alertes orange empilées (l.600 et l.656) avant les boutons d'action. La deuxième alerte (« 🔑 La clé Gemini se configure dans Paramètres ») reste redondante avec le toast PAS_DE_CLE et le bandeau de la vue guide.
- **Friction 2 — Suggestions Myco** : puces lourdes (bordure 3 px + ombre) pour un menu de suggestions, sans navigation clavier flèches — même constat que les passes 13-15, maintenant doublé par le problème de tri (voir P2-4).

**Checklist 8 items :** 1 Focus unique ✅ · 2 Chunking ≤ 4 ✅ · 3 Regroupement visuel ✅ · 4 Hiérarchie ✅ · 5 Une chose à la fois ✅ · 6 Choix minimaux ≤ 4 ❌ (feuille variété : 8 champs + 4 boutons photo + 2 alertes) · 7 Mémoire de travail ✅ · 8 Divulgation progressive ✅. **1 échec sur 8.**

## 4. Voyage émotionnel

Ouverture chaleureuse (header dégradé, formes flottantes, zigzag) → le guide accueille avec l'alerte rouge « Règle d'or » : la sécurité prime → la fiche hybride reste le sommet : cocher une spécificité est une récompense tactile, et sur les fiches mortelles la coche rouge sans barré arrête la satisfaction là où le danger commence → **le creux de la passe 15 est refermé** : « amanite phalloïde » répond enfin dans l'autocomplétion — le moment le plus angoissant du cueilleur (doute sur LE champignon le plus mortel) est maintenant servi → **nouveaux creux** : taper « pied-de-mouton » ou « fausse chanterelle » (noms du guide) donne zéro suggestion ou un taxon différent ; « amanite vireuse » propose toujours « Amanita amerivirosa » en premier ; et cliquer « Générer les manquantes » quand tout est généré fige le bouton pour la session. Le point faible émotionnel reste le même : le rebond élastique s'applique aussi aux alertes mortelles.

## 5. Forces

1. **Un design system tenu de bout en bout** — les quatre règles nommées (Trait Noir, Rouge Mortel, Décalage Net, Inclinaison) sont appliquées sans exception, du header au toast, y compris dans les correctifs v39. C'est un système, pas un habillage.
2. **La fiche hybride est une idée de design remarquable** — checklist terrain + verdicts dynamiques ⚠️/✅/☠️ qui transforment un guide passif en protocole actif. Le fix 13E (coche rouge sans barré, verdict-att rouge conditionné) tient toujours.
3. **Le garde-fou de fermeture est enfin complet** — poignée (l.1007-1010), voile (l.1003-1006) et bouton Annuler (l.1649) passent tous par `fermerFeuilleVariete`, et `formulaireEspeceSale` teste maintenant les 7 champs texte + la photo + **le statut et la prudence** (l.1650-1653). Changer « ✅ Comestible » → « ☠️ MORTEL » puis fermer par n'importe quel geste déclenche la confirmation. Le pattern « vérifier chaque geste séparément » du rapport 14E est enfin tenu.
4. **Le pattern anti-double-clic est uniforme** — `e-generer` (l.1724-1747), `genererIllu` (l.2126-2143) et `illu-toutes` (l.2163-2188) désactivent leur bouton avec un libellé « ⏳ En cours… » et le restaurent sur succès, erreur et PAS_DE_CLE. Le double-clic payant est refermé — avec une exception (voir P2-5 nouveau).
5. **La sécurité reste redondante sans être hystérique** — alerte en tête + verdict dynamique + antipoison répété + matche flou des synonymes + fail-safe IA + focus initial sur « Annuler ». Le rouge est exactement là où il doit être.

## 6. Problèmes prioritaires

**P2-2 (passe 15) — ✅ CORRIGÉ ET VÉRIFIÉ, avec une régression.** `genererIllu(i, btn)` (l.2126-2143) et `illu-toutes` (l.2163-2188) désactivent leur bouton (`btn.disabled = true` + « ⏳ En cours… ») et le restaurent sur tous les chemins de sortie du try/catch. Le pattern `e-generer` est étendu aux deux autres boutons. **Régression :** dans `illu-toutes`, le chemin `if (!manquantes.length) { toast('Toutes les spécificités ont déjà une image ✨'); return; }` (l.2170) sort **sans restaurer le bouton** — il reste désactivé pour toute la session (le HTML de la feuille n'est pas re-rendu à la réouverture, `ouvrirSheetIllu` ne touche pas au bouton). Même mécanisme dans `genererIllu` : `if (!e) return;` (l.2129) et `if (!it) return;` (l.2131) laissent le bouton figé (cas limite). *Fix :* restaurer `btn.disabled = false; btn.textContent = '✨ Générer les manquantes';` avant chaque return, ou centraliser la restauration dans un `finally`/helper.

**P2-3 (passe 15) — ✅ CORRIGÉ ET VÉRIFIÉ.** La poignée route vers `fermerFeuilleVariete` quand la feuille variété est ouverte (l.1007-1010), et `formulaireEspeceSale` inclut `e-statut` et `e-prudence` (l.1650-1653). Les trois gestes de fermeture (poignée, voile, Annuler) passent par le garde-fou. Résidu : Escape ne ferme toujours aucune feuille (l.1049-1064 ne couvre que les modales) — P3.

**P2-4 (passe 15) — ✅ CORRIGÉ ET VÉRIFIÉ.** Le repli IA est conditionné à l'ordre choisi : `if (ordre.includes('ia'))` (l.1838), sinon `throw new Error('Aucune image trouvée dans les sources choisies (' + ordre.join(', ') + ')')` (l.1841) — échec honnête, plus d'appel Gemini hors ordre ni de toast « ajoutez votre clé » pour une source non demandée. *Résidu P3 :* le message passe par `messageErreurIA` (l.2141) qui ne matche aucun pattern → affiché « ⚠️ Erreur IA : Aucune image trouvée… — réessayez. » — ce n'est pas une erreur IA, le libellé trompe.

**P2-5 (passe 15) — ⚠️ PARTIELLEMENT CORRIGÉ — les 3 cas nommés répondent, mais 4 espèces du guide restent muettes ou mal servies, et le mauvais taxon gagne toujours.** Vérifié sur la base (3936 entrées) avec le prédicat réel de l'app (l.1571-1578) :
- ✅ « amanite phalloïde » → « Amanite phalloïde » (Amanita phalloides) · « amanite panthère » → « Amanite panthère » (Amanita pantherina) · « paxille enroulé » → « Paxille enroulé » (Paxillus involutus).
- ❌ « pied-de-mouton » → **zéro suggestion** (l'entrée existante s'appelle « Hydne ombiliqué ») — le nom du guide est muet.
- ❌ « fausse chanterelle » → suggère « Fausse chanterelle de Prescot » (Cantharellopsis prescotii) — un taxon **différent** de la fausse chanterelle toxique du guide (Hygrophoropsis aurantiaca), avec auto-remplissage du latin erroné.
- ❌ « morille » et « gyromitre » → l'espèce du guide (« Morchella spp. », « Gyromitra commun » = Gyromitra esculenta **MORTELLE**) est **coupée par `slice(0, 6)`** : les 12 entrées injectées sont en fin de base, le tri (l.1573-1577) ne priorise que nomFr-vs-latin (binaire), pas l'exactitude du match — « Morille » exacte arrive derrière « Cératiomyxie morille », « Morille à pied ponctué », etc.
- ⚠️ « amanite vireuse » → 2 suggestions, **« Amanite vireuse » (Amanita amerivirosa) toujours première** (entrée existante avec img, avant l'injectée « Amanita virosa » sans img) — l'auto-remplissage du latin erroné dénoncé en passe 15 n'est pas adressé. Même mécanisme pour « chanterelle commune » → « Cantharellus enelensis » premier.
- ⚠️ Les 12 entrées injectées ont `img:''` — les suggestions des espèces du guide n'ont **aucune miniature**, contrairement aux entrées existantes.

*Fix :* (1) trier par longueur de match (le nomFr le plus court d'abord) ou par égalité exacte avant inclusion ; (2) insérer les 21 espèces du guide en **tête** de base (ou les fusionner avec les entrées existantes : garder le nomFr du guide et la miniature existante) ; (3) pour « pied-de-mouton », ajouter le nom du guide comme nomFr de l'entrée « Hydne ombiliqué » ou injecter une entrée dédiée.

**P3-1 (passe 15) — ⚠️ PARTIELLEMENT CORRIGÉ.** Les 5 règles `data-f="comestible|prudence|npas|toxique|mortel"` sont supprimées (diff v39), mais `data-fs` (l.167) et `data-f="tous"` (l.168) restent — or plus aucun élément `data-f`/`data-fs` n'existe dans le HTML/JS (les puces ont été remplacées par des selects en v36). Le claim « CSS mort purgé » est partiel. *Fix :* supprimer les lignes 167-168.

**P3-2 (passe 15) — ✅ CORRIGÉ ET VÉRIFIÉ.** Toast « Photo MycoQuébec 🍄 » pour `res.source === 'myco'` (l.2139). *Résidu P3 :* dans la boucle `illu-toutes` (l.2180), seul `wikimedia` a un toast de succès — une photo myco trouvée dans la boucle n'a aucune confirmation (le toast de progression reste, puis rien).

**P3-3 (passe 15) — ✅ CORRIGÉ ET VÉRIFIÉ.** FAB aria-label dynamique (l.984 : « Ajouter un spot » / « Ajouter une cueillette »), toast long 4,5 s pour les messages > 60 caractères (l.742), « 🍄 Fiche MycoQuébec » pleine largeur (l.651-653), bouton « ↩️ Réinitialiser les filtres » dans l'état vide (l.1335 + `reinitialiserFiltres` l.1315-1321 qui remet recherche + les 2 selects). Résidus non adressés (P3) : 🗑️ icon-only sans aria-label (l.1184 spots, l.1465 cueillettes) ; double alerte orange dans la feuille variété (l.600, l.656) ; champ recherche sans label visible (l.388) ; suggestions (cueillette + variété) sans navigation clavier flèches (l.1474, l.1575) ; focus perdu sur les selects de filtre (re-rendu du DOM à chaque changement, l.1308) ; Escape ne ferme pas les feuilles.

**P3-4 (passe 15) — ❌ NON CORRIGÉ.** Miniatures MycoQuébec distantes (URLs mycoquebec.org) — et les 12 entrées injectées n'ont même pas de miniature (`img:''`). Hors-ligne dès la première utilisation, les suggestions des espèces du guide n'affichent aucune image. *Fix :* documenter la limite, ou télécharger les miniatures dans `img/`.

**P3-5 (passe 15) — ✅ CORRIGÉ ET VÉRIFIÉ.** « Tous les critères vérifiés sur une espèce mortelle » (l.467) — plus de « 5/5 » en dur à côté du compteur dynamique.

## 7. Red flags par persona

- **Jonathan en forêt, une main, gants, fatigue** : le pire moment de la passe 15 (taper « amanite phalloïde » → silence) est **corrigé** — le champignon le plus mortel répond. Nouveaux pièges : en doute sur un pied-de-mouton ou une fausse chanterelle, il tape le nom du guide → zéro suggestion ou un taxon différent (P2-4) ; et après une session d'illustrations, cliquer « Générer les manquantes » quand tout est fait fige le bouton pour la session (P2-5 nouveau).
- **Proche débutant (via export/import)** : le garde-fou couvre maintenant tous les gestes de fermeture ✅, les verdicts sont conditionnés au statut ✅. Le risque restant : choisir une suggestion Myco (ex. « Fausse chanterelle de Prescot ») laisse le statut « ✅ Comestible » par défaut dans la feuille variété — l'autocomplétion encourage à badger comestible des espèces dont le statut est inconnu de la base.
- **Utilisateur pressé / en doute** : le double-clic payant est protégé sur les 3 boutons de génération ✅. Le piège : le bouton figé (P2-5 nouveau) et le message « ⚠️ Erreur IA : Aucune image trouvée… » qui oriente vers un problème de clé alors que c'est un échec de sources (P3).

## 8. Observations mineures

- `data-fs` et `data-f="tous"` orphelins (l.167-168) — résidu du claim P3-1.
- Les 12 entrées injectées en fin de base avec `img:''` — aucune miniature pour les suggestions des espèces du guide.
- `btn:disabled` sans style visuel : un bouton désactivé garde l'apparence d'un bouton actif (seul le libellé change) — l'état n'est pas lisible au premier coup d'œil.
- Le tri des suggestions (l.1573-1577) est binaire (nomFr vs latin) : « Morille » exacte arrive derrière « Cératiomyxie morille » (un myxomycète) — l'ordre interne est celui de la base.
- `choisirNomMyco` (l.1586-1592) : le latin n'est auto-rempli que si le champ est vide — un latin partiel saisi reste, créant une incohérence nomFr/latin possible (résidu 15E).
- `chargerBaseMyco` (l.1557-1564) : échec de fetch silencieux (`baseMyco = []`) — les suggestions disparaissent sans message (résidu).
- `mois-col .lab` à 10,5 px (l.316) : contraste OK (noir sur crème, 14:1) mais très petit (résidu).
- `COULEURS_MOIS` (l.2344) : les 12 couleurs se répètent par blocs de 6 sans logique saisonnière lisible (résidu).
- Barres de stats (`topRangs`, l.2345-2351) sans `role="progressbar"` (résidu).
- Lightbox (l.2195-2215) : Escape + focus restore ✅, mais pas de focus trap (résidu).
- `alt="photo"` générique sur les photos des zones (l.1132) (résidu).
- `imageEnBase64` (l.1763-1771) sans limite de taille (résidu).
- « Dernière sortie » à 24 px dans une carte 2 colonnes (l.2360) : « 15 août 2026 » risque de déborder sur écran étroit (résidu 13E).
- `ouvrirMyco` (l.2192-2194) : lien externe — hors-ligne, le navigateur affiche sa page d'erreur sans message de l'app (résidu).

## 9. Questions provocatrices

1. Les 12 espèces injectées sont en fin de base, et le tri ne priorise que nomFr-vs-latin, pas l'exactitude : « morille » et « gyromitre » (l'espèce MORTELLE du guide) sont coupées par `slice(0, 6)`. Pourquoi injecter des données sans vérifier qu'elles apparaissent dans les résultats ?
2. « Amanite vireuse » suggère toujours « Amanita amerivirosa » en premier — le latin auto-rempli reste celui d'un taxon différent du guide. Le fix a ajouté la bonne entrée, mais le mauvais taxon gagne toujours. Qui vérifie l'ordre des suggestions ?
3. « Fausse chanterelle » suggère « Fausse chanterelle de Prescot » (Cantharellopsis prescotii) — un champignon différent de la fausse chanterelle toxique du guide. Une suggestion qui auto-remplit un latin erroné est-elle pire que le silence ?
4. Le bouton « Générer les manquantes » se fige définitivement si toutes les images existent déjà (return sans restauration du disabled). Le fix anti-double-clic a-t-il été testé sur tous les chemins de sortie ?
5. Les 12 espèces injectées n'ont pas de miniature (`img:''`). La promesse « 100 % hors-ligne » du PRODUCT.md s'arrête-t-elle aux données, ou aux images ?
6. Le garde-fou couvre maintenant poignée, voile et Annuler — mais Escape ne ferme toujours aucune feuille. Pourquoi le geste clavier le plus standard reste-t-il le seul non couvert ?
7. Choisir une suggestion Myco (ex. « Gyromitre à spores rondes ») laisse le statut « ✅ Comestible » par défaut dans la feuille variété. L'autocomplétion encourage-t-elle à badger comestible des espèces dont la base ne dit rien ?
8. Le message « Aucune image trouvée dans les sources choisies » est affiché comme « ⚠️ Erreur IA : … ». Un échec de sources est-il une erreur IA ?
9. Les 2 règles CSS orphelines (`data-fs`, `data-f="tous"`) : le claim « CSS mort purgé » est-il vérifié avant d'être écrit dans le commit ?
10. Le toast de progression « Génération de X… (10-20 s) » meurt à 2,2 s — le bouton « ⏳ En cours… » compense, mais pourquoi ne pas allonger le toast de progression lui-même ?

---

**Correctifs de la passe 15 vérifiés :** P2-2 boutons désactivés (pattern e-generer étendu) ✅ **avec régression** (illu-toutes figé si tout est généré, l.2170) · P2-3 poignée → garde-fou + statut/prudence dans le test ✅ · P2-4 repli IA conditionné à l'ordre ✅ (résidu : libellé « Erreur IA ») · P2-5 3 cas nommés répondent ✅ **mais 4 espèces du guide muettes/mal servies + amerivirosa premier** ⚠️ · P3-1 5/7 règles data-f purgées ⚠️ (data-fs et data-f="tous" restent) · P3-2 toast « Photo MycoQuébec 🍄 » ✅ (résidu : pas de toast myco dans la boucle) · P3-3 FAB aria-label + toast 4,5 s + MycoQuébec pleine largeur + réinitialiser filtres ✅ · P3-5 carte aide sans « 5/5 » ✅ · SW bump cqm-v39 ✅ (sw.js l.4).
**Claims v39 vérifiés :** 8 claims — 6 entièrement tenus, 2 partiellement (P2-5, P3-1). Le libellé « 21 espèces injectées » est inexact sur les données : 12 injectées, 9 déjà présentes (21/21 présentes par latin, 17/21 répondent par nom français exact).
**Non corrigés (passe 15) :** P3-4 (miniatures distantes — aggravé : les injectées n'ont aucune miniature).
