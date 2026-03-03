from random import choice


class Moteur:

  def __init__(self, questions, tableaux_des_prix):
    self.questions = questions
    self.tableau_des_prix = tableaux_des_prix
    self.score = 0
    self.montant_actuel = 0
    self.montant_garanti = 0

  def nouvelle_question(self):
    # choisir une question
    question = choice(self.questions)

    # retirer la question de la liste des questions
    index_de_la_question = self.questions.index(question)
    del self.questions[index_de_la_question]

    # afficher la question
    print(f"\n\033[92mQuestion pour {self.tableau_des_prix[self.score]} euros\n-> {question.phrase}\033[00m\n\n\t{question.choix_a}\n\t{question.choix_b}\n\t{question.choix_c}\n\t{question.choix_d} (réponse : {question.reponse})")

    # récupérer la réponse
    choix = input("\nRéponse: ")

    # vérifier la réponse et retourner le résultat
    resultat = self.verifier_reponse(question, choix)
    return resultat

  def verifier_reponse(self, question, choix):
    if choix.lower().strip() == question.reponse.lower().strip():
      self.score += 1
      self.calculer_palier()
      return True
    else:
      print(f"Vous avez dit '{choix}'")
      self.montant_actuel = self.montant_garanti
      return False

  def calculer_palier(self):
    if self.tableau_des_prix[self.score - 1] == 1_000 or self.tableau_des_prix[self.score - 1] == 24_000:
      self.montant_garanti = self.tableau_des_prix[self.score - 1]
      print("\033[92mNouveau palier débloqué.\033[00m")

    # calculer montant actuel
    self.montant_actuel = self.tableau_des_prix[self.score - 1]
