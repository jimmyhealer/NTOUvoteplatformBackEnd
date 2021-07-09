from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
  username = models.TextField(unique = True)
  password = models.CharField(max_length = 128)
  name = models.CharField(max_length = 50)

class Group(models.Model):
  name = models.CharField(max_length = 50, unique = True)
  group = models.ForeignKey(User, on_delete = models.CASCADE)