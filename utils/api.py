from rest_framework.response import Response
from rest_framework.views import APIView

class APIView(APIView):
  
  def response(self, data):
    return Response(data)

  def success(self, data = None):
    return self.response({'error': None, 'data': data})

  def error(self, err = 'error', msg = 'error'):
    return self.response({'error': err, 'data': msg})
