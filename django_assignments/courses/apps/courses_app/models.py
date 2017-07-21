from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 10:
            errors['name'] = "The course name must be at least 10 characters."
        if len(postData['desc']) < 15:
            errors['desc'] = "The course description must be at least 15 characters."
        return errors
# The above class allows me to have validations
# when a user is adding a course


class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = CourseManager()
# This is the actual course class which allows me to add
# into the database

class CommentManager(models.Manager):
    def com_val(self, postData):
        errors = {}
        if len(postData['comment']) < 10:
            errors['comm'] = "Comments must be at least 10 characters."
        return errors
# This manager gives me ability to have validations for
# comments

class Comment(models.Model):
    comment = models.TextField(max_length=255)
    objects = CommentManager()
    course = models.ForeignKey(Course, related_name = "comments")
# The comment class allows me to place comments into
# database. One to Many relationship between course and
# comments.
