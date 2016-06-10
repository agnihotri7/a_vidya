from django.conf.urls import patterns, url, include
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'),
    url(r'^profiles/$', views.profiles, name='profiles'),
    url(r'^download/$', views.download_csv, name='download'),
)
