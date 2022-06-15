from django.urls import path

from .views import (
    create_question, 
    groups_add, 
    savol_detail,
    savollar,
    check_answer,
    create_question, 
    group, 
    remove_group,
    edit_group,
    create_choice
    )

app_name = 'poll'
urlpatterns = [
    path('', savollar, name='savollar'),
    path('savol/<int:id>/', savol_detail, name='savol'),
    path('check/<int:variant_id>/', check_answer, name='check_answer'),
    path('create_question/',  create_question, name='create'),
    path('groups_add/',  groups_add, name='add'),
    path('groups/',  group, name='groups'),
    path('remove-group/<int:id>/', remove_group, name="remove_group"),
    path('edti-group/<int:id>/', edit_group, name="edit_group"),
    path('tanlov-yaratish/',  create_choice, name='create_choice'),

]
