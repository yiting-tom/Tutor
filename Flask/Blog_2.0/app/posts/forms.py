from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length, StopValidation

from app.models import Unique
from app.models.post import Post


class NewPostForm(FlaskForm):
    r"""For create a new post form model."""
    title = StringField(
        label='Title',
        validators=[
            DataRequired(), Unique(Post, Post.title), Length(3)
        ]
    )

    content = TextAreaField(
        label='Content',
        validators=[
            DataRequired(), Length(3, 1024)
        ]
    )

    submit = SubmitField('Post!')


class UpdatePostForm(FlaskForm):
    r"""For create a new post form model."""
    title = StringField(
        label='Title',
        validators=[
            DataRequired(), Unique(Post, Post.title), Length(3)
        ]
    )

    content = TextAreaField(
        label='Content',
        validators=[
            DataRequired(), Length(3, 1024)
        ]
    )

    submit = SubmitField('Post!')
