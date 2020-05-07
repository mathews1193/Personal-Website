from flask import Flask , render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Donald Mathews',
        'title': 'Project 1 ', 
        'content': 'First post content',
        'date_posted': 'May 6, 2020'
    },
    {
        'author': 'Donald Mathews',
        'title': 'Project 2 ', 
        'content': 'Second post content',
        'date_posted': 'May 6, 2020'
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



