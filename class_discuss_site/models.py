from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    course_id = models.PositiveIntegerField()
    name = models.CharField(max_length=80)
    instructor = models.CharField(max_length=80)
    description = models.CharField(max_length=160)

    def __unicode__(self):
        return self.name


class Discussion(models.Model):
    course = models.ForeignKey(Course, related_name='course+')
    organizer = models.ForeignKey(User, related_name='organizer+')
    name = models.CharField(max_length=80)
    members = models.ManyToManyField(User, related_name='members+')
    location = models.CharField(max_length=40)
    datetime = models.DateTimeField()  # todo: rename to datetime
    size = models.IntegerField()

    def __unicode__(self):
        return self.name


class ForumMessage(models.Model):
    sender = models.ForeignKey(User, related_name='sender+')
    discussion = models.ForeignKey(Discussion, related_name='discussion+')
    text = models.CharField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.message