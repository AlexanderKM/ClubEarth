from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username

class Event(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    host = models.ForeignKey(Profile, null=True, blank=True)
    description = models.CharField(max_length=400, default="")
    location1 = models.CharField(max_length=400, default="")
    location2 = models.CharField(max_length=400, default="")
    date = models.CharField(max_length=400, default="")
    start_time = models.CharField(max_length=400, default="")
    end_time = models.CharField(max_length=400, default="")

    def __str__(self):
        return self.name

class Attending(models.Model):
    person = models.ForeignKey(Profile)
    event = models.ForeignKey(Event)

    def __str__(self):
        return "%s is attending %s" % (self.person.user.username, self.event)

class Category(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=140, null=True, blank=True)

    def __str__(self):
        return self.name

class Thread(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=80, null=False, blank=False)
    content = models.CharField(max_length=1000, null=True, blank=True)
    author = models.ForeignKey(Profile, null=True, blank=True)
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return "Title: %s" % self.title

class Comment(models.Model):
    content = models.CharField(max_length=400, null=False, blank=False)
    author = models.ForeignKey(Profile, null=True, blank=True)
    date = models.DateField(default=timezone.now())
    thread = models.ForeignKey(Thread, null=True, blank=True)

    def __str__(self):
        return "Content: %s" % self.content

class EventComment(models.Model):
    author = models.ForeignKey(Profile)
    body = models.CharField(max_length=400, null=False, blank=False)
    event = models.ForeignKey(Event)

    def __str__(self):
        return self.body

class Article(models.Model):
    title = models.CharField(max_length=400)
    url = models.CharField(max_length=400)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


