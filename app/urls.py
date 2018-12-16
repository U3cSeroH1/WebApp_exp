from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [
    path('', views.ListAndList.as_view(), name='list_and_list'),
    path('create/', views.ListAndCreate.as_view(), name='list_and_create'),
    path('detail/<int:pk>/', views.DetailAndCreate.as_view(), name='detail_and_create'),
]
