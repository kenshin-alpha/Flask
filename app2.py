from flask import Flask

app = Flask(__name__)

def testFunction():
    return "this is alternate to routing demo"


## this is alternate method to assign route to the function
# using add_url_rule
# syntax : add_url_rule()

app.add_url_rule("/test" ,"sampleRoute",testFunction)

app.run(debug=True)