from django import forms
from .models import Choice


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'

        widgets = {
           "question": forms.Select(attrs={'class': "form-control mb-2"}),
           "choice": forms.TextInput(attrs={'class': "form-control mb-2"}) 
        }
    