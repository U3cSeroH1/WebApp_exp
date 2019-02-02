from django.shortcuts import render

from django.utils import timezone

from django.views import generic

from .models import WeatherDetail, Date

from django.http.response import JsonResponse
import os

from django.http import HttpResponse,Http404

import json
import logging
import re


# Create your views here.



def dateView(request):
    #a={'tinko':'tinkoko','unti':'untiti'}

    d ={
        'datekey': 'text',
        'hourkey': 'htenko',
    }
    return render(request, 'scraping/date_page.html',d)

def hourView(request, p_date):
    #a={'tinko':'tinkoko','unti':'untiti'}
    Date.objects.update_or_create(pub_date = str(p_date))

    d ={
        'datekey': p_date,
        'WeatherDetail': WeatherDetail.objects.filter(target = Date.objects.get(pub_date= p_date)),

    }

    print(WeatherDetail.objects.filter(target = Date.objects.get(pub_date= p_date)))

    return render(request, 'scraping/hour_page.html',d)
