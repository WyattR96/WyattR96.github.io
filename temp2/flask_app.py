from flask import Flask, render_template, url_for, send_from_directory, request
from flask_mail import Mail, Message

import flask_sqlalchemy

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_PASSWORD'] = 'qzuhswckzguinwiq'
app.config['MAIL_USERNAME'] = 'cs334teamproject@gmail.com'
app.config['MAIL_USE_SSL'] = True


mail = Mail(app)



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
    return render_template('form.html')

@app.route("/Item-Management.html")
def itemManagement():
    return render_template('Item-Management.html')





@app.route("/SubmitForm", methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        name = request.form.get("Name")
        msg = Message('Your Favorite Ice Cream Shop Order Confirmation', sender='cs334teamproject@gmail.com', recipients=[request.form.get("Email")])
        msg.body = 'Thank you for your order ' + name + '!'
        mail.send(msg)
        return render_template('SubmitForm.html', result='Success!')
    else:
        return render_template('SubmitForm.html', result='Fail')






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
    
