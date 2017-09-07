from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
app.debug = True
app.secret_key = 'ThisIsSecret'
mysql = MySQLConnector(app, 'friendsdb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
	query = "SELECT id, first_name, last_name, email, DATE_FORMAT(created_at, '%m/%e/%Y %l:%i%p')as created_at, DATE_FORMAT(created_at, '%m/%e/%Y %l:%i%p')as updated_at FROM friends"
	friends = mysql.query_db(query)
	print friends
	return render_template("index.html", friends=friends)


@app.route('/friends/<id>/edit')
def edit(id):
	query = "SELECT id, first_name, last_name, email, DATE_FORMAT(updated_at, '%m/%e/%Y %l:%i%p')as updated FROM friends WHERE id = " + id
	friend = mysql.query_db(query)
	print friend
	return render_template('edit.html', friend=friend[0])


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


@app.route('/friends/<id>', methods=['POST'])
def update(id):
	form = request.form
	query = "UPDATE friends SET "
	cols = []

	# Check to see if any data was submitted
	if not form['first_name'] and not form['last_name'] and not form['email']:
		flash('Please fill out at least one field')
		print 'Did not enter info'
		return redirect('/friends/' + id + '/edit')

	# First Name evaluation
	if form['first_name']:
		session['first_name'] = form['first_name']
		cols.append('first_name = \'' + form['first_name'].strip() + '\'')

	# Last Name evaluation
	if form['last_name']:
		session['last_name'] = form['last_name']
		cols.append('last_name = \'' + form['last_name'].strip() + '\'')

	# Email evaluations
	if form['email']:
		# Perform checks
		if len(form['email'].strip()) < 6:
			flash('You must enter an email with more than 5 characters')
			return redirect('/friends/' + id + '/edit')
		elif not EMAIL_REGEX.match(form['email']):
			flash('You must enter a valid email address')
			return redirect('/friends/' + id + '/edit')
		else:
			cols.append('email = \'' + form['email'].strip() + '\'')

	# Create Query
	for col in range(len(cols)):
		if col < len(cols) - 1:
			query += cols[col] + ', '
		else:
			query += cols[col]
	query += ' WHERE id = ' + id
	print query
	mysql.query_db(query)
	return redirect('/friends/' + id + '/edit')


@app.route('/delete/<email_id>', methods=['POST', 'GET'])
def delete(email_id):
	print email_id
	query = "DELETE FROM friends WHERE id = :id"
	data = {'id': email_id}
	mysql.query_db(query, data)
	return redirect('/')

app.run()
