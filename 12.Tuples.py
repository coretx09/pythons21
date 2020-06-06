"""
les Tuples sont des variables non modifiables, dans laquelle on peut mettre plusieurs autres variables

"""

numeros = (1, 2, 8)
print(numeros.index(2))  # donne l'index
print(numeros.count(8))  # donne le nombre occurence

""" numeros[0] = 21  renvoie error  """

cordonnees = (34, 65, 105)
x = cordonnees[0]
y = cordonnees[1]
z = cordonnees[2]

x, y, z = cordonnees
