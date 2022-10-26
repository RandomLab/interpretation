import pygame
from pygame.locals import *
import sys
import math
import numpy as np
filename = sys.argv[1]
f = open(filename, "rb")
content = f.read()


size = (1366, 720)


pygame.mixer.init()

# buffer = np.sin(2 * np.pi * np.arange(44100) * 880 / 44100).astype(np.float32)
sound = pygame.mixer.Sound(content)

sound.play(0)
pygame.time.wait(int(sound.get_length() * 1000))
