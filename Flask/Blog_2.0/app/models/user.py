from hashlib import md5
from datetime import datetime
from flask import current_app
from flask_wtf import FlaskForm
from flask_login import UserMixin, login_user, current_user
from typing import Union, TypeVar, Optional, List, ClassVar
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length, StopValidation
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager
from app.models.post import Post
from app.models import Unique


User = TypeVar('User')
LoginForm = TypeVar('LoginForm')
RegisterForm = TypeVar('RegisterForm')
EditProfileForm = TypeVar('EditProfileForm')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    sex = db.Column(db.Numeric(4))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    about_me = db.Column(db.String(255))

    # DB ....
    posts = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, form: RegisterForm, **kwargs):
        self.username = form.username.data
        self.email = form.email.data
        self.sex = form.sex.data
        self.password_hash = generate_password_hash(form.password.data)

        if kwargs.get('add_to_db'):
            db.session.add(self)
            db.session.commit()

    def check_password(self, args: Union[str, LoginForm]) -> bool:
        r"""check the user's password is correct.'"""
        password = args
        if isinstance(args, LoginForm):
            password = args.password.data
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_user(form: LoginForm) -> Optional[User]:
        r"""Check user can login."""
        return User.query.filter_by(
            username=form.username.data,
        ).first()

    @staticmethod
    def login(form: LoginForm) -> Optional[User]:
        user = User.get_user(form)

        if user is None or not user.check_password(form):
            return None

        return login_user(user, remember=form.remember_me.data)

    def avatar(self, size: Optional[int] = 36):
        r"""The user avatar."""
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s{size}'

    def update_profile(self, form: EditProfileForm):
        self.username = form.username.data
        self.about_me = form.about_me.data
        db.session.commit()

    # def get_reset_token(self, expires_sec=1800):
    #     s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
    #     return s.dumps({'user_id': self.id}).decode('utf-8')

    # @staticmethod
    # def verify_reset_token(token):
    #     s = Serializer(current_app.config['SECRET_KEY'])
    #     try:
    #         user_id = s.loads(token)['user_id']
    #     except:
    #         return None
    #     return User.query.get(user_id)

    # def __repr__(self):
    #     return f"User('{self.username}', '{self.email}', '{self.image_file}')"


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
            DataRequired(), Unique(User, User.username)]
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
            DataRequired(), Unique(User, User.email)]
    )

    sex = SelectField(
        label='Sex',
        choices=[(0, 'Female'), (1, 'Male'), (2, 'Others')],
        validators=[
            DataRequired()]
    )

    submit = SubmitField('Register')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')
