from django.db import models
from accounts.models import User

# Create your models here.
class Announcement(models.Model):
  created = models.DateTimeField(auto_now_add = True)
  title = models.CharField(max_length = 200, blank = True, default = '')
  content = models.TextField(blank = True, default = '')
  # published = models.DateTimeField(blank = True)
  # author = models.ForeignKey(User, on_delete = models.CASCADE)

  class Meta:
    ordering = ['created']