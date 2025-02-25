from flask import Flask,render_template,url_for
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '80aa0cb771d3eb8b44794fdc822eebe6'
posts = [
    {
        'author': 'Sripada Pradhan',
        'title': 'Blog Post 1',
        'content': 'first flask tut',
        'date_posted':'April 20,2018'
    },
    {
        'author': 'Prabhupad Pradhan',
        'title': 'Blog Post 2',
        'content': 'first flask tut2',
        'date_posted': 'April 28,2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)
@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register',form=form)

@app.route("/Login")
def login():
    form = LoginForm()
    return render_template('login.html',title='Login',form=form)
if __name__ == '__main__':
    app.run(debug=True)