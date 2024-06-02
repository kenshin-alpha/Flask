#Handlong Routes using URL building

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/veg")
def vegMenu():
    return "this is Vegetarians Menu"

@app.route("/nonveg")
def nonVegMenu():
    return "NonVeg Menu is here.."

@app.route("/dosa")
def dosa():
    return "Dosa is Here"

@app.route("/read")
def readMe():
    string = ''
    data = open("/Users/uthejkarnam/Documents/file.txt").readlines()
    for i in data:
        string += i + "\n"
    return string

@app.route("/zomato/<order>")
def book(order):
    if order == 'cheese':
        return redirect(url_for('vegMenu'))

    elif order == 'chicken':
        return redirect(url_for('nonVegMenu'))

    elif order == 'dosa':
        return redirect(url_for("dosa"))


app.run(debug=True)

