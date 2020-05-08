# Main application of the flask website including all the routes to each page 

from flask import Flask , render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

# Secret key for application 

app.config['SECRET_KEY'] = 'c62058f0d97fd33f4c54' 

posts = [
    {
        'author': 'Donald Mathews',
        'title': 'Sous Chef ', 
        'content': 'First application using Java to organzie meals.',
        'date_posted': 'May 6, 2020'
    },
    {
        'author': 'Donald Mathews',
        'title': 'Track Master ', 
        'content': 'Second application using Python to face detect using artifical intelligence.',
        'date_posted': 'May 7, 2020'
    }

]

# home page 
@app.route("/") 
@app.route('/home')
def home():
    return render_template ('home.html')

# about page 
@app.route("/about")
def about():
    return render_template('about.html')

# project page 
@app.route("/projects")
def project():
    return render_template('projects.html', posts=posts)

# contact page 
@app.route("/contact")
def contact():
    return render_template('contact.html')



