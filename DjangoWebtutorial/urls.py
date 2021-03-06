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
    path('admin/', admin.site.urls),
    path('', include('register.urls')),
    path('comment/', include('comment.urls')),
    path('scraping/', include('scraping.urls')),

]
