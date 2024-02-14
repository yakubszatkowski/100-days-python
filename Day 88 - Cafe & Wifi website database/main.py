from flask import Flask, render_template, request
from request import RequestCafePlaces
import os
import ast

app = Flask(__name__)
API_KEY = os.environ.get("Google_API_KEY")
request_cafe = RequestCafePlaces()

@app.route('/', methods=['GET', 'POST'])
def index():
    list_of_cafes, name = None, None
    if request.method == 'POST':
        args = request.form
        name, geolocation = args['search_input'], args['geometry']
        if name and geolocation:
            geolocation = ast.literal_eval(geolocation)
            print(name, geolocation)
            list_of_cafes = request_cafe.query_results(geolocation)
            print(list_of_cafes)

    return render_template('index.html', API_KEY=API_KEY, cafes=list_of_cafes, location=name)

if __name__ == '__main__':
    app.run(debug=True)
    


#TODO
    # CSS div card for place details
    # Card should contain:
    # Card elements: Name, rating, user_ratings_total, address, opening_hours, phone_number website

    # Check out Flask-Limiter - it may help with limiting post requests to 10 per hour

