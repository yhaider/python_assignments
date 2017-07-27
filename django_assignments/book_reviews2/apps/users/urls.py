from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^users/(?P<number>\d+)$', views.users),
    url(r'^logout$', views.logout)
]
