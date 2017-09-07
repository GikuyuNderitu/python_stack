from django.shortcuts import render, redirect
import random, datetime

# Create your views here.
def index(req):
	# req.session.flush()
	return render(req, 'gold/index.html')


def process(req, building):
	curcoin = 0
	message = ''
	curdict = {}
	curtime = datetime.datetime.now().strftime('%Y/%m/%d %I:%M') + datetime.datetime.now().strftime('%p').lower()
	if not 'list' in req.session:
		req.session['list'] = []
		req.session['total'] = 0
	if building == 'farm':
		curcoin = random.randint(10,20)
	elif building == 'cave':
		curcoin = random.randint(5,10)
	elif building == 'house':
		curcoin = random.randint(2,5)
	elif building == 'casino':
		curcoin = random.randint(-50,50)

	req.session['total'] += curcoin
	if curcoin < 0:
		message = 'Entered a casino and lost ' + str(curcoin*-1) + ' gold coins... Ouch...'
	else:
		message = 'Earned ' + str(curcoin) + ' gold coins from the ' + building + '!'

	curdict['message'] = message
	curdict['gold'] = curcoin
	curdict['date'] = curtime
	req.session['list'].insert(0,curdict)
	return redirect('/')
