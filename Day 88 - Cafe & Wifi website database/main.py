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
        if args:
            name, geolocation = args['search_input'], args['geometry']
            geolocation = ast.literal_eval(geolocation)

            print(name, geolocation, '\n')

            # data = request_cafe.nearby_search(geolocation)  # this one expensive
            # for business in data['results']:
            #     print(business['place_id'])


    return render_template('index.html', API_KEY=API_KEY)


if __name__ == '__main__':
    app.run(debug=True)

#TODO
    # Read about terms of service here https://developers.google.com/terms
    # Read about billing here https://developers.google.com/maps/documentation/places/web-service/usage-and-billing
    # Get Place Details search here https://developers.google.com/maps/documentation/places/web-service/details

    # Research about nearby search to reduce cost
    # Research about place details search to reduce cost

    # Cache/Save city name into database with revelant place_ids - if someone search for this city - check if it's in database first
# rather than using API, delete the row if it's older than 25 days - same about place details!
    # Cache/Save place details too
    # Limit searches to 10 every hour for IP address

    # Do something about scroll bar on the right
    # CSS div card for place details
    # Card should contain: name of business, rating, address, opening hours, contant number, photo (maybe photo carousel?)
    
