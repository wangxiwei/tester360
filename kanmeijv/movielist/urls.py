from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^hdtv/', views.HDTVView.as_view(), name='hdtv'),
    url(r'^save_url/', views.save_url, name='hdtv'),
]