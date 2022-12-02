import turtle


class Paddle(turtle.Turtle):
    def __init__(self, first_player):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        if first_player:
            self.goto(-350, 0)
        else:
            self.goto(350, 0)

    def up(self):
        new_y = self.ycor() + 30
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.goto(x=self.xcor(), y=new_y)
