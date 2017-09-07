class Car(object):
	"""docstring for Car."""
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = .12
		if price > 10000:
			self.tax = .15
		self.displayAll()

	def displayAll(self):
		print  ("Price: {price}\n"
				"Speed: {speed}\n"
				"Fuel: {fuel}\n"
				"Mileage: {mileage}\n"
				"Tax: {tax}\n".format(price=self.price,speed=self.speed,fuel=self.fuel,mileage=self.mileage,tax=self.tax))

car1 = Car(20000,'75mph','Full',20000)
car2 = Car(40000,'45mph','Full',80000)
car3 = Car(10000,'125mph','Full',95000)
car4 = Car(25000,'45mph','Full', 70000)
car5 = Car(90000,'925mph','Full',12500)
car6 = Car(50007,'65mph','Full',150000)
