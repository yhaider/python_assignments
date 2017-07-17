from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
from validate_email import validate_email
import bcrypt


app = Flask(__name__)
app.secret_key = "key"
mysql = MySQLConnector(app, 'users_login_regis')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def register():
    valid = True
    query = "SELECT * FROM users WHERE email = :email"
    data = {'email': request.form['email']}
    email_check = mysql.query_db(query,data)
    if email_check:
        valid = False
        flash('Error: Email already registered!')
    if len(request.form['first_name']) < 2:
        valid = False
        flash('Error: First name not valid! Length is less than 2 characters.')
    if len(request.form['last_name']) < 2:
        valid = False
        flash('Error: Last name not valid! Length is less than 2 characters.')
    if not validate_email(request.form['email']):
        valid = False
        flash('Error: Email not valid!')

    if len(request.form['password']) < 8:
        valid = False
        flash('Error: Password is not 8 characters!')
    if request.form['password'] != request.form['pass_con']:
        valid = False
        flash('Error: Passwords do not match!')
    if valid == False:
        return redirect('/')
    elif valid == True:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        hashedpw = bcrypt.hashpw(request.form['password'].encode('utf8'), bcrypt.gensalt())
        data = {
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'password': hashedpw
        }
        mysql.query_db(query, data)
        return redirect('/success_registration')

@app.route('/login', methods=['POST'])
def login():
    data = {'email' : request.form['email']}
    user = mysql.query_db("SELECT * FROM users WHERE users.email = :email", data)
    if len(user) != 0:
        if bcrypt.checkpw(request.form['password'].encode('utf8'), user[0]['password'].encode('utf8')):
            session['name'] = user[0]['first_name']
            return redirect('/success_login')
        else:
            flash('Error: Incorrect password!')
            return redirect('/')
    else:
        flash('Error: Incorrect or Invalid email!')
        return redirect('/')

@app.route('/success_registration')
def success_reg():
    return render_template('success_registration.html')

@app.route('/success_login')
def success_login():
    return render_template('success_login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have logged out!')
    return redirect('/')

app.run(debug = True)
