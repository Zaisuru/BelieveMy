age = 70

print("Bienvenue dans la discothèque")

if age >= 18 and age <= 70:
    print("Vous êtes majeur")
elif age >= 70:
    print("Vous pouvez entrer")
else:
    passe_droit = input("Avez-vous un passe-droit ?").lower()
    if passe_droit == "oui":
        print("Vous pouvez entrer")
    else:
        print("Vous ne pouvez pas entrer")

