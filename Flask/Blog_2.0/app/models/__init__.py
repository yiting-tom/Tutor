from datetime import datetime
from typing import Union, TypeVar, Optional, List, ClassVar
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length, StopValidation

from flask import flash

from app import db, login_manager


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
