#!/usr/bin/env python3
"""Télécharge une photo libre (Wikimedia Commons) pour chaque espèce du guide
et la convertit en JPEG 800 px max dans img/especes/. Écrit img/especes/credits.json
(auteur + licence + page source) pour l'attribution.
Usage : python scripts/telecharger_photos.py"""
import io, json, os, re, sys, time, urllib.parse, urllib.request
from PIL import Image

UA = 'CueilletteMemphis/1.0 (application personnelle de cueillette de champignons)'

ESPECES = [
    ('chanterelle', 'Cantharellus cibarius'),
    ('chanterelle-tube', 'Craterellus tubaeformis'),
    ('cepe', 'Boletus edulis'),
    ('bolet-bai', 'Imleria badia'),
    ('pied-mouton', 'Hydnum umbilicatum'),
    ('morille', 'Morchella esculenta'),
    ('pleurote', 'Pleurotus ostreatus'),
    ('coprin', 'Coprinus comatus'),
    ('lepiote', 'Macrolepiota procera'),
    ('amanite-rougissante', 'Amanita rubescens'),
    ('bolet-amer', 'Tylopilus felleus'),
    ('tue-mouches', 'Amanita muscaria'),
    ('panthere', 'Amanita pantherina'),
    ('entolome', 'Entoloma sinuatum'),
    ('paxille', 'Paxillus involutus'),
    ('fausse-chanterelle', 'Hygrophoropsis aurantiaca'),
    ('phalloide', 'Amanita phalloides'),
    ('vireuse', 'Amanita virosa'),
    ('galerine', 'Galerina marginata'),
    ('gyromitre', 'Gyromitra esculenta'),
    ('lepiote-brunatre', 'Lepiota brunneoincarnata'),
]

def requete(fn, tentatives=5):
    """Exécute fn avec backoff exponentiel sur erreurs réseau/429."""
    for i in range(tentatives):
        try:
            return fn()
        except urllib.error.HTTPError as e:
            if e.code == 429 and i < tentatives - 1:
                attente = 5 * (2 ** i)
                print(f'   …429 : nouvelle tentative dans {attente} s')
                time.sleep(attente)
            else:
                raise
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            if i < tentatives - 1:
                time.sleep(4 * (i + 1))
            else:
                raise

def api(q):
    url = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode({
        'action': 'query', 'format': 'json', 'generator': 'search',
        'gsrsearch': 'filetype:bitmap ' + q, 'gsrnamespace': '6', 'gsrlimit': '10',
        'prop': 'imageinfo', 'iiprop': 'url|size|extmetadata', 'iiurlwidth': '800'
    })
    def _get():
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=20) as r:
            return json.loads(r.read().decode())
    return requete(_get)

def meilleure(rep):
    pages = (rep.get('query') or {}).get('pages') or {}
    candidats = []
    for p in pages.values():
        ii = (p.get('imageinfo') or [{}])[0]
        titre = p.get('title', '').lower()
        if any(m in titre for m in ['map', 'diagram', 'chart', 'stamp', 'coin', 'poster']):
            continue
        if ii.get('width', 0) < 400:
            continue
        candidats.append((ii.get('width', 0), ii.get('thumburl') or ii.get('url'), ii))
    candidats.sort(key=lambda c: c[0], reverse=True)
    return candidats[0] if candidats else None

def telecharger(url):
    def _get():
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read()
    return requete(_get)

def nettoyer_html(s):
    return re.sub('<[^>]+>', '', s or '').strip()

def main():
    os.makedirs('img/especes', exist_ok=True)
    credits = {}
    for esp_id, latin in ESPECES:
        try:
            rep = api(latin)
            meilleure_img = meilleure(rep)
            if not meilleure_img:
                raise RuntimeError('aucune image trouvée')
            _, url, ii = meilleure_img
            data = telecharger(url)
            im = Image.open(io.BytesIO(data)).convert('RGB')
            im.thumbnail((800, 800))
            chemin = f'img/especes/{esp_id}.jpg'
            im.save(chemin, 'JPEG', quality=82)
            credits[esp_id] = {
                'fichier': chemin,
                'espece': latin,
                'auteur': nettoyer_html(ii.get('extmetadata', {}).get('Artist', {}).get('value', 'inconnu'))[:100],
                'licence': nettoyer_html(ii.get('extmetadata', {}).get('LicenseShortName', {}).get('value', '?')),
                'page': ii.get('descriptionurl', '')
            }
            print('OK  ', esp_id, f'({latin}) -> {os.path.getsize(chemin)//1024} Ko')
        except Exception as e:
            print('ÉCHEC', esp_id, f'({latin}) :', e)
        time.sleep(2)
    with open('img/especes/credits.json', 'w', encoding='utf-8') as f:
        json.dump(credits, f, ensure_ascii=False, indent=2)
    reussis = [k for k in credits]
    print(f'\n{len(reussis)}/{len(ESPECES)} photos téléchargées : {", ".join(reussis)}')

if __name__ == '__main__':
    main()
