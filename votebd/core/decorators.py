import functools
from rest_framework.response import Response



class BasePermissionDecorator(object):
  def __init__(self, func):
    self.func = func
  
  def __get__(self, obj, obj_type):
    return functools.partial(self.__call__, obj)

  def error(self, data):
    return Response({"error": "permission-denied", "data": data, 'status': 403})

  def __call__(self, *args, **kwargs):
    self.request = args[1]

    if self.check_permission():
      # if self.request.user.is_active:
      #   return self.error("Your account is disabled")
      return self.func(*args, **kwargs)
    else:
      return self.error("Please login first")

  def check_permission(self):
    raise NotImplementedError()

class login_required(BasePermissionDecorator):
  def check_permission(self):
    return self.request.user.is_authenticated