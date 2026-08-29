# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Utilisateur principal : Jonathan (le propriétaire), sur son téléphone, en forêt et à la maison. Partage possible à des proches (export/import JSON) — pas un outil public.

## Product Purpose

Carnet de chasse personnel + guide d'identification des champignons du Québec, 100 % hors-ligne, dans un style Memphis ludique. Le succès = retrouver ses coins secrets, noter ses récoltes, identifier un champignon avec confiance, et prendre du plaisir à le faire.

## Positioning

Le carnet vit sur le téléphone, sans compte ni serveur : les données ne quittent jamais l'appareil, tout fonctionne en forêt sans réseau. Le guide combine 21 espèces documentées du Québec, l'identification par photo (IA) et des variétés personnelles enrichies par IA — avec un parti pris sécurité systématique (alertes MORTEL/toxique, centre antipoison).

## Operating Context

- Terrain : forêts du Québec, téléphone en main, souvent sans réseau — PWA installable, 100 % hors-ligne dès la première visite.
- Saisons de cueillette : morilles au printemps, chanterelles/cèpes été-automne.
- Utilisation : noter un spot (GPS), identifier sur place (photo), journaliser la récolte (poids, météo, spot), consulter les stats.
- Partage : export/import JSON complet (version 5, inclut espèces masquées, supprimées et illustrations).

## Capabilities and Constraints

- Spots : nom, description, GPS (précision affichée), photo, lien Google Maps.
- Guide : 21 espèces avec photos Wikimedia embarquées, badges comestible / prudence / immangeable / toxique / MORTEL ☠️, saison, habitat, caractéristiques clés, confusions dangereuses.
- Fiches hybrides : 5 spécificités d'identification par espèce (chapeau, hyménium, pied, chair, habitat) avec photo réelle embarquée (100 photos Wikimedia dans `img/specs/`), description de ce qu'il faut vérifier, checklist terrain interactive (cases à cocher, compteur, verdict ⚠️/✅) persistée localement.
- Identification par photo : Gemini vision (appareil ou galerie), avec niveau de confiance et alertes de sécurité.
- Variétés perso : ajout / modification / suppression, masquage / restauration sélective, fiche générée par IA (Gemini), photo Wikimedia Commons ou illustration IA (par spécificité : chapeau, lames, pied, section, habitat).
- Cueillettes : date, espèce (suggestions + libre), poids kg (virgule acceptée), spot lié, météo, note, photo.
- Stats : total récolté, sorties, espèces distinctes, dernière sortie, tops espèces/spots, barres mensuelles.
- Sauvegarde : export/import JSON, effacement complet avec double confirmation.
- Contrainte technique : PWA statique mono-fichier (`index.html`, ~170 Ko, zéro framework, pas de build), service worker cache-first avec bump `cqm-vN` à chaque changement (le numéro courant vit dans `sw.js`, jamais dans cette doc). API Wikimedia/Gemini exclues du cache. Déployée sur GitHub Pages (jonathancote1984.github.io/cueillette-memphis), push main → déploiement auto.
- Données : IndexedDB (`cqm_bd` v5 : spots, cueillettes, especes, caches, illustrations, supprimees, checklist) avec repli localStorage ; clé Gemini stockée localement, jamais envoyée ailleurs. Paramètres : unités kg/lb (affichage + saisie), clé API. Suppression d'espèces d'origine = store `supprimees` + double confirmation.
- Langue : français du Québec.

## Brand Commitments

- Nom : « Cueillette Québec — édition Memphis » (court : Cueillette).
- Style Memphis assumé : bordures noires épaisses (3 px), coins cassés, ombres dures sans flou, formes géométriques, titres légèrement inclinés, zigzags/pois.
- Palette AUTOMNE/TERRE : ambre `#D9A441`, rouille `#B45309`, terracotta `#B94527`, olive `#6F8F3E`, cuir `#8A5A2B`, crème `#F3E8D5`, blanc `#FDF6E7`, noir `#241A0F`.
- Typographie : Fredoka (arrondie) avec repli système.
- Icône : jaune à pois + champignon rouge (générée par `generer_icones.py`).
- Jamais de boîtes système navigateur (confirm/alert) : modales stylées Memphis.
- Avertissements de sécurité non négociables : alertes MORTEL/toxique + centre antipoison Québec 1-800-463-5060.

## Evidence on Hand

- Photos réelles des 21 espèces dans `img/especes/` avec crédits Wikimedia (`credits.json`).
- 100 photos de spécificités dans `img/specs/` (21 espèces × 5 critères) avec crédits Wikimedia (`credits.json`).
- Icônes PWA (`icons/`), scripts de génération (`generer_icones.py`, `scripts/telecharger_photos.py`).
- README documenté. Aucun témoignage ni donnée utilisateur publique — les données sont privées et locales.

## Product Principles

1. La sécurité prime : toute ambiguïté d'identification penche vers la prudence et le centre antipoison.
2. Le terrain d'abord : conçue pour une utilisation en forêt, une main, sans réseau — rapide et hors-ligne.
3. Le carnet est privé : données 100 % locales, aucune donnée envoyée sans action explicite de l'utilisateur.
4. Le plaisir de la récolte : l'identité Memphis rend le carnet chaleureux et ludique, pas clinique.
5. Zéro friction : pas de compte, pas de serveur, pas d'abonnement — l'app est libre et installable.
