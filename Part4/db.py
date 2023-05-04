from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class items(db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    flavor = db.Column("flavor", db.String(100))
    price = db.Column("price", db.String(100))

    def __init__(self, flavor, price):
        self.flavor = flavor
        self.price = price

class users(db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    user_name = db.Column("user_name", db.String(100))
    password= db.Column("password", db.String(100))

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

class orders(db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column("name", db.String(100))
    total = db.Column("total", db.Integer)
    email = db.Column("email", db.String(100))

    def __init__(self, name, total, email):
        self.name = name
        self.total = total
        self.email = email



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)