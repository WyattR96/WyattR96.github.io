from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

from sqlalchemy import ForeignKey

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

db = SQLAlchemy(app)

class Flavors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(50))
    name = db.Column(db.String(50))

class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.relationship(db.Integer, ForeignKey('Customers.id'))
    items = db.Column(db.PickleType())

def init_db():
    with app.app_context():
        db.create_all()
        db.session.commit()

if __name__ == '__main__':
    init_db()