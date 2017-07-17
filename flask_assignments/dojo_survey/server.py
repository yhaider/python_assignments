from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods = ['post'])
def result():
    result_name = request.form['name']
    result_location = request.form['location']
    result_favelang = request.form['favelang']
    result_comment = request.form['comment']
    valid = True
    if len(result_name) < 
    return render_template("result.html", name = result_name, location = result_location, favelang = result_favelang, comment = result_comment)

app.run(debug = True)
