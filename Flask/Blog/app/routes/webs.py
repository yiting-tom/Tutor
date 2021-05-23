from datetime import datetime
from typing import List

from flask import render_template, redirect, flash, url_for, request
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app import app, login, db
from app.models.user import LoginForm, RegisterForm, User, EditProfileForm
from app.models.post import Post, NewPostForm, EditPostForm


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    posts = Post.query.all()
    form = NewPostForm()

    if form.validate_on_submit():
        Post(form, add_to_db=True)
        flash('Posted successfully!')
        return redirect(url_for('index'))

    return render_template("index.html", title='Home Page', posts=posts, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login already.
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # Login.
    form = LoginForm()
    # Correct form format.
    if form.validate_on_submit():

        # User login.
        if not User.login(form):
            flash('Invalid username or password.')
            return redirect(url_for('login'))

        # Get next page.
        next_page = request.args.get('next')

        if not next_page\
                or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # Registration.
    form = RegisterForm()

    if form.validate_on_submit():       # insert into db.
        User(form, add_to_db=True)      # implement a new user.
        flash('Registration successful!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Registration', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user_: User = User.query.filter_by(username=username).first_or_404()
    posts_: List[Post] = Post.get_posts(user_)
    # print(user_.followed_posts()[0])

    return render_template('user.html', user=user_, posts=posts_)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm()

    if form.validate_on_submit():
        current_user.update_profile(form)
        flash("Your have changed your profile.")
        return redirect(f"user/{form.username.data}")

    if request.method == 'get':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me

    return render_template('edit_profile.html', title='Edit Profile', form=form)


@app.route('/edit_post/<int:pid>', methods=['GET', 'POST'])
def edit_post(pid):
    form = EditPostForm()

    if form.validate_on_submit():
        # Query: search from db.
        post = Post.query.filter_by(id=pid).first()

        if post.user_id != current_user.id:
            flash("Your don't have authority to edit this post.")
            return redirect(url_for('index'))

        post.update(form)

        # update completed.
        flash("Your have updated your post.")
        return redirect(url_for("index"))

    return render_template('edit_post.html', title='Edit Post', form=form)
