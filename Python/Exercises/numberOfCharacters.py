
texte = input("Quel texte voulez-vous compter ? \n\n")

mots = texte.split()

compteur = {}

for mot in mots :
    compteur[mot] = len(mot)

print(f"\n {compteur}")