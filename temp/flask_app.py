from flask import Flask, render_template, url_for

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


if __name__ == '__main__':
    app.run(debug=True)
