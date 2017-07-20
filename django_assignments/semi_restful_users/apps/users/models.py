from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "User name should be at least two characters."
        if len(postData['email']) < 1:
            errors['email'] = "Please enter a valid email."
        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()
