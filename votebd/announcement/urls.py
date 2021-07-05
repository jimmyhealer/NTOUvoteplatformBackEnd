from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from announcement import views

urlpatterns = [
  path('a/', views.Announcement_list),
  path('a/<int:pk>/', views.Announcement_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)