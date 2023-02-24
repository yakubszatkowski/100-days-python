from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice

app = Flask(__name__)

# # Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# # Café TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=['GET'])  # GET is allowed by default on all routes actually
def get_random_cafe():
    cafe = db.session.query(Cafe).all()
    random_cafe = choice(cafe)
    return jsonify(
        cafe={
            'id': random_cafe.id,
            'name': random_cafe.name,
            'map_url': random_cafe.map_url,
            'img_url': random_cafe.img_url,
            'location': random_cafe.location,
            'has_sockets': random_cafe.has_sockets,
            'has_toilet': random_cafe.has_sockets,
            'has_wifi': random_cafe.has_wifi,
            'can_take_calls': random_cafe.can_take_calls,
            'seats': random_cafe.seats,
            'coffee_price': random_cafe.coffee_price
        }
    )


# # HTTP GET - Read Record

# # HTTP POST - Create Record

# # HTTP PUT/PATCH - Update Record

# # HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
