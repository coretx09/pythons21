try:
    age = int(input("ton age: "))
    print(age)
    income = 2000
    risk = income / age
    print("{:.2g}".format(risk))
except ValueError:               # on cible les erreurs de valeur
    print("Veuillez entree votre vrai age")
except ZeroDivisionError:
    print("on ne peut diviser un nombre par zero ")
except:             # pour tous les erreurs possibles
    print("une error c'est produite ")


# EXCEPTIONS DANS UN BLOC
# guessing game
secret_number = 8  # le nombre secret a trouver
guess_limit = 3    # nombre de chance
guess_count = 0    # compteur de nombre de chance
while guess_count < guess_limit:  # le bloc
    try:
        guess = int(input("Guess: "))  # votre nombre choisi
        guess_count += 1  # on fai l'indentation si seulement il n'y a pas d'error
        if guess == secret_number:  # condition dans un bloc
            print("BRAVOS \n Vous avez trouve le nombre secret ")
            break  # arrete le bloc quand la condition est vrai (True)
        else:
            print("Veuillez ressayer!")  # s'affiche a chaque fois que la condition est fause(False)
            print(f"il vous reste {guess_limit - guess_count} chance")
    except:  # on affiche et on  recommence la boucle ou elle c'est arrete
        print("une Error c'est produite ")
else:
    print("Desole, Vous avez echouer ")  # s'affiche une fois le bloc termine