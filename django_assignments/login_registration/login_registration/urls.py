from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.lr.urls')),
    # There is just one app, so we want everything
    # to route to that specific app, hence just the
    # '^' with no closing '$'
]
