import turtle as t
import random as r
screen = t.Screen()
screen.setup(width=500, height=480)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win a race?: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = -150
all_turtles = []
is_race_on = False

for turtle_color in colors:
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(turtle_color)
    new_turtle.penup()
    new_turtle.setpos(x=-200, y=y_position)
    y_position += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f'The winner is {winner}! You\'ve won!')
            else:
                print(f'The winner is {winner}! You\'ve lost...')
            is_race_on = False
        random_distance = r.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
