from flask import render_template, redirect, flash, url_for, request
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.urls import url_parse

from app import app, login, db
from app.models.user import LoginForm, RegisterForm, User
from app.models.post import Post


@app.route('/')
@login_required
def index():
    if current_user.is_authenticated:
        posts = Post.query.filter_by(user_id=current_user.id).all()
    return render_template("index.html", title='Home Page', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Login already.
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # Login.
    form = LoginForm()
    # Correct form format.
    if form.validate_on_submit():
        # Get user from DB.
        user = User.query.filter_by(username=form.username.data).first()
        # Login Failed.
        if user is None\
                or user.check_password(form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        # Login.
        login_user(user, remember=form.remember_me.data)
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
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Registration', form=form)