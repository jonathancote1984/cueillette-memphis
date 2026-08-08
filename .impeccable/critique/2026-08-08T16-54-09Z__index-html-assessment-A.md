# Assessment A — Revue design · Cueillette Québec, édition Memphis

**Fichier évalué :** `index.html` (1728 lignes, HTML/CSS/JS monolithique) — lecture source uniquement, aucun navigateur, aucune modification.
**Vérité produit :** `PRODUCT.md` (63 lignes) — carnet de chasse personnel + identification à égalité, 100 % hors-ligne, PWA mono-fichier, style Memphis AUTOMNE/TERRE, alertes MORTEL/antipoison non négociables.
**Documents lus aussi :** `README.md`, `manifest.json`, `sw.js` (cache `cqm-v10`).
**Méthode :** lecture intégrale du fichier + calculs de contraste WCAG (luminance relative, ratios vérifiés deux fois).

---

## 1. Verdict de spécificité design

**Deux axes, test du « screenshot sans texte » :**

- **Axe conceptuel : ~90 %.** Le vocabulaire est profondément ancré dans CE produit : « boisé du rang 4 » (placeholder spot), « coins secrets », règle d'or « en cas de doute, on ne mange pas » (l.351), centre antipoison 1-800-463-5060 (l.1089, 1558), saisons de cueillette (« Mai à juin (printemps) », l.724), fausse chanterelle vs chanterelle (l.703), gyromitre vs morille « la confusion la plus meurtrière du printemps » (l.798), « récolte » par panier, météo avec 🌧️/🌫️. Le français du Québec est tenu partout. Aucun de ces choix ne survivrait à un autre domaine.
- **Axe visuel : ~80 %.** Le système Memphis est réellement exécuté, pas plaqué : bordures 3 px, coins cassés, ombres dures sans flou, zigzag d'en-tête (l.336-338), pois au body (l.28-29), formes géométriques SVG (l.316-320), Fredoka, palette automne/terre (tokens l.16-20), y compris dans les états vides, les modales et les confirmations — aucune boîte système native nulle part (0 `alert(`/`confirm(` natif, vérifié par grep + lecture). MAIS : la grammaire (zigzag + pois + coins cassés + ombres dures) est celle du mouvement Memphis générique, et elle est partagée avec l'édition classique « carnet de pêche » du même auteur. Sans le texte ni les emojis 🍄/🧺/📍, on devinerait « carnet de récolte nature ludique », pas spécifiquement « champignons du Québec ».

**Verdict : ancré, non interchangeable.** Ce n'est pas un template SaaS repeint : le langage visuel est décliné avec discipline sur chaque état, et le langage conceptuel est irréductible au domaine. Réserve : l'axe visuel resterait crédible pour un carnet de pêche ou de chasse — la spécificité « champignon » repose beaucoup sur les emojis et les photos.

---

## 2. Évaluation holistique

- **Hiérarchie visuelle (bonne, 2 faiblesses).** H1 incliné + zigzag → titre de vue en pastille → cartes ; l'échelle est tenue (21/20/18/15,5/14/12,5 px). Faiblesse 1 : les 4 cartes de stats (l.1613-1618) ont un poids visuel strictement égal (jaune/bleu/vert/rose, même taille de valeur 24 px) pour des métriques inégales — « Dernière sortie » rivalise avec « Total récolté » (l.1617). Faiblesse 2 : la vue Identifier empile 4 jobs (alerte → ID photo → recherche → filtres) avant la liste, ce qui est une hiérarchie correcte mais dense.
- **Architecture de l'information (incohérence terminologique + un rangement discutable).** 4 onglets, complet (spots/guide/cueillettes/stats) — rien d'atteignable n'est innavigable. MAIS : la même entité s'appelle « Cueillettes » (onglet, l.397), « Mon journal » (titre, l.363) et « Sorties » (carte stats, l.1615) — triple appellation de la métrique la plus vue. La sauvegarde export/import ET l'effacement total vivent dans la carte « 💾 Sauvegarde » sous l'onglet « Statistiques » (l.374-383) : l'action anti-perte la plus critique du produit est rangée sous une étiquette qui ne la nomme pas.
- **Adéquation émotionnelle (forte, sauf 2 vallées).** Le registre « carnet chaleureux » est tenu jusque dans les états vides (« Appuyez sur le bouton rose pour ajouter votre premier coin secret ! », l.967 ; « pour noter votre première récolte ! », l.1138). L'offline n'est jamais montré en rouge destructif — bonne valence (offline = mode normal ici). Les deux vallées : (1) la fonction phare (identification photo) exige une clé API dont le chemin de configuration est introuvable (détail infra) ; (2) la feuille d'espèce est un mur de formulaire froid au milieu d'un carnet chaleureux.
- **Découvrabilité (le point faible n°1).** « 📷 Appareil photo » (l.353) → sans clé : toast éphémère de 2,2 s (l.634) « Ajoutez votre clé Gemini pour l'identification IA (aistudio.google.com/apikey) » (l.1530). La clé se configure dans un `<details>` « 🔑 Clé Gemini » (l.565-569) situé au bas de la feuille d'ajout d'espèce — qu'on n'ouvre jamais si on veut juste identifier. Aucun onboarding, aucune page d'aide in-app. Le badge compteur du header (l.334) semble cliquable (pastille, title tooltip) et ne l'est pas.
- **Composition (solide mobile).** max-width 640 px, une colonne, FAB contextuel (📍 en spots, ＋ ailleurs, caché en stats/détail, l.844-845), feuilles bottom-sheet 84 vh (l.249) avec poignée (l.254), voile, 4 onglets avec indicateur d'onglet actif en zigzag. 69 styles inline ponctuels — tolérable, mais signe de tokens d'espacement incomplets.
- **Typographie (bien).** Fredoka 400-700 avec repli système (l.24), aucune césure forcée, aucun uppercase forcé, tailles cohérentes. Seul accroc : 3 tailles ad hoc inline (16,5/17 px) sans token.
- **Couleur (palette tenue, micro-dérives + 2 contrastes en échec).** Tokens respectés ; hors palette : les couleurs d'onglets actifs `#0B6E96/#B3540B/#0E8F6B/#C2185B` (l.77-80), le dégradé header `#9A4A12→#D9A441` (l.34), fonds d'alertes `#F6DFD2/#F4E3C3` (l.202, 208), barre vide `#D8C9AC` (l.1643) — dérives assumées mais non documentées dans PRODUCT.md. Contrastes calculés (WCAG) : voir Accessibilité.
- **Accessibilité (lacunes réelles).** Détail complet en 5. Points saillants : items du guide = `div` cliquables sans `role`/`tabIndex` (l.1069) ; puces de filtre = `span` cliquables (l.1050-1051) ; 24 `onclick` inline ; aucune gestion Échap ni retour de focus ; zéro `prefers-reduced-motion` (animations `pop` l.96-97, transitions de feuilles) ; `alt=""` sur les vignettes photo de spots/cueillettes (l.971, 1143) alors qu'elles portent l'information visuelle principale ; `aria-label="Ajouter"` sur le FAB (l.392) vague (ajouter quoi ?) ; focus ring jaune ≈ 2,2:1 sur fond blanc (anneau de focus peu visible, la bordure noire 3 px sauve la détection).
- **États (bons états vides, 2 trous).** États vides chaleureux et guidants partout (spots, cueillettes, guide, tops, mois). Trou 1 : l'identification « inconnue » dit « Impossible d'identifier avec certitude » (l.1544) — bonne prudence, mais aucun rappel de la règle d'or dans ce message (le moment où l'utilisateur a le plus besoin du garde-fou). Trou 2 : le repli silencieux vers localStorage si IndexedDB échoue (l.653) — l'utilisateur ne sait jamais qu'il est en mode fragile.
- **Copy (bonne dans l'ensemble, 3 accrocs).** Langue québécoise naturelle, placeholders riches (« Quantité par panier, qualité, autres espèces vues… », l.492). Accrocs : « Sorties » vs « Cueillettes » vs « Mon journal » ; le bouton poubelle 🗑️ des items du guide masque (réversible, l.1076) alors que le même 🗑️ sur les variétés perso supprime (irréversible) — même icône, deux sémantiques ; erreur GPS brute « err.message » en anglais possible (l.1036).
- **Cas limites (bien gérés pour la plupart).** Spot supprimé → ses cueillettes survivent et les stats affichent « Spot supprimé » (l.1628) : bon. Masquage d'espèce → les cueillettes passées perdent silencieusement leur badge de statut (infoEspece passe par toutesEspeces() qui exclut les masquées, l.825-833) : le journal change de sens sans prévenir. Lat/lng acceptées sans validation (« abc,def » → lien Google Maps cassé, l.973). Import : écrase tout avec UNE confirmation (l.1667) vs double confirmation pour « Tout effacer » (l.1681-1683) — asymétrie dangereuse. Export : dataURL photo incluses → fichier potentiellement de plusieurs Mo (acceptable, non documenté).

---

## 3. Checklist charge cognitive — **6 échecs sur 8**

| # | Item | Verdict | Preuve |
|---|------|---------|--------|
| 1 | Focus unique | ❌ | L'écran « Identifier » sert 4 jobs : consulter, filtrer, identifier par photo, ajouter une variété (FAB, l.854). Les 3 autres onglets passent (1 job chacun). |
| 2 | Chunking ≤ 4 | ❌ | Liste du guide : jusqu'à 21 items empilés sans regroupement ni pagination ; feuille d'espèce : 13 champs visibles d'un coup (l.514-569) ; liste de cueillettes non paginée. Les 4 cartes stats et les 4 filtres, eux, passent. |
| 3 | Regroupement visuel | ✅ | Cartes, `grille2` par paires, sections « guide-sujet » (l.293), groupes photo/météo/spot bien délimités par les bordures 3 px. |
| 4 | Hiérarchie claire | ✅ | Échelle constante h1→titre-vue→carte→sujet ; seule entorse : 4 cartes stats à poids égal pour métriques inégales. |
| 5 | Une chose à la fois | ❌ | La feuille d'espèce mêle 4 workflows dans une seule sheet : saisie manuelle + « Détails par IA » + photo (4 boutons) + configuration de clé. |
| 6 | Choix minimaux ≤ 4 | ❌ | Filtres 4 ✅, statut 4 ✅, mais météo = 5 options (l.482-488) ; section photo de la feuille espèce = 4 boutons + zone (l.555-562) ; feuille d'espèce = 13 champs + 6 boutons + 2 actions visibles. |
| 7 | Mémoire de travail | ❌ | L'utilisateur doit se rappeler où se cache la clé Gemini (dans le `<details>` d'une feuille d'ajout) ; que l'export est sous « Stats » ; que masquer une espèce efface les badges de statut de ses vieilles cueillettes ; « Spot supprimé » remplace le nom du coin dans les tops. |
| 8 | Divulgation progressive | ❌ | La feuille d'espèce déploie tout d'un coup ; la fiche guide est intégralement déroulée (description + caractéristiques + confusions + galerie) ; l'alerte de clé manquante est un toast de 2,2 s au lieu d'un panneau persistant. Seul bon exemple : le `<details>` de la clé (l.565). |

**Total : 6 échecs / 8.** Le motif dominant : les *feuilles* (spot, cueillette, espèce) violent tout — la feuille d'espèce est le pire cas (13 champs visibles + 6 boutons photo/IA + 2 actions, l.514-573).

---

## 4. Parcours émotionnel (peak-end)

- **Entrée (peak modéré).** Header incliné + zigzag + formes SVG + animation `pop` des vues (l.96-97) : accueil chaleureux. État vide de spots guidant (« bouton rose ») : bonne première impression.
- **Vallée n°1 — la fonction phare bloquée.** Jonathan ramasse un champignon douteux, clique « 📷 Appareil photo » → toast 2,2 s « Ajoutez votre clé Gemini » (l.1530). Pas de chemin dans l'app, pas de panneau, une URL externe dans un toast éphémère. C'est le moment le plus à risque émotionnel ET physique de la journée.
- **Vallée n°2 — le mur de saisie.** La feuille d'espèce (13 champs) refroidit l'élan « je veux documenter ma trouvaille ». Et une cueillette à la fois : 20 chanterelles = 20 formulaires.
- **Vallée n°3 — erreurs IA sans guidance.** « ⚠️ IA indisponible (API 400) » (l.1345) ou « Génération impossible : … » (l.1490) : pas de prochaine étape proposée.
- **Reassurance aux moments à haut risque : excellente sur le MORTEL.** Fiche d'espèce mortelle : alerte rouge ☠️ + centre antipoison 1-800-463-5060 (l.1088-1091). Identification photo mortelle : même alerte dans le résultat (l.1557-1560). Filtre dédié « ☠️ Mortels ». Prompt IA forcé à « inconnu » en cas de doute (l.1591). Double confirmation pour l'effacement total (l.1681-1683). **Deux trous de reassurance :** (1) import JSON = écrasement total avec une seule confirmation (l.1667) — le geste le plus destructeur après l'effacement n'a pas le même filet ; (2) une identification à « Confiance : 62 % » affiche un badge « Comestible » vert sans seuil ni mise en garde (l.1554-1556) — fausse réassurance sur un sujet où l'erreur est fatale.
- **Fin de journée (peak réel, pas de faux peak).** Le dernier geste typique = « Cueillette enregistrée ✅ » ou l'export. Pas de célébration de fin de sortie (pas de récap « 3,2 kg aujourd'hui »), mais les stats colorées compensent. Aucun « tout est parfait » mensonger nulle part — les compteurs sont câblés aux vraies données (vérifié l.1609-1645).
- **Valence :** offline jamais montré en rouge (correct pour une PWA offline-first) ; les erreurs réseau IA sont en orange informatif, pas destructif.

---

## 5. Heuristiques Nielsen — **29/40**

| # | Heuristique | Score | Note clé |
|---|-------------|-------|----------|
| 1 | Visibilité de l'état du système | 3/4 | Badge compteur live (l.1708), toasts, états vides, spinner d'analyse « L'IA examine chapeau, lames, pied et habitat (10-20 s) » (l.1537). Pénalités : repli localStorage silencieux, aucune indication d'écriture en cours. |
| 2 | Correspondance monde réel | 4/4 | Métaphores champêtres (spots, paniers, météo, coins secrets), québécois naturel, emojis familiers. |
| 3 | Contrôle et liberté | 4/4 | Annuler partout, poignée + voile + bouton pour fermer, masquage réversible, double confirmation destructeur. |
| 4 | Cohérence et standards | 2/4 | Design system très tenu, mais 🗑️ = masquer OU supprimer selon le contexte ; Cueillettes/Mon journal/Sorties ; zone photo qui affiche un CTA mais n'agit pas ; FAB 📍/＋ variable. |
| 5 | Prévention des erreurs | 3/4 | Doubles confirmations, validations de champs requis avec focus (l.1011, 1195), import validé. Pénalités : import mono-confirmation, lat/lng non validées, statut « MORTEL » sélectionnable sans garde-fou dans la feuille (l.528). |
| 6 | Reconnaissance plutôt que rappel | 3/4 | Datalist d'espèces, filtres, placeholders riches. Pénalités : clé Gemini à se rappeler, export à se rappeler (Stats), aucune suggestion des dernières espèces/spots utilisés. |
| 7 | Flexibilité et efficacité | 3/4 | GPS one-tap avec précision affichée (l.1030-1034), date du jour par défaut (l.1166), météo par défaut. Pénalité majeure pour le persona form-heavy : une seule cueillette par formulaire, pas de duplication. |
| 8 | Esthétique et minimalisme | 3/4 | Identité assumée et cohérente. Pénalités : feuille d'espèce surchargée (13 champs), alerte « Règle d'or » permanente au-dessus des actions (l.351), carte Sauvegarde dans Stats. |
| 9 | Aide à la récupération | 3/4 | « Fichier invalide — import annulé » (l.1677), restauration sélective avec compteur, erreurs IA explicites. Pénalités : pas de retour de focus après modale, err.message anglais possible (l.1036). |
| 10 | Aide et documentation | 1/4 | **Aucune aide in-app ni onboarding.** La seule documentation est l'alerte « Règle d'or » et le README (hors app). La configuration de la clé Gemini n'est expliquée nulle part à l'endroit où elle est exigée. |

**Profil :** très fort sur l'identité, la prévention et la liberté ; faible sur la documentation, la cohérence sémantique et le support des utilisateurs à haute fréquence de saisie.

---

## 6. Forces, problèmes, personas, observations, questions

### Forces (3)

1. **Le système Memphis est exécuté, pas décoré** — zéro boîte système native, tokens tenus, bordures 3 px/ombres dures/coins cassés/zigzag/pois déclinés jusque dans les confirmations (l.221-235), états vides, toasts et FAB. Une discipline que la plupart des apps « ludiques » perdent à la première modale.
2. **La sécurité est un citoyen de premier rang du design** — alerte MORTEL + antipoison dans la fiche (l.1088-1091) ET dans le résultat d'identification photo (l.1557-1560), filtre « ☠️ Mortels » dédié, prompt IA qui force « inconnu » en cas de doute (l.1591), double confirmation d'effacement (l.1681-1683). Le principe 1 du PRODUCT.md est respecté là où ça compte.
3. **Les états vides et l'interaction mobile sont soignés** — états vides chaleureux et guidants (l.967, 1138), feuilles bottom-sheet avec poignée + voile + Annuler (3 voies de sortie), FAB contextuel, GPS one-tap avec précision affichée. L'app se comporte comme une app native, pas comme une page web.

### Problèmes prioritaires (5)

- **P1-1 · Identification IA : la fonction phare bloque sur une clé introuvable.** `index.html:1530` (toast) + `:565-569` (clé dans un `<details>` au bas de la feuille d'ajout d'espèce). L'utilisateur en forêt avec un champignon suspect reçoit un toast de 2,2 s renvoyant vers une URL externe, sans chemin in-app. **Correctif :** bandeau persistant sur la vue Identifier quand la clé manque (« Configurer la clé → » qui ouvre la feuille d'espèce avec le `<details>` déplié et le champ focus), ou onboarding au premier lancement.
- **P1-2 · Confiance IA affichée sans seuil : fausse réassurance sur un sujet mortel.** `index.html:1554-1556` : « Chanterelle commune + badge Comestible vert + Confiance : 62 % ». Le produit promet « identifier avec confiance » (PRODUCT.md) ; 62 % n'est pas de la confiance, et rien ne le dit. **Correctif :** seuils explicites (≥ 90 % vert, 60-89 % « vérifiez avec le guide », < 60 % → traiter comme inconnu) + rappel de la règle d'or dans le résultat d'identification.
- **P2-1 · L'import écrase toutes les données avec une seule confirmation.** `index.html:1667` vs double confirmation de l'effacement (l.1681-1683). Une mauvaise manipulation = carnet entier remplacé. **Correctif :** double confirmation ou résumé avant écrasement (« Remplacer 214 cueillettes, 12 spots ? »).
- **P2-2 · La zone photo ment : le CTA le plus visible est inerte.** `index.html:1045` (et :1217, :1440) : la zone affiche « 📷 Appareil photo ou galerie », a `cursor:pointer`, mais un clic ne fait rien quand elle est vide — seuls les petits boutons « Appareil/Galerie » en dessous fonctionnent. **Correctif :** clic sur zone vide = ouvrir le choix photo (ou au minimum retirer le placeholder trompeur).
- **P2-3 · Contraste en échec sur des composants porteurs.** Calculs WCAG (luminance vérifiée deux fois) : texte noir sur `--bleu #8A5A2B` = **2,91:1** (boutons « Modifier », « Utiliser ma position », « Exporter », `guide-sujet` l.293) ; noir sur `--rose #C1502E` = **3,62:1** (boutons « Appareil » 13 px, FAB — le FAB passe en texte large 3:1) ; `#0E8F6B` des mesures kg sur blanc = **3,78:1** (l.133, 14 px bold) ; titre header noir sur la portion sombre du dégradé `#9A4A12` ≈ **2,7:1** (estimation, dégradé variable — échoue même en texte large) ; focus ring jaune sur blanc ≈ **2,2:1**. Les bons : noir/vert 4,61:1, noir/jaune 7,59:1, blanc/rouge 6,07:1, noir/blanc 15,9:1. **Correctif :** texte blanc sur bleu et rose, ou éclaircir les fonds (`#A8763F`, `#D96A45`) ; `#0E8F6B` → `#0B7A55` ; assombrir le départ du dégradé ou passer le titre en blanc.
- *(P2-4 · Export enfoui :* la seule protection contre la perte du carnet est sous « Statistiques » (l.374-383). Correctif : onglet ou entrée « Sauvegarde » nommée, ou bandeau « Jamais exporté » sur la vue Stats.)

### Red flags par persona (Sam, Casey, Riley)

- **Sam — mobile distrait (forêt, une main, soleil).** Clique la grande zone photo → rien (P2-2). Clique « Appareil photo » pour identifier → toast éphémère de clé (P1-1). Le FAB change d'icône selon l'onglet (📍 vs ＋, l.845) : pattern subtil pour un usage distrait. **Pire moment :** champignon suspect en main, identification impossible, aucune piste dans l'app pour débloquer — risque réel de consommation sans identification.
- **Casey — form-heavy (saisit chaque récolte).** 13 champs pour une variété (l.514-569) ; une seule cueillette par formulaire, aucun « dupliquer la dernière », pas de suggestion des dernières espèces — 20 chanterelles = 20 allers-retours feuille + 20 fois « 💾 Enregistrer » (l.504). **Pire moment :** la 12ᵉ cueillette de la journée, quand la fatigue transforme la feuille en corvée.
- **Riley — terrain hors-ligne (vendue « 100 % hors-ligne »).** Les données et le guide sont hors-ligne (vrai, sw.js cache-first) ; mais l'identification IA et l'illustration IA exigent réseau + clé — la fonction phare meurt en forêt sans préavis : les boutons 📷/🖼️ sont là, l'échec arrive 10-20 s plus tard (l.1537) ou au toast de clé. **Pire moment :** le jour où l'app est le plus nécessaire — sans réseau — est celui où sa promesse d'identification s'évapore.

### Observations mineures

- 69 styles inline : tokens d'espacement incomplets (acceptable, à documenter).
- Couleurs hors palette non documentées : onglets actifs `#0B6E96/#B3540B/#0E8F6B/#C2185B`, dégradé `#9A4A12`, fonds d'alertes `#F6DFD2/#F4E3C3`, barre vide `#D8C9AC`.
- Badge du header (l.334) non cliquable avec tooltip — semble interactif.
- `alt=""` sur les vignettes photos de spots et cueillettes (contenu informatif réel, l.971/1143).
- Toast à 2,2 s trop court pour un message contenant une URL (clé Gemini, l.1530).
- Erreur GPS possible en anglais brut via `err.message` (l.1036).
- « Spot supprimé » agrège potentiellement plusieurs coins différents dans les tops (l.1628) — correct mais grossier.
- `loading="lazy"` uniquement sur les vignettes du guide ; les dataURL de photos spots/cueillettes chargent tout d'un coup (lourdeur possible avec une saison complète).
- La date utilise le picker natif `type="date"` — seule entorse assumée au « jamais de composant système » (défendable sur mobile).
- Repli IndexedDB→localStorage silencieux (l.653).

### Questions provocatrices

1. Si la photo d'un champignon suspect est le moment le plus critique de la journée, pourquoi la première action de l'app exige-t-elle une clé API que Jonathan doit aller chercher lui-même sur un site Google ?
2. « 100 % hors-ligne » : l'identification IA — la fonction phare — est-elle honnêtement hors-ligne ? Que se passe-t-il en forêt sans réseau quand on clique « Appareil photo » ?
3. L'alerte MORTEL n'apparaît qu'à l'ouverture de la fiche : le badge rouge « ☠️ MORTEL » dans la liste suffit-il, ou le fil de sécurité exige-t-il l'alerte + antipoison dès la liste ?
4. « Cueillettes », « Mon journal », « Sorties » : trois mots pour une même entité — lequel est le nom du produit ?
5. La zone photo affiche « Appareil photo ou galerie » et ne fait rien au clic quand elle est vide : qui gagne, le placeholder ou le bouton ?
6. L'export JSON, seule protection contre la perte de tout un carnet, est rangé sous « Statistiques » : quel est le coût d'un onglet « Sauvegarde » nommé ?
7. À « Confiance : 62 % », le design doit-il afficher un badge « Comestible » vert — ou une question ?
8. 13 champs dans la feuille d'espèce : est-ce un formulaire, ou une fiche que l'IA devrait pré-remplir à 100 % avant toute saisie manuelle ?
9. Le FAB change d'icône (📍 vs ＋) : ce pattern s'apprend-il en forêt, avec des gants et un panier ?
10. Pourquoi la clé Gemini vit-elle dans la feuille d'ajout d'espèce plutôt que dans un premier lancement ou une section réglages ?
11. Le 🗑️ masque (réversible) sur les espèces du guide mais supprime (irréversible) les variétés perso : l'icône doit-elle porter cette différence ?
12. « Dernière sortie » a le même poids visuel que « Total récolté » : que doit-on regarder en premier dans les stats — et le design le dit-il ?
