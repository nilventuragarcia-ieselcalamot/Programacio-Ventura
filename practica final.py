colors = ["blau", "verd", "groc", "vermell", "taronja", "lila"]
colors_abreviats = ["b", "e", "g", "v", "t", "l"]

print("Benvingut al joc de Mastermind!")
print("El teu objectiu és adivinar una llista de 4 colors en les seves posicions exactes (blau, verd, groc, vermell, taronja, lila o un dells abreviat) (verd abreviat es 'e' ) .")


#copiat de altres pràctiques, fa que l'usuari introdueixi un número enter i si no ho fa, li demana que ho torni a fer fins que ho faci correctament
def anti_texto(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: introduce un número entero válido.")

#si l'usuari introdueix un color que no és vàlid, li demana que torni a introduir un color fins que ho faci correctament. Si introdueix "verd", el converteix en "e" per a que sigui més fàcil de comparar amb els colors generats aleatòriament. Si introdueix un color vàlid, el converteix en la seva abreviatura (la primera lletra del color) per a que sigui més fàcil de comparar amb els colors generats aleatòriament. Si introdueix un color abreviat, el retorna tal qual.   
def anti_nocolor(mensaje):
    while True:
            color = input(mensaje)
            if color == "":
                print("Error: no has introduït cap color.")
            elif color == "verd":
                color = "e"
                return color
            elif color in colors and color != "verd":
                color = color[0]
                return color
            elif color in colors_abreviats:
                return color
            else:
                print("Error: introduce un color válido (blau, verd, groc, vermell, taronja, lila o un dells abreviat).")

#escogir dificultat
print("Escull la dificultat del joc:")
print("1 = Fàcil")
print("0 = Difícil")
dificultat = anti_texto("Introdueix el número de la dificultat: ")
if dificultat == 1:
    print("Has escollit la dificultat fàcil.")
elif dificultat == 0:
    print("Has escollit la dificultat difícil.")
else:
    print("Has escollit una dificultat no vàlida. Per defecte, es jugarà a la dificultat normal.")

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




#comprovar resultados, por pasos, correctos --> regulares, para evitar contar regulares de mas

while colors_escogits != colors_verdaders:
    n_correcte = 0
    n_regular = 0
#bolsa para los regulars sobrantes, para evitar contar regulares de mas
    sobrants = []

    estat = ["", "", "", ""]
    colors_escogits = []
    escogir_color()

    # Correctos
    for i in range(4):
        if colors_escogits[i] == colors_verdaders[i]:
            n_correcte = n_correcte + 1
            estat[i] = "correcte"
        else:
            sobrants.append(colors_verdaders[i])

    #regulares
    for i in range(4):
        if estat[i] == "":
            if colors_escogits[i] in sobrants:
                n_regular = n_regular + 1
                estat[i] = "regular"
                sobrants.remove(colors_escogits[i])
            else:
                estat[i] = "incorrecte"

    # Mensajes por posición (fácil)
    if dificultat == 1:
        for i in range(4):
            if estat[i] == "correcte":
                print("El color numero", i + 1, "és correcte.")
            elif estat[i] == "regular":
                print("El color numero", i + 1, "és correcte però està en una posició diferent.")
            else:
                print("El color numero", i + 1, "és incorrecte.")

    print("Els colors escollits són:", colors_escogits)
    print("Tens", n_correcte, "colors correctes i", n_regular, "colors regulars.")

if colors_escogits == colors_verdaders:
    print("Has encertat tots els colors!")