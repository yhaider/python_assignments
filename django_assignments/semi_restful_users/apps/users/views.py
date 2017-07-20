from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import *

# Create your views here.
def home(request):
    return redirect('/users')

def index(request):
    context = {
        'users': User.objects.all().values()
    }
    return render(request, 'users/index.html', context)

def new(request):
    return render(request, 'users/new.html')

def create(request):
    User.objects.create(name = request.POST['name'], email = request.POST['email'])
    return redirect('/users')

def show(request, number):
    if request.method == "POST":
        user = User.objects.get(id=number)
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.save()
    context = {
        "user":User.objects.get(id=number)
    }
    return render(request, 'users/show.html', context)

def edit(request,number):
    context = {
        'user': User.objects.get(id=number)
    }
    return render(request, 'users/edit.html', context)


def destroy(request, number):
    User.objects.get(id=number).delete()
    return redirect('/users')
