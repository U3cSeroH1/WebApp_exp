from django.contrib import admin


# Register your models here.
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget


class CityAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }