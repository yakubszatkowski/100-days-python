from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/main')
def main_page(language):
    if language == 'polish':
        return render_template('main.html')
    elif language == 'english':
        return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
