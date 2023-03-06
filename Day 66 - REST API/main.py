from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice
from distutils.util import strtobool

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

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=['GET'])  # GET is allowed by default on all routes actually
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = choice(cafes)
    # print(type(random_cafe))
    return jsonify(cafe=random_cafe.to_dict())


# # HTTP GET - All the cafés
@app.route('/all')  # GET is allowed by default on all routes actually
def all_cafes():
    cafes = db.session.query(Cafe).all()
    # print(type(cafes))
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])
    # # ALTERNATIVE
    # all_cafes_json = {}
    # for cafe in cafes:
    #     all_cafes_json[cafe.id] = cafe.to_dict()
    # return all_cafes_json


# # HTTP Get - Find a Cafe
@app.route('/search')
def search():
    loc = request.args.get('loc').title()
    cafes = db.session.query(Cafe).filter_by(location=loc).all()  # returns the list of all cafés of requested location
    if len(cafes) == 0:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location"})
    else:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


# def make_bool(val: int) -> bool:  # may be helpful in future
#     return bool(int(val))


# # HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():
    new_cafe = Cafe(  # 'args' is for GET requests, 'form' for POST requests
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('location'),
        seats=request.form.get('seats'),
        has_sockets=bool(strtobool(request.form.get("sockets"))),
        has_toilet=bool(strtobool(request.form.get("toilet"))),
        has_wifi=bool(strtobool(request.form.get("wifi"))),
        can_take_calls=bool(strtobool(request.form.get("calls"))),
        coffee_price=request.form.get('price'),
    )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# # HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=['POST'])
def patch(cafe_id):
    # updpate price of choosen cafe's coffee
    return cafe_id


# # HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
