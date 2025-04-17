import turtle
import random

LIST_OF_COLORS = ['red', 'blue', 'green', 'yellow', 'purple', 'black', 'pink', 'cyan']


class Cars(turtle.Turtle):
    def __init__(self):
        super(Cars, self).__init__()
        x_cord = random.randint(-300, 300)
        y_cord = random.randint(-250, 250)
        self.shape('square')
        self.color(random.choice(LIST_OF_COLORS))
        self.shapesize(stretch_len=2)
        self.penup()
        self.goto(x_cord, y_cord)

    def driving(self, speed):
        new_x = self.xcor() - speed
        self.goto(new_x, self.ycor())
