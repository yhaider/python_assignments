from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    return render(request,'sf/index.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['favelang'] = request.POST['favelang']
    request.session['comment'] = request.POST['comment']
    if not 'number' in request.session:
        request.session['number'] = 1
    else:
        request.session['number'] += 1
    return redirect('/result')

def result(request):
    return render(request,'sf/submit.html')
