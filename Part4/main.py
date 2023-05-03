from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("Main-Page.html")

@app.route("/Main-Page.html")
def home1():
  return render_template("Main-Page.html")

@app.route("/Checkout.html")
def checkout():
  return render_template("Checkout.html")


#API for flavors/prices?
#@app.route("/")
#def my_items():
#    items = {}
#    items["flavors"] = ['Blackberry', 'Chocolate', 'Cookies and Cream', 'Cotton Candy', 'Mango', 'Pistachio', 'Toffee', 'Strawberry', 'Vanilla']
#    items["prices"] = [1.99, 1.99, 1.99, 1.99, 1.99, 1.99, 1.99, 1.99, 1.99]
#   return jsonify(items)



if __name__ == '__main__':
    app.run(debug = True)
