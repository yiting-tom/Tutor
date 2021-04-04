r"""The routes to web."""
import sys
from __init__ import *
from models import User


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        if not(User.in_db(request.form)):
            new_user = User.insert(request.form)
            print(new_user, file=sys.stderr)

    return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('home.html')