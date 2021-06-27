from flask_wtf import FlaskForm
from typing import Union, TypeVar, Optional, List, ClassVar

from app import db

Post = TypeVar('Post')
User = TypeVar('User')
NewPostForm = TypeVar('NewPostForm')
UpdatePostForm = TypeVar('UpdatePostForm')


# table
class Post(db.Model):
    # column
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    # date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, form: NewPostForm, user: User, **kwargs):
        self.title = form.title.data
        self.content = form.content.data
        self.user_id = user.id

        if kwargs.get('add_to_db'):
            db.session.add(self)
            db.session.commit()

    def __repr__(self):
        return f"Post('{self.title}', '{self.author}')"

    def update(self, form: UpdatePostForm):
        self.title = form.title.data
        self.content = form.content.data
        db.session.commit()

    @staticmethod
    def get_spc_posts(**kwargs) -> list[Post]:
        """Get posts in specific way.

        Parameters
        ==========
        **limit : int
            The limitation of posts.

        Return
        ======
        list[Post]
            The target posts.
        """
        return Post.query.limit(kwargs.pop('limit', 5))