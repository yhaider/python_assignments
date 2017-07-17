from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if not 'count' in request.session:
        request.session['count'] = 1
    content = {
        'string': get_random_string(length=14),
    }
    return render(request,'rwg/index.html', content)
    
def process(request):
    request.session['count'] += 1
    return redirect('/')

def reset(request):
    del request.session['count']
    return redirect('/')
