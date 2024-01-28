from flask import Flask, render_template
import os

app = Flask(__name__)
API_KEY = os.environ.get("Google_API_KEY")


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', API_KEY=API_KEY)

if __name__ == '__main__':
    app.run(debug=True)
