from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from livereload import Server

app = Flask(__name__)
app.debug = True
app.secret_key = 'ThisIsSecret'
server = Server(app.wsgi_app)
mysql = MySQLConnector(app, 'emailsdb')


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/success')
def show(friend_id):
	query = "Select * FROM friends WHERE id = :specific_id"
	data = {'specific_id': friend_id}
	friend = mysql.query_db(query, data)
	return render_template('success.html', friends=friend)


@app.route('/friends', methods=['POST'])
def create():
	query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
	data = {
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'occupation': request.form['occupation']
	}
	mysql.query_db(query, data)
	return redirect('/')


@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
	query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
	data = {
		'first_name': request.form['first_name'],
		'last_name': request.form['last_name'],
		'occupation': request.form['occupation'],
		'id': friend_id
	}
	mysql.query_db(query, data)
	return redirect('/')


@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
	query = "DELETE FROM friends WHERE id = :id"
	data = {'id': friend_id}
	mysql.query_db(query, data)
	return redirect('/')


server.watch('./')
server.serve(port=5500, host='127.0.1.1')
