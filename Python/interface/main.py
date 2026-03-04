from turtle import Screen, Turtle

ecran = Screen()
ecran.setup(width=500, height=500)
ecran.title("Mon programme de test")

franklin = Turtle()

franklin.color("green")
franklin.shape("turtle")
franklin.shapesize(1.5, 1.5)

franklin.penup()
franklin.goto(x=-125, y=125)

print(franklin.xcor())
