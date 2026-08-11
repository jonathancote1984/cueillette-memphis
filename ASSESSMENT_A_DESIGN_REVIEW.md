# Assessment A — Critique design : Cueillette Québec — édition Memphis (6e passe)

**Cible :** `index.html` (2334 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **Méthode :** lecture statique (Assessment A), Nielsen ×10, spécificité, charge cognitive, parcours émotionnel, personas.

---

## 1. Verdict de spécificité design

**Conceptuel : ~95 %.** Le vocabulaire est celui du domaine, pas d'un dashboard générique : « coins secrets », « MORTEL ☠️ », « centre antipoison 1-800-463-5060 », « on ne mange pas », « alvéoles en nid d'abeille », « volve en sac », « anneau coulissant », saisons de cueillette (morilles au printemps), unités kg/lb, météo emoji, espèces du Québec (chanterelle, cèpe, pied-de-mouton, gyromitre). Aucune abstraction générique.

**Visuel : ~90 %.** Le langage Memphis est exécuté au pixel près : bordure noire 3 px sur toute surface colorée, coins cassés (18/5 px), ombres dures sans flou (3–6 px), zigzag d'en-tête, pois crème au fond, rayures ambre/blanc des vignettes, titres inclinés −1 à −2°, pastilles pilules, Fredoka partout, rebonds élastiques. Un screenshot sans texte crierait « carnet ludique de champignons » — les emojis champignon, le logo à pois et le zigzag ne trompent pas.

**Test du screenshot sans texte :** réussi des deux axes. **Verdict : interface hautement spécifique, cohérente avec la North Star « La Récolte ».**

---

## 2. Évaluation holistique

### Hiérarchie visuelle
- Échelle documentée respectée : display 21 px (L45), titre-vue 20 px (L103), feuille 18 px (L284), corps 16 px, label 13 px, meta 12.5 px. Pas d'uppercase forcé.
- **Dérive ponctuelle : `font-weight:900`** sur `.spec-num` (L253) et `.spec-carre` (L256) — hors échelle 400–700 documentée (« jamais de graisse inférieure à 400 », DESIGN.md L235 ; la borne haute n'est pas explicite, mais 900 casse la discipline).
- Styles `inline` massifs dans les gabarits JS (ex. `style="margin:0 0 6px"` sur les h3 des cartes Stats L401-403, `style="display:flex;..."` L381, L1276) : la hiérarchie des titres de carte repose sur du inline plutôt que sur des classes — fragile, mais visuellement stable.
- Triple encodage de l'onglet actif (zigzag ambre + icône relevée 4 px + couleur propre) : redondance bien dosée (L75-85).
- Positions des tops stats colorées par `nth-child(4n+2/3/4)` (L305-307) : cycle décoratif sans sémantique (la 2e place est bleue, la 1re jaune) — pure ornementation, acceptable en Memphis mais arbitraire.

### Architecture de l'information
- 5 onglets = 5 domaines, labels stables (« Cueillettes » = « Mon journal » en titre de vue, L393 — légère variation assumée).
- **Filtres du guide incomplets face au vocabulaire des badges** : 4 puces (Tous/Comestibles/Toxiques/Mortels, L1204) pour 5 statuts + `prudence` (L887-893). Conséquences : (a) « Toxiques » exclut les « Immangeable » (le bolet amer n'apparaît sous aucun filtre « ne pas manger ») ; (b) les espèces « Comestible — prudence » (morille, amanite rougissante) se cachent sous « Comestibles » sans distinction au niveau liste ; (c) aucun filtre « Prudence ». Pour un outil dont le principe n°1 est « la sécurité prime », la segmentation par sécurité est la moins complète.
- Restauration sélective, masquage, suppression : flux complets et cohérents (L1005-1032, L1497-1524).

### Adéquation émotionnelle
- Concept ↔ exécution alignés : le ludisme Memphis sert un carnet personnel chaleureux, pas un jeu ; les alertes de sécurité restent sobres et non négociables.
- **Valence à surveiller** : le verdict ✅ vert (`verdict-ok`, olive) s'affiche aussi sur les fiches MORTELLES quand les 5 critères sont cochés — le texte « restez prudent » (L1283) tempère, mais un vert de validation sur une fiche mortelle est un choix sémantique risqué.
- Erreurs IA brutes exposées : `⚠️ IA indisponible (Failed to fetch)` (L1567), `Génération impossible : ...` (L1947), `Échec sur « ... » : ... — série interrompue` (L1979) : message technique anglais dans un carnet chaleureux — rupture de ton.

### Découvrabilité
- Bandeau « Configurer la clé → » avec bouton d'action direct (L2001-2004) : excellent pattern d'onboarding.
- FAB contextuel (📍 Spots / ＋ ailleurs, masqué en Stats/détail/Paramètres, L926-928) : clair.
- Fiches hybrides : la feature phare n'a pas d'explication dédiée au premier lancement ; seule la micro-phrase « Vérifiez chaque critère sur le champignon » (L1276) l'introduit. Suffisant pour un outil personnel, mais un premier passage en forêt ne comprend pas immédiatement le flux cocher → compteur → verdict.

### Composition
- Colonne unique 640 px, grilles 2 colonnes pour paires de boutons, cartes espacées 16 px : conforme (DESIGN.md L169). Rythme 4/8/12/16/24 respecté.
- Barre de mois : 12 colonnes flexibles dans une carte — les tiges de 4 px minimum pour les mois vides (L2150) créent une fausse lecture de « petite récolte » là où il n'y a rien ; le gris `#D8C9AC` distingue, mais la hauteur résiduelle est un artefact visuel.

### Typographie
- Fredoka unique, repli système, pas d'uppercase forcé ✓. Interlignages 1.65/1.5/1.4 conformes.
- `letter-spacing:.2px` sur le display (L45) ✓ conforme DESIGN.md.
- Poids 900 hors échelle (voir plus haut). Tailles arbitraires inline (13.5 px, 15.5 px…) : tolérées par la doc mais nombreuses.

### Couleur
- Palette respectée : aucun vert/bleu/rouge hors palette détecté ; les dérives documentées (onglets actifs, dégradé header, fonds d'alertes, barre vide) sont présentes telles que prévues (L81-85, L38, L208-218, L2150).
- **Règle du Rouge Mortel tenue** : le rouge n'apparaît que danger/destruction/compteur (documenté).
- **Règle du Trait Noir tenue** : toute surface colorée porte sa bordure 3 px (vérifié sur stat-cartes, pastilles, puces, rang, barres).
- Contrastes (calculés, luminances relatives sRGB) :
  - Noir sur blanc 15.87:1, noir sur crème 14.08:1, noir sur ambre 7.59:1, noir sur olive 4.61:1, blanc sur rouge 6.07:1, blanc sur orange 4.67:1, blanc sur terracotta 4.95:1, blanc sur cuir 5.45:1 — **AA partout**.
  - Onglets actifs colorés sur fond blanc : 4.66–5.74:1 — AA ✓ (les 5 couleurs passent).
  - **Échecs AA (12 px, graisse 700) :** libellés des stat-cartes 2 et 4 — `blanc à 80 %` sur cuir = **4.15:1** (L293) et sur terracotta = **3.74:1** (L295) — sous le seuil 4.5:1. Fix : opacité → .9/.95 ou blanc pur.
  - Coche ✓ du `.spec-carre.fait` : blanc sur olive **3.44:1** — passe comme graphique non-textuel (≥3:1, WCAG 1.4.11), à noter.
  - Meta `.85` (L136) = 10.16:1, info-gps `.75` = 6.71:1, ligne-latin `.65` = 4.93:1 : tous les correctifs de contraste de la 5e passe tiennent.

### Accessibilité
- Correctifs 5e passe vérifiés et tenus : `role="button"` + `tabindex="0"` sur puces filtres (L1208, L1211), puces espèces spot (L1135), items guide (L1239), cartes spécificités (L1278) ; handler clavier Enter/Espace global (L954-959) ; `aria-live="polite"` sur toast (L681) ; `prefers-reduced-motion` (L337) ; focus ambre 3 px (L178) ; cibles ≥44 px (btn-petit L154, puces L158, btn-suppr-item L122) ; boites `role="alertdialog"/"dialog"` + aria-modal + aria-labelledby/describedby (L464, L474).
- **Trous restants :**
  - Aucune modale n'a de **focus trap** ni de gestion **Échap** ; le focus initial est posé (Annuler, L975) mais on peut tabber derrière le voile.
  - **Lightbox** (L1987-1994) : créée en div, pas de `role="dialog"`, pas d'Échap, pas de focus ; le déclencheur « 🔍 Agrandir » (L1279) est un span non focusable (l'img a un onclick avec stopPropagation mais ni role ni tabindex) ; l'image de détail `cursor:zoom-in` (L1295) même problème.
  - Nav à onglets : pas de `role="tablist"`/`aria-current`/`aria-selected` (L452-458) — les boutons restent focusables, mais l'état actif n'est pas annoncé.
  - Suggestions d'autocomplétion (L1362-1366) : accessibles à la souris/au clic, pas de navigation flèches.

### États
- Vides honnêtes avec guidance (« Appuyez sur le bouton rose… » L1075, L1331) ✓. Aucun « tout va bien » codé en dur.
- Verdicts : **le correctif P0-1 tient** — à 0 critère ET après décoche totale, `nbFaits (0) < items.length` → `verdict-att` ouvert avec « Rien n'est encore vérifié » (L1284, L1322-1324) ; le verdict ✅ ne s'ouvre qu'à égalité parfaite.
- Erreurs : toasts sans guidance de récupération pour l'IA (juste le code d'erreur brut).
- **Bug d'état latent (checklist indexée par position)** : `Etat.checklist[id].faits` est un tableau indexé par l'index d'item (L1315-1318, L1273). `retirerIllu(i)` fait un `splice` des items (L1951-1952) **sans toucher aux faits** → toutes les coches des critères suivants se réassignent silencieusement au mauvais critère. Ex. : cocher Chapeau+VOLVE sur une phalloïde, retirer le critère n°2 → la coche « VOLVE » saute sur « Pied » (lames blanches) et le verdict peut basculer à tort.

### Copy
- Française du Québec, chaleureuse et précise (« goûter une miette et cracher », « un seul spécimen suffit »). Ton constant.
- **Double alerte redondante** dans la feuille variété : deux bandeaux orange quasi identiques « clé Gemini » à 52 lignes d'écart (L576 et L628) — bruit visuel dans un formulaire déjà long.
- Terminologie stable : « Masquer/Restaurer/Supprimer », « Enregistrer », cohérents partout.
- Promesses tenues : l'export télécharge réellement un JSON (L2164-2175) — aucun « Ctrl+P » ni promesse creuse.

### Cas limites
- **Export/import incomplet : la checklist est absente du JSON.** L'export (L2165) embarque spots, cueillettes, especesCustom, illustrations, cachees, supprimees — **pas le store `checklist`** (pourtant persisté en IndexedDB, L732). L'import (L2177-2201) ne la lit pas non plus. Or la note d'export promet « il sert aussi de transfert vers un autre téléphone » (L413) : toutes les vérifications terrain (verdicts ⚠️/✅) sont silencieusement perdues au transfert.
- Suppression d'une espèce du guide : les cueillettes liées gardent leur badge via `especeId` archivé (L1336-1339) — excellent.
- Import : aucune validation de version (tout JSON avec `spots`/`cueillettes` arrays est accepté, L2181) — un export v3 ou un fichier corrompu passe sans avertissement de version.
- Filtres saison : `saisonDe` (L1216-1223) classe par le premier mois mentionné — « Juillet à octobre » (chanterelle) n'apparaît qu'en été, jamais en automne ; « Septembre à décembre » (pleurote) uniquement en automne, jamais en hiver. Segmentation discutable pour un outil saisonnier.

---

## 3. Évaluation de charge cognitive (8 items)

| # | Item | Verdict | Preuve |
|---|------|---------|--------|
| 1 | Focus unique (une tâche par écran) | ✅ | Feuilles bottom-sheet mono-objectif ; une vue = une tâche (l'onglet Stats cumule stats + sauvegarde, mitigé) |
| 2 | Chunking ≤ 4 | ❌ | Fiche détail : 5 cartes spécificités (L1277-1282) + 4-6 caractéristiques + 2 verdicts + 4 boutons — groupes de 5 et plus |
| 3 | Regroupement visuel | ✅ | Cartes cerclées, sections `guide-sujet`, grille2, stat-grille ; espaces 16 px |
| 4 | Hiérarchie | ✅ | 6 niveaux d'échelle cohérents (21→12.5 px) ; dérive 900 ponctuelle |
| 5 | Une chose à la fois | ✅ | Chaque feuille sert un seul formulaire ; FAB contextuel |
| 6 | Choix minimaux ≤ 4 | ❌ | Filtre saisons = 5 puces (L1205) ; météo = 5 options (L546-551) ; feuille cueillette = 7 champs ; feuille variété = 10 champs + 2 alertes + 4 boutons photo |
| 7 | Mémoire de travail | ❌ | Checklist indexée par position : retirer un critère décale les coches sans rien indiquer ; la checklist ne survit pas à l'export — l'utilisateur ne peut pas savoir ce qui sera perdu |
| 8 | Divulgation progressive | ❌ | La fiche détail déplie tout d'un coup (alerte + KV + description + carac + confusions + 5 specs + 2 verdicts + 4 boutons, L1293-1307) ; la checklist est entièrement visible, rien n'est plié |

**Échecs : 4/8.** Le poids vient des formulaires (6) et de la fiche détail (2, 8), et de la fragilité d'état de la checklist (7).

---

## 4. Voyage émotionnel (peak-end)

- **Entrée** : header dégradé ambre/rouille, logo pois + champignon, zigzag, pastille compteur rouge inclinée, apparition `pop` élastique (.22 s, bezier 1.6) — accueil chaleureux immédiat.
- **Pic** : la fiche hybride — cocher le dernier critère fait passer le verdict ⚠️ ambre au ✅ olive (« Chanterelle confirmé — récolte possible ») avec rebond ; c'est le moment « panier plein ». **Faux pic potentiel** : le même ✅ vert sur une fiche MORTELLE (tous critères cochés) — le texte « restez prudent » atténue, mais la valence verte reste discutable.
- **Vallées** : erreurs IA brutes (« Failed to fetch ») sans guidance ; double alerte orange dans la feuille variété ; après un import de transfert, les verdicts ⚠️/✅ ont disparu sans un mot — vallée silencieuse.
- **Fin de journée** : Stats colorées (4 cartes + tops + barres mensuelles) ; badge compteur dans le header ; aucun faux « tout terminé ».
- **Réassurance** : excellente sur les moments à risque — alerte « Règle d'or » permanente dans le guide, MORTEL + centre antipoison systématiques (fiche L1259, résultat IA L2058), double confirmation sur toutes les destructions (L1024-1025, L2203-2205), alerte « Jamais exporté » (L2160-2162), garde-fou de perte de saisie variété (L1464-1472, L947-951). Les vallées sont rares et bien amorties ; la faille checklist-export est la seule trahison silencieuse.

---

## 5. Heuristiques de Nielsen (0–4)

| # | Heuristique | Score | Problème clé |
|---|-------------|-------|--------------|
| 1 | Visibilité de l'état du système | 4 | Badge compteur, toasts, compteur n/5, verdicts, bandeau clé — tout est vivant |
| 2 | Correspondance système ↔ monde réel | 4 | Langage mycologique québécois authentique, saisons, « on ne mange pas » |
| 3 | Contrôle et liberté | 4 | Annuler partout, masquer/restaurer, poignée + voile, garde-fou saisie |
| 4 | Cohérence et standards | 3 | Zéro boîte système ✓, mais double alerte orange, filtres incomplets vs badges, CSS mort, inline massif |
| 5 | Prévention des erreurs | 4 | Doubles confirmations, fail-safe IA (statut hors vocabulaire → inconnu, L2029-2031), garde-fou variété |
| 6 | Reconnaissance plutôt que mémorisation | 4 | Suggestions espèces, puces à bascule, filtres visibles, restauration sélective |
| 7 | Flexibilité et efficacité | 3 | FAB contextuel, « Générer les manquantes » en masse, mais pas de tri ni de recherche dans Cueillettes/Spots |
| 8 | Esthétique minimaliste | 3 | Memphis assumé mais chargé : fiche détail surchargée, double bandeau, erreurs brutes |
| 9 | Aide à la reconnaissance/diagnostic des erreurs | 3 | Toasts clairs, mais `err.message` bruts (anglais), pas de guidance après échec IA |
| 10 | Aide et documentation | 3 | Placeholders et notes excellents, bandeau clé ; pas d'aide sur le flux checklist au 1er lancement |

**Total : 34/40** — profil : excellent sur la sécurité, l'état et le langage ; faible sur la densité (fiche détail, formulaires) et la finition des erreurs.

---

## 6. Forces spécifiques (3)

1. **La fiche hybride terrain (checklist + verdicts fail-safe)** — le mécanisme le plus abouti : 5 spécificités avec photos réelles Wikimedia embarquées (105 photos, `img/specs/`), descriptions orientées action (« Coupez en deux pour vérifier »), coche olive barrée, compteur n/5, verdict ⚠️/✅ persistant, et le fail-safe « Rien n'est encore vérifié → on ne mange pas » qui survit à la décoche totale (L1266-1285, L1311-1325). Aucun autre guide champignon grand public n'offre ce protocole de vérification interactif.
2. **La discipline du design system au pixel** — les règles nommées du DESIGN.md sont tenues sans exception dans les 340 lignes de CSS : Trait Noir 3 px partout, Décalage Net (aucune ombre floutée), Rouge Mortel (aucun rouge décoratif), coins cassés, inclinaisons, élastique. C'est une rareté : le style n'est pas un habillage, il est le produit.
3. **Le système de réassurance sécurité, sans panique** — alerte « Règle d'or » permanente (L380), MORTEL + centre antipoison systématiques avec fond saumon et coin rayé (L208-213, L1259, L2058), double confirmation de destruction, alerte « Jamais exporté », badge de sécurité conservé sur les cueillettes d'espèces supprimées via `especeId` archivé (L1336-1339), fail-safe de vocabulaire IA (L2029-2031). La promesse « la sécurité prime » est tenue dans la logique, pas seulement dans le copy.

---

## 7. Problèmes prioritaires (5)

**P1-1 — La checklist terrain ne survit pas à l'export/import (perte de données silencieuse).**
`index.html:2165` (export) et `:2177-2201` (import) omettent le store `checklist` (créé `:732`), alors que la note d'export promet le transfert vers un autre téléphone (`:413`). Toutes les vérifications ⚠️/✅ d'un carnet complet disparaissent au transfert sans aucun message. *Pourquoi c'est grave :* c'est exactement le pattern « ça sauvegarde mais ça ne voyage pas » — perte silencieuse de données terrain. *Fix :* ajouter `checklist: Object.values(Etat.checklist)` à l'export (version 5) et la relire à l'import, avec migration si `version` < 5.

**P1-2 — La checklist est indexée par position : retirer une spécificité corrompt les coches.**
`retirerIllu(i)` fait `ent.items.splice(i,1)` (`:1951-1952`) sans ajuster `faits[]` (écrit par position à `:1315-1318`, lu à `:1273`). Retirer le critère n°2 décale toutes les coches suivantes d'un cran : le verdict peut basculer à tort (✅ ou ⚠️ erroné) sur une espèce mortelle. *Fix :* stocker les faits par identifiant de critère (`{id: it.id, fait:true}`) ou réindexer `faits` dans `retirerIllu`, et re-dériver le verdict après splice.

**P2-1 — Contrastes AA manquants sur 2 libellés de stats.**
`.stat-carte:nth-child(2)` (cuir) et `:nth-child(4)` (terracotta) : libellés 12 px graisse 700 en blanc à 80 % → **4.15:1** et **3.74:1** (calculs : composite α=0.8 puis ratio). Les autres cartes passent (noir sur ambre 5.14:1). *Fix :* opacité `.8` → `.95` ou blanc pur (5.45:1 / 4.95:1).

**P2-2 — Filtres de sécurité du guide incomplets.**
4 puces (`tous/comestible/toxique/mortel`, `:1204`) pour 5 statuts + `prudence` (`:887-893`) : les « Immangeable » (bolet amer) n'apparaissent sous aucun filtre « ne pas manger » ; les « Comestible — prudence » (morille, amanite rougissante) sont noyés dans « Comestibles » ; pas de filtre « Prudence ». Pour un outil dont le principe n°1 est la sécurité, la segmentation sécurité est la plus pauvre. *Fix :* ajouter une puce « ⚠️ Prudence » et soit fusionner « Toxiques + Immangeables » en « Ne pas manger », soit ajouter « Immangeables ».

**P2-3 — Erreurs techniques brutes exposées à l'utilisateur.**
`⚠️ IA indisponible (Failed to fetch)` (`:1567`), `Génération impossible : ...` (`:1947`), `Échec sur « ... » : ... — série interrompue` (`:1979`) : `err.message` anglais dans un carnet chaleureux, sans guidance de récupération. *Fix :* mapper les erreurs connues (réseau, clé invalide, quota, modèle) vers des messages français avec l'action suivante (« Vérifiez votre connexion puis réessayez », « Clé invalide — revoyez ⚙️ Paramètres »).

*(P3)* **P3-1 — Modales sans focus trap ni Échap ; lightbox non clavier.** `boite-confirm`/`boite-choix` (`:464-480`) posent le focus initial mais ne le piègent pas ; la lightbox (`:1987-1994`) n'a ni `role="dialog"` ni Échap ; « 🔍 Agrandir » est un span non focusable (`:1279`). *Fix :* piège de focus + Échap sur les modales, `role="dialog"` + Échap + bouton fermer focusable sur la lightbox.

---

## 8. Red flags par persona

**Jonathan, en forêt, une main, gants (persona principal).**
- ✅ Ce qui marche : cibles 44 px, FAB à portée de pouce, tout hors-ligne, checklist rapide à cocher, verdicts lisibles à 10 m.
- 🚩 Le pire moment : il transfère son carnet sur un nouveau téléphone (ou restaure après casse) et toutes ses vérifications terrain ont disparu — sans avertissement (P1-1). Deuxième pire : il retire une spécificité d'une fiche mortelle et une coche saute d'un critère à l'autre sans qu'il le voie (P1-2).
- 🚩 En pleine saison de morilles : il filtre « Comestibles » et la morille (prudence) s'y trouve sans distinction au niveau liste — il faut ouvrir la fiche pour voir l'alerte cuisson/alcool.

**Utilisateur clavier / lecteur d'écran.**
- ✅ Puces, cartes, items clavier-complets (fix 5e passe tenu), aria-live sur toasts, modales ARIA correctement étiquetées.
- 🚩 Tab dans une modale → le focus sort derrière le voile (pas de trap) ; Échap ne ferme rien ; la lightbox est invisible au clavier ; l'état actif des onglets n'est pas annoncé (pas d'`aria-selected`).

**Utilisateur pressé / distrait (le dimanche soir, note sa récolte en vitesse).**
- ✅ Formulaires courts par défaut (date préremplie, météo par défaut), suggestions d'espèces, valeur libre acceptée, unités kg/lb converties.
- 🚩 Erreur IA → « Failed to fetch » sans marche à suivre, au moment où il a le moins de patience ; double alerte orange qui fait défiler la feuille variété inutilement.

---

## 9. Observations mineures

- `.illu-onglets` et `.illu-img` (L243-247) : CSS orphelin — l'ancienne galerie à onglets a été remplacée par la feuille liste ; code mort à purger.
- Double alerte orange « clé Gemini » dans `sheet-espece` (L576 et L628) : la seconde (« 🔑 La clé Gemini se configure dans Paramètres… ») répète la première.
- `font-weight:900` sur `.spec-num` et `.spec-carre` (L253, L256) : hors échelle documentée 400–700.
- `saisonDe` (L1216-1223) classe par premier mois cité : « Juillet à octobre » n'apparaît qu'en été, « Septembre à décembre » qu'en automne — la chanterelle ne se montre jamais en automne, le pleurote jamais en hiver.
- L'import n'annonce ni la version du fichier ni la checklist manquante ; il accepte tout JSON de forme valide.
- Tiges de mois vides à 4 px minimum (L2150) : suggèrent une micro-récolte là où il n'y a rien.
- `.item .mesures` (L137) : vert `#0B7A55` dur codé en dur plutôt que `--vert`/`--olive` — une 3e variable verte non documentée.
- Coche ✓ du spec-carre : 3.44:1 (blanc sur olive) — sous AA pour du texte, OK comme graphique ; à surveiller si on agrandit la coche.
- `header .pastille` (L50-55) : le compteur rouge est documenté, mais rouge = compteur et rouge = MORTEL dans le même écran (header + badges) — la distinction repose sur la forme (pastille vs pilule), fragile à petite taille.
- Placeholders avec emojis (🔎, 📷) : charmants et cohérents, mais ils disparaissent au focus sur certains navigateurs — penser aux labels visibles.

---

## 10. Questions provocatrices

1. **La checklist doit-elle voyager dans l'export ?** Si le carnet est « le succès = retrouver ses coins secrets, noter ses récoltes », pourquoi les vérifications terrain — la donnée la plus précieuse — sont-elles les seules à ne pas être exportées ? Version 5 ?
2. **Le verdict ✅ olive sur une fiche MORTELLE est-il une erreur de valence ?** « Tous les critères correspondent » en vert sous un bandeau ☠️ rouge : le vert valide-t-il la checklist ou la consommation ? Faut-il un verdict neutre/noir pour les mortelles ?
3. **Faut-il un filtre « Prudence » et « Immangeable » dans le guide, ou fusionner « Toxiques + Immangeables » en « Ne pas manger » ?** Le principe n°1 (sécurité prime) justifie-t-il que le bolet amer soit invisible sous « Toxiques » ?
4. **Le splash d'entrée `pop` à 1.6 de bezier est-il assez « panier plein » ou trop ?** Et que devient le rebond pour un utilisateur qui ouvre l'app 40 fois par saison — le plaisir tient-il à la répétition ?
5. **Pourquoi 4 couleurs de positions dans les tops stats sans sémantique ?** Si la 1re place est jaune et la 2e bleue, qu'apprend-on ? Ne serait-il pas plus fort de donner l'or à la 1re ?
6. **L'import doit-il valider la version du JSON avant de tout remplacer ?** Un export v3 importé aujourd'hui réécrit le carnet sans prévenir que des données (checklist, variantes) manquent.
7. **La fiche détail doit-elle tout déplier ?** Les 5 cartes spécificités + 2 verdicts + 4 boutons après 2 sections de texte : la divulgation progressive (critères pliés, verdict visible) servirait-elle mieux le terrain ?
8. **Les suggestions d'espèces doivent-elles être navigables au clavier (flèches) ?** L'input accepte la valeur libre, mais un utilisateur clavier ne peut pas choisir une suggestion sans souris.
9. **« Juillet à octobre » doit-elle apparaître sous Automne ?** Le filtre saison promet « trouvez ce qui pousse maintenant » ; la chanterelle d'octobre est invisible sous 🍂 Automne — le filtre ment-il à la mi-saison ?
10. **Le rouge du compteur header et le rouge MORTEL peuvent-ils cohabiter ?** La Règle du Rouge Mortel tolère le compteur, mais un nouvel utilisateur qui voit le badge rouge « 3 » et un badge rouge « MORTEL ☠️ » dans le même écran a-t-il le même réflexe ?

---

*Méthode : lecture statique intégrale de `index.html` (2334 lignes), `PRODUCT.md`, `DESIGN.md`, `sw.js` (cqm-v25), `git log` (correctifs 4e/5e passes vérifiés un à un), contrastes calculés (sRGB → luminance relative → ratio WCAG). Aucun fichier modifié. Correctifs des passes 4 et 5 confirmés tenus : verdict ⚠️ à 0 critère et après décoche totale, variables `--ambre/--olive/--cuir`, a11y clavier, contrastes verdict/meta, autocomplétion, cibles 44 px, focus ambre, garde-fou variété.*
