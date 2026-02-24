import random

user_choice = int(input("Pierre = 0 ? Feuille = 1 Ciseaux = 2 ? "))

compute_choice = random.randint(0, 2)

if (user_choice == 0 and compute_choice == 1) or (user_choice == 1 and compute_choice == 2) or (user_choice == 2 and compute_choice == 0):
    print("Vous avez perdu")
else :
    print("Vous avez gagnez")

