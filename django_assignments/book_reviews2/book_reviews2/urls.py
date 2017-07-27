from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.books.urls')),
    url(r'^', include('apps.users.urls')),
]
