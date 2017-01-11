def odd_even(limit):
	for val in range(1,limit+1):
		if(val % 2 != 0):
			print 'Number is ' + str(val) + '.\tThis is an odd number.'
		else:
			print 'Number is ' + str(val) + '.\tThis is an even number.'


odd_even(2000)
