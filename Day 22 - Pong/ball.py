import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 5
        self.y_move = 5

    def serve(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_collision(self):
        self.y_move *= -1

    def paddle_collision(self):
        self.x_move *= -1

    def reset_position(self):
        self.x_move *= -1
        self.goto(0, 0)

