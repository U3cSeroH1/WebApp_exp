from django.contrib import admin


# Register your models here.

from .models import WeatherDetail, Date, Tomorrow, test


admin.site.register(WeatherDetail)
admin.site.register(Date)
admin.site.register(Tomorrow)

admin.site.register(test)