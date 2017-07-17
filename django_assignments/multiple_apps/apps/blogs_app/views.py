from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    placeholder = "This is a placeholder to later display all blogs."
    return HttpResponse(placeholder)

def new(request):
    response = "This is a placeholder to display a new form to create a new blog."
    return HttpResponse(response)

def create(request):
    return redirect ('/blogs')

def show(request, number = "1"):
    response = "Placeholder for blog number ", number
    return HttpResponse(response)

def edit(request, number = "1"):
    response = "Placeholder for blog number ",number, " to be edited"
    return HttpResponse(response)

def delete(request, number = "1"):
    response = "Placholder for blog number ", number," to be deleted."
    return HttpResponse(response)

def createform(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")
