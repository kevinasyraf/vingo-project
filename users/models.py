from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
	objects = CustomUserManager()
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	
