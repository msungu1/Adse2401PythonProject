# our site's registration / sign up form

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, RadioField, PasswordField, TelField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
    names = StringField(
        'Full Name',
        validators=[DataRequired(), Length(max=50)],
        render_kw={
            "placeholder": "Enter your full name",
            "title": "Your full legal name",
            "tabindex": 10
        }
    )

    birthdate = DateField(
        'Birthdate',
        format='%Y-%m-%d',
        validators=[DataRequired()],
        render_kw={
            "placeholder": "YYYY-MM-DD",
            "title": "Enter your date of birth",
            "tabindex": 20
        }
    )

    gender = RadioField(
        'Gender',
        choices=[('male', 'Male'), ('female', 'Female')],
        validators=[DataRequired()],
        render_kw={
            "title": "Select your gender",
            "tabindex": 30
        }
    )

    phone = TelField(
        'Phone Number',
        validators=[DataRequired(), Length(min=10, max=15)],
        render_kw={
            "placeholder": "+254700123456",
            "title": "Enter your phone number",
            "tabindex": 40
        }
    )

    email = EmailField(
        'Email Address',
        validators=[DataRequired(), Email()],
        render_kw={
            "placeholder": "example@domain.com",
            "title": "Enter a valid email address",
            "tabindex": 50
        }
    )

    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=6, message="Password must be at least 6 characters long")],
        render_kw={
            "placeholder": "Enter password",
            "title": "Choose a strong password",
            "tabindex": 60
        }
    )

    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password', message="Passwords must match")],
        render_kw={
            "placeholder": "Re-enter password",
            "title": "Confirm your password",
            "tabindex": 70
        }
    )

    submit = SubmitField(
        'Register',
        render_kw={
            "class": "btn btn-primary",
            "title": "Click to submit your registration",
            "tabindex": 80
        }
    )

         reset = SubmitField(
            label='Reset',
             render_kw={
             "title": "clear",
             "tabindex": 90,})