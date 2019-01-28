from django.contrib import admin


# Register your models here.

from .models import WeatherDetail, Date, Tomorrow


admin.site.register(WeatherDetail)
admin.site.register(Date)
admin.site.register(Tomorrow)
