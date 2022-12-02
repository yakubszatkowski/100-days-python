import turtle


class Level(turtle.Turtle):
    def __init__(self):
        super(Level, self).__init__()
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(x=-250, y=250)
        self.write(arg=f'Level: {self.level}', align='center', font=('Comic Sans', 15, 'bold'))

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(arg=f'GAME OVER', align='center', font=('Comic Sans', 20, 'bold'))
        print('Game over')

    def next_level(self):
        self.clear()
        self.goto(x=-250, y=250)
        self.level += 1
        self.write(arg=f'Level: {self.level}', align='center', font=('Comic Sans', 15, 'bold'))
