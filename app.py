from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

from md.cl.forms import RegisterForm
from md._db.insert import Insert

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
        #name = form.name.data
        #email = form.email.data
        #username = form.username.data
        #password = form.password.data

        #pwd = password.encode('utf-8')
        #hashed = bcrypt.hashpw(pwd, bcrypt.gensalt())
        #passw = hashed.decode(encoding='utf-8')

        Insert.user(form.name.data, form.email.data, form.username.data, form.password.data)

        flash('You are now registered and can log in', 'success')

        return redirect(url_for(''))
    return render_template('register.jinja2', form=form)

if __name__ == '__main__':
    app.run()
    app.secret_key = 'secret123'
