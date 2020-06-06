# Definition d'une fonction
def bonjour(nom):          # nom = parametre
    return f"bonjour Mr {nom}"

# Appel d'une fonction
bonjour("eric")  # ne va rien afficher avec return

# il faut appeler la fonction print() pour afficher
print(bonjour(1))
print(bonjour("Ngampio"))
a = "sauvet"
print(bonjour(a))

# la fonction qui affiche elle meme
def salutation(prenom):
    print(f"Salut {prenom}")
    print(" bienvenue")

salutation("charles")  # sans parametre salutation() renvoie error

# fonction avec parametre par defauts
def aurevoir(nom=""): 
    print(f"Good bye Mr {nom}")
aurevoir()
aurevoir("Jean")


# fonction sur les liste avec 3 parametre
def liste_search(A:list, N:int, x:int):
    """
    :param A: nom de la liste
    :param N: diapason
    :param x: element a rechercher
    :return: index de x dans la liste A ou -1 s'il y'en a pas
    """
    for i in range(N):
        if A[i] == x:
            return i
        else:
            return f"{x} ne se trouve pas dans la liste {A}"


liste1 = [1, 2, 3, 4, 0, 4]
print(liste_search(liste1, 500, 400))


# fonction sur les dictionnaires
def smilies_converter(message):
    words = message.split(" ")  # .split permet de couper une chaine de caractere (objet immutable) en  liste
    smilies = {
    ":)": "😘",        # avec les valeurs hashable
    ":(": "😞"
     }
    output = " "
    for ch in words:     # pour tous valeurs quelcquonques (ch) dans la liste words
        output += smilies.get(ch, ch) + " "  # s'ils correspondents aux clefs (ch) on les convertis
    return output
