from flask import Flask, render_template, request, session,redirect

app = Flask(__name__)
app.secret_key = 'this_is_a_secret_key' #this is to use session

@app.route('/')
def index():
    try: #this says to add one to {{session['times']}}
        session['times'] += 1
    except:
        session['times'] = 1 #...unless it is the first time
    return render_template("index.html")

@app.route('/add2', methods = ['POST'])
def plustwo():
    print 'adding two...'
    session['times'] += 1
    #have to add only one because it redirects to '/' and will otherwise add too many
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    print 'resetting...'
    session['times'] = 0
    return redirect('/')

app.run(debug = True)
