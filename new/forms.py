import django


from django import forms

from .models import New


class  NewForm(forms.ModelForm):
    class Meta:
        model = New
        exclude = ['created']


class  NewFormMine(forms.ModelForm):
    class Meta:
        model = New
        exclude = ['author', 'created']
