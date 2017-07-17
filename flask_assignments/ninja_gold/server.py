from flask import Flask, render_template, redirect, request, session
import random
import datetime

app = Flask(__name__)
app.secret_key = "secrets secrets secrets"

@app.route('/')
def index():
    if "gold" not in session:
        session['gold'] = 0
        session['activities']
    return render_template('index.html')

@app.route('/process_money', methods = ['POST'])
def process():
    now = datetime.datetime.now()
    if request.form['building'] == 'farm':
        gold_earned = random.randrange(10, 21)
        session['gold'] += gold_earned
        activity = "<p style='color:green;'> Earned " + str(gold_earned) + " gold at the farm. (" + str(now) + ") </p>"
        session['activities'].append(activity)

    if request.form['building'] == 'cave':
        gold_earned = random.randrange(5,11)
        session['gold'] += gold_earned
        activity = "<p style='color: green;'>Earned " + str(gold_earned) + " gold at the cave.(" + str(now) + ") </p>"
        session['activities'].append(activity)

    if request.form['building'] == 'house':
        gold_earned = random.randrange(2,6)
        session['gold'] += gold_earned
        activity = "<p style='color:green;'> Earned " + str(gold_earned) + " gold at the house.(" + str(now) + ") </p>"
        session['activities'].append(activity)

    if request.form['building'] == 'casino':
        gold_earned = random.randrange(0, 51)
        chance = random.randint(1,3)
        if chance == 1:
            session['gold'] += gold_earned
            activity = "<p style='color:green;'> Earned " + str(gold_earned) + " gold at the casino.(" + str(now) + ") </p>"
            session['activities'].append(activity)
        elif chance == 2:
            session['gold'] -= gold_earned
            activity = "<p style='color:red;'> Lost " + str(gold_earned) + " gold at the casino.(" + str(now) + ") </p>"
            session['activities'].append(activity)
    return redirect('/')

@app.route('/reset')
def reset():
    session['activities'] =[]
    session['gold'] = 0
    return redirect('/')

app.run(debug = True)
