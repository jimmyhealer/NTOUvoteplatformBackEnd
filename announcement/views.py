from rest_framework import status
# from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from announcement.models import Announcement
from announcement.serializers import AnnouncementSerializer

from votebd.core.decorators import login_required

from utils.api import APIView

class AnnouncementList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request, format = None):
        announcement = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcement, many = True)
        return self.success(serializer.data)

    @login_required
    def post(self, request, format = None):
        serializer = AnnouncementSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class AnnouncementDetail(APIView):
    """
    Retrieve, update or delete a code Announcement.
    """
    def get_object(self, pk):
        try:
            return Announcement.objects.get(pk = pk)
        except Announcement.DoesNotExist:
            return Http404

    def get(self, request, pk, format = None):
        announcement = self.get_object(pk)
        serializer = AnnouncementSerializer(announcement)
        return Response(serializer.data)

    @login_required
    def put(self, request, pk, format = None):
        announcement = self.get_object(pk)
        serializer = AnnouncementSerializer(announcement, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    @login_required
    def delete(self, request, pk, format = None):
        announcement = self.get_object(pk)
        announcement.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)