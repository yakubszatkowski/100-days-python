from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def say_bye():
    return 'Bye!'


# set FLASK_APP=hello.py
# go to the destination folder
# flask run

# print(random.__name__)
# print(__name__)

# same as flask run
if __name__ == '__main__':
    app.run()
