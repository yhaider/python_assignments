from django.conf.urls import url, include
from . import views           # This line is new!


urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^test$', views.test)
 ]
