import functools

from rest_framework.response import Response
from rest_framework.views import APIView

class APIView(APIView):
  
  def response(self, data):
    return Response(data)

  def success(self, status = 200, data = None):
    return self.response({'error': None, 'data': data, 'status': status})

  def error(self, status, err = 'error', msg = 'error'):
    return self.response({'error': err, 'data': msg, 'status': status})

  def extract_errors(self, errors, key="field"):
    if isinstance(errors, dict):
      if not errors:
        return key, "Invalid field"
      key = list(errors.keys())[0]
      return self.extract_errors(errors.pop(key), key)
    elif isinstance(errors, list):
      return self.extract_errors(errors[0], key)

    return key, errors

  def invalid_serializer(self, serializer):
    key, error = self.extract_errors(serializer.errors)
    if key == "non_field_errors":
      msg = error
    else:
      msg = f"{key}: {error}"
    return self.error(status = 400, err=f"invalid-{key}", msg=msg)


def validate_serializer(serializer):
    """
    @validate_serializer(TestSerializer)
    def post(self, request):
      return self.success(request.data)
    """
    def validate(view_method):
      @functools.wraps(view_method)
      def handle(*args, **kwargs):
        self = args[0]
        request = args[1]
        s = serializer(data = request.data)
        if s.is_valid():
          request.data = s.data
          request.serializer = s
          return view_method(*args, **kwargs)
        else:
          return self.invalid_serializer(s)
      return handle
    return validate