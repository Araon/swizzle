from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email,length


class RegistrationForm(FlaskForm):
    '''
    This class is responsible for handling the registration data and making the registration page

    '''

    username = StringField('Username',validators=[DataRequired(), length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=2)])

    submit = SubmitField('Sign Up')


    
class LoginForm(FlaskForm):
    '''
    This class is responsible for handling the login data and making the login page

    '''

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), length(min=2)])
    submit = SubmitField('Login')

