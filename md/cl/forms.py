from wtforms import Form, StringField, TextAreaField, PasswordField, validators

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=1, max=25)])
    surname = StringField('Surname', [validators.Length(min=1, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

class RecordForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=1, max=25)])
    surname = StringField('Email', [validators.Length(min=1, max=50)])

class InjectionForm(Form):
    injection = StringField('Injection', [validators.Length(min=1, max=100)])
