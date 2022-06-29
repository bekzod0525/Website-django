from django.urls import path
from .views import (
    my_detail,
    news_list,
    news_detail, 
    create, 
    remove, 
    my_news, 
    my_create, 
    my_update,
    my_detail, 
    like,
    dislike   
)

app_name = 'new'
urlpatterns = [
    path('', news_list, name='list'),
    path('detail/<int:id>/', news_detail, name='detail'),
    path('yaratish/', create, name='create'),
    path('remove/<int:id>/', remove, name='remove'),   
    path('my-news/', my_news, name='my_news'),
    path('my-create/', my_create, name='my_create'),
    path('my-update/<int:id>/', my_update, name='my_update'), 
    path('my-detail/<int:id>/',  my_detail, name='my_detail'),
    path('like/<int:id>/',  like, name='like'),
    path('dislike/<int:id>/',  dislike, name='dislike'),
]
