from django.contrib import admin

# Register your models here.
from class_discuss_site.models import Group, Course, ForumMessage

admin.site.register(Group)
admin.site.register(Course)
admin.site.register(ForumMessage)