import turtle


def middle_split():
    cross = turtle.Turtle()
    cross.hideturtle()
    cross.speed('fastest')
    cross.penup()
    cross.pencolor('white')
    cross.goto(0, -285)
    cross.setheading(90)
    for _ in range(15):
        cross.pendown()
        cross.forward(20)
        cross.penup()
        cross.forward(20)
