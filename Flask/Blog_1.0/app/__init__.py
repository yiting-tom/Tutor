from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from .configs import DevConfig

app = Flask(__name__)

# Load the configurations.
app.config.from_object(DevConfig)
# DB
db = SQLAlchemy(app)
# Migration
migrate = Migrate(app, db)
# User Login
login = LoginManager(app)
login.login_view = 'login'

from .routes import webs, errors
from .models import user

# TODO: split to home_pages, user_pages, posts_pages

# version: x.y.z
# 1.1.100 -> static
# x -> huge
# y -> function
# z -> debug
