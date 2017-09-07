from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User, UtoC
from ..courses.models import Course

# Create your views here.
def index(request):
	# removes = User.objects.all().delete()
	return render(request, 'login_reg/index.html')


def show_edit(request):
	context = {
		'users' : User.objects.all()
	}
	return render(request, 'login_reg/edit.html', context)

def show_courses(request):
	print UtoC.objects.all()
	context = {
		'users': User.objects.all(),
		'courses': Course.objects.all(),
		'user_courses': UtoC.objects.all()
	}
	return render(request, 'login_reg/user_courses.html', context)

def logout(request):
	request.session.flush()
	return redirect(reverse('login:index'))


def edit(request, id):
	print id
	return redirect(reverse('login:show_edit'))


def login(request):
	response = User.objects.login(**request.POST)
	if not response[0]:
		for message in response[1]:
			messages.error(request, message)
		return redirect(reverse('login:index'))

	messages.success(request, response[1])
	request.session['id'] = response[2]['id']
	request.session['first_name'] = response[2]['name']

	return redirect(reverse('login:show_edit'))


def register(request):
	response = User.objects.register(**request.POST)
	if not response[0]:
		for message in response[1]:
			messages.error(request, message)
		return redirect(reverse('login:index'))

	messages.success(request, response[1])

	request.session['id'] = response[2]['id']
	request.session['first_name'] = response[2]['name']
	return redirect(reverse('login:show_edit'))

def match_user_course(request):
	try:
		course = Course.objects.get(id=request.POST['cid'])
	except Exception as e:
		messages.error("I'm sorry, the selected course does not exist anymore")

	try:
		user = User.objects.get(id=request.POST['uid'])
	except Exception as e:
		messages.error("I'm sorry, the selected user does not exist anymore")

	UtoC.objects.create(user=user, course=course)

	# print User.courses.all()



	return redirect(reverse('login:show_courses'))
