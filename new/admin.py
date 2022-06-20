from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import New, Comment

@admin.register(New)
class NewAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')

    
admin.site.register(Comment)
