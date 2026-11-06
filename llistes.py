llista = [2, "hola", 3.5]
print(llista[0])
print(llista[1])
print(llista[2])

#llista de llistes
llista2 = [[1, 11, 111], [2, 22, 222], [3, 33, 333]]
print(llista2[1][2])
print(llista2[0])

print(len(llista))
print(len(llista2))

#juntar llistes
llista = [2, 3] + [4, 6, 9]
print(llista)

#separar llistes
llista = [2, 3, 4, 6, 9]
print(llista[1:3])

#reassignar valors a llistes
llista[2] = "gat"
print(llista)

#eliminar valors de llistes
del llista[2]
print(llista)

#deixar en blanc una posició de la llista
llista[2] = ""
print(llista)

#DNI

dni = (input("Introdueix el teu DNI: "))
dni_sense_lletra = dni[0:8]
dni_sense_lletra = int(dni_sense_lletra)
dni_lletra = str(dni)[-1]
modul_dni = dni_sense_lletra % 23
llista_lletras_mayus = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
llista_lletras_minus = ["t", "r", "w", "a", "g", "m", "y", "f", "p", "d", "x", "b", "n", "j", "z", "s", "q", "v", "h", "l", "c", "k", "e"]
if len(dni) != 9:
    print("Aquesta no és una longitud de DNI vàlida")
else:
    if dni_lletra == llista_lletras_mayus[modul_dni] or dni_lletra == llista_lletras_minus[modul_dni]:
        print("El DNI és correcte")
    else:
        print("El DNI és incorrecte")

#append 

print("La llista es: ", llista)
llista.append("gat")
print("La llista es: ", llista)