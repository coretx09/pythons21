def lbs_en_kg(poids):   # module lbs en kg
    return poids * 0.45

def kg_en_lbs(poids):   # module kg en lbs
    return poids / 0.45

# le nombre avec le plus grand indice
def search_max(numeros):
    max = numeros[0]
    for i in numeros:
        if i > max:
            max = i
    return max

