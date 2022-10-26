#!/usr/bin/env python3

# Importer les libraires
from random import randint               # Fonction aléatoire
from utils import color_print

# Taille de la zone d'affichage (en nombre de caractères)
width = 115
height = 30

# 2) espace couleur aléatoire + fond
for y in range(0, height):
    for x in range(0, width):
        color = (randint(0,255),randint(0,255),randint(0,255))
        color_print("@", fg_color=color, bg_color=color)
    print()
print()


