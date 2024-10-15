from flask import Flask, render_template, url_for
app = Flask(__name__)

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


def hello():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return render_template('about.html', title ='About')



if __name__ == '__main__':      #__main_- only on python, else == file name
    app.run(debug=True)