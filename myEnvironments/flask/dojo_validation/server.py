"""
Intro to Flask.
To give a full accounting
"""

from flask import Flask, render_template, request, redirect, session, flash
from livereload import Server

app = Flask(__name__)
app.debug = True
app.secret_key = 'ThisIsSecret'
server = Server(app.wsgi_app)


@app.route('/')
def index():
	"""Route function hello_world to root."""
	if 'name' not in session:
		session['name'] = ''
	return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
	"""Process Form Data"""
	flash_message = ''
	incorrect = False
	if len(request.form['full_name']) < 1:
		flash_message += 'Name cannot be an empty Field. '
		incorrect = True
	if len(request.form['comment']) < 1:
		flash_message += 'Come on man, you\'ve gott to type at least one letter in the comment field!'
		incorrect = True
	if len(request.form['comment']) > 120:
		flash_message += 'Your comment cannot be longer than 120 chars!'
		incorrect = True
	if incorrect:
		flash(flash_message)
		return redirect('/error')
	else:
		flash(request.form)
	return redirect('/results')


@app.route('/results')
def show_submission():
	"""Return the dojo form"""
	return render_template('results.html')


@app.route('/error')
def error():
	return render_template('error.html')


server.watch('./')
server.serve(port=5500, host='127.0.1.1')
