print("BIENVENUES ", "Veuillez nous fournir quelques informations ", sep='\n   ')

''' nom_utilisateur = input("votre nom: ")
print("   Tres bien", "Maintenant veuillez nous fournir votre age", sep='\n   ')
'''
age = int(float((input("votre age: "))))
if (age) <= 18:
    print("Desole vous etes encore mineur")

else:
    print("bien")

print("MERCI POUR TOUTES CES INFORMATIONS")
#print("Nom = ", nom_utilisateur)
print("Age = {:.1g}".format(age))

birth_year = input("Entrer votre anne da naissance")
type_str = "type de caracters "
if type(birth_year) == type(type_str):
    birth_day = int(birth_year)
#print(type(birth_year))
#ton_age = 2020 - birth_year
