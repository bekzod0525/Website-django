from dataclasses import fields
import django


from django import forms

from .models import New, Comment


class  NewForm(forms.ModelForm):
    class Meta:
        model = New
        exclude = ['created']


class  NewFormMine(forms.ModelForm):
    class Meta:
        model = New
        exclude = ['author', 'created']

class  CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
