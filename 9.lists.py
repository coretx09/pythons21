noms = ["Marc", "Prince", "Sauvet", "Carlos", "jean"]
print(noms[1][3])  # [1]=prince,[3]=n
print(noms[0:3:2])  # start 0, stop 3, sep 2
print("\n")

# le plus grand nombre
numeros = [1, 4, 3, 9, 2]
max = numeros[0]
for i in numeros:
    if i > max:
        max = i
print(max, "\n")

# Matrice
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0][1] = 20
print(matrix[0][1])
print(matrix, "\n")

for row in matrix:
    print(row)  # affiche la list matrix
print("\n")

for row in matrix:
    for i in row:
        print(i)  # affiche tous elements de matrix
