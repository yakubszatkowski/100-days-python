from screen import middle_split
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import turtle

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('The Pong game')
screen.tracer(0)

middle_split()
ball = Ball()
l_paddle = Paddle(first_player=True)
r_paddle = Paddle(first_player=False)
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=r_paddle.up, key='Up')
screen.onkeypress(fun=r_paddle.down, key='Down')
screen.onkeypress(fun=l_paddle.up, key='w')
screen.onkeypress(fun=l_paddle.down, key='s')

round_on = True
while round_on:
    time.sleep(0.1)
    screen.update()
    ball.serve()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_collision()
    if ball.distance(r_paddle) <= 50 and ball.xcor() > 320 or ball.distance(l_paddle) <= 50 and ball.xcor() < -320:
        ball.paddle_collision()
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.left_point()
    elif ball.xcor() < -400:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
