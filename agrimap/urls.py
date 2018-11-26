from django.urls import path

from . import views

app_name = 'agrimap'
urlpatterns = [
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),

]

