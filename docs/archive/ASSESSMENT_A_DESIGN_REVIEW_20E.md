# Assessment A — Critique design (20e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2647 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v45) · **Base :** `img/mycoquebec.json` (3938 entrées)
**Méthode :** lecture statique seule (Assessment A). Vérification des 3 findings de la passe 19E (P2-1, P3-1, P3-2) et des claims du commit `1cbad9c` dans le code ET sur les données : base JSON interrogée en Python par identité (latin), existence des fichiers vérifiée sur disque, liste `FICHIERS` du SW lue ligne à ligne, comparateur de suggestions (l.1586-1606) répliqué pour les 25 requêtes à haut risque, battery design complète (palette, ombres, uppercase, graisses, contrastes WCAG exacts).
**Note globale :** les 3 findings de 19E sont **entièrement corrigés** — et le P2-1 est tenu sur l'axe que l'utilisateur vit (le hors-ligne), vérifié par identité, pas au comptage. Aucune régression introduite. Le score plateau à 38,5/40 est honnête : H6 garde sa pénalité mais elle change d'identité (les vignettes distantes sont remplacées par un défaut de rappel de synonymes), les autres pénalités 19E sont toutes levées.

---

## 1. Verdict de spécificité design : 9/10 (inchangé)

La grammaire Memphis tient du header au toast, pour la 20e passe consécutive : 0 couleur hors palette documentée, 0 box-shadow flouté, 0 uppercase, 0 graisse hors 400-700, 0 boîte système (battery grep complète, cette passe). Les quatre règles nommées (Trait Noir, Rouge Mortel, Décalage Net, Inclinaison) sont respectées sans exception mesurable, y compris dans le correctif de cette passe (la réinitialisation du header réutilise le sous-titre exact, pastille incluse). Le point de vacillement reste identique : le langage ludique (rebond élastique) s'applique uniformément, y compris aux alertes mortelles.

**Axes :** conceptuel ~90 % (carnet de chasse, vocabulaire mycologique québécois, antipoison, cueillettes/spots) · visuel ~90 % (une capture sans texte révèle immédiatement Memphis-automne-champignon : pois, zigzag, coins cassés, vignettes rayées). Verdict : spécifique sur les deux axes, rare.

## 2. Évaluation holistique

- **Hiérarchie visuelle** — tenue : h2 en pastille inclinée, cartes à poids distincts, badge rouge unique en header. L'ajout de cette passe (réinitialisation header) restaure la hiérarchie après navigation (l.987-990).
- **Architecture de l'information** — 5 onglets complets, FAB contextuel, sous-titre du header suit l'entité ouverte. Résidu : le libellé d'une même espèce MORTELLE diverge entre deux surfaces (voir P2-1).
- **Adéquation émotionnelle** — le creux majeur de 19E (vignette cassée sur une MORTELLE, en forêt) est refermé. Les vallées restantes sont la densité de la feuille variété et le rebond élastique des alertes rouges.
- **Découvrabilité** — FAB, puces, feuilles : tout est visible, rien de caché au hover. La carte « Comment identifier » couvre H10.
- **Composition** — colonne unique 640 px, grilles 2 colonnes, feuilles 84 vh. La « Dernière sortie » à 24 px (l.2428) reste le seul risque de débordement.
- **Typographie** — Fredoka 400-700, hiérarchie 21/20/18/16/13/12,5 px, inclinaisons -1 à -2°, pas d'uppercase. `tabular-nums` sur mesures/rangs/compteurs (v44).
- **Couleur** — 0 dérive. Contrastes recalculés (WCAG exact) : tout le texte passe AA, y compris `.meta`/.note/.ligne-latin/.spec-desc à .85 (4,91:1), les 5 couleurs d'onglets actifs (4,66-5,74:1) et le sous-titre du header sur l'extrémité la plus claire du dégradé (4,79:1). Seule exception : le barré `.spec-carte.fait .spec-titre` à .75 (3,36:1) — intentionnel et documenté (DESIGN.md, satisfaction encodée par le barré, pas un texte à lire).
- **Accessibilité** — aria-labels couvrent FAB/destructions/selects/zoom ; role="button" toujours accompagné de tabindex ; focus-trap sur les modales ; Escape hiérarchisé (modale avant feuille) ; `prefers-reduced-motion` global (l.340-342). Résidus connus en section 9.
- **États** — états vides présents partout, analyse annulable, boutons désactivés pendant les appels IA, bandeau clé conditionnel. Pas de signal « tout va bien » codé en dur détecté.
- **Copy** — français du Québec cohérent, toasts à valence alignée sur leur branche (aucun ✨ sur un chemin d'échec, vérifié branche par branche). Résidu : deux noms pour une même espèce (P2-1).
- **Cas limites** — dates locales partout (`aujourdhui()`), version d'import vérifiée, checklist réindexée au retrait d'un critère, orphelins de `caches` nettoyés au rechargement.

## 3. Évaluation de charge cognitive : 1 échec / 8

1. Focus unique ✅ · 2. Chunking ≤ 4 ✅ · 3. Regroupement visuel ✅ · 4. Hiérarchie ✅ · 5. Une chose à la fois ✅ · 6. Choix minimaux ≤ 4 ❌ (feuille variété : 8 champs + 4 boutons photo + 1 alerte, l.599-662 — inchangé depuis 15E) · 7. Mémoire de travail ✅ (l'outil de désambiguïsation visuelle est maintenant 100 % hors-ligne — le croisement mental « quelle vignette fonctionnera ? » disparaît) · 8. Divulgation progressive ✅.

**1 échec franc sur 8** — l'avertissement de 19E (item 7) est levé.

## 4. Voyage émotionnel

Ouverture chaleureuse inchangée (header dégradé, formes flottantes, zigzag) → guide avec la Règle d'or → fiche hybride (cocher reste une récompense tactile, la coche rouge sans barré arrête la satisfaction où le danger commence). **Le creux 19E est refermé au pire moment du parcours :** en forêt, sans réseau, un doute sur Gyromitre ou Galérine marginée affiche désormais une vraie miniature locale — la décision visuelle fonctionne dans le mode d'emploi promis. Nouveau micro-plaisir intact de v44 : l'appui physique des cartes/boutons (ombre + translation animées ensemble). Vallées restantes : densité de la feuille variété (8 champs), rebond élastique des alertes mortelles (historique), et le P2-1 — taper « fausse morille » (le nom que la fiche enseigne) dans la feuille variété ne retourne rien, un silence au moment où l'utilisateur cherche à nommer la confusion la plus meurtrière du printemps.

## 5. Scores heuristiques Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | 4 | Toasts, états vides, analyse annulable, `btn:disabled` — et le header ne reste plus en « mode détail » après navigation (P3-1 19E ✅) |
| 2 | Correspondance monde réel | 4 | Réplication du comparateur : les 25 requêtes à haut risque servent le bon taxon du guide en premier, vignette locale |
| 3 | Contrôle et liberté | 4 | Annuler partout, ← sticky avec restauration du scroll, garde-fou 4 gestes, analyse annulable, ordre des images tenu |
| 4 | Cohérence et standards | 4 | L'aria-label du FAB suit enfin l'action réelle par onglet (P3-2 19E ✅) — plus aucun accroc détecté |
| 5 | Prévention des erreurs | 4 | Branche modale avant branche feuille dans Escape (l.1054-1079), matche flou des synonymes à la sauvegarde de cueillette, double confirmation, focus initial sur Annuler |
| 6 | Reconnaissance vs mémorisation | 3.5 | **Pénalité changée d'identité :** les 21/21 miniatures locales remplacent les 9 distantes (vérifié par identité), mais taper le synonyme appris par la fiche (« fausse morille », « ange destructeur ») retourne 0 suggestion — l'app exige de se rappeler le nom de la base (P2-1) |
| 7 | Flexibilité / efficacité | 4 | FAB contextuel, « Réessayer » dernière source, « Générer les manquantes », ordre des images persistant et tenu |
| 8 | Esthétique minimaliste | 3 | Feuille variété toujours dense : 8 champs + 4 boutons photo + 1 alerte |
| 9 | Aide à la récupération d'erreurs | 4 | messageErreurIA en français par cause, « série interrompue », repli copie du partage, fail-safe statut IA |
| 10 | Aide et documentation | 4 | Carte « Comment identifier », crédits Commons, note honnête du paramètre Ordre des images |

**Total : 38,5/40 — plateau honnête.** Les pénalités 19E sont toutes levées (H1 : header, H4 : aria-label FAB, H6 : vignettes distantes), mais H6 garde -0,5 pour un défaut de rappel de synonymes (P2-1) qui n'était jusqu'ici qu'une question (19E Q2), jamais score. Profil : sécurité, contrôle, état du système excellents ; le talon d'Achille reste la fidélité du vocabulaire entre la fiche (ce qu'on apprend) et la base (ce qu'on peut taper).

## 6. Forces spécifiques

1. **Le P2-1 19E est tenu sur l'axe que l'utilisateur vit, vérifié par identité.** Les 21 entrées `guide:true` de la base portent une `img` locale (`img/especes/<id>.jpg`) — dont les 9 anciennement distantes (Coprin chevelu, Galérine marginée, Gyromitre, Pied-de-mouton, Fausse chanterelle, Bolet bai, Paxille enroulé, Pleurote, Bolet amer) ; l'ensemble `guide:true` correspond exactement aux 21 latins du guide (0 faux positif, 0 faux négatif) ; les 21 fichiers existent sur disque ; les 21 figurent dans `FICHIERS` du SW (l.12-32, cqm-v45). La promesse « 100 % hors-ligne dès la première visite » couvre enfin les suggestions, pas seulement les fiches.
2. **La chaîne nom → taxon → fiche est cohérente pour les 21 espèces, re-vérifiée par réplication du comparateur réel** (score exact/préfixe/guide, tie-break guide, puis longueur) : « gyromitre » → Gyromitra esculenta ★🖼 premier, « phalloïde », « vireuse », « galerine marginee », « paxille enroule », « pied-de-mouton », « morille », les 25 requêtes servent le bon taxon en position 1, vignette locale.
3. **Un correctif qui suit le pattern recommandé au lieu de contourner.** Le P3-1 est résolu exactement comme le suggérait 19E Q3 : la réinitialisation du header vit dans `naviguer()` (l.987-990), le chemin de sortie unique ne porte plus l'état. Et le P3-2 est résolu par la solution à 3 valeurs (l.985). Deux correctifs qui renforcent l'architecture au lieu d'empiler des cas spéciaux.

## 7. Problèmes prioritaires

**P2-1 (NOUVEAU) — le synonyme vernaculaire appris par la fiche est ininterrogeable, et le libellé diverge, pour deux espèces dont une MORTELLE.** La fiche du guide enseigne « Gyromitre (fausse morille) » (l.905) et « Amanite vireuse (ange destructeur) » (l.895) ; la base MycoQuébec les nomme « Gyromitre commun » et « Amanite vireuse ». Deux conséquences mesurées : (a) taper « fausse morille » ou « ange destructeur » dans la feuille variété (`e-nom`) retourne **0 suggestion** — le filtre l.1587 ne matche que `nomFr`/`latin` ; (b) la suggestion affiche « Gyromitre commun », un troisième libellé que la fiche n'utilise jamais — l'utilisateur en doute doit se demander si c'est la même espèce. Le chemin cueillette est protégé (`infoEspece` matche par inclusion et lève le badge ☠️ + confirmation, l.962-970, l.1543-1546), mais la feuille variété ne l'est pas : un nom libre « fausse morille » peut être enregistré avec le statut défaut « ✅ Comestible » (l.1662). Pour l'espèce MORTELLE au centre de la confusion la plus meurtrière du printemps, c'est un silence au pire moment. *Fix (données, trivial) :* aligner `nomFr` des entrées `guide:true` sur le nom exact de la fiche (« Gyromitre (fausse morille) », « Amanite vireuse (ange destructeur) ») — les synonymes deviennent queryables, le libellé suggéré = celui de la fiche, et le même fix règle « Galérine »/« Galerine » (accent).

**P3-1 (NOUVEAU) — `fermerDetail()` réinitialise encore le header que `naviguer('guide')` vient de réinitialiser.** l.1437-1439 répètent mot pour mot les l.988-989 désormais centralisées dans `naviguer()`. Inoffensif, mais c'est exactement la duplication que 19E demandait d'éliminer ; le prochain développeur qui modifie le sous-titre ne pensera qu'à un des deux endroits. *Fix :* supprimer les l.1438-1439, ne garder que la restauration du scroll.

## 8. Red flags par persona

- **Jonathan en forêt, une main, sans réseau** : le pire moment de 19E est refermé — en doute sur un Gyromitre ou une Galérine (deux MORTELLES), la suggestion affiche une vraie miniature locale, la décision visuelle fonctionne hors-ligne. Restant : taper « fausse morille » dans la feuille variété ne suggère rien (P2-1), et le statut défaut de la feuille variété est « ✅ Comestible » — un nom libre dangereux peut être enregistré vert sans alerte (résidu 16E).
- **Proche débutant (via export/import)** : import avec vérification de version ✅, verdicts conditionnés au statut ✅, marquage guide 21/21 par identité ✅. Risque restant : « Gyromitre commun » dans la suggestion vs « Gyromitre (fausse morille) » dans la fiche — deux libellés pour la confusion qu'on lui a appris à craindre (P2-1).
- **Utilisateur pressé / en doute** : le lecteur d'écran entend enfin « Nouvelle variété » sur l'onglet Identifier (P3-2 ✅) et le header ne ment plus après un saut d'onglet (P3-1 ✅). Petit piège restant : les suggestions Myco n'ont toujours pas de navigation clavier ↑/↓ (résidu 16E).

## 9. Observations mineures

- `choisirNomMyco` (l.1621-1622) : le latin n'est auto-rempli que si le champ est vide — résidu 15E.
- `chargerBaseMyco` (l.1573-1578) : échec de fetch silencieux (`baseMyco = []`) — les suggestions disparaissent sans message — résidu 15E.
- Champ recherche du guide sans label visible (l.390, placeholder seul) — résidu 16E.
- Focus perdu sur les selects de filtre (re-rendu du DOM, l.1313-1321) — résidu 16E.
- `COULEURS_MOIS` (l.2412) : le cycle de 6 couleurs se répète deux fois par an — résidu 16E.
- Barres de stats (`topRangs`, l.2417) sans `role="progressbar"` ni valeur sur la barre ; 0 kg dessine un stub de 4 % (`Math.max(4, …)`) — résidus 16E/19E.
- Lightbox (l.2262-2282) : Escape + focus restore ✅, pas de focus trap — résidu 16E.
- `alt="photo"` générique (l.1147) — résidu 16E.
- `imageEnBase64` (l.1829-1836) sans limite de taille — résidu 16E.
- « Dernière sortie » à 24 px dans une carte 2 colonnes (l.2428) : risque de débordement sur écran étroit — résidu 13E.
- `ouvrirMyco` (l.2259-2261) : lien externe — hors-ligne, page d'erreur du navigateur sans message de l'app — résidu 16E.
- `.mois-col .lab` à 10,5 px (l.318) : contraste OK (14,08:1) mais très petit — résidu 16E.
- Boucle `illu-toutes` : une image générée par IA ne déclenche aucun toast par item (l.2246-2247, seuls wiki/myco en ont) — résidu 18E.
- Toast « Aucune spécificité — ajoutez-en une ci-dessous » (l.2177) inatteignable : `ouvrirSheetIllu` injecte les 5 défauts (l.2141-2144) — résidu 18E.
- `spec-zoom` : span `role="button"` imbriqué dans une carte `role="button"` (l.1396-1397) — fonctionnel grâce au stopPropagation, mais imbrication interactive — résidu 19E.
- Le fetch handler du SW (l.159-165) met en cache toute réponse GET réussie (hors wikimedia/googleapis/clé) : croissance du cache non bornée pour une PWA 100 % hors-ligne — nouveau constat, pas de fix proposé dans les passes précédentes.
- Accent : base « Galérine marginée » vs fiche « Galerine marginée » — corrigé de facto par la normalisation des accents, mais divergences d'affichage — absorbé par P2-1.

## 10. Questions provocatrices

1. La fiche enseigne « fausse morille », la base exige « gyromitre » : quel vocabulaire est la vérité du produit, et pourquoi le nom de la confusion la plus meurtrière du printemps n'est-il pas queryable dans la feuille variété alors que `infoEspece` sait déjà le matcher par inclusion ?
2. Pourquoi les 21 entrées `guide:true` ne portent-elles pas exactement le `nomFr` de leur fiche (fix de données d'une ligne), alors que c'est ce que le comparateur utilise pour servir « le bon taxon » ?
3. La feuille variété enregistre un nom libre sans jamais interroger `infoEspece` : une variété nommée « fausse morille » peut être créée verte « ✅ Comestible » sans une seule alerte — la sécurité ne devrait-elle pas s'appliquer à l'enregistrement d'une espèce, pas seulement à celui d'une cueillette ?
4. `fermerDetail()` répète la réinitialisation que `naviguer('guide')` fait déjà : la centralisation doit-elle être complète (supprimer le doublon) ou le doublon est-il une ceinture-bretelles assumée ?
5. `Math.max(4, …)` dessine une barre de 4 % pour 0 kg récolté : un zéro honnête doit-il être un zéro invisible, ou la barre symbolise-t-elle autre chose que le poids ?
6. `COULEURS_MOIS` répète le même cycle de 6 deux fois par an : cycle saisonnier délibéré (l'automne québécois en double) ou copie de tableau ?
7. Les suggestions Myco sont sans navigation clavier depuis 16E : à quel moment un champ d'autocomplétion devient-il un vrai combobox ARIA dans ce projet ?
8. Les barres de stats n'ont ni `role="progressbar"` ni valeur affichée sur la barre : la donnée (poids par espèce) doit-elle être accessible aux lecteurs d'écran, et affichée sur la barre pour les yeux ?
9. Le SW met en cache toute réponse GET réussie, sans plafond : la promesse « 100 % hors-ligne » justifie-t-elle une croissance de cache non bornée, ou faut-il un quota (ou au moins exclure les domaines tiers par défaut) ?
10. Le statut défaut de la feuille variété est « ✅ Comestible » alors que la base suggère des espèces MORTELLES : le défaut ne devrait-il pas être « ⚠️ Inconnu » pour toute variété dont le nom vient d'une suggestion sans statut connu ?

---

**Correctifs de la passe 19E vérifiés :** P2-1 ✅ **entièrement corrigé, par identité** (21/21 entrées `guide:true` à `img` locale `img/especes/<id>.jpg` — dont les 9 anciennement distantes, Galérine marginée et Gyromitre MORTELLES comprises ; 0 URL distante parmi `guide:true` ; l'ensemble flaggé = exactement les 21 latins du guide, 0 faux positif/négatif ; 21/21 fichiers sur disque ; 21/21 dans `FICHIERS` du SW, cqm-v45) · P3-1 ✅ (l.987-990 : `naviguer()` réinitialise `#sous-titre` et `#badge` pour toute vue ≠ detail ; le sous-titre détail est posé par `ouvrirDetail` après `naviguer('detail')` — ordre correct) · P3-2 ✅ (l.985 : ternary à 3 valeurs spots → « Ajouter un spot », cueillettes → « Ajouter une cueillette », sinon → « Nouvelle variété », aligné sur le dispatch du clic FAB l.997-1001) · SW cqm-v45 ✅.
**Claims v44 (699ae19) toujours tenus** (aucune ligne de ces zones modifiée depuis 19E) : transitions ombre+transform (l.62/104/128/167), onglets 0,15 s interruptibles (l.83), hit area 44 px (l.250), outlines 10 % (l.137/189/248/326), tabular-nums (l.55/141/267/298/312), text-wrap:pretty (l.140/259/320/330), antialiased (l.29).
**Non corrigés :** P2-1 (NOUVEAU 20E — synonymes ininterrogeables + libellés divergents), P3-1 (NOUVEAU 20E — doublon `fermerDetail`), navigation clavier des suggestions, résidus listés en section 9.
