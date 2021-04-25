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

from .routes import web
from .models import user
