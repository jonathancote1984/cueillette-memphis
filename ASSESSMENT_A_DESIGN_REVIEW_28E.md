# Assessment A — Critique design (28e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2812 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v55) · **Méthode :** lecture statique seule (Assessment A, aucun navigateur, aucun détecteur). Vérification des 6 claims de `b87d1dd` (fix critique-27e) ligne par ligne — chaque ligne citée provient de `read_file` ou de `git show`, aucune de search_files. HEAD = `33351cc` (docs uniquement), arbre git propre : l'état évalué est exactement le commit du fix. Batterie de dérive re-passée : 0 ombre floutée, 0 uppercase, 0 `window.confirm` (seul le commentaire l.235), 0 `aria-invalid`, 0 font-weight hors jeu — CSS intact (le diff ne touche aucun `<style>`).

**Note globale :** 5 claims sur 6 sont **tenus en code** (P1-1, P2-1, P2-2 sur l'appareil, P3-2, SW bump) ; **P3-1 est tenu en code mais inobservable dans le scénario visé** (voir §7). La passe révèle en contrepartie : **P2-1 — les tombes ne traversent pas l'export/import** (le filet et les badges se taisent sur le téléphone du proche — flux produit documenté), **P2-2 — la suppression perso n'a ni confirmation ni undo** alors que le même bouton sur le guide en exige deux, et trois P3 (fiche fantôme post-suppression, espèce masquée indésélectionnable d'un spot, c-date hors garde-fou). Score **38,5/40** (+0,5 vs 27E) : les deux fausses rétroactions 27E sont fermées en code (H1 +0,5, H4 +0,5 récupérés), compensées par la brèche export (H5) et l'irréversibilité de la suppression perso (H9).

---

## 1. Verdict de spécificité design : 9/10 (inchangé)

Le diff du commit ne contient **aucun CSS** (18 insertions/11 suppressions, tout en JS + sw.js) : 0 couleur hors palette, 0 ombre floutée (La Règle du Décalage Net tient), 0 `text-transform`/uppercase, 0 boîte système. Contrastes inchangés depuis 25E (4,61–13,5:1, tous AA). **Axes :** conceptuel ~90 % (carnet de chasse, vocabulaire mycologique, antipoison, verdicts ⚠️/☠️/✅, « le guide a le dernier mot », désormais aussi « les tombes » — la métaphore de la pierre tombale pour les espèces supprimées est du langage de domaine) · visuel ~90 % (une capture sans texte révèle Memphis-automne-champignon : zigzag, coins cassés, ombres dures, pois). Verdict : spécifique sur les deux axes ; la discipline tient sur une sixième passe consécutive sans dérive visuelle.

## 2. Évaluation holistique

- **Hiérarchie visuelle** — tenue. Le P1-1 rend enfin le rangement vrai : masquer une variété perso la retire du guide, des puces du spot et des suggestions (`toutesEspeces` l.973-976 filtre `especesCustom` par `cachees` et `supprimees`). La hiérarchie badge → alertes → actions de la fiche hybride est inchangée.
- **Architecture de l'information** — `rendreCueillettes` adopte `infoEspeceArchive` (l.1560) : le patron inline 27E est éliminé, il ne reste que `infoEspece` + `infoEspeceArchive` (le repli `infoArchivee` l.1561 par `c.especeId` subsiste pour les vieilles cueillettes du guide — légitime). Le filet et l'affichage partagent désormais la même fonction de vérité.
- **Adéquation émotionnelle** — les deux vallées 27E sont fermées en code : plus de toast « Espèce masquée 🙈 » mensonger (le masquage est réel), plus de garde-fou qui crie au loup sur une feuille intacte (comparaison à `meteoInitial`, l.1083-1084). **Nouvelle vallée introduite par la tombe :** la suppression perso est instantanée, sans confirmation ni annulation possible, et la fiche reste ouverte sur un cadavre interactif (P2-2 et P3-1, §7).
- **Découvrabilité** — inchangé : bandeau clé, FAB contextuel avec aria-label par vue (l.1049), étapes progressives, rien au hover.
- **Composition** — colonne 640 px, feuilles 84 vh, grille 2 colonnes conservées ; aucun changement structurel.
- **Typographie** — inchangée (aucun CSS modifié) : Fredoka 400/500/600/700 chargés (l.17), aucun poids hors jeu, Meta 400/12,5 px/0,85 conforme à DESIGN.md l.162.
- **Couleur** — 0 dérive dans le diff. La Règle du Rouge Mortel tient dans le code. Tension documentée (pas un drift) : la pastille numérotée rouge de l'étape active (l.308), autorisée par DESIGN.md l.225 — question 27E toujours ouverte.
- **Accessibilité** — ordre des branches Escape **toujours le bon** : `boiteVisible()` d'abord (l.1134-1139), feuille variété ensuite (l.1142-1146), feuille générique en dernier (l.1148-1149). Garde-fou couvert sur voile (l.1094), poignées (l.1095), Escape, Annuler spot (l.1372) et Annuler cueillette (l.1659). Reste : `aria-invalid` = 0 partout (grep confirmé), lightbox sans piège Tab (l.2410-2430), `p-cle` (l.460) et `g-recherche` (l.411) sans label.
- **États** — l'état « feuille cueillette sale » est enfin calculé juste (météo comparée à la valeur d'ouverture, posée aux deux ouvertures l.1607 et l.1622). **Nouveau :** l'état « fiche ouverte » ne suit pas la suppression — la fiche d'une variété supprimée reste affichée avec ses cartes mortes (P3-1).
- **Copy** — le toast « Variété supprimée définitivement 🗑️ » (l.1197) est honnête, mais il annonce une destruction que rien n'a confirmée et que rien ne peut annuler (P2-2). Le message du garde-fou ne tire plus à tort.
- **Cas limites** — dates locales (l.752-755), import versionné, checklist réindexée au retrait (l.2363-2367). Nouveau : tombe sans photo → vig « 🍄 » des cueillettes (l.1564, repli correct — pas d'image cassée) ; orphelins de caches purgés au rechargement (l.2775-2779) ; checklist orpheline après suppression perso (§9).

## 3. Évaluation de charge cognitive : 1 échec / 8 (inchangé)

1. Focus unique ✅ · 2. Chunking ≤ 4 ✅ · 3. Regroupement visuel ✅ · 4. Hiérarchie ✅ · 5. Une chose à la fois ✅ · 6. Choix minimaux ≤ 4 ❌ — **étape 1 = 5 champs** (nom, latin, comestibilité, saison, prudence) + 2 boutons + 1 encart ; inchangé depuis 21E · 7. Mémoire de travail ✅ — le croisement guide/tombes réduit la charge au moment critique ; **réserve :** sur la fiche fantôme post-suppression, l'utilisateur doit se rappeler qu'il vient de supprimer la variété pour comprendre pourquoi les cases ne répondent plus (P3-1) · 8. Divulgation progressive ✅.

**1 échec franc sur 8.**

## 4. Voyage émotionnel

Ouverture chaleureuse → guide → fiche hybride inchangés. **Les deux vallées 27E sont fermées, vérifiées en code :** (a) masquer une variété perso la retire réellement de toutes les listes (`toutesEspeces` l.975 — le toast « Espèce masquée 🙈 » est enfin un pic de sécurité vrai, plus un faux pic) ; (b) la feuille cueillette intacte se ferme en silence — plus de confirmation mensongère en forêt (l.1083-1084 contre l.1607/1622). **Nouvelles vallées :** (i) supprimer une variété perso est un geste unique, définitif, sans confirmation ni undo — la pire combinaison pour du contenu enrichi par IA (P2-2) ; (ii) après ce geste, la fiche reste ouverte : cartes qui ne réagissent plus, boutons morts — un moment « l'app est cassée » en pleine session (P3-1). Fin de journée : rappel d'export honnête, pas de faux pic.

## 5. Scores heuristiques Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | **4** (+0,5) | Le toast « Espèce masquée 🙈 » confirme enfin un état réel (l.1184 vs l.975) ; réserve P3 : la fiche fantôme post-suppression (l.1191-1198 ne ferme pas le détail) |
| 2 | Correspondance monde réel | 4 | Vocabulaire du carnet de chasse ; « le guide a le dernier mot » ; tombes = langage de domaine cohérent |
| 3 | Contrôle et liberté | 4 | Annuler via garde-fou sur les 3 feuilles (l.1372, 1659) ; ordre Escape-modal vérifié l.1134-1149 |
| 4 | Cohérence et standards | **3,5** (=) | Le garde-fou dit enfin la vérité, mais le même bouton « Supprimer définitivement » vaut 2 confirmations pour le guide (l.1202-1203) et 0 pour une variété perso (l.1191) |
| 5 | Prévention des erreurs | **4** (+0,5) | Filet complet sur l'appareil : guide + perso + tombes, exact + flou + inclusion, surclassement GRAV upgrade-only (l.2483-2489) ; seule brèche : les tombes ne traversent pas export/import (P2-1, §7) |
| 6 | Reconnaissance vs mémorisation | 4 | Noms requêtables sous toutes leurs formes ; croisement normNom + synonymes + Levenshtein + inclusion sur guide+perso+tombes |
| 7 | Flexibilité / efficacité | 4 | IA remplit les 2 étapes, retry + repli modèle, ordre des images persistant, 21 guide:true identité-vérifiés |
| 8 | Esthétique minimaliste | 3,5 | Étape 1 à 5 champs, étape 2 ~13 éléments (inchangé) |
| 9 | Aide à la récupération d'erreurs | **3,5** (−0,5) | messageErreurIA par cause, parserJSONIA tolérant, import versionné ; mais la suppression perso est irréversible, sans undo, et emporte illustrations + fiche IA (l.1195-1196) |
| 10 | Aide et documentation | 4 | Commentaires référencent la bonne passe (« P2-1 (27e) » l.1083, « P2-2 27e » l.1192, « P1-2 + P3-2 (27e) » l.1559) ; DESIGN.md à jour |

**Total : 38,5/40 (+0,5 vs 27E).** Les fixes 27E sont vérifiés et réels : H1 et H4 récupèrent chacun leur demi-point (fausses rétroactions fermées). La hausse est plafonnée par deux dettes nommées : la brèche export des tombes (H5) et la suppression perso sans confirmation ni undo (H9), plus l'asymétrie de confirmation du même bouton selon l'espèce (H4).

## 6. Forces spécifiques

1. **La tombe est le bon patron, posé au bon endroit.** `BASE_COMPLETE` (l.1011) ajoute `Etat.tombes` sans jamais filtrer la visibilité : le filet de sécurité consulte guide + perso + tombes (l.1012-1033), pendant que `toutesEspeces` (l.973-976) applique le rangement (cachees/supprimees) aux deux sources. Sécurité et rangement sont découplés par construction — la bonne architecture pour un produit où la prudence ne dépend pas de l'état du guide. Et le surclassement `GRAV` reste **upgrade-only** (l.2488) : un faux appariement flou ne peut jamais adoucir un verdict.
2. **Le correctif c-meteo applique le bon principe d'état : initial vs courant.** Au lieu de tester une valeur non vide, le garde-fou compare le champ à sa valeur d'ouverture, posée aux DEUX ouvertures (création l.1607, édition l.1622). C'est le patron d'état juste pour tout champ pré-rempli — il attend seulement d'être généralisé à `c-date` (Q5).
3. **La discipline des données tient sur l'axe que l'utilisateur vit vraiment (hors-ligne).** 21/21 espèces du guide avec `img/especes/*.jpg` locales et dans le SW ; 105/105 spécificités dans `SPECS_DEFAUT` avec `img/specs/*.jpg` locales ; SW bump `cqm-v55` (sw.js l.4) avec FICHIERS complet (21 especes + 105 specs + credits + mycoquebec.json — re-vérifié par script). Les 21 `guide:true` correspondent par identité aux 21 latins d'`ESPECES`.

## 7. Problèmes prioritaires

**P2-1 (NOUVEAU — SÉCURITÉ EN TRANSFERT) — les tombes ne survivent pas à l'export/import.** L'export sérialise `supprimees: Etat.supprimees` (l.2626) — or `Etat.supprimees` est la liste des **ids nus** (`suBrut.map(x => x.id)`, l.2771). Les records de tombes (nom, latin, statut, prudence) ne quittent jamais l'appareil. À l'import, `data.supprimees` est réécrite en `{id}` (l.2664) ; `recharger` ne reconstruit une tombe que si `x.nom` existe (l.2773) → `tombes = {}` sur le téléphone du proche. Conséquence : sur un carnet transféré (flux produit documenté, PRODUCT.md l.26 « partage à des proches »), les cueillettes d'une variété perso MORTELLE supprimée perdent leur badge (l.1560 ne trouve plus rien), et l'identification photo sur ce nom ne croise plus le guide (l.2486). Le claim « le filet et les badges survivent à l'effacement » est vrai **sur l'appareil seulement**. *Fix :* exporter les records — `supprimees: suBrut` (ou `tombes: Object.values(Etat.tombes)` + ids guide) — et à l'import écrire chaque entrée telle quelle (`typeof id === 'string' ? {id} : id`) ; ajouter le cas à la vérification de version.

**P2-2 (NOUVEAU, PRÉEXISTANT — PREMIER SIGNALEMENT) — la suppression d'une variété perso n'a ni confirmation ni undo, alors que le guide en exige deux.** Même bouton « 🗑️ Supprimer définitivement » dans la même modale : guide = double `confirmer()` (l.1202-1203) ; perso = effacement immédiat (l.1191-1198, le seul clic de la modale sert de confirmation implicite). Le geste emporte irréversiblement la fiche (desc, carac, confusions, photo) et les **illustrations générées** (l.1196), sans toast-action « Annuler » ni fenêtre de récupération. Pour du contenu enrichi par IA que l'utilisateur a construit, c'est la pire combinaison H5/H9. *Fix :* une `confirmer()` Memphis avant l'effacement perso (symétrie avec le guide), et/ou un toast avec action Annuler qui réécrit la variété + ses illustrations depuis une capture pré-suppression.

**P3-1 (CLAIM P3-1 TENU EN CODE, MAIS INOBSERVABLE — FICHE FANTÔME) — après suppression depuis sa propre fiche, la fiche reste ouverte sur une variété morte.** Le lookup `BASE_COMPLETE().find(x => x.id === Etat.detailId)` (l.1540) trouve bien la tombe (même id) → le glyphe ☠️ serait correct. Mais le chemin est inatteignable dans le scénario visé : la suppression efface `illustrations` (l.1196) → après `recharger()`, `Etat.illustrations[id]` est vide → `basculerSpec` retourne avant le code du glyphe (l.1524-1525 `{ items: [] }` → `if (!illu.items[i]) return`). Concrètement : la fiche affiche encore photo, badges et verdict (rendus à l'ouverture), mais les spec-cartes ne réagissent plus — un « l'app est cassée » muet. Le vrai correctif du scénario n'est pas le lookup : c'est la fermeture. *Fix :* `fermerDetail()` (ou un état « variété supprimée ») à la fin du chemin perso de `choix-supprimer` ; le lookup tombe reste utile si la fiche devient consultable en lecture seule.

**P3-2 (NOUVEAU) — une espèce masquée ne peut plus être retirée des puces d'un spot.** `remplirSelectEspecesSpot` rend les puces depuis `toutesEspeces()` (l.1325) : la puce d'une espèce masquée disparaît, mais son nom reste dans `Etat.spot.especes` (l.1338) — invisible et indésélectionnable (le toggle n'existe que par clic de puce, l.1329-1335). Le spot garde à jamais une association que l'utilisateur ne voit plus. *Fix :* afficher les espèces sélectionnées-masquées en puce grisée cliquable (retrait), ou lister les noms sélectionnés avec un « × » indépendant des puces.

**P3-3 (NOUVEAU) — `c-date` est hors du garde-fou.** `feuilleSaisieSale` teste c-espece, c-poids, c-note, photo, c-spot et c-meteo (l.1080-1084), mais pas la date — pourtant pré-remplie à `aujourdhui()` (l.1604) comme la météo l'est à 🌞. Changer uniquement la date puis annuler (voile/poignée/Escape/Annuler) la perd en silence. *Fix :* le même patron que c-meteo : `dateInitial` posé aux deux ouvertures, comparé dans le garde-fou.

## 8. Red flags par persona

- **Jonathan en forêt, une main, sans réseau** : le moment de vérité (photo ID) est désormais protégé pour le guide masqué/supprimé, les perso masquées ET supprimées (tombes, l.1011-1033, 2486-2489) — le trou 27E est fermé sur l'appareil. **Pire moment :** un tap de trop sur « Supprimer définitivement » d'une variété perso (glissement, gant, pluie) = destruction instantanée de la fiche et des illustrations, sans confirmation — puis une fiche fantôme qui ne répond plus (P2-2, P3-1).
- **Proche débutant (via export/import)** : la règle simple « ☠️ = ne jamais manger » tient tant que le carnet vit sur un seul téléphone. **Pire moment :** recevoir le carnet du propriétaire et découvrir que les cueillettes de la variété perso MORTELLE supprimée n'ont plus de badge, et que l'identification photo ne la reconnaît plus (P2-1) — le filet s'est arrêté à la frontière de l'export.
- **Utilisateur au clavier / lecteur d'écran** : ordre Escape-modal sûr, verdict-att cohérent en audio, Annuler protégé comme le voile. **Pire moment :** la fiche fantôme post-suppression annonce des `aria-pressed` sur des cartes qui n'agissent plus (silence complet au clavier, P3-1) ; et la suppression perso sans confirmation n'offre aucune sortie de secours au clavier non plus (P2-2).

## 9. Observations mineures

**Nouveaux :**
- La checklist d'une variété perso supprimée reste orpheline dans IndexedDB (le chemin de suppression ne purge pas le store `checklist`, l.1195-1196) — données mortes, inoffensives mais jamais nettoyées.
- La tombe perso n'a pas de photo : les cueillettes liées affichent la vignette « 🍄 » générique (l.1564, repli correct) — acceptable, mais le carnet perd la vignette que l'utilisateur avait choisie pour cette variété.
- Commentaire l.2648 « P2-2 : vérification de la version » — numérotation d'une ancienne passe ; s'ajoute au « P1-5 » de l.2478 (signalé 25E/26E/27E, toujours là).
- Le fix P3-1 (lookup tombe l.1540) est du code mort dans le scénario supprimer-depuis-sa-fiche : les cartes sont mortes avant lui (voir P3-1, §7) — le garder, mais ne pas le compter comme la réparation du scénario.

**Résidus inchangés (non re-scorés, re-confirmés présents en 28E) :** `rendreBandeauCle` insère un `<button>` dans un `<p class="note">` (l.2446-2449, HTML invalide) · `p-cle` sans label (l.460) · `g-recherche` sans label (l.411) · toast de pré-remplissage sans mention du statut transféré (l.2563) · `retirerIllu` ne re-rend pas la vue détail sous-jacente (l.2359-2376) · PRODUCT.md l.39 (`especesCustom`/`cachees`) vs code (`especes`/`caches`, l.792-793) · échec silencieux de `chargerBaseMyco` → « 0 espèces de la base » mensonger hors-ligne (l.1669-1672, 1711) · focus perdu sur les selects de filtre (re-rendu `rendreFiltres`, l.1395-1403) · `alt="photo"` générique (l.1229) · `ouvrirMyco` sans message hors-ligne (l.2407-2409) · `.mois-col .lab` 10,5 px (l.339) · cache SW non borné pour les GET réussis (sw.js l.160-163) · `aria-invalid` : 0 partout (re-grep confirmé), validation toast-only · `COULEURS_MOIS` cycle 6×2 sans sémantique de saison (l.2575) · lightbox sans piège à focus (l.2410-2430) · `feuilleSaisieSale` via `document.getElementById` au lieu de `$` (l.1074/1079, style).

## 10. Questions provocatrices

1. Les tombes sont la mémoire de sécurité des suppressions perso : pourquoi l'export les réduit à des ids nus (l.2626) alors que le partage à un proche est un flux produit documenté ? Qui possède la vérité de sérialisation de `supprimees` — et que vaut le filet sur un carnet transféré ?
2. Pourquoi « Supprimer définitivement » vaut une double confirmation pour une espèce du guide (l.1202-1203) et zéro pour une variété perso (l.1191) — laquelle des deux normes est la bonne pour du contenu enrichi par IA que l'utilisateur a construit ?
3. Après suppression depuis sa propre fiche, la fiche reste ouverte sur une variété morte : doit-elle se fermer, passer en lecture seule, ou afficher un état « variété supprimée » — et qui re-rend `detail-contenu` quand `recharger()` passe ?
4. Un spot peut porter le nom d'une espèce masquée que les puces ne montrent plus : l'association doit-elle être visible (puce grisée), retirable (chip « × »), ou interdite à la source ?
5. `c-date` est pré-remplie à aujourd'hui exactement comme `c-meteo` l'est à 🌞 : pourquoi le garde-fou protège la seconde et pas la première ? Le principe « champ pré-rempli ≠ sale » doit-il être généralisé à tout le formulaire ?
6. À quel moment une tombe peut-elle être purgée (jamais ? à l'export ? après N versions ?) sans réintroduire le trou 27E — et qui porte cette décision ?
7. La checklist d'une variété supprimée survit dans IndexedDB : mémoire voulue pour une restauration future, ou déchet à purger dans le même geste que les illustrations (l.1196) ?

---

**Claims `b87d1dd` vérifiés** (`git show --stat` : index.html +18/−11, sw.js ±1 — conforme) :

- **P1-1 ✅ tenu.** `toutesEspeces` filtre `especesCustom` par `cachees` ET `supprimees` (l.975) ; `Etat.cachees` et `Etat.supprimees` sont bien des tableaux d'ids (l.2770-2771) — le `includes` matche. Le toast « Espèce masquée 🙈 » confirme un état réel ; guide, puces du spot et suggestions partagent le même filtre.
- **P2-1 ✅ tenu.** Comparaison à `meteoInitial` (l.1083-1084), posé à la création (l.1607) ET à l'édition (l.1622) — feuille intacte plus jamais faussement sale.
- **P2-2 ✅ tenu sur l'appareil, ❌ dégradé à l'export.** Tombe écrite `{id, nom, latin, statut, prudence}` (l.1194) ; `Etat.tombes` reconstruit si `x.nom` (l.2773, `perso: true`) ; `BASE_COMPLETE` inclut les tombes (l.1011) ; filet photo (l.2486) et badges (l.1560) couvrent la variété supprimée. **Réserve :** l'export sérialise les ids nus (l.2626) → tombes perdues à l'import (l.2664) → P2-1 28E.
- **P3-1 ✅ tenu en code, inobservable.** `BASE_COMPLETE().find` par `Etat.detailId` trouve la tombe (même id, l.1540) → ☠️ correct si le chemin est atteint ; il ne l'est pas (illustrations effacées → `basculerSpec` retourne avant, l.1524-1525) — le scénario réel exige la fermeture de la fiche (P3-1 28E).
- **P3-2 ✅ tenu.** `rendreCueillettes` passe par `infoEspeceArchive` (l.1560) ; tombe `perso: true` → vig repli « 🍄 » (l.1564, pas d'image cassée) ; badge MORTEL conservé pour les cueillettes d'une variété supprimée.
- **SW bump ✅ tenu.** `CACHE = 'cqm-v55'` (sw.js l.4) ; FICHIERS complet (21 especes + 105 specs + credits + mycoquebec.json — vérifié par script). Arbre git propre, HEAD = docs uniquement.

**Non corrigés (nouveaux de cette passe) :** P2-1 (tombes perdues à l'export), P2-2 (suppression perso sans confirmation ni undo), P3-1 (fiche fantôme), P3-2 (espèce masquée indésélectionnable d'un spot), P3-3 (c-date hors garde-fou) ci-dessus, et les résidus de la section 9.
