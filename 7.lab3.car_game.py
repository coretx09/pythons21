command = ""
demareur = False  # variable sera utiliser pour start et stop car les deux sont liees
# avant qu'on stop on doit d'abord demarer
while True:  # { while command.lower() != "quit" } condition du bloc
    command = input("> ").lower()  # operation a effectuer
    if command == "start":
        if demareur:  # cette condition ne sera pas execute pour la premiere fois car
            # demareur = False, mais pour le reste de fois du bloc car demareur = True deja
            print("la voiture est deja en marche")
        else:
            demareur = True  # cette condition sera execute juste pour la premiere fois, car une
            # une fois execute: demareur = True dans tout le bloc
            print("Voiture demare...")
    elif command == "stop":
        if not demareur:  # pour la 1ere fois cette condition ne sera pas execute car
            # demareur = True, mais pour le reste de fois car demareur = False
            print("la voiture n'etait pas allume ")
        else:
            demareur = False  # cette condition sera execute juste pour la premiere fois, car une
            # une fois execute: demareur = False dans tout le bloc
            print("Voiture arrete...")
    elif command == "help":
        print("""
              start - to start the car
              stop - to stop the car 
              quit - to quit
              """)
    elif command == "quit":  # condition pour arreter le bloc
        print("Au revoir Mr")
        break
    else:
        print("""desole, je n'ai pas compris votre commande
        tapez help pour plus d'infos
        """)

