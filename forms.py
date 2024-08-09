#importing the flask wtForms
from flask_wtf import FlaskForm
#importing the string feild 
from wtforms import StringFeild
#importing the form validators it is used to validate some parameters like length of the some string like username 
from wtforms.validators import DataRequired,Length 
class RegestrationForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)] )
