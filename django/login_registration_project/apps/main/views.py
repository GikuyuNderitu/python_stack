from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	# removes = User.objects.all().delete()
	return render(request, 'main/index.html')


def show_edit(request):
	context = {
		'users' : User.objects.all()
	}
	return render(request, 'main/edit.html', context)

def logout(request):
	request.session.flush()
	return redirect('/')


def login(request):
	response = User.objects.login(**request.POST)
	if not response[0]:
		for message in response[1]:
			messages.error(request, message)
		return redirect('/')

	messages.success(request, response[1])
	request.session['id'] = response[2]['id']
	request.session['first_name'] = response[2]['name']

	return redirect('/edit')


def register(request):
	response = User.objects.register(**request.POST)
	if not response[0]:
		for message in response[1]:
			messages.error(request, message)
		return redirect('/')

	messages.success(request, response[1])

	request.session['id'] = response[2]['id']
	request.session['first_name'] = response[2]['name']
	return redirect('/edit')
