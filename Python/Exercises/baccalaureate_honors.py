# 10 : passable
# 12 : assez bien
# 14 : Bien
# 16 : Très bien

# Consignes
"""
Ajouter un 4ème champ dans la liste eleves nommé mention et lui définir la valeur ci-dessus en fonction de la moyenne

"""

eleves = [
  {
    "prenom": "Jessica",
    "nom": "Pounel",
    "moyenne": 14
  },
  {
    "prenom": "Pierre",
    "nom": "John",
    "moyenne": 10
  },
  {
    "prenom": "Samantha",
    "nom": "Diao",
    "moyenne": 17
  },
  {
    "prenom": "Casey",
    "nom": "Vret",
    "moyenne": 15
  },
  {
    "prenom": "Jasmine",
    "nom": "Pontri",
    "moyenne": 11
  },
  {
    "prenom": "Zoro",
    "nom": "Koro",
    "moyenne": 18
  },
  {
    "prenom": "Jordan",
    "nom": "Iotri",
    "moyenne": 10
  }
]

for eleve in eleves:
    if  eleve["moyenne"] >= 16:
        eleve["mention"] = "Très bien"
    elif eleve["moyenne"] >= 14:
        eleve["mention"] = "Bien"
    elif eleve["moyenne"] >= 12:
        eleve["mention"] = "Assez bien"
    else :
        eleve["mention"] = "Passable"

print(eleves)