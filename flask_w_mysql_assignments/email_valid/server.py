from flask import Flask, render_template, request, redirect, session
from mysqlconnection import MySQLConnector
from validate_email import validate_email # this is an additional python module to validate emails at three different levels
from datetime import datetime

app = Flask(__name__)
mysql = MySQLConnector(app, 'email_valid')
app.secret_key = 'secrets'

@app.route('/')
def index():
    if 'valid' not in session:
        session['valid'] = True
    print session['valid']
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    if not validate_email(request.form['email']):
        session['valid'] = False
        return redirect('/')
    elif validate_email(request.form['email']):
        session['valid'] = True
        session['email_address'] = request.form['email']
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
                'email': request.form['email']
        }
        mysql.query_db(query, data)
        return redirect('/success')

@app.route('/success')
def success():
    query = "SELECT * FROM emails"
    email_db = mysql.query_db(query)
    return render_template('success.html', emails = email_db, email_address = session['email_address'])

app.run(debug = True)
