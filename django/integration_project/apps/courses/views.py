from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Course, Description

# Create your views here.

def index(request):
	context = {
		'courses' : Course.objects.all()
	}
	return render(request, 'courses/index.html', context)

def show_delete(request, id):
	context = {
	'course' : Course.objects.get(id=id)
	}
	return render(request, 'courses/delete.html', context)

def add(request):
	form = request.POST
	incorrect = False
	if len(form['name']) < 2:
		messages.add_message(request, messages.ERROR, 'Name must be longer than 2 characters')
		incorrect = True

	if form['description'] and len(form['description']) < 10:
		incorrect = True
		messages.add_message(request, messages.ERROR, 'Description must be longer than 10 characters (if you\'re going to write one.)')


	if incorrect:
		return redirect(reverse('course:index'))

	d = Description.objects.create(description=form['description'])
	Course.objects.create(course=form['name'], description=d)

	print d

	messages.add_message(request, messages.SUCCESS, 'Successful submission')

	return redirect(reverse('course:index'))



def destroy(req, id):
	Course.objects.get(id=id).delete()
	return redirect(reverse('course:index'))
