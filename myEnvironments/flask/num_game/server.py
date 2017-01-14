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


def getRandomInt():
	return int(round((random.random() * 100) + 1))


@app.route('/')
def index():
	"""Route function hello_world to root."""
	if 'random_num' not in session:
		session['random_num'] = getRandomInt()
	return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
	"""Return the dojo form"""
	print request.form
	print session['random_num']
	session['match'] = ''
	session['times_played'] = request.form['times_played']
	session['guess'] = request.form['guess']
	print session['guess']
	if int(session['guess']) == session['random_num']:
		session['match'] = True
	else:
		if int(session['guess']) > int(session['random_num']):
			session['value'] = 'HIGH'
		else:
			session['value'] = 'LOW'
	print session['match']
	# session['counter'] = str(int(session['counter']) + 2)
	return redirect('/')


@app.route('/play-again')
def play_again():
	session.clear()
	return redirect('/')


server.watch('./')
server.serve(port=5500, host='127.0.1.1')
# index()
