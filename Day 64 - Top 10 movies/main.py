from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-10-movies.db"
Bootstrap5(app)
db.init_app(app)
api_key = os.environ.get('d64_api_key')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    movies = db.session.query(Movie).all()


class RateMovieForm(FlaskForm):
    rating = StringField("New score", validators=[DataRequired()])
    review = StringField("New review", validators=[DataRequired()])
    submit = SubmitField('Submit')


class NewMovieForm(FlaskForm):
    title = StringField("Movie title", validators=[DataRequired()])
    submit = SubmitField('Add movie')


@app.route("/")
def home():
    return render_template("index.html", movies=movies)


@app.route('/edit', methods=['GET', "POST"])
def edit():
    movie_id = request.args.get('id')
    edit_form = RateMovieForm()
    if edit_form.validate_on_submit():
        movie_to_update = db.session.get(Movie, movie_id)
        movie_to_update.rating = edit_form.rating.data
        movie_to_update.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=edit_form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.session.get(Movie, movie_id)
    print(f'{movie_to_delete} would be deleted if not commented lines :)')
    # db.session.delete(movie_to_delete)
    # db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['GET', "POST"])
def add():
    add_form = NewMovieForm()
    if add_form.validate_on_submit():
        new_movie_title = add_form.title.data
        parameters = {
            'api_key': api_key,
            'query': new_movie_title,
        }
        response = requests.get(f'https://api.themoviedb.org/3/search/movie', params=parameters)
        data = response.json()
        return redirect(url_for('select'))

    return render_template('add.html', form=add_form)


@app.route('/select', methods=['GET', "POST"])
def select():
    return render_template('select.html')


if __name__ == '__main__':
    app.run(debug=True)
