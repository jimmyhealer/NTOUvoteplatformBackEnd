from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.utils import module_loading
# Create your models here.

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)

class Group(models.Model):
  group = models.ForeignKey(User, on_delete = models.CASCADE)
  groupname = models.CharField(max_length = 50, unique = True)