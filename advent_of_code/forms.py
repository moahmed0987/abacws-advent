from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Length
from advent_of_code.models import User

class RegistrationForm(FlaskForm):
    username_new = StringField("Username", validators=[DataRequired(), Length(5, 20, message="Username must be between 5 and 20 characters long. Try again.")])
    email_address_new = StringField("Email Address", validators=[DataRequired()])
    password_new = PasswordField("Password", validators=[DataRequired(), Length(8, 32, message="Password must be between 8 and 32 characters long. Try again."), EqualTo("password_confirm", message="Passwords do not match. Try again.")])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(), Length(5, 20, message="Password must be between 5 and 20 characters long. Try again.")])
    submit = SubmitField("Register")

    def validate_username_new(self, username_new):
        user = User.query.filter_by(username=username_new.data).first()
        if user is not None:
            raise ValidationError("Username already exists. Please choose a different one.")
    
    def validate_email_address_new(self, email_address_new):
        user = User.query.filter_by(email_address=email_address_new.data).first()
        if user is not None:
            raise ValidationError("Email address is taken. Please choose a different one.")
        if "@" not in email_address_new.data:
            raise ValidationError("Email address is invalid. Please try again.")
        elif "@cardiff.ac.uk" not in email_address_new.data.lower():
            raise ValidationError("Email address is invalid. You must use a Cardiff University email address. Please try again.")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is None:
            raise ValidationError("Username not found. Please try again.")
    
    def validate_password(self, password):
        user = User.query.filter_by(username=self.username.data).first()
        if user is not None:
            if not user.verify_password(password.data):
                raise ValidationError("Incorrect password. Please try again.")

class PuzzleForm(FlaskForm):
    answer = StringField("Answer", validators=[DataRequired()])
    submit = SubmitField("Submit")