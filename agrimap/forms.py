from django import forms

class latlngForm(forms.Form):
    """ログインフォーム"""

    lat = forms.IntegerFieldField()
    lng = forms.IntegerFieldField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
