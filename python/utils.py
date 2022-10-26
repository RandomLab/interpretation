from xtermcolor import colorize          # Fonction qui permet d'afficher des caractères colorés
from random import randint
from math import radians, fabs, cos, sin


# Affiche un caractère dans le terminal avec une couleur de texte et une couleur de fond.
def color_print(c = ".", fg_color=(255,255,255), bg_color=(0,0,0)):
    fg = rgb_color(fg_color)
    bg = rgb_color(bg_color)
    print(colorize(c, rgb=fg, bg=bg), end='')

# Changement d'intervale
# ex: [0,1] -> [0-255]
# Interpolation linéaire
# https://stackoverflow.com/questions/1969240/mapping-a-range-of-values-to-another
def map_range(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def rgb_color(color):
    return int(f"{int(color[0]):02X}{int(color[1]):02X}{int(color[2]):02X}", 16)

# Retourne un angle aléatoire
def random_angle():
    return radians(randint(0, 360))

# Retourne une couleur aléatoire
def random_color():
    return (randint(0,255), randint(0,255), randint(0,255))

# Interpolation linéaire d'une couleur vers une autre
def color_step(step, width, from_color, to_color):
    r = map_range(step, 0, width, from_color[0], to_color[0])
    g = map_range(step, 0, width, from_color[1], to_color[1])
    b = map_range(step, 0, width, from_color[2], to_color[2])
    return (r, g, b)

# Rotation d'un système de coordonée en  fonction d'un angle (radians)
def rotate_gradient(x, y, angle):
    return fabs(x * cos(angle) - y * sin(angle))

# Rotation d'un système de coordonée en  fonction d'un angle (degrées)
def rotate_gradient_degrees(x, y, angle):
    angle = radians(angle)
    return rotate_gradient(x, y, angle)


# Lire un fichier en mode binare

def read_file(filepath):
    f = open(filepath, "rb")
    return f.read()

