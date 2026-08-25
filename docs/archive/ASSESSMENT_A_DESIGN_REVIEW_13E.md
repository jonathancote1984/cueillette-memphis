# Assessment A — Critique design (13e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2484 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v34)
**Méthode :** lecture statique seule (Assessment A), vérification des correctifs des passes 4-12 dans le code.
**Note :** rapport reconstitué depuis le résumé du subagent (le fichier original n'a pas été écrit avant l'échec du résumé B).

---

## 1. Verdict de spécificité design : **9/10**

Design **indissociable de son sujet** : le carnet de chasse automnal québécois est présent dans chaque décision — palette de septembre, zigzag d'en-tête, pois de fond, vignettes rayées ambre/blanc, inclinaisons « sourire du carnet », rebonds élastiques. La Règle du Trait Noir, la Règle du Rouge Mortel et la Règle du Décalage Net sont tenues du header au toast, sans dérive hors palette. C'est un système, pas un habillage. Le seul endroit où la spécificité vacille : le langage visuel ludique s'applique uniformément, y compris aux moments mortels (voir P2-3 et questions).

## 2. Scores heuristiques Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 4 | Rien de bloquant : badge, toasts, compteur n/5, « Analyse en cours… », scroll mémorisé. Seul bémol : toast à 2,2 s, court pour les messages d'erreur IA |
| 2 | Correspondance monde réel | 3 | Le filtre « ☠️ Ne pas manger » **exclut les 5 espèces mortelles** (P1) — contre-intuitif pour un cueilleur |
| 3 | Contrôle et liberté | 4 | Annuler partout, ← sticky, voile/poignée/Escape, garde-fou de saisie, analyse annulable, restauration sélective |
| 4 | Cohérence et standards | 3 | « Mon journal » (h2) vs « Cueillettes » (onglet) ; deux alertes orange dans la feuille variété ; verdict ⚠️ générique inadapté aux fiches mortelles (P0) ; aria-label FAB fixe « Ajouter » alors que l'icône change |
| 5 | Prévention des erreurs | 3 | Double confirmation, import versionné, matche flou+synonymes avec alerte ☠️ — mais le verdict-att « avant de consommer » sur fiche mortelle peut créer une fausse sécurité (P0) |
| 6 | Reconnaissance vs mémorisation | 4 | Autocomplétion, 10 puces de filtres visibles, recherche, tout est à l'écran |
| 7 | Flexibilité / efficacité | 4 | FAB contextuel, « Réessayer » dernière source, « Générer les manquantes », pré-remplissage IA |
| 8 | Esthétique minimaliste | 3 | Densité assumée mais réelle : vue Identifier = alerte rouge + bandeau orange + 2 boutons verts + recherche + 10 puces avant la liste ; fiche détail ~2000 px de scroll |
| 9 | Aide à la récupération d'erreurs | 4 | messageErreurIA en français, « série interrompue », repli copie du partage, fail-safe statut IA |
| 10 | Aide et documentation | 4 | Carte « Comment identifier » (verdicts expliqués + antipoison), notes partout, crédits Commons |

**Moyenne : 3,6/4** — très solide, tirée vers le bas par la cohérence des messages de sécurité et la densité.

## 3. Charge cognitive : modérée, deux points de friction

- **Bonne nouvelle** : une seule famille typographique, un seul vocabulaire de formes (carte/puce/bouton/feuille), modèles répétés partout. Le système s'apprend en 2 minutes.
- **Friction 1 — Vue Identifier** : 4 blocs de signal empilés (alerte rouge « Règle d'or » + bandeau clé orange + 2 boutons verts + 10 puces) avant le premier champignon. Quand la clé manque, deux alertes colorées se touchent.
- **Friction 2 — Fiche détail** : la galerie de 5 spécificités (photos 16:9 pleine largeur, ~1000 px) sépare l'alerte de sécurité du contenu textuel ; « ⚠️ Confusions possibles » — la section la plus critique — arrive après ~2000 px de défilement.
- **Double langage d'état actif** : puces statut actives = couleur sémantique + inclinaison ; puces saison actives = noir/crème. Lisible, mais deux grammaires pour « actif ».

## 4. Parcours émotionnel

Ouverture chaleureuse et réussie (header dégradé, formes flottantes, zigzag) → le guide accueille avec une alerte rouge permanente (« Règle d'or ») : la sécurité prime, mais le plaisir retombe d'un coup → la fiche hybride est le sommet émotionnel : cocher une spécificité (case olive + ✓ + texte barré) est une **récompense tactile** qui transforme la lecture en protocole → la cueillette enregistrée (toast ✅, badge qui monte) et les stats colorées ferment la boucle « panier plein ». Le point faible émotionnel : sur une fiche mortelle, la même coche olive « satisfaisante » récompense la confirmation du danger, et le verdict ⚠️ ambre adoucit le message dès qu'on décoche (P0, P2-3).

## 5. Forces

1. **Un design system tenu de bout en bout** — les quatre règles nommées (Trait Noir, Rouge Mortel, Décalage Net, Inclinaison) sont appliquées sans exception, du header au toast. C'est rare et c'est ce qui rend l'identité immédiatement reconnaissable.
2. **La fiche hybride est une idée de design remarquable** : checklist terrain + verdicts dynamiques ⚠️/✅/☠️ qui transforment un guide passif en protocole actif de vérification. Le compteur n/5, la coche barrée et les trois verdicts exclusifs forment un système de feedback cohérent et engageant.
3. **La sécurité est redondante sans être hystérique** : alerte en tête + verdict dynamique + antipoison répété + matche flou des synonymes + fail-safe IA + focus initial sur « Annuler ». Le rouge est exactement là où il doit être.

## 6. Problèmes prioritaires

**P0 — Le verdict ⚠️ (verdict-att) est dangereusement générique sur les fiches mortelles et toxiques.** À 0 critère : « Cochez chaque critère sur le champignon **avant de consommer** » ; après décoche : « Ne consommez pas **tant que tout n'est pas vérifié** ». Sur une fiche phalloïde, gyromitre ou vireuse, ce libellé sous-entend que la consommation devient possible une fois 5/5 cochés — contredisant l'alerte rouge en tête et le verdict ☠️ qui n'apparaît qu'à 5/5. Pire : décocher un critère fait **passer le message du rouge ☠️ au jaune ⚠️** alors que le danger réel n'a pas changé. Correctif : libellé conditionné au statut — pour mortel/toxique, le verdict-att doit rester rouge et dire « Espèce MORTELLE — ne jamais consommer, même si tous les critères semblent correspondre », quel que soit n. *(Corrigé en passe 13 — commit 32cebce.)*

**P1 — Le filtre « ☠️ Ne pas manger » (npas) exclut les mortelles.** `okF = e.statut === 'toxique' || e.statut === 'immangeable'` — les 5 espèces mortelles n'y figurent pas. Un cueilleur qui filtre « Ne pas manger » pour repérer le danger rate la catégorie la plus dangereuse. Soit inclure `mortel` dans npas, soit renommer le filtre (« ⚠️ Toxiques ») et ajouter une puce « Tout ce qui est dangereux ». *(Corrigé en passe 13.)*

**P1 — Hiérarchie de la fiche détail : les confusions sont reléguées en bas de ~2000 px de galerie.** L'ordre actuel : photo → nom → alerte → 5 cartes de spécificités (photos 16:9) → verdicts → saison/habitat → description → caractéristiques → confusions → boutons. La section la plus critique pour la sécurité (« ⚠️ Confusions possibles » : morille vs gyromitre, lépiote vs lépiote brunâtre) exige de défiler 5 photos pleine largeur. Recommandation : remonter « Confusions possibles » juste sous l'alerte, ou condenser la galerie en vignettes. *(Corrigé en passe 13.)*

**P2 — L'affordance de la coche est identique sur fiches comestibles et mortelles.** `.spec-carte.fait .spec-carre` passe en olive avec ✓ blanc et le titre se barre — la même « satisfaction » visuelle, même quand cocher confirme un danger mortel. Sur une fiche mortelle, cocher « Volve en sac au pied » récompense visuellement la confirmation du danger. Le plaisir Memphis devrait s'arrêter là où le danger commence : case rouge, pas de barré satisfaisant, sur les fiches non comestibles. *(Corrigé en passe 13.)*

**P2 — Surcharge de la vue Identifier.** Alerte rouge « Règle d'or » + bandeau clé orange + 2 boutons verts + recherche + 10 puces avant la liste. Le bandeau clé (information de configuration) n'a pas le poids d'une alerte de sécurité : le passer en note discrète libérerait la vue. *(Corrigé en passe 13.)*

**P3 — Nomenclature et placement.** L'onglet dit « Cueillettes », le h2 dit « Mon journal » ; le bouton « 🍄 Fiche MycoQuébec » de la feuille variété est noyé dans le bloc Photo alors que c'est une action d'information, pas de photo ; le badge rouge « 0 » du header (compteur) crée une fausse alarme visuelle quotidienne — le rouge est censé être réservé au danger. *(Corrigé en passe 13.)*

## 7. Red flags par persona

- **Jonathan en forêt, une main, gants, fatigue** : le verdict ⚠️ « avant de consommer » sur une fiche mortelle, lu rapidement en fin de journée, est le pire scénario — c'est le P0. La fiche longue (confusions en bas) aggrave : en forêt on ne défile pas 2000 px.
- **Proche débutant (via export/import)** : le filtre « Ne pas manger » qui exclut les mortelles — un débutant qui filtre pour éviter le danger croit avoir tout vu. Le matche flou protège la saisie, mais pas le filtrage.
- **Utilisateur pressé / en doute** : le parcours photo IA est bien sécurisé (fail-safe, « à vérifier »), mais « Réessayer » relance la même source sans offrir de changer de photo directement — il faut fermer et repartir.

## 8. Observations mineures

- Le toast (2,2 s) est court pour les messages d'erreur IA longs (« Limite de requêtes atteinte — patientez… »).
- Le verdict ☠️ est aussi utilisé pour toxique/immangeable (« ☠️ 5/5 critères vérifiés — non comestible »), diluant la spécificité du symbole mortel que les badges, eux, réservent au ☠️ MORTEL.
- Les suggestions d'autocomplétion sont des puces lourdes (bordure 3 px + ombre) — bruyantes pour un menu de suggestions, et sans navigation clavier flèches.
- Le champ recherche du guide n'a pas de label visible ni de bouton d'effacement ; « Aucun champignon trouvé » ne propose pas de réinitialiser les filtres.
- Le bouton 🗑️ icon-only des items (spots/cueillettes) n'a pas d'aria-label.
- La carte « Dernière sortie » (date longue « 12 août 2026 ») risque de déborder dans la grille 2 colonnes sur écran étroit.
- Le FAB a un aria-label fixe « Ajouter » alors que son contenu change (📍/＋).
- Le « pop » élastique s'applique aussi aux alertes mortelles — le rebond ludique et le grave se côtoient.
- Les puces saison actives (noir/crème) paraissent moins « actives » que les puces statut colorées — deux grammaires d'état.

## 9. Questions provocatrices

1. Le rouge est réservé au danger absolu… sauf le compteur de cueillettes du header, rouge en permanence, même à « 0 ». Un badge rouge quotidien n'use-t-il pas la vigilance qu'il est censé préserver ?
2. Le verdict ⚠️ dit « ne consommez pas tant que tout n'est pas vérifié » sur une fiche phalloïde. Feriez-vous confiance à un panneau « ne traversez pas tant que le feu n'est pas vert » posé sur une voie ferrée ?
3. La coche olive + texte barré récompense la confirmation du danger sur les fiches mortelles. Le « plaisir de la récolte » doit-il sourire quand il confirme la mort ?
4. « Ne pas manger » qui exclut les mortelles : si un proche demande « montre-moi tout ce qu'on ne mange pas », que lui montrez-vous ?
5. La fiche mortelle est-elle organisée là où le danger est maximal ? Les confusions — le vrai risque — sont en bas de 2000 px de photos de spécificités.
6. Le bandeau « Configurer la clé → » a le même poids visuel qu'une alerte de sécurité. Combien de signaux d'importance différente peut empiler la vue Identifier avant que le cueilleur ne lise plus rien ?

---

**Correctifs des passes 4-12 vérifiés et tenus** (verdicts dynamiques, matche flou+synonymes, AbortController, import versionné, focus trap, réindexation, MycoQuébec, helpers unifiés, etc. — confirmés dans le code).
**Note de suivi** : les problèmes ci-dessus ont tous été corrigés au commit `32cebce` (SW cqm-v35) — P0 verdict-att conditionné, P1 filtre npas+mortelles, P1 confusions remontées, P2 coche rouge dangereux, P2 bandeau clé discret, P3 nomenclature+badge masqué à 0.
