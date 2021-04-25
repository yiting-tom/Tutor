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
        # User login.
        try:
            User.login(form)
        except ValueError as error:
            flash(error)

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