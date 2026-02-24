"""
Dans cet exercice, vous allez devoir :

Générer une liste de 100 notes
Chaque note doit contenir :
Le prénom et le nom de l'élève
Une note sur 300 - il s'agit d'un examen officiel

à la fin il faut afficher : "Le meilleur élève est X avec une note de X / 300
"""

import random
from faker import Faker
fake = Faker("fr_FR")
_class = []

for _ in range (100):
    _class.append([random.randint(0,300), fake.unique.name()])
    print(_class)

best_student = max(_class[1])
print(f"Le meilleur élève est {best_student[1]} avec une note de {best_student[0]} / 300")