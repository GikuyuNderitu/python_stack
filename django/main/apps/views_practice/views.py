from django.shortcuts import render

# Create your views here.
def index(req):
	return render(req, 'views_practice/index.html')


def show(req):
	print(req.method)
	return render(req, 'views_practice/users.html')
