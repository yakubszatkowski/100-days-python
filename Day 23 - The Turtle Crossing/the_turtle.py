import turtle


class The_Turtle(turtle.Turtle):
    def __init__(self):
        super(The_Turtle, self).__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
