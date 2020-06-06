def separateur():
    print("- " * 30)


beau_temps = False
money = False
if beau_temps:
    print("oui c'est vrai, il fait beau")
    print("la vie est belle")
elif money:
    print("tant que j'ai l'argent, la vie est belle")
else:
    print("c'est faux")
    print("je ne peut pas supporter cette vie")
separateur()

# logical operations
# or et and:

if beau_temps and money:
    print("il fait beau et j'ai l'argent")
elif beau_temps or money:
    print("c'est vrai une bonne temperature ou l argent peut rendre heureux")
else:
    print("c'est gate")
separateur()

# not : pour que not soit execute il faut que sa condition renvoie False

copine = True
travail = False
if copine and not travail:
    print("j'ai une copine mais je ne travail pas ")
elif copine or not travail:
    print("je sais que tu a soit une copine ou bien tu travail")
