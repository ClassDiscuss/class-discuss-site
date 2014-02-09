from django.contrib import admin

# Register your models here.
from class_discuss_site.models import Discussion, Course, ForumMessage

admin.site.register(Discussion)
admin.site.register(Course)
admin.site.register(ForumMessage)