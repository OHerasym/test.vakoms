from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth import models as auth_models

import datetime

import re

class CustomUserManager(auth_models.BaseUserManager):
	def create_user(self, email, first_name, last_name, mobile, password): #####

		if not re.match(r'\d{10}$', mobile):
			raise ValueError('Enter a valid mobile!')

		user = self.model(
				email = CustomUserManager.normalize_email(email),
				first_name = first_name, ###
				last_name = last_name, ###
				mobile = mobile,
			)
		user.is_staff = True
		user.set_password(password)
		user.is_active = False

		user.save(using = self._db)
		return user

	def create_superuser(self, email, first_name, last_name, mobile, password): ###

		if not re.match(r'\d{10}$', mobile):
			raise ValueError('Enter a valid mobile!')

		user = self.model(
				email = CustomUserManager.normalize_email(email),
				first_name = first_name,
				last_name = last_name,
				mobile = mobile,
			)
		user.is_staff = True
		user.is_superuser = True
		user.set_password(password)
		user.is_active = True

		user.save(using = self._db)
		return user

class UserProfile(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
	email = models.EmailField(unique = True)  ######
	mobile = models.CharField(max_length = 10)
	first_name = models.CharField(max_length= 30)
	last_name = models.CharField(max_length = 30)
	is_staff = models.BooleanField()
	activation_key = models.CharField(max_length=40, blank=True) 
	key_expires = models.DateTimeField(default=datetime.date.today())
	is_active = models.BooleanField()

	#def __str__(self):
	#	return self.user.first_name

	#class Meta:
	#	verbose_name_plural=u'User profiles'

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['mobile', 'first_name', 'last_name']
	objects = CustomUserManager()

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	def is_staff(self):
		return self.is_staff


