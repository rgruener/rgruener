from django.conf.urls import patterns, url

from personalsite import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^research/$', views.research, name='research'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^contact/$', views.contact, name='contact'),
)
