from django.shortcuts import render, redirect
from django.contrib import messages
from models import *


def index(request):
    context = {
        'courses': Course.objects.all().values()
    }
    return render(request, 'courses_app/index.html', context)
    # Just the homepage; context pulls course info to be
    # called in template

def add(request):
    errors = Course.objects.validator(request.POST)
    if len(errors):
        for tag,error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else:
        Course.objects.create(name = request.POST['name'], desc = request.POST['desc'])
    return redirect('/')
    # Validates that the course name is at least 10 characters
    # and if not, messages will flash; else, will be added
    # to the database and then redirect to home where new
    # class will be visible now

def drop(request, number):
    context = {
        "course": Course.objects.get(id=number)
    }
    return render(request, 'courses_app/drop.html', context)
    # This pulls the course number from the index template
    # and then uses the number in the url to identify the course
    # so its specific information can be pulled onto this template

#***********************************
# def modal(request,number):
#     request.session.trigger = True
#     request.session.classinfo = Course.objects.get(id=number)
#     return redirect('/')
#***********************************
    #The above is functionality that
    #I am still working out

def process(request, number):
    Course.objects.get(id=number).delete()
    return redirect('/')
    # Uses number pulled from url to grab that course's database
    # and delete it from database to then redirect to home and see changes

def comment(request, number):
    context = {
        'course': Course.objects.get(id=number),
        'comments': Course.objects.get(id=number).comments.all()
    }
    return render(request, 'courses_app/comments.html', context)
    # This is the comments page. Pulls comments and course info
    # from the number in the url which is course id

def addcomm(request,number):
    errors = Comment.objects.com_val(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else:
        newcomm = request.POST['comment']
        Comment.objects.create(comment = newcomm, course = Course.objects.get(id=number))
    return redirect('/course/{}'.format(number))
    # Method checks that submitted comment is valid (at least
    # 10 characters) and if so, adds to database and redirects
    # to the course's comment page; else it flashes messages


def delete(request,number):
    Comment.objects.get(id=number).delete()
    return redirect('/')
    # Method just deletes comment from database and redirects to
    # main page
