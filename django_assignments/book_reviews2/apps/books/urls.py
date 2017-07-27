from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^books$', views.home),
    url(r'^books/add$', views.add),
    url(r'^processadd$', views.process),
    url(r'^books/(?P<number>\d+)', views.book),
]
