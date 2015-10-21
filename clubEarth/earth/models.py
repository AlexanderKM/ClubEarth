from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return "Profile for user %r" % self.user.username

class Event(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    host = models.ForeignKey(Profile, null=True, blank=True)

    def __str__(self):
        return self.name

class Attending(models.Model):
    person = models.ForeignKey(Profile)
    event = models.ForeignKey(Event)

    def __str__(self):
        return "%s is attending %s" % (self.person.user.username, self.event)
