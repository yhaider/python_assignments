from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
        # This is the homepage view of adding courses
        # and showing courses
    url(r'^add$', views.add),
        # This adds the new course into the database
        # In the views.py file you can see that it has
        # all necessary validations
    url(r'^drop/(?P<number>\d+)$', views.drop),
        # This brings the user to the drop confirmation page
        # I was messing around with triggering a modal, and
        # that functionality is not yet complete
    url(r'^course/(?P<number>\d+)$', views.comment),
        # This brings the user to the comments page for
        # each individual class.
        # Here a user can add their comments to the page
        # anonymously, but there are limitations and
        # validations that require the comment to be at
        # least 10 characters
    url(r'^addcomm/(?P<number>\d+)$', views.addcomm),
        # This method adds comments into the database and
        # redirects user back to the comments page so they
        # can now see their comment
    url(r'^delete/(?P<number>\d+)$', views.delete),
        # This is the method that deletes a comment
        # Glyphicon is currently a cloud; will change
        # to something more appropriate
    url(r'^process/(?P<number>\d+)$', views.process),
        # This method actually drops the class once the
        # user confirms drop
    #  url(r'^modal/(?P<number>\d+)$', views.modal)
        # the above commented out url is functionality
        # I am still working on
]
