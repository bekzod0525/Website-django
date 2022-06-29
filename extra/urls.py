from django.urls import path

from .views import gallery_view


app_name = "extra"
urlpatterns = [
    path("gallery/", gallery_view, name="gallery")
]