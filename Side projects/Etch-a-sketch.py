from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def w():
    tim.forward(10)


def s():
    tim.backward(10)


def a():
    tim.left(15)


def d():
    tim.right(15)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkeypress(key='Up', fun=w)      # no need for key and fun
screen.onkeypress(key='Down', fun=s)
screen.onkeypress(key='Left', fun=a)
screen.onkeypress(key='Right', fun=d)
screen.onkeypress(key='C', fun=clear)

screen.exitonclick()
