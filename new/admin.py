from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import New, Comment, Like, Dislike

@admin.register(New)
class NewAdmin(SummernoteModelAdmin):
    summernote_fields = ('body')

    
admin.site.register(Comment)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(Dislike)
class DislikeAdmin(admin.ModelAdmin):
    pass