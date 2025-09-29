from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import data_required,length,Email,EqualTo,ValidationError
from app.models import User


class Registration_form(FlaskForm):

    username=StringField('Username',validators=[data_required(),length(min=2,max=20)])

    email=StringField('Email',validators=[data_required(),Email()])

    password=PasswordField('Password',validators=[data_required(),length(min=3)])

    confirm_password=PasswordField('Confirm Password',validators=[data_required(),EqualTo('password')])

    submit=SubmitField('Sign Up')


    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Username taken!Please try a diffrent one')
        
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email is already in use!Please try a diffrent email')



class Login_form(FlaskForm):

    email=StringField('Email',validators=[data_required(),Email()])

    password=PasswordField('Password',validators=[data_required()])

    remember=BooleanField('Remember me')

    submit=SubmitField("Login")



class Profile_form(FlaskForm):

    username = StringField('Username',validators=[data_required(),length(min=2,max=20)])

    email = StringField('Email',validators=[data_required(),Email()])

    submit = SubmitField('Update')


    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()

        if user and user != current_user:
            raise ValidationError('Username taken!Please try a diffrent one')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        
        if user and user != current_user:
            raise ValidationError('Email is already in use!Please try a diffrent email')
        

class Request_Reset_Form(FlaskForm):

    email = StringField('Email',validators=[data_required(),Email()])

    submit = SubmitField('Send Link')

    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()

        if not user:
            raise ValidationError('No such account found associated with that email.Please re-check or register a account')
        
class Reset_Password_Form(FlaskForm):

    new_password = PasswordField('New Password',validators=[data_required(),length(min=2,max=60)])

    confirm_password = PasswordField('Confirm Password',validators=[data_required(),EqualTo('new_password')])

    submit = SubmitField('Update Password') 