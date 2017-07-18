from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'buy/index.html')

def process(request):
    if request.method == "POST":
        print request.POST['id']
        print request.POST['quantity']
        if request.POST['id'] == '1':
            quantity = int(request.POST['quantity'])
            total = quantity * 19.99
            request.session['charge'] = total
        elif request.POST['id'] == '2':
            quantity = int(request.POST['quantity'])
            total = quantity * 29.99
            request.session['charge'] = total
        elif request.POST['id'] == '3':
            quantity = int(request.POST['quantity'])
            total = quantity * 9.99
            request.session['charge'] = total
        elif request.POST['id'] == '4':
            quantity = int(request.POST['quantity'])
            total = quantity * 49.99
            request.session['charge'] = total

        if not 'item_count' in request.session:
            request.session['item_count'] = 0
        count = request.session['item_count']
        count += quantity
        request.session['item_count'] = count

        if not 'totalspent' in request.session:
            request.session['totalspent'] = 0
        totalspent = request.session['totalspent']
        totalspent += total
        request.session['totalspent'] = totalspent

        return redirect('/checkout')
    else:
        return redirect('/')

def checkout(request):
    return render(request, 'buy/checkout.html')
