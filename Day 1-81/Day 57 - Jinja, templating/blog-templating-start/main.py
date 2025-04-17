from flask import Flask, render_template
from post import Post

app = Flask(__name__)
all_posts = Post().response_blog

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:id>')
def get_post(id):
    id -= 1
    post = all_posts[id]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
