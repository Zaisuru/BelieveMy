class Animal:
    def __init__(self, nombre_de_pattes, nombre_yeux, poils, nom):
        self.nombre_de_pattes = nombre_de_pattes
        self.nombre_yeux = nombre_yeux
        self.poils = poils
        self.nom = nom

    def boire(self):
        print(f"{self.nom} est en train de boire.")

    def manger(self):
        print(f"{self.nom} est en train de manger.")