from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class TechnicalSkill(db.Model):
    __tablename__ = 'technical_skills'
    technology = db.Column(db.String(200))


class Subtechnology(db.Model):
    _tablename__ = 'subtechnologies'
    technology = db.Column(db.String(200), db.ForeignKey('TechnicalSkill.technology'))
    subtechnology = db.Column(db.String(200))

if __name__ == '__main__':
    app.run(debug=True)