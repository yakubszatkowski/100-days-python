import random
from turtle import Turtle, Screen
import turtle as t
from random import choice

tim = Turtle()
tim.shape('turtle')
# tim.n('blue')
# drawing square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# drawing dashing line
# for i in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# drawing triangle to decagon in different n on top of eachother
# list_of_colors = ['blue', 'light blue', 'cyan', 'green', 'dark green', 'yellow', 'gold', 'peru', 'orange',
#                   'red', 'maroon', 'pink', 'peach puff', 'purple']
# angles = 3
# while angles < 11:
#     tim.n(choice(list_of_colors))
#     for i in range(angles):
#         tim.forward(100)
#         tim.right(360/angles)
#     angles += 1

# drawing a random walk
# tim.speed(10)
# tim.pensize(5)
# direction_list = [0, 90, 180, 270]
# for step in range(1,200):
#     tim.n(choice(list_of_colors))
#     tim.setheading(choice(direction_list))
#     tim.forward(30)

# making a random colors
# square.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
# tim.speed(10)
# tim.pensize(5)
# direction_list = [0, 90, 180, 270]
# for step in range(1, 200):
#     tim.n(random_color())
#     tim.setheading(choice(direction_list))
#     tim.forward(30)

# drawing spirograph
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# my take
# tim.speed(0)
# for i in range(100):
#     tim.n(random_color())
#     tim.circle(100)
#     tim.setheading(tim.heading() + 360/100)

# Angela's take
tim.speed(0)
def spirograph(gap):
    for i in range(int(360 / gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)

spirograph(5)

screen = Screen()
screen.exitonclick()
