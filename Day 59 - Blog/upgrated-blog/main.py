from flask import Flask, render_template
import requests

response = requests.get(url='https://api.npoint.io/81bab482e62ce81face5')
posts = response.json()

app = Flask(__name__)


@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html', posts=posts)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route(f'/<int:post_id>.html')
def post(post_id):
    post_id -= 1
    return render_template('post.html', post=posts[post_id])


if __name__ == '__main__':
    app.run(debug=True)
