from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template('index.html',
                           books=db.session.query(Books).all())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == 'POST':
        with app.app_context():
            db.session.add(Books(title=request.form.get('book_name'),
                                 author=request.form.get('book_author'),
                                 rating=request.form.get('rating')))
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit", methods=["GET", "POST"])
def edit():
    book_id = request.args.get('id')
    book = db.get_or_404(Books, book_id)
    if request.method == 'POST':
        new_score = request.form['new_score']
        book.rating = new_score
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',
                           book_id=book_id,
                           book_title=book.title,
                           book_author=book.author,
                           book_score=book.rating)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.session.get(Books, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
