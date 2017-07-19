from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime

# Create your views here.

def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
    if request.session['gold'] < 0:
        request.session['gold'] = 0
    if not 'activities' in request.session:
        request.session['activities'] = []
    return render(request, 'ng/index.html')

def process(request):
    now = datetime.now().strftime('%H:%M %p, %b %d, %Y')
    if request.POST['building'] == 'farm':
        gold = random.randint(10,20)
        request.session['gold'] += gold
        activity = "Found " + str(gold) + " gold from the farm - " + str(now) + "."
        request.session['activities'].append(activity)
    elif request.POST['building'] == 'cave':
        gold = random.randint(5,10)
        request.session['gold'] += gold
        activity = "Found " + str(gold) + " gold from the cave - " + str(now) + "."
        request.session['activities'].append(activity)
    elif request.POST['building'] == 'house':
        gold = random.randint(2,5)
        request.session['gold'] += gold
        activity = "Found " + str(gold) + " gold from the house - " + str(now) + "."
        request.session['activities'].append(activity)
    elif request.POST['building'] == 'casino':
        gold = random.randint(0,50)
        chance = random.randint(1,2)
        if chance == 1:
            request.session['gold'] -= gold
            activity = "Lost " + str(gold) + " gold from the casino - " + str(now) + "."
            request.session['activities'].append(activity)
        else:
            request.session['gold'] += gold
            activity = "Found " + str(gold) + " gold from the casino - " + str(now) + "."
            request.session['activities'].append(activity)
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
