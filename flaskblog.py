from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b79bf25643fd10ff819f36875969a09e'

posts =[
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date': 'April 21, 2018'
    },
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts) #passing the dummy variable (latter) to a variable named posts(former)


@app.route("/about")
def about():
    return render_template('about.html', title ='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':      #__main_- only on python, else == file name
    app.run(debug=True)