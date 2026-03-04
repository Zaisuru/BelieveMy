from turtle import Turtle, Screen
from random import choice


COULEURS = ["#2980b9", "#613BDB", "#34495e", "#e67e22", "#2ecc71", "#e74c3c", "#27ae60", "#9b59b6", "#7f8c8d"]

ecran = Screen()
ecran.setup(width=500, height=500)

franklin = Turtle()
franklin.shape("turtle")


for mouvements in range(3, 13):
    franklin.color(choice(COULEURS))
    angle = 360 / mouvements

    for _ in range(mouvements):
        franklin.forward(50)
        franklin.right(angle)


ecran.exitonclick()