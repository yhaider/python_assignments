from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.

def sw(request):
    return render(request, 'sw/sw.html')

def add(request):
    if request.method == "POST":
        date = datetime.now().strftime('%I:%M%p, %b %d, %Y')
        info = {
            'word': request.POST['word'],
            'color': request.POST['color'],
            'big': request.POST['big'],
            'time': str(date)
        }

        if not 'list' in request.session:
            request.session['list'] = []
        saved_list = request.session['list']
        saved_list.append(info)
        request.session['list'] = saved_list
        print request.session['list']
    return redirect('/sw')

def clear(request):
    request.session.clear()
    return redirect('/')
