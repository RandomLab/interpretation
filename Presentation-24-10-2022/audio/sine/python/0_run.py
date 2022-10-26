#!/usr/bin/env python
import sys
import pysine
import random

filename = sys.argv[1]
f = open(filename, "rb")
content = f.read()

MAX_SIZE=1000000

f_offset = 840
for i in range(0, len(content), 2):
    if i > MAX_SIZE: break
    f = content[i]  % 200
    f += f_offset
    # if i%f == 0:
    #     f_offset = random.choice(content)
    d = content[i + 1] / 255.
    print(float(f))
    pysine.sine(frequency=float(f), duration=d/2.)
