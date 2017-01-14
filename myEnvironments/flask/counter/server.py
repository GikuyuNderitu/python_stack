"""
Intro to Flask.
To give a full accounting
"""
import random
from flask import Flask, render_template, request, redirect, session
from livereload import Server

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
app.debug = True
server = Server(app.wsgi_app)


@app.route('/')
def index():
	"""Route function hello_world to root."""
	return render_template('index.html')


@app.route('/add', methods=['POST'])
def create_users():
	"""Return the dojo form"""
	if request.form['counter'] == 'reset':
		session.clear()
		session['counter'] = '-1'
	if not('counter' in session):
		session['counter'] = str(1)
	session['counter'] = str(int(session['counter']) + 2)
	return redirect('/')


def getRandomNum():
	str = ''
	for i in range(1, 13):
		print type(round(random.random() * 9))
	return str


server.watch('./')
server.serve(port=5500, host='127.0.1.1')
