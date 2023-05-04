from flask import Flask, render_template, url_for, send_from_directory
import flask_sqlalchemy

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('Main-Page.html')

@app.route("/Main-Page.html")
def mainPage():
    return render_template('Main-Page.html')

@app.route("/Login.html")
def login():
    return render_template('Login.html')

@app.route("/Checkout.html")
def checkout():
    return render_template('Checkout.html')

@app.route("/Item-Management.html")
def itemManagement():
    return render_template('Item-Management.html')

@app.route("/SubmitForm.html")
def submit():
    return render_template('SubmitForm.html')
@app.route("/manifest.json")
def manifest():
    return send_from_directory('static','manifest.json')

@app.route("/js/app.js")
def app_js():
    return send_from_directory('static','js/app.js')

@app.route("/serviceWorker.js")
def serviceWorker():
    return send_from_directory('static','js/serviceWorker.js')


if __name__ == '__main__':
    app.run(debug=True)
