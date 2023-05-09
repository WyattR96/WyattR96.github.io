from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory, session
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import timedelta

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_PASSWORD'] = 'cgbpzdflvhpukjbe'  # qzuhswckzguinwiq'
app.config['MAIL_USERNAME'] = 'yourfavoriteicecreamshop@gmail.com'
# app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


db = SQLAlchemy(app)
app.secret_key = "mySecret"


class Flavors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(50))
    name = db.Column(db.String(50))


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(64))


class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(64))


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.PickleType())


@app.route("/", methods=['GET','POST'])
def main():
    fla = Flavors.query.all()
    return render_template('Main-Page.html', flavors=fla)


@app.route("/Main-Page.html", methods=['GET','POST'])
def mainPage():
    fla = Flavors.query.all()

    if request.method == 'POST':
        item = request.form['select']
        flavor = Flavors.query.filter(Flavors.name == item).first().name
        return render_template('form.html',items=flavor)

    return render_template('Main-Page.html', flavors=fla)


@app.route("/Login.html", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if 'User' in request.form and 'Pass' in request.form:
            Name = request.form['User']
            password = request.form['Pass']
            customer = db.session.query(Customers.id).filter_by(name=Name).first()
            if customer is not None:
                print(customer.password)
                fla = Flavors.query.all()
                return render_template('Main-Page.html', flavors=fla)

    return render_template('Login.html')


@app.route("/form.html", methods=['GET', 'POST'])
def checkout(items):
    return render_template('form.html')


@app.route("/Item-Management.html", methods=['GET', 'POST'])
def itemManagement():
    fla = Flavors.query.all()

    if request.method == 'POST':
        if 'title' in request.form and 'URL' in request.form:
            Name = request.form['title']
            Url = request.form['URL']
            newFlavor = Flavors(name=Name, url=Url)
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


@app.route("/SubmitForm", methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        name = request.form.get("Name")
        msg = Message('Your Favorite Ice Cream Shop Order Confirmation', sender='yourfavoriteicecreamshop@gmail.com',
                      recipients=[request.form.get("Email")])
        msg.body = 'Thank you for your order ' + name + '!'
        mail.send(msg)
        return render_template('SubmitForm.html', result='Success!')
    else:
        return render_template('SubmitForm.html', result='Fail')


@app.route("/manifest.json")
def manifest():
    return send_from_directory('static', 'manifest.json')


@app.route("/js/app.js")
def app_js():
    return send_from_directory('static', 'js/app.js')


@app.route("/serviceWorker.js")
def serviceWorker():
    return send_from_directory('static', 'js/serviceWorker.js')


# added to prevent server error
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
