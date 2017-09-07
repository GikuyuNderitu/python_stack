from __future__ import unicode_literals
import re
import bcrypt
from django.db import models
from ..courses.models import Course

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
	"""docstring for UserManager."""
	def login(self, **kwargs):
		errors = []
		email = str(kwargs['email'][0])
		password = str(kwargs['password'][0])
		incorrect = False

		if not EMAIL_REGEX.match(email):
			incorrect = True
			errors.append('Please insert a valid email address')
			return (False, errors)

		try:
			user = User.objects.get(email=email)
		except Exception as e:
			errors.append('{}'.format(e))
			return (False, errors)

		hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))


		if user.password != bcrypt.hashpw(password, user.password.encode()):
			errors.append('I\'m sorry, the password you entered was wrong.')
			return (False, errors)

		return (True, 'Successful Login', {'id': user.id, 'name' : user.first_name})




	def register(self, **kwargs):
		errors = []
		email = str(kwargs['email'][0])
		f_name = str(kwargs['first_name'][0])
		l_name = str(kwargs['last_name'][0])
		password = str(kwargs['password'][0])
		confirm = str(kwargs['confirmation'][0])

		incorrect = False

		#First Name check
		if not f_name or len(f_name) < 2:
			incorrect = True
			errors.append("Please enter a valid first name")

		# Last name check
		if not l_name or len(l_name) < 2:
			incorrect = True
			errors.append("Please enter a valid last name")

		# Password Checks
		if not password or len(password) < 8:
			incorrect = True
			errors.append("Please enter a password with 8 or more characters")
		elif not password == confirm:
			incorrect = True
			errors.append("Passwords do not match, try again")

		# Email Check
		if not email or not EMAIL_REGEX.match(email):
			incorrect = True
			errors.append("Please enter a valid email")


		# Check to see if flag was tripped at all
		if incorrect:
			return (False, errors)

		hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))
		print len(hashed), hashed
		newId = User.objects.create(first_name=f_name, last_name=l_name, password=hashed, email=email)
		print newId.id
		return (True, 'Successfully registered!', {'id' : newId.id, 'name' : f_name})


class User(models.Model):
	"""docstring for User."""
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	password = models.CharField(max_length=100)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()


class UtoC(models.Model):
	"""docstring for UtoC."""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
