from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include('announcement.urls')),
    path('', include('accounts.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]