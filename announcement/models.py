from votebd.core.models import User
from django.db import models
import datetime

# Create your models here.
class Announcement(models.Model):

  created = models.DateTimeField(auto_now_add = True)
  title = models.CharField(max_length = 200, blank = True, default = '')
  # voteEvent = models.ForeignKey(VoteEvent, on_delete = models.CASCADE, default = None)
  published_date = models.DateTimeField(default = datetime.datetime.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
  content = models.TextField(blank = True)

  class Meta:
    ordering = ['created']

  def __str__(self):
    return str(self.voteEvent)

  def __unicode__(self):
    return self.title