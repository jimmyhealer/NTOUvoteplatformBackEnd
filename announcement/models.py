from votebd.core.models import User
from django.db import models
import datetime

# Create your models here.
class Announcement(models.Model):

  title = models.CharField(max_length = 200, blank = True, default = '')
  content = models.TextField(blank = True)
  published_date = models.DateTimeField(default = datetime.datetime.now)
  created = models.DateTimeField(auto_now_add = True)
  author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

  class Meta:
    ordering = ['created']

  def __str__(self):
    return str(self.voteEvent)

  def __unicode__(self):
    return self.title