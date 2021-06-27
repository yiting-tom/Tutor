from flask import render_template, request, Blueprint, flash, redirect, url_for
from flask_login import current_user, logout_user

from app import db
from app.models.user import User, RegisterForm, LoginForm
from app.models.post import Post

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
@main.route('/index')
@main.route('/home')
def index():
    posts = Post.get_spc_posts(limit=5)

    return render_template('main_pages/index.html', posts=posts)


@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash('Registered already.')
        return redirect(url_for('main.index'))

    # Registration.
    form = RegisterForm()

    if form.validate_on_submit():       # insert into db.
        User(form, add_to_db=True)
        flash('Registration successful!')
        return redirect(url_for('main.login'))

    return render_template('main_pages/register.html', title='Registration', form=form)


@main.route('/login', methods=['GET', 'POST'])
def login():
    # Login already.
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    # Login.
    form = LoginForm()
    # Correct form format.
    if form.validate_on_submit():

        # User login.
        if not User.login(form):
            flash('Invalid username or password.')
            return redirect(url_for('main.login'))

        return redirect(url_for('main.index'))

    return render_template('main_pages/login.html', title='Log In', form=form)


@main.route('/logout')
def logout():
    logout_user()
    flash('Log out successful!')
    return redirect(url_for('main.index'))
