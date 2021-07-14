from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, time
from ckeditor.fields import RichTextField


class Question(models.Model):
    title = models.CharField(max_length=255)
    question = RichTextField(blank=True, null=True)
    category = models.CharField(max_length=255, default = 'uncategorised')
    answered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votesscore = models.IntegerField(default='0')
    amountofvotes = models.IntegerField(default='0')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, blank=False, null=True)
    answer = RichTextField(blank=True, null=True)
    answered = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votesscore = models.IntegerField(default='0')
    amountofvotes = models.IntegerField(default='0')
    userUpVotes = models.ManyToManyField(User, blank=True, related_name='threadUpVotes')
    userDownVotes = models.ManyToManyField(User, blank=True, related_name='threadDownVotes')

    def total_likes(self):
        return self.userUpVotes.count() - self.userDownVotes.count()

    def __str__(self):
        return self.question_id.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')



