from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from livereload import Server
import re

app = Flask(__name__)
app.debug = True
app.secret_key = 'ThisIsSecret'
server = Server(app.wsgi_app)
mysql = MySQLConnector(app, 'friendsdb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
	query = "SELECT id, first_name, last_name, email, DATE_FORMAT(created_at, '%m/%e/%Y %l:%i%p')as created_at, DATE_FORMAT(created_at, '%m/%e/%Y %l:%i%p')as updated_at FROM friends"
	friends = mysql.query_db(query)
	print friends
	return render_template("index.html", friends=friends)


@app.route('/emails')
def success():
	query = "SELECT id, email, DATE_FORMAT(created_at, '%m/%e/%Y %l:%i%p')as created_at FROM emails"
	emails = mysql.query_db(query)
	print emails
	return render_template('success.html', emails=emails)


@app.route('/friends', methods=['POST'])
def create():
	incorrect = False
	form = request.form
	session['first_name'] = form['first_name']
	session['last_name'] = form['last_name']
	if len(form['first_name']) < 1:
		incorrect = True
		flash('You must enter a first name.', 'first_name')
	if len(form['last_name']) < 1:
		incorrect = True
		flash('You must enter a last name.', 'last_name')
	if len(form['email']) < 1:
		incorrect = True
		flash('You must enter an email.')
	elif not EMAIL_REGEX.match(form['email']):
		incorrect = True
		flash('You\'ve submitted an invalid email. Please, try again', 'email')
		session['email'] = form['email']
	if incorrect:
		return redirect('/')
	else:
		flash('Thank you for signing up to the friends DB!')
		query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
		data = {
			'first_name': form['first_name'],
			'last_name': form['last_name'],
			'email': form['email']
		}
		mysql.query_db(query, data)
	return redirect('/')


@app.route('/delete/<email_id>', methods=['POST', 'GET', 'DELETE'])
def delete(email_id):
	print email_id
	query = "DELETE FROM friends WHERE id = :id"
	data = {'id': email_id}
	mysql.query_db(query, data)
	return redirect('/')


server.watch('./')
server.serve(port=5500, host='127.0.1.1')
