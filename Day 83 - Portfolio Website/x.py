from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, fields, marshal, abort
from sqlalchemy_utils import generic_relationship


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class AboutMe(db.Model):
    __tablename__ = 'aboutme'
    id = db.Column(db.Integer, primary_key=True)


class Technology(db.Model):
    __tablename__ = 'technologies'
    id = db.Column(db.Integer, primary_key=True)
    subtechnologies = db.relationship('SubTechnology', backref='technology')
    technology_name = db.Column(db.String(50), nullable=False)


class SubTechnology(db.Model):
    __tablename__ = 'subtechnologies'
    id = db.Column(db.Integer, primary_key=True)
    technology_name = db.Column(db.String, db.ForeignKey(Technology.technology_name))
    subtechnology_name = db.Column(db.String(50), nullable=False)


class Description(db.Model):
    __tablename__ = 'descriptions'
    id = db.Column(db.Integer, primary_key=True)
    object_type = db.Column(db.String)
    object_id = db.Column(db.Integer)
    language = db.Column(db.String)
    text = db.Column(db.String)
    object = generic_relationship(object_type, object_id)