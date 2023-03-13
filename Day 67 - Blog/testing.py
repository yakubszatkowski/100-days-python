# import requests
#
# response = requests.get(url='https://api.npoint.io/81bab482e62ce81face5')
# posts = response.json()
#
# print(posts)
#
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"
# db.init_app(app)
#
#
# class BlogPost(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     subtitle = db.Column(db.String(250), nullable=False)
#     date = db.Column(db.String(250), nullable=False)
#     body = db.Column(db.Text, nullable=False)
#     author = db.Column(db.String(250), nullable=False)
#     img_url = db.Column(db.String(250), nullable=False)
#
#
# with app.app_context():
#     posts = db.session.query(BlogPost).all()
#
#
# def show_post(index):
#     requested_post = None
#     for blog_post in posts:
#         if blog_post["id"] == index:
#             requested_post = blog_post
#             print(requested_post)

import datetime
print(datetime.date.today().strftime("%d %B, %Y"))

