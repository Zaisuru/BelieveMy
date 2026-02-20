class Utilisateur:
    def __init__(self, pseudo_que_je_recois, biograhpie):
        self.pseudo = pseudo_que_je_recois
        self.abonnes = 0
        self.personnes_suivis = 0
        self.biograhpie = biograhpie


    def ajouter_un_nouvel_abonne(self):
        self.abonnes += 1
        print("Vous avez un nouvel abonné")



class Voiture:

    def __init__(self, marque, modele, prix, motorisation, nombre_de_porte):
        self.marque = marque
        self.modele = modele

    @classmethod
    def tesla_model_3(cls):
        return cls("tesla", "model3", 50000, 300, 2)

    @classmethod
    def peugeot_rcz(cls):
        return cls("Peugeot", "RCZ", 30000, 300, 2)

tesla_model_3 = Voiture.tesla_model_3()
peugeot_rcz = Voiture.peugeot_rcz()

print(peugeot_rcz.marque)