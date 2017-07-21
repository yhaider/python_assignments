from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    # Navigates to homepage
    # where there are login
    # and registration forms

    url(r'^login$', views.login),
    # Processes login with validations
    # Either proceeds to success page or
    # displays messages as dismissable alerts

    url(r'^register$', views.register),
    # Processes registration with validations
    # Either proceeds to success page or
    # displays messages as dismissable alerts

    url(r'^success$', views.success),
    # Displays a welcome message with user's
    # name and a back button
]
