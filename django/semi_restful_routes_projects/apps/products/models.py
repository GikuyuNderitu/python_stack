from __future__ import unicode_literals
import re
from django.db import models

FLOAT_PRICE = re.compile(r'^[0-9.]+$')

# Create your models here.
class ProductManager(models.Manager):
	"""docstring for ProductManager."""
	def validate(self, **kwargs):
		name = str(kwargs['name'][0])
		description = str(kwargs['description'][0])
		price = str(kwargs['price'][0])
		errors = []
		incorrect = False

		if not name:
			incorrect = True
			errors.append("You forgot to give the product a name.")

		if not price:
			incorrect = True
			errors.append("You forgot to give the product a price.")

		elif not FLOAT_PRICE.match(price):
			incorrect = True
			errors.append("The entered price must be comprised of digits.")

		if incorrect:
			return (False, errors)

		fprice = float(price)

		Product.objects.create(name=name, description=description, price=fprice)

		return (True, "You successfully entered a new Product")

class Product(models.Model):
	"""docstring for Product."""
	name = models.CharField(max_length=60)
	description = models.TextField(max_length=500)
	price = models.FloatField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ProductManager()
