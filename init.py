from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return 'This is the project page'


@app.route('/blog')
def blog():
    return 'This will be the blog page'

if __name__ == "__main__":
    app.run(debug=True)