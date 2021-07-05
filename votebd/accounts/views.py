from .models import User, Group
from rest_framework.response import Response
from rest_framework.views import APIView


def loginAPI(data):
  if data.username == 'root' and data.password == 'rootroot':
    return {'username': 'root', 'name': 'root', 'group': ['A', 'B']}
  return None

# Create your views here.
class UserLoginAPI(APIView):

  def POST(self, request):
    user = loginAPI(request.data)
    if user:
      return Response(user)
    else:
      return Response({'message': 'Login Error'})