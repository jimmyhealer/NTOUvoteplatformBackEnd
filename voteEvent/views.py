from django.http.request import validate_host
from django.http.response import Http404, HttpResponse

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from votebd.core.decorators import login_required
from announcement.serializers import AnnouncementSerializer
from announcement.models import Announcement
from voteEvent.serializers import VoteEventSerializer
from voteEvent.models import VoteEvent

# Create your views here.

class VoteEventList(APIView):

    def get(self, request):
        all_voteEvent = VoteEvent.objects.all()
        #print(all_voteEvent)
        serializer = VoteEventSerializer(all_voteEvent, many = True)
        return Response(serializer.data)

    @login_required
    def post(self, request):
        serializer = VoteEventSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class VoteEventDetail(APIView):

    def get_object(self, pk):
        try:
            return VoteEvent.objects.get(pk = pk)
        except VoteEvent.DoesNotExist:
            return Http404
    
    def get(self, request, pk):
        voteEvent = self.get_object(pk)
        serializer = VoteEventSerializer(voteEvent)
        return Response(serializer.data)

    @login_required
    def put(self, request, pk):
        voteEvent = self.get_object(pk)
        voteEventSerializer = VoteEventSerializer(voteEvent, data = request.data)
        if voteEventSerializer.is_valid():
            voteEventSerializer.save()
            return Response(voteEventSerializer.data)
        return Response(voteEventSerializer.errors, status = status.HTTP_400_BAD_REQUEST)

    @login_required
    def delete(self, request, pk):
        voteEvent = self.get_object(pk)
        voteEvent.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        
        
        
