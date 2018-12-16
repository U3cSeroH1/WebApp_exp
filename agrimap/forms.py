from django import forms

from .models import latlng




class ProfileForm(forms.Form):

    name = forms.CharField()
    age = forms.IntegerField() 