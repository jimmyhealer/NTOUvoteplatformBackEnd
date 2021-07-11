import typing
from .models import User

def create_user(username: str, name: str, password: str) -> User:
  return User.objects.create_user(username = username, name = name, password = password)

def find_user_by_username(username: str) -> typing.Optional[User]:
  try:
    return User.objects.get(username = username)
  except User.DoesNotExist:
    return None