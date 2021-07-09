import typing
import json

from .models import User
from votebd.core import services

from django.contrib.auth.backends import BaseBackend
from django.urls.conf import path
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, response
from django.views.decorators.http import require_http_methods

class CheckPasswordBackend(BaseBackend):
  def authenticate(
        self, request = None, email = None, password = None
      ) -> typing.Optional[User]:
    user = services.find_user_by_email(email = email)
    if user is None: 
      return None
    
    return user if user.check_password(password) else None

  def get_user(self, user_id) -> typing.Optional[User]:
    try:
      return User.objects.get(id = user_id)
    except User.DoesNotExist:
      return None

@require_http_methods(["POST"])
def login_view(request):
  body = json.loads(request.body.decode())
  user = authenticate(request, email=body["email"], password=body["password"])

  if user:
    login(request, user)
    return HttpResponse("OK")
  else:
    return HttpResponse("Unauthorized", status=401)

@require_http_methods(["GET"])
def get_user_list(request):
  user = User.objects.all()
  return response(user)

urlpatterns = [
  path("login", login_view),
  path("user", login_view),
]