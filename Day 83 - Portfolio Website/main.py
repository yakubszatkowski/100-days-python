from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)


@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/main/<language>')
def main_page(language):
    if language == 'polish':
        return render_template('main.html')
    if language == 'english':
        return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
