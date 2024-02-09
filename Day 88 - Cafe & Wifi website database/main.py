from flask import Flask, render_template, request
from request import RequestCafePlaces
import os
import ast

app = Flask(__name__)
API_KEY = os.environ.get("Google_API_KEY")
request_cafe = RequestCafePlaces()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        args = request.form
        name, geolocation = args['search_input'], args['geometry']
        if name and geolocation:
            geolocation = ast.literal_eval(geolocation)
            print(name, geolocation, '\n')

            # data = request_cafe.nearby_search(geolocation)  # this one expensive
            # for business in data['results']:
            #     print(business['place_id'])


    return render_template('index.html', API_KEY=API_KEY)


if __name__ == '__main__':
    app.run(debug=True)


#TODO
    # this may be the one to inspect response? https://requests-cache.readthedocs.io/en/stable/user_guide/inspection.html
    # read requests-cache library https://requests-cache.readthedocs.io/en/stable/index.html

    # Do something about scroll bar on the right
    # CSS div card for place details
    # Card should contain: name of business, rating, address, opening hours, contant number, photo (maybe photo carousel?)
