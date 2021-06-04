r"""Configurations file"""
import os
from pathlib import Path


BASE_DIR = Path(__file__).cwd()


class DevConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default_secret_key'
    DEBUG = True

    # DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = \
        os.environ.get('DATABASE_URL') \
        or 'sqlite:///' + str(BASE_DIR / 'dev_db.sqlite')
