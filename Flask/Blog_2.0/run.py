r"""run file (master app)"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from configs import DevConfig

app = Flask(__name__)

# DB
db = SQLAlchemy(app)
# Migration
migrate = Migrate(app, db)
# Configuration setup.
app.config.from_object(DevConfig)

# TODO: login module bind.


def main():
    from app.home_pages import home
    app.register_blueprint(home)

    app.run()


if __name__ == '__main__':
    main()
