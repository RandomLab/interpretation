#!/usr/bin/env python3

import sys

filename = sys.argv[1]
f = open(filename, "rb")
content = f.read()

MAX_SIZE=1000

header = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        * {
            margin:0;
            padding:0;
            box-sizing: border-box;
        }
        body {
            color: white;
            background-color: black;
            width: 100%;
            margin: auto;
        }
        .section {
            padding: 20px;
            border: 3px solid grey;
            margin:20px;

        }
        h1 {
            text-align: center;
            padding: 100px;
            width:100%;
            margin: auto;
        }
        .rectangle1 {
            width: 255px;
            height: 255px;
            display: inline-block;
            border-radius: 50px;
        }
        .rectangle {
            width: 20px;
            height: 20px;
            display: inline-block;
            border-radius: 50px;
        }
    </style>
</head>
<body>

"""

footer = """

</body>
</html>
"""

print(header)



def rgb_radius_rgb(limit):
    print("<div class='section'>")
    print(f"<h1>RGB, radius as RGB {filename}</h1>")
    for i in range(0, len(content), 4):
        if i > limit: break
        try:
            r = content[i]
            g = content[i+1]
            b = content[i+2]
            print(f"<div class='rectangle1' style='background-color:rgb({r}, {g}, {b});border-radius:{r}px {g}px {b}px {(r+g+b)/3.}px;'></div>")
        except:
            pass
    print("</div>")
def rgb_rrrr(limit):
    print("<div class='section'>")
    print(f"<h1>RGB, radius, radius, radius, radius {filename}</h1>")
    for i in range(0, len(content), 7):
        if i > limit: break
        try:
            r = content[i]
            g = content[i+1]
            b = content[i+2]
            r1 = content[i+3]
            r2 = content[i+4]
            r3 = content[i+5]
            r4 = content[i+6]
            print(f"<div class='rectangle1' style='background-color:rgb({r}, {g}, {b});border-radius:{r1}px {r2}px {r3}px {r4}px;'></div>")
        except:
            pass
    print("</div>")
def rgb_wh(limit):
    print("<div class='section'>")
    print(f"<h1>RGB, width and height {filename}</h1>")
    for i in range(0, len(content), 5):
        if i > limit: break
        try:
            r = content[i]
            g = content[i+1]
            b = content[i+2]
            w = content[i+3]
            h = content[i+4]
            print(f"<div class='rectangle' style='background-color:rgb({r}, {g}, {b});width:{w}px;height:{h}px;'></div>")
        except:
            pass
    print("</div>")
def rgb_w(limit):
    print("<div class='section'>")
    print(f"<h1>RGB, width {filename}</h1>")
    for i in range(0, len(content), 4):
        if i > limit: break
        try:
            r = content[i]
            g = content[i+1]
            b = content[i+2]
            w = content[i+3]
            print(f"<div class='rectangle' style='background-color:rgb({r}, {g}, {b});width:{w}px'></div>")
        except:
            pass
    print("</div>")

def rgb(limit):
    print("<div class='section'>")
    print(f"<h1>RGB {filename}</h1>")
    for i in range(0, len(content), 3):
        if i > limit: break
        try:
            r = content[i]
            g = content[i+1]
            b = content[i+2]
            print(f"<div class='rectangle' style='background-color:rgb({r}, {g}, {b})'></div>")
        except:
            pass
    print("</div>")
def rotation(limit):
    print("<div class='section'>")
    print(f"<h1>RGB rotation as RGB {filename}</h1>")
    for i in range(0, len(content), 3):
        if i > limit: break
        try:
            r = content[i]
            g = content[i+1]
            b = content[i+2]
            #print(f" <div class='rectangle' style='background-color:rgb({r}, {g}, {b});'> </div> ")
            print(f"<div class='rectangle1' style='background-color:rgb({r}, {g}, {b});border-radius:{r}px {g}px {b}px 0px;transform: rotate({r}deg) scale({0.5 + ((r+g+b)/3)/255.});'></div>")
        except:
            pass
    print("</div>")

def hls(limit):
    print("<div class='section'>")
    print(f"<h1>HLS {filename}</h1>")
    for i in range(0, len(content), 3):
        if i > limit: break
        try:
            r = content[i]
            g = content[i+1]
            b = content[i+2]
            print(f"<div class='rectangle1' style='background-color:hsl({g}, {b%100}%, {(r/255.) * 100}%);'></div>")
        except:
            pass
    print("</div>")

rgb(limit=MAX_SIZE)
#rgb_w(limit=MAX_SIZE)
#rgb_wh(limit=MAX_SIZE)
#rgb_rrrr(limit=MAX_SIZE)
#rgb_radius_rgb(limit=MAX_SIZE)
#rotation(limit=MAX_SIZE)
#hls(limit=MAX_SIZE)




# print("<div class='section'>")
# 
# for i in range(0, len(content), 4):
#     try:
#         r = content[i]
#         g = content[i+1]
#         b = content[i+2]
#         l = content[i+3]
# 
#         print(f"<div class='rectangle' style='background-color:rgb({r}, {g}, {b});width:{l}px'></div>")
#     except:
#         pass
# 
# print("</div>")
# print("<div class='section'>")
# 
# for i in range(0, len(content), 3):
#     try:
#         r = content[i]
#         g = content[i+1]
#         b = content[i+2]
# 
#         print(f"<div class='rectangle' style='background-color:hsl({g}, {b%100}%, {(r/255.) * 100}%);'></div>")
#     except:
#         pass
# 
# print("</div>")
# 
# print("<div class='section'>")
# 
# for i in range(0, len(content), 4):
#     try:
#         r = content[i]
#         g = content[i+1]
#         b = content[i+2]
#         l = content[i+3]
# 
#         print(f"<div class='rectangle' style='background-color:hsl({g}, {b%100}%, {50}%);width:{l}px'></div>")
#     except:
#         pass
# 
# print("</div>")
# 
# print("<div class='section'>")
# 
# for i in range(0, len(content), 4):
#     try:
#         r = content[i]
#         g = content[i+1]
#         b = content[i+2]
#         l = content[i+3]
# 
#         print(f"<div class='rectangle' style='background-color:hsl({g}, {b%100}%, {50}%);height:{l}px'></div>")
#     except:
#         pass
# 
# print("</div>")
# 
# print("<div class='section'>")
# 
# for i in range(0, len(content), 5):
#     try:
#         r = content[i]
#         g = content[i+1]
#         b = content[i+2]
#         l = content[i+3]
#         h = content[i+4]
# 
#         print(f"<div class='rectangle' style='background-color:hsl({g}, {b%100}%, {50}%);width:{l}px;height:{h}px;'></div>")
#     except:
#         pass
# 
# print("</section>")


print(footer)
