import random

WhoGame = input("Qui sont les personnes qui peuvent payer ? \n"
                "Séparez-les par des virgules. \n")
WhoGame_Sorting = WhoGame.split(", ")
WhoGame_Choice = random.choice(WhoGame_Sorting)
print(f"C'est à {WhoGame_Choice} de payer pour tout le monde !")
