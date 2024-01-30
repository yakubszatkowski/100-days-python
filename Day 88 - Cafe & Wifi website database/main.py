from flask import Flask, render_template, request
import os

app = Flask(__name__)
API_KEY = os.environ.get("Google_API_KEY")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        args = request.form
        if args:
            print(args['search_input'])
            print(args['geometry'])
    return render_template('index.html', API_KEY=API_KEY)


if __name__ == '__main__':
    app.run(debug=True)
