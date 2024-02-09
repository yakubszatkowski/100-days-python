from flask import Flask, render_template, request
from request import RequestCafePlaces
import os
import ast

app = Flask(__name__)
API_KEY = os.environ.get("Google_API_KEY")
request_cafe = RequestCafePlaces()

@app.route('/', methods=['GET', 'POST'])
def index():
    list_of_cafes = None
    if request.method == 'POST':
        args = request.form
        name, geolocation = args['search_input'], args['geometry']
        if name and geolocation:
            geolocation = ast.literal_eval(geolocation)
            print(name, geolocation)
            list_of_cafes = request_cafe.query_results(geolocation)

    return render_template('index.html', API_KEY=API_KEY, cafes=list_of_cafes)

if __name__ == '__main__':
    app.run(debug=True)


#TODO
    # Do something about scroll bar on the right
    # CSS div card for place details
    # Card should contain:
    # From nearby_places: 'place_id', 'name', 'rating', 'user_ratings_total', 'vicinity'
    # From place_detail: 'weekday_text', 'formatted_phone_number', 'website'
