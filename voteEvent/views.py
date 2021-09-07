from utils.api import APIView, validate_serializer
from votebd.core.decorators import login_required
from voteEvent.serializers import VoteEventSerializer
from voteEvent.models import VoteEvent


# Create your views here.

class VoteEventList(APIView):
    
    def get(self, request):
        voteEvent = VoteEvent.objects.all()
        data = self.paginate_data(request, voteEvent, VoteEventSerializer)
        return self.success(data = data)

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
        return self.success(status = 204)