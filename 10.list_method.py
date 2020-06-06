"""
les List sont des variables modifiables, dans laquelle on peut mettre plusieurs autres variables
et effectuer les operations suivantes:
"""

numeros = [7, 9, 3, 2, 8]  # une liste
print(f"la liste: {numeros}")

print(f"{numeros[0]} le premier element de la liste")  # affiche l'element se trouvant a l'index i

numeros.append(20)  # ajoute
print(f"{numeros} On ajoute 20")

numeros.insert(0, 10)  # ajoute un element en precisant son index .insert(index, object)
print(f"{numeros} On ajoute 10 en 1ere position")

numeros.remove(7)  # supprime un element par sa valeur
print(f"{numeros} On a supprime 7")

del numeros[2]  # supprime un element par son index
print(f"{numeros} on a supprime l'element se trouvant a l'index 2")

print(numeros.pop(2))  # enleve et renvoie l'element se trouvant a l'index i .pop(i), ou le dernier element si .pop()
print(f"{numeros} on a enleve l'element se trouvant a l'index 2")

print(f"l'index de 8: {numeros.index(8)}")  # donne l'index de l'element,renvoie error si l'element n'est pas ds la list

print(f"8 se trouve dans les numeros : {8 in numeros}")  # renvoie True or False

print(
    f"il y'a combien de 5 dans la liste numeros : {numeros.count(5)}")  # renvoie le nombre d'occurence d'une valeur

numeros.sort()  # classifie par ordre croissant et decroissant .sort(reverse=True)
print(numeros)
numeros.reverse()
print(f"{numeros} ")  # m'est en position inverse

numeros2 = numeros.copy()  # copie
print(f"numeros2: {numeros2} copie de numeros")

numeros.append(30)
print(f"{numeros}")

numeros.clear()  # supprime tous elements
print(f"{numeros} on a supprime tous les elements de la liste")

# exemple
nombres = [2, 2, 4, 6, 4, 1, 6]
uniques = []
for i in nombres:
    if i not in uniques:
        uniques.append(i)
print(uniques)

# .extend et .append
chiffres_1 = [6, 4, 7, 2]
chiffres_2 = [6, 4, 7, 2]
chiffres_manquand = [5, 3]

chiffres_1.append(chiffres_manquand)  #.append ajoute la liste dans la liste
print(f"{chiffres_1} ajout de [5, 3] avec .append)")

chiffres_2.extend(chiffres_manquand)  #.extend  ettend la liste
print(f"{chiffres_2} ajout de [5 et 3] avec .extend")
