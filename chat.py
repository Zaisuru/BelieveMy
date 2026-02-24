from animal import Animal

class Chat(Animal):
    stock_de_croquettes = 5

    def __init__(self, nombre_de_pattes, nombre_yeux, poils, nom, aime_herbe_chat):
        super().__init__(nombre_de_pattes, nombre_yeux, poils,nom)
        self.aime_herbe_chat = aime_herbe_chat

    def parler(self):
        print(f"{self.nom} miaule.")

    def boire(self):
        print(f"{self.nom} s'humecte")

    def manger(self):
        Chat.stock_de_croquettes -= 0.15
        super().manger()

    @staticmethod
    def bilan_des_stocks():
        print(f"Le stock de croquette est à : {Chat.stock_de_croquettes}")
