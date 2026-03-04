from turtle import Screen, Turtle

ecran = Screen()
franklin = Turtle()

# Dans cet exercice, votre mission est simple : tracer une ligne sous forme de petits tirets

ecran.setup(width=500, height=500)
ecran.title("#10 Turtle - Novice")

franklin.color("green")
franklin.shape("turtle")
franklin.shapesize(1.5, 1.5)

for _ in range(5):
    franklin.forward(10)
    franklin.penup()
    franklin.forward(10)
    franklin.pendown()

ecran.exitonclick()