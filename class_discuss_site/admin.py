from django.contrib import admin

# Register your models here.
from class_discuss_site.models import Group
from class_discuss_site.models import Course

admin.site.register(Group)
admin.site.register(Course)