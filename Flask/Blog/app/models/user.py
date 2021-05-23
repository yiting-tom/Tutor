from app.models.__init__ import *
from app.models.post import Post


followers = db.Table(
    'followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(db.Model, UserMixin):
    r"""The user model."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(31), index=True, unique=True)
    email = db.Column(db.String(63), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    sex = db.Column(db.Numeric(4))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    about_me = db.Column(db.String(255))

    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

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

    def avatar(self, size: Optional[int] = 36):
        r"""The user avatar."""
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s{size}'

    def update_profile(self, form: EditProfileForm):
        self.username = form.username.data
        self.about_me = form.about_me.data
        db.session.commit()

    def is_following(self, user: User):
        return self.followd.filter(followers.c.followed_id == user.id).count() > 0

    def follow(self, user: User):
        if not self.is_following(user):
            self.followed.append(user)

    def unfollow(self, user: User):
        if self.is_following(user):
            self.followed.remove(user)

    def followed_posts(self):
        followed = Post.query.join(
            followers,
            (followers.c.followed_id == Post.user_id)
        ).filter(followers.c.follower_id == self.id)

        own = Post.query.filter_by(user_id=self.id)

        return own

    @staticmethod
    def get_user(form: LoginForm) -> Optional[User]:
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
    def login(form: LoginForm) -> Optional[User]:
        user = User.get_user(form)

        if user is None or not user.check_password(form):
            return None

        return login_user(user, remember=form.remember_me.data)


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
