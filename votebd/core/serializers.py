from django.db.models import fields
from votebd.core import models
from rest_framework import serializers
from votebd.core.models import User

class UserListSerializers(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'name']