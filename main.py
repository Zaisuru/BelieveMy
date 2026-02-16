def additionner(*nombres):
    """
    Additionne les nombres passés en arguments

    Args :
        nombres : une suite de nombres
        nombres_après_la_virgule : Le nombre de chiffres après la virgule
    Returns :
        Retourne l'addition des nombres passés en arguments
    """
    total = 0

    for nombre in nombres :
        total += int(nombre)
    return total

print(additionner(5, 5,5,5,5,5,5))