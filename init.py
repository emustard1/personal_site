from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/about-me')
def about_me():
    return 'About page'


@app.route('/contact')
def contact():
    return 'THis is the contact page'

@app.route('/projects')
def projects():
    return 'This is the project page'

if __name__ == "__main__":
    app.run(debug=True)