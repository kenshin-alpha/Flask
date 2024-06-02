from flask import Flask

app = Flask(__name__)

# this means the name of our application is App1
# our application object is app

@app.route("/")
def Index():
    return "<h1>Hurray!! this is my first flask APP!! <h1/>"


@app.route("/aboutus")
def about():
    return "We are World's Best Intership company! WileyEdge.com"

@app.route("/cohorts")
def projects():
    return "Here we provide training on Various technologies that helps for Production Management Analyst and Software Development"


# routes with parameters

@app.route("/order/<food>")
def placeOrder(food):
    return "You have Placed Order for " + food 


#Data type specific parameters

@app.route("/power/<int:strength>")
def pokemon(strength):
    return "Bulbasur Strength is %d " % strength
    
app.run(debug=True)



# @app.route("/")
# here / means when the website is accessed at 
# http://localhost using this url then 
# automatically Index() will be called.
