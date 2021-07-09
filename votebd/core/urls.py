from django.urls import path, include

urlpatterns = [
  path("auth/", include("votebd.core.auth")),
]