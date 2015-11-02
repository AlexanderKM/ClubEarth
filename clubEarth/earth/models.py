from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return "Profile for user %r" % self.user.username

class Event(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    host = models.ForeignKey(Profile, null=True, blank=True)
    description = models.CharField(max_length=400, default="")
    date = models.DateField(default=timezone.now())
    start_time = models.TimeField(default=timezone.now())
    end_time = models.TimeField(default=timezone.now())

    def __str__(self):
        return self.name

class Attending(models.Model):
    person = models.ForeignKey(Profile)
    event = models.ForeignKey(Event)

    def __str__(self):
        return "%s is attending %s" % (self.person.user.username, self.event)

class Thread(models.Model):
    category = models.CharField(max_length=400, null=False, blank=False)
    title = models.CharField(max_length=80, null=False, blank=False)
    author = models.ForeignKey(Profile, null=True, blank=True)
    date = models.DateField(default=timezone.now())

class Comment(model.Model):
    content = models.CharField(max_length=400, null=False, blank=False)
    author = models.ForeignKey(Profile, null=True, blank=True)
    date = model.DateField(default=timezone.now())
    thread = models.ForeignKey(Thread, null=True, blank=True)


