from datetime import datetime
from typing import Union, TypeVar, Optional, List, ClassVar

from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length, StopValidation
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, current_user
from hashlib import md5
from app import db, login

User = TypeVar('User')
LoginForm = TypeVar('LoginForm')
RegisterForm = TypeVar('RegisterForm')
EditProfileForm = TypeVar('EditProfileForm')

Post = TypeVar('Post')
NewPostForm = TypeVar('NewPostForm')
EditPostForm = TypeVar('EditPostForm')


class Unique(object):
    r"""Check if column value of Form objects is unique.

    Parameters
    ==========
    model : db.Model
        The model class.
    column : db.Column
        The column object in model class.
    message : Optional[str] = None
        The message for prompting the user for repeated value.
        (default: name of column object)
    """
    def __init__(self, model: db.Model, column: db.Column, message: Optional[str] = None):
        self.model = model
        self.column = column
        self.message = message if message else r"Repeated " + column.name

    def __call__(self, form, field):
        if self.model.query.filter(self.column == field.data).first():
            raise StopValidation(self.message)
#
#
# def get_obj(cls: ClassVar, oid: int):
#     return cls.query.get(int(oid))
