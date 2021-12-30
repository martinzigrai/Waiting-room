from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

from md.cl.forms import RegisterForm
from md._db.insert import Insert
from md._db.select import Select
from md.cl.verify import *
from md.cl.user import *


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.jinja2')

@app.route('/about')
def about():
    return render_template('about.jinja2')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():

        hashed = bcrypt.hashpw((form.password.data).encode('utf-8'), bcrypt.gensalt())

        new_user = User(None, form.name.data, form.email.data, form.username.data, hashed.decode(encoding='utf-8'))

        Insert.user(new_user)

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('register'))
    return render_template('register.jinja2', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        my_list = Select.users()
        user_names = my_list.getUserNames()
        username = request.form['username']
        password_candidate = request.form['password']

        if username in user_names:
            my_user = my_list.getUser(username)
            password = my_user.password

        #query = ' SELECT * FROM public.user WHERE username = %s;'
        #val = ([username])

        #result = cursor.execute(query, val)
        #result = cursor.execute(' SELECT * FROM public.user WHERE username = %s;', [username])
            #data = cursor.fetchone()
            #password = data['password']

            if bcrypt.checkpw(password_candidate.encode('utf-8'), password.encode('utf-8')):
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.jinja2', error=error)
            #con.close()
        else:
            error = 'Username not found'
            return render_template('login.jinja2', error=error)

    return render_template('login.jinja2')

@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

@app.route('/dashboard')
@is_logged_in
def dashboard():
    return render_template('dashboard.jinja2')

if __name__ == '__main__':
    app.secret_key='root'
    app.run()
