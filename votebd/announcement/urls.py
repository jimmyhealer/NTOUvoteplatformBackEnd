from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from announcement import views

urlpatterns = [
  path('a/', views.AnnouncementList.as_view()),
  path('a/<int:pk>/', views.AnnouncementDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)