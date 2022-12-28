from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function


def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>this is cat</p>' \
           '<img src="https://media.giphy.com/media/K1tgb1IUeBOgw/giphy.gif" width=200px> '


# Different routes using the app.route decorator
@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return 'Bye!'


# # Path variable
# @app.route('/username/<path:name>')
# def greet(name):
#     return f"Hello {name + ' !'}!!"

# Creating variable paths and converting the path to a specified data type
@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}! You are {number} years old!"


if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
