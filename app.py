from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import bcrypt
from flask_mysqldb import MySQL #treba to premenit na POSTGRESQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

from md.cl.forms import RegisterForm

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
        return True
    return render_template('register.jinja2', form=form)

if __name__ == '__main__':
    app.run()
