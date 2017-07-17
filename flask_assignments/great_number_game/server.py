from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = 'secrety_secrets'


@app.route('/')
def index():
    print "I'm picking my number..."
    session['actual'] = int(random.randrange(0,101))
    print session['actual']
    print "Ok, got it. Ready for your defeat?"
    return render_template('index.html')


@app.route('/checking', methods = ['POST'])
def checking():
    guess = int(request.form['guess'])
    status = "none"
    if guess > session['actual']:
        status = "high"
    elif guess < session['actual']:
        status = "low"
    elif guess == session['actual']:
        status = "correct"
    return render_template('checking.html', status = status, guess = request.form['guess'])

@app.route('/reset')
def reset():
    session.pop('actual')
    return redirect('/')

app.run(debug = True)
