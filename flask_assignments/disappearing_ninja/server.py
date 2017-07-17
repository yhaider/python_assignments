from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return "No ninjas here."

@app.route('/ninja')
def ninjas():
    return render_template("ninjas.html")

@app.route('/ninja/<ninja_colour>')
def indiv_ninja(ninja_colour):
    print ninja_colour
    return render_template("ninja_indiv.html",colour=str(ninja_colour))


app.run(debug = True)
