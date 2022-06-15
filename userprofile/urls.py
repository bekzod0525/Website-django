from django.urls import path

from .views import register, login_view, profile, logout_view

app_name = "userprofile"
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
     path('logout/', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
]