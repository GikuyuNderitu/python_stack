from __future__ import unicode_literals
import re
from django.db import models

EMAIL_REGEX = re.compile(ur'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class EmailManager(models.Manager):
	"""docstring for EmailManager."""
	def validate(self, **kwargs):
		email = str(kwargs['email'][0])
		print type(email)
		if not EMAIL_REGEX.match(email):
			return (False, 'Please enter a VALID email!')

		Email.objects.create(email=email)
		return (True, 'The email address you entered (' + str(kwargs["email"][0]) + ') is a VALID email address! Thank you!')


class Email(models.Model):
	email = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = EmailManager()
