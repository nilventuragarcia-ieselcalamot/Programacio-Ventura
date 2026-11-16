def anti_texto(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: introduce un número entero válido.")




parells_17_100 = []
for i in range(17, 101):
    if i % 2 == 0:
        parells_17_100.append(i)
print("Números pares entre 17 y 100:")
print(parells_17_100)


#notes classe   
notes = [[6, 6, 7, 10, 9], [10, 7, 6, 7, 7], [5, 5, 10, 7, 10]]

n_10 = 0
posicio_dels_10_notes_notes_de_1alumne = 0
posicio_dels_10 = []

for notes_de_1alumne in notes:
    posicio_dels_10_notes_notes_de_1alumne_sub = 0
    for cada_nota in notes_de_1alumne:
        if cada_nota == 10:
            n_10 += 1
            posicio = "En la fila", posicio_dels_10_notes_notes_de_1alumne, "columna", posicio_dels_10_notes_notes_de_1alumne_sub
            posicio_dels_10.append(posicio)
        posicio_dels_10_notes_notes_de_1alumne_sub += 1
    posicio_dels_10_notes_notes_de_1alumne += 1

print("El nombre de 10 és: ", n_10)
print("La posició dels 10 és: ", posicio_dels_10)

#WHILE - adivinar un nombre entre 1 i 10

adivinat = False
while adivinat == False:
    intent = int(input("Introdueix un nombre entre 1 i 10: "))
    if intent == 7:
        print("Has encertat!")
        adivinat = True
    else:
        print("No has encertat, torna-ho a intentar.")