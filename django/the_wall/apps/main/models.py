from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	password = models.CharField(max_length=100)
	email = models.EmailField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class Message(models.Model):
	content = models.TextField(max_length=1000)
	user_id = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class Comment(models.Model):
	content = models.TextField(max_length=1000)
	user_id = models.ForeignKey(User)
	message_id = models.ForeignKey(Message)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
