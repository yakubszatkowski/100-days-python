from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# Notice that the methods parameter accepts a dictionary, so you can have multiple methods targeted by one route. e.g.
# @app.route("/contact", methods=["GET", "POST"]
@app.route('/login', methods=['POST'])
def handle_data():
    username = request.form['username']
    password = request.form['password']
    return f'<h1> Name: {username}, Password: {password}'


if __name__ == '__main__':
    app.run(debug=True)

# Knowledge from this project was used in previous day to update contact tab so it is possible for someone
# to send an e-mail to me
