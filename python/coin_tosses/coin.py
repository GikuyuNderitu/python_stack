import random

def flip_coin():
	return round(random.random()*2)

def probability(flips):
	coin = ''
	head_counter = 0
	tail_counter = 0
	for val in range(1, flips+1):
		coin_val = flip_coin()
		if coin_val == 0:
			coin = 'tail'
			tail_counter += 1
		else:
			coin = 'head'
			head_counter += 1
		print 'Attempt #{}: Throwing a coin...  It\'s a {}! ... Got {} head(s) so far and {} tail(s) so far'.format(val, coin, head_counter, tail_counter)

probability(500)
