from django.shortcuts import render, redirect
from django.contrib import messages
from models import User, UserManager
import bcrypt


def index(request):
    return render(request, 'lr/index.html')
    # Simply renders the template for login/registration forms

def login(request):
    errors = User.objects.loginvalidator(request.POST)
    if len(errors):
        for tag,error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        request.session['name'] = User.objects.get(email=request.POST['email']).first_name
        return redirect('/success')
    # If there are errors, they will display as dismissable alerts
    # on the homepage, otherwise it will proceed and login in the user

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag,error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else:
        pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], email = request.POST['email'], password = pwhash)
        request.session['name'] = request.POST['fname']
        return redirect('/success')
    return redirect('/')
    # If there are errors, they will display as dismissable alerts
    # on the homepage, otherwise it will proceed, add, and welcome the user


def success(request):
    return render(request, 'lr/success.html')
    # Simply displays the welcome page once
    # a successful login or registration has
    # taken place
