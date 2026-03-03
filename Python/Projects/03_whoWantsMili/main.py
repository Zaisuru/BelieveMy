from data import LES_QUESTIONS
from question import Question
from logo import LOGO
from moteur import Moteur

# Générer des questions
questions = []
for question in LES_QUESTIONS:
    id = question["id"]
    phrase = question["question"]
    choix_a = question["propositions"][0]
    choix_b = question["propositions"][1]
    choix_c = question["propositions"][2]
    choix_d = question["propositions"][3]
    reponse = question["reponse"]
    nouvelle_question = Question(id, phrase, choix_a, choix_b, choix_c, choix_d, reponse)
    questions.append(nouvelle_question)

# Générer le tableau des prix
TABLEAU_DES_PRIX = [
    100,
    200,
    300,
    500,
    1_000,
    2_000,
    4_000,
    8_000,
    12_000,
    24_000,
    36_000,
    72_000,
    150_000,
    300_000,
    1_000_000
]

# Afficher le logo et le tableau des prix du jeu
print(f"{LOGO}\n\nVoici le tableau des prix :\n")

for i in range(len(TABLEAU_DES_PRIX)):
    print(f"{i + 1} - {TABLEAU_DES_PRIX[i]}")

# Afficher le total de questions
Question.total_questions()

moteur = Moteur(questions, TABLEAU_DES_PRIX)

# Boucle de vie
while True:
  # Poser une question
  a_bien_repondu = moteur.nouvelle_question()

  # Vérifier si on peut continuer
  if a_bien_repondu:
    # score total atteint
    if moteur.score == len(TABLEAU_DES_PRIX):
      print(f"Bravo ! Vous avez gagné {TABLEAU_DES_PRIX[-1]} euros ! À vous la vie de rêve !")
      break
    else:
      # afficher le montant gagné
      print(f"Bravo ! Vous atteignez les {moteur.montant_actuel} euros.")

      # stopper ou continuer
      choix = input("\nSouhaitez-vous arrêter ? (non / entrer)")

      if choix.lower() == "non":
        print(f"Vous décidez de partir avec vos {moteur.montant_actuel} euros à la question {moteur.score}.")
        break
  else:
    # fin du jeu
    print(f"Perdu ! Vous repartez avec {moteur.montant_actuel} euros.")
    break