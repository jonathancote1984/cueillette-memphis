# Contribution

> **Wiki Cueillette Québec — édition Memphis** · [Accueil du dépôt](../README.md) ·
> [Index du wiki](README.md)

Projet personnel, sans équipe : ces conventions servent surtout de mémoire de travail et de
cadre pour tout contributeur occasionnel (humain ou agent).

## Sommaire

- [Environnement de travail](#environnement-de-travail)
- [Architecture à respecter](#architecture-à-respecter)
- [Conventions de code](#conventions-de-code)
- [Conventions de commit](#conventions-de-commit)
- [Checklist avant de livrer](#checklist-avant-de-livrer)
- [Documents à tenir à jour](#documents-à-tenir-à-jour)
- [Scripts utilitaires](#scripts-utilitaires)
- [Limites non négociables](#limites-non-négociables)

## Environnement de travail

```bash
git clone https://github.com/jonathancote1984/cueillette-memphis.git
cd cueillette-memphis
python3 -m http.server 8091   # http://localhost:8091
```

Aucune dépendance à installer pour l'app. Pour les scripts Python, un environnement virtuel
suffit :

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install pillow requests
```

Fichiers ignorés par Git : `__pycache__/`, `*.pyc`, `.DS_Store`, `Thumbs.db`, `.agents/`.

## Architecture à respecter

- **Mono-fichier** : HTML, CSS et JavaScript vivent dans `index.html`. Pas de bundler, pas de
  framework, pas de dépendance chargée depuis un CDN.
- **Tout est relatif** : chemins en `./…` afin que la publication dans un sous-dossier de
  GitHub Pages fonctionne.
- **Hors-ligne d'abord** : toute ressource nécessaire au guide doit être embarquée dans le
  dépôt et listée dans `FICHIERS` de `sw.js`.
- **Auto-hébergement des assets** : police dans `fonts/`, images dans `img/` — aucun appel à
  Google Fonts ou à un CDN d'images.
- **Le réseau est un bonus** : Wikimedia, MycoQuébec et Gemini sont facultatifs ; l'app doit
  rester pleinement utilisable sans eux.

## Conventions de code

- **Langue** : identifiants, commentaires et libellés en français (`recharger`, `ouvrirDetail`,
  `especesCustom`). L'interface est en français du Québec.
- **Fonctions courtes et nommées par l'intention** ; les helpers partagés évitent la
  duplication (`appelGemini`, `lierPhoto`, `compresser`, `confirmer`, `toast`).
- **Aucune boîte système** : pas de `confirm()`, `alert()`, `prompt()` — utiliser les modales
  Memphis (`confirmer`, `choix`, `toast`).
- **Accessibilité** : cibles tactiles ≥ 44 px, `aria-current` sur l'onglet actif,
  `role="tablist"` et navigation au clavier sur les étapes, `aria-live` sur les compteurs,
  `:focus-visible` visible, contraste AA (opacité de la méta jamais sous 0,8).
- **Style** : respecter les tokens de [../DESIGN.md](../DESIGN.md) ; toute couleur nouvelle
  doit y être documentée avant usage.
- **Sécurité** : jamais de HTML construit avec une donnée non validée ; les gestionnaires
  passent par `data-*` et `dataset` plutôt que par `onclick` interpolé ; les entrées
  importées sont validées (identifiants, statuts, URL d'images).
- **Un commentaire d'audit** (`// AUDIT M8 (2026-08) : …`) documente les correctifs
  structurels : ne pas les retirer sans raison.

## Conventions de commit

Format `type(portée): description` en français, à l'impératif ou au constat, avec mention du
bump du service worker quand il y en a un.

| Type | Usage |
|---|---|
| `feat` | nouvelle capacité |
| `fix` | correctif (souvent suffixé par la passe de critique : `fix(critique-29e)`) |
| `polish` | finitions d'interface sans changement fonctionnel |
| `refactor` | réorganisation sans changement de comportement |
| `perf` | performance |
| `docs` | documentation seulement |
| `chore` | tâches diverses (bump isolé, ménage) |

Exemples réels du dépôt :

```
feat(etapes): feuille variété en 2 étapes progressives … — SW bump cqm-v48
fix(ia): fallback on 404 and add timeout to Gemini calls
chore(sw): bump cache to cqm-v62
docs: audit webapp complet (3 axes) — AUDIT_RAPPORT.md consolidé
```

Le message porte l'information : décrire **ce que ça change pour l'utilisateur**, pas
seulement le fichier touché.

## Checklist avant de livrer

- [ ] l'app se charge sans erreur en console, y compris sans violation de CSP ;
- [ ] parcours testé : créer un spot, journaliser une cueillette, ouvrir une fiche, cocher la
      checklist, exporter, réimporter ;
- [ ] aucune régression de sécurité : un badge vert ne peut apparaître sur une espèce non
      comestible, et une alerte mortelle affiche le centre antipoison ;
- [ ] `cqm-vN` incrémenté dans `sw.js` si un fichier servi a changé ;
- [ ] nouvelles ressources ajoutées à `FICHIERS` dans `sw.js` et créditées dans le
      `credits.json` correspondant ;
- [ ] tokens de design respectés (bordure 3 px, ombre sans flou, coin cassé, rouge = danger) ;
- [ ] documentation mise à jour (voir section suivante) ;
- [ ] test hors-ligne effectué (mode avion ou *Network → Offline*).

## Documents à tenir à jour

| Document | À mettre à jour quand… |
|---|---|
| [../PRODUCT.md](../PRODUCT.md) | les capacités, contraintes ou principes du produit changent |
| [../DESIGN.md](../DESIGN.md) | une couleur, un token ou un composant change ou apparaît |
| [README.md](../README.md) | la présentation, l'installation ou la structure du dépôt change |
| [fonctionnalites.md](fonctionnalites.md) | un écran gagne ou perd une fonction |
| [guide-identification.md](guide-identification.md) | le guide change d'espèces ou de méthode |
| [securite-alimentaire.md](securite-alimentaire.md) | un garde-fou de sécurité est ajouté ou modifié |
| [donnees-confidentialite.md](donnees-confidentialite.md) | le schéma de données ou le format d'export change |
| [changelog.md](changelog.md) | à chaque itération notable |

Règle : **ne jamais recopier le numéro de cache courant dans la documentation.** Il vit dans
`sw.js`, et seulement là.

## Scripts utilitaires

| Script | Rôle | Dépendance |
|---|---|---|
| `generer_icones.py` | régénère `icons/icon-192.png`, `icon-512.png`, `icon-maskable-512.png` | Pillow |
| `scripts/telecharger_photos.py` | re-télécharge les photos d'espèces depuis Wikimedia Commons et met à jour les crédits | requests |

Après exécution : vérifier les crédits, ajouter les fichiers à `FICHIERS` si nécessaire, puis
bumper `cqm-vN`.

## Limites non négociables

1. **Sécurité d'abord** : toute ambiguïté d'identification penche vers la prudence et le
   centre antipoison. Aucun raccourci d'interface ne peut affaiblir cette règle.
2. **Données locales** : aucune donnée utilisateur ne quitte l'appareil sans action explicite.
   Pas d'analytique, pas de traceur, pas de compte.
3. **Zéro build** : si une contribution exige une étape de compilation, elle est refusée.
4. **Hors-ligne complet** : une fonction qui ne dégrade pas proprement sans réseau n'est pas
   terminée.

Voir aussi : [Déploiement](deploiement.md) · [AUDIT_RAPPORT.md](AUDIT_RAPPORT.md) ·
[AUDIT_QUALITE.md](AUDIT_QUALITE.md)
