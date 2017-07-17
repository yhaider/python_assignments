from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from validate_email import validate_email
import re
import bcrypt
from datetime import datetime, date, timedelta


app = Flask(__name__)
app.secret_key = 'the wall is a secret'
mysql = MySQLConnector(app, 'the_wall')

@app.route('/')
def index():
    if session and session.has_key('id'):
        return redirect('/wall')
    else:
        return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/process/login', methods = ['POST'])
def login_check():
    data = {'email' : request.form['email']}
    user = mysql.query_db("SELECT * FROM users WHERE users.email = :email", data)
    if len(user) != 0:
        if bcrypt.checkpw(request.form['password'].encode('utf8'), user[0]['password'].encode('utf8')):
            session['name'] = user[0]['first_name']
            session['id']= user[0]['id']
            session['email'] = user[0]['email']
            session['last'] = user[0]['last_name']
            return redirect('/wall')
        else:
            flash('Error: Incorrect password!')
            return redirect('/login')
    else:
        flash('Error: Incorrect or Invalid email!')
        return redirect('/login')
    return redirect('/wall')

@app.route('/process/register', methods = ['POST'])
def registration_check():
    valid = True
    info = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password']
    }
    query = "SELECT * FROM users WHERE email = :email"
    emaildata = {'email': request.form['email']}
    email_check = mysql.query_db(query,emaildata)
    if email_check:
        valid = False
        flash('Error: Email already registered.')
    if not validate_email(request.form['email']):
        flash('Please input a valid email.')
    for key in info:
        if len(info[key]) < 1:
            flash('Please input' + info[key] + '.')
            valid = False
    if 1 <= len(info['password']) < 8:
        flash('Please input a password of at least 8 characters.')
        valid = False
    if info['password'] != request.form['pass_con']:
        valid = False
        flash('Error: Passwords do not match.')
    if not re.match('[A-Za-z-]', info['first_name']):
            flash('First name must only contain letters.')
            valid = False
    if not re.match('[A-Za-z-]', info['last_name']):
            flash('Last name must only contain letters.')
            valid = False
    if valid == False:
        return redirect('/register')
    elif valid == True:
        hashedpw = bcrypt.hashpw(request.form['password'].encode("utf8"), bcrypt.gensalt())
        data = {
            'first_name': request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email': request.form['email'],
            'password' : hashedpw
        }
        insert_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        mysql.query_db(insert_query, data)
        flash('Registration successful. Log in to The Wall')
        return redirect('/login')

@app.route('/wall')
def the_wall():
    message_pull = mysql.query_db("SELECT messages.id, messages.user_id, messages.message, messages.created_at, users.first_name, users.last_name FROM messages JOIN users ON messages.user_id = users.id")
    comment_pull = mysql.query_db("SELECT comments.id AS comment_id, comments.message_id, comments.comment, comments.created_at, messages.id, messages.message, users.id AS user_id, users.first_name, users.last_name FROM comments JOIN messages ON comments.message_id = messages.id JOIN users ON comments.user_id = users.id")
    return render_template('wall.html', messages = message_pull, comments = comment_pull)

@app.route('/process/post', methods = ['POST'])
def post():
    if len(request.form['post']) < 1:
        flash('Please enter a message.')
        return redirect('/wall')
    else:
        query = 'INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (:id,:message, NOW(), NOW())'
        message_info = {
            'id': session['id'],
            'message': request.form['post']
        }
        mysql.query_db(query,message_info)
        return redirect('/wall')

@app.route('/process/comment', methods = ['POST'])
def comment():
    if len(request.form['comment']) <1:
        flash('Please enter a comment.', 'comment_error')
        return redirect('/wall')
    else:
        query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES(:user_id, :msg_id, :comment, NOW(), NOW())"
        data = {
            'user_id': session['id'],
            'msg_id': request.form['msg_id'],
            'comment': request.form['comment']
        }
        mysql.query_db(query, data)
        return redirect('/wall')

@app.route('/logout')
def logout():
    session.clear()
    flash("You've logged out.")
    return redirect('/')

@app.route('/edit')
def edit():
    data = { 'id': session['id'] }
    query = "SELECT * FROM users WHERE id = :id"
    user = mysql.query_db(query, data)
    return render_template('edit.html', user = user)

@app.route('/process/edit', methods = ['POST'])
def edit_process():
    update = {
        'first_name': str(request.form['first_name']),
        'last_name': str(request.form['last_name']),
        'email': str(request.form['email']),
        'id': session['id']
    }
    fnquery = "UPDATE users SET first_name = :first_name WHERE id = :id"
    lnquery = "UPDATE users SET last_name = :last_name WHERE id = :id"
    emailquery = "UPDATE users SET email = :email WHERE id = :id"
    mysql.query_db(fnquery, update)
    mysql.query_db(lnquery, update)
    mysql.query_db(emailquery,update)
    flash('Your information has been updated. Please log back in to see your changes.')
    return redirect('/wall')

@app.route('/process/delete', methods = ['POST'])
def delete():
    # if request.form['msg_time'] <= 30:
    data = {
        'postid': request.form['messageid']
    }
    commquery = "DELETE FROM comments WHERE message_id = :postid"
    mysql.query_db(commquery, data)
    deletequery = "DELETE FROM messages WHERE id = :postid"
    mysql.query_db(deletequery, data)
    flash("You've successfully deleted the post from viewing.")
    return redirect('/wall')
    # elif request.form['msg_time'] > 30:
    #     flash('Post was made more than 30 minutes ago. Cannot be deleted.')
    #     return redirect('/wall')

@app.route('/process/deletecomm', methods = ['POST'])
def deletecom():
    # now  = str(datetime.now())
    # comment = str(request.form['com_time'])
    # FMT = '%M'
    # elapsed_time = datetime.strptime(now, FMT) - datetime.strptime(comment, FMT)
    # if elapsed_time.minutes <= 30:
    data = {
        'comment_id': request.form['comment_id']
    }
    deletecomquery = "DELETE FROM comments WHERE id = :comment_id"
    mysql.query_db(deletecomquery, data)
    flash("You've successfully deleted the comment from viewing.")
    return redirect('/wall')
    # elif elapsed_time.minutes > 30:
    #     flash('Comment was made more than 30 minutes ago. Cannot be deleted.')
    #     return redirect('/wall')

app.run(debug = True)
