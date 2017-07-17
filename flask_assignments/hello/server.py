from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hru')
def hru():
    return render_template('hru.html')

app.run(debug = True)
