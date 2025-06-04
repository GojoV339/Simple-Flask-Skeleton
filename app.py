from flask import Flask
"""
It creates an instace of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application
"""

app = Flask(__name__) # entry point to run the application is passed as the parameter

@app.route("/")
def welcome():
    return "Welcome to the flask boot camp. This should be an amazing course"

@app.route("/index")
def index():
    return "Welcome to the index page"

if __name__=="__main__":
    app.run(debug=True) # with debug = True , everytime you make a change , you don't have to restart the server , you just have to save and reload the page