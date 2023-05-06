from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_PASSWORD'] = 'qzuhswckzguinwiq'
app.config['MAIL_USERNAME'] = 'cs334teamproject@gmail.com'
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route("/")
def index():
    return render_template('Checkout.html')

@app.route("/result", methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        msg = Message(request.form.get("Subject"), sender='cs334teamproject@gmail.com', recipients=[request.form.get("Email")])
        msg.body = 'Thank you for your order!'
        mail.send(msg)
        return render_template('result.html', result='Success!')
    else:
        return render_template('result.html', result='Fail')

if __name__ == '__main__':
    app.run(debug=True)
