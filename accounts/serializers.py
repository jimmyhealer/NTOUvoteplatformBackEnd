from django.db import models
from rest_framework import serializers
from accounts.models import User


class AccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'name']

class UserLoginSerializer(serializers.ModelSerializer):
  class Meta:
    models = User
    fields = ['username', 'password']