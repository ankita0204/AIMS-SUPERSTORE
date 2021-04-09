"""
Created on Wed Mar 31 22:50:02 2021

@author: Ankita Dasgupta
"""

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__)


app.secret_key = '0204'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0204'
app.config['MYSQL_DB'] = 'aimslogin'

mysql = MySQL(app)

@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = % s AND password = % s', (email, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            return render_template('inventory.html')
        else:
            msg = 'Incorrect Email / password !' 
    return render_template('login.html', msg = msg)

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'first_name' in request.form and 'last_name' in request.form and 'phone' in request.form and 'address' in request.form:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif len(phone)!=10 or not phone.isdecimal():
            msg = 'Invalid phone number !'
        elif not first_name.isalpha():
            msg = 'Name must only contain alphabets !'
        elif not last_name.isalpha():
            msg = 'Name must only contain alphabets !'
        elif not first_name or not last_name or not phone or not password or not email:
            msg = 'Please fill out the form !'
        elif len(password) < 4:
            msg = 'Password should have at least 4 characters'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s, % s, %s, %s)', (first_name, last_name, phone, email, address, password, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

@app.route('/update', methods =['GET', 'POST'])
def update():
    if session:
        msg = ''
        if request.method == 'POST' and 'first_name' in request.form and 'last_name' in request.form and 'phone' in request.form and 'address' in request.form:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            phone = request.form['phone']
            address = request.form['address']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM accounts WHERE email = % s', (session['email'],))
            account = cursor.fetchone()
            if first_name:
                if not first_name.isalpha():
                    msg = 'Name must only contain alphabets !'
                else:
                    cursor.execute('Update accounts SET first_name = % s WHERE email = % s', (first_name, account['email']))
                    mysql.connection.commit()
                    msg = 'Your account has been updated!'
            if last_name:
                if not last_name.isalpha():
                    msg = 'Name must only contain alphabets !'
                else:
                    cursor.execute('Update accounts SET last_name = % s WHERE email = % s', (last_name, account['email']))
                    mysql.connection.commit()
                    msg = 'Your account has been updated!'
            if phone:
                if len(phone) != 10 or not phone.isdecimal():
                    msg = 'Invalid phone number !'
                else:
                    cursor.execute('Update accounts SET phone = % s WHERE email = % s', (phone, account['email']))
                    mysql.connection.commit()
                    msg = 'Your account has been updated!'
            if address:
                cursor.execute('Update accounts SET address = % s WHERE email = % s', (address, account['email']))
                mysql.connection.commit()
                msg = 'Your account has been updated!'
            if not first_name and not last_name and not address and not phone:
                msg = 'No Update!'
    return render_template('update.html', msg = msg)

@app.route('/home')
def home():
    if session:
        return render_template('home.html')

@app.route('/inventory')
def inventory():
    if session:
        return render_template('inventory.html')
    
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    return redirect(url_for('login'))