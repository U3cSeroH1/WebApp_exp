"""
Definition of urls for DjangoWebtutorial.
"""

from django.contrib import admin
from django.urls import include, path

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),

]
