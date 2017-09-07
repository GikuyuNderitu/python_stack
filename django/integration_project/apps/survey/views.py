from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(req):
	return render(req, 'survey/index.html')


def result(req):
	return render(req, 'survey/result.html')

def process(req):
	form = req.POST
	print form

	name = form['name']
	req.session['loc'] = form['loc']
	req.session['lang'] = form['lang']
	comment = form['comment']
	incorrect = False
	if not name or len(name) < 2:
		messages.error(req, 'Please fill out the name section of the form')
		incorrect = True
	else:
		req.session['name'] = name
	if not comment or len(comment) < 1:
		messages.error(req, 'Please fill out the comment section of the form.')
		incorrect = True
	else:
		req.session['comment'] = comment
	if incorrect:
		return redirect('/')
	else:
		req.session['completed'] = True
		messages.info(req, 'Successful form submission')
		return redirect('/result')

def reset(req):
	req.session.flush()
	return redirect('/')
