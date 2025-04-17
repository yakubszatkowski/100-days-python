from the_turtle import The_Turtle
from cars import Cars
from level import Level
import time
import random
import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title('The Turtle Crossing')
screen.tracer(0)

tim = The_Turtle()
lvl = Level()

cars = []
for n in range(30):
    car = Cars()
    cars.append(car)

screen.listen()
screen.onkeypress(fun=tim.up, key='Up')
screen.onkeypress(fun=tim.down, key='Down')

game_on = True
speed = 5
while game_on:
    time.sleep(0.05)
    screen.update()
    for d_car in cars:
        d_car.driving(speed)
        if d_car.xcor() < -320:
            d_car.goto(y=random.randint(-250, 250), x=320)
        if tim.distance(d_car) < 25 and d_car.ycor() + 18 > tim.ycor() > d_car.ycor() - 25:
            game_on = False
            lvl.game_over()
        if tim.ycor() > 270:
            tim.goto(0, -280)
            lvl.next_level()
            speed += 2.5

screen.exitonclick()
