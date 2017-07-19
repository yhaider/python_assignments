from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class UsersManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}
#         if len(postData['first_name']) < 2:
#             errors['first_name'] = "First name must be at least two characters."
#         if len(postData['last_name']) < 2:
#             errors['last_name'] = "Last name must be at least two characters."
#         if postData['age'] < 13 or postData['age'] > 105:
#             errors['age'] = "Age must be at least 13 and no more than 105."
#         return errors


class Users(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # usersManager = UsersManager()
    def __repr__(self):
        return "<Users object: {} {} {} {}".format(self.first_name, self.last_name, self.email, self.age)
