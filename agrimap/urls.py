from django.urls import path

from . import views

app_name = 'agrimap'
urlpatterns = [
    path('', views.index, name='index'),
    path('user_map/<int:pk>/', views.UserMap.as_view(), name='user_map'),

]

