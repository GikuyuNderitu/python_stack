from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)
app.debug = True
server = Server(app.wsgi_app)


@app.route('/')
def index():
	return render_template("index.html", phrase='Cool phrase bro', times=5)


server.serve()
