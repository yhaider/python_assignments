from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors['fnamelen'] = "First name must be at least 2 characters."
        elif not re.match('[A-Za-z]+', postData['fname']):
            errors['fnamevalid'] = "First name must only contain letters."
        if len(postData['lname']) < 2:
            errors['lnamelen'] = "Last name must be at least 2 characters."
        elif not re.match('[A-Za-z]+', postData['lname']):
            errors['lnamevalid'] = "Last name must only contain letters."
        if len(postData['email']) < 1:
            errors['emaillen'] = "Email is required."
        elif not re.match('[A-Za-z-0-9-_]+(.[A-Za-z-0-9-_]+)*@[A-Za-z-0-9-_]+(.[A-Za-z-0-9-_]+)*(.[A-Za-z]{2,})', postData['email']):
            errors['emailvalid'] = "Email is not valid."
        elif User.objects.filter(email=postData['email']):
            errors['emailtaken'] = "Email was already registered."
        if len(postData['password']) < 8:
            errors['passlen'] = "Password must be at least 8 characters."
        if postData['password'] != postData['conpass']:
            errors['passconpass'] = "Passwords do not match."
        return errors
    # This is the registration validator. It runs when the site routes to the
    # '/register' page to determine if everything follows the validations and
    # whether to add user and to proceed to welcome page

    def loginvalidator(self, postData):
        errors = {}
        if len(postData['email']) < 1:
            errors['no_email'] = "Please input an email."
        elif not re.match('[A-Za-z-0-9-_]+(.[A-Za-z-0-9-_]+)*@[A-Za-z-0-9-_]+(.[A-Za-z-0-9-_]+)*(.[A-Za-z]{2,})', postData['email']):
            errors['email_valid'] = "Email is not valid."
        elif not User.objects.get(email=postData['email']):
            errors['email_exist'] = "This email is not registered in our database."
        if len(postData['password']) < 1:
            errors['no_pass'] = "Please input a password."
        elif len(postData['password']) < 8:
            errors['short_pass'] = "Incorrect password: less than 8 characters."
        elif bcrypt.checkpw(postData['password'].encode(), User.objects.get(email=postData['email']).password.encode()) == False:
            errors['incorrect_pass'] = "Incorrect password: does not match password stored in database."
        return errors
    # This is the login validator. It runs when the site routes to the
    # '/login' page after the user has submitted their information.
    # It determines if everything follows the validations and whether
    # to log in the user and present the welcome page


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
# This is the user class which allows us to add in user objects
# with these specific attributes.
