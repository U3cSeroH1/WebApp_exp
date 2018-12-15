from django import forms

from .models import latlng

class latlngForm(forms.ModelForm):
    """ログインフォーム"""



    class Meta:

        model = latlng

        fields = ('lat', 'lng')


class ProfileForm(forms.Form):

    name = forms.CharField()
    age = forms.IntegerField() 