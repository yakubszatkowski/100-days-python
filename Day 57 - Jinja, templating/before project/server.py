from flask import Flask, render_template
from datetime import datetime
import requests
import random

app = Flask(__name__)


@app.route('/')
def home():
    current_year = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, year=current_year)


@app.route('/guess/<name>')
def name_predictions(name):
    response_age = requests.get(url=f'https://api.agify.io?name={name}')
    response_gender = requests.get(url=f'https://api.genderize.io?name={name}')
    name = name.title()
    age = response_age.json()['age']
    gender = response_gender.json()['gender']
    return render_template('name_prediction.html', name=name, age=age, gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    response_blog = requests.get(url='https://api.npoint.io/2a276e24e4756cd30605').json()
    return render_template('blog.html', posts=response_blog)


if __name__ == "__main__":
    app.run(debug=True)
