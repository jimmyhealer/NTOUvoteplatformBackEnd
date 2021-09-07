<<<<<<< HEAD
from rest_framework.pagination import PageNumberPagination

from utils.api import APIView
=======
from utils.api import APIView, validate_serializer
>>>>>>> master
from votebd.core.decorators import login_required
from voteEvent.serializers import VoteEventSerializer
from voteEvent.models import VoteEvent
from voteEvent.pagination import PaginationHandlerMixin


# Create your views here.

<<<<<<< HEAD
class BasicPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'
    max_page_size = 10

class VoteEventList(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination
    
    def get(self, request):
        try:
            self.pagination_class.page_size = int(request.data['page_size'])
        except KeyError or ValueError:
            self.pagination_class.page_size = self.pagination_class.page_size
        all_voteEvent = VoteEvent.objects.all()
        page = self.paginate_queryset(all_voteEvent)
        if page is not None:
            serializer = self.get_paginated_response(VoteEventSerializer(page, many = True).data)
        else:
            serializer = VoteEventSerializer(all_voteEvent, many = True)
        return self.success(data = serializer.data)
=======
class VoteEventList(APIView):
    
    def get(self, request):
        voteEvent = VoteEvent.objects.all()
        data = self.paginate_data(request, voteEvent, VoteEventSerializer)
        return self.success(data = data)
>>>>>>> master

    @validate_serializer(VoteEventSerializer)
    @login_required
    def post(self, request):
        serializer = VoteEventSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return self.success(data = serializer.data, status = 201)
        return self.error(msg = serializer.errors, status = 400)

class VoteEventDetail(APIView):

    def get_object(self, pk):
        try:
            return VoteEvent.objects.get(pk = pk)
        except VoteEvent.DoesNotExist:
            return self.error(status = 404)
    
    def get(self, request, pk):
        voteEvent = self.get_object(pk)
        serializer = VoteEventSerializer(voteEvent)
        return self.success(data = serializer.data)

    @login_required
    def put(self, request, pk):
        voteEvent = self.get_object(pk)
        serializer = VoteEventSerializer(voteEvent, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return self.success(data = serializer.data)
        return self.error(msg = serializer.errors, status = 400)

    @login_required
    def delete(self, request, pk):
        voteEvent = self.get_object(pk)
        voteEvent.delete()
<<<<<<< HEAD
        return self.success(status = 204)
        
        
        
=======
        return self.success(status = 204)
>>>>>>> master
