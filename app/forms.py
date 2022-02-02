# Forms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, DataRequired
class LoginForm(FlaskForm):
    #field name = DatatypeField('LABEL', validators=[LIST OF validators])
    email = StringField('Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
