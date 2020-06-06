# guessing game
secret_number = 8  # le nombre secret a trouver
guess_limit = 3    # nombre de chance
guess_count = 0    # compteur de nombre de chance
while guess_count < guess_limit:  # le bloc
    guess = int(input("Guess: "))  # votre nombre choisi
    guess_count += 1
    if guess == secret_number:  # condition dans un bloc
        print("BRAVOS \n Vous avez trouve le nombre secret ")
        break  # arrete le bloc quand la condition est vrai (True)
    else:
        print("Veuillez ressayer!")  # s'affiche a chaque fois que la condition est fause(False)
        print(f"il vous reste {guess_limit - guess_count} chance")
else:
    print("Desole, Vous avez echouer ")  # s'affiche une fois le bloc termine
