from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^amadon$', views.index),
    url(r'^process$', views.process),
    url(r'^checkout$', views.checkout)
]
