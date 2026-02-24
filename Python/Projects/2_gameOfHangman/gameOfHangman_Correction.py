import faker
import random
import replit
import gameofHangman_logo

fake = faker.Faker()

# Génération du mot
wordList = [fake.word() for _ in range(10)]
wordToFind = list(random.choice(wordList))
wordLen = len(wordToFind)

# Préparation de l'affichage (tirets)
x = ["_"] * wordLen
wordDisplay = "".join(x)

userWordTried = []
life = 6

print(gameofHangman_logo.LOGO)  # Affiche le logo au lancement

while life > 0:
    # 1. On demande la lettre
    userLetter = input("Quelle est votre lettre ? ").lower()

    # 2. On nettoie l'écran IMMEDIATEMENT pour redessiner proprement
    replit.clear()
    print(gameofHangman_logo.LOGO)  # On réaffiche le titre après le clear

    if userLetter in userWordTried:
        print(f"La lettre '{userLetter}' a déjà été proposée !")
    else:
        userWordTried.append(userLetter)

        if userLetter in wordToFind:
            # On met à jour les tirets
            for i in range(wordLen):
                if wordToFind[i] == userLetter:
                    x[i] = userLetter
            wordDisplay = "".join(x)
            print("Bien joué !")
        else:
            print(f"La lettre '{userLetter}' n'est pas dans le mot.")
            life -= 1

    # 3. On affiche l'état du jeu
    print(wordDisplay)
    # On utilise 6 - life pour faire évoluer le dessin
    print(gameofHangman_logo.PENDU[6 - life])

    # 4. Vérification de victoire
    if "_" not in x:
        print(f"Bravo ! Vous avez trouvé le mot : {''.join(wordToFind)}")
        break

if life == 0:
    print(f"PERDU ! Le mot était : {''.join(wordToFind)}")