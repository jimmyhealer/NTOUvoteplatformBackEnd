from django.utils import timezone
from django.db import models
from votebd.core.models import User

# Create your models here.

class VoteEvent(models.Model):

    title = models.CharField(max_length = 1024, blank = True)
    content = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    startTime = models.DateTimeField(default = timezone.now)
    endTime = models.DateTimeField(default = timezone.now)
    isPublish = models.BooleanField(default = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, default = None)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
        
    def __unicode__(self):
        return self.title
    
    def publish_post(self):
        self.isPublish = True
        return self.isPublish

class Question(models.Model):

    title = models.CharField(max_length = 128, blank = True)
    voteEvent = models.ForeignKey(VoteEvent, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class Choice(models.Model):

    choice_text = models.CharField(max_length = 128)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text

    def __unicode__(self):
        return self.choice_text