#!/usr/bin/env python3

import sys

filename = sys.argv[1]


# filename = "image.bmp"
# filename = "../alphabet.txt"



f = open(filename, "rb")
content = f.read()


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
            background-color: black;
        }
        .section {
            margin: 20px;
            padding: 20px;
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: center;

        }
        .rectangle {
            width: 20px;
            height: 20px;
            display: inline-block;
            margin:0;
            padding:0;
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


print("<div class='section'>")

for i in range(0, len(content), 3):
    try:
        r = content[i]
        g = content[i+1]
        b = content[i+2]

        print(f"<div class='rectangle' style='background-color:rgb({r}, {g}, {b})'></div>")
    except:
        pass
print("</div>")
print("<div class='section'>")

for i in range(0, len(content), 4):
    try:
        r = content[i]
        g = content[i+1]
        b = content[i+2]
        l = content[i+3]

        print(f"<div class='rectangle' style='background-color:rgb({r}, {g}, {b});width:{l}px'></div>")
    except:
        pass

print("</div>")
print("<div class='section'>")

for i in range(0, len(content), 3):
    try:
        r = content[i]
        g = content[i+1]
        b = content[i+2]

        print(f"<div class='rectangle' style='background-color:hsl({g}, {b%100}%, {(r/255.) * 100}%);'></div>")
    except:
        pass

print("</div>")

print("<div class='section'>")

for i in range(0, len(content), 4):
    try:
        r = content[i]
        g = content[i+1]
        b = content[i+2]
        l = content[i+3]

        print(f"<div class='rectangle' style='background-color:hsl({g}, {b%100}%, {50}%);width:{l}px'></div>")
    except:
        pass

print("</div>")

print("<div class='section'>")

for i in range(0, len(content), 4):
    try:
        r = content[i]
        g = content[i+1]
        b = content[i+2]
        l = content[i+3]

        print(f"<div class='rectangle' style='background-color:hsl({g}, {b%100}%, {50}%);height:{l}px'></div>")
    except:
        pass

print("</div>")

print("<div class='section'>")

for i in range(0, len(content), 5):
    try:
        r = content[i]
        g = content[i+1]
        b = content[i+2]
        l = content[i+3]
        h = content[i+4]

        print(f"<div class='rectangle' style='background-color:hsl({g}, {b%100}%, {50}%);width:{l}px;height:{h}px;'></div>")
    except:
        pass

print("</section>")


print(footer)
