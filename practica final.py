colors = ["blau", "verd", "groc", "vermell", "taronja", "lila"]
colors_abreviats = ["b", "e", "g", "v", "t", "l"]

def anti_nocolor(mensaje):
    while True:
            color = input(mensaje)
            if color in colors:
                color = color[0]
                return color
            elif color in colors_abreviats:
                return color
            else:
                print("Error: introduce un color válido (blau, verd, groc, vermell, taronja, lila o un dells abreviat).")

#generar 4 nombres aleatoris per seleccionar els colors

import random

color1 = colors_abreviats[random.randint(0, 5)]
color2 = colors_abreviats[random.randint(0, 5)]
color3 = colors_abreviats[random.randint(0, 5)]
color4 = colors_abreviats[random.randint(0, 5)]

colors_verdaders = [color1, color2, color3, color4]
colors_escogits = []

def escogir_color():
    for i in range(4):
        colors_escogits.append(anti_nocolor("Introdueix el color numero " + str(i + 1) + ": "))

print(color1, color2, color3, color4)

while colors_escogits != colors_verdaders:
    colors_escogits = []
    escogir_color()
    for i in range(4):
        if colors_escogits[i] == colors_verdaders[i]:
            print("El color numero", i + 1, "és correcte.")
        elif colors_escogits[i] in colors_verdaders:
            print("El color numero", i + 1, "és correcte però està en una posició diferent.")
        else:
            print("El color numero", i + 1, "és incorrecte.")
if colors_escogits == colors_verdaders:
    print("Has encertat tots els colors!")