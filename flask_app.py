# A very simple Flask Hello World app for you to get started with...
#from flask import Flask
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('welcome.html')  # render a template
#    return 'Hello from Flask!'

@app.route('/welcome')
def welcome():
#    return 'Welcome!'
    return render_template('welcome.html')  # render a template

@app.route('/webcam')
def webcam():
    return render_template('webcam.html')  # render a template

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        return jsonify(request.form['userID'], request.form['file'])
    return render_template('signup.html')

@app.route('/hello')
def hello():
    return "Hello, World!"  # return a string

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Sorry. Please try again.'
        else:
            error = 'Good. Welcome admin.'
    return render_template('login.html', error=error)
