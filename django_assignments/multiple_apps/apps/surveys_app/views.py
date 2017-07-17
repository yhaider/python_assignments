from django.shortcuts import render,HttpResponse, redirect

# Create your views here.

def index(request):
    response = "Placeholder to display all surveys created."
    return HttpResponse(response)

def new(request):
    response = "Placeholder for users to add a new survey."
    return HttpResponse(response)
