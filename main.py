from flask import Flask,render_template
"""
It creates an instace of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application
"""
"""
since we are using render_template , all the html pages should be templates folder , because the render_template
#by default checks in the templates folder
"""
app = Flask(__name__) # entry point to run the application is passed as the parameter

@app.route("/")
def welcome():
    return "<html><h3>Welcome to the course</h3></html>"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True) 