from django.shortcuts import render, redirect

# Create your views here.
def index(req):
	return render(req, 'ninjas/index.html')

def ninjas(req):
	return render(req, 'ninjas/ninjas.html')

def ninja(req, color):
	print color
	context = {
		"color" : color
	}
	return render(req, 'ninjas/ninjas.html', context)

def reset(req):
	return redirect('/ninjas')
