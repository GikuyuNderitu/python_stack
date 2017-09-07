"""
Intro to Flask.
To give a full accounting
"""
import re
from flask import Flask, render_template, redirect
from livereload import Server

app = Flask(__name__)
app.debug = True
app.secret_key = 'ThisIsSecret'
server = Server(app.wsgi_app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/', methods=['GET'])
def index():
	return render_template("index.html")


@app.route('/ninja')
def ninjas():
	return render_template("ninja.html")


@app.route('/ninja/<color>')
def ninja(color):
	return render_template("ninja.html", color=color)


@app.route('/reset')
def reset():
	return redirect('/')


server.watch('./')
server.serve(port=5500, host='127.0.1.1')
