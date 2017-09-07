"""
Intro to Flask.
To give a full accounting
"""

from flask import Flask, render_template
from livereload import Server, shell

app = Flask(__name__)
app.debug = True
server = Server(app.wsgi_app)


@app.route('/')
def hello_world():
	"""Route function hello_world to root."""
	return render_template('index.html', name='Awesome!')


@app.route('/success')
def success():
	"""GET success.html from template"""
	return render_template('success.html')


server.watch('./')
server.serve(port=5500, host='127.0.1.1')
