def getStars(start, string):
	if start < 1:
		return ''
	else:
		return string + getStars(start-1, string)

def printStarArr(arr):
	for val in arr:
		if type(val) is str:
			print getStars(len(val), val[0].lower())
		elif type(val) is int:
			print getStars(val, '*')

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
printStarArr(x)
