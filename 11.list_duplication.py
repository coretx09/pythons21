"""
    Modifier les elements d'une liste: DUPLICATION
"""

liste1 = [4, 5, 8, 9, 10]

print("modification avec liste2 = liste1 ")
liste2 = liste1  # les changements effectuer par la suite a la [liste1] vont s'appliquer aussi a [liste2] et vis versa
print(liste2)  # [liste2] n'est que [liste1] mais avec de noms differents
# modifications des elements avec l'index
liste1[0] = 23
liste1[1] = 20
liste1[2] = 56
liste1[3] = 23
liste1[4] = 15
print(liste1)
print(liste2)
liste2[0] = 0
print(liste1)  # liste1 aussi a change


# DUPLICATIN :

print("modification avec liste3 = liste1.copy() ")
liste3 = list(liste1)  # les changements effectuer par la suite a la [liste1] ne vont pas s'appliquer a [liste3]
# liste3 = liste1.copy() fait la meme chose
print(liste3)
liste1[0] = 10
print(liste1)
print(liste3)

print("modification avec liste4[i] = liste1[i] ")  # les changements ne s'applique pas par la suite
lonugueure_liste1 = len(liste1)
liste4 = [0] * lonugueure_liste1  # meme nombre d'elements
for i in range(lonugueure_liste1):
    liste4[i] = liste1[i]  # ils doivent avoir le meme nombre d'elements
print(liste4)
liste1[2] = 8
print(liste4)


