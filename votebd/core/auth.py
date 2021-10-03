import typing
import json

from rest_framework.response import Response
from rest_framework.views import APIView


from .models import User
from .serializers import UserListSerializers
from .decorators import login_required
from votebd.core import services

from django.contrib.auth.backends import BaseBackend
from django.urls.conf import path
from django.contrib.auth import authenticate, login, logout

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
    # body = json.loads(request.body.decode())
    data = request.data
    user = authenticate(request, username = data["username"], password = data["password"])

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
  def get(self, request):
    logout(request)
    return Response("logout")

class UserSignUpAPI(APIView):
  
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
  
  def get(self, request):
    return Response('Test')

class UserDetailView(APIView):
    
    @login_required
    def get(self, request):
        user = User.objects.get(username = request.data['username'])
        serializer = UserListSerializers(user)
        return self.success(data = serializer.data)

urlpatterns = [
  path("signin/", UserSigninAPI.as_view()),
  path('signout/', UserSignoutAPI.as_view()),
  path('signup/', UserSignUpAPI.as_view()),
    path('profile/', UserDetailView.as_view()) 
]