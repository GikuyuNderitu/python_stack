"""
Intro to Flask.
To give a full accounting
"""
import random
import datetime
from flask import Flask, render_template, request, redirect, session
from livereload import Server

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
app.debug = True
server = Server(app.wsgi_app)


def fifty_50():
	if random.random() < .5:
		return -1
	else:
		return 1


def getRandomCoins(valrange, sign):
	value = int(round((random.random() * (valrange[1] - valrange[0])) + valrange[0]))
	if sign != 'pos':
		value *= fifty_50()
	return value


@app.route('/')
def index():
	# session.clear()
	"""Route function hello_world to root."""
	if 'total' not in session:
		session['total'] = 0
		session['list'] = []
	return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def guess():
	"""Return the dojo form"""
	context = request.form['building']
	curval = 0
	if context == 'farm':
		curval = getRandomCoins([10, 20], 'pos')
	elif context == 'cave':
		curval = getRandomCoins([5, 10], 'pos')
	elif context == 'house':
		curval = getRandomCoins([2, 5], 'pos')
	else:
		curval = getRandomCoins([10, 50], 'NEGATIVE')
	session['total'] += curval
	datestring = datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S') + datetime.datetime.now().strftime('%p').lower()
	dictionary = {'gold': curval, 'building': context, 'time': datestring}
	tup = (curval, dictionary)
	session['list'].insert(0, tup)
	return redirect('/')


@app.route('/reset')
def reset():
	session.clear()
	return redirect('/')


server.watch('./')
server.serve(port=5500, host='127.0.1.1')
# index()
