from django.urls import path
from . import views
from . import sku

app_name = 'scraping'
urlpatterns = [
    path('', sku.main1, name='saiki'),
    path('mirai/', sku.main2, name='mirai'),
    path('forecast/',views.dateView,name='date_page'),
    path('forecast/<slug:p_date>/',views.hourView,name='hour_page'),
]

