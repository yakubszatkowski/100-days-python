from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


# Creating a table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)


# CRUD - Create, Remove, Update, Delete
with app.app_context():
    db.create_all()
    # Create
    user = User(username='user6', email='user2@gmail.com')
    db.session.add(user)
    db.session.commit()

    # Read all records
    user_database = db.session.query(User).all()
    for user in user_database:
        print(user.username)

    # Read a specific record by username "user1"
    user = db.one_or_404(db.select(User).filter_by(username='user3'))
    print(user.id)

    # Read a specific record by id
    user = db.get_or_404(User, 1)
    print(user.username)

    # Update a Particular record by Query
    user_to_update = db.one_or_404(db.select(User).filter_by(username='user6'))
    user_to_update.username = 'amazing user'
    db.session.commit()
    print(user_to_update.username)

    # Update a record by primary key
    record_id = 4
    record_to_update = db.session.get(User, record_id)
    record_to_update.username = 'Harry'
    db.session.commit()
    print(record_to_update.username)

    # Delete a record by primary key
    record_id = 4
    record_to_delete = db.session.get(User, record_id)
    db.session.delete(record_to_delete)
    db.session.commit()
