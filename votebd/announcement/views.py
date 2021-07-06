from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from announcement.models import Announcement
from announcement.serializers import AnnouncementSerializer

@api_view(['GET', 'POST'])
@csrf_exempt
class AnnouncementList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request):
        announcement = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcement, many = True)
        return JsonResponse(serializer.data, safe = False)

    def post(self, request):
        serializer = AnnouncementSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
class AnnouncementDetail(APIView):
    """
    Retrieve, update or delete a code Announcement.
    """
    def get_object(self, pk):
        try:
            return Announcement.objects.get(pk = pk)
        except Announcement.DoesNotExist:
            return Http404

    def get(self, request, pk):
        announcement = self.get_object(pk)
        serializer = AnnouncementSerializer(announcement)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        announcement = self.get_object(pk)
        serializer = AnnouncementSerializer(announcement, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        announcement = self.get_object(pk)
        announcement.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)