from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from livereload import Server
import re

app = Flask(__name__)
app.debug = True
app.secret_key = 'ThisIsSecret'
server = Server(app.wsgi_app)
mysql = MySQLConnector(app, 'usersdb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
	query = "SELECT id, first_name, last_name, email, DATE_FORMAT(created_at, '%m/%e/%Y %l:%i%p')as created_at, DATE_FORMAT(created_at, '%m/%e/%Y %l:%i%p')as updated_at FROM users"
	user = mysql.query_db(query)
	return render_template("index.html", user=user)


@app.route('/register', methods=['POST'])
def register():
	form = request.form
	fname = form['first_name']
	lname = form['last_name']

	if not(fname or lname):
		flash('Please fill out both first and last name fields!')
		print 'invalid name'

	return redirect('/')


@app.route('/login', methods=['POST'])
def login():
	form = request.form
	print form
	if not form['email'] or not EMAIL_REGEX.match(form['email']):
		flash('Please enter a valid email.')
		print form['email']
		return redirect('/')
	if not form['password'] or len(form['password']) < 8:
		flash('Please enter a valid password')
		print form['password']
		return redirect('/')

	query = "SELECT id FROM users WHERE email = " + form['email']
	results = mysql.query_db(query)

	if not results:
		flash('Invalid user submitted')
		return redirect('/')
	else:
		print results['password']
	return redirect


@app.route('/users/<id>')
def edit(id):
	query = "SELECT id, first_name, last_name, email, DATE_FORMAT(updated_at, '%m/%e/%Y %l:%i%p')as updated FROM users WHERE id = " + id
	friend = mysql.query_db(query)
	print friend
	return render_template('edit.html', friend=friend[0])


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
