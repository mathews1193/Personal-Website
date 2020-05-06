from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
@app.route('/home')
def home():
    return render_template ('home.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/projects")
def project():
    return render_template('projects.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')



