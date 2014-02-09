from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    course_id = models.PositiveIntegerField()
    name = models.CharField(max_length=70)
    instructor = models.CharField(max_length=70)
    description = models.CharField(max_length=210)
    def __unicode__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=70)
    location = models.CharField(max_length=50)
    organizer = models.ForeignKey(User, related_name='organizer+')
    attendees = models.ManyToManyField(User, related_name='attendees+')
    time = models.DateTimeField() # todo: rename to datetime
    course = models.ForeignKey(Course, related_name='course+')
    size = models.IntegerField()
    def __unicode__(self):
        return self.name