from django.db import models

# Create your models here.

class VoteEvent(models.Model):

    title = models.CharField(max_length = 1024, blank = True)
    content = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
        
    def __unicode__(self):
        return self.title

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

# class QuestionChoice(models.Model):
    
#     question = models.ForeignKey(Question)
#     choice = models.ForeignKey(Choice)