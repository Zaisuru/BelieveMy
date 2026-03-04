from turtle import Turtle, Screen
from random import randint, shuffle

ecran = Screen()
ecran.setup(width=500, height=400)
ecran.title("Le lièvre et la tortue")
ecran.register_shape("hare.gif")

turtle = Turtle(shape="turtle")
turtle.color("green")
turtle.penup()
turtle.goto(x=-235, y=-100)

hare = Turtle(shape="hare.gif")
hare.penup()
hare.goto(x=-235, y=100)

competitions = [turtle, hare]

game = True

shuffle(competitions)
while game:
    for competition in competitions:
        distance = randint(-3, 5 )
        competition.forward(distance)

        if competition.xcor() > 230:
            game = False


ecran.exitonclick()