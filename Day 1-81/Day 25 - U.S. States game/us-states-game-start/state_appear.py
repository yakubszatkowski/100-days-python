import pandas as pd
import turtle

states = pd.read_csv('50_states.csv')


class State(turtle.Turtle):
    def __init__(self):
        super(State, self).__init__()
        self.hideturtle()
        self.penup()
        self.color('black')

    def state_popup(self, right_state):
        row = states[states.state == right_state]
        x_coor = int(row.x)
        y_coor = int(row.y)
        self.goto(x_coor, y_coor)
        self.write(f'{right_state}')

    def you_won(self):
        self.goto(0, 0)
        self.write(f'YOU GUESSED EVERY STATE!', align='center', font=('Comic Sans', 30, 'bold'))

# for right_state in states['state']:
#     row = states[states.state == right_state]
#     print(int(row.x), int(row.y))
