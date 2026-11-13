parells_17_100 = []
for i in range(17, 101):
    if i % 2 == 0:
        parells_17_100.append(i)
print("Números pares entre 17 y 100:")
print(parells_17_100)


#notes classe   
notes = [[6, 6, 7, 10, 9], [10, 7, 6, 7, 7], [5, 5, 10, 7, 10]]

n_10 = 0
l = 0
posicio_dels_10 = []

for i in notes:
    l_sub = 0
    for j in i:
        if j == 10:
            n_10 += 1
            posicio_dels_10.append([[l], [l_sub]])
            l_sub += 1
    l += 1

print("El nombre de 10 és: ", n_10)
print("La posició dels 10 és: ", posicio_dels_10)