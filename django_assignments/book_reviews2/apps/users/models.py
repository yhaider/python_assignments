from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['namelen'] = "Name must be at least 2 characters."
        elif not re.match('[A-Za-z]+', postData['name']):
            errors['namevalid'] = "Name must only contain letters."
        if len(postData['alias']) < 2:
            errors['aliaslen'] = "Alias must be at least 2 characters."
        if len(postData['email']) < 1:
            errors['emaillen'] = "Email is required."
        elif not re.match('[A-Za-z-0-9-_]+(.[A-Za-z-0-9-_]+)*@[A-Za-z-0-9-_]+(.[A-Za-z-0-9-_]+)*(.[A-Za-z]{2,})', postData['email']):
            errors['emailvalid'] = "Email is not valid."
        elif User.objects.filter(email=postData['email']):
            errors['emailtaken'] = "Email was already registered."
        if len(postData['password']) < 8:
            errors['passlen'] = "Password must be at least 8 characters."
        if postData['password'] != postData['passcon']:
            errors['passcon'] = "Passwords do not match."
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
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
