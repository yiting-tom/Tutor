# for forms.
from typing import Union
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
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

    sex = SelectField(
        label='Sex',
        choices=[(0, 'Female'), (1, 'Male'), (2, 'Others')],
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
    sex = db.Column(db.Numeric(4))

    def __init__(self, form: LoginForm, **kwargs):
        self.username = form.username.data
        self.email = form.email.data
        self.sex = form.sex.data
        self.password_hash = generate_password_hash(form.password.data)

        if kwargs.get('add_to_db'):
            db.session.add(self)
            db.session.commit()

    def __repr__(self):
        return f"<User {self.id} {self.username}"

    def check_password(self, args: Union[str, LoginForm]) -> bool:
        r"""check the user's password is correct.'"""
        password = args
        if isinstance(args, LoginForm):
            password = args.password.data
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_user_by_form(form: LoginForm) -> bool:
        r"""Check user can login."""
        return User.query.filter_by(
            username=form.username.data,
        ).first()

    @staticmethod
    @login.user_loader
    def load_user(uid):
        r"""Load in user."""
        return User.query.get(int(uid))

    @staticmethod
    def login(form: LoginForm) -> User:
        user = User.get_user_by_form(form)

        if user is None or not user.check_password(form):
            raise ValueError('Invalid username or password.')

        login_user(user, remember=form.remember_me.data)
        return user

