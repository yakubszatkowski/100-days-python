from flask import Flask, render_template, request
from request import RequestCafePlaces
import os
import ast
import pprint

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
            print('\n', name, '\n', geolocation, '\n')
            data = request_cafe.send_request(geolocation)
            return render_template('index.html', API_KEY=API_KEY, data=data['results'])
    else:  
        return render_template('index.html', API_KEY=API_KEY)


if __name__ == '__main__':
    app.run(debug=True)

