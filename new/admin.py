from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import New, Comment

admin.site.register(New)
admin.site.register(Comment)
