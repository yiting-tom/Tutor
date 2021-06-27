from app.models.__init__ import *


class Post(db.Model):
    r"""The post model."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(31), unique=True)
    body = db.Column(db.String(1023))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, form: FlaskForm, **kwargs):
        self.title = form.title.data
        self.body = form.body.data
        self.user_id = current_user.id

        if kwargs.get('add_to_db'):
            db.session.add(self)
            db.session.commit()

    def __repr__(self):
        return f'<Post {self.id} {self.user_id}>'

    def update(self, form: EditPostForm):
        r"""Update post information in db."""
        self.title = form.title.data
        self.body = form.body.data
        self.timestamp = datetime.utcnow()
        db.session.commit()

    @staticmethod
    def get_posts(uid: int):
        return Post.query.filter_by(user_id=uid).all()


class NewPostForm(FlaskForm):
    r"""For create a new post form model."""
    title = StringField(
        label='Title',
        validators=[
            DataRequired(), Unique(Post, Post.title), Length(3)
        ]
    )

    body = StringField(
        label='Body',
        validators=[
            DataRequired(), Length(3, 1024)
        ]
    )

    submit = SubmitField('Post!')


class EditPostForm(FlaskForm):
    title = StringField(
        label='New Title',
        validators=[
            DataRequired(), Unique(Post, Post.title), Length(3)
        ]
    )

    body = StringField(
        label='New Body',
        validators=[
            DataRequired(), Length(3, 1024)
        ]
    )

    submit = SubmitField('Update!')


# Goal
# do not import. (V)
