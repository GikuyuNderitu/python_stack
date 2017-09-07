from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
	"""docstring for Course."""
	course = models.CharField(max_length=70)
	description = models.OneToOneField('Description', on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Description(models.Model):
	"""docstring for Course."""
	description = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
