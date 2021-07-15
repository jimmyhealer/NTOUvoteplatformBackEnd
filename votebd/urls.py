from voteEvent.models import VoteEvent
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include('announcement.urls')),
    path('vote/', include('voteEvent.urls')),
    path('auth/', include('votebd.core.auth')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]