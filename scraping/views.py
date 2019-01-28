from django.shortcuts import render

from django.utils import timezone

from django.views import generic

from .models import WeatherDetail, Date



# Create your views here.
def dateView(request, p_date):
    #a={'tinko':'tinkoko','unti':'untiti'}

    field_value = []

    print(p_date)

    for i in range(1,25):
        print(i)


        obj = WeatherDetail.objects.get(hour = i,target = Date.objects.get(pub_date= p_date))
        field_object = WeatherDetail._meta.get_field('hour')

        field_value.append(field_object.value_from_object(obj))

        print(field_value)

    d ={
        'datekey': p_date,
        'hourkey': field_value,
    }
    return render(request, 'scraping/date_page.html',d)

def hourView(request, p_date, p_hour):
    #a={'tinko':'tinkoko','unti':'untiti'}

    field_value = []

    WeatherDetail.objects.get(hour = p_hour, target = Date.objects.get(pub_date= p_date))

    print(p_hour)


    d ={
        'forecast': WeatherDetail.objects.get(hour = p_hour, target = Date.objects.get(pub_date= p_date)),
    }
    return render(request, 'scraping/hour_page.html',d)




