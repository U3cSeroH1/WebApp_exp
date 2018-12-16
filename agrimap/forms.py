from django import forms

from .models import latlng

class latlngForm(forms.ModelForm):
    """ログインフォーム"""



    class Meta:

        model = latlng

        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ProfileForm(forms.Form):

    name = forms.CharField()
    age = forms.IntegerField() 