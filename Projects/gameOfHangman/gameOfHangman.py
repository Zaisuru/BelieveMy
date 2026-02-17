# Import des modules
import faker
import random
import replit
import gameofHangman_logo
fake = faker.Faker()

# Génération des mots
wordList = []
for _ in range (300):
    wordList.append(fake.word())

# Sélection du mot
wordToFind = random.choice(wordList)
wordToFind = list(wordToFind)
x = []
word = len(wordToFind)

# Changement du mot par des _
i = 0
while i != word:
    x.append("_")
    i += 1
# Chargement des variables users
wordDisplay = "".join(x)
userWordTried = []
life = 6

#Affichage du logo
print(gameofHangman_logo.LOGO)

#Boucle de vie
while life > 0:
    # Demande user
    userLetter = input("Quelle est votre lettre ? ").lower()
    # Nettoyage de l'écran
    replit.clear()

    if userLetter not in userWordTried:
        if userLetter in wordToFind :
            userWordTried.append(userLetter)
            for i in range(word):
                if wordToFind[i] == userLetter:
                    x[i] = userLetter
                    wordDisplay = "".join(x)
                    print(wordDisplay)
            if "_" not in wordDisplay:
                print(f"Bravo vous avez trouvé le mot {wordDisplay}")
        else:
            print(wordDisplay)
            life -= 1

    else:
        print(f"La lettre {userLetter} est déjà trouvée")

    print({gameofHangman_logo.PENDU[6 - life]})


    continue

if life == 0:
    print(f"Dommage ! vous avez perdu ! \n"
          f"Le mot à trouver était {"".join(wordToFind)}")