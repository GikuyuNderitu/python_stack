from django.shortcuts import render, redirect
from random import choice
from string import ascii_uppercase

# Create your views here.

ALPHANUM_DICT = ascii_uppercase+'0123456789'
attempt = 0

def generate(req):
	if 'attempt' not in req.session :
		req.session['attempt'] = 0
	req.session['attempt'] += 1
	req.session['num'] = ''.join(choice(ALPHANUM_DICT) for i in range(14))
	return redirect('/')

def index(req):
	return render(req, 'randomwordgenerator/index.html')
