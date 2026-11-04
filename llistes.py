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