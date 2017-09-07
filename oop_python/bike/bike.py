class Bike(object):
	"""docstring for Bike."""
	def __init__(self, price, max_speed, miles = 0):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	def displayInfo(self):
		print self.price, self.max_speed, self.miles

	def ride(self):
		print "Riding"
		self.miles += 10
		return self

	def reverse(self):
		if not self.miles - 5 < 0:
			print "Reversing"
			self.miles -= 5
		else:
			print "Can't Reverse!"
		return self


bike1 = Bike(200,"25mph")
bike2 = Bike(250,"35mph")
bike3 = Bike(100,"15mph")

bike1.displayInfo()
bike1.ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
