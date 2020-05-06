from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route('/home')
def home():
    return "<h1> Home Page <h1>"

@app.route("/about")
def about():
    return "<h1> About <h1>"


@app.route("/projects")
def project():
    return "<h1> Projects <h1>"


@app.route("/contact")
def contact():
    return "<h1> Contact Information <h1>"




