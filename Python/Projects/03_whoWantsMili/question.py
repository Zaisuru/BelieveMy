class Question:
    nombre_de_questions = 0

    def __init__(self, id, phrase, choix_a, choix_b, choix_c, choix_d, reponse):
        self.id = id
        self.phrase = phrase
        self.choix_a = choix_a
        self.choix_b = choix_b
        self.choix_c = choix_c
        self.choix_d = choix_d
        self.reponse = reponse
        Question.nombre_de_questions += 1

    @staticmethod
    def total_questions():
        print(f"\nIl y a {Question.nombre_de_questions} questions en stock.")