from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def my_items():
    items = {}
    items["flavors"] = ['Blackberry', 'Chocolate', 'Cookies and Cream', 'Cotton Candy', 'Mango', 'Pistachio', 'Toffee', 'Strawberry', 'Vanilla']
    items["prices"] = [1.99, 1.99, 1.99, 1.99, 1.99, 1.99, 1.99, 1.99, 1.99]
    return jsonify(items)



if __name__ == '__main__':
    app.run(debug = True)