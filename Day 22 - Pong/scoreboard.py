from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.score_text()

    def score_text(self):
        self.clear()
        self.goto(x=0, y=270)
        self.write(arg=f'{self.left_score}      {self.right_score}', align='center', font=('Comic Sans', 20, 'bold'))

    def left_point(self):
        self.left_score += 1
        self.score_text()

    def right_point(self):
        self.right_score += 1
        self.score_text()
