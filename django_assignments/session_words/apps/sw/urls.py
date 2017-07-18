from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sw),
    url(r'^sw/$', views.sw),
    url(r'^sw/add$', views.add),
    url(r'^sw/clear', views.clear)
]
