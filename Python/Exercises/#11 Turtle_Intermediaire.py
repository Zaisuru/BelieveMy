from turtle import Screen, Turtle
from turtledemo.clock import setup

ecran = Screen()
franklin = Turtle()

# Dans cet exercice intermédiaire, votre mission est de former un carré grâce à notre tortue Franklin.

ecran.setup(width=500, height=500)
ecran.title("#11 Turtle - Intermédiaire")

franklin.color("green")
franklin.shape("turtle")
franklin.shapesize(1.5, 1.5)


for _ in range(4):
    franklin.forward(130)
    franklin.left(90)

ecran.exitonclick()