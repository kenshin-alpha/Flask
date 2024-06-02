
# this lab demonstrates transferring data from python to html file

from flask import * 

app = Flask(__name__)

@app.route("/")
def index():
    secret = "Santa Claus is Thanos"
    return render_template("index1.html",msg=secret)


@app.route("/tbl/<int:digit>")
def generate(digit):
    return render_template('tblshow.html',num=digit)


@app.route("/showlist")
def sending():
    ice_cream=['vanilla','choclate','rum-rasin']
    return render_template('index2.html',items = ice_cream)


@app.route("/showdict")
def sending2():
    states = {
        'TX' : 'Texas',
        'AL' : 'Alabama',
        'CA' : 'California'
    }
    return render_template('index3.html',us_states = states)

@app.route("/report")
def sending3():
    empdetails = [
        {'productid' : 101,'name' : 'Acer Laptop','Description' : 'Entertainment Laptop'},
        {'productid' : 102,'name' : 'Dell Laptop','Description' : 'Office Laptop'},
        {'productid' : 103,'name' : 'Alienware Laptop','Description' :  'Multipurpose Laptop'}
    ]
    return render_template('index4.html',employees = empdetails)
app.run(debug=True)
