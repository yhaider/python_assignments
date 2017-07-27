from django.shortcuts import render, redirect
from .models import User
import bcrypt
from datetime import datetime
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'users/index.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag,error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        hashedpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(name = request.POST['name'], alias = request.POST['alias'], email = request.POST['email'], password = hashedpw, created_at = datetime.now(), updated_at = datetime.now())
        request.session['name'] = request.POST['name']
        request.session['alias'] = request.POST['alias']
        request.session['email'] = request.POST['email']
        request.session['id'] = User.objects.get(email=request.POST['email']).id
    return redirect('/books')

def login(request):
    errors = User.objects.loginvalidator(request.POST)
    if len(errors):
        for tag,error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        request.session['name'] = User.objects.get(email=request.POST['email']).name
        request.session['alias'] = User.objects.get(email=request.POST['email']).alias
        request.session['email'] = User.objects.get(email=request.POST['email']).email
        request.session['id'] = User.objects.get(email=request.POST['email']).id
        return redirect('/books')


def users(request,number):
    user = User.objects.get(id=number)
    context = {
        'name': user.name,
        'alias': user.alias,
        'email': user.email,
        'review_count': user.reviews.count()
    }
    return render(request, 'users/users.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')


# Create your views here.
