# A very simple Flask Hello World app for you to get started with...
#from flask import Flask
#import urllib.request
import os
from app import app
from flask import Flask, flash, request, redirect, render_template, jsonify
#from flask import Flask, render_template, request, jsonify

from werkzeug.utils import secure_filename
#app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'exe', 'php', 'py', 'zip', 'mp4', 'html',])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#@app.route('/')
#def hello_world():
#    return render_template('welcome.html')  # render a template
##    return 'Hello from Flask!'

@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			flash('File successfully uploaded')
			return redirect('/')
		else:
			flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
			return redirect(request.url)

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

@app.route('/upload')
def pageuploadfile():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def uploadfile():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

if __name__ == '__main__':
#   app.run(debug = True)
   app.run()
