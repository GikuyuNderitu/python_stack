#Authors Ekapob and Gikuyu
#These are the basic 13

#1
def print1to255():
	for val in range(1,256):
		print val

# print1to255()

#2
def printOdss1to255():
	for val in range(1,256):
		if val % 2 != 0:
			print val

#printOdss1to255()

#3
def printIntAndSum():
	sum = 0
	for val in range(1,256):
		print val
		sum += val
		print sum

# printIntAndSum()

#4
def iterPrint(arr):
	for val in arr:
		print val
	print '\n'
	for idx, val in enumerate(arr):
		print arr[idx]

# iterPrint([10,2,4,58])

#5
def printMax(arr):
	maxVal = arr[0]
	for val in arr:
		if val > maxVal:
			maxVal = val

	print maxVal

# printMax([120,3214,348,12830,34])

#6
def printAvg(lis):
	sum = 0
	for val in lis:
		sum += val
	print sum/len(lis)

# printAvg([2.0,5.0])

#7
def odd_array():
	newlist = []
	for val in range(1,256):
		if val%2 != 0:
			newlist.append(val)
	print newlist

# odd_array()

#8
def squared(lis):
	for idx, val in enumerate(lis):
		lis[idx] = val*val
#
# a = [4,2,8,12]
# print a, '\n'
# squared(a)
# print a

#9
def greater_than_y(arr,Y):
	count = 0
	for val in arr:
		if val > Y:
			count+=1
	print count

# greater_than_y([3,4123,80342,348,123], 350)

#10
def zero_neg(lis):
	for idx, val in enumerate(lis):
		if val < 0:
			lis[idx] = 0

	return lis

# print zero_neg([2,4,6,-8])

#11
def max_min_avg(arr):
	max = arr[0]
	min = max
	sum = 0
	for val in arr:
		if val > max:
			max = val
		if val < min:
			min = val
		sum += val
	print max, min, float(sum)/len(arr)

# max_min_avg([1,2,3,4,6])

#12
def shift_values(arr):
	for idx, val in enumerate(arr):
		if idx < len(arr)-1:
			arr[idx] = arr[idx+1]
		else:
			arr[idx] = 0
	return arr

# print shift_values([1,2,3,4,5])

#13
def swap_string(arr):
	for idx, val in enumerate(arr):
		if val < 0:
			arr[idx] = 'Dojo'

a = [0,3,1,-8,-123]
swap_string(a)
print a
