class Animal(object):
	"""docstring for Animal."""
	global greeting
	greeting = 'Animal'
	def __init__(self, name = 'Some Animal'):
		self.name = name
		self.health = 100

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print greeting
		print "The animal '{}' has {} health".format(self.name, self.health)



animal = Animal().walk().walk().walk().run().run().displayHealth()


class Dog(Animal):
	"""docstring for Dog."""
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150

	def pet(self):
		self.health += 10
		return self


dog = Dog('Fido').walk().walk().walk().run().run().pet().displayHealth()


class Dragon(Animal):
	"""docstring for Dragon."""
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170

	def fly(self):
		self.health -= 10
		return self


dragon = Dragon('Smaug').walk().walk().walk().run().run().fly().fly().displayHealth()

# animal.fly()
# animal.pet()
