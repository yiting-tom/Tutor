from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from app.config import DevConfig


app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
# login_manager.login_message_category = 'info'

from app.users.routes import user
from app.posts.routes import post
from app.main.routes import main
from app.errors.handlers import errors

app.register_blueprint(user)
app.register_blueprint(post)
app.register_blueprint(main)
app.register_blueprint(errors)

from app.models import user
from app.models import post


def create_app(config_class=DevConfig):

    return app
