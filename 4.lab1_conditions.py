age = int(input("votre age: "))
genre = input("(M)masculin ou (F)feminin: ")
if genre.upper() == "M" and age >= 18:
    print(f"un homme adulte, age de {age} ans ")
elif genre.upper() == "M" and age < 18:
    print("un jeune homme mineur, age de", age, "ans" )
elif genre.upper() == "F" and age >= 18:
    print(f"une Femme adulte ,age de {age} ans")
elif genre.upper() == "F" and age < 18:
    print(f"jeune femme mineure age, de {age} ans")
else:
    print("une erreure a du se produire\n Veuillez recommencer ")