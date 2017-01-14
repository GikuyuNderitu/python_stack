"""
Intro to Flask.
To give a full accounting
"""
import re
from flask import Flask, render_template, request, redirect, session, flash
from livereload import Server

app = Flask(__name__)
app.debug = True
app.secret_key = 'ThisIsSecret'
server = Server(app.wsgi_app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def oneAndone(password):
	hasUpper = True
	for val in range(len(password)):
		if password[val].isupper():
			continue
		else:
			hasUpper = True
			break
	return hasUpper and password.isalpha()


@app.route('/', methods=['GET'])
def index():
	# session.clear()
	return render_template("index.html")


@app.route('/process', methods=['POST'])
def submit():
	session['data'] = ' '
	form = request.form
	flashData = False
	print form
	session['fname'] = form['first_name']
	session['lname'] = form['last_name']
	session['email'] = form['email']
	if len(form['email']) < 1:
		flashData = True
		flash('Email field must not be blank!')
	elif not EMAIL_REGEX.match(form['email']):
		flashData = True
		session['email'] = ' '
		flash('Invalid Email Address!')
	if not form['first_name'] or len(form['first_name']) < 1:
		flashData = True
		flash('First name field must be spelled out')
	elif not form['first_name'].isalpha():
		session['fname'] = ' '
		flashData = True
		flash('First name field must be spelled out')
	if not form['last_name'] or len(form['last_name']) < 1:
		flashData = True
		flash('Last name field must be spelled out')
		print 'ERROR'
	elif not form['last_name'].isalpha():
		session['lname'] = ' '
		flashData = True
		flash('First name field must be spelled out')
	if not form['password'] or len(form['password']) < 9:
		flashData = True
		flash('Password must be greater than 8 characters!')
	elif oneAndone(form['password']):
		flashData = True
		flash('Password must have one uppercase letter and one number')
	elif form['password'] != form['confirm_password']:
		flashData = True
		flash('The Passwords gotta match sUCKA!')

	if flashData:
		return redirect('/')

	return redirect('/success')


@app.route('/success')
def success():
	return render_template('success.html')


@app.route('/reset')
def reset():
	return redirect('/')


server.watch('./')
server.serve(port=5500, host='127.0.1.1')
