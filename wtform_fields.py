from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError

from passlib.hash import pbkdf2_sha256
#from models import User

'''
def invalid_credentials(form, field):
    """ Username and password checker """

    password = field.data
    username = form.username.data

    # Check username is invalid
    user_data = User.query.filter_by(username=username).first()
    if user_data is None:
        raise ValidationError("Username or password is incorrect")

    # Check password in invalid
    elif not pbkdf2_sha256.verify(password, user_data.hashed_pswd):
        raise ValidationError("Username or password is incorrect")
'''

class RegistrationForm(FlaskForm):
    """ Registration form"""

    username = StringField('username', validators=[InputRequired(message="Username required"), Length(min=4, max=25, message="Username must be between 4 and 25 characters")])
    password = PasswordField('password', validators=[InputRequired(message="Password required"), Length(min=4, max=25, message="Password must be between 4 and 25 characters")])
    confirm_pswd = PasswordField('confirm_pswd', validators=[InputRequired(message="Password required"), EqualTo('password', message="Passwords must match")])
    name = StringField('name', validators=[InputRequired(message="Name required")])
    age = StringField('age')
    cooking_skill = RadioField('cooking_skill', choices=[("none", "No experience"), ("beginner", "Beginner"), ("intermediate", "Intermediate"), ("advanced", "Advanced"), ("expert", "Expert")])
    vegetarian = RadioField('vegetarian', choices=[("veg", "Yes"), ("no-veg", "No")])
    sec_question = PasswordField('sec_question', validators=[InputRequired(message="Answer to security questions required")])

    '''
    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already exists. Select a different username.")
    '''


class LoginForm(FlaskForm):
    """ Login form """

    username = StringField('username', validators=[InputRequired(message="Username required")])
    # add back invalid credentials to password later
    password = PasswordField('password', validators=[InputRequired(message="Password required")])