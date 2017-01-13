"""
Intro to Flask.
To give a full accounting
"""

from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)
app.debug = True
server = Server(app.wsgi_app)


@app.route('/')
def hello_world():
	"""Route function hello_world to root."""
	return render_template('index.html')


@app.route('/ninjas')
def ninjas():
	"""Route function ninjas from template"""
	return render_template('ninjas.html')


@app.route('/dojo/new')
def dojo_form():
	"""Return the dojo form"""
	return render_template('dojo.html')


server.watch('./')
server.serve(port=5500, host='127.0.1.1')
