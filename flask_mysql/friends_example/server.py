from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from livereload import Server
import re

app = Flask(__name__)
app.debug = True
app.secret_key = 'ThisIsSecret'
server = Server(app.wsgi_app)
mysql = MySQLConnector(app, 'emailsdb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/emails')
def success():
	query = "SELECT id, email, DATE_FORMAT(created_at, '%m/%e/%Y %l:%i%p')as created_at FROM emails"
	emails = mysql.query_db(query)
	print emails
	return render_template('success.html', emails=emails)


@app.route('/process', methods=['POST'])
def submit():
	if len(request.form['email']) < 1:
		flash('You\'ve gotta type something man!')
		return redirect('/')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('You\'ve submitted an incorrect email. Please, try again')
		flash(request.form['email'])
		return redirect('/')
	else:
		flash('The email address you entered (' + request.form['email'] + ') is a VALID email address! Thank you!')
		query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
		data = {
			'email': request.form['email']
		}
		mysql.query_db(query, data)
		return redirect('/emails')


@app.route('/delete/<email_id>', methods=['POST', 'GET', 'DELETE'])
def delete(email_id):
	print email_id
	query = "DELETE FROM emails WHERE id = :id"
	data = {'id': email_id}
	mysql.query_db(query, data)
	return redirect('/emails')


server.watch('./')
server.serve(port=5500, host='127.0.1.1')
