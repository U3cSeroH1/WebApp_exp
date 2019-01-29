import datetime
from django.db import models
from django.utils import timezone


class Date(models.Model):
    
    pub_date = models.CharField('date published', max_length=200 , default = timezone.now().date())

    def __str__(self):
        return self.pub_date

# Create your models here.


def get_or_create_date():
    date, _ = Date.objects.get_or_create(pub_date=timezone.now().date())
    return date

class WeatherDetail(models.Model):
    
    hour = models.CharField(max_length=4)
    temperature = models.CharField(max_length=8)
    precipitation = models.CharField(max_length=4)
    wind_blow = models.CharField(max_length=4)
    wind_speed = models.CharField(max_length=4)
    day_length = models.CharField(max_length=4)
    target = models.ForeignKey(Date, on_delete=models.CASCADE, default = get_or_create_date)


    def __str__(self):
        return  str(self.target)+ '/' + self.hour + '時'


def get_or_create_date():
    date, _ = Date.objects.get_or_create(pub_date=timezone.now().date())
    return date

class Tomorrow(models.Model):

    weather = models.CharField(max_length=16)
    info = models.CharField(max_length=64)
    rain = models.CharField(max_length=64)
    temp_min = models.CharField(max_length=4)
    temp_max = models.CharField(max_length=4)
    target = models.ForeignKey(Date, on_delete=models.CASCADE, default = get_or_create_date)

    def __str__(self):
        return str(self.target)


class test(models.Model):

    test = models.CharField(max_length=100)

    def __str__(self):
        return self.test