from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
from livereload import Server
import re

app = Flask(__name__)
app.debug = True
app.secret_key = 'ThisIsSecret'
bcrypt = Bcrypt(app)
server = Server(app.wsgi_app)
mysql = MySQLConnector(app, 'usersdb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
	query = "SELECT id, first_name, last_name, email, DATE_FORMAT(created_at, '%m/%e/%Y %l:%i%p')as created_at, DATE_FORMAT(created_at, '%m/%e/%Y %l:%i%p')as updated_at FROM users"
	user = mysql.query_db(query)
	return render_template("index.html", user=user)


@app.route('/register', methods=['POST'])
def user():
	form = request.form
	fname = form['first_name']
	lname = form['last_name']
	password = form['password']
	confirmation = form['confirmation']
	email = form['email']

	incorrect = False

	#First Name check
	if not fname or len(fname) < 2:
		incorrect = True
		flash("Please enter a valid first name")

	# Last name check
	if not lname or len(lname) < 2:
		incorrect = True
		flash("Please enter a valid last name")

	# Password Checks
	if not password or len(password) < 8:
		incorrect = True
		flash("Please enter a password with 8 or more characters")
	elif not password == confirmation:
		incorrect = True
		flash("Passwords do not match, try again")

	# Email Check
	if not form['email'] or not EMAIL_REGEX.match(form['email']):
		incorrect = True
		flash("Please enter a valid email")

	# Check to see if flag was tripped at all
	if incorrect:
		redirect('/')
	else:
		pw_hash = bcrypt.generate_password_hash(password)
		query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())"
		data = {
			'first_name': form['first_name'],
			'last_name': form['last_name'],
			'email': form['email'],
			'pw_hash': pw_hash
		}
		mysql.query_db(query, data)

	return redirect('/')


@app.route('/login', methods=['POST'])
def login():
	form = request.form
	email = form['email']
	password = form['password']

	if not form['email'] or not EMAIL_REGEX.match(form['email']):
		flash('Please enter a valid email.')
		print form['email']
		return redirect('/')
	if not form['password'] or len(form['password']) < 8:
		flash('Please enter a valid password')
		print form['password']
		return redirect('/')

	query = "SELECT * FROM users WHERE email = :email LIMIT 1"
	data = {
		'email': form['email']
	}
	user = mysql.query_db(query, data)

	if not user:
		flash('Username/email not found. Please try again')
		return redirect('/')
	else:
		if not bcrypt.check_password_hash(user[0]['pw_hash'], password):
			flash('You supplied the incorrect password')
		else:
			print 'successful login'
			session['id'] = user[0]['id']
			session['first_name'] = user[0]['first_name']
	return redirect('/')


@app.route('/users', methods=['POST'])
def create():
	incorrect = False
	form = request.form
	session['first_name'] = form['first_name']
	session['last_name'] = form['last_name']
	if not form['first_name'] or len(form['first_name']) < 3:
		incorrect = True
		flash('You must enter a first name greater than 3 characters.', 'first_name')
	if not form['last_name'] or len(form['last_name']) < 3:
		incorrect = True
		flash('You must enter a last name greater than 3 characters.', 'last_name')
	if not form['email']:
		incorrect = True
		flash('You must enter an email.')
	elif not EMAIL_REGEX.match(form['email']):
		incorrect = True
		flash('You\'ve submitted an invalid email. Please, try again', 'email')
		session['email'] = form['email']
	if not form['password']:
		incorrect = True
		flash('You must enter a password.')
	elif form['password'] < 8:
		incorrect = True
		flash('You must enter a password greater than 7 characters.')

	if incorrect:
		return redirect('/')
	else:
		flash('Thank you for signing up to the users DB!')
		query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
		data = {
			'first_name': form['first_name'],
			'last_name': form['last_name'],
			'email': form['email']
		}
		mysql.query_db(query, data)
	return redirect('/')


@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')


server.watch('./')
server.serve(port=5500, host='127.0.1.1')
