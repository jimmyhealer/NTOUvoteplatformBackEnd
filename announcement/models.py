from django.db import models

# Create your models here.
class Announcement(models.Model):

  created = models.DateTimeField(auto_now_add = True)
  title = models.CharField(max_length = 200, blank = True, default = '')
  content = models.TextField(blank = True, default = '')
  #voteEvent = models.ForeignKey(VoteEvent, on_delete = models.CASCADE, default = None)
  # published = models.DateTimeField(blank = True)
  # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  class Meta:
    ordering = ['created']

  def __str__(self):
    return str(self.voteEvent)

  def __unicode__(self):
    return self.title