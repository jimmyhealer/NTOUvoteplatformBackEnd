import uuid

from django.db import models
from django.contrib.auth.models import (
  AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):

  def create_user(self, username, name, password = None):
    if not username:
      raise ValueError('Users must have an username')

    user = self.model(
      username = username,
      name = name
    )

    user.set_password(password)
    user.save()
    return user

class User(AbstractBaseUser):

  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  username = models.CharField(max_length = 32, blank = True, unique = True)
  name = models.CharField(max_length = 32, blank = False, null = False)
  is_active = models.BooleanField(default = True)

  objects = UserManager()

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['name']

  def __str__(self):
    return self.username