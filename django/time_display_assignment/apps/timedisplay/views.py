from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(request):
	time = datetime.datetime.now()
	print time
	obj = {
		'time': time
	}
	return render(request, 'timedisplay/index.html', obj)
