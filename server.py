from flask import Flask, render_template, redirect, request
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'maneroto'


@app.route('/')
def home():
    return "Hello World! xD"

@app.route('/about')
def about():
    return 'The about page'

@app.route('/blog')
def blog():
    posts = [{'title': 'Technology in 2019', 'author': 'Mane'}, {'title': 'Expansion of oil in Russia', 'author': 'Me'}]
    return render_template('blog.html', author='Mane', sunny = True, posts = posts)

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return 'This is blog post number ' + blog_id

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        return render_template('user.html', result = result)
    return render_template('signup.html', form = form)
if __name__ == '__main__':
    app.run()