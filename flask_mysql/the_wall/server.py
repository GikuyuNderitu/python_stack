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
mysql = MySQLConnector(app, 'thewalldb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
	return render_template("index.html")


@app.route('/wall')
def wall():
	comments = 'comment hello'
	message_query = "SELECT users.id AS user_id, messages.id AS message_id, users.first_name, users.last_name, content AS message, DATE_FORMAT(messages.created_at, '%M %D %Y') AS created_at FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.id DESC"
	messages = mysql.query_db(message_query)
	comment_query = 	("SELECT users.id AS user_id, messages.id AS message_id, comments.id AS comment_id, users.first_name, users.last_name, comments.content AS comment, DATE_FORMAT(comments.created_at, '%M %D %Y') AS created_at "
						"FROM users "
						"JOIN comments ON comments.user_id = users.id "
						"JOIN messages ON messages.id = comments.message_id "
						"ORDER BY messages.id, created_at")
	comments = mysql.query_db(comment_query)
	return render_template("index.html", posts=messages, comments=comments)


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

		session['id'] = mysql.query_db(query, data)
		session['first_name'] = fname

	return redirect('/')


@app.route('/login', methods=['POST'])
def login():
	form = request.form
	email = form['email']
	password = form['password']

	if not form['email'] or not EMAIL_REGEX.match(form['email']):
		flash('Please enter a valid email.')
		return redirect('/')
	if not form['password'] or len(form['password']) < 8:
		flash('Please enter a valid password')
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
			session['id'] = user[0]['id']
			session['first_name'] = user[0]['first_name']
	return redirect('/wall')


@app.route('/message', methods=['POST'])
def message():
	message = request.form['message']
	if not message or len(message.strip()) < 1:
		flash('You must enter a message ')
		return redirect('/wall')

	query = "INSERT INTO messages (user_id, content, created_at, updated_at) VALUES (:user_id, :content, NOW(), NOW())"
	data = {
		'user_id':  session['id'],
		'content': message
	}

	mysql.query_db(query, data)
	return redirect('/wall')


@app.route('/message/<msg_id>', methods=['POST'])
def comment(msg_id):
	comment = request.form['comment']
	if not comment or len(comment.strip()) < 1:
		flash('You must type words to comment!')
		return redirect('/wall')

	query = "INSERT INTO comments (user_id, message_id, content, created_at, updated_at) VALUES (:user_id, :message_id, :content, NOW(), NOW())"
	data = {
		'user_id':  session['id'],
		'message_id': msg_id,
		'content': comment
	}
	mysql.query_db(query, data)
	return redirect('/wall')


@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')


server.watch('./')
server.serve(port=5500, host='127.0.1.1')
