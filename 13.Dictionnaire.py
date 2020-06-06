"""
    DICTIONNAIRES : = {clet:objet, .....} une clet peut contenir qu'un seul objet

À la différence des séquences, qui sont indexées par des nombres, les dictionnaires sont indexés par des clés, qui
 peuvent être de n'importe quel type immuable ; les chaînes de caractères, les tuples et les nombres peuvent toujours
  être des clés.

"""

informations = {"nom": "ngampio",
                "age": 30,
                "verifie": True
                }
print(informations)

print(informations.get("sexe", "la clet sexe n'existe pas"))  # si la clet n'exste pas .get renvoie None ou peut renvoie
                           #  une chaine de caractere ou une variable si cela est specifier

print(f"voici les clets existants : {informations.keys()}")  # affiche les clets


informations["aniversaire"] = "29 09 1990"    # ajout d'un element avec la clet
informations["age"] = 50  # modification de la valeur d'un element avec sa clet
print(informations)

"""
Un objet mapping fait correspondre des valeurs hashable à des objets arbitraires. Les mappings sont des objets muables.
  __(mapping en anglais) __  Conteneur permettant de rechercher des éléments à partir de clés
"""

# les chiffres en lettres
telephone = input("telephone: ")
chiffre_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = " "
for ch in telephone:
    output += chiffre_mapping.get(ch, "!") + " "
print(output)



# smilies
message = input("> ")  # on va correspondre les valeurs entrees arbitraires
words = message.split(" ")  # .split permet de couper une chaine de caractere (objet immutable) en  liste
smilies = {
    ":)": "😘",        # avec les valeurs hashable
    ":(": "😞"
}
output = " "
for ch in words:     # pour tous valeurs quelcquonques ch dans la liste words
    output += smilies.get(ch, ch) + " "  # s'ils correspondents aux clefs (ch) des valeurs
print(output)
