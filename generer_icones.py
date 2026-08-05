#!/usr/bin/env python3
"""Icônes PWA style Memphis : fond jaune vif avec pois colorés, champignon géométrique
rouge à pois crème, contours noirs épais. Usage : python generer_icones.py"""
import os
from PIL import Image, ImageDraw

JAUNE = (255, 209, 102)
ROUGE = (255, 77, 109)
BLEU = (76, 201, 240)
ROSE = (255, 112, 166)
VERT = (6, 214, 160)
CREME = (255, 244, 224)
NOIR = (31, 26, 23)

def fond(d, taille):
    d.rectangle([0, 0, taille, taille], fill=JAUNE)
    # pois décoratifs Memphis (disposés en quinconce)
    pois = [(0.10, 0.12, BLEU), (0.88, 0.14, ROSE), (0.15, 0.86, VERT), (0.86, 0.84, BLEU),
            (0.50, 0.03, ROSE), (0.05, 0.48, ROUGE), (0.95, 0.50, VERT), (0.50, 0.97, BLEU)]
    for px, py, couleur in pois:
        r = taille * 0.045
        d.ellipse([px * taille - r, py * taille - r, px * taille + r, py * taille + r],
                  fill=couleur, outline=NOIR, width=max(2, int(taille * 0.012)))

def champignon(d, cx, cy, e):
    """Champignon géométrique Memphis centré en (cx, cy), taille relative e."""
    lw = max(3, int(e * 0.09))
    # Pied
    d.rounded_rectangle([cx - 0.30 * e, cy - 0.05 * e, cx + 0.30 * e, cy + 1.05 * e],
                        radius=0.14 * e, fill=CREME, outline=NOIR, width=lw)
    # Chapeau (demi-cercle)
    d.pieslice([cx - 1.25 * e, cy - 1.10 * e, cx + 1.25 * e, cy + 0.60 * e],
               180, 360, fill=ROUGE, outline=NOIR, width=lw)
    # Pois crème
    for px, py, pr in [(-0.50, -0.55, 0.14), (0.05, -0.72, 0.16), (0.58, -0.42, 0.12),
                       (-0.10, -0.25, 0.11), (0.40, -0.02, 0.10), (-0.60, -0.16, 0.09)]:
        d.ellipse([cx + (px - pr) * e, cy + (py - pr) * e, cx + (px + pr) * e, cy + (py + pr) * e],
                  fill=CREME)

def generer(taille, nom, masquable=False):
    img = Image.new('RGBA', (taille, taille))
    d = ImageDraw.Draw(img)
    fond(d, taille)
    e = taille * (0.40 if masquable else 0.30)
    champignon(d, taille / 2, taille / 2, e)
    img.save(os.path.join('icons', nom))
    print('OK', nom, taille)

if __name__ == '__main__':
    os.makedirs('icons', exist_ok=True)
    generer(192, 'icon-192.png')
    generer(512, 'icon-512.png')
    generer(512, 'icon-maskable-512.png', masquable=True)
