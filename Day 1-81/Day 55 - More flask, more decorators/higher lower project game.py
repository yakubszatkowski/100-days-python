# at first, I tried to do the project with decorators and really easy function that returns number,
# but then I saw Angela's solution which saved some unnecessary lines of code which are commented
from flask import Flask
from random import randint

app = Flask(__name__)
random_number = randint(0, 9)


@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


# def high_low_equal(function):
@app.route(f'/<int:num>')
def wrapper(num):
    if num > random_number:
        return '<h1 style="color:purple">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif num < random_number:
        return '<h1 style="color:red">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1 style="color:green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

    # return wrapper


# @app.route(f'/<int:num>')
# @high_low_equal
# def check(num):
#     return num


if __name__ == '__main__':
    app.run(debug=True)
print(random_number)
