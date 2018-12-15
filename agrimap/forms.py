
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget


class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ("coordinates", "city_hall")
        widgets = {
            'coordinates': GooglePointFieldWidget,
            'city_hall': GoogleStaticOverlayMapWidget,
        }