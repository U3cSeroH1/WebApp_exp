import select
import requests
from bs4 import BeautifulSoup
import json
import time
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import WeatherDetail, Tomorrow, Date, test

from django.utils import timezone
import datetime

import random

#from .models import Cdate

def main1(request):
    URL1 = 'http://www.jma.go.jp/jp/amedas_h/yesterday-83401.html?areaCode=&groupCode='
    a={}
    a["kkk"]=uuu(URL1)
    return HttpResponse(a["kkk"])

def main2(request):
    URL2 = 'https://www.jma.go.jp/jp/yoho/350.html'
    b={}
    b["kkk"]=uuu2(URL2)
    return HttpResponse(b["kkk"])

funcs = [main1, main2]    #実行したい関数の集合

def uuu(url):
    s = soup(url)
    soup_td = s.find(id ='div_table')
    return forecast3dict(soup_td)

def uuu2(url):
    s = soup(url)
    soup_td = s.find(class_ = 'forecast')
    return forecastmirai(soup_td)


def soup(url):
    r = requests.get(url)
    html = r.text.encode(r.encoding)
    return BeautifulSoup(html, 'lxml')


#main1

def forecast3dict(soup):
    data={}
    aiue          = soup.select('td')
    for itr in range(0, len(aiue)):
        a = aiue[itr].text.strip()
        if itr >= 12 and itr <= 155 and itr%6 == 0:
            a1=a
        elif itr >= 12 and itr <= 155 and itr%6 == 1:
            a2=a
        elif itr >= 12 and itr <= 155 and itr%6 == 2:
            a3=a
        elif itr >= 12 and itr <= 155 and itr%6 == 3:
            a4=a
        elif itr >= 12 and itr <= 155 and itr%6 == 4:
            a5=a
        elif itr >= 12 and itr <= 155 and itr%6 == 5:
            a6=a


            Date.objects.update_or_create(pub_date = str(timezone.now().date()-timezone.timedelta(days= 1 )))

            WeatherDetail.objects.update_or_create(
                hour=a1,
                target = Date.objects.get(pub_date= str(timezone.now().date()-timezone.timedelta(days= 1 ))),

                defaults={
                    'temperature': a2,
                    'precipitation': a3,
                    'wind_blow': a4,
                    'wind_speed': a5,
                    'day_length': a6,
                },
            )
            


            print(str(timezone.now()))

    test(test=str(random.randint(0, 10000))).save()


    return


#main2

def forecastmirai(soup):
    data={}
    wea           = soup.select('img')
    info          = soup.select('.info')
    rain          = soup.select('.rain')
    temp_min      = soup.select('.temp .min') #なんか.いれないとエラー出る
    temp_max      = soup.select('.temp .max')


    if 5 <= datetime.datetime.today().time().hour < 11:
        for itr in range(0, 8):
            forecast = {}

            a1 = wea[itr]['alt']
            a2 = info[itr].text.strip()
            print('5~11時です')

            a3 = rain[itr+1].text.strip()
            a4 = temp_min[itr].text.strip()
            a5 = temp_max[itr].text.strip()
            if itr == 6 or itr == 7:

                print(itr-6)

                Date.objects.update_or_create(pub_date = str(timezone.now().date()+timezone.timedelta(days= itr-6 )))
                Tomorrow.objects.update_or_create(
                    target = Date.objects.get(pub_date= str(timezone.now().date()+timezone.timedelta(days= itr-6))),

                    defaults={
                        'weather': a1,
                        'info': a2,
                        'rain': a3,
                        'temp_min': a4,
                        'temp_max': a5,
                    },
                )

                print(datetime.datetime.today().time().hour)


    elif 11 <= datetime.datetime.today().time().hour < 17:


        for itr in range(0, 8):
            forecast = {}

            for i in range(0, 4):
                a1 = wea[i+itr]['alt']
                a2 = info[i+itr].text.strip()
                print('11~17時です')

            a3 = rain[itr+1].text.strip()
            a4 = temp_min[itr].text.strip()
            a5 = temp_max[itr].text.strip()
            if itr == 6 or itr == 7:

                print(itr-6)

                Date.objects.update_or_create(pub_date = str(timezone.now().date()+timezone.timedelta(days= itr-6 )))
                Tomorrow.objects.update_or_create(
                    target = Date.objects.get(pub_date= str(timezone.now().date()+timezone.timedelta(days= itr-6))),

                    defaults={
                        'weather': a1,
                        'info': a2,
                        'rain': a3,
                        'temp_min': a4,
                        'temp_max': a5,
                    },
                )

            print(datetime.datetime.today().time().hour)

    else:
        print('17~翌日5時です')
        

if __name__ == '__main__':
    # 佐伯市のその日の一時間ごとの気象情報URL
    funcs



