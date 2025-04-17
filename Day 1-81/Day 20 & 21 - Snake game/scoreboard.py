from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x=0, y=270)
        self.score_text()

    def score_text(self):
        self.clear()
        self.write(arg=f'Score: {self.score}   High Score: {self.high_score}', align='center', font=('Comic Sans',
                                                                                                     12, 'bold'))

    def update(self):
        self.score += 1
        self.score_text()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.score_text()
        with open('data.txt', mode='w') as data:
            data.write(f'{self.high_score}')

    # def game_over(self):
    #     self.goto(raw_data=0, y=0)
    #     self.write(arg=f'GAME OVER', align='center', font=('Comic Sans', 12, 'bold'))
