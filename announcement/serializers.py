from rest_framework import serializers
from announcement.models import Announcement
from votebd.core.serializers import UserSerializers

class AnnouncementSerializer(serializers.ModelSerializer): 

  author = UserSerializers()

  class Meta:
    model = Announcement
    fields = ['id', 'title', 'author', 'published_date']

class AnnouncementSubmitSerializer(serializers.ModelSerializer): 

  class Meta:
    model = Announcement
    fields = ['id', 'title', 'content', 'published_date']

class AnnouncementDetailSerializer(serializers.ModelSerializer):

  author = UserSerializers()

  class Meta:
    model = Announcement
    fields = ['id', 'title', 'author', 'published_date', 'content']