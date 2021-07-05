from rest_framework import serializers
from accounts.models import User


class AccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'name']