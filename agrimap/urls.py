from django.urls import path

from . import views

app_name = 'agrimap'
urlpatterns = [
    path('detail/', views.detail, name='detail'),

]

