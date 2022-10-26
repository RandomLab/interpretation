#!/usr/bin/env python3
import wave
import pygame
import sys
from utils import read_file

# sampling frequency (in Herz: the number of samples per second)
SAMPLINGFREQ = 48000
# the number of channels (1=mono, 2=stereo)
NCHANNELS = 2

# Le premier paramètre est le fichier à interpréter.
file = sys.argv[1]
# Lire le fichier et mettre tous son contenu dans la variable content
content = read_file(file)

# # # # #
# PREPARE

# initialise mixer module
pygame.mixer.init(frequency=SAMPLINGFREQ, channels=NCHANNELS)

# create a sound from the list
snd = pygame.mixer.Sound(content)

# # # # #
# WAVE IT UP
	
# open new wave file
sfile = wave.open('output.wav', 'w')

# set the parameters
sfile.setframerate(SAMPLINGFREQ)
sfile.setnchannels(NCHANNELS)
sfile.setsampwidth(2)

# write raw PyGame sound buffer to wave file
sfile.writeframesraw(snd)

# close file
sfile.close()
