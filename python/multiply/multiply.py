##Point of the problem
def multiply1(mylist, multiplicand):
	newList = []
	for val in mylist:
		newList.append(val*multiplicand)
	return newList

##More efficient
def multiply2(mylist, multiplicand):
	for idx in range(0,len(mylist)):
		mylist[idx] *= 5


a = [2,4,10,16]
print a
b = multiply1(a, 5)
multiply2(a, 5)
print a,b #Should be the same
