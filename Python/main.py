from chat import Chat
from chien import Chien


tarzan = Chat(4, 2, "long", "Tarzan", True)
tarzan.parler()
tarzan.boire()
tarzan.manger()
print(tarzan.stock_de_croquettes)
Chat.bilan_des_stocks()
tarzan.aime_herbe_chat = True

arthus = Chien(4, 2, "long", "Arthus")
arthus.parler()
arthus.boire()