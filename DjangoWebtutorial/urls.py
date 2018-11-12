"""
Definition of urls for DjangoWebtutorial.
"""

from django.contrib import admin
from django.urls import include, path

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('map/', include('agrimap.urls')),
    path('admin/', admin.site.urls),
    path('', include('register.urls')),

]
