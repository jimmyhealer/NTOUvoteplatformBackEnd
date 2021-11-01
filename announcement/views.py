from announcement.models import Announcement
from announcement.serializers import AnnouncementSerializer, AnnouncementSubmitSerializer, AnnouncementDetailSerializer

from votebd.core.decorators import login_required
from utils.api import APIView, validate_serializer

class AnnouncementList(APIView):
    """
    List all code snippets, or create a new snippet.
    """
    def get(self, request):
        announcement = Announcement.objects
                        .filter(published_date__lte = timezone.now()).order_by('-published_date')
        data = self.paginate_data(request, announcement, AnnouncementSerializer)
        return self.success(data = data)

    @validate_serializer(AnnouncementSubmitSerializer)
    @login_required
    def post(self, request):
        serializer = AnnouncementSubmitSerializer(data = request.data)
        serializer.save(author = request.user)
        return self.success(data = serializer.data, status = 201)


class AnnouncementDetail(APIView):
    """
    Retrieve, update or delete a code Announcement.
    """
    def get_object(self, pk):
        try:
            return Announcement.objects.get(pk = pk)
        except Announcement.DoesNotExist:
            return self.error(status = 404)

    def get(self, request, pk, format = None):
        announcement = self.get_object(pk)
        serializer = AnnouncementDetailSerializer(announcement)
        return self.success(data = serializer.data)

    @login_required
    def put(self, request, pk, format = None):
        announcement = self.get_object(pk)
        serializer = AnnouncementDetailSerializer(announcement, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return self.success(data = serializer.data)
        return self.error(msg = serializer.errors, status = 400)

    @login_required
    def delete(self, request, pk, format = None):
        announcement = self.get_object(pk)
        announcement.delete()
        return self.success(status = 204)