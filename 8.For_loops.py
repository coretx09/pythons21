for item in ['Mosh', 'john', 'sarah', 'michel', 1, 2, 5.6, ]:
    print(item)

# compteur
for i in range(0, 10, 2):
    print(i)

# decompteur
for i in range(50, 5, -5):
    print(i)

# dessin
numbers = [5, 2, 5, 2, 2]
for i in numbers:
    print("x" * i)

# list
prices = [15, 20, 50]  # prix des produits
total = 0
for i in prices:  # avec i represente tous les elements de prices (variable compteur)
    prix = i
    print(f"prix = {prix} euros")  # affiche tous les elements de prices
    total += i
print(f"Total des prix = {total} euros")



for x in range(3):
    for y in range(2):
        print(f"({x}, {y})")
