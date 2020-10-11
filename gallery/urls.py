from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='gallery-home'),
    url('^search/', views.search, name='search'),
    url('^location/(?P<locale>\w+)/', views.location, name='location'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
