from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Email

# Create your views here.
def index(request):
	return render(request, 'main/index.html')


def show_Emails(request):
	context = {
		'emails' : Email.objects.all()
	}
	return render(request, 'main/success.html', context)


def process(request):
	email_response = Email.objects.validate(**request.POST)
	if not email_response[0]:
		messages.error(request, email_response[1])
		return redirect('/')
	messages.success(request, email_response[1])
	return redirect('/success')

def delete(request, id):
	Email.objects.get(id=id).delete()
	return redirect('/success')
