"""
Intro to Flask.
To give a full accounting
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
	"""Route function hello_world to root."""
	return render_template('index.html', name='Awesome!')


@app.route('/success')
def success():
	"""GET success.html from template"""
	return render_template('success.html')


app.run(debug=True)
