from flask import Flask , render_template, url_for
app = Flask(__name__)

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



