from django.urls import path

from . import views

app_name = 'agrimap'
urlpatterns = [
    path('detail/', include('agrimap.urls', namespace='agrimap')),

]

