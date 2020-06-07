phrase = "une famille "
print(phrase)
print(phrase[0])  # affiche le premier element
print(phrase[1:])  # affiche le deuxieme element jusqu'au dernier
print(phrase[:7])  # affiche le premier au dernier 6e element
print(phrase[1:7])  # affiche le 2e element au 6e element

# formated string

first = "sauvet"
last = "ngampio"
message = first + ' [' + last + '] is a coder'
print(message)
message_2 = first + last
print(message_2)
message_3 = f"{first} [{last}] is a coder"
print(message_3)

# string methods v

print(len(phrase))  # renvoie le nombre de caracteres
print(phrase.upper())  # majuscule
print((phrase.lower()))  # minuscule
print(phrase.index("ille "))  # renvoie l indice (si le caractere recherche n existe pas renvoie error)
print(phrase.find("i"))  # renvoie l indice (si .... renvoie -1)
print(phrase.replace("famille", "fille"))
print(phrase)  # "famille" n'est pas remplace dans la variable elle meme
print(phrase.count("l"))  # renvoie le nombre d'element ayant la meme valeur dans la chaine
print("une" in phrase)  # renvoie True ou False
