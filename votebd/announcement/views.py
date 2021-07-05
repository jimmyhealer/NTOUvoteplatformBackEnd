import announcement
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from announcement.models import Announcement
from announcement.serializers import AnnouncementSerializer

@api_view(['GET', 'POST'])
@csrf_exempt
def Announcement_list(request, format = None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        announcement = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcement, many = True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        serializer = AnnouncementSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def Announcement_detail(request, pk, format = None):
    """
    Retrieve, update or delete a code Announcement.
    """
    try:
        announcement = Announcement.objects.get(pk = pk)
    except Announcement.DoesNotExist:
        return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnnouncementSerializer(announcement)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = AnnouncementSerializer(announcement, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Announcement.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)