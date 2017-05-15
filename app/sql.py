from flask import Flask
from views import app
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
randomChar = os.urandom(24)
app.config['SECRET_KEY'] = randomChar
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db/users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True)
    user_email = db.Column(db.String(120), unique=True)
    user_key = db.Column(db.String(120))

    def __init__(self, user_name, user_email, user_key):
        self.user_name = user_name
        self.user_email = user_email
        self.user_key = user_key

    def __repr__(self):
        return '%r, %r, %r' % (self.user_name, self.user_email, self.user_key)
