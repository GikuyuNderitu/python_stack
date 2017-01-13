"""
Intro to Flask.
To give a full accounting
"""

from flask import Flask, render_template, request
from livereload import Server

app = Flask(__name__)
app.debug = True
server = Server(app.wsgi_app)


@app.route('/')
def index():
	"""Route function hello_world to root."""
	return render_template('index.html')


@app.route('/results', methods=['POST'])
def show_submission():
	"""Return the dojo form"""
	return render_template('results.html', data=request.form)


server.watch('./')
server.serve(port=5500, host='127.0.1.1')
