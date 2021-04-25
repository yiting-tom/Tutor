# for forms.
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
# for user password.
from werkzeug.security import generate_password_hash, check_password_hash
# for user login.
from flask_login import UserMixin

from app import db, login


class LoginForm(FlaskForm):
    r"""The Login Form class."""
    username = StringField(
        'Username',
        validators=[
            DataRequired()])

    password = PasswordField(
        'Password',
        validators=[
            DataRequired()]
    )

    remember_me = BooleanField('Remember Me')

    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    r"""The Register Form class."""
    username = StringField(
        label='Username',
        validators=[
            DataRequired()]
    )

    password = PasswordField(
        label='Password',
        validators=[
            DataRequired()]
    )

    password2 = PasswordField(
        label='Repeat Password',
        validators=[
            DataRequired(), EqualTo('password')]
    )

    email = StringField(
        label='Email',
        validators=[
            DataRequired()]
    )

    submit = SubmitField('Register')

    def validate_username(self, username):
        r"""Validate the username is repeated."""
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidateError('Repeated username')

    def validate_email(self, email):
        r"""Validate the email."""
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidateError('Repeated email')


class User(db.Model, UserMixin):
    r"""The user model."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(31), index=True, unique=True)
    email = db.Column(db.String(63), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<User {self.id} {self.username}"

    def set_password(self, password):
        r"""Set the user's password with hashed."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        r"""check the user's password is correct.'"""
        return check_password_hash(self.password_hash, password)

    @staticmethod
    @login.user_loader
    def load_user(uid):
        r"""Load in user."""
        return User.query.get(int(uid))
