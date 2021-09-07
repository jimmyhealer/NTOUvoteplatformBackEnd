import typing
import json

from rest_framework.response import Response
from rest_framework.views import APIView


from .models import User
from .serializers import UserListSerializers
from .decorators import login_required
from votebd.core import services

from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.contrib.auth.backends import BaseBackend
from django.urls.conf import include, path
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods

class CheckPasswordBackend(BaseBackend):
  def authenticate(
        self, request = None, username = None, password = None
      ) -> typing.Optional[User]:
    user = services.find_user_by_username(username = username)
    if user is None: 
      return None
    
    return user if user.check_password(password) else None

  def get_user(self, user_id) -> typing.Optional[User]:
    try:
      return User.objects.get(id = user_id)
    except User.DoesNotExist:
      return None

class UserSigninAPI(APIView):
  def post(self, request):
    '''
    user Signin API
    '''
    body = json.loads(request.body.decode())
    user = authenticate(request, username = body["username"], password = body["password"])

    if user:
      login(request, user)
      return Response("Accepted", status = 202)
    else:
      return Response("Unauthorized", status = 401)
  
  @login_required
  def get(self, request):
    '''
    get user list
    '''
    user = User.objects.all()
    serializers = UserListSerializers(user, many = True)
    return Response(serializers.data)

class UserSignoutAPI(APIView):
  
  @login_required
  def post(self, request):
    logout(request)
    return Response("logout")

class SignUpAPI(APIView):
  
  def post(self, request):
    data = request.data
    try:
      user = services.create_user(username = data['username'],
                          name = data['name'],
                          password = data['password'])
    except:
      return Response('Bad Request', status = 400)

    if user:
      return Response('Created', status = 201)
    
    return Response('Internal Server Error', status = 500)
  
  @method_decorator(ensure_csrf_cookie)
  def get(self, request):
    return Response('Test')

urlpatterns = [
  path("signin/", UserSigninAPI.as_view()),
  path('signout/', UserSignoutAPI.as_view()),
  path('signup/', SignUpAPI.as_view()),
]