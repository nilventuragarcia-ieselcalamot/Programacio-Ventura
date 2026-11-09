def anti_texto(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: introduce un número entero válido.")

num1 = anti_texto("Introduiex el primer nombre ")
num2 = anti_texto("Introduiex el segon nombre ")
num3 = anti_texto("Introduiex el tercer nombre ")   
num4 = anti_texto("Introduiex el últim nombre ")

numeros = [num1, num2, num3, num4]

ronda = 0
while ronda < 3:
    posicio = 0
    while posicio < 3 - ronda:
        #comparar els valors de la llista i intercanviar-los si cal
        if numeros[posicio] < numeros[posicio + 1]:
            numeros[posicio], numeros[posicio + 1] = numeros[posicio + 1], numeros[posicio]
        posicio = posicio + 1
    ronda = ronda + 1

print("Ordenats de mayor a menor serian:")
print(numeros)