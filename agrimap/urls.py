from django.urls import path

from . import views

app_name = 'agrimap'
urlpatterns = [
    path('', views.index, name='index'),

]