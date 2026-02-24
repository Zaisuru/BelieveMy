from animal import Animal

class Chien(Animal):
    def __init__(self, nombre_de_pattes, nombre_yeux, poils, nom):
        super().__init__(nombre_de_pattes, nombre_yeux, poils,nom)


    def parler(self):
        print(f"{self.nom} aboie.")

