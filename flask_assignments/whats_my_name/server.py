from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    print "Received information successfully."
    your_name = request.form['your_name']
    print your_name
    return redirect('/')

app.run(debug = True)
