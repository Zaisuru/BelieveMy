import random
"""
Votre mission dans cet exercice est de créer un générateur de mot de passe sécurisé !

Voici le résultat que vous devez réussir à obtenir :


Bienvenue dans le générateur de mot de passe !

Combien de lettres souhaitez-vous ?
Combien de nombres souhaitez-vous ?
Combien de symbole souhaitez-vous ?

Voici votre mot de passe :

"""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = []

print("Bienvenue dans le générateur de mot de passe ! \n")

howMany_letter = int(input("Combien de lettres souhaitez-vous ? "))
howMany_number = int(input("Combien de nombres souhaitez-vous ? "))
howMany_symbol = int(input("Combien de symboles souhaitez-vous ? "))


for i in range(0, howMany_letter):
    password.append(random.choice(letters))
for i in range(0, howMany_number):
    password.append(random.choice(numbers))
for i in range(0, howMany_symbol):
    password.append(random.choice(symbols))

print(f"Votre mot de passe est {"".join(password)}")