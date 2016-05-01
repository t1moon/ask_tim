from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    added_at = models.DateTimeField(default=datetime.datetime.now)
    author = models.ForeignKey(User)
    rating = models.IntegerField(default=0)