from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,EmailField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flasktutorial.models import User

# print(dir(wtforms))
# print(help(wtforms.PasswordField))
# print(type(FlaskForm))









