from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os

from sqlalchemy import ForeignKey

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

db = SQLAlchemy(app)
app.secret_key="mySecret"

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
    items = db.Column(db.PickleType())


@app.route("/")
def main():
    fla = Flavors.query.all()
    return render_template('Main-Page.html', flavors=fla)


@app.route("/Main-Page.html")
def mainPage():
    fla = Flavors.query.all()
    return render_template('Main-Page.html', flavors=fla)


@app.route("/Login.html")
def login():
    return render_template('Login.html')


@app.route("/Checkout.html")
def checkout():
    return render_template('Checkout.html')


@app.route("/Item-Management.html", methods=['GET', 'POST'])
def itemManagement():
    fla = Flavors.query.all()

    if request.method == 'POST':
        if 'title' in request.form and 'URL' in request.form:
            Name = request.form['title']
            Url = request.form['URL']
            newFlavor = Flavors(name=Name,url=Url)
            db.session.add(newFlavor)
            db.session.commit()

        if 'deleteID' in request.form:
            Id = request.form['deleteID']
            delete = Flavors.query.filter_by(id=Id).first()
            db.session.delete(delete)
            db.session.commit()

        if 'updateId' in request.form:
            print("asdf")
            Id = request.form['updateId']
            newName = request.form['updateName']
            newUrl = request.form['updateUrl']
            flavor = Flavors.query.filter_by(id=Id).first()
            flavor.name = newName
            flavor.url = newUrl
            db.session.commit()

    return render_template('Item-Management.html', flavors=fla)



@app.route("/SubmitForm.html")
def submit():
    return render_template('SubmitForm.html')


@app.route("/manifest.json")
def manifest():
    return send_from_directory('static', 'manifest.json')


@app.route("/js/app.js")
def app_js():
    return send_from_directory('static', 'js/app.js')


@app.route("/serviceWorker.js")
def serviceWorker():
    return send_from_directory('static', 'js/serviceWorker.js')


if __name__ == '__main__':
    app.run(debug=True)
