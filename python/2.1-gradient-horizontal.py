#!/usr/bin/env python3


# Importer les libraires
from math import cos, sin                   # Fonctions mathématiques cosinus et sinus
from math import fabs                       # Fonctions mathématiques value absolue
from utils import color_print, map_range    # Fonctions utilitaires d'affichage et d'interpolation linéaire
from utils import random_color              # Fonction tirage aléatoire d'une couleur
from utils import color_step                # Fonction d'interpolation linéaire de couleur
from utils import rotate_gradient_degrees           # Fonction de rotation

# Taille de la zone d'affichage (en caractères)
width = 115
height = 30

# Définition des couleurs de départ et d'arrivée du dégradé
from_color = random_color() 
to_color   = random_color() 

for y in range(0, height):
    for x in range(0, width):
        step = rotate_gradient_degrees(x, y, 0)
        color = color_step(step, width, from_color, to_color)
        color_print(" ", color, color)
    print()
print()

