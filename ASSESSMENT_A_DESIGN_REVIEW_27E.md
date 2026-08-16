# Assessment A — Critique design (27e passe) : Cueillette Québec — édition Memphis

**Fichier évalué :** `index.html` (2805 lignes, HTML+CSS+JS mono-fichier) · **Docs :** `PRODUCT.md`, `DESIGN.md` · **SW :** `sw.js` (cqm-v54) · **Méthode :** lecture statique seule (Assessment A, aucun navigateur, aucun détecteur). Vérification des 7 claims de `bd04b49` (fix critique-26e) ligne par ligne — chaque ligne citée provient de `read_file`, de `git show` ou d'un grep Python `io.open`, aucune de search_files. HEAD = `238fc14` (docs uniquement), arbre git propre : l'état évalué est exactement le commit du fix.

**Note globale :** 5 claims sur 7 sont **tenus en code sans réserve** (P2-3, P3-1, P3-2, P3-3, SW bump). **P2-1 est tenu pour tout sauf un cas : la variété perso SUPPRIMÉE** — l'effacement du store retire l'enregistrement de `BASE_COMPLETE`, le claim « variété perso supprimée → mortel » du message de commit n'est pas tenu. **P2-2 contient un bug introduit par le fix : `c-meteo` est testé `!== ''` sur un select sans option vide → la feuille cueillette est TOUJOURS sale** — chaque fermeture d'une feuille intacte déclenche le garde-fou avec un message faux. Et la passe révèle un **P1 préexistant jamais signalé : « Masquer » une variété perso ne la masque pas** (`toutesEspeces` ne filtre jamais `especesCustom` par `Etat.cachees`). Score **38/40** (−1 vs 26E) : les six correctifs vérifiés sont réels, mais un P1 de fausse rétroaction et un P2 de faux positif (introduit ce round) plafonnent H1 et H4.

---

## 1. Verdict de spécificité design : 9/10 (inchangé)

Le diff du commit ne contient **aucun CSS** (38 insertions/11 suppressions, tout en JS + sw.js) : 0 couleur hors palette, 0 ombre floutée (batterie : 37 `box-shadow`, aucune avec flou — La Règle du Décalage Net tient), 0 `text-transform`/uppercase, 0 boîte système (le seul « window.confirm » est le commentaire l.235). Contrastes inchangés depuis 25E (4,61–13,5:1, tous AA). **Axes :** conceptuel ~90 % (carnet de chasse, vocabulaire mycologique, antipoison, verdicts ⚠️/☠️/✅, « le guide a le dernier mot ») · visuel ~90 % (une capture sans texte révèle Memphis-automne-champignon : zigzag, coins cassés, ombres dures, pois). Verdict : spécifique sur les deux axes ; la discipline tient sur une passe 100 % logique.

## 2. Évaluation holistique

- **Hiérarchie visuelle** — tenue. La fiche hybride a désormais un état composite synchronisé : titre (l.1540) ET corps (l.1542-1543) suivent le compteur — le mélange « titre dynamique + corps figé » de 26E est fermé. La carte idphoto garde sa hiérarchie badge → alertes → actions, dérivée d'un seul `r.statut` croisé.
- **Architecture de l'information** — le filet du flux photo consulte `BASE_COMPLETE` (l.1011-1033). **Résidu non traité :** le flux cueillette garde son patron inline (l.1556-1560) au lieu d'adopter `infoEspeceArchive` — trois fonctions de croisement coexistent maintenant (P3-2, §7).
- **Adéquation émotionnelle** — les vallées 26E sont refermées : plus de toast « confirmez la comestibilité » sous une carte MORTEL corrigée (l.2487, après croisement, `!connue.id`), plus de ☠️/⚠️ incohérent sur la checklist (l.1537-1538), corps du verdict cohérent à 0/5 (l.1484). **Nouvelle vallée introduite ce round :** le garde-fou de la feuille cueillette crie au loup à chaque fermeture, même d'une feuille intacte (P2-1, §7).
- **Découvrabilité** — inchangé : bandeau clé, FAB contextuel avec aria-label par vue (l.1049), étapes progressives, rien au hover.
- **Composition** — colonne 640 px, feuilles 84 vh, grille 2 colonnes conservées ; aucun changement structurel.
- **Typographie** — inchangée (aucun CSS modifié) : Fredoka 400/500/600/700 chargés (l.17), aucun poids hors jeu, Meta 400/12,5 px/0,85 conforme à DESIGN.md l.162.
- **Couleur** — 0 dérive dans le diff. La Règle du Rouge Mortel tient dans le code. Tension documentée (pas un drift) : la pastille numérotée de l'étape active est rouge (l.308) — DESIGN.md l.225 l'autorise explicitement, mais le rouge entre en collision sémantique avec la règle « rouge = danger seulement » (cf. §10).
- **Accessibilité** — ordre des branches Escape **toujours le bon** : `boiteVisible()` d'abord (l.1134-1139), feuille variété ensuite (l.1141-1146), feuille générique en dernier (l.1147-1148). Vérification par geste du garde-fou : voile (l.1093), poignées (l.1094), Escape (l.1147), **Annuler spot (l.1369) et Annuler cueillette (l.1654) désormais couverts** — plus aucune sortie non protégée sur spot/cueillette. Reste : `aria-invalid` = 0 partout (grep confirmé), lightbox sans piège Tab (l.2405-2425).
- **États** — boutons IA désactivés pendant les appels (l.1941-1942, 2336-2337, 2374-2375), états vides honnêtes. **Nouveau :** l'état « feuille cueillette sale » est calculé faux (toujours vrai) — l'état affiché ne correspond pas à l'état réel (P2-1).
- **Copy** — le message du garde-fou (« Quitter sans enregistrer ? Les champs remplis seront perdus. ») est honnête… sauf quand la feuille est intacte et qu'il tire quand même (P2-1). Le toast « Espèce masquée 🙈 » (l.1184) ment pour les variétés perso (P1-1).
- **Cas limites** — dates locales (l.752-755), import versionné, checklist réindexée au retrait (l.2358-2362). Nouveau : espèce **supprimée** depuis sa propre fiche → `BASE_COMPLETE` ne la trouve plus → glyphe ⚠️ au lieu de ☠️ (P3-1, §7).

## 3. Évaluation de charge cognitive : 1 échec / 8 (inchangé)

1. Focus unique ✅ · 2. Chunking ≤ 4 ✅ · 3. Regroupement visuel ✅ · 4. Hiérarchie ✅ · 5. Une chose à la fois ✅ · 6. Choix minimaux ≤ 4 ❌ — **étape 1 = 5 champs** (nom, latin, comestibilité, saison, prudence) + 2 boutons + 1 encart ; inchangé depuis 21E · 7. Mémoire de travail ✅ — le croisement guide/IA réduit la charge au moment critique ; **réserve :** la variété perso « masquée » reste visible, l'utilisateur doit se rappeler qu'il a masqué sans effet (P1-1) · 8. Divulgation progressive ✅.

**1 échec franc sur 8.**

## 4. Voyage émotionnel

Ouverture chaleureuse → guide → fiche hybride inchangés. **Les trois vallées 26E sont fermées dans leurs cas nominaux, vérifiées en code :** (a) la phalloïde masquée croise désormais `BASE_COMPLETE` avec synonymes/frappe (inclusion : « fausse morille » ⊂ « Gyromitre (fausse morille) », « phaloide » ⊂ « amanite phalloide » après `normNom` ; Levenshtein ≤ 2 sur nom+latin ; l.1015-1030) ; (b) le verdict-att affiche ⚠️/☠️ selon le statut même après masquage depuis sa fiche (l.1537) ; (c) le toast de coercition ne tire plus jamais en contradiction avec la carte (l.2487). **Vallées restantes ou nouvelles :** (i) la feuille cueillette intacte déclenche une confirmation qui prétend que des champs sont remplis — friction et fausse alerte au pire endroit (forêt, une main, P2-1) ; (ii) masquer une variété perso donne un toast de soulagement (« masquée 🙈 ») pendant que l'espèce reste en tête de liste — **un faux pic de sécurité**, le pire type de vallée pour ce produit (P1-1). Fin de journée : rappel d'export honnête, pas de faux pic.

## 5. Scores heuristiques Nielsen (0-4)

| # | Heuristique | Score | Problème clé |
|---|---|---|---|
| 1 | Visibilité de l'état du système | **3,5** (−0,5) | Le toast « Espèce masquée 🙈 » est une fausse confirmation d'état : la variété perso reste visible (l.1184 vs l.973-976) |
| 2 | Correspondance monde réel | 4 | Vocabulaire du carnet de chasse ; « le guide a le dernier mot » — métaphore juste |
| 3 | Contrôle et liberté | 4 | Annuler passe enfin par le garde-fou sur les 3 feuilles (l.1369, 1654) ; ordre Escape-modal vérifié l.1133-1149 |
| 4 | Cohérence et standards | **3,5** (−0,5) | Gestes enfin uniformes, mais le garde-fou affirme « champs remplis » sur une feuille intacte (l.1083 toujours vrai) — le système contredit l'état |
| 5 | Prévention des erreurs | 3,5 (=) | Filet guide masqué/supprimé + perso masqué + synonymes/frappes fermé en code ; plafonné par le claim « perso supprimée » non tenu (l.1190-1196) et le faux positif du garde-fou |
| 6 | Reconnaissance vs mémorisation | 4 | Noms requêtables sous toutes leurs formes ; croisement normNom + synonymes + Levenshtein + inclusion sur la base complète |
| 7 | Flexibilité / efficacité | 4 | IA remplit les 2 étapes, retry + repli modèle, ordre des images persistant, 21 guide:true **identité-vérifiés** (latins bidirectionnels vs ESPECES) |
| 8 | Esthétique minimaliste | 3,5 | Étape 1 à 5 champs, étape 2 ~13 éléments (inchangé) |
| 9 | Aide à la récupération d'erreurs | 4 | messageErreurIA par cause, parserJSONIA tolérant, import versionné, garde-fou de confirmation |
| 10 | Aide et documentation | 4 | Commentaires référencent la bonne passe (P2-1 25e/26e l.1009, P3-2/P3-3 26e l.1536/1541) ; DESIGN.md à jour |

**Total : 38/40 (−1 vs 26E).** Les correctifs 26E sont vérifiés et réels ; la baisse est honnête : un P1 de fausse rétroaction (masquer perso sans effet — préexistant, premier signalement) et un P2 de faux positif (garde-fou c-meteo — introduit par ce round) pèsent sur H1 et H4, offset des six fixes confirmés.

## 6. Forces spécifiques

1. **`BASE_COMPLETE` est le bon patron, au bon prix.** `infoEspeceArchive` (l.1012-1033) laisse au chemin visible toute sa finesse (synonymes, Levenshtein, inclusion) et ne consulte la base complète (guide+perso, sans filtre de visibilité) qu'en dernier recours, avec le flag `archivee:true` qui gouverne le seul rendu sensible (bouton « Voir la fiche du guide » masqué, l.2526). Et le surclassement `GRAV` est **upgrade-only** (l.2483-2485) : un faux appariement flou ne peut jamais adoucir un verdict — la direction de l'erreur est bornée vers la prudence.
2. **La discipline des données tient sur l'axe que l'utilisateur vit vraiment (hors-ligne).** 21/21 espèces du guide avec `img/especes/*.jpg` locales et dans le SW ; 105/105 spécificités dans `SPECS_DEFAUT` avec `img/specs/*.jpg` locales (SW : 106 entrées specs = 105 jpg + credits.json) ; les 21 `guide:true` de `img/mycoquebec.json` correspondent **par identité** aux 21 latins d'`ESPECES` (aucun écart dans les deux sens — vérifié par script, pas par comptage).
3. **La réparation 17E survit à un troisième round d'ajouts de chemins de confirmation.** Le garde-fou gagne deux nouveaux déclencheurs (Annuler spot/cueillette, l.1369/1654), mais la branche Escape teste `boiteVisible()` avant tout (l.1134-1139) : la confirmation ne peut pas se ré-empiler. Le piège que la passe 17E avait payé cher est évité par construction, et la vérification est cette fois par geste (voile, poignée, Escape, Annuler — chacun tracé séparément).

## 7. Problèmes prioritaires

**P1-1 (NOUVEAU, PRÉEXISTANT — FAUSSE RÉTROACTION) — « Masquer » une variété perso ne la masque pas.** `toutesEspeces` (l.973-976) filtre `ESPECES` par `Etat.cachees` mais **jamais** `especesCustom` : une variété perso masquée via la modale (l.1165-1167 promet « masquez-la temporairement », l.1180-1186 écrit `caches` + toast « Espèce masquée 🙈 ») reste dans le guide, dans les puces du spot et dans les suggestions. Le toast confirme un état qui n'existe pas, la feuille de restauration (l.1899) propose de « restaurer » une espèce qui n'a jamais quitté la liste — et la 26E a écrit son P2-1 en croyant que le masquage perso fonctionnait (prémisse fausse). *Fix :* filtrer `especesCustom` par `Etat.cachees` dans `toutesEspeces` (le filet `BASE_COMPLETE` reste volontairement non filtré — la sécurité ne dépend pas du rangement) ; utiliser `infoEspeceArchive` dans `rendreCueillettes` pour que les badges survivent.*

**P2-1 (NOUVEAU, INTRODUIT PAR LE FIX 26E — FAUX POSITIF DU GARDE-FOU) — `c-meteo` est testé `!== ''` sur un select sans option vide.** Le select météo (l.592-598) n'a aucune option vide et la feuille s'ouvre sur « 🌞 Ensoleillé » (l.1603) : `String($('c-meteo').value || '') !== ''` (l.1083) est **toujours vrai** → la feuille cueillette est toujours « sale » → chaque fermeture (voile, poignée, Escape, Annuler) d'une feuille **intacte** ouvre la confirmation « Quitter sans enregistrer ? Les champs remplis seront perdus. » — message faux, friction en forêt, alarm fatigue sur le seul garde-fou de l'app. La suggestion 26E était explicite : comparer au défaut. *Fix :* `$('c-meteo').value !== '🌞 Ensoleillé'` (ou traiter le défaut comme valeur nulle).*

**P2-2 (CLAIM NON TENU — SÉCURITÉ) — « variété perso supprimée → mortel » n'est pas tenu en code.** `choix-supprimer` perso efface l'enregistrement des stores `especes` et `illustrations` (l.1190-1196, inchangé) : une variété perso MORTELLE supprimée n'existe plus dans `BASE_COMPLETE` (l.1011). IA « comestible 95 % » sur cette espèce → `connue.id = null` → badge vert possible. Le filet couvre bien les perso **masquées** (elles restent dans `especesCustom`) — le message de commit surestime la couverture d'un cran. *Fix :* à la suppression d'une variété perso, écrire une pierre tombale dans `supprimees` (aujourd'hui réservé aux ids du guide) avec `{id, nom, statut}` et l'inclure dans `BASE_COMPLETE` ; ou interdire la suppression définitive d'une variété MORTELLE sans export préalable.*

**P3-1 (RÉSIDU DU CLAIM P3-2 — BORD) — glyphe ⚠️ sur une fiche perso MORTELLE supprimée en cours de consultation.** Le masquage est couvert (l.1537 trouve l'espèce dans `BASE_COMPLETE`), mais la **suppression** depuis sa propre fiche (modale l.1187-1196) efface l'enregistrement : `basculerSpec` → `BASE_COMPLETE().find(...)` → `undefined` → `glypheAtt = '⚠️'` (l.1538) sur une carte rouge `verdict-danger-att`. Même racine que P2-2. *Fix :* capturer le statut (`nonComestible`) dans `Etat` à l'ouverture de la fiche (suggestion 26E déjà) ou appliquer la pierre tombale de P2-2.*

**P3-2 (RÉSIDU 26E §9 DURCI) — les cueillettes d'une variété perso supprimée perdent leur badge de sécurité.** `rendreCueillettes` (l.1556-1560) croise `infoEspece` (visible) puis un repli `ESPECES`-only sur `c.especeId` : pour une perso supprimée, `statutEff = null` → aucune pastille. Trois fonctions de croisement coexistent (`infoEspece`, `infoEspeceArchive`, patron inline). *Fix :* `const info = infoEspeceArchive(c.espece)` avec `c.especeId` comme repli d'identité — une seule fonction de vérité.*

## 8. Red flags par persona

- **Jonathan en forêt, une main, sans réseau** : le moment de vérité (photo ID) est protégé pour le guide masqué/supprimé ET les perso masquées (l.1011-1033, 2481-2485). **Pire moment :** ouvrir la feuille cueillette d'un tap maladroit et devoir répondre à une confirmation qui affirme que des champs sont remplis alors qu'il n'a rien touché (P2-1) ; ou photographier une **variété perso MORTELLE qu'il a supprimée** — le filet se tait (P2-2).
- **Proche débutant (via export/import)** : la règle simple « ☠️ = ne jamais manger » tient (glyphe selon statut, toast après croisement). **Pire moment :** masquer une variété qui lui fait peur, voir le toast « Espèce masquée 🙈 », puis la retrouver en tête du guide — il apprend à douter de toutes les confirmations de l'app (P1-1).
- **Utilisateur au clavier / lecteur d'écran** : ordre Escape-modal sûr, verdict-att cohérent en audio, Annuler protégé comme le voile. **Pire moment :** Tab sort de la lightbox (l.2405-2425, résidu) ; et la confirmation du garde-fou s'annonce pour une feuille vide (P2-1).

## 9. Observations mineures

**Nouveaux :**
- Le garde-fou de la feuille cueillette est le seul endroit où le message peut être faux (c-meteo) — le tester une fois à la main l'aurait montré : le fix P2-2 26E n'a pas été exercé sur la valeur par défaut.
- Trois fonctions de croisement coexistent désormais (`infoEspece`, `infoEspeceArchive`, patron inline l.1558) — la question 26E « une seule fonction ? » reste ouverte et s'aggrave.
- Commentaire l.2643 « P2-2 : vérification de la version » — numérotation d'une ancienne passe ; s'ajoute au « P1-5 » de l.2473 (signalé 25E/26E, toujours là).

**Résidus inchangés (non re-scorés, re-confirmés présents en 27E) :** `rendreBandeauCle` insère un `<button>` dans un `<p class="note">` (l.2441-2444, HTML invalide) · `p-cle` sans label (l.460) · `g-recherche` sans label (l.411) · toast de pré-remplissage sans mention du statut transféré (l.2558) · `retirerIllu` ne re-rend pas la vue détail sous-jacente (l.2354-2371) · PRODUCT.md l.39 (`especesCustom`/`cachees`) vs code (`especes`/`caches`, l.792-793) · échec silencieux de `chargerBaseMyco` → « 0 espèces de la base » mensonger hors-ligne (l.1662-1669, 1706) · focus perdu sur les selects de filtre (re-rendu `rendreFiltres`, l.1389-1403) · `alt="photo"` générique (l.1226) · `ouvrirMyco` sans message hors-ligne (l.2402-2404) · `.mois-col .lab` 10,5 px (l.339) · cache SW non borné pour les GET réussis (sw.js l.160-163) · `aria-invalid` : 0 partout (re-grep confirmé), validation toast-only · `COULEURS_MOIS` cycle 6×2 sans sémantique de saison (l.2570) · lightbox sans piège à focus (l.2405-2425) · `feuilleSaisieSale` via `document.getElementById` au lieu de `$` (l.1074/1079/1088, style).

## 10. Questions provocatrices

1. Pourquoi `toutesEspeces` n'a jamais filtré `especesCustom` par `Etat.cachees` — et pourquoi le P2-1 de la 26E a été écrit comme si le masquage perso fonctionnait ? Qui possède la vérité de visibilité des variétés perso ?
2. Supprimer une variété perso MORTELLE vaut-il renoncement à la protection du filet (état actuel, claim non tenu), ou la sécurité exige-t-elle une pierre tombale `{nom, statut}` dans `supprimees` — et qui la purge, quand ?
3. Un select avec une valeur par défaut est-il « sale » par définition, ou seulement quand il diffère du défaut ? Le garde-fou doit-il dire la vérité (« champs remplis ») ou apprendre à distinguer « rempli » de « modifié » ?
4. Le message du garde-fou tire sur une feuille intacte à chaque fermeture : à quel taux de faux positifs la confirmation devient-elle elle-même le danger (habituation, puis vraie perte ignorée) ?
5. Trois filets coexistent : `infoEspece` (visible+flou), `infoEspeceArchive` (base complète), patron inline des cueillettes (l.1558). Quand `rendreCueillettes` adopte-t-il `infoEspeceArchive` — et qui décide de la source de vérité unique ?
6. La fiche d'une espèce supprimée reste ouverte (`recharger` ne re-rend pas `detail`) : doit-elle se fermer, ou rester consultable — et dans ce dernier cas, avec quel glyphe quand `BASE_COMPLETE` ne la trouve plus (perso supprimée, l.1537-1538) ?
7. La pastille numérotée rouge de l'étape active (l.308) est documentée dans DESIGN.md (l.225), mais la Règle du Rouge Mortel dit « rouge = danger seulement » : l'exception documentée vaut-elle toujours la collision sémantique sur un composant de navigation de formulaire ?

---

**Claims `bd04b49` vérifiés** (`git show --stat` : index.html +38/−11, sw.js ±1 — conforme) :
- **P2-1 ✅ tenu, avec une réserve.** `BASE_COMPLETE` l.1011 ; exact + Levenshtein ≤ 2 + inclusion sur guide+perso l.1015-1030 ; branché l.2481 ; surclassement GRAV upgrade-only l.2483-2485 ; fiche masquée si `archivee` l.2526-2528. Fausse morille masquée → gyromitre MORTEL (inclusion) ; « phaloide » → phalloïde MORTELLE (normNom + inclusion) ; perso masquée → trouvée (reste dans `especesCustom`). **Réserve : « variété perso supprimée » non couverte** — l'effacement l.1190-1196 retire l'enregistrement de la base (P2-2).
- **P2-2 ✅ tenu pour les puces et c-spot, ❌ bug pour c-meteo.** Puces l.1077, c-spot l.1082 corrects ; c-meteo l.1083 toujours vrai (select sans option vide, défaut l.1603) → feuille cueillette toujours sale (P2-1).
- **P2-3 ✅ tenu.** `s-cancel` l.1369 et `c-cancel` l.1654 → `fermerFeuilleAvecGardeFou` ; sémantique d'Annuler désormais uniforme sur les 3 feuilles.
- **P3-1 ✅ tenu.** Toast déplacé après le croisement, gated `!statutValide && !connue.id` (l.2487) — plus de contradiction possible avec une carte corrigée par le guide.
- **P3-2 ✅ tenu, avec un bord.** `BASE_COMPLETE().find` l.1537 ; espèce du guide masquée depuis sa fiche → ☠️ conservé. **Bord :** perso **supprimée** depuis sa fiche → `undefined` → ⚠️ (P3-1).
- **P3-3 ✅ tenu.** `span.corps-att` l.1484 + mise à jour dynamique l.1542-1543 — le corps suit le compteur.
- **SW bump ✅ tenu.** `CACHE = 'cqm-v54'` (sw.js l.4) ; FICHIERS complet (21 especes + 105 specs + credits + mycoquebec.json — vérifié par script). Arbre git propre, HEAD = docs uniquement. Données re-vérifiées par identité : 21 `guide:true` ↔ 21 latins ESPECES (bidirectionnel exact), 105/105 specs locales dans SW.

**Non corrigés (nouveaux de cette passe) :** P1-1 (masquer perso sans effet), P2-1 (c-meteo toujours sale), P2-2 (claim perso supprimée non tenu), P3-1 (glyphe ⚠️ après suppression), P3-2 (badge cueillette perdu) ci-dessus, et les résidus de la section 9.
