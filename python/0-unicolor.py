#!/usr/bin/env python3

# Importer les libraires

from utils import color_print

# Taille de la zone d'affichage (en caractères)
width = 115
height = 30

# Couleur de texte (l'espace n'a pas de couleur...)
fg_color = (0, 0, 0)
# Couleur de fond
bg_color = (255, 0, 0)

# Affichage des caractères colorés
for y in range(0, height):
    for x in range(0, width):
        color_print(c=" ", fg_color=fg_color, bg_color=bg_color)
    print()

