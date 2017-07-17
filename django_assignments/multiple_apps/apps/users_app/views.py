from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "home"
    return HttpResponse(response)
    
def register(request):
    response = "placeholder for users to register"
    return HttpResponse(response)

def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)

def users(request):
    response = "placeholder to display all users"
    return HttpResponse(response)
