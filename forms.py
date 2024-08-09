#importing the flask wtForms
from flask_wtf import FlaskForm
#importing the string feild,password feild ,Submit feild,BooleanFeild
from wtforms import StringFeild,PasswordFeild,SubmitFeild,BooleanFeild
#importing the form validators it is used to validate some parameters like length of the some string like username or email  and equalto
from wtforms.validators import DataRequired,Length,Email,EqualTo


class RegestrationForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)] )
	email=StringField('Email',validators=[DataRequired(),Email()])
	password =PasswordFeild('Password',validators=[DataRequired()])
	confirm_password =PasswordFeild('Confirm Password',validators=[DataRequired(),EqualTo('password')])
	submit=SubmitFeild('Sign Up')


class LoginForm(FlaskForm):
        email=StringField('Email',validators=[DataRequired(),Email()])
        password =PasswordFeild('Password',validators=[DataRequired()])
	remember=BooleanFeild('Remember Me ')
        submit=SubmitFeild('LogIn ')
