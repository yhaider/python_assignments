from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'full_friends')

@app.route('/')
def index():
    query = "SELECT * FROM friends"
    full_friends = mysql.query_db(query)
    return render_template("index.html", friends = full_friends)

@app.route('/add', methods = ['POST'])
def add():
    query = "INSERT INTO friends (name, age, created_at, updated_at) VALUES (:name, :age, NOW(), NOW())"
    data = { 'name': request.form['name'],
            'age': request.form['age']
    }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
