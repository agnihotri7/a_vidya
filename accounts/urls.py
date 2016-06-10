from django.conf.urls import patterns, url, include
from . import views

urlpatterns = patterns('',
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
)
