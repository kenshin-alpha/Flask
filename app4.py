## this lab explains how to render html pages and take input from html pages.

from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register")
def reg():
    return render_template('signup.html')


@app.route("/authenticate")
def login():
    return render_template('login.html')

@app.route("/verify",methods = ['POST'])
def authorisation():
    data = open("/Users/uthejkarnam/Documents/Flask/data.txt").readlines()
    UN = request.form['user']
    PSS = request.form['pass']
    data = data[:-1]
    for i in data:
        print(data)
        details = i.split(",")
        details[1] = details[1].rstrip("\n")
        username = details[0]
        password = details[1]
        print(details)
        if(username == UN and password == PSS):
            return render_template("welcome.html")
    return render_template("error.html")

@app.route("/save",methods = ['POST'])
def saveit():
    UN = request.form['usertxt']
    PSS = request.form['passtxt']
    data = open("data.txt",'a')
    data.write(UN + "," + PSS + "\n" )

    return f'''
    you Entered 
    Username : {UN}
    Password : {PSS}
    '''

app.run(debug=True)

