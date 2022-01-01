from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

from md.cl.forms import RegisterForm
from md.cl.forms import RecordForm
from md._db.insert import Insert
from md._db.select import Select
from md._db.update import Update
from md._db.delete import Delete
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

            if bcrypt.checkpw(password_candidate.encode('utf-8'), password.encode('utf-8')):
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('table'))
            else:
                error = 'Invalid login'
                return render_template('login.jinja2', error=error)
        else:
            error = 'Username not found'
            return render_template('login.jinja2', error=error)

    return render_template('login.jinja2')

@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

@app.route('/add_record', methods=['GET', 'POST'])
@is_logged_in
def add_record():
    form = RecordForm(request.form)
    if request.method == 'POST' and form.validate():
        new_user = User(None, form.name.data, form.email.data, form.username.data, None)

        Insert.user(new_user)

        flash('Record Created', 'success')

        return redirect(url_for('table'))

    return render_template('add_record.jinja2', form=form)

@app.route('/edit_record/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_record(id):
    record = Select.record_by_id(id)

    form = RecordForm(request.form)

    form.name.data = record.name
    form.email.data = record.email
    form.username.data = record.username

    if request.method == 'POST' and form.validate():
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']

        new_user = User(None, name, email, username, None)

        app.logger.info(username)
        Update.record_update(new_user, id)

        flash('Record Updated', 'success')

        return redirect(url_for('table'))

    return render_template('edit_record.jinja2', form=form)

@app.route('/delete_record/<string:id>', methods=['POST'])
@is_logged_in
def delete_record(id):

    Delete.record_from_table(id)

    flash('Record Deleted', 'success')

    return redirect(url_for('table'))


@app.route('/table')
@is_logged_in
def table():
    uzivatelia = Select.users()
    my_list = uzivatelia.getUsersInfo()
    my_list.reverse()
    if len(my_list) > 0:
        return render_template('table.jinja2', my_list=my_list)
    else:
        msg = 'No Data Found'
        return render_template('table.jinja2', msg=msg)

if __name__ == '__main__':
    #aplikaciu spustime pomocou prikazu python app.py
    app.secret_key='root'
    app.run(host='0.0.0.0', port = 5000)
