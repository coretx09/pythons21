"""
Une classe est un ensemble incluant des variables ou attributs et des fonctions ou méthodes. Les attributs sont
 des variables accessibles depuis toute méthode de la classe où elles sont définies. En python, les classes sont
  des types modifiables.
"""

# Déclaration d’une classe
class Point:
    def move(self):   # declaration d'une methode ou fonction, elle peut contenir des parametres
        print("move")
    def draw(self):
        print("draw")

# Instanciation d’une classe
point1 = Point()
print(type(point1))

point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

class touch_class:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def droite(self):
        print("a droite")
    def gauche(self):
        print("a gauche")
touch = touch_class(40, 60)
touch.x = 79
print(touch.x)

# constructions

class person_class:
    def __init__(self, name):
        self.name = name     # attributs (variable) global

    def salutation(self):
        print(F" bonjour, Mr {self.name}")

john = person_class("john smith")
print(john.name)
john.salutation()

marc = person_class("mar hunter")
marc.salutation()


# inheritance

class animal_class:
    def marche(self):
        print("animal qui marche")


class dog_class(animal_class):   # dog_class est liee a animal_class : on peut utiliser les fonctions et attributs de
    # animal_class avec dog_class
    def aboie (self):
        print("le chien qui aboie ")


class cat_class(animal_class):
    def grimpe(self):
        print("le chat grimpe")

dog1 = dog_class()
dog1.marche()
dog1.aboie()

cat1 = cat_class()
cat1.marche()
cat1.grimpe()


# Modules:

import mes_fonctions
print(mes_fonctions.kg_en_lbs(56))
from mes_fonctions import kg_en_lbs
print(kg_en_lbs(56))

# le plus grand nombre
nombres = [254, 45664, 773788, 646, 5446]
from mes_fonctions import search_max
print(search_max(nombres))




