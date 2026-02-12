# noinspection LanguageDetectionInspection
"""
Dans cet exercice sera de permettre à n'importe quel étudiant en terminal du bac général de calculer sa moyenne scolaire, grâce aux coeficients de chaque matière.

Voici ce que vous devrez réaliser :

Bienvenue dans le calculateur de moyenne scolaire pour le bac général !

Voici les coefficients actuels :
    -> 8 - Spécialité
    -> 6 - Langue vivante principale
    -> 6 - Langue vivante secondaire
    -> 6 - Histoire-géographie
    -> 6 - Enseignement scientifique
    -> 6 - EPS
    -> 2 - EMC
    -> 5 - Français écrit
    -> 5 - Français oral
    -> 8 - Philosophie
    -> 10 - Grand oral
    -> 16 - Spécialité 1
    -> 16 - Spécialité 2

Quelle est votre moyenne pour : Spécialité ? 15
Quelle est votre moyenne pour : Langue vivante principale ? 10
Quelle est votre moyenne pour : Langue vivante secondaire ? 12
Quelle est votre moyenne pour : Histoire-géographie ? 5
Quelle est votre moyenne pour : Enseignement scientifique ? 20
Quelle est votre moyenne pour : EPS ? 1
Quelle est votre moyenne pour : EMC ? 12
Quelle est votre moyenne pour : Français écrit ? 14
Quelle est votre moyenne pour : Français oral ? 15
Quelle est votre moyenne pour : Philosophie ? 9
Quelle est votre moyenne pour : Grand oral ? 10
Quelle est votre moyenne pour : Spécialité 1 ? 12
Quelle est votre moyenne pour : Spécialité 2 ? 13

Votre moyenne cette année est de 11.49

"""
from wsgiref.util import request_uri

print(f"Bienvenue dans le calculateur de moyenne scolaire pour le bac général \n\n"
      f"Voici les coefficients actuels : \n"
      f"\t -> 8 - Spécialité \n"
      f"\t -> 6 - Langue vivante principale \n"
      f"\t -> 6 - Langue vivante secondaire \n"
      f"\t -> 6 - Histoire-géographie \n"
      f"\t -> 6 - Enseignement scientifique \n"
      f"\t -> 6 - EPS \n"
      f"\t -> 2 - EMC \n"
      f"\t -> 5 - Français écrit \n"
      f"\t -> 5 - Français oral \n"
      f"\t -> 8 - Philosophie \n"
      f"\t -> 10 - Grand oral \n"
      f"\t -> 16 - Spécialité 1 \n"
      f"\t -> 16 - Spécialité 2\n")

materials = [
      ["Spécialité",
       8],
      ["Langue vivante principale",
       6],
      ["Langue vivante secondaire",
       6],
      ["Histoire-géographie",
       6],
      ["Enseignement scientifique",
       6],
      ["EPS",
       6],
      ["EMC",
       2],
      ["Français oral",
       5],
      ["Français écrit",
       5],
      ["Philosophie",
       8],
      ["Grand oral",
       10],
      ["Spécialité 1",
       16],
      ["Spécialité 2",
       16]
]

average = []
coefficients = []

for note in materials:
      your_average = float(input(f"Quelle est votre moyenne pour : {note[0]} ? "))
      average.append(your_average * note[1])
      coefficients.append(note[1])

final_average = sum(average) / sum(coefficients)
print(f"Votre moyenne cette année est de {round(final_average, 2)} !")

