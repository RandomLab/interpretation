#!/usr/bin/env python3

# Importer les libraires
import sys
from utils import color_print, read_file

# Taille de la zone d'affichage (en caractères)
width = 1024

# Le premier paramètre est le fichier à interpréter.
file = sys.argv[1]
# Lire le fichier et mettre tous son contenu dans la variable content
content = read_file(file)

# Affichage des caractères colorés

for index in range(0, len(content), 3):
    try:
        b = content[index]
        g = content[index + 1]
        r = content[index + 2]
        bg_color = (r,g,b)
        fg_color = (r,g,b)
    except:
        bg_color = (0,0,0)
        fg_color = (0,0,0)
        

    color_print(c=" ", fg_color=fg_color, bg_color=bg_color)
    if index % width == 0: print()

print()

